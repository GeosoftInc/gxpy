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

    The :class:`geosoft.gxapi.GXEMAPTEMPLATE` class provides access to a map template as displayed within
    Oasis montaj, but does not change data within the template itself.
    It performs functions such as setting the currently displayed area,
    or drawing "tracking" lines or boxes on the template (which are not
    part of the template itself).

    **Note:**

    To obtain access to the map template itself, it is recommended practice
    to begin with an :class:`geosoft.gxapi.GXEMAPTEMPLATE` object, and use the Lock function to
    lock the underlying template to prevent external changes. The returned
    :class:`geosoft.gxapi.GXMAPTEMPLATE` object may then be safely used to make changes to the template itself.
    
    VIRTUAL :class:`geosoft.gxapi.GXEMAPTEMPLATE` SUPPORT
    
    These methods are only available when running in an external application.
    They allow the GX to open a map template and then create a Virtual :class:`geosoft.gxapi.GXEMAPTEMPLATE` from that
    map template. The GX can then call MakeCurrent and set the current :class:`geosoft.gxapi.GXEMAPTEMPLATE` so
    that code that follows sees this map template as the current :class:`geosoft.gxapi.GXMAPTEMPLATE`.
    
    Supported methods on Virtual EMAPTEMPLATEs are:
    
      Current_EMAPTEMPLATE
      CurrentNoActivate_EMAPTEMPLATE
      MakeCurrent_EMAPTEMPLATE
      iHaveCurrent_EMAPTEMPLATE
      CurrentIfExists_EMAPTEMPLATE
    
      Lock_EMAPTEMPLATE
      UnLock_EMAPTEMPLATE
    
      IGetName_EMAPTEMPLATE
    
      iLoaded_EMAPTEMPLATE
      Load_EMAPTEMPLATE
      LoadNoActivate_EMAPTEMPLATE
      UnLoadVerify_EMAPTEMPLATE
      UnLoad_EMAPTEMPLATE
    
      CreateVirtual_EMAPTEMPLATE
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
        A null (undefined) instance of :class:`geosoft.gxapi.GXEMAPTEMPLATE`
        
        :returns: A null :class:`geosoft.gxapi.GXEMAPTEMPLATE`
        """
        return cls()

    def is_null(self):
        """
        Check if the instance of :class:`geosoft.gxapi.GXEMAPTEMPLATE` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of :class:`geosoft.gxapi.GXEMAPTEMPLATE`, False otherwise.
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




    def set_drag_drop_enabled(self, p2):
        """
        Set whether drag-and-drop is enabled for the map.
        """
        self._wrapper.set_drag_drop_enabled(p2)
        




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

        This function acts just like Current_EMAPTEMPLATE except that the document is not activated (brought to foreground) and no
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
    def get_map_templates_lst(cls, p1, p2):
        """
        Load the file names of open maps into a :class:`geosoft.gxapi.GXLST`.
        """
        ret_val = gxapi_cy.WrapEMAPTEMPLATE.get_map_templates_lst(GXContext._get_tls_geo(), p1._wrapper, p2)
        return ret_val




    def get_name(self, p2):
        """
        Get the name of the map object of this :class:`geosoft.gxapi.GXEMAPTEMPLATE`.
        """
        p2.value = self._wrapper.get_name(p2.value.encode())
        



    @classmethod
    def have_current(cls):
        """
        This method returns whether a current map is loaded
        """
        ret_val = gxapi_cy.WrapEMAPTEMPLATE.have_current(GXContext._get_tls_geo())
        return ret_val



    @classmethod
    def i_get_specified_map_name(cls, p1, p2, p3):
        """
        Find a loaded map that has a setting in its reg.
        """
        ret_val, p3.value = gxapi_cy.WrapEMAPTEMPLATE.i_get_specified_map_name(GXContext._get_tls_geo(), p1.encode(), p2.encode(), p3.value.encode())
        return ret_val




    def is_locked(self):
        """
        Is this MapTemplate locked
        """
        ret_val = self._wrapper.is_locked()
        return ret_val



    @classmethod
    def loaded(cls, p1):
        """
        Returns 1 if a map is loaded .
        """
        ret_val = gxapi_cy.WrapEMAPTEMPLATE.loaded(GXContext._get_tls_geo(), p1.encode())
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
        




    def read_only(self):
        """
        Checks if a map is currently opened in a read-only mode.
        """
        ret_val = self._wrapper.read_only()
        return ret_val



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
        ret_val = gxapi_cy.WrapEMAPTEMPLATE.load(GXContext._get_tls_geo(), p1.encode())
        return GXEMAPTEMPLATE(ret_val)



    @classmethod
    def load_no_activate(cls, p1):
        """
        Loads documents into the workspace

        **Note:**

        This function acts just like Load_EMAPTEMPLATE except that the document(s) is not activated (brought to foreground) and no
        guarantee is given about which document is currently active.
        """
        ret_val = gxapi_cy.WrapEMAPTEMPLATE.load_no_activate(GXContext._get_tls_geo(), p1.encode())
        return GXEMAPTEMPLATE(ret_val)




    def lock(self):
        """
        This method locks the Edited map.
        """
        ret_val = self._wrapper.lock()
        return GXMAPTEMPLATE(ret_val)




    def make_current(self):
        """
        Makes this :class:`geosoft.gxapi.GXEMAPTEMPLATE` object the current active object to the user.
        """
        self._wrapper.make_current()
        



    @classmethod
    def un_load(cls, p1):
        """
        Unloads a map template.

        **Note:**

        If the map template is not loaded, nothing happens.
        Same as UnLoadVerify_EMAPTEMPLATE with FALSE to prompt save.
        """
        gxapi_cy.WrapEMAPTEMPLATE.un_load(GXContext._get_tls_geo(), p1.encode())
        



    @classmethod
    def un_load_all(cls):
        """
        Unloads all opened maps
        """
        gxapi_cy.WrapEMAPTEMPLATE.un_load_all(GXContext._get_tls_geo())
        



    @classmethod
    def un_load_verify(cls, p1, p2):
        """
        Unloads an edited map, optional prompt to save.

        **Note:**

        If the map is not loaded, nothing happens.
        If "FALSE", map is saved without a prompt.
        """
        gxapi_cy.WrapEMAPTEMPLATE.un_load_verify(GXContext._get_tls_geo(), p1.encode(), p2)
        




    def un_lock(self):
        """
        This method unlocks the Edited map.
        """
        self._wrapper.un_lock()
        




# Input



    def get_box(self, p2, p3, p4, p5, p6):
        """
        Returns the coordinates of a user selected box.

        **Note:**

        The coordinates are returned in the current template units
        (See GetUnits and SetUnits in :class:`geosoft.gxapi.GXMAPTEMPLATE`)
        """
        ret_val, p3.value, p4.value, p5.value, p6.value = self._wrapper.get_box(p2.encode(), p3.value, p4.value, p5.value, p6.value)
        return ret_val




    def get_line(self, p2, p3, p4, p5, p6):
        """
        Returns the end points of a line.

        **Note:**

        The coordinates are returned in the current template units
        (See GetUnits and SetUnits in :class:`geosoft.gxapi.GXMAPTEMPLATE`)
        """
        ret_val, p3.value, p4.value, p5.value, p6.value = self._wrapper.get_line(p2.encode(), p3.value, p4.value, p5.value, p6.value)
        return ret_val




    def get_point(self, p2, p3, p4):
        """
        Returns the coordinates of a user selected point.

        **Note:**

        The coordinates are returned in the current template units
        (See GetUnits and SetUnits in :class:`geosoft.gxapi.GXMAPTEMPLATE`)
        """
        ret_val, p3.value, p4.value = self._wrapper.get_point(p2.encode(), p3.value, p4.value)
        return ret_val




    def get_rect(self, p2, p3, p4, p5, p6):
        """
        Returns the coordinates of a user selected box starting at a corner.

        **Note:**

        The coordinates are returned in the current template units
        (See GetUnits and SetUnits in :class:`geosoft.gxapi.GXMAPTEMPLATE`)
        """
        ret_val, p3.value, p4.value, p5.value, p6.value = self._wrapper.get_rect(p2.encode(), p3.value, p4.value, p5.value, p6.value)
        return ret_val




    def track_point(self, p2, p3, p4):
        """
        Get point without prompt or cursor change with tracking
        """
        ret_val, p3.value, p4.value = self._wrapper.track_point(p2, p3.value, p4.value)
        return ret_val




# Selection Methods



    def get_item_selection(self, p2):
        """
        Gets info about the current selected item

        **Note:**

        If nothing is selected the string will be empty and the function will return :attr:`geosoft.gxapi.GS_FALSE`;
        """
        ret_val, p2.value = self._wrapper.get_item_selection(p2.value.encode())
        return ret_val




    def set_item_selection(self, p2):
        """
        Sets the current selected item

        **Note:**

        An empty string will unselect everything.
        """
        self._wrapper.set_item_selection(p2.encode())
        




# View Window



    def get_display_area(self, p2, p3, p4, p5):
        """
        Get the area you are currently looking at.

        **Note:**

        The coordinates are based on the current template units
        (See GetUnits and SetUnits in :class:`geosoft.gxapi.GXMAPTEMPLATE`)
        """
        p2.value, p3.value, p4.value, p5.value = self._wrapper.get_display_area(p2.value, p3.value, p4.value, p5.value)
        




    def get_template_layout_props(self, p2, p3, p4, p5, p6, p7, p8, p9):
        """
        Get the base layout view properties.

        **Note:**

        This affects the display units and other related properties for the base
        view of a map.
        """
        p2.value, p3.value, p4.value, p5.value, p6.value, p7.value, p8.value, p9.value = self._wrapper.get_template_layout_props(p2.value, p3.value, p4.value, p5.value, p6.value, p7.value, p8.value, p9.value)
        




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

        The coordinates are based on the current template units
        (See GetUnits and SetUnits in :class:`geosoft.gxapi.GXMAPTEMPLATE`)
        """
        self._wrapper.set_display_area(p2, p3, p4, p5)
        




    def set_template_layout_props(self, p2, p3, p4, p5, p6, p7, p8, p9):
        """
        Set the base layout view properties.

        **Note:**

        This affects the display units and other related properties for the base
        view of a map.
        """
        self._wrapper.set_template_layout_props(p2, p3, p4, p5, p6, p7, p8, p9)
        




    def set_window_state(self, p2):
        """
        Changes the state of the map window
        """
        self._wrapper.set_window_state(p2)
        




# Virtual


    @classmethod
    def create_virtual(cls, p1):
        """
        Makes this :class:`geosoft.gxapi.GXEMAPTEMPLATE` object the current active object to the user.
        """
        ret_val = gxapi_cy.WrapEMAPTEMPLATE.create_virtual(GXContext._get_tls_geo(), p1.encode())
        return GXEMAPTEMPLATE(ret_val)





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer