### extends 'class_empty.py'
### block ClassImports
# NOTICE: Do not edit anything here, it is generated code
from . import gxapi_cy
from geosoft.gxapi import GXContext, float_ref, int_ref, str_ref
from .GXE3DV import GXE3DV
from .GXMAP import GXMAP


### endblock ClassImports

### block Header
# NOTICE: The code generator will not replace the code in this block
### endblock Header

### block ClassImplementation
# NOTICE: Do not edit anything here, it is generated code
class GXEMAP(gxapi_cy.WrapEMAP):
    """
    GXEMAP class.

    The `GXEMAP <geosoft.gxapi.GXEMAP>` class provides access to a map as displayed within
    Oasis montaj, but (usually) does not change data within the map itself.
    It performs functions such as setting the currently displayed area,
    or drawing "tracking" lines or boxes on the map (which are not
    part of the map itself).

    **Note:**

    To obtain access to the map itself, it is recommended practice
    to begin with an `GXEMAP <geosoft.gxapi.GXEMAP>` object, and use the `lock <geosoft.gxapi.GXEMAP.lock>` function to
    lock the underlying map to prevent external changes. The returned
    `GXMAP <geosoft.gxapi.GXMAP>` object (see `GXMAP <geosoft.gxapi.GXMAP>`) may then be safely used to make changes to the map itself.

    `GXMAP <geosoft.gxapi.GXMAP>` Redraw Rules:

        1. Redraws only occur at the end of the proccess (GX or SCRIPT) not during.
           You can safely call other GX's and the map will not redraw. If you need the
           map to redraw immediately use `redraw <geosoft.gxapi.GXEMAP.redraw>` instead.
        2. If the final GX calls `GXSYS.cancel_ <geosoft.gxapi.GXSYS.cancel_>`, the map redraw is not done. If you
           need to force a redraw when the user hits cancel use the `redraw <geosoft.gxapi.GXEMAP.redraw>` function.
        3. You can set the redraw flag to `EMAP_REDRAW_YES <geosoft.gxapi.EMAP_REDRAW_YES>` or `EMAP_REDRAW_NO <geosoft.gxapi.EMAP_REDRAW_NO>` at any
            time using `set_redraw_flag <geosoft.gxapi.GXEMAP.set_redraw_flag>`. This flag will only be looked at, when
            the last call to `un_lock <geosoft.gxapi.GXEMAP.un_lock>` occurs and is ignored on a `GXSYS.cancel_ <geosoft.gxapi.GXSYS.cancel_>`.
        4. `redraw <geosoft.gxapi.GXEMAP.redraw>` only works if the current map is not locked. It will do nothing
           if the map is locked.  Issue an `un_lock <geosoft.gxapi.GXEMAP.un_lock>` before using this function.


    VIRTUAL `GXEMAP <geosoft.gxapi.GXEMAP>` SUPPORT

    These methods are only available when running in an external application.
    They allow the GX to open a `GXMAP <geosoft.gxapi.GXMAP>` and then create a Virtual `GXEMAP <geosoft.gxapi.GXEMAP>` from that
    map. The GX can then call `make_current <geosoft.gxapi.GXEMAP.make_current>` and set the current `GXEMAP <geosoft.gxapi.GXEMAP>` so
    that code that follows sees this map as the current `GXMAP <geosoft.gxapi.GXMAP>`.

    Supported methods on Virtual EMAPS are:

        | `current <geosoft.gxapi.GXEMAP.current>`
        | `current_no_activate <geosoft.gxapi.GXEMAP.current_no_activate>`
        | `make_current <geosoft.gxapi.GXEMAP.make_current>`
        | `have_current <geosoft.gxapi.GXEMAP.have_current>`
        | `current_if_exists <geosoft.gxapi.GXEMAP.current_if_exists>`
        | `GXMAP.current <geosoft.gxapi.GXMAP.current>`
        | `lock <geosoft.gxapi.GXEMAP.lock>`
        | `un_lock <geosoft.gxapi.GXEMAP.un_lock>`
        | `is_locked <geosoft.gxapi.GXEMAP.is_locked>`
        | `get_name <geosoft.gxapi.GXEMAP.get_name>`
        | `set_redraw_flag <geosoft.gxapi.GXEMAP.set_redraw_flag>`
        | `redraw <geosoft.gxapi.GXEMAP.redraw>`
        | `loaded <geosoft.gxapi.GXEMAP.loaded>`
        | `load <geosoft.gxapi.GXEMAP.load>`
        | `load_no_activate <geosoft.gxapi.GXEMAP.load_no_activate>`
        | `un_load_verify <geosoft.gxapi.GXEMAP.un_load_verify>`
        | `un_load <geosoft.gxapi.GXEMAP.un_load>`
        | `create_virtual <geosoft.gxapi.GXEMAP.create_virtual>`
    """

    def __init__(self, handle=0):
        super(GXEMAP, self).__init__(GXContext._get_tls_geo(), handle)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of `GXEMAP <geosoft.gxapi.GXEMAP>`
        
        :returns: A null `GXEMAP <geosoft.gxapi.GXEMAP>`
        :rtype:   GXEMAP
        """
        return GXEMAP()

    def is_null(self):
        """
        Check if this is a null (undefined) instance
        
        :returns: True if this is a null (undefined) instance, False otherwise.
        :rtype:   bool
        """
        return self._internal_handle() == 0



# Drag-and-drop methods



    def drop_map_clip_data(self, hglobal):
        """
        Drop Map clipboard data on this `GXEMAP <geosoft.gxapi.GXEMAP>`
        
        :param hglobal:  Handle to Global Clipboard data
        :type  hglobal:  int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.
        """
        self._drop_map_clip_data(hglobal)
        




    def drag_drop_enabled(self):
        """
        Checks if drag-and-drop enabled for the map
        
        :rtype:       bool

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.
        """
        ret_val = self._drag_drop_enabled()
        return ret_val




    def set_drag_drop_enabled(self, enable):
        """
        Set whether drag-and-drop is enabled for the map.
        
        :param enable:  Enables/disables drag-and-drop
        :type  enable:  bool

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.
        """
        self._set_drag_drop_enabled(enable)
        




# Drawing



    def copy_to_clip(self):
        """
        Copy entire map to clipboard.
        

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.

        **Note:** Four objects are placed on the clipboard:

            1. Georefernce Text
            2. Bitmap of current window screen resolution
            3. EMF of current window screen resolution
            4. Entire map as a Geosoft View (go to view mode and hit paste). The coordinates are placed
               in the current view coordinates.
        """
        self._copy_to_clip()
        




    def draw_line(self, min_x, min_y, max_x, max_y):
        """
        Draws a line on the current map.
        
        :param min_x:  X1
        :param min_y:  Y1
        :param max_x:  X2
        :param max_y:  Y2
        :type  min_x:  float
        :type  min_y:  float
        :type  max_x:  float
        :type  max_y:  float

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.

        **Note:** Locations are in the current view user units.

        The line is temporary and will disappear on the next
        screen refresh.  This function is for you to provide
        interactive screen feedback to your user.
        """
        self._draw_line(min_x, min_y, max_x, max_y)
        




    def draw_rect(self, min_x, min_y, max_x, max_y):
        """
        Draws a rect on the current map.
        
        :param min_x:  X1
        :param min_y:  Y1
        :param max_x:  X2
        :param max_y:  Y2
        :type  min_x:  float
        :type  min_y:  float
        :type  max_x:  float
        :type  max_y:  float

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.

        **Note:** Locations are in the current view user units.

        The line is temporary and will disappear on the next
        screen refresh.  This function is for you to provide
        interactive screen feedback to your user.
        """
        self._draw_rect(min_x, min_y, max_x, max_y)
        




    def draw_rect_3d(self, x, y, z, pix):
        """
        Plot a square symbol on a section view.
        
        :param x:     X - True X location
        :param y:     Y - True Y location
        :param z:     Z - True Z location
        :param pix:   Size in pixels ("radius")
        :type  x:     float
        :type  y:     float
        :type  z:     float
        :type  pix:   int

        .. versionadded:: 9.1

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.

        **Note:** Plot a square symbol on a section view, but input 3D user coordinates

        The line is temporary and will disappear on the next
        screen refresh.  This function is for you to provide
        interactive screen feedback to your user.
        """
        self._draw_rect_3d(x, y, z, pix)
        




    def draw_ply(self, polygon):
        """
        Draws a polygon on the current map.
        
        :param polygon:  `GXPLY <geosoft.gxapi.GXPLY>` Object
        :type  polygon:  GXPLY

        .. versionadded:: 9.6

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.

        **Note:** Locations are in the current view user units.

        The polygon is temporary and will disappear on the next
        screen refresh.  This function is for you to provide
        interactive screen feedback to your user.
        """
        self._draw_ply(polygon)
        




    def get_display_area(self, min_x, min_y, max_x, max_y):
        """
        Get the area you are currently looking at.
        
        :param min_x:  X Min returned
        :param min_y:  Y Min returned
        :param max_x:  X Max returned
        :param max_y:  Y Max returned
        :type  min_x:  float_ref
        :type  min_y:  float_ref
        :type  max_x:  float_ref
        :type  max_y:  float_ref

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.

        **Note:** Coordinates are based on the current view units.
        For 3D views this will return the full map extents.
        """
        min_x.value, min_y.value, max_x.value, max_y.value = self._get_display_area(min_x.value, min_y.value, max_x.value, max_y.value)
        




    def get_display_area_raw(self, min_x, min_y, max_x, max_y):
        """
        Get the area you are currently looking at in raw map units
        
        :param min_x:  X Min returned
        :param min_y:  Y Min returned
        :param max_x:  X Max returned
        :param max_y:  Y Max returned
        :type  min_x:  float_ref
        :type  min_y:  float_ref
        :type  max_x:  float_ref
        :type  max_y:  float_ref

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.

        **Note:** Coordinates are in millimeters.
        For 3D views this will return the full map extents.
        """
        min_x.value, min_y.value, max_x.value, max_y.value = self._get_display_area_raw(min_x.value, min_y.value, max_x.value, max_y.value)
        




    def get_map_layout_props(self, snap_to_grid, snap_dist, view_grid, view_rulers, view_units, grid_red, grid_green, grid_blue):
        """
        Get the base layout view properties.
        
        :param snap_to_grid:  Snap to grid
        :param snap_dist:     Snapping distance (always in mm)
        :param view_grid:     View Grid
        :param view_rulers:   View Rulers
        :param view_units:    :ref:`LAYOUT_VIEW_UNITS` View Units
        :param grid_red:      Grid Red Component (0-255)
        :param grid_green:    Grid Green Component (0-255)
        :param grid_blue:     Grid Blue Component (0-255)
        :type  snap_to_grid:  bool_ref
        :type  snap_dist:     float_ref
        :type  view_grid:     int_ref
        :type  view_rulers:   int_ref
        :type  view_units:    int_ref
        :type  grid_red:      int_ref
        :type  grid_green:    int_ref
        :type  grid_blue:     int_ref

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.

        **Note:** This affects the display units and other related properties for the base
        view of a map.
        """
        snap_to_grid.value, snap_dist.value, view_grid.value, view_rulers.value, view_units.value, grid_red.value, grid_green.value, grid_blue.value = self._get_map_layout_props(snap_to_grid.value, snap_dist.value, view_grid.value, view_rulers.value, view_units.value, grid_red.value, grid_green.value, grid_blue.value)
        




    def get_map_snap(self, snap):
        """
        Get current snapping distance in MM
        
        :param snap:  Snap value in MM (returned)
        :type  snap:  float_ref

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.
        """
        snap.value = self._get_map_snap(snap.value)
        




    def get_window_state(self):
        """
        Retrieve the current state of the map window
        

        :returns:     :ref:`EMAP_WINDOW_STATE`
        :rtype:       int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.
        """
        ret_val = self._get_window_state()
        return ret_val




    def set_display_area(self, min_x, min_y, max_x, max_y):
        """
        Set the area you wish to see.
        
        :param min_x:  X Min
        :param min_y:  Y Min
        :param max_x:  X Max
        :param max_y:  Y Max
        :type  min_x:  float
        :type  min_y:  float
        :type  max_x:  float
        :type  max_y:  float

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.

        **Note:** Coordinates are based on the current view user units.
        The map is immediatly redrawn.
        """
        self._set_display_area(min_x, min_y, max_x, max_y)
        




    def set_map_layout_props(self, snap_to_grid, snap_dist, view_grid, view_rulers, view_units, grid_red, grid_green, grid_blue):
        """
        Set the base layout view properties.
        
        :param snap_to_grid:  Snap to grid
        :param snap_dist:     Snapping distance (always in mm)
        :param view_grid:     View Grid
        :param view_rulers:   View Rulers
        :param view_units:    :ref:`LAYOUT_VIEW_UNITS` View Units
        :param grid_red:      Grid Red Component (0-255)
        :param grid_green:    Grid Green Component (0-255)
        :param grid_blue:     Grid Blue Component (0-255)
        :type  snap_to_grid:  bool
        :type  snap_dist:     float
        :type  view_grid:     int
        :type  view_rulers:   int
        :type  view_units:    int
        :type  grid_red:      int
        :type  grid_green:    int
        :type  grid_blue:     int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.

        **Note:** This affects the display units and other related properties for the base
        view of a map.
        """
        self._set_map_layout_props(snap_to_grid, snap_dist, view_grid, view_rulers, view_units, grid_red, grid_green, grid_blue)
        




    def set_map_snap(self, snap):
        """
        Set current snapping distance in MM
        
        :param snap:  Snap value in MM
        :type  snap:  float

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.
        """
        self._set_map_snap(snap)
        




    def set_window_state(self, state):
        """
        Changes the state of the map window
        
        :param state:  :ref:`EMAP_WINDOW_STATE`
        :type  state:  int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.
        """
        self._set_window_state(state)
        




# General



    def packed_files(self):
        """
        The number of packed files in the map.
        

        :returns:     The number of packed files in map.
        :rtype:       int

        .. versionadded:: 9.2

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.
        """
        ret_val = self._packed_files()
        return ret_val




    def activate_group(self, view_group):
        """
        Activates a group and associated tools.
        
        :param view_group:  "View/Group"
        :type  view_group:  str

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.

        **Note:** Activating a group basically enters the edit mode associated
        with the type of group. E.g. a vector group will enable the
        edit toolbar for that gorup and an `GXAGG <geosoft.gxapi.GXAGG>` will bring up the
        image color tool. Be sure to pass a combined name containing
        both the view name and the group separated by a "/" or "\\".
        """
        self._activate_group(view_group.encode())
        




    def activate_view(self, view):
        """
        Activates a view and associated tools.
        
        :param view:  "View"
        :type  view:  str

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.
        """
        self._activate_view(view.encode())
        



    @classmethod
    def current(cls):
        """
        This method returns the Current Edited map.
        

        :returns:    `GXEMAP <geosoft.gxapi.GXEMAP>` Object
        :rtype:      GXEMAP

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.
        """
        ret_val = gxapi_cy.WrapEMAP._current(GXContext._get_tls_geo())
        return GXEMAP(ret_val)



    @classmethod
    def current_no_activate(cls):
        """
        This method returns the Current Edited map.
        

        :returns:    `GXEMAP <geosoft.gxapi.GXEMAP>` Object
        :rtype:      GXEMAP

        .. versionadded:: 9.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.

        **Note:** This function acts just like `current <geosoft.gxapi.GXEMAP.current>` except that the document is not activated (brought to foreground) and no
        guarantee is given about which document is currently active.
        """
        ret_val = gxapi_cy.WrapEMAP._current_no_activate(GXContext._get_tls_geo())
        return GXEMAP(ret_val)



    @classmethod
    def current_if_exists(cls):
        """
        This method returns the Current Edited map.
        

        :returns:    `GXEMAP <geosoft.gxapi.GXEMAP>` Object to current edited map. If there is no current map,
                  the user is not prompted for a map, and 0 is returned.
        :rtype:      GXEMAP

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.
        """
        ret_val = gxapi_cy.WrapEMAP._current_if_exists(GXContext._get_tls_geo())
        return GXEMAP(ret_val)






    def destroy_view(self, unload_flag):
        """
        Removes the view from the workspace.
        
        :param unload_flag:  :ref:`EMAP_REMOVE`
        :type  unload_flag:  int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.

        **Note:** Can only be run in interactive mode. After this call the
        `GXEMAP <geosoft.gxapi.GXEMAP>` object will become invalid. If this is the last view on
        the document and the document has been modified the map will be
        unloaded and optionally saved depending on the :ref:`EMAP_REMOVE`
        parameter.
        """
        self._destroy_view(unload_flag)
        




    def font_lst(self, lst, which):
        """
        List all Windows and geosoft fonts.
        
        :param lst:    List Object
        :param which:  :ref:`EMAP_FONT`
        :type  lst:    GXLST
        :type  which:  int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.

        **Note:** To get TT and GFN fonts, call twice with the same list
        and `EMAP_FONT_TT <geosoft.gxapi.EMAP_FONT_TT>`, then `EMAP_FONT_GFN <geosoft.gxapi.EMAP_FONT_GFN>`, or vice-versa to
        change order of listing.
        """
        self._font_lst(lst, which)
        




    def change_current_view(self, view):
        """
        Change the current working view.
        
        :param view:  View name
        :type  view:  str

        :returns:     0 if view set, 1 if view does not exist.
        :rtype:       int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.

        **Note:** This function operates on the current map.
        Unlike `set_current_view <geosoft.gxapi.GXEMAP.set_current_view>` this function's action
        survive the GX finishing.
        """
        ret_val = self._change_current_view(view.encode())
        return ret_val




    def create_group_snapshot(self, lst):
        """
        Loads an `GXLST <geosoft.gxapi.GXLST>` with the current view/group names
        existing in a map. Typically used to track group
        changes that are about to occur.
        
        :param lst:   `GXLST <geosoft.gxapi.GXLST>` object to fill
        :type  lst:   GXLST

        :returns:     0 if `GXLST <geosoft.gxapi.GXLST>` filled properly
                      1 if not
        :rtype:       int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.
        """
        ret_val = self._create_group_snapshot(lst)
        return ret_val




    def get_3d_view_name(self, name):
        """
        Get the name of a 3D view if the current view is 3D.
        
        :param name:  Name returned
        :type  name:  str_ref

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.
        """
        name.value = self._get_3d_view_name(name.value.encode())
        




    def get_current_group(self, group):
        """
        Get the current group name.
        
        :param group:  Returned group name
        :type  group:  str_ref

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.

        **Note:** This function operates on the current map.
        """
        group.value = self._get_current_group(group.value.encode())
        




    def get_current_view(self, view):
        """
        Get the current view name.
        
        :param view:  Returned view name
        :type  view:  str_ref

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.

        **Note:** This function operates on the current map.
        """
        view.value = self._get_current_view(view.value.encode())
        



    @classmethod
    def get_maps_lst(cls, lst, path):
        """
        Load the file names of open maps into a `GXLST <geosoft.gxapi.GXLST>`.
        
        :param lst:   `GXLST <geosoft.gxapi.GXLST>` to load
        :param path:  :ref:`EMAP_PATH`
        :type  lst:   GXLST
        :type  path:  int

        :returns:     The number of documents loaded into the `GXLST <geosoft.gxapi.GXLST>`.
                      The `GXLST <geosoft.gxapi.GXLST>` is cleared first.
        :rtype:       int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.
        """
        ret_val = gxapi_cy.WrapEMAP._get_maps_lst(GXContext._get_tls_geo(), lst, path)
        return ret_val




    def get_name(self, name):
        """
        Get the name of the map object of this `GXEMAP <geosoft.gxapi.GXEMAP>`.
        
        :param name:  Name returned
        :type  name:  str_ref

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.
        """
        name.value = self._get_name(name.value.encode())
        



    @classmethod
    def have_current(cls):
        """
        This method returns whether a current map is loaded
        

        :returns:    0 - no current map.
                  1 - current map
        :rtype:      int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.
        """
        ret_val = gxapi_cy.WrapEMAP._have_current(GXContext._get_tls_geo())
        return ret_val



    @classmethod
    def i_get_specified_map_name(cls, field, value, name):
        """
        Find a loaded map that has a setting in its reg.
        
        :param field:  `GXREG <geosoft.gxapi.GXREG>` field name
        :param value:  `GXREG <geosoft.gxapi.GXREG>` field value to find
        :param name:   Buffer for map name
        :type  field:  str
        :type  value:  str
        :type  name:   str_ref

        :returns:      0 - Ok
                       1 - No Map Found
        :rtype:        int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.
        """
        ret_val, name.value = gxapi_cy.WrapEMAP._i_get_specified_map_name(GXContext._get_tls_geo(), field.encode(), value.encode(), name.value.encode())
        return ret_val




    def is_grid(self):
        """
        Is the map a grid map?
        

        :returns:     1 - Yes, 0 - No
        :rtype:       int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.
        """
        ret_val = self._is_grid()
        return ret_val



    @classmethod
    def reload_grid(cls, name):
        """
        Reloads a grid document.
        
        :param name:  Source file name
        :type  name:  str

        .. versionadded:: 9.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.

        **Note:** Use this method to reload (if loaded) a grid document if the file on disk changed.
        """
        gxapi_cy.WrapEMAP._reload_grid(GXContext._get_tls_geo(), name.encode())
        




    def is_3d_view(self):
        """
        Is the current view a 3D view.
        

        :returns:     1 - Yes, 0 - No
        :rtype:       int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.
        """
        ret_val = self._is_3d_view()
        return ret_val




    def get_e_3dv(self):
        """
        Get an `GXE3DV <geosoft.gxapi.GXE3DV>` from the `GXEMAP <geosoft.gxapi.GXEMAP>`
        

        :returns:     `GXE3DV <geosoft.gxapi.GXE3DV>` object
        :rtype:       GXE3DV

        .. versionadded:: 9.3

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.
        """
        ret_val = self._get_e_3dv()
        return GXE3DV(ret_val)




    def is_locked(self):
        """
        Checks if map is locked
        
        :rtype:       bool

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.
        """
        ret_val = self._is_locked()
        return ret_val



    @classmethod
    def loaded(cls, name):
        """
        Returns 1 if a map is loaded .
        
        :param name:  Map name
        :type  name:  str

        :returns:     1 if map is loaded, 0 otherwise.
        :rtype:       int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.
        """
        ret_val = gxapi_cy.WrapEMAP._loaded(GXContext._get_tls_geo(), name.encode())
        return ret_val




    def read_only(self):
        """
        Checks if a map is currently opened in a read-only mode.
        
        :rtype:       bool

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
        :param state:        Window state :ref:`EMAP_WINDOW_STATE`
        :param is_floating:  Docked or floating :ref:`EMAP_WINDOW_POSITION`
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
        :param state:        Window state :ref:`EMAP_WINDOW_STATE`
        :param is_floating:  Docked or floating :ref:`EMAP_WINDOW_POSITION`
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
        




    def doubleize_group_snapshot(self, state):
        """
        The `GXLST <geosoft.gxapi.GXLST>` passed in must contain View\\Group strings in
        the Name field only. The function will compare with
        a more current `GXLST <geosoft.gxapi.GXLST>` and zoom the map to the new entry.
        
        :param state:  `GXLST <geosoft.gxapi.GXLST>` object used for comparison
        :type  state:  GXLST

        :returns:      0 if zoom proceeded ok
                       1 if error
        :rtype:        int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.

        **Note:** Typically this function is used in conjunction with
        CreateSnapshot_EMAP.
        """
        ret_val = self._doubleize_group_snapshot(state)
        return ret_val




    def set_current_view(self, view):
        """
        Set the current working view.
        
        :param view:  View name
        :type  view:  str

        :returns:     0 if view set, 1 if view does not exist.
        :rtype:       int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.

        **Note:** This function operates on the current map.
        It changes the view only during the execution of the
        GX. As soon as the GX terminates the view will revert
        to the original one.
        """
        ret_val = self._set_current_view(view.encode())
        return ret_val




    def get_view_ipj(self, view, ipj):
        """
        Get a view's `GXIPJ <geosoft.gxapi.GXIPJ>`.
        
        :param view:  View name
        :param ipj:   `GXIPJ <geosoft.gxapi.GXIPJ>` in which to place the view `GXIPJ <geosoft.gxapi.GXIPJ>`
        :type  view:  str
        :type  ipj:   GXIPJ

        .. versionadded:: 9.1

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.

        **Note:** This function can be used to obtain a views coordinate system 
        without having to call `lock <geosoft.gxapi.GXEMAP.lock>`. This could be an expensive operation
        that cause undesirable UX.
        """
        self._get_view_ipj(view.encode(), ipj)
        



    @classmethod
    def load(cls, name):
        """
        Loads maps into the editor.
        
        :param name:  List of maps (';' or '|' delimited) to load.
        :type  name:  str

        :returns:     `GXEMAP <geosoft.gxapi.GXEMAP>` Object to edited map.
        :rtype:       GXEMAP

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.

        **Note:** The last map in the list will be the current map.

        Maps may already be loaded.

        Only the first file in the list may have a directory path.
        All other files in the list are assumed to be in the same
        directory as the first file.
        """
        ret_val = gxapi_cy.WrapEMAP._load(GXContext._get_tls_geo(), name.encode())
        return GXEMAP(ret_val)



    @classmethod
    def load_no_activate(cls, name):
        """
        Loads documents into the workspace
        
        :param name:  List of documents (';' or '|' delimited) to load.
        :type  name:  str

        :returns:     Handle to current edited document, which will be the last
                      database in the list if multiple files were provided.
        :rtype:       GXEMAP

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.

        **Note:** This function acts just like `load <geosoft.gxapi.GXEMAP.load>` except that the document(s) is not activated (brought to foreground) and no
        guarantee is given about which document is currently active.
        """
        ret_val = gxapi_cy.WrapEMAP._load_no_activate(GXContext._get_tls_geo(), name.encode())
        return GXEMAP(ret_val)



    @classmethod
    def load_with_view(cls, name, p2):
        """
        Load an `GXEMAP <geosoft.gxapi.GXEMAP>` with the view from a current `GXEMAP <geosoft.gxapi.GXEMAP>`.
        
        :param name:  Source Map name
        :param p2:    `GXEMAP <geosoft.gxapi.GXEMAP>` to use as the source view
        :type  name:  str
        :type  p2:    GXEMAP

        :returns:     New `GXEMAP <geosoft.gxapi.GXEMAP>` handle.
        :rtype:       GXEMAP

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.

        **Note:** Can only be run in interactive mode. Is used by
        dbsubset to create a new database with the same
        view as previously.
        """
        ret_val = gxapi_cy.WrapEMAP._load_with_view(GXContext._get_tls_geo(), name.encode(), p2)
        return GXEMAP(ret_val)




    def lock(self):
        """
        This method locks the Edited map.
        

        :returns:     `GXEMAP <geosoft.gxapi.GXEMAP>` Object to map associated with edited map.
        :rtype:       GXMAP

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.

        **Note:** The Redraw flag is set to `EMAP_REDRAW_YES <geosoft.gxapi.EMAP_REDRAW_YES>` when this functions is called.
        """
        ret_val = self._lock()
        return GXMAP(ret_val)




    def make_current(self):
        """
        Makes this `GXEMAP <geosoft.gxapi.GXEMAP>` object the current active object to the user.
        

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.
        """
        self._make_current()
        




    def print_(self, entire_map, scale_to_fit, print_to_file, all_pages, centre, copies, first_page, last_page, scale_factor, overlap_size, offset_x, offset_y, file):
        """
        Print the current map to current printer.
        
        :param entire_map:     lEntireMap  (0 or 1)
        :param scale_to_fit:   lScaleToFit 0 - use scale factor 1 - fit to media 2 - fit to roll media
        :param print_to_file:  lPrintToFile(0 or 1)
        :param all_pages:      lAllPages   (0 or 1)
        :param centre:         lCentre     (0 or 1)
        :param copies:         lCopies
        :param first_page:     lFirstPage
        :param last_page:      lLastPage
        :param scale_factor:   dScaleFactor (2.0 doubles plot size)
        :param overlap_size:   lOverlapSize (mm)
        :param offset_x:       lOffsetX     (mm)
        :param offset_y:       lOffsetY     (mm)
        :param file:           szFile       (if lPrintToFile==1)
        :type  entire_map:     int
        :type  scale_to_fit:   int
        :type  print_to_file:  int
        :type  all_pages:      int
        :type  centre:         int
        :type  copies:         int
        :type  first_page:     int
        :type  last_page:      int
        :type  scale_factor:   float
        :type  overlap_size:   int
        :type  offset_x:       int
        :type  offset_y:       int
        :type  file:           str

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.
        """
        self._print_(entire_map, scale_to_fit, print_to_file, all_pages, centre, copies, first_page, last_page, scale_factor, overlap_size, offset_x, offset_y, file.encode())
        




    def redraw(self):
        """
        Redraw the map immediately.
        

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.

        **Note:** Redraws the map immediately. Map must not be locked.
        """
        self._redraw()
        




    def select_group(self, view_group):
        """
        Select a group.
        
        :param view_group:  "View/Group"
        :type  view_group:  str

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.
        """
        self._select_group(view_group.encode())
        




    def set_redraw_flag(self, redraw):
        """
        Set the redraw flag.
        
        :param redraw:  :ref:`EMAP_REDRAW`
        :type  redraw:  int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.

        **Note:** This function is generally used to prevent redrawing of
        the map, which normally occurs after the last `un_lock <geosoft.gxapi.GXEMAP.un_lock>`
        call, in cases where it is known that no changes are being
        made to the map.

        Typical usage would be to call `lock <geosoft.gxapi.GXEMAP.lock>` followed by
        `set_redraw_flag <geosoft.gxapi.GXEMAP.set_redraw_flag>` (with `EMAP_REDRAW_NO <geosoft.gxapi.EMAP_REDRAW_NO>`) prior
        to querying information from the map. And then end with a call to
        `un_lock <geosoft.gxapi.GXEMAP.un_lock>`.
        """
        self._set_redraw_flag(redraw)
        



    @classmethod
    def un_load(cls, name):
        """
        Unloads a `GXMAP <geosoft.gxapi.GXMAP>`.
        
        :param name:  Name of the map to unload
        :type  name:  str

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.

        **Note:** If the `GXMAP <geosoft.gxapi.GXMAP>` is not loaded, nothing happens.
        Same as `un_load_verify <geosoft.gxapi.GXEMAP.un_load_verify>` with FALSE to prompt save.
        """
        gxapi_cy.WrapEMAP._un_load(GXContext._get_tls_geo(), name.encode())
        



    @classmethod
    def un_load_all(cls):
        """
        Unloads all opened maps
        

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.
        """
        gxapi_cy.WrapEMAP._un_load_all(GXContext._get_tls_geo())
        



    @classmethod
    def un_load_verify(cls, name, prompt):
        """
        Unloads an edited map, optional prompt to save.
        
        :param name:    Name of map to unload
        :param prompt:  Prompt?
        :type  name:    str
        :type  prompt:  bool

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.

        **Note:** If the map is not loaded, nothing happens.
        If "FALSE", map is saved without a prompt.
        """
        gxapi_cy.WrapEMAP._un_load_verify(GXContext._get_tls_geo(), name.encode(), prompt)
        




    def un_lock(self):
        """
        This method unlocks the Edited map.
        

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.
        """
        self._un_lock()
        




# Input



    def get_cur_point(self, x, y):
        """
        Returns the coordinates of the currently selected point in view coordinates
        
        :param x:     X coordinate in current user units.
        :param y:     Y
        :type  x:     float_ref
        :type  y:     float_ref

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.
        """
        x.value, y.value = self._get_cur_point(x.value, y.value)
        




    def get_cur_point_mm(self, x, y):
        """
        Returns the coordinates of the currently selected point in mm on map
        
        :param x:     X coordinate in map mm
        :param y:     Y
        :type  x:     float_ref
        :type  y:     float_ref

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.
        """
        x.value, y.value = self._get_cur_point_mm(x.value, y.value)
        




    def get_cursor(self, x, y):
        """
        Returns the coordinates of the last known cursor location
        
        :param x:     X coordinate in current view user units
        :param y:     Y
        :type  x:     float_ref
        :type  y:     float_ref

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.
        """
        x.value, y.value = self._get_cursor(x.value, y.value)
        




    def get_cursor_mm(self, x, y):
        """
        Returns the coordinates of the last known cursor location in mm on map.
        
        :param x:     X coordinate in map mm
        :param y:     Y
        :type  x:     float_ref
        :type  y:     float_ref

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.
        """
        x.value, y.value = self._get_cursor_mm(x.value, y.value)
        




    def digitize(self, wa, img, digits, prompt, prefix, delim, newline):
        """
        Digitise points from the current map and place in a `GXWA <geosoft.gxapi.GXWA>`.
        
        :param wa:       `GXWA <geosoft.gxapi.GXWA>` in which to write digitized points
        :param img:      `GXIMG <geosoft.gxapi.GXIMG>` for Z value, or `IMG_NULL <geosoft.gxapi.IMG_NULL>` for no Z.
        :param digits:   Number of significant digits to use, 0 for all.
        :param prompt:   Command line prompt string
        :param prefix:   New line prefix string
        :param delim:    Delimiter
        :param newline:  0 for no newline 1 for automatic newline at each point
        :type  wa:       GXWA
        :type  img:      GXIMG
        :type  digits:   int
        :type  prompt:   str
        :type  prefix:   str
        :type  delim:    str
        :type  newline:  int

        :returns:        0 if user digitized some points.
                         1 if user cancelled.
        :rtype:          int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.

        **Note:** The command line will start to recieve digitized points
        from the mouse.  Whenever the left mouse button is
        pressed, the current view X,Y are placed on the workspace
        command line.  If a valid `GXIMG <geosoft.gxapi.GXIMG>` is passed, the Z value is
        also placed on the command line.  If auto-newline is
        specified, the line is immediately placed into `GXWA <geosoft.gxapi.GXWA>`,
        otherwise the user has the oportunity to enter data
        before pressing Enter.

        Locations are in the current view user units
        """
        ret_val = self._digitize(wa, img, digits, prompt.encode(), prefix.encode(), delim.encode(), newline)
        return ret_val




    def digitize2(self, vvx, vvy, vvz, img, prompt, newline):
        """
        Digitise points from the current map and place in VVs.
        
        :param vvx:      Real X `GXVV <geosoft.gxapi.GXVV>`
        :param vvy:      Real Y `GXVV <geosoft.gxapi.GXVV>`
        :param vvz:      Real Z `GXVV <geosoft.gxapi.GXVV>`
        :param img:      `GXIMG <geosoft.gxapi.GXIMG>` for Z value, or `IMG_NULL <geosoft.gxapi.IMG_NULL>` for no Z.
        :param prompt:   Command line prompt string
        :param newline:  0 for no newline 1 for automatic newline at each point
        :type  vvx:      GXVV
        :type  vvy:      GXVV
        :type  vvz:      GXVV
        :type  img:      GXIMG
        :type  prompt:   str
        :type  newline:  int

        :returns:        0 if user digitized some points.
                         1 if user cancelled.
        :rtype:          int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.

        **Note:** The command line will start to recieve digitized points
        from the mouse.  Whenever the left mouse button is
        pressed, the current view X,Y are placed on the workspace
        command line.  If a valid `GXIMG <geosoft.gxapi.GXIMG>` is passed, the Z value is
        also placed on the command line.  If auto-newline is
        specified, the line is immediately placed into the VVs,
        otherwise the user has the oportunity to enter data
        before pressing Enter.

        Locations are in the current view user units
        """
        ret_val = self._digitize2(vvx, vvy, vvz, img, prompt.encode(), newline)
        return ret_val




    def digitize_peaks(self, vvx, vvy, vvz, img, prompt, newline):
        """
        Digitise points from the current map and place in VVs.
        
        :param vvx:      Real X `GXVV <geosoft.gxapi.GXVV>`
        :param vvy:      Real Y `GXVV <geosoft.gxapi.GXVV>`
        :param vvz:      Real Z `GXVV <geosoft.gxapi.GXVV>`
        :param img:      `GXIMG <geosoft.gxapi.GXIMG>` for Z value, or `IMG_NULL <geosoft.gxapi.IMG_NULL>` for no Z.
        :param prompt:   Command line prompt string
        :param newline:  0 for no newline 1 for automatic newline at each point
        :type  vvx:      GXVV
        :type  vvy:      GXVV
        :type  vvz:      GXVV
        :type  img:      GXIMG
        :type  prompt:   str
        :type  newline:  int

        :returns:        0 if user digitized some points.
                         1 if user cancelled.
        :rtype:          int

        .. versionadded:: 9.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.

        **Note:** Same as `digitize2 <geosoft.gxapi.GXEMAP.digitize2>`, but the closest peaks to the selected locations are
        returned instead of the selected location. The method chooses the highest value
        of the 8 surrounding points, the repeats this process until no higher value can
        be found in any of the 8 surrounding points. If there are two or more points with
        a higher value, it will just take the first one and continue, and this method will
        stall on flat areas as well (since no surrounding point is larger).
        """
        ret_val = self._digitize_peaks(vvx, vvy, vvz, img, prompt.encode(), newline)
        return ret_val




    def digitize_polygon(self, vvx, vvy, vvz, img, prompt, newline, pixel_radius):
        """
        Same as iDigitze2_EMAP, but automatically close polygons.
        
        :param vvx:           Real X `GXVV <geosoft.gxapi.GXVV>`
        :param vvy:           Real Y `GXVV <geosoft.gxapi.GXVV>`
        :param vvz:           Real Z `GXVV <geosoft.gxapi.GXVV>`
        :param img:           `GXIMG <geosoft.gxapi.GXIMG>` for Z value, or `IMG_NULL <geosoft.gxapi.IMG_NULL>` for no Z.
        :param prompt:        Command line prompt string
        :param newline:       0 for no newline 1 for automatic newline at each point
        :param pixel_radius:  Close the polygon if the selected location is within this radius in screen pixels.
        :type  vvx:           GXVV
        :type  vvy:           GXVV
        :type  vvz:           GXVV
        :type  img:           GXIMG
        :type  prompt:        str
        :type  newline:       int
        :type  pixel_radius:  int

        :returns:             0 if user digitized some points.
                              1 if user cancelled.
        :rtype:               int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.

        **Note:** This is the same as `digitize2 <geosoft.gxapi.GXEMAP.digitize2>`, except that it automatically
        detects, (except for the 2nd and 3rd points) when a selected location
        is within the entered number of pixels from the starting point. If yes,
        the polygon is assumed to be closed, and the operation is the same as
        the RMB "done" command, and the process returns 0.
        """
        ret_val = self._digitize_polygon(vvx, vvy, vvz, img, prompt.encode(), newline, pixel_radius)
        return ret_val




    def get_box(self, str_val, min_x, min_y, max_x, max_y):
        """
        Returns the coordinates of a user selected box.
        
        :param str_val:  User prompt string
        :param min_x:    X minimum in current view user units.
        :param min_y:    Y
        :param max_x:    X maximum
        :param max_y:    Y
        :type  str_val:  str
        :type  min_x:    float_ref
        :type  min_y:    float_ref
        :type  max_x:    float_ref
        :type  max_y:    float_ref

        :returns:        0 if point returned.
                         1 if user cancelled.
        :rtype:          int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.
        """
        ret_val, min_x.value, min_y.value, max_x.value, max_y.value = self._get_box(str_val.encode(), min_x.value, min_y.value, max_x.value, max_y.value)
        return ret_val




    def get_box2(self, str_val, x1, y1, x2, y2, x3, y3, x4, y4):
        """
        Returns the coordinates of a user selected box in a warped view.
        
        :param str_val:  User prompt string
        :param x1:       X1 bottom left corner
        :param y1:       Y1
        :param x2:       X2 bottom right corner
        :param y2:       Y2
        :param x3:       X3 top right corner
        :param y3:       Y3
        :param x4:       X4 top left corner
        :param y4:       Y4
        :type  str_val:  str
        :type  x1:       float_ref
        :type  y1:       float_ref
        :type  x2:       float_ref
        :type  y2:       float_ref
        :type  x3:       float_ref
        :type  y3:       float_ref
        :type  x4:       float_ref
        :type  y4:       float_ref

        :returns:        0 if point returned.
                         1 if user cancelled.
        :rtype:          int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.

        **Note:** If the data view has a rotational (or other) warp, then the
        `get_box <geosoft.gxapi.GXEMAP.get_box>` function returns only opposite diagonal points in the
        box, not enough info to determine the other two corners. This
        function returns the exact coordinates of all four corners, calculated
        from the pixel locations.
        """
        ret_val, x1.value, y1.value, x2.value, y2.value, x3.value, y3.value, x4.value, y4.value = self._get_box2(str_val.encode(), x1.value, y1.value, x2.value, y2.value, x3.value, y3.value, x4.value, y4.value)
        return ret_val




    def get_grid(self, str_val, nx, ny, angle, x1, y1, x_len, y_len):
        """
        Position and size a grid on a map.
        
        :param str_val:  User prompt string
        :param nx:       Number of elements along primary axis to draw.
        :param ny:       Number of elements along secondary axis to draw.
        :param angle:    Angle of primary axis in degrees
        :param x1:       Grid origin X
        :param y1:       Grid origin Y
        :param x_len:    Primary axis length
        :param y_len:    Secondary axis length
        :type  str_val:  str
        :type  nx:       int
        :type  ny:       int
        :type  angle:    float_ref
        :type  x1:       float_ref
        :type  y1:       float_ref
        :type  x_len:    float_ref
        :type  y_len:    float_ref

        :returns:        0 if line returned.
                         1 if user cancelled.
        :rtype:          int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.

        **Note:** If the input angle is `rDUMMY <geosoft.gxapi.rDUMMY>`, an extra step is inserted
        for the user to define the angle by drawing a line
        with the mouse.
        The output primary axis angle will always be in the
        range -90 < angle <= 90. The grid origin is shifted to
        whichever corner necessary to make this possible, while keeping
        the secondary axis at 90 degrees greater than the primary (
        going counter-clockwise).
        The coordinates are returned in the current User projection
        (See `GXMVIEW.get_user_ipj <geosoft.gxapi.GXMVIEW.get_user_ipj>` and `GXMVIEW.set_user_ipj <geosoft.gxapi.GXMVIEW.set_user_ipj>`.)
        """
        ret_val, angle.value, x1.value, y1.value, x_len.value, y_len.value = self._get_grid(str_val.encode(), nx, ny, angle.value, x1.value, y1.value, x_len.value, y_len.value)
        return ret_val




    def get_line(self, str_val, min_x, min_y, max_x, max_y):
        """
        Returns the end points of a line.
        
        :param str_val:  User prompt string
        :param min_x:    X1 in view user units
        :param min_y:    Y1
        :param max_x:    X2
        :param max_y:    Y2
        :type  str_val:  str
        :type  min_x:    float_ref
        :type  min_y:    float_ref
        :type  max_x:    float_ref
        :type  max_y:    float_ref

        :returns:        0 if line returned.
                         1 if user cancelled.
        :rtype:          int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.

        **Note:** The coordinates are returned in the current User projection
        (See `GXMVIEW.get_user_ipj <geosoft.gxapi.GXMVIEW.get_user_ipj>` and `GXMVIEW.set_user_ipj <geosoft.gxapi.GXMVIEW.set_user_ipj>`.)
        """
        ret_val, min_x.value, min_y.value, max_x.value, max_y.value = self._get_line(str_val.encode(), min_x.value, min_y.value, max_x.value, max_y.value)
        return ret_val




    def get_line_ex(self, str_val, min_x, min_y, max_x, max_y):
        """
        Returns the end points of a line.
        
        :param str_val:  User prompt string
        :param min_x:    X1 in view user units
        :param min_y:    Y1
        :param max_x:    X2
        :param max_y:    Y2
        :type  str_val:  str
        :type  min_x:    float_ref
        :type  min_y:    float_ref
        :type  max_x:    float_ref
        :type  max_y:    float_ref

        :returns:        0 if line returned.
                         1 - Right Mouse
                         2 - Escape/Cancel
        :rtype:          int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.

        **Note:** The coordinates are returned in the current User projection
        (See `GXMVIEW.get_user_ipj <geosoft.gxapi.GXMVIEW.get_user_ipj>` and `GXMVIEW.set_user_ipj <geosoft.gxapi.GXMVIEW.set_user_ipj>`.)
        """
        ret_val, min_x.value, min_y.value, max_x.value, max_y.value = self._get_line_ex(str_val.encode(), min_x.value, min_y.value, max_x.value, max_y.value)
        return ret_val




    def get_line_xyz(self, str_val, min_x, min_y, min_z, max_x, max_y, max_z):
        """
        Returns the end points of a line in X,Y and Z
        
        :param str_val:  User prompt string
        :param min_x:    X1 in view user units
        :param min_y:    Y1
        :param min_z:    Z1
        :param max_x:    X2
        :param max_y:    Y2
        :param max_z:    Z2
        :type  str_val:  str
        :type  min_x:    float_ref
        :type  min_y:    float_ref
        :type  min_z:    float_ref
        :type  max_x:    float_ref
        :type  max_y:    float_ref
        :type  max_z:    float_ref

        :returns:        0 if line returned.
                         1 - Right Mouse
                         2 - Escape/Cancel
        :rtype:          int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.

        **Note:** The coordinates are returned in the current User projection
        (See `GXMVIEW.get_user_ipj <geosoft.gxapi.GXMVIEW.get_user_ipj>` and `GXMVIEW.set_user_ipj <geosoft.gxapi.GXMVIEW.set_user_ipj>`.)
        This is useful for digitizing a line in an oriented view and getting
        the true coordinates in (X, Y, Z) at the selected point on the view plane.
        """
        ret_val, min_x.value, min_y.value, min_z.value, max_x.value, max_y.value, max_z.value = self._get_line_xyz(str_val.encode(), min_x.value, min_y.value, min_z.value, max_x.value, max_y.value, max_z.value)
        return ret_val




    def get_point(self, str_val, x, y):
        """
        Returns the coordinates of a user selected point.
        
        :param str_val:  User prompt string
        :param x:        X coordinate in current view user units.
        :param y:        Y
        :type  str_val:  str
        :type  x:        float_ref
        :type  y:        float_ref

        :returns:        0 if point returned.
                         1 if user cancelled.
        :rtype:          int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.

        **Note:** This will wait for user to select a point.

        .. seealso::

            iTrackPoint, GetCurPoint, GetCursor
        """
        ret_val, x.value, y.value = self._get_point(str_val.encode(), x.value, y.value)
        return ret_val




    def get_point_ex(self, str_val, x, y):
        """
        Returns the coordinates of a user selected point.
        
        :param str_val:  User prompt string
        :param x:        X coordinate in current view user units.
        :param y:        Y
        :type  str_val:  str
        :type  x:        float_ref
        :type  y:        float_ref

        :returns:        0 if point returned.
                         1 if user used right mouse and then Done.
                         2 if user cancelled.
                         3 if capture is lost.
        :rtype:          int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.

        **Note:** This will wait for user to select a point.

        .. seealso::

            iTrackPoint, GetCurPoint, GetCursor
        """
        ret_val, x.value, y.value = self._get_point_ex(str_val.encode(), x.value, y.value)
        return ret_val




    def get_point_3d(self, str_val, x, y, z):
        """
        Returns the coordinates of a user selected point.
        
        :param str_val:  User prompt string
        :param x:        X coordinate in current view user units.
        :param y:        Y
        :param z:        Z
        :type  str_val:  str
        :type  x:        float_ref
        :type  y:        float_ref
        :type  z:        float_ref

        :returns:        0 if point returned.
                         1 if user used right mouse and then Done.
                         2 if user cancelled.
                         3 if capture is lost.
        :rtype:          int

        .. versionadded:: 9.1

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.

        **Note:** This will wait for user to select a point.

        .. seealso::

            iTrackPoint, GetCurPoint, GetCursor
        """
        ret_val, x.value, y.value, z.value = self._get_point_3d(str_val.encode(), x.value, y.value, z.value)
        return ret_val




    def get_poly_line(self, str_val, vv_x, vv_y):
        """
        Returns a polyline.
        
        :param str_val:  User prompt string
        :param vv_x:     X
        :param vv_y:     Y
        :type  str_val:  str
        :type  vv_x:     GXVV
        :type  vv_y:     GXVV

        :returns:        0 if line returned.
                         1 if user cancelled.
        :rtype:          int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.

        **Note:** The coordinates are returned in the current User projection
        (See `GXMVIEW.get_user_ipj <geosoft.gxapi.GXMVIEW.get_user_ipj>` and `GXMVIEW.set_user_ipj <geosoft.gxapi.GXMVIEW.set_user_ipj>`.)
        """
        ret_val = self._get_poly_line(str_val.encode(), vv_x, vv_y)
        return ret_val




    def get_poly_line_xyz(self, str_val, vv_x, vv_y, vv_z):
        """
        Returns a polyline.
        
        :param str_val:  User prompt string
        :param vv_x:     X
        :param vv_y:     Y
        :param vv_z:     Z
        :type  str_val:  str
        :type  vv_x:     GXVV
        :type  vv_y:     GXVV
        :type  vv_z:     GXVV

        :returns:        0 if line returned.
                         1 if user cancelled.
        :rtype:          int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.

        **Note:** The coordinates are returned in the current User projection
        (See `GXMVIEW.get_user_ipj <geosoft.gxapi.GXMVIEW.get_user_ipj>` and `GXMVIEW.set_user_ipj <geosoft.gxapi.GXMVIEW.set_user_ipj>`.) In this version
        of the method X, Y and Z (depth) are returned. Initially created
        to deal with crooked sections.
        """
        ret_val = self._get_poly_line_xyz(str_val.encode(), vv_x, vv_y, vv_z)
        return ret_val




    def get_rect(self, str_val, min_x, min_y, max_x, max_y):
        """
        Returns the coordinates of a user selected box starting at a corner.
        
        :param str_val:  User prompt string
        :param min_x:    X minimum in current view user units.   (defines corner)
        :param min_y:    Y
        :param max_x:    X maximum
        :param max_y:    Y
        :type  str_val:  str
        :type  min_x:    float_ref
        :type  min_y:    float_ref
        :type  max_x:    float_ref
        :type  max_y:    float_ref

        :returns:        0 if point returned.
                         1 if user cancelled.
        :rtype:          int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.

        **Note:** The coordinates are returned in the current User projection
        (See `GXMVIEW.get_user_ipj <geosoft.gxapi.GXMVIEW.get_user_ipj>` and `GXMVIEW.set_user_ipj <geosoft.gxapi.GXMVIEW.set_user_ipj>`.)
        If the user `GXIPJ <geosoft.gxapi.GXIPJ>` distorts the coordinates from being rectilinear
        (e.g. for a TriPlot graph), then care should be taken since the
        (Xmin, Ymin) and (Xmax, Ymax) values returned do not necessarily
        correspond to the lower-left and upper-right corners. In fact, the
        returned values are calculated by taking the starting (fixed) corner
        and the tracked (opposite) corner, and finding the min and max for
        X and Y among these two points. With a warped User projection, those
        two corner locations could easily be (Xmin, Ymax) and (Xmax, Ymin).
        This becomes quite important if you want to use the rectangle for a
        masking operation, because the "other" two corner's coordinates may
        need to be constructed based on a knowledge of the User projection,
        and may not be directly obtained from the returned X and Y min and
        max values. What appears to be a rectangle as seen on the map is not
        necessarily a rectangle in the User coordinates.
        """
        ret_val, min_x.value, min_y.value, max_x.value, max_y.value = self._get_rect(str_val.encode(), min_x.value, min_y.value, max_x.value, max_y.value)
        return ret_val




    def track_point(self, flags, x, y):
        """
        Get point without prompt or cursor change with tracking
        
        :param flags:  :ref:`EMAP_TRACK`
        :param x:      X coordinate in current view user units.
        :param y:      Y
        :type  flags:  int
        :type  x:      float_ref
        :type  y:      float_ref

        :returns:      0 if point returned.
                       1 if user cancelled.
        :rtype:        int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.
        """
        ret_val, x.value, y.value = self._track_point(flags, x.value, y.value)
        return ret_val




# Map Viewport Mode Methods



    def get_aoi_area(self, min_x, min_y, max_x, max_y):
        """
        Get the area of interest.
        
        :param min_x:  X Min returned
        :param min_y:  Y Min returned
        :param max_x:  X Max returned
        :param max_y:  Y Max returned
        :type  min_x:  float_ref
        :type  min_y:  float_ref
        :type  max_x:  float_ref
        :type  max_y:  float_ref

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.

        **Note:** Coordinates are based on the current view units.
        """
        min_x.value, min_y.value, max_x.value, max_y.value = self._get_aoi_area(min_x.value, min_y.value, max_x.value, max_y.value)
        




    def set_aoi_area(self, min_x, min_y, max_x, max_y):
        """
        Set the area of interest.
        
        :param min_x:  X Min
        :param min_y:  Y Min
        :param max_x:  X Max
        :param max_y:  Y Max
        :type  min_x:  float
        :type  min_y:  float
        :type  max_x:  float
        :type  max_y:  float

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.

        **Note:** Coordinates are based on the current view user units.
        The map is immediatly redrawn.
        """
        self._set_aoi_area(min_x, min_y, max_x, max_y)
        




    def set_viewport_mode(self, mode):
        """
        Set the viewport mode.
        
        :param mode:  :ref:`EMAP_VIEWPORT`
        :type  mode:  int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.

        **Note:** This is handy for using a map to define an area of interest. Use in conjunction
        with Get/Set AOIArea. If this is used inside montaj it is important to set or provide
        for a method to set the map mode back to normal as this is not exposed in the interface.
        """
        self._set_viewport_mode(mode)
        




# Tracking Methods



    def get_selected_vertices(self, vv_x, vv_y):
        """
        Get the verticies of selected object
        
        :param vv_x:  X `GXVV <geosoft.gxapi.GXVV>` Handle
        :param vv_y:  Y `GXVV <geosoft.gxapi.GXVV>` Handle
        :type  vv_x:  GXVV
        :type  vv_y:  GXVV

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.

        **Note:** Works only in Vertex Edit Mode
        """
        self._get_selected_vertices(vv_x, vv_y)
        




# Virtual


    @classmethod
    def create_virtual(cls, name):
        """
        Makes this `GXEMAP <geosoft.gxapi.GXEMAP>` object the current active object to the user.
        
        :param name:  Name of map to create a virtual `GXEMAP <geosoft.gxapi.GXEMAP>` from
        :type  name:  str

        :returns:     `GXEMAP <geosoft.gxapi.GXEMAP>` Object
        :rtype:       GXEMAP

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.
        """
        ret_val = gxapi_cy.WrapEMAP._create_virtual(GXContext._get_tls_geo(), name.encode())
        return GXEMAP(ret_val)




# External Window


    @classmethod
    def load_control(cls, map_file, window):
        """
        Version of `load <geosoft.gxapi.GXEMAP.load>` that can be used to load a database via subclassing into a Windows control.
        
        :param map_file:  Map filename
        :param window:    Window handle to receive document
        :type  map_file:  str
        :type  window:    int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.
        """
        gxapi_cy.WrapEMAP._load_control(GXContext._get_tls_geo(), map_file.encode(), window)
        



    @classmethod
    def load_with_view_control(cls, map_file, emap, window):
        """
        Version of `GXEDB.load_with_view <geosoft.gxapi.GXEDB.load_with_view>` that can be used to load a database via subclassing into a Windows control.
        
        :param map_file:  Map filename
        :param emap:      `GXEMAP <geosoft.gxapi.GXEMAP>` handle to use as the source view
        :param window:    Window handle to receive document
        :type  map_file:  str
        :type  emap:      GXEMAP
        :type  window:    int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.
        """
        gxapi_cy.WrapEMAP._load_with_view_control(GXContext._get_tls_geo(), map_file.encode(), emap, window)
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer