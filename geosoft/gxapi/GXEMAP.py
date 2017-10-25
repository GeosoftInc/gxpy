### extends 'class_empty.py'
### block ClassImports
# NOTICE: Do not edit anything here, it is generated code
from typing import NewType
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
class GXEMAP:
    """
    GXEMAP class.

    The :class:`geosoft.gxapi.GXEMAP` class provides access to a map as displayed within
    Oasis montaj, but (usually) does not change data within the map itself.
    It performs functions such as setting the currently displayed area,
    or drawing "tracking" lines or boxes on the map (which are not
    part of the map itself).

    **Note:**

    To obtain access to the map itself, it is recommended practice
    to begin with an :class:`geosoft.gxapi.GXEMAP` object, and use the Lock_EMAP function to
    lock the underlying map to prevent external changes. The returned
    :class:`geosoft.gxapi.GXMAP` object (see :class:`geosoft.gxapi.GXMAP`) may then be safely used to make changes to the map itself.
    
    :class:`geosoft.gxapi.GXMAP` Redraw Rules:
    
    1. Redraws only occur at the end of the proccess (GX or SCRIPT) not during.
    You can safely call other GX's and the map will not redraw. If you need the
    map to redraw immediately use Redraw_EMAP instead.
    
    2. If the final GX calls Cancel_SYS, the map redraw is not done. If you
    need to force a redraw when the user hits cancel use the Redraw_EMAP function.
    
    3. You can set the redraw flag to :attr:`geosoft.gxapi.EMAP_REDRAW_YES` or :attr:`geosoft.gxapi.EMAP_REDRAW_NO` at any
    time using SetRedrawFlag_EMAP. This flag will only be looked at, when
    the last call to UnLock_EMAP occurs and is ignored on a Cancel_SYS.
    
    4. Redraw_EMAP only works if the current map is not locked. It will do nothing
    if the map is locked.  Issue an UnLock_EMAP before using this function.
    
    
    VIRTUAL :class:`geosoft.gxapi.GXEMAP` SUPPORT
    
    These methods are only available when running in an external application.
    They allow the GX to open a :class:`geosoft.gxapi.GXMAP` and then create a Virtual :class:`geosoft.gxapi.GXEMAP` from that
    map. The GX can then call MakeCurrent_EMAP and set the current :class:`geosoft.gxapi.GXEMAP` so
    that code that follows sees this map as the current :class:`geosoft.gxapi.GXMAP`.
    
    Supported methods on Virtual EMAPS are:
    
    Current_EMAP
    CurrentNoActivate_EMAP
    MakeCurrent_EMAP
    iHaveCurrent_EMAP
    CurrentIfExists_EMAP
    Current_MAP
    
    Lock_EMAP
    UnLock_EMAP
    iIsLocked_EMAP
    
    IGetName_EMAP
    SetRedrawFlag_EMAP
    Redraw_EMAP
    
    iLoaded_EMAP
    Load_EMAP
    LoadNoActivate_EMAP
    UnLoadVerify_EMAP
    UnLoad_EMAP
    
    CreateVirtual_EMAP
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._wrapper = None

    def __del__(self):
        self._wrapper = None

    def __init__(self, wrapper=None):
        self._wrapper = wrapper if wrapper else gxapi_cy.WrapEMAP(GXContext._get_tls_geo(), 0)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of :class:`geosoft.gxapi.GXEMAP`
        
        :returns: A null :class:`geosoft.gxapi.GXEMAP`
        """
        return cls()

    def is_null(self):
        """
        Check if the instance of :class:`geosoft.gxapi.GXEMAP` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of :class:`geosoft.gxapi.GXEMAP`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Drag-and-drop methods



    def drop_map_clip_data(self, p2):
        """
        Drop Map clipboard data on this :class:`geosoft.gxapi.GXEMAP`
        """
        self._wrapper.drop_map_clip_data(p2)
        




    def drag_drop_enabled(self):
        """
        Is drag-and-drop enabled for the map?
        """
        ret_val = self._wrapper.drag_drop_enabled()
        return ret_val




    def set_drag_drop_enabled(self, p2):
        """
        Set whether drag-and-drop is enabled for the map.
        """
        self._wrapper.set_drag_drop_enabled(p2)
        




# Drawing



    def copy_to_clip(self):
        """
        Copy entire map to clipboard.

        **Note:**

        Four objects are placed on the clipboard:
        
        1. Georefernce Text
        2. Bitmap of current window screen resolution
        3. EMF of current window screen resolution
        4. Entire map as a Geosoft View (go to view mode
        and hit paste). The coordinates are placed
        in the current view coordinates.
        """
        self._wrapper.copy_to_clip()
        




    def draw_line(self, p2, p3, p4, p5):
        """
        Draws a line on the current map.

        **Note:**

        Locations are in the current view user units.
        
        The line is temporary and will disappear on the next
        screen refresh.  This function is for you to provide
        interactive screen feedback to your user.
        """
        self._wrapper.draw_line(p2, p3, p4, p5)
        




    def draw_rect(self, p2, p3, p4, p5):
        """
        Draws a rect on the current map.

        **Note:**

        Locations are in the current view user units.
        
        The line is temporary and will disappear on the next
        screen refresh.  This function is for you to provide
        interactive screen feedback to your user.
        """
        self._wrapper.draw_rect(p2, p3, p4, p5)
        




    def draw_rect_3d(self, p2, p3, p4, p5):
        """
        Plot a square symbol on a section view.

        **Note:**

        Plot a square symbol on a section view, but input 3D user coordinates
        
        The line is temporary and will disappear on the next
        screen refresh.  This function is for you to provide
        interactive screen feedback to your user.
        """
        self._wrapper.draw_rect_3d(p2, p3, p4, p5)
        




    def get_display_area(self, p2, p3, p4, p5):
        """
        Get the area you are currently looking at.

        **Note:**

        Coordinates are based on the current view units.
        For 3D views this will return the full map extents.
        """
        p2.value, p3.value, p4.value, p5.value = self._wrapper.get_display_area(p2.value, p3.value, p4.value, p5.value)
        




    def get_display_area_raw(self, p2, p3, p4, p5):
        """
        Get the area you are currently looking at in raw map units

        **Note:**

        Coordinates are in millimeters.
        For 3D views this will return the full map extents.
        """
        p2.value, p3.value, p4.value, p5.value = self._wrapper.get_display_area_raw(p2.value, p3.value, p4.value, p5.value)
        




    def get_map_layout_props(self, p2, p3, p4, p5, p6, p7, p8, p9):
        """
        Get the base layout view properties.

        **Note:**

        This affects the display units and other related properties for the base
        view of a map.
        """
        p2.value, p3.value, p4.value, p5.value, p6.value, p7.value, p8.value, p9.value = self._wrapper.get_map_layout_props(p2.value, p3.value, p4.value, p5.value, p6.value, p7.value, p8.value, p9.value)
        




    def get_map_snap(self, p2):
        """
        Get current snapping distance in MM
        """
        p2.value = self._wrapper.get_map_snap(p2.value)
        




    def get_window_state(self):
        """
        Retrieve the current state of the map window
        """
        ret_val = self._wrapper.get_window_state()
        return ret_val




    def set_display_area(self, p2, p3, p4, p5):
        """
        Set the area you wish to see.

        **Note:**

        Coordinates are based on the current view user units.
        The map is immediatly redrawn.
        """
        self._wrapper.set_display_area(p2, p3, p4, p5)
        




    def set_map_layout_props(self, p2, p3, p4, p5, p6, p7, p8, p9):
        """
        Set the base layout view properties.

        **Note:**

        This affects the display units and other related properties for the base
        view of a map.
        """
        self._wrapper.set_map_layout_props(p2, p3, p4, p5, p6, p7, p8, p9)
        




    def set_map_snap(self, p2):
        """
        Set current snapping distance in MM
        """
        self._wrapper.set_map_snap(p2)
        




    def set_window_state(self, p2):
        """
        Changes the state of the map window
        """
        self._wrapper.set_window_state(p2)
        




# General



    def packed_files(self):
        """
        The number of packed files in the map.
        """
        ret_val = self._wrapper.packed_files()
        return ret_val




    def activate_group(self, p2):
        """
        Activates a group and associated tools.

        **Note:**

        Activating a group basically enters the edit mode associated
        with the type of group. E.g. a vector group will enable the
        edit toolbar for that gorup and an :class:`geosoft.gxapi.GXAGG` will bring up the
        image color tool. Be sure to pass a combined name containing
        both the view name and the group separated by a "/" or "\\".
        """
        self._wrapper.activate_group(p2.encode())
        




    def activate_view(self, p2):
        """
        Activates a view and associated tools.
        """
        self._wrapper.activate_view(p2.encode())
        



    @classmethod
    def current(cls):
        """
        This method returns the Current Edited map.
        """
        ret_val = gxapi_cy.WrapEMAP.current(GXContext._get_tls_geo())
        return GXEMAP(ret_val)



    @classmethod
    def current_no_activate(cls):
        """
        This method returns the Current Edited map.

        **Note:**

        This function acts just like Current_EMAP except that the document is not activated (brought to foreground) and no
        guarantee is given about which document is currently active.
        """
        ret_val = gxapi_cy.WrapEMAP.current_no_activate(GXContext._get_tls_geo())
        return GXEMAP(ret_val)



    @classmethod
    def current_if_exists(cls):
        """
        This method returns the Current Edited map.
        """
        ret_val = gxapi_cy.WrapEMAP.current_if_exists(GXContext._get_tls_geo())
        return GXEMAP(ret_val)






    def destroy_view(self, p2):
        """
        Removes the view from the workspace.

        **Note:**

        Can only be run in interactive mode. After this call the
        :class:`geosoft.gxapi.GXEMAP` object will become invalid. If this is the last view on
        the document and the document has been modified the map will be
        unloaded and optionally saved depending on the `EMAP_REMOVE`
        parameter.
        """
        self._wrapper.destroy_view(p2)
        




    def font_lst(self, p2, p3):
        """
        List all Windows and geosoft fonts.

        **Note:**

        To get TT and GFN fonts, call twice with the same list
        and :attr:`geosoft.gxapi.EMAP_FONT_TT`, then :attr:`geosoft.gxapi.EMAP_FONT_GFN`, or vice-versa to
        change order of listing.
        """
        self._wrapper.font_lst(p2._wrapper, p3)
        




    def change_current_view(self, p2):
        """
        Change the current working view.

        **Note:**

        This function operates on the current map.
        Unlike iSetCurrentView_EMAP this function's action
        survive the GX finishing.
        """
        ret_val = self._wrapper.change_current_view(p2.encode())
        return ret_val




    def create_group_snapshot(self, p2):
        """
        Loads an :class:`geosoft.gxapi.GXLST` with the current view/group names
        existing in a map. Typically used to track group
        changes that are about to occur.
        """
        ret_val = self._wrapper.create_group_snapshot(p2._wrapper)
        return ret_val




    def get_3d_view_name(self, p2):
        """
        Get the name of a 3D view if the current view is 3D.
        """
        p2.value = self._wrapper.get_3d_view_name(p2.value.encode())
        




    def get_current_group(self, p2):
        """
        Get the current group name.

        **Note:**

        This function operates on the current map.
        """
        p2.value = self._wrapper.get_current_group(p2.value.encode())
        




    def get_current_view(self, p2):
        """
        Get the current view name.

        **Note:**

        This function operates on the current map.
        """
        p2.value = self._wrapper.get_current_view(p2.value.encode())
        



    @classmethod
    def get_maps_lst(cls, p1, p2):
        """
        Load the file names of open maps into a :class:`geosoft.gxapi.GXLST`.
        """
        ret_val = gxapi_cy.WrapEMAP.get_maps_lst(GXContext._get_tls_geo(), p1._wrapper, p2)
        return ret_val




    def get_name(self, p2):
        """
        Get the name of the map object of this :class:`geosoft.gxapi.GXEMAP`.
        """
        p2.value = self._wrapper.get_name(p2.value.encode())
        



    @classmethod
    def have_current(cls):
        """
        This method returns whether a current map is loaded
        """
        ret_val = gxapi_cy.WrapEMAP.have_current(GXContext._get_tls_geo())
        return ret_val



    @classmethod
    def i_get_specified_map_name(cls, p1, p2, p3):
        """
        Find a loaded map that has a setting in its reg.
        """
        ret_val, p3.value = gxapi_cy.WrapEMAP.i_get_specified_map_name(GXContext._get_tls_geo(), p1.encode(), p2.encode(), p3.value.encode())
        return ret_val




    def is_grid(self):
        """
        Is the map a grid map?
        """
        ret_val = self._wrapper.is_grid()
        return ret_val



    @classmethod
    def reload_grid(cls, p1):
        """
        Reloads a grid document.

        **Note:**

        Use this method to reload (if loaded) a grid document if the file on disk changed.
        """
        gxapi_cy.WrapEMAP.reload_grid(GXContext._get_tls_geo(), p1.encode())
        




    def is_3d_view(self):
        """
        Is the current view a 3D view.
        """
        ret_val = self._wrapper.is_3d_view()
        return ret_val




    def get_e_3dv(self):
        """
        Get an :class:`geosoft.gxapi.GXE3DV` from the :class:`geosoft.gxapi.GXEMAP`
        """
        ret_val = self._wrapper.get_e_3dv()
        return GXE3DV(ret_val)




    def is_locked(self):
        """
        Is this Map locked
        """
        ret_val = self._wrapper.is_locked()
        return ret_val



    @classmethod
    def loaded(cls, p1):
        """
        Returns 1 if a map is loaded .
        """
        ret_val = gxapi_cy.WrapEMAP.loaded(GXContext._get_tls_geo(), p1.encode())
        return ret_val




    def read_only(self):
        """
        Checks if a map is currently opened in a read-only mode.
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
        




    def doubleize_group_snapshot(self, p2):
        """
        The :class:`geosoft.gxapi.GXLST` passed in must contain View\\Group strings in
        the Name field only. The function will compare with
        a more current :class:`geosoft.gxapi.GXLST` and zoom the map to the new entry.

        **Note:**

        Typically this function is used in conjunction with
        CreateSnapshot_EMAP.
        """
        ret_val = self._wrapper.doubleize_group_snapshot(p2._wrapper)
        return ret_val




    def set_current_view(self, p2):
        """
        Set the current working view.

        **Note:**

        This function operates on the current map.
        It changes the view only during the execution of the
        GX. As soon as the GX terminates the view will revert
        to the original one.
        """
        ret_val = self._wrapper.set_current_view(p2.encode())
        return ret_val




    def get_view_ipj(self, p2, p3):
        """
        Get a view's :class:`geosoft.gxapi.GXIPJ`.

        **Note:**

        This function can be used to obtain a views coordinate system 
        without having to call Lock_EMAP. This could be an expensive operation
        that cause undesirable UX.
        """
        self._wrapper.get_view_ipj(p2.encode(), p3._wrapper)
        



    @classmethod
    def load(cls, p1):
        """
        Loads maps into the editor.

        **Note:**

        The last map in the list will be the current map.
        
        Maps may already be loaded.
        
        Only the first file in the list may have a directory path.
        All other files in the list are assumed to be in the same
        directory as the first file.
        """
        ret_val = gxapi_cy.WrapEMAP.load(GXContext._get_tls_geo(), p1.encode())
        return GXEMAP(ret_val)



    @classmethod
    def load_no_activate(cls, p1):
        """
        Loads documents into the workspace

        **Note:**

        This function acts just like Load_EMAP except that the document(s) is not activated (brought to foreground) and no
        guarantee is given about which document is currently active.
        """
        ret_val = gxapi_cy.WrapEMAP.load_no_activate(GXContext._get_tls_geo(), p1.encode())
        return GXEMAP(ret_val)



    @classmethod
    def load_with_view(cls, p1, p2):
        """
        Load an :class:`geosoft.gxapi.GXEMAP` with the view from a current :class:`geosoft.gxapi.GXEMAP`.

        **Note:**

        Can only be run in interactive mode. Is used by
        dbsubset to create a new database with the same
        view as previously.
        """
        ret_val = gxapi_cy.WrapEMAP.load_with_view(GXContext._get_tls_geo(), p1.encode(), p2._wrapper)
        return GXEMAP(ret_val)




    def lock(self):
        """
        This method locks the Edited map.

        **Note:**

        The Redraw flag is set to :attr:`geosoft.gxapi.EMAP_REDRAW_YES` when this functions is called.
        """
        ret_val = self._wrapper.lock()
        return GXMAP(ret_val)




    def make_current(self):
        """
        Makes this :class:`geosoft.gxapi.GXEMAP` object the current active object to the user.
        """
        self._wrapper.make_current()
        




    def print_(self, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14):
        """
        Print the current map to current printer.
        """
        self._wrapper.print_(p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14.encode())
        




    def redraw(self):
        """
        Redraw the map immediately.

        **Note:**

        Redraws the map immediately. Map must not be locked.
        """
        self._wrapper.redraw()
        




    def select_group(self, p2):
        """
        Select a group.
        """
        self._wrapper.select_group(p2.encode())
        




    def set_redraw_flag(self, p2):
        """
        Set the redraw flag.

        **Note:**

        This function is generally used to prevent redrawing of
        the map, which normally occurs after the last UnLock_EMAP
        call, in cases where it is known that no changes are being
        made to the map.
        
        Typical usage:
        
        ap = Lock_EMAP(EMap);
        etRedrawFlag_EMAP(EMap,:attr:`geosoft.gxapi.EMAP_REDRAW_NO`);
        
        Stuff....
        
        UnLock_EMAP(Map);
        """
        self._wrapper.set_redraw_flag(p2)
        



    @classmethod
    def un_load(cls, p1):
        """
        Unloads a :class:`geosoft.gxapi.GXMAP`.

        **Note:**

        If the :class:`geosoft.gxapi.GXMAP` is not loaded, nothing happens.
        Same as UnLoadVerify_EMAP with FALSE to prompt save.
        """
        gxapi_cy.WrapEMAP.un_load(GXContext._get_tls_geo(), p1.encode())
        



    @classmethod
    def un_load_all(cls):
        """
        Unloads all opened maps
        """
        gxapi_cy.WrapEMAP.un_load_all(GXContext._get_tls_geo())
        



    @classmethod
    def un_load_verify(cls, p1, p2):
        """
        Unloads an edited map, optional prompt to save.

        **Note:**

        If the map is not loaded, nothing happens.
        If "FALSE", map is saved without a prompt.
        """
        gxapi_cy.WrapEMAP.un_load_verify(GXContext._get_tls_geo(), p1.encode(), p2)
        




    def un_lock(self):
        """
        This method unlocks the Edited map.
        """
        self._wrapper.un_lock()
        




# Input



    def get_cur_point(self, p2, p3):
        """
        Returns the coordinates of the currently selected point in view coordinates
        """
        p2.value, p3.value = self._wrapper.get_cur_point(p2.value, p3.value)
        




    def get_cur_point_mm(self, p2, p3):
        """
        Returns the coordinates of the currently selected point in mm on map
        """
        p2.value, p3.value = self._wrapper.get_cur_point_mm(p2.value, p3.value)
        




    def get_cursor(self, p2, p3):
        """
        Returns the coordinates of the last known cursor location
        """
        p2.value, p3.value = self._wrapper.get_cursor(p2.value, p3.value)
        




    def get_cursor_mm(self, p2, p3):
        """
        Returns the coordinates of the last known cursor location in mm on map.
        """
        p2.value, p3.value = self._wrapper.get_cursor_mm(p2.value, p3.value)
        




    def digitize(self, p2, p3, p4, p5, p6, p7, p8):
        """
        Digitise points from the current map and place in a :class:`geosoft.gxapi.GXWA`.

        **Note:**

        The command line will start to recieve digitized points
        from the mouse.  Whenever the left mouse button is
        pressed, the current view X,Y are placed on the workspace
        command line.  If a valid :class:`geosoft.gxapi.GXIMG` is passed, the Z value is
        also placed on the command line.  If auto-newline is
        specified, the line is immediately placed into :class:`geosoft.gxapi.GXWA`,
        otherwise the user has the oportunity to enter data
        before pressing Enter.
        
        Locations are in the current view user units
        """
        ret_val = self._wrapper.digitize(p2._wrapper, p3._wrapper, p4, p5.encode(), p6.encode(), p7.encode(), p8)
        return ret_val




    def digitize2(self, p2, p3, p4, p5, p6, p7):
        """
        Digitise points from the current map and place in VVs.

        **Note:**

        The command line will start to recieve digitized points
        from the mouse.  Whenever the left mouse button is
        pressed, the current view X,Y are placed on the workspace
        command line.  If a valid :class:`geosoft.gxapi.GXIMG` is passed, the Z value is
        also placed on the command line.  If auto-newline is
        specified, the line is immediately placed into the VVs,
        otherwise the user has the oportunity to enter data
        before pressing Enter.
        
        Locations are in the current view user units
        """
        ret_val = self._wrapper.digitize2(p2._wrapper, p3._wrapper, p4._wrapper, p5._wrapper, p6.encode(), p7)
        return ret_val




    def digitize_peaks(self, p2, p3, p4, p5, p6, p7):
        """
        Digitise points from the current map and place in VVs.

        **Note:**

        Same as iDigitize2_EMAP, but the closest peaks to the selected locations are
        returned instead of the selected location. The method chooses the highest value
        of the 8 surrounding points, the repeats this process until no higher value can
        be found in any of the 8 surrounding points. If there are two or more points with
        a higher value, it will just take the first one and continue, and this method will
        stall on flat areas as well (since no surrounding point is larger).
        """
        ret_val = self._wrapper.digitize_peaks(p2._wrapper, p3._wrapper, p4._wrapper, p5._wrapper, p6.encode(), p7)
        return ret_val




    def digitize_polygon(self, p2, p3, p4, p5, p6, p7, p8):
        """
        Same as iDigitze2_EMAP, but automatically close polygons.

        **Note:**

        This is the same as iDigitize2_EMAP, except that it automatically
        detects, (except for the 2nd and 3rd points) when a selected location
        is within the entered number of pixels from the starting point. If yes,
        the polygon is assumed to be closed, and the operation is the same as
        the RMB "done" command, and the process returns 0.
        """
        ret_val = self._wrapper.digitize_polygon(p2._wrapper, p3._wrapper, p4._wrapper, p5._wrapper, p6.encode(), p7, p8)
        return ret_val




    def get_box(self, p2, p3, p4, p5, p6):
        """
        Returns the coordinates of a user selected box.
        """
        ret_val, p3.value, p4.value, p5.value, p6.value = self._wrapper.get_box(p2.encode(), p3.value, p4.value, p5.value, p6.value)
        return ret_val




    def get_box2(self, p2, p3, p4, p5, p6, p7, p8, p9, p10):
        """
        Returns the coordinates of a user selected box in a warped view.

        **Note:**

        If the data view has a rotational (or other) warp, then the
        iGetBox_EMAP function returns only opposite diagonal points in the
        box, not enough info to determine the other two corners. This
        function returns the exact coordinates of all four corners, calculated
        from the pixel locations.
        """
        ret_val, p3.value, p4.value, p5.value, p6.value, p7.value, p8.value, p9.value, p10.value = self._wrapper.get_box2(p2.encode(), p3.value, p4.value, p5.value, p6.value, p7.value, p8.value, p9.value, p10.value)
        return ret_val




    def get_grid(self, p2, p3, p4, p5, p6, p7, p8, p9):
        """
        Position and size a grid on a map.

        **Note:**

        If the input angle is :attr:`geosoft.gxapi.rDUMMY`, an extra step is inserted
        for the user to define the angle by drawing a line
        with the mouse.
        The output primary axis angle will always be in the
        range -90 < angle <= 90. The grid origin is shifted to
        whichever corner necessary to make this possible, while keeping
        the secondary axis at 90 degrees greater than the primary (
        going counter-clockwise).
        The coordinates are returned in the current User projection
        (See GetUserIPJ_MVIEW and SetUserIPJ_MVIEW.)
        """
        ret_val, p5.value, p6.value, p7.value, p8.value, p9.value = self._wrapper.get_grid(p2.encode(), p3, p4, p5.value, p6.value, p7.value, p8.value, p9.value)
        return ret_val




    def get_line(self, p2, p3, p4, p5, p6):
        """
        Returns the end points of a line.

        **Note:**

        The coordinates are returned in the current User projection
        (See GetUserIPJ_MVIEW and SetUserIPJ_MVIEW.)
        """
        ret_val, p3.value, p4.value, p5.value, p6.value = self._wrapper.get_line(p2.encode(), p3.value, p4.value, p5.value, p6.value)
        return ret_val




    def get_line_ex(self, p2, p3, p4, p5, p6):
        """
        Returns the end points of a line.

        **Note:**

        The coordinates are returned in the current User projection
        (See GetUserIPJ_MVIEW and SetUserIPJ_MVIEW.)
        """
        ret_val, p3.value, p4.value, p5.value, p6.value = self._wrapper.get_line_ex(p2.encode(), p3.value, p4.value, p5.value, p6.value)
        return ret_val




    def get_line_xyz(self, p2, p3, p4, p5, p6, p7, p8):
        """
        Returns the end points of a line in X,Y and Z

        **Note:**

        The coordinates are returned in the current User projection
        (See GetUserIPJ_MVIEW and SetUserIPJ_MVIEW.)
        This is useful for digitizing a line in an oriented view and getting
        the true coordinates in (X, Y, Z) at the selected point on the view plane.
        """
        ret_val, p3.value, p4.value, p5.value, p6.value, p7.value, p8.value = self._wrapper.get_line_xyz(p2.encode(), p3.value, p4.value, p5.value, p6.value, p7.value, p8.value)
        return ret_val




    def get_point(self, p2, p3, p4):
        """
        Returns the coordinates of a user selected point.

        **Note:**

        This will wait for user to select a point.
        """
        ret_val, p3.value, p4.value = self._wrapper.get_point(p2.encode(), p3.value, p4.value)
        return ret_val




    def get_point_ex(self, p2, p3, p4):
        """
        Returns the coordinates of a user selected point.

        **Note:**

        This will wait for user to select a point.
        """
        ret_val, p3.value, p4.value = self._wrapper.get_point_ex(p2.encode(), p3.value, p4.value)
        return ret_val




    def get_point_3d(self, p2, p3, p4, p5):
        """
        Returns the coordinates of a user selected point.

        **Note:**

        This will wait for user to select a point.
        """
        ret_val, p3.value, p4.value, p5.value = self._wrapper.get_point_3d(p2.encode(), p3.value, p4.value, p5.value)
        return ret_val




    def get_poly_line(self, p2, p3, p4):
        """
        Returns a polyline.

        **Note:**

        The coordinates are returned in the current User projection
        (See GetUserIPJ_MVIEW and SetUserIPJ_MVIEW.)
        """
        ret_val = self._wrapper.get_poly_line(p2.encode(), p3._wrapper, p4._wrapper)
        return ret_val




    def get_poly_line_xyz(self, p2, p3, p4, p5):
        """
        Returns a polyline.

        **Note:**

        The coordinates are returned in the current User projection
        (See GetUserIPJ_MVIEW and SetUserIPJ_MVIEW.) In this version
        of the method X, Y and Z (depth) are returned. Initially created
        to deal with crooked sections.
        """
        ret_val = self._wrapper.get_poly_line_xyz(p2.encode(), p3._wrapper, p4._wrapper, p5._wrapper)
        return ret_val




    def get_rect(self, p2, p3, p4, p5, p6):
        """
        Returns the coordinates of a user selected box starting at a corner.

        **Note:**

        The coordinates are returned in the current User projection
        (See GetUserIPJ_MVIEW and SetUserIPJ_MVIEW.)
        If the user :class:`geosoft.gxapi.GXIPJ` distorts the coordinates from being rectilinear
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
        ret_val, p3.value, p4.value, p5.value, p6.value = self._wrapper.get_rect(p2.encode(), p3.value, p4.value, p5.value, p6.value)
        return ret_val




    def track_point(self, p2, p3, p4):
        """
        Get point without prompt or cursor change with tracking
        """
        ret_val, p3.value, p4.value = self._wrapper.track_point(p2, p3.value, p4.value)
        return ret_val




# Map Viewport Mode Methods



    def get_aoi_area(self, p2, p3, p4, p5):
        """
        Get the area of interest.

        **Note:**

        Coordinates are based on the current view units.
        """
        p2.value, p3.value, p4.value, p5.value = self._wrapper.get_aoi_area(p2.value, p3.value, p4.value, p5.value)
        




    def set_aoi_area(self, p2, p3, p4, p5):
        """
        Set the area of interest.

        **Note:**

        Coordinates are based on the current view user units.
        The map is immediatly redrawn.
        """
        self._wrapper.set_aoi_area(p2, p3, p4, p5)
        




    def set_viewport_mode(self, p2):
        """
        Set the viewport mode.

        **Note:**

        This is handy for using a map to define an area of interest. Use in conjunction
        with Get/Set AOIArea. If this is used inside montaj it is important to set or provide
        for a method to set the map mode back to normal as this is not exposed in the interface.
        """
        self._wrapper.set_viewport_mode(p2)
        




# Tracking Methods



    def get_selected_vertices(self, p2, p3):
        """
        Get the verticies of selected object

        **Note:**

        Works only in Vertex Edit Mode
        """
        self._wrapper.get_selected_vertices(p2._wrapper, p3._wrapper)
        




# Virtual


    @classmethod
    def create_virtual(cls, p1):
        """
        Makes this :class:`geosoft.gxapi.GXEMAP` object the current active object to the user.
        """
        ret_val = gxapi_cy.WrapEMAP.create_virtual(GXContext._get_tls_geo(), p1.encode())
        return GXEMAP(ret_val)




# External Window


    @classmethod
    def load_control(cls, p1, p2):
        """
        Version of Load_EMAP that can be used to load a database via subclassing into a Windows control.
        """
        gxapi_cy.WrapEMAP.load_control(GXContext._get_tls_geo(), p1.encode(), p2)
        



    @classmethod
    def load_with_view_control(cls, p1, p2, p3):
        """
        Version of LoadWithView_EDB that can be used to load a database via subclassing into a Windows control.
        """
        gxapi_cy.WrapEMAP.load_with_view_control(GXContext._get_tls_geo(), p1.encode(), p2._wrapper, p3)
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer