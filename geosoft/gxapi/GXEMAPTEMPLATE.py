### extends 'class_empty.py'
### block ClassImports
# NOTICE: Do not edit anything here, it is generated code
from . import gxapi_cy
from geosoft.gxapi import GXContext, float_ref, int_ref, str_ref
from .GXMAPTEMPLATE import GXMAPTEMPLATE


### endblock ClassImports

### block Header
# NOTICE: The code generator will not replace the code in this block
### endblock Header

### block ClassImplementation
# NOTICE: Do not edit anything here, it is generated code
class GXEMAPTEMPLATE(gxapi_cy.WrapEMAPTEMPLATE):
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

    def __init__(self, handle=0):
        super(GXEMAPTEMPLATE, self).__init__(GXContext._get_tls_geo(), handle)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of `GXEMAPTEMPLATE <geosoft.gxapi.GXEMAPTEMPLATE>`
        
        :returns: A null `GXEMAPTEMPLATE <geosoft.gxapi.GXEMAPTEMPLATE>`
        :rtype:   GXEMAPTEMPLATE
        """
        return GXEMAPTEMPLATE()

    def is_null(self):
        """
        Check if this is a null (undefined) instance
        
        :returns: True if this is a null (undefined) instance, False otherwise.
        :rtype:   bool
        """
        return self._internal_handle() == 0



# Drag-and-drop methods



    def drag_drop_enabled(self):
        """
        Checks if drag-and-drop is enabled for the map
        
        :rtype:               bool

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.
        """
        ret_val = self._drag_drop_enabled()
        return ret_val




    def set_drag_drop_enabled(self, enable):
        """
        Set whether drag-and-drop is enabled for the map.
        
        :param enable:        Enables/disables drag-and-drop
        :type  enable:        bool

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.
        """
        self._set_drag_drop_enabled(enable)
        




# General


    @classmethod
    def current(cls):
        """
        This method returns the Current Edited map template.
        

        :returns:    `GXEMAPTEMPLATE <geosoft.gxapi.GXEMAPTEMPLATE>` Object
        :rtype:      GXEMAPTEMPLATE

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.
        """
        ret_val = gxapi_cy.WrapEMAPTEMPLATE._current(GXContext._get_tls_geo())
        return GXEMAPTEMPLATE(ret_val)



    @classmethod
    def current_no_activate(cls):
        """
        This method returns the Current Edited map template.
        

        :returns:    `GXEMAPTEMPLATE <geosoft.gxapi.GXEMAPTEMPLATE>` Object
        :rtype:      GXEMAPTEMPLATE

        .. versionadded:: 9.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.

        **Note:** This function acts just like `current <geosoft.gxapi.GXEMAPTEMPLATE.current>` except that the document is not activated (brought to foreground) and no
        guarantee is given about which document is currently active.
        """
        ret_val = gxapi_cy.WrapEMAPTEMPLATE._current_no_activate(GXContext._get_tls_geo())
        return GXEMAPTEMPLATE(ret_val)



    @classmethod
    def current_if_exists(cls):
        """
        This method returns the Current Edited map.
        

        :returns:    `GXEMAPTEMPLATE <geosoft.gxapi.GXEMAPTEMPLATE>` Object to current edited map. If there is no current map,
                  the user is not prompted for a map, and 0 is returned.
        :rtype:      GXEMAPTEMPLATE

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.
        """
        ret_val = gxapi_cy.WrapEMAPTEMPLATE._current_if_exists(GXContext._get_tls_geo())
        return GXEMAPTEMPLATE(ret_val)





    @classmethod
    def get_map_templates_lst(cls, lst, path):
        """
        Load the file names of open maps into a `GXLST <geosoft.gxapi.GXLST>`.
        
        :param lst:   `GXLST <geosoft.gxapi.GXLST>` to load
        :param path:  :ref:`EMAPTEMPLATE_PATH`
        :type  lst:   GXLST
        :type  path:  int

        :returns:     The number of documents loaded into the `GXLST <geosoft.gxapi.GXLST>`.
                      The `GXLST <geosoft.gxapi.GXLST>` is cleared first.
        :rtype:       int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.
        """
        ret_val = gxapi_cy.WrapEMAPTEMPLATE._get_map_templates_lst(GXContext._get_tls_geo(), lst, path)
        return ret_val




    def get_name(self, name):
        """
        Get the name of the map object of this `GXEMAPTEMPLATE <geosoft.gxapi.GXEMAPTEMPLATE>`.
        
        :param name:          Name returned
        :type  name:          str_ref

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
        ret_val = gxapi_cy.WrapEMAPTEMPLATE._have_current(GXContext._get_tls_geo())
        return ret_val



    @classmethod
    def i_get_specified_map_name(cls, field, value, name):
        """
        Find a loaded map that has a setting in its reg.
        
        :param field:  `GXREG <geosoft.gxapi.GXREG>` field name
        :param value:  `GXREG <geosoft.gxapi.GXREG>` field value to find
        :param name:   buffer for map name
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
        ret_val, name.value = gxapi_cy.WrapEMAPTEMPLATE._i_get_specified_map_name(GXContext._get_tls_geo(), field.encode(), value.encode(), name.value.encode())
        return ret_val




    def is_locked(self):
        """
        Is this MapTemplate locked
        
        :rtype:               bool

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
        
        :param name:  map name
        :type  name:  str

        :returns:     1 if map is loaded, 0 otherwise.
        :rtype:       int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.
        """
        ret_val = gxapi_cy.WrapEMAPTEMPLATE._loaded(GXContext._get_tls_geo(), name.encode())
        return ret_val




    def get_window_position(self, left, top, right, bottom, state, is_floating):
        """
        Get the map window's position and dock state
        
        :param left:          Window left position
        :param top:           Window top position
        :param right:         Window right position
        :param bottom:        Window bottom position
        :param state:         Window state :ref:`EMAPTEMPLATE_WINDOW_STATE`
        :param is_floating:   Docked or floating :ref:`EMAPTEMPLATE_WINDOW_POSITION`
        :type  left:          int_ref
        :type  top:           int_ref
        :type  right:         int_ref
        :type  bottom:        int_ref
        :type  state:         int_ref
        :type  is_floating:   int_ref

        .. versionadded:: 9.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.
        """
        left.value, top.value, right.value, bottom.value, state.value, is_floating.value = self._get_window_position(left.value, top.value, right.value, bottom.value, state.value, is_floating.value)
        




    def set_window_position(self, left, top, right, bottom, state, is_floating):
        """
        Get the map window's position and dock state
        
        :param left:          Window left position
        :param top:           Window top position
        :param right:         Window right position
        :param bottom:        Window bottom position
        :param state:         Window state :ref:`EMAPTEMPLATE_WINDOW_STATE`
        :param is_floating:   Docked or floating :ref:`EMAPTEMPLATE_WINDOW_POSITION`
        :type  left:          int
        :type  top:           int
        :type  right:         int
        :type  bottom:        int
        :type  state:         int
        :type  is_floating:   int

        .. versionadded:: 9.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.
        """
        self._set_window_position(left, top, right, bottom, state, is_floating)
        




    def read_only(self):
        """
        Checks if a map is currently opened in a read-only mode.
        
        :rtype:               bool

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.
        """
        ret_val = self._read_only()
        return ret_val



    @classmethod
    def load(cls, name):
        """
        Loads maps into the editor.
        
        :param name:  list of maps (';' or '|' delimited) to load.
        :type  name:  str

        :returns:     `GXEMAPTEMPLATE <geosoft.gxapi.GXEMAPTEMPLATE>` Object to edited map.
        :rtype:       GXEMAPTEMPLATE

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.

        **Note:** The last map in the list will be the current map.

        Maps may already be loaded.

        Only the first file in the list may have a directory path.
        All other files in the list are assumed to be in the same
        directory as the first file.
        """
        ret_val = gxapi_cy.WrapEMAPTEMPLATE._load(GXContext._get_tls_geo(), name.encode())
        return GXEMAPTEMPLATE(ret_val)



    @classmethod
    def load_no_activate(cls, name):
        """
        Loads documents into the workspace
        
        :param name:  List of documents (';' or '|' delimited) to load.
        :type  name:  str

        :returns:     Handle to current edited document, which will be the last
                      database in the list if multiple files were provided.
        :rtype:       GXEMAPTEMPLATE

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.

        **Note:** This function acts just like `load <geosoft.gxapi.GXEMAPTEMPLATE.load>` except that the document(s) is not activated (brought to foreground) and no
        guarantee is given about which document is currently active.
        """
        ret_val = gxapi_cy.WrapEMAPTEMPLATE._load_no_activate(GXContext._get_tls_geo(), name.encode())
        return GXEMAPTEMPLATE(ret_val)




    def lock(self):
        """
        This method locks the Edited map.
        

        :returns:             `GXMAPTEMPLATE <geosoft.gxapi.GXMAPTEMPLATE>` Object to map associated with edited map.
        :rtype:               GXMAPTEMPLATE

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.
        """
        ret_val = self._lock()
        return GXMAPTEMPLATE(ret_val)




    def make_current(self):
        """
        Makes this `GXEMAPTEMPLATE <geosoft.gxapi.GXEMAPTEMPLATE>` object the current active object to the user.
        

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.
        """
        self._make_current()
        



    @classmethod
    def un_load(cls, name):
        """
        Unloads a map template.
        
        :param name:  Name of the map to unload
        :type  name:  str

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.

        **Note:** If the map template is not loaded, nothing happens.
        Same as `un_load_verify <geosoft.gxapi.GXEMAPTEMPLATE.un_load_verify>` with FALSE to prompt save.
        """
        gxapi_cy.WrapEMAPTEMPLATE._un_load(GXContext._get_tls_geo(), name.encode())
        



    @classmethod
    def un_load_all(cls):
        """
        Unloads all opened maps
        

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.
        """
        gxapi_cy.WrapEMAPTEMPLATE._un_load_all(GXContext._get_tls_geo())
        



    @classmethod
    def un_load_verify(cls, name, prompt):
        """
        Unloads an edited map, optional prompt to save.
        
        :param name:    Name of map to unload
        :param prompt:  prompt
        :type  name:    str
        :type  prompt:  bool

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.

        **Note:** If the map is not loaded, nothing happens.
        If "FALSE", map is saved without a prompt.
        """
        gxapi_cy.WrapEMAPTEMPLATE._un_load_verify(GXContext._get_tls_geo(), name.encode(), prompt)
        




    def un_lock(self):
        """
        This method unlocks the Edited map.
        

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.
        """
        self._un_lock()
        




# Input



    def get_box(self, state, min_x, min_y, max_x, max_y):
        """
        Returns the coordinates of a user selected box.
        
        :param state:         user prompt string
        :param min_x:         X minimum in current view user units.
        :param min_y:         Y minimum in current view user units.
        :param max_x:         X maximum in current view user units.
        :param max_y:         Y maximum in current view user units.
        :type  state:         str
        :type  min_x:         float_ref
        :type  min_y:         float_ref
        :type  max_x:         float_ref
        :type  max_y:         float_ref

        :returns:             0 if point returned.
                              1 if user cancelled.
        :rtype:               int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.

        **Note:** The coordinates are returned in the current template units
        (See GetUnits and SetUnits in `GXMAPTEMPLATE <geosoft.gxapi.GXMAPTEMPLATE>`)
        """
        ret_val, min_x.value, min_y.value, max_x.value, max_y.value = self._get_box(state.encode(), min_x.value, min_y.value, max_x.value, max_y.value)
        return ret_val




    def get_line(self, str_val, min_x, min_y, max_x, max_y):
        """
        Returns the end points of a line.
        
        :param str_val:       user prompt string
        :param min_x:         X1 in view user units
        :param min_y:         Y1
        :param max_x:         X2
        :param max_y:         Y2
        :type  str_val:       str
        :type  min_x:         float_ref
        :type  min_y:         float_ref
        :type  max_x:         float_ref
        :type  max_y:         float_ref

        :returns:             0 if line returned.
                              1 if user cancelled.
        :rtype:               int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.

        **Note:** The coordinates are returned in the current template units
        (See GetUnits and SetUnits in `GXMAPTEMPLATE <geosoft.gxapi.GXMAPTEMPLATE>`)
        """
        ret_val, min_x.value, min_y.value, max_x.value, max_y.value = self._get_line(str_val.encode(), min_x.value, min_y.value, max_x.value, max_y.value)
        return ret_val




    def get_point(self, str_val, x, y):
        """
        Returns the coordinates of a user selected point.
        
        :param str_val:       user prompt string
        :param x:             X coordinate in current view user units.
        :param y:             Y
        :type  str_val:       str
        :type  x:             float_ref
        :type  y:             float_ref

        :returns:             0 if point returned.
                              1 if user cancelled.
        :rtype:               int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.

        **Note:** The coordinates are returned in the current template units
        (See GetUnits and SetUnits in `GXMAPTEMPLATE <geosoft.gxapi.GXMAPTEMPLATE>`)
        """
        ret_val, x.value, y.value = self._get_point(str_val.encode(), x.value, y.value)
        return ret_val




    def get_rect(self, str_val, min_x, min_y, max_x, max_y):
        """
        Returns the coordinates of a user selected box starting at a corner.
        
        :param str_val:       user prompt string
        :param min_x:         X minimum in current view user units.   (defines corner)
        :param min_y:         Y
        :param max_x:         X maximum
        :param max_y:         Y
        :type  str_val:       str
        :type  min_x:         float_ref
        :type  min_y:         float_ref
        :type  max_x:         float_ref
        :type  max_y:         float_ref

        :returns:             0 if point returned.
                              1 if user cancelled.
        :rtype:               int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.

        **Note:** The coordinates are returned in the current template units
        (See GetUnits and SetUnits in `GXMAPTEMPLATE <geosoft.gxapi.GXMAPTEMPLATE>`)
        """
        ret_val, min_x.value, min_y.value, max_x.value, max_y.value = self._get_rect(str_val.encode(), min_x.value, min_y.value, max_x.value, max_y.value)
        return ret_val




    def track_point(self, flags, x, y):
        """
        Get point without prompt or cursor change with tracking
        
        :param flags:         :ref:`EMAPTEMPLATE_TRACK`
        :param x:             X coordinate in current view user units.
        :param y:             Y
        :type  flags:         int
        :type  x:             float_ref
        :type  y:             float_ref

        :returns:             0 if point returned.
                              1 if user cancelled.
        :rtype:               int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.
        """
        ret_val, x.value, y.value = self._track_point(flags, x.value, y.value)
        return ret_val




# Selection Methods



    def get_item_selection(self, item):
        """
        Gets info about the current selected item
        
        :param item:          returned item name
        :type  item:          str_ref

        :returns:             Returns ``True`` if the item is a view
        :rtype:               bool

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Limitations:** May not be available while executing a command line program.

        **Note:** If nothing is selected the string will be empty and the function will return ``False``
        """
        ret_val, item.value = self._get_item_selection(item.value.encode())
        return ret_val




    def set_item_selection(self, item):
        """
        Sets the current selected item
        
        :param item:          item name
        :type  item:          str

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Limitations:** May not be available while executing a command line program.

        **Note:** An empty string will unselect everything.
        """
        self._set_item_selection(item.encode())
        




# View Window



    def get_display_area(self, min_x, min_y, max_x, max_y):
        """
        Get the area you are currently looking at.
        
        :param min_x:         X Min returned
        :param min_y:         Y Min returned
        :param max_x:         X Max returned
        :param max_y:         Y Max returned
        :type  min_x:         float_ref
        :type  min_y:         float_ref
        :type  max_x:         float_ref
        :type  max_y:         float_ref

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.

        **Note:** The coordinates are based on the current template units
        (See GetUnits and SetUnits in `GXMAPTEMPLATE <geosoft.gxapi.GXMAPTEMPLATE>`)
        """
        min_x.value, min_y.value, max_x.value, max_y.value = self._get_display_area(min_x.value, min_y.value, max_x.value, max_y.value)
        




    def get_template_layout_props(self, snap_to_grid, snap_dist, view_grid, view_rulers, view_units, grid_red, grid_green, grid_blue):
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
        snap_to_grid.value, snap_dist.value, view_grid.value, view_rulers.value, view_units.value, grid_red.value, grid_green.value, grid_blue.value = self._get_template_layout_props(snap_to_grid.value, snap_dist.value, view_grid.value, view_rulers.value, view_units.value, grid_red.value, grid_green.value, grid_blue.value)
        




    def get_window_state(self):
        """
        Retrieve the current state of the map window
        

        :returns:             :ref:`EMAPTEMPLATE_WINDOW_STATE`
        :rtype:               int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.
        """
        ret_val = self._get_window_state()
        return ret_val




    def set_display_area(self, min_x, min_y, max_x, max_y):
        """
        Set the area you wish to see.
        
        :param min_x:         X Min
        :param min_y:         Y Min
        :param max_x:         X Max
        :param max_y:         Y Max
        :type  min_x:         float
        :type  min_y:         float
        :type  max_x:         float
        :type  max_y:         float

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.

        **Note:** The coordinates are based on the current template units
        (See GetUnits and SetUnits in `GXMAPTEMPLATE <geosoft.gxapi.GXMAPTEMPLATE>`)
        """
        self._set_display_area(min_x, min_y, max_x, max_y)
        




    def set_template_layout_props(self, snap_to_grid, snap_dist, view_grid, view_rulers, view_units, grid_red, grid_green, grid_blue):
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
        self._set_template_layout_props(snap_to_grid, snap_dist, view_grid, view_rulers, view_units, grid_red, grid_green, grid_blue)
        




    def set_window_state(self, state):
        """
        Changes the state of the map window
        
        :param state:         :ref:`EMAPTEMPLATE_WINDOW_STATE`
        :type  state:         int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.
        """
        self._set_window_state(state)
        




# Virtual


    @classmethod
    def create_virtual(cls, name):
        """
        Makes this `GXEMAPTEMPLATE <geosoft.gxapi.GXEMAPTEMPLATE>` object the current active object to the user.
        
        :param name:  Name of map to create a virtual EMAMTEMPLATE from
        :type  name:  str

        :returns:     `GXEMAPTEMPLATE <geosoft.gxapi.GXEMAPTEMPLATE>` Object
        :rtype:       GXEMAPTEMPLATE

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.
        """
        ret_val = gxapi_cy.WrapEMAPTEMPLATE._create_virtual(GXContext._get_tls_geo(), name.encode())
        return GXEMAPTEMPLATE(ret_val)





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer