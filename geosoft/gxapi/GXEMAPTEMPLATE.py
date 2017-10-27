### extends 'class_empty.py'
### block ClassImports
# NOTICE: Do not edit anything here, it is generated code
from typing import NewType
from . import gxapi_cy
from geosoft.gxapi import GXContext, float_ref, int_ref, str_ref
from .GXMAPTEMPLATE import GXMAPTEMPLATE


### endblock ClassImports

### block Header
# NOTICE: The code generator will not replace the code in this block
### endblock Header

### block ClassImplementation
# NOTICE: Do not edit anything here, it is generated code
class GXEMAPTEMPLATE:
    """
    GXEMAPTEMPLATE class.

    The `GXEMAPTEMPLATE <geosoft.gxapi.GXEMAPTEMPLATE>` class provides access to a map template as displayed within
    Oasis montaj, but does not change data within the template itself.
    It performs functions such as setting the currently displayed area,
    or drawing "tracking" lines or boxes on the template (which are not
    part of the template itself).

    **Note:**

    To obtain access to the map template itself, it is recommended practice
    to begin with an `GXEMAPTEMPLATE <geosoft.gxapi.GXEMAPTEMPLATE>` object, and use the Lock function to
    lock the underlying template to prevent external changes. The returned
    `GXMAPTEMPLATE <geosoft.gxapi.GXMAPTEMPLATE>` object may then be safely used to make changes to the template itself.
    
    VIRTUAL `GXEMAPTEMPLATE <geosoft.gxapi.GXEMAPTEMPLATE>` SUPPORT
    
    These methods are only available when running in an external application.
    They allow the GX to open a map template and then create a Virtual `GXEMAPTEMPLATE <geosoft.gxapi.GXEMAPTEMPLATE>` from that
    map template. The GX can then call MakeCurrent and set the current `GXEMAPTEMPLATE <geosoft.gxapi.GXEMAPTEMPLATE>` so
    that code that follows sees this map template as the current `GXMAPTEMPLATE <geosoft.gxapi.GXMAPTEMPLATE>`.
    
    Supported methods on Virtual EMAPTEMPLATEs are:
    
      `current <geosoft.gxapi.GXEMAPTEMPLATE.current>`
      `current_no_activate <geosoft.gxapi.GXEMAPTEMPLATE.current_no_activate>`
      `make_current <geosoft.gxapi.GXEMAPTEMPLATE.make_current>`
      `have_current <geosoft.gxapi.GXEMAPTEMPLATE.have_current>`
      `current_if_exists <geosoft.gxapi.GXEMAPTEMPLATE.current_if_exists>`
    
      `lock <geosoft.gxapi.GXEMAPTEMPLATE.lock>`
      `un_lock <geosoft.gxapi.GXEMAPTEMPLATE.un_lock>`
    
      `get_name <geosoft.gxapi.GXEMAPTEMPLATE.get_name>`
    
      `loaded <geosoft.gxapi.GXEMAPTEMPLATE.loaded>`
      `load <geosoft.gxapi.GXEMAPTEMPLATE.load>`
      `load_no_activate <geosoft.gxapi.GXEMAPTEMPLATE.load_no_activate>`
      `un_load_verify <geosoft.gxapi.GXEMAPTEMPLATE.un_load_verify>`
      `un_load <geosoft.gxapi.GXEMAPTEMPLATE.un_load>`
    
      `create_virtual <geosoft.gxapi.GXEMAPTEMPLATE.create_virtual>`
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._wrapper = None

    def __del__(self):
        self._wrapper = None

    def __init__(self, wrapper=None):
        self._wrapper = wrapper if wrapper else gxapi_cy.WrapEMAPTEMPLATE(GXContext._get_tls_geo(), 0)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of `GXEMAPTEMPLATE`
        
        :returns: A null `GXEMAPTEMPLATE`
        """
        return cls()

    def is_null(self):
        """
        Check if the instance of `GXEMAPTEMPLATE` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of `GXEMAPTEMPLATE`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Drag-and-drop methods



    def drag_drop_enabled(self):
        """
        Is drag-and-drop enabled for the map?
        """
        ret_val = self._wrapper.drag_drop_enabled()
        return ret_val




    def set_drag_drop_enabled(self, enable):
        """
        Set whether drag-and-drop is enabled for the map.
        """
        self._wrapper.set_drag_drop_enabled(enable)
        




# General


    @classmethod
    def current(cls):
        """
        This method returns the Current Edited map template.
        """
        ret_val = gxapi_cy.WrapEMAPTEMPLATE.current(GXContext._get_tls_geo())
        return GXEMAPTEMPLATE(ret_val)



    @classmethod
    def current_no_activate(cls):
        """
        This method returns the Current Edited map template.

        **Note:**

        This function acts just like `current <geosoft.gxapi.GXEMAPTEMPLATE.current>` except that the document is not activated (brought to foreground) and no
        guarantee is given about which document is currently active.
        """
        ret_val = gxapi_cy.WrapEMAPTEMPLATE.current_no_activate(GXContext._get_tls_geo())
        return GXEMAPTEMPLATE(ret_val)



    @classmethod
    def current_if_exists(cls):
        """
        This method returns the Current Edited map.
        """
        ret_val = gxapi_cy.WrapEMAPTEMPLATE.current_if_exists(GXContext._get_tls_geo())
        return GXEMAPTEMPLATE(ret_val)





    @classmethod
    def get_map_templates_lst(cls, lst, path):
        """
        Load the file names of open maps into a `GXLST <geosoft.gxapi.GXLST>`.
        """
        ret_val = gxapi_cy.WrapEMAPTEMPLATE.get_map_templates_lst(GXContext._get_tls_geo(), lst._wrapper, path)
        return ret_val




    def get_name(self, name):
        """
        Get the name of the map object of this `GXEMAPTEMPLATE <geosoft.gxapi.GXEMAPTEMPLATE>`.
        """
        name.value = self._wrapper.get_name(name.value.encode())
        



    @classmethod
    def have_current(cls):
        """
        This method returns whether a current map is loaded
        """
        ret_val = gxapi_cy.WrapEMAPTEMPLATE.have_current(GXContext._get_tls_geo())
        return ret_val



    @classmethod
    def i_get_specified_map_name(cls, field, value, name):
        """
        Find a loaded map that has a setting in its reg.
        """
        ret_val, name.value = gxapi_cy.WrapEMAPTEMPLATE.i_get_specified_map_name(GXContext._get_tls_geo(), field.encode(), value.encode(), name.value.encode())
        return ret_val




    def is_locked(self):
        """
        Is this MapTemplate locked
        """
        ret_val = self._wrapper.is_locked()
        return ret_val



    @classmethod
    def loaded(cls, name):
        """
        Returns 1 if a map is loaded .
        """
        ret_val = gxapi_cy.WrapEMAPTEMPLATE.loaded(GXContext._get_tls_geo(), name.encode())
        return ret_val




    def get_window_position(self, left, top, right, bottom, state, is_floating):
        """
        Get the map window's position and dock state
        """
        left.value, top.value, right.value, bottom.value, state.value, is_floating.value = self._wrapper.get_window_position(left.value, top.value, right.value, bottom.value, state.value, is_floating.value)
        




    def set_window_position(self, left, top, right, bottom, state, is_floating):
        """
        Get the map window's position and dock state
        """
        self._wrapper.set_window_position(left, top, right, bottom, state, is_floating)
        




    def read_only(self):
        """
        Checks if a map is currently opened in a read-only mode.
        """
        ret_val = self._wrapper.read_only()
        return ret_val



    @classmethod
    def load(cls, name):
        """
        Loads maps into the editor.

        **Note:**

        The last map in the list will be the current map.
        
        Maps may already be loaded.
        
        Only the first file in the list may have a directory path.
        All other files in the list are assumed to be in the same
        directory as the first file.
        """
        ret_val = gxapi_cy.WrapEMAPTEMPLATE.load(GXContext._get_tls_geo(), name.encode())
        return GXEMAPTEMPLATE(ret_val)



    @classmethod
    def load_no_activate(cls, name):
        """
        Loads documents into the workspace

        **Note:**

        This function acts just like `load <geosoft.gxapi.GXEMAPTEMPLATE.load>` except that the document(s) is not activated (brought to foreground) and no
        guarantee is given about which document is currently active.
        """
        ret_val = gxapi_cy.WrapEMAPTEMPLATE.load_no_activate(GXContext._get_tls_geo(), name.encode())
        return GXEMAPTEMPLATE(ret_val)




    def lock(self):
        """
        This method locks the Edited map.
        """
        ret_val = self._wrapper.lock()
        return GXMAPTEMPLATE(ret_val)




    def make_current(self):
        """
        Makes this `GXEMAPTEMPLATE <geosoft.gxapi.GXEMAPTEMPLATE>` object the current active object to the user.
        """
        self._wrapper.make_current()
        



    @classmethod
    def un_load(cls, name):
        """
        Unloads a map template.

        **Note:**

        If the map template is not loaded, nothing happens.
        Same as `un_load_verify <geosoft.gxapi.GXEMAPTEMPLATE.un_load_verify>` with FALSE to prompt save.
        """
        gxapi_cy.WrapEMAPTEMPLATE.un_load(GXContext._get_tls_geo(), name.encode())
        



    @classmethod
    def un_load_all(cls):
        """
        Unloads all opened maps
        """
        gxapi_cy.WrapEMAPTEMPLATE.un_load_all(GXContext._get_tls_geo())
        



    @classmethod
    def un_load_verify(cls, name, prompt):
        """
        Unloads an edited map, optional prompt to save.

        **Note:**

        If the map is not loaded, nothing happens.
        If "FALSE", map is saved without a prompt.
        """
        gxapi_cy.WrapEMAPTEMPLATE.un_load_verify(GXContext._get_tls_geo(), name.encode(), prompt)
        




    def un_lock(self):
        """
        This method unlocks the Edited map.
        """
        self._wrapper.un_lock()
        




# Input



    def get_box(self, state, min_x, min_y, max_x, max_y):
        """
        Returns the coordinates of a user selected box.

        **Note:**

        The coordinates are returned in the current template units
        (See GetUnits and SetUnits in `GXMAPTEMPLATE <geosoft.gxapi.GXMAPTEMPLATE>`)
        """
        ret_val, min_x.value, min_y.value, max_x.value, max_y.value = self._wrapper.get_box(state.encode(), min_x.value, min_y.value, max_x.value, max_y.value)
        return ret_val




    def get_line(self, str_val, min_x, min_y, max_x, max_y):
        """
        Returns the end points of a line.

        **Note:**

        The coordinates are returned in the current template units
        (See GetUnits and SetUnits in `GXMAPTEMPLATE <geosoft.gxapi.GXMAPTEMPLATE>`)
        """
        ret_val, min_x.value, min_y.value, max_x.value, max_y.value = self._wrapper.get_line(str_val.encode(), min_x.value, min_y.value, max_x.value, max_y.value)
        return ret_val




    def get_point(self, str_val, x, y):
        """
        Returns the coordinates of a user selected point.

        **Note:**

        The coordinates are returned in the current template units
        (See GetUnits and SetUnits in `GXMAPTEMPLATE <geosoft.gxapi.GXMAPTEMPLATE>`)
        """
        ret_val, x.value, y.value = self._wrapper.get_point(str_val.encode(), x.value, y.value)
        return ret_val




    def get_rect(self, str_val, min_x, min_y, max_x, max_y):
        """
        Returns the coordinates of a user selected box starting at a corner.

        **Note:**

        The coordinates are returned in the current template units
        (See GetUnits and SetUnits in `GXMAPTEMPLATE <geosoft.gxapi.GXMAPTEMPLATE>`)
        """
        ret_val, min_x.value, min_y.value, max_x.value, max_y.value = self._wrapper.get_rect(str_val.encode(), min_x.value, min_y.value, max_x.value, max_y.value)
        return ret_val




    def track_point(self, flags, x, y):
        """
        Get point without prompt or cursor change with tracking
        """
        ret_val, x.value, y.value = self._wrapper.track_point(flags, x.value, y.value)
        return ret_val




# Selection Methods



    def get_item_selection(self, item):
        """
        Gets info about the current selected item

        **Note:**

        If nothing is selected the string will be empty and the function will return `GS_FALSE <geosoft.gxapi.GS_FALSE>`;
        """
        ret_val, item.value = self._wrapper.get_item_selection(item.value.encode())
        return ret_val




    def set_item_selection(self, item):
        """
        Sets the current selected item

        **Note:**

        An empty string will unselect everything.
        """
        self._wrapper.set_item_selection(item.encode())
        




# View Window



    def get_display_area(self, min_x, min_y, max_x, max_y):
        """
        Get the area you are currently looking at.

        **Note:**

        The coordinates are based on the current template units
        (See GetUnits and SetUnits in `GXMAPTEMPLATE <geosoft.gxapi.GXMAPTEMPLATE>`)
        """
        min_x.value, min_y.value, max_x.value, max_y.value = self._wrapper.get_display_area(min_x.value, min_y.value, max_x.value, max_y.value)
        




    def get_template_layout_props(self, snap_to_grid, snap_dist, view_grid, view_rulers, view_units, grid_red, grid_green, grid_blue):
        """
        Get the base layout view properties.

        **Note:**

        This affects the display units and other related properties for the base
        view of a map.
        """
        snap_to_grid.value, snap_dist.value, view_grid.value, view_rulers.value, view_units.value, grid_red.value, grid_green.value, grid_blue.value = self._wrapper.get_template_layout_props(snap_to_grid.value, snap_dist.value, view_grid.value, view_rulers.value, view_units.value, grid_red.value, grid_green.value, grid_blue.value)
        




    def get_window_state(self):
        """
        Retrieve the current state of the map window
        """
        ret_val = self._wrapper.get_window_state()
        return ret_val




    def set_display_area(self, min_x, min_y, max_x, max_y):
        """
        Set the area you wish to see.

        **Note:**

        The coordinates are based on the current template units
        (See GetUnits and SetUnits in `GXMAPTEMPLATE <geosoft.gxapi.GXMAPTEMPLATE>`)
        """
        self._wrapper.set_display_area(min_x, min_y, max_x, max_y)
        




    def set_template_layout_props(self, snap_to_grid, snap_dist, view_grid, view_rulers, view_units, grid_red, grid_green, grid_blue):
        """
        Set the base layout view properties.

        **Note:**

        This affects the display units and other related properties for the base
        view of a map.
        """
        self._wrapper.set_template_layout_props(snap_to_grid, snap_dist, view_grid, view_rulers, view_units, grid_red, grid_green, grid_blue)
        




    def set_window_state(self, state):
        """
        Changes the state of the map window
        """
        self._wrapper.set_window_state(state)
        




# Virtual


    @classmethod
    def create_virtual(cls, name):
        """
        Makes this `GXEMAPTEMPLATE <geosoft.gxapi.GXEMAPTEMPLATE>` object the current active object to the user.
        """
        ret_val = gxapi_cy.WrapEMAPTEMPLATE.create_virtual(GXContext._get_tls_geo(), name.encode())
        return GXEMAPTEMPLATE(ret_val)





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer