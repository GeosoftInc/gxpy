### extends 'class_empty.py'
### block ClassImports
# NOTICE: Do not edit anything here, it is generated code
from . import gxapi_cy
from geosoft.gxapi import GXContext, float_ref, int_ref, str_ref


### endblock ClassImports

### block Header
# NOTICE: The code generator will not replace the code in this block
### endblock Header

### block ClassImplementation
# NOTICE: Do not edit anything here, it is generated code
class GXGUI(gxapi_cy.WrapGUI):
    """
    GXGUI class.

    These are graphical functions that typically create a
    dialog-style window for a specific function. Examples include
    file import wizards, and the Histogram and Scatter tools.
    """

    def __init__(self, handle=0):
        super().__init__(GXContext._get_tls_geo(), handle)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of `GXGUI <geosoft.gxapi.GXGUI>`
        
        :returns: A null `GXGUI <geosoft.gxapi.GXGUI>`
        :rtype:   GXGUI
        """
        return GXGUI()

    def is_null(self):
        """
        Check if this is a null (undefined) instance
        
        :returns: True if this is a null (undefined) instance, False otherwise.
        :rtype:   bool
        """
        return self._internal_handle() == 0



# Miscellaneous


    @classmethod
    def create_wnd_from_hwnd(cls, p1):
        """
        Create a standard WND object from an HWND.
        
        :param p1:  HWND Handle
        :type  p1:  int

        :returns:    x - WND object created
        :rtype:      int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.

        **Note:** The object returned must be destroyed by the
        destroy object call.
        """
        ret_val = gxapi_cy.WrapGUI._create_wnd_from_hwnd(GXContext._get_tls_geo(), p1)
        return ret_val



    @classmethod
    def fft2_spec_filter(cls, spec_file_name, con_file_name):
        """
        Interactive `GXFFT2 <geosoft.gxapi.GXFFT2>` radially averaged power spectrum filter
        
        :param spec_file_name:  Name of the input spectrum file
        :param con_file_name:   Name of the output control file
        :type  spec_file_name:  str
        :type  con_file_name:   str

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Limitations:** May not be available while executing a command line program.
        """
        gxapi_cy.WrapGUI._fft2_spec_filter(GXContext._get_tls_geo(), spec_file_name.encode(), con_file_name.encode())
        



    @classmethod
    def get_parent_wnd(cls):
        """
        Get the current parent window
        

        :returns:    Parent window.
        :rtype:      int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.
        """
        ret_val = gxapi_cy.WrapGUI._get_parent_wnd(GXContext._get_tls_geo())
        return ret_val



    @classmethod
    def get_printer_lst(cls, lst):
        """
        Gets a list of all printers.
        
        :param lst:  List to place into
        :type  lst:  GXLST

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Limitations:** May not be available while executing a command line program.
        """
        gxapi_cy.WrapGUI._get_printer_lst(GXContext._get_tls_geo(), lst)
        



    @classmethod
    def get_window_state(cls):
        """
        Retrieve the current state of the Oasis montaj window
        

        :returns:    :ref:`WINDOW_STATE`
        :rtype:      int

        .. versionadded:: 9.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.
        """
        ret_val = gxapi_cy.WrapGUI._get_window_state(GXContext._get_tls_geo())
        return ret_val



    @classmethod
    def set_window_state(cls, state):
        """
        Changes the state of the Oasis montaj window
        
        :param state:  :ref:`WINDOW_STATE`
        :type  state:  int

        .. versionadded:: 9.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.
        """
        gxapi_cy.WrapGUI._set_window_state(GXContext._get_tls_geo(), state)
        



    @classmethod
    def get_window_position(cls, left, top, right, bottom, state):
        """
        Get the Oasis montaj window's position state
        
        :param left:    Window left position
        :param top:     Window top position
        :param right:   Window right position
        :param bottom:  Window bottom position
        :param state:   Window state :ref:`WINDOW_STATE`
        :type  left:    int_ref
        :type  top:     int_ref
        :type  right:   int_ref
        :type  bottom:  int_ref
        :type  state:   int_ref

        .. versionadded:: 9.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.
        """
        left.value, top.value, right.value, bottom.value, state.value = gxapi_cy.WrapGUI._get_window_position(GXContext._get_tls_geo(), left.value, top.value, right.value, bottom.value, state.value)
        



    @classmethod
    def set_window_position(cls, left, top, right, bottom, state):
        """
        Get the Oasis montaj window's position and state
        
        :param left:    Window left position
        :param top:     Window top position
        :param right:   Window right position
        :param bottom:  Window bottom position
        :param state:   Window state :ref:`WINDOW_STATE`
        :type  left:    int
        :type  top:     int
        :type  right:   int
        :type  bottom:  int
        :type  state:   int

        .. versionadded:: 9.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.
        """
        gxapi_cy.WrapGUI._set_window_position(GXContext._get_tls_geo(), left, top, right, bottom, state)
        



    @classmethod
    def get_client_window_area(cls, min_x, min_y, max_x, max_y):
        """
        Get the location of the Oasis montaj client window.
        
        :param min_x:  X Min returned (0)
        :param min_y:  Y Min returned (0)
        :param max_x:  X Max returned (width)
        :param max_y:  Y Max returned (height)
        :type  min_x:  int_ref
        :type  min_y:  int_ref
        :type  max_x:  int_ref
        :type  max_y:  int_ref

        .. versionadded:: 9.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Limitations:** May not be available while executing a command line program.

        **Note:** Returns the coordinates of the client window area (where MDI document windows are placed).
        The returned coordinates are 0,0 for the minimum X and Y and the window width
        width and height for the maximum X and Y.
        """
        min_x.value, min_y.value, max_x.value, max_y.value = gxapi_cy.WrapGUI._get_client_window_area(GXContext._get_tls_geo(), min_x.value, min_y.value, max_x.value, max_y.value)
        



    @classmethod
    def grid_stat_hist(cls, grid_name):
        """
        Display Histogram of grid
        
        :param grid_name:  Name of the grid to get stats from
        :type  grid_name:  str

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Limitations:** May not be available while executing a command line program.
        """
        gxapi_cy.WrapGUI._grid_stat_hist(GXContext._get_tls_geo(), grid_name.encode())
        



    @classmethod
    def voxel_stat_hist(cls, vox_name):
        """
        Display Histogram of Voxel
        
        :param vox_name:  Name of the Voxel to get stats from
        :type  vox_name:  str

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Limitations:** May not be available while executing a command line program.
        """
        gxapi_cy.WrapGUI._voxel_stat_hist(GXContext._get_tls_geo(), vox_name.encode())
        



    @classmethod
    def color_form(cls, col, no_col):
        """
        Select a color.
        
        :param col:     Color (modified)
        :param no_col:  Ask about `C_TRANSPARENT <geosoft.gxapi.C_TRANSPARENT>` if white is selected (1: yes, 0: no)?
        :type  col:     int_ref
        :type  no_col:  int

        :returns:       0 - Ok
                        1 - Cancel
        :rtype:         int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.

        **Note:** Color value is set on input, and new value returned.
        If the input color type is `C_TRANSPARENT <geosoft.gxapi.C_TRANSPARENT>`, then the color
        is set to white, if any other type is input the output is
        guaranteed to be of the same type.

        If ``no_col`` is 1, then on exit, if white is
        selected, the user is prompted: 'Do you want white (Yes) or
        "None" (No) ?' and the color is converted as requested.
        If this is not the case, the `C_TRANSPARENT <geosoft.gxapi.C_TRANSPARENT>` is converted
        to white (if "Ok" is selected) and no choice is offered.
        """
        ret_val, col.value = gxapi_cy.WrapGUI._color_form(GXContext._get_tls_geo(), col.value, no_col)
        return ret_val



    @classmethod
    def color_transform(cls, itr, st):
        """
        Define an `GXITR <geosoft.gxapi.GXITR>` of up to 8 zones.
        
        :param itr:  `GXITR <geosoft.gxapi.GXITR>` object (modified)
        :param st:   `GXST <geosoft.gxapi.GXST>` object (input)
        :type  itr:  GXITR
        :type  st:   GXST

        :returns:    0 if OK
                     1 if user cancels
        :rtype:      int

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Limitations:** May not be available while executing a command line program.

        **Note:** The statistics object is required in order to determine
        data ranges, percentiles, etc. Create it using
        `GXST.create_exact <geosoft.gxapi.GXST.create_exact>`, or be sure to enable histogram statistics.
        """
        ret_val = gxapi_cy.WrapGUI._color_transform(GXContext._get_tls_geo(), itr, st)
        return ret_val



    @classmethod
    def coord_sys_wizard(cls, ipj, editable, mode, source_label, source):
        """
        Launch the coordinate system definition/display `GXGUI <geosoft.gxapi.GXGUI>`.
        
        :param ipj:           `GXIPJ <geosoft.gxapi.GXIPJ>` object
        :param editable:      Editable `GXIPJ <geosoft.gxapi.GXIPJ>` (0:No, 1:Yes)
        :param mode:          :ref:`COORDSYS_MODE`
        :param source_label:  Data source label
        :param source:        Data source
        :type  ipj:           GXIPJ
        :type  editable:      int
        :type  mode:          int
        :type  source_label:  str
        :type  source:        str

        :returns:             0 - Ok
                              1 - Cancel
        :rtype:               int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.

        **Note:** Launches the new GX.Net single-dialog coordinate system
        definition dialog. The input `GXIPJ <geosoft.gxapi.GXIPJ>` is modified on return
        if OK is selected (and the editable parameter is 1).
        The "Data source label" and "Data source" is information displayed
        in the dialog for the user to know where the `GXIPJ <geosoft.gxapi.GXIPJ>` came from (e.g. "Grid: X.grd")
        """
        ret_val = gxapi_cy.WrapGUI._coord_sys_wizard(GXContext._get_tls_geo(), ipj, editable, mode, source_label.encode(), source.encode())
        return ret_val



    @classmethod
    def coord_sys_wizard_licensed(cls, ipj, editable, mode, source_label, source):
        """
        Launch the coordinate system definition/display `GXGUI <geosoft.gxapi.GXGUI>`.
        
        :param ipj:           `GXIPJ <geosoft.gxapi.GXIPJ>` object
        :param editable:      Editable `GXIPJ <geosoft.gxapi.GXIPJ>` (0:No, 1:Yes)
        :param mode:          :ref:`COORDSYS_MODE`
        :param source_label:  Data source label
        :param source:        Data source
        :type  ipj:           GXIPJ
        :type  editable:      int
        :type  mode:          int
        :type  source_label:  str
        :type  source:        str

        :returns:             0 - Ok
                              1 - Cancel
        :rtype:               int

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Limitations:** May not be available while executing a command line program.

        **Note:** Same as `coord_sys_wizard_licensed <geosoft.gxapi.GXGUI.coord_sys_wizard_licensed>` but will always be editable. The other
        method is not editable in the viewer while this one is.
        """
        ret_val = gxapi_cy.WrapGUI._coord_sys_wizard_licensed(GXContext._get_tls_geo(), ipj, editable, mode, source_label.encode(), source.encode())
        return ret_val



    @classmethod
    def coord_sys_wizard_grid(cls, ipj, target_ipj, editable, mode, source_label, source, nx, ny, x0, y0, dx, dy, rot):
        """
        Launch the coordinate system definition/display `GXGUI <geosoft.gxapi.GXGUI>`.
        
        :param ipj:           Original grid `GXIPJ <geosoft.gxapi.GXIPJ>` object
        :param target_ipj:    Source (target) grid `GXIPJ <geosoft.gxapi.GXIPJ>` object. This is supplied so the modified orientation can be calculated and displayed.
        :param editable:      Editable `GXIPJ <geosoft.gxapi.GXIPJ>` (0:No, 1:Yes)
        :param mode:          :ref:`COORDSYS_MODE`
        :param source_label:  Data source label
        :param source:        Data source
        :param nx:            Number of cells in X
        :param ny:            Number of cells in Y
        :param x0:            Grid orgin X (grid's own coordinate system)
        :param y0:            Grid orgin Y (grid's own coordinate system)
        :param dx:            Grid cell size X
        :param dy:            Grid cell size Y
        :param rot:           Grid rotation angle (degrees CCW)
        :type  ipj:           GXIPJ
        :type  target_ipj:    GXIPJ
        :type  editable:      int
        :type  mode:          int
        :type  source_label:  str
        :type  source:        str
        :type  nx:            int
        :type  ny:            int
        :type  x0:            float_ref
        :type  y0:            float_ref
        :type  dx:            float_ref
        :type  dy:            float_ref
        :type  rot:           float_ref

        :returns:             0 - Ok
                              1 - Cancel
        :rtype:               int

        .. versionadded:: 9.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.

        **Note:** Same as `coord_sys_wizard_licensed <geosoft.gxapi.GXGUI.coord_sys_wizard_licensed>` but allows the original grid info to be adjusted
        when projections on section or oriented plan grids are modified.
        In the tool, it is the "modified" orientation required to keep the edited projection's grid
        in the same location as it was in the target projection.
        """
        ret_val, x0.value, y0.value, dx.value, dy.value, rot.value = gxapi_cy.WrapGUI._coord_sys_wizard_grid(GXContext._get_tls_geo(), ipj, target_ipj, editable, mode, source_label.encode(), source.encode(), nx, ny, x0.value, y0.value, dx.value, dy.value, rot.value)
        return ret_val



    @classmethod
    def database_type(cls, name, type):
        """
        Returns the type string of an external DAO database.
        
        :param name:  File Name
        :param type:  Database type (returned)
        :type  name:  str
        :type  type:  str_ref

        :returns:     0 - OK
                      -1 - Cancel
                      terminates on error
        :rtype:       int

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Limitations:** May not be available while executing a command line program.

        **Note:** If the file extension is "mdb", then an MSJET (Microsoft Access)
        database is assumed. If the file name is "ODBC", then "ODBC" is
        returned as the type. Otherwise, a dialog appears listing the
        other valid DAO database types.
        """
        ret_val, type.value = gxapi_cy.WrapGUI._database_type(GXContext._get_tls_geo(), name.encode(), type.value.encode())
        return ret_val



    @classmethod
    def datamine_type(cls, file, type):
        """
        Returns the type of a Datamine file.
        
        :param file:  File Name (for display purposes only)
        :type  file:  str
        :type  type:  int_ref

        :returns:     0 - OK
                      -1 - Cancel
        :rtype:       int

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Limitations:** May not be available while executing a command line program.

        **Note:** Often, a Datamine file can be opened a number of different ways
        (e.g. as a string file or a as wireframe (point) file.
        The following function checks to see if there is a choice to be made
        between types supported by Geosoft for import. If not, it just returns
        the original type "hint" from Datamine. If there is a choice, it puts up
        a dialog with the choices for the user to pick from.
        Do a bit-wise AND with the returned type to determine the file type
        (or the type selected).

        Currently supported overlapping types/choices:

        dmString
        dmWireframePoint
        """
        ret_val, type.value = gxapi_cy.WrapGUI._datamine_type(GXContext._get_tls_geo(), file.encode(), type.value)
        return ret_val



    @classmethod
    def export_xyz_template_editor(cls, db, template, size):
        """
        Allows the user to edit XYZ export template
        using a complex dialog. The Template name
        may change during editing.
        
        :param db:        Database
        :param template:  Name of the Template (can change)
        :param size:      Size of the Template
        :type  db:        GXDB
        :type  template:  str
        :type  size:      int

        :returns:         0 - OK
                          1 - Error
        :rtype:           int

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Limitations:** May not be available while executing a command line program.

        **Note:** Only uses the current `GXDB <geosoft.gxapi.GXDB>`. This function does
        not exactly work as supposed to. Instead of using
        the `GXEDB <geosoft.gxapi.GXEDB>` handle passed to it, it only will use
        the current `GXDB <geosoft.gxapi.GXDB>`. Please see ExportXYXTemplateEditorEx_GUI
        for an updated function.
        """
        ret_val = gxapi_cy.WrapGUI._export_xyz_template_editor(GXContext._get_tls_geo(), db, template.encode(), size)
        return ret_val



    @classmethod
    def export_xyz_template_editor_ex(cls, edb, template):
        """
        Allows the user to edit an XYZ export template
        using a complex dialog. The template name
        may change during editing.
        
        :param edb:       `GXEDB <geosoft.gxapi.GXEDB>` object
        :param template:  Template name
        :type  edb:       GXEDB
        :type  template:  str_ref

        :returns:         0 - OK
                          1 - Error
        :rtype:           int

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Limitations:** May not be available while executing a command line program.
        """
        ret_val, template.value = gxapi_cy.WrapGUI._export_xyz_template_editor_ex(GXContext._get_tls_geo(), edb, template.value.encode())
        return ret_val



    @classmethod
    def file_filter_index(cls, filter):
        """
        Return the FILE_FILTER_XXX value for a file filter string.
        
        :param filter:  Input filter string
        :type  filter:  str

        :returns:       :ref:`FILE_FILTER`, -1 if not found
        :rtype:         int

        .. versionadded:: 7.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** For example, if "Database (``*.gdb``)" is input,
        then the `FILE_FILTER_GDB <geosoft.gxapi.FILE_FILTER_GDB>` value is returned.
        """
        ret_val = gxapi_cy.WrapGUI._file_filter_index(GXContext._get_tls_geo(), filter.encode())
        return ret_val



    @classmethod
    def gcs_datum_warning_shp(cls, data_source, ipj):
        """
        Launch the GCS Datum Warning dialog for `GXSHP <geosoft.gxapi.GXSHP>` files.
        
        :param data_source:  Data source
        :param ipj:          `GXIPJ <geosoft.gxapi.GXIPJ>` object
        :type  data_source:  str
        :type  ipj:          GXIPJ

        :returns:            0 - Ok
                             1 - Cancel
        :rtype:              int

        .. versionadded:: 7.1

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Runs the GCS Warning dialog with one data source
        """
        ret_val = gxapi_cy.WrapGUI._gcs_datum_warning_shp(GXContext._get_tls_geo(), data_source.encode(), ipj)
        return ret_val



    @classmethod
    def gcs_datum_warning_shpdb_ex(cls, source_lst, datum_from_lst, ldtlst, db):
        """
        Launch the GCS Datum Warning dialog for `GXSHP <geosoft.gxapi.GXSHP>` files (Database).
        
        :param source_lst:      Data source names
        :param datum_from_lst:  Corresponding datum names
        :param ldtlst:          Returned corresponding LDT names
        :type  source_lst:      GXLST
        :type  datum_from_lst:  GXLST
        :type  ldtlst:          GXLST
        :type  db:              GXDB

        :returns:               0 - Ok
                                1 - Cancel
        :rtype:                 int

        .. versionadded:: 7.1

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Runs the GCS Warning dialog with multiple data sources (Database)
        """
        ret_val = gxapi_cy.WrapGUI._gcs_datum_warning_shpdb_ex(GXContext._get_tls_geo(), source_lst, datum_from_lst, ldtlst, db)
        return ret_val



    @classmethod
    def gcs_datum_warning_shp_ex(cls, source_lst, datum_from_lst, ldtlst, mview):
        """
        Launch the GCS Datum Warning dialog for `GXSHP <geosoft.gxapi.GXSHP>` files.
        
        :param source_lst:      Data source names
        :param datum_from_lst:  Corresponding datum names
        :param ldtlst:          Returned corresponding LDT names
        :type  source_lst:      GXLST
        :type  datum_from_lst:  GXLST
        :type  ldtlst:          GXLST
        :type  mview:           GXMVIEW

        :returns:               0 - Ok
                                1 - Cancel
        :rtype:                 int

        .. versionadded:: 7.1

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Runs the GCS Warning dialog with multiple data sources
        """
        ret_val = gxapi_cy.WrapGUI._gcs_datum_warning_shp_ex(GXContext._get_tls_geo(), source_lst, datum_from_lst, ldtlst, mview)
        return ret_val



    @classmethod
    def get_area_of_interest(cls, min_x, min_y, max_x, max_y, ply, ipj):
        """
        Get the current area of interest from the application.
        
        :param min_x:  AOI Area Min X
        :param min_y:  AOI Area Min Y
        :param max_x:  AOI Area Max X
        :param max_y:  AOI Area Max y
        :param ply:    AOI Bounding `GXPLY <geosoft.gxapi.GXPLY>` (Filled if available, otherwise empty)
        :param ipj:    AOI Bounding `GXIPJ <geosoft.gxapi.GXIPJ>`
        :type  min_x:  float_ref
        :type  min_y:  float_ref
        :type  max_x:  float_ref
        :type  max_y:  float_ref
        :type  ply:    GXPLY
        :type  ipj:    GXIPJ

        :returns:      :ref:`AOI_RETURN_STATE`
        :rtype:        int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.

        **Note:** Depending on what is currently visible on screen and
        the defined coordinate system the user may be prompted
        by a warning and optionaly cancel the process.
        """
        ret_val, min_x.value, min_y.value, max_x.value, max_y.value = gxapi_cy.WrapGUI._get_area_of_interest(GXContext._get_tls_geo(), min_x.value, min_y.value, max_x.value, max_y.value, ply, ipj)
        return ret_val



    @classmethod
    def get_area_of_interest_3d(cls, min_x, min_y, min_z, max_x, max_y, max_z, ply, ipj):
        """
        Get the current area of interest from the application in 3D.
        
        :param min_x:  AOI Area Min X
        :param min_y:  AOI Area Min Y
        :param min_z:  AOI Area Min Z
        :param max_x:  AOI Area Max X
        :param max_y:  AOI Area Max y
        :param max_z:  AOI Area Max Z
        :param ply:    AOI Bounding `GXPLY <geosoft.gxapi.GXPLY>` (Filled if available, otherwise empty)
        :param ipj:    AOI Bounding `GXIPJ <geosoft.gxapi.GXIPJ>`
        :type  min_x:  float_ref
        :type  min_y:  float_ref
        :type  min_z:  float_ref
        :type  max_x:  float_ref
        :type  max_y:  float_ref
        :type  max_z:  float_ref
        :type  ply:    GXPLY
        :type  ipj:    GXIPJ

        :returns:      :ref:`AOI_RETURN_STATE`
        :rtype:        int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.

        **Note:** Depending on what is currently visible on screen and
        the defined coordinate system the user may be prompted
        by a warning and optionaly cancel the process.
        """
        ret_val, min_x.value, min_y.value, min_z.value, max_x.value, max_y.value, max_z.value = gxapi_cy.WrapGUI._get_area_of_interest_3d(GXContext._get_tls_geo(), min_x.value, min_y.value, min_z.value, max_x.value, max_y.value, max_z.value, ply, ipj)
        return ret_val



    @classmethod
    def get_dat_defaults(cls, flags, open, ext, qual):
        """
        Return the user default extension and qualifier for grids/images.
        
        :param flags:  :ref:`DAT_TYPE`
        :param open:   :ref:`FILE_FORM`
        :param ext:    Returned default extension (e.g. "grd")
        :param qual:   Returned default qualifier (e.g. "GRD")
        :type  flags:  int
        :type  open:   int
        :type  ext:    str_ref
        :type  qual:   str_ref

        .. versionadded:: 7.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** The default grid/image filters are normally stored in
        "MONTAJ.DEFAULT_XGD_IN" and "MONTAJ.DEFAULT_XGD_OUT"

        If no filter is defined, or the filter is not found
        then "grd" and "GRD" are returned as the default extension
        and qualifier.
        """
        ext.value, qual.value = gxapi_cy.WrapGUI._get_dat_defaults(GXContext._get_tls_geo(), flags, open, ext.value.encode(), qual.value.encode())
        



    @classmethod
    def get_file_filter(cls, file_filter, filter, mask, ext, path):
        """
        Return the defined filter, mask, extension and directory for an input filter.
        
        :param file_filter:  :ref:`FILE_FILTER`
        :param filter:       Returned file filter string
        :param mask:         Returned file mask string
        :param ext:          Returned file extension
        :param path:         :ref:`GS_DIRECTORY` Returned directory.
        :type  file_filter:  int
        :type  filter:       str_ref
        :type  mask:         str_ref
        :type  ext:          str_ref
        :type  path:         int_ref

        .. versionadded:: 7.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Returns the four parts of the file filter;
        e.g. for `FILE_FILTER_GDB <geosoft.gxapi.FILE_FILTER_GDB>` it returns:

        Filter:    "Database (``*.gdb``)"
        Mask:      "``*.gdb``"
        Extension: "gdb"
        Directory: "`GS_DIRECTORY_NONE <geosoft.gxapi.GS_DIRECTORY_NONE>`"

        This function is useful for constuction open/save dialog
        file filters, especially in GX.Net functions.
        """
        filter.value, mask.value, ext.value, path.value = gxapi_cy.WrapGUI._get_file_filter(GXContext._get_tls_geo(), file_filter, filter.value.encode(), mask.value.encode(), ext.value.encode(), path.value)
        



    @classmethod
    def get_gs_directory(cls, path, dir):
        """
        Return the directory path for value of :ref:`GS_DIRECTORY`.
        
        :param path:  :ref:`GS_DIRECTORY` Returned directory.
        :param dir:   Returned directory path
        :type  path:  int
        :type  dir:   str_ref

        .. versionadded:: 7.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Works along with the `get_file_filter <geosoft.gxapi.GXGUI.get_file_filter>` function. Note that
        most values of FILE_FILTER_XXX will return `GS_DIRECTORY_NONE <geosoft.gxapi.GS_DIRECTORY_NONE>`,
        and give the current workspace directory.

        This function is useful for constuction open/save dialog
        file filters, especially in GX.Net functions.
        """
        dir.value = gxapi_cy.WrapGUI._get_gs_directory(GXContext._get_tls_geo(), path, dir.value.encode())
        



    @classmethod
    def browse_dir(cls, title, default, dir_path):
        """
        Browses for a specific directory.
        
        :param title:     Title of the Form
        :param default:   Default path (Can be "")
        :param dir_path:  Result Path Buffer (default on input)
        :type  title:     str
        :type  default:   str
        :type  dir_path:  str_ref

        :returns:         0 - Ok
                          1 - Cancel
        :rtype:           int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.
        """
        ret_val, dir_path.value = gxapi_cy.WrapGUI._browse_dir(GXContext._get_tls_geo(), title.encode(), default.encode(), dir_path.value.encode())
        return ret_val



    @classmethod
    def color_transform_ex(cls, itr, st, zones, load_save, file):
        """
        Define an `GXITR <geosoft.gxapi.GXITR>` of up to 12 zones, with file load/save buttons.
        
        :param itr:        `GXITR <geosoft.gxapi.GXITR>` object (modified)
        :param st:         `GXST <geosoft.gxapi.GXST>` object (input)
        :param zones:      Max number of zones (8 or 12)
        :param load_save:  Show file load/save buttons (TRUE or FALSE)?
        :param file:       Default color transform file name
        :type  itr:        GXITR
        :type  st:         GXST
        :type  zones:      int
        :type  load_save:  int
        :type  file:       str_ref

        :returns:          0 if OK
                           1 if user cancels
        :rtype:            int

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Limitations:** May not be available while executing a command line program.

        **Note:** The statistics object is required in order to determine
        data ranges, percentiles, etc. Create it using
        `GXST.create_exact <geosoft.gxapi.GXST.create_exact>`, or be sure to enable histogram statistics.
        The color transform file name is used as the default when the save
        button is pushed, and is updated both after the load and save buttons
        are pushed by the value input or selected by the user.
        """
        ret_val, file.value = gxapi_cy.WrapGUI._color_transform_ex(GXContext._get_tls_geo(), itr, st, zones, load_save, file.value.encode())
        return ret_val



    @classmethod
    def cumulative_percent(cls, file, itr):
        """
        Define a percent-based `GXITR <geosoft.gxapi.GXITR>` of up to 12 zones.
        
        :param file:  Default color transform file name
        :param itr:   `GXITR <geosoft.gxapi.GXITR>` object (returned)
        :type  file:  str_ref
        :type  itr:   GXITR

        :returns:     0 if OK
                      1 if user cancels
        :rtype:       int

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Limitations:** May not be available while executing a command line program.

        **Note:** The `GXITR <geosoft.gxapi.GXITR>` values are interpreted as cumulative percent values, using
        the "PERCENT=1" value in the `GXITR <geosoft.gxapi.GXITR>`'s `GXREG <geosoft.gxapi.GXREG>`.

        Note that processes using ITRs do not automatically know to convert between
        percent values and "actual" data values. The `GXREG <geosoft.gxapi.GXREG>` "PERCENT" value is simply
        a flag to indicate to a user that the values are intended to be in the range
        from 0 < x < 100. The `GXITR <geosoft.gxapi.GXITR>` should not, therefore, be applied directly to data
        unless that data is already given in percent.

        If the file name is defined on input, the initial `GXITR <geosoft.gxapi.GXITR>` will be loaded from it.
        If it is left blank, a default 5-color transform with
        The color transform file name is used as the default when the save
        button is pushed, and is updated both after the load and save buttons
        are pushed by the value input or selected by the user.
        """
        ret_val, file.value = gxapi_cy.WrapGUI._cumulative_percent(GXContext._get_tls_geo(), file.value.encode(), itr)
        return ret_val



    @classmethod
    def dat_file_form(cls, title, default, psz_file_path, type, validation_type, multi):
        """
        Grid and Image file Open/Save Form for Multiple/Single file selections
        
        :param title:            Title of the Form
        :param default:          Default value
        :param psz_file_path:    Where the file name(s) is returned
        :param type:             :ref:`DAT_TYPE`
        :param validation_type:  :ref:`FILE_FORM`
        :param multi:            Allow Multiple file selections = TRUE Single   file selections = FALSE
        :type  title:            str
        :type  default:          str
        :type  psz_file_path:    str_ref
        :type  type:             int
        :type  validation_type:  int
        :type  multi:            int

        :returns:                0 - Ok
                                 1 - Cancel
        :rtype:                  int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.

        **Note:** Remember to make the string size big enough for multiple file
        selections. In the case of multiple selections the names will be separated
        by a semicolon and only the first file will contain the full path.

        When using the multiple flag on any of these functions please be aware that
        the string returned will be in the format:
        drive:\\path1\\path2\\name.grid|name2.grid|name3.grid(QUALIFIERS)
        All grids are required to be of the same type.
        """
        ret_val, psz_file_path.value = gxapi_cy.WrapGUI._dat_file_form(GXContext._get_tls_geo(), title.encode(), default.encode(), psz_file_path.value.encode(), type, validation_type, multi)
        return ret_val



    @classmethod
    def gen_file_form(cls, title, filt_vv, filter, default, file_path, type, multi):
        """
        General file Open/Save Form for Multiple/Single file selections and multiple filter capability
        
        :param title:      Title of the Form
        :param filt_vv:    INT `GXVV <geosoft.gxapi.GXVV>` of file filters to use :ref:`FILE_FILTER` The first one is default, can pass (`GXVV <geosoft.gxapi.GXVV>`) 0 for to use next parameter.
        :param filter:     :ref:`FILE_FILTER` (ignored if parameter above is not zero)
        :param default:    Default value
        :param file_path:  Where the file name(s) is returned
        :param type:       :ref:`FILE_FORM`
        :param multi:      Allow Multiple file selections = TRUE Single   file selections = FALSE
        :type  title:      str
        :type  filt_vv:    GXVV
        :type  filter:     int
        :type  default:    str
        :type  file_path:  str_ref
        :type  type:       int
        :type  multi:      int

        :returns:          0 - Ok
                           1 - Cancel
        :rtype:            int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.

        **Note:** Remember to make the string size big enough for multiple file
        selections. In the case of multiple selections the names will be separated
        by a semicolon and only the first file will contain the full path.

        Defined Functions     The following four functions are handy defines and simply pass the appropriate
        parameter.

        iFileOpen_GUI
        iFileSave_GUI
        iMultiFileOpen_GUI
        iMultiFileSave_GUI
        """
        ret_val, file_path.value = gxapi_cy.WrapGUI._gen_file_form(GXContext._get_tls_geo(), title.encode(), filt_vv, filter, default.encode(), file_path.value.encode(), type, multi)
        return ret_val



    @classmethod
    def custom_file_form(cls, title, filter, default, file_path, type, multi):
        """
        General file Open/Save Form for Multiple/Single file selections and custom filter capability
        
        :param title:      Title of the Form
        :param filter:     Custom filter.
        :param default:    Default value
        :param file_path:  Where the file name(s) is returned
        :param type:       :ref:`FILE_FORM`
        :param multi:      Allow Multiple file selections = TRUE Single   file selections = FALSE
        :type  title:      str
        :type  filter:     str
        :type  default:    str
        :type  file_path:  str_ref
        :type  type:       int
        :type  multi:      int

        :returns:          0 - Ok
                           1 - Cancel
        :rtype:            int

        .. versionadded:: 9.3

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.

        **Note:** Remember to make the string size big enough for multiple file
        selections. In the case of multiple selections the names will be separated
        by a semicolon and only the first file will contain the full path.
        """
        ret_val, file_path.value = gxapi_cy.WrapGUI._custom_file_form(GXContext._get_tls_geo(), title.encode(), filter.encode(), default.encode(), file_path.value.encode(), type, multi)
        return ret_val



    @classmethod
    def import_drill_database_ado2(cls, connect, temp, table, type, reg):
        """
        Same as `import_drill_database_ado <geosoft.gxapi.GXGUI.import_drill_database_ado>`, but template name is returned.
        
        :param connect:  External database connection string (Blank for OLEDB Wizard)
        :param temp:     Template to make (if left blank, the created template name is returned)
        :param table:    Name of table
        :param type:     Type of import returned :ref:`DH_DATA`
        :param reg:      Drill Hole Object `GXREG <geosoft.gxapi.GXREG>` handle
        :type  connect:  str
        :type  temp:     str_ref
        :type  table:    str_ref
        :type  type:     int_ref
        :type  reg:      GXREG

        :returns:        0 - OK
                         -1 - Cancel
        :rtype:          int

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Limitations:** May not be available while executing a command line program.

        **Note:** If it is not defined on input, the template name is set
        to be the Wholeplot table name; e.g.
        "HOLESURVEY.i4" for "Project_HOLESURVEY"
        """
        ret_val, temp.value, table.value, type.value = gxapi_cy.WrapGUI._import_drill_database_ado2(GXContext._get_tls_geo(), connect.encode(), temp.value.encode(), table.value.encode(), type.value, reg)
        return ret_val



    @classmethod
    def import_drill_database_esri(cls, connect, temp, table, type, geochem, reg):
        """
        Same as iImportDrillDatabaseADO2_GUI, but from an ArcGIS Geodatabase
        
        :param connect:  External database connection string  (e.g. "d:\\Personal\\test.mdb|Table" or "d:\\File\\test.gdb|TableX|FeatureClassY)"
        :param temp:     Template to make (if left blank, the created template name is returned)
        :param table:    Name of table
        :param type:     Type of import returned :ref:`DH_DATA`
        :param geochem:  Geosoft Geochemistry Database?
        :param reg:      Drill Hole Object `GXREG <geosoft.gxapi.GXREG>` handle
        :type  connect:  str
        :type  temp:     str_ref
        :type  table:    str_ref
        :type  type:     int_ref
        :type  geochem:  bool
        :type  reg:      GXREG

        :returns:        0 - OK
                         -1 - Cancel
        :rtype:          int

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Limitations:** May not be available while executing a command line program.

        **Note:** If it is not defined on input, the template name is set
        to be the Wholeplot table name; e.g.
        "HOLESURVEY.i4" for "Project_HOLESURVEY"
        """
        ret_val, temp.value, table.value, type.value = gxapi_cy.WrapGUI._import_drill_database_esri(GXContext._get_tls_geo(), connect.encode(), temp.value.encode(), table.value.encode(), type.value, geochem, reg)
        return ret_val



    @classmethod
    def import_drill_database_odbc(cls, connect, temp, table, type, reg):
        """
        Generate a template file for importing drill holes
        from ODBC database data.
        
        :param connect:  Connection string
        :param temp:     Template to make
        :param table:    Name of table
        :param type:     Type of import returned :ref:`DH_DATA`
        :param reg:      Drill Hole Object `GXREG <geosoft.gxapi.GXREG>` handle
        :type  connect:  str_ref
        :type  temp:     str_ref
        :type  table:    str_ref
        :type  type:     int_ref
        :type  reg:      GXREG

        :returns:        0 - OK
                         -1 - Cancel
        :rtype:          int

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Limitations:** May not be available while executing a command line program.

        **Note:** If the input connection string is empty (""), then the ODBC connection dialogs
        will appear (e.g. to connect to a machine database) before the import wizard
        is run. The connect string used for this connection is then returned.
        This string can then be used on input to skip the ODBC connection dialogs and
        go straight to the Wholeplot import wizard.
        Because the name of the database is not necessarily known, the template name is created
        from the name of the table opened - e.g. "HOLELOCATION.i4".
        """
        ret_val, connect.value, temp.value, table.value, type.value = gxapi_cy.WrapGUI._import_drill_database_odbc(GXContext._get_tls_geo(), connect.value.encode(), temp.value.encode(), table.value.encode(), type.value, reg)
        return ret_val



    @classmethod
    def import_drill_database_odbc_maxwell(cls, connect, temp, table, type, reg):
        """
        Same as `import_drill_database_odbc <geosoft.gxapi.GXGUI.import_drill_database_odbc>` but customized for Maxwell.
        
        :param connect:  Connection string
        :param temp:     Template to make
        :param table:    Name of table
        :param type:     Type of import returned :ref:`DH_DATA`
        :param reg:      Drill Hole Object `GXREG <geosoft.gxapi.GXREG>` handle
        :type  connect:  str_ref
        :type  temp:     str_ref
        :type  table:    str_ref
        :type  type:     int_ref
        :type  reg:      GXREG

        :returns:        0-OK 1-Cancel
        :rtype:          int

        .. versionadded:: 8.3

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Limitations:** May not be available while executing a command line program.

        **Note:** Same as `import_drill_database_odbc <geosoft.gxapi.GXGUI.import_drill_database_odbc>` but customized for Maxwell.
        """
        ret_val, connect.value, temp.value, table.value, type.value = gxapi_cy.WrapGUI._import_drill_database_odbc_maxwell(GXContext._get_tls_geo(), connect.value.encode(), temp.value.encode(), table.value.encode(), type.value, reg)
        return ret_val



    @classmethod
    def import_ascii_wizard(cls, name, temp):
        """
        Generate a template file from a gui.
        
        :param name:  Data file name
        :param temp:  Template to make
        :type  name:  str
        :type  temp:  str

        :returns:     0 - OK
                      1 - Cancel
        :rtype:       int

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Limitations:** May not be available while executing a command line program.
        """
        ret_val = gxapi_cy.WrapGUI._import_ascii_wizard(GXContext._get_tls_geo(), name.encode(), temp.encode())
        return ret_val



    @classmethod
    def import_chem_database(cls, name, temp, table, type):
        """
        Generate a template file for importing Geochems Database.
        
        :param name:   Data file name
        :param temp:   Template to make
        :param table:  Name of table
        :param type:   :ref:`IMPCH_TYPE`
        :type  name:   str
        :type  temp:   str
        :type  table:  str_ref
        :type  type:   int

        :returns:      0 - OK
                       -1 - Cancel
        :rtype:        int

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Limitations:** May not be available while executing a command line program.
        """
        ret_val, table.value = gxapi_cy.WrapGUI._import_chem_database(GXContext._get_tls_geo(), name.encode(), temp.encode(), table.value.encode(), type)
        return ret_val



    @classmethod
    def import_chem_database_ado(cls, connect, temp, table, type):
        """
        Improved template creation for importing geochem database (ADO).
        
        :param connect:  External database connection string (Blank for OLEDB Wizard)
        :param temp:     Template to make
        :param table:    Name of table
        :param type:     :ref:`IMPCH_TYPE`
        :type  connect:  str
        :type  temp:     str
        :type  table:    str_ref
        :type  type:     int

        :returns:        0 - OK
                         -1 - Cancel
        :rtype:          int

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Limitations:** May not be available while executing a command line program.

        **Note:** This is an improved version of ImportChemDatabase_GUI using the
        new ADO technology, as opposed to DAO. Use in conjuction with
        `GXDU.import_ado <geosoft.gxapi.GXDU.import_ado>`. See also ImportDatabaseADO_GUI.
        """
        ret_val, table.value = gxapi_cy.WrapGUI._import_chem_database_ado(GXContext._get_tls_geo(), connect.encode(), temp.encode(), table.value.encode(), type)
        return ret_val



    @classmethod
    def import_database(cls, name, temp, table):
        """
        Create template to import an external database table.
        
        :param name:   External database file name
        :param temp:   Template to make
        :param table:  Name of table imported (returned)
        :type  name:   str
        :type  temp:   str
        :type  table:  str_ref

        :returns:      0 - OK
                       -1 - Cancel
        :rtype:        int

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Limitations:** May not be available while executing a command line program.

        **Note:** This is used to select a single database table, and
        selected fields from that table. If the database is not
        Microsoft Access (type .mdb), an introductory dialog
        requests the file type.
        This function DOES NOT import the table itself, but
        creates an import template which may be used to import
        the table (see `GXDU.import_dao <geosoft.gxapi.GXDU.import_dao>`).
        """
        ret_val, table.value = gxapi_cy.WrapGUI._import_database(GXContext._get_tls_geo(), name.encode(), temp.encode(), table.value.encode())
        return ret_val



    @classmethod
    def import_database_ado(cls, connect, temp, table):
        """
        Create template to import an external database table (ADO Version).
        
        :param connect:  External database connection string (Blank for OLEDB Wizard)
        :param temp:     Template to make
        :param table:    Name of table imported (returned)
        :type  connect:  str
        :type  temp:     str
        :type  table:    str_ref

        :returns:        0 - OK
                         -1 - Cancel
        :rtype:          int

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Limitations:** May not be available while executing a command line program.

        **Note:** 1. This is used to select a single database table, and
           selected fields from that table.

        2. This function DOES NOT import the table itself, but
           creates an import template which may be used to import
           the table (see `GXDU.import_ado <geosoft.gxapi.GXDU.import_ado>`).

        3. If connection string is of type "FILENAME=..." the connection will attempt to resolve
           it as a file database. (see also ODBCFileConnect_GUI)
        """
        ret_val, table.value = gxapi_cy.WrapGUI._import_database_ado(GXContext._get_tls_geo(), connect.encode(), temp.encode(), table.value.encode())
        return ret_val



    @classmethod
    def import_database_sql(cls, name, sql, temp, line):
        """
        Create template to import an external database table,
        created using SQL.
        
        :param name:  External database file name
        :param sql:   Text file with SQL queries to use, ("" - get from database)
        :param temp:  Import template to make
        :param line:  Name of table imported (returned)
        :type  name:  str
        :type  sql:   str
        :type  temp:  str
        :type  line:  str_ref

        :returns:     0 - OK
                      -1 - Cancel
        :rtype:       int

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Limitations:** May not be available while executing a command line program.

        **Note:** 1. This is used to build an Oasis montaj group (line) from
           one or more database tables and fields, by selecting from
           one or more SQL selection queries. The list of queries
           is read from a text file with the following syntax:

           Query_Name_1
           Query...
           Query... (continued)
           ...
           ...
           END_QUERY
           Query_Name_2
           etc.

        2. Each query has a title line, the query itself, then the
           "END_QUERY" line to finish.  The title of a subsequent query
           is on the line after an "END_QUERY" line.

        3. If the text file parameter is left blank (""), then
           selection queries in the database itself are listed.
           In addition to the pre-defined queries, there is a
           "User Defined" query which may be filled in by the user.

        4. This function DOES NOT import the table itself, but
           creates an import template which may be used to import
           the data (see `GXDU.import_dao <geosoft.gxapi.GXDU.import_dao>`).

        5. If connection string is of type "FILENAME=..." the connection will attempt to resolve
           it as a file database. (see also ODBCFileConnect_GUI)
        """
        ret_val, line.value = gxapi_cy.WrapGUI._import_database_sql(GXContext._get_tls_geo(), name.encode(), sql.encode(), temp.encode(), line.value.encode())
        return ret_val



    @classmethod
    def import_database_sqlado(cls, connect, sql, temp, line):
        """
        Create template to import an external database table,
        created using SQL (New ADO Version).
        
        :param connect:  External database connection string (Blank for OLEDB Wizard)
        :param sql:      Text file with SQL queries to use, ("" - get from database)
        :param temp:     Import template to make
        :param line:     Name of table imported (returned)
        :type  connect:  str
        :type  sql:      str
        :type  temp:     str
        :type  line:     str_ref

        :returns:        0 - OK
                         -1 Cancel
        :rtype:          int

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Limitations:** May not be available while executing a command line program.

        **Note:** This is used to build an Oasis montaj group (line) from
        one or more database tables and fields, by selecting from
        one or more SQL selection queries. The list of queries
        is read from a text file with the following syntax:

        Query_Name_1
        Query...
        Query... (continued)
        ...
        ...
        END_QUERY
        Query_Name_2
        etc.

        Each query has a title line, the query itself, then the
        "END_QUERY" line to finish.  The title of a subsequent query
        is on the line after an "END_QUERY" line.

        If the text file parameter is left blank (""), then
        selection queries in the database itself are listed.
        In addition to the pre-defined queries, there is a
        "User Defined" query which may be filled in by the user.

        This function DOES NOT import the table itself, but
        creates an import template which may be used to import
        the data (see `GXDU.import_dao <geosoft.gxapi.GXDU.import_dao>`).
        """
        ret_val, line.value = gxapi_cy.WrapGUI._import_database_sqlado(GXContext._get_tls_geo(), connect.encode(), sql.encode(), temp.encode(), line.value.encode())
        return ret_val



    @classmethod
    def import_drill_database_ado(cls, connect, temp, table, type, reg):
        """
        Generate a template file for importing drill holes.
        
        :param connect:  External database connection string (Blank for OLEDB Wizard)
        :param temp:     Template to make
        :param table:    Name of table
        :param type:     Type of import returned :ref:`DH_DATA`
        :param reg:      Drill Hole Object `GXREG <geosoft.gxapi.GXREG>` handle
        :type  connect:  str
        :type  temp:     str
        :type  table:    str_ref
        :type  type:     int_ref
        :type  reg:      GXREG

        :returns:        0 - OK
                         -1 - Cancel
        :rtype:          int

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Limitations:** May not be available while executing a command line program.

        **Note:** This is an improved version of ImportDrillDatabase_GUI using the
        new ADO technology, as opposed to DAO. Use in conjunction with
        `GXDU.import_ado <geosoft.gxapi.GXDU.import_ado>`. See also ImportDatabaseADO_GUI.
        """
        ret_val, table.value, type.value = gxapi_cy.WrapGUI._import_drill_database_ado(GXContext._get_tls_geo(), connect.encode(), temp.encode(), table.value.encode(), type.value, reg)
        return ret_val



    @classmethod
    def import_template_sql(cls, name, temp, sql, line):
        """
        Create template to import an external database table; provide query.
        
        :param name:  External database file name
        :param temp:  Import template to make
        :param sql:   SQL selection query to run on database
        :param line:  Name of Oasis table to create
        :type  name:  str
        :type  temp:  str
        :type  sql:   str
        :type  line:  str

        :returns:     0 - OK
                      -1 Cancel
                      terminates on error
        :rtype:       int

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Limitations:** May not be available while executing a command line program.

        **Note:** This is similar to `import_database_sql <geosoft.gxapi.GXGUI.import_database_sql>`, but dispenses with
        the dialog offering a selection of queries. Instead, the
        user supplies the query as a string.

        This function DOES NOT import the table itself, but
        creates an import template which may be used to import
        the data (see `GXDU.import_dao <geosoft.gxapi.GXDU.import_dao>`).
        """
        ret_val = gxapi_cy.WrapGUI._import_template_sql(GXContext._get_tls_geo(), name.encode(), temp.encode(), sql.encode(), line.encode())
        return ret_val



    @classmethod
    def import_template_sqlado(cls, name, temp, sql, line):
        """
        Create template to import an external database table; provide query.
        
        :param name:  External database connection string (Blank for OLEDB Wizard)
        :param temp:  Import template to make
        :param sql:   SQL selection query to run on database
        :param line:  Name of Oasis table to create
        :type  name:  str
        :type  temp:  str
        :type  sql:   str
        :type  line:  str

        :returns:     0 - OK
                      -1 - Cancel
                      terminates on error
        :rtype:       int

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Limitations:** May not be available while executing a command line program.

        **Note:** This is similar to `import_database_sql <geosoft.gxapi.GXGUI.import_database_sql>`, but dispenses with
        the dialog offering a selection of queries. Instead, the
        user supplies the query as a string.

        This function DOES NOT import the table itself, but
        creates an import template which may be used to import
        the data (see `GXDU.import_ado <geosoft.gxapi.GXDU.import_ado>`).
        """
        ret_val = gxapi_cy.WrapGUI._import_template_sqlado(GXContext._get_tls_geo(), name.encode(), temp.encode(), sql.encode(), line.encode())
        return ret_val



    @classmethod
    def import_xyz_template_editor(cls, db, template, size, file):
        """
        Allows the user to edit XYZ import templates
        using a complex dialog. The Template name
        may change during editing.
        
        :param db:        Database
        :param template:  Name of the Template (can change)
        :param size:      Size of the Template
        :param file:      Name of the XYZ file to base it on
        :type  db:        GXDB
        :type  template:  str
        :type  size:      int
        :type  file:      str

        :returns:         0 - OK
                          1 - Error
        :rtype:           int

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Limitations:** May not be available while executing a command line program.
        """
        ret_val = gxapi_cy.WrapGUI._import_xyz_template_editor(GXContext._get_tls_geo(), db, template.encode(), size, file.encode())
        return ret_val



    @classmethod
    def odbc_file_connect(cls, file, connect, usage, table):
        """
        Get the connection string for a file database as well as optional table name and FileUsage attribute
        
        :param file:     File Name
        :param connect:  Connection string (returned)
        :param usage:    File Usage (0 - ODBC drivers not queried, 1 - Directory containing tables, 2 - File containing tables)
        :param table:    Table name of file (returned if plUsage==1)
        :type  file:     str
        :type  connect:  str_ref
        :type  usage:    int
        :type  table:    str_ref

        :returns:        0 - OK
                         -1 - Cancel
                         terminates on error
        :rtype:          int

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Limitations:** May not be available while executing a command line program.

        **Note:** If the file extension is "mdb" or "xls" then a Microsoft Access
        or Excel database is assumed. Otherwise, a dialog appears listing
        the installed ODBC file database drivers. If the driver takes a
        directory as a database (FileUsage==1) the table name is also
        returned. This is needed because the table name may or may not include
        the file extension.
        """
        ret_val, connect.value, table.value = gxapi_cy.WrapGUI._odbc_file_connect(GXContext._get_tls_geo(), file.encode(), connect.value.encode(), usage, table.value.encode())
        return ret_val



    @classmethod
    def symbol_form(cls, symb_font, geo_font, weight, symb_num, symb_size, symb_ang, edge_col, fill_col):
        """
        - Select a symbol.
        
        :param symb_font:  Symbol font file name
        :param geo_font:   Geosoft font?
        :param weight:     Weight :ref:`MVIEW_FONT_WEIGHT`
        :param symb_num:   Symbol number
        :param symb_size:  Symbol size
        :param symb_ang:   Symbol angle
        :param edge_col:   Edge color
        :param fill_col:   Fill color
        :type  symb_font:  str_ref
        :type  geo_font:   bool_ref
        :type  weight:     int_ref
        :type  symb_num:   int_ref
        :type  symb_size:  float_ref
        :type  symb_ang:   float_ref
        :type  edge_col:   int_ref
        :type  fill_col:   int_ref

        :returns:          0 - Ok
                           1 - Cancel
        :rtype:            int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.

        **Note:** Symbols are set on input, and new values returned.
        """
        ret_val, symb_font.value, geo_font.value, weight.value, symb_num.value, symb_size.value, symb_ang.value, edge_col.value, fill_col.value = gxapi_cy.WrapGUI._symbol_form(GXContext._get_tls_geo(), symb_font.value.encode(), geo_font.value, weight.value, symb_num.value, symb_size.value, symb_ang.value, edge_col.value, fill_col.value)
        return ret_val



    @classmethod
    def meta_data_tool(cls, meta, root_token, schema):
        """
        Edit a `GXMETA <geosoft.gxapi.GXMETA>` object
        
        :param meta:        Meta object
        :param root_token:  Root Token, `H_META_INVALID_TOKEN <geosoft.gxapi.H_META_INVALID_TOKEN>` for root
        :param schema:      Display schema information ?
        :type  meta:        GXMETA
        :type  root_token:  int
        :type  schema:      int

        :returns:           0         - OK
                            non-zero  - Cancel
        :rtype:             int

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Limitations:** May not be available while executing a command line program.
        """
        ret_val = gxapi_cy.WrapGUI._meta_data_tool(GXContext._get_tls_geo(), meta, root_token, schema)
        return ret_val



    @classmethod
    def import_chem_wizard(cls, name, temp, type):
        """
        Generate a template file for importing geochems.
        
        :param name:  Data file name
        :param temp:  Template to make
        :param type:  :ref:`IMPCH_TYPE`
        :type  name:  str
        :type  temp:  str
        :type  type:  int

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Limitations:** May not be available while executing a command line program.
        """
        gxapi_cy.WrapGUI._import_chem_wizard(GXContext._get_tls_geo(), name.encode(), temp.encode(), type)
        



    @classmethod
    def import_drill_wizard(cls, name, temp, table, type, reg):
        """
        Generate a template file for importing drill holes.
        
        :param name:   Data file name
        :param temp:   Template to make
        :param table:  Name of table
        :param type:   Type of import returned :ref:`DH_DATA`
        :param reg:    Drill Hole Object `GXREG <geosoft.gxapi.GXREG>` handle
        :type  name:   str
        :type  temp:   str
        :type  table:  str_ref
        :type  type:   int_ref
        :type  reg:    GXREG

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Limitations:** May not be available while executing a command line program.
        """
        table.value, type.value = gxapi_cy.WrapGUI._import_drill_wizard(GXContext._get_tls_geo(), name.encode(), temp.encode(), table.value.encode(), type.value, reg)
        



    @classmethod
    def import_drill_wizard_ex(cls, name, temp, table, type, reg):
        """
        Generate a template file for importing drill holes where type is known
        
        :param name:   Data file name
        :param temp:   Template to make
        :param table:  Name of table
        :param type:   Type of import :ref:`DH_DATA`
        :param reg:    Drill Hole Object `GXREG <geosoft.gxapi.GXREG>` handle
        :type  name:   str
        :type  temp:   str
        :type  table:  str_ref
        :type  type:   int
        :type  reg:    GXREG

        .. versionadded:: 9.5

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Limitations:** May not be available while executing a command line program.
        """
        table.value = gxapi_cy.WrapGUI._import_drill_wizard_ex(GXContext._get_tls_geo(), name.encode(), temp.encode(), table.value.encode(), type, reg)
        



    @classmethod
    def internet_trust(cls):
        """
        Change the Internet Trust Relationships
        

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Limitations:** May not be available while executing a command line program.
        """
        gxapi_cy.WrapGUI._internet_trust(GXContext._get_tls_geo())
        



    @classmethod
    def pattern_form(cls, pat, size, thick, dense, col, back_col):
        """
        - Select a pattern.
        
        :param pat:       Current Pattern
        :param size:      Current Size,           // returned
        :param thick:     Current Thick (0-100)   // returned
        :param dense:     Current Density,        // returned
        :param col:       Current Pattern Color   // passed in and returned
        :param back_col:  Current Background Color  // passed in and returned; can be `C_TRANSPARENT <geosoft.gxapi.C_TRANSPARENT>`
        :type  pat:       int_ref
        :type  size:      float_ref
        :type  thick:     int_ref
        :type  dense:     float_ref
        :type  col:       int_ref
        :type  back_col:  int_ref

        :returns:         0 - Ok
                          1 - Cancel
        :rtype:           int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.

        **Note:** Pattern values set on input, and new values returned.
        Solid fill is indicated by Pattern number 0.

        Returned Values (not set on input)

        Size
             pattern tile size in mm.

        Thick
             pattern line thickness in percent of the tile size.
             valid range is 0-100.

        Density
             Tile spacing. A value of 1 means tiles are laid with no overlap.
             A value of 2 means they overlap each other.

        The pattern Angle and Style parameters are not user-definable.
        """
        ret_val, pat.value, size.value, thick.value, dense.value, col.value, back_col.value = gxapi_cy.WrapGUI._pattern_form(GXContext._get_tls_geo(), pat.value, size.value, thick.value, dense.value, col.value, back_col.value)
        return ret_val



    @classmethod
    def line_pattern_form(cls, pattern, thickness, pitch, colour):
        """
        Select a line pattern.
        
        :param pattern:    Current Pattern
        :param thickness:  Current Thickness
        :param pitch:      Current Pitch
        :param colour:     Current Pattern Color
        :type  pattern:    int_ref
        :type  thickness:  float_ref
        :type  pitch:      float_ref
        :type  colour:     int_ref

        :returns:          0 - Ok
                           1 - Cancel
        :rtype:            int

        .. versionadded:: 8.1

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.

        **Note:** Same as `pattern_form <geosoft.gxapi.GXGUI.pattern_form>` but for line patterns.
        """
        ret_val, pattern.value, thickness.value, pitch.value, colour.value = gxapi_cy.WrapGUI._line_pattern_form(GXContext._get_tls_geo(), pattern.value, thickness.value, pitch.value, colour.value)
        return ret_val



    @classmethod
    def two_panel_selection(cls, ls_tf, ls_ts, title):
        """
        General purpose two-panel selection.
        
        :param ls_tf:  All available items for selection.
        :param ls_ts:  Selections (altered on output)
        :param title:  Title for dialog
        :type  ls_tf:  GXLST
        :type  ls_ts:  GXLST
        :type  title:  str

        :returns:      0 - Ok
                       1 - Cancel
        :rtype:        int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.

        **Note:** Takes as input two LSTs, one contains all available items,
        the second currently selected items. These are processed,
        and in the left panel are displayed all items in the first
        `GXLST <geosoft.gxapi.GXLST>` not in the selection `GXLST <geosoft.gxapi.GXLST>`, and on the right all items
        in the first `GXLST <geosoft.gxapi.GXLST>` which are in the selection `GXLST <geosoft.gxapi.GXLST>`. (Items in
        the selection `GXLST <geosoft.gxapi.GXLST>` NOT in the first `GXLST <geosoft.gxapi.GXLST>` are ignored).
        Once the user has finalized the selections, the final selections
        are returned in the selection `GXLST <geosoft.gxapi.GXLST>`.

        Selections and display are based on the `LST_ITEM_NAME <geosoft.gxapi.LST_ITEM_NAME>` part of the
        `GXLST <geosoft.gxapi.GXLST>` item, but on export both the `LST_ITEM_NAME <geosoft.gxapi.LST_ITEM_NAME>` and `LST_ITEM_VALUE <geosoft.gxapi.LST_ITEM_VALUE>`
        elements of the selected items from the first `GXLST <geosoft.gxapi.GXLST>` are transferred
        to the second list for output.

        The sConvertToCSV_LST and sConvertFromCSV_LST functions in lst.h
        can be used to convert the selection LSTs to forms that can be
        stored and retrieved from GX parameters (or `GXREG <geosoft.gxapi.GXREG>` or INI, etc.).
        """
        ret_val = gxapi_cy.WrapGUI._two_panel_selection(GXContext._get_tls_geo(), ls_tf, ls_ts, title.encode())
        return ret_val



    @classmethod
    def two_panel_selection2(cls, ls_tf, ls_ts, title):
        """
        Two-panel selection, items not sorted alphabetically.
        
        :param ls_tf:  All available items for selection.
        :param ls_ts:  Selections (altered on output)
        :param title:  Title for dialog
        :type  ls_tf:  GXLST
        :type  ls_ts:  GXLST
        :type  title:  str

        :returns:      0 - Ok
                       1 - Cancel
        :rtype:        int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.

        **Note:** Same as `two_panel_selection <geosoft.gxapi.GXGUI.two_panel_selection>`, but the items in the
        two lists are not sorted alphabetically, but are ordered
        exactly as input, and when an item is selected it is
        added at the end of the lists.
        """
        ret_val = gxapi_cy.WrapGUI._two_panel_selection2(GXContext._get_tls_geo(), ls_tf, ls_ts, title.encode())
        return ret_val



    @classmethod
    def two_panel_selection_ex(cls, ls_tf, ls_ts, sorted, allow_no_select, title):
        """
        Two-panel selection; options for sort and ability to select no items.
        
        :param ls_tf:            All available items for selection.
        :param ls_ts:            Selections (altered on output)
        :param sorted:           Sort items alphabetically (0:No, 1:Yes)
        :param allow_no_select:  Allow no items selected (0:No, 1:Yes)
        :param title:            Title for dialog
        :type  ls_tf:            GXLST
        :type  ls_ts:            GXLST
        :type  sorted:           int
        :type  allow_no_select:  int
        :type  title:            str

        :returns:                0 - Ok
                                 1 - Cancel
        :rtype:                  int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.

        **Note:** Same as `two_panel_selection <geosoft.gxapi.GXGUI.two_panel_selection>`, but the items in the
        two lists are not sorted alphabetically, but are ordered
        exactly as input, and when an item is selected it is
        added at the end of the lists.
        """
        ret_val = gxapi_cy.WrapGUI._two_panel_selection_ex(GXContext._get_tls_geo(), ls_tf, ls_ts, sorted, allow_no_select, title.encode())
        return ret_val



    @classmethod
    def two_panel_selection_ex2(cls, ls_tf, ls_ts, sorted, allow_no_select, title, help):
        """
        Two-panel selection; extended options including a help link.
        
        :param ls_tf:            All available items for selection.
        :param ls_ts:            Selections (altered on output)
        :param sorted:           Sort items alphabetically (0:No, 1:Yes)
        :param allow_no_select:  Allow no items selected (0:No, 1:Yes)
        :param title:            Title for dialog
        :param help:             Help link
        :type  ls_tf:            GXLST
        :type  ls_ts:            GXLST
        :type  sorted:           int
        :type  allow_no_select:  int
        :type  title:            str
        :type  help:             str

        :returns:                0 - Ok
                                 1 - Cancel
        :rtype:                  int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.

        **Note:** Same as `two_panel_selection_ex <geosoft.gxapi.GXGUI.two_panel_selection_ex>`, but user can specify a help
        link.
        """
        ret_val = gxapi_cy.WrapGUI._two_panel_selection_ex2(GXContext._get_tls_geo(), ls_tf, ls_ts, sorted, allow_no_select, title.encode(), help.encode())
        return ret_val



    @classmethod
    def launch_single_geo_dotnetx_tool(cls, dll, func, meta):
        """
        Launch a user created .Net GEOXTOOL ensuring a single instance.
        
        :param dll:   Assembly name
        :param func:  Control Class Name
        :param meta:  `GXMETA <geosoft.gxapi.GXMETA>` Handle (holding tool configuration data)
        :type  dll:   str
        :type  func:  str
        :type  meta:  GXMETA

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.
        """
        gxapi_cy.WrapGUI._launch_single_geo_dotnetx_tool(GXContext._get_tls_geo(), dll.encode(), func.encode(), meta)
        



    @classmethod
    def launch_geo_dotnetx_tool(cls, dll, func, meta):
        """
        Launch a user created .Net GEOXTOOL.
        
        :param dll:   Assembly name
        :param func:  Control Class Name
        :param meta:  `GXMETA <geosoft.gxapi.GXMETA>` Handle (holding tool configuration data)
        :type  dll:   str
        :type  func:  str
        :type  meta:  GXMETA

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.
        """
        gxapi_cy.WrapGUI._launch_geo_dotnetx_tool(GXContext._get_tls_geo(), dll.encode(), func.encode(), meta)
        



    @classmethod
    def launch_geo_x_tool(cls, dll, func, meta):
        """
        Launch a user created GEOXTOOL.
        
        :param dll:   DLL name
        :param func:  Function Name
        :param meta:  `GXMETA <geosoft.gxapi.GXMETA>` Handle (holding tool configuration data)
        :type  dll:   str
        :type  func:  str
        :type  meta:  GXMETA

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.
        """
        gxapi_cy.WrapGUI._launch_geo_x_tool(GXContext._get_tls_geo(), dll.encode(), func.encode(), meta)
        



    @classmethod
    def launch_single_geo_dotnetx_tool_ex(cls, dll, func, meta, align, dock, width, height):
        """
        Launch a user created .Net GEOXTOOL ensuring a single instance.
        
        :param dll:     Assembly name
        :param func:    Control Class Name
        :param meta:    `GXMETA <geosoft.gxapi.GXMETA>` Handle (holding tool configuration data)
        :param align:   :ref:`XTOOL_ALIGN` (can specify one or more or `XTOOL_ALIGN_ANY <geosoft.gxapi.XTOOL_ALIGN_ANY>`)
        :param dock:    :ref:`XTOOL_DOCK`
        :param width:   Default width
        :param height:  Default height
        :type  dll:     str
        :type  func:    str
        :type  meta:    GXMETA
        :type  align:   int
        :type  dock:    int
        :type  width:   int
        :type  height:  int

        .. versionadded:: 9.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.
        """
        gxapi_cy.WrapGUI._launch_single_geo_dotnetx_tool_ex(GXContext._get_tls_geo(), dll.encode(), func.encode(), meta, align, dock, width, height)
        



    @classmethod
    def launch_geo_dotnetx_tool_ex(cls, dll, func, meta, align, dock, width, height):
        """
        Launch a user created .Net GEOXTOOL.
        
        :param dll:     Assembly name
        :param func:    Control Class Name
        :param meta:    `GXMETA <geosoft.gxapi.GXMETA>` Handle (holding tool configuration data)
        :param align:   :ref:`XTOOL_ALIGN` (can specify one or more or `XTOOL_ALIGN_ANY <geosoft.gxapi.XTOOL_ALIGN_ANY>`)
        :param dock:    :ref:`XTOOL_DOCK`
        :param width:   Default width
        :param height:  Default height
        :type  dll:     str
        :type  func:    str
        :type  meta:    GXMETA
        :type  align:   int
        :type  dock:    int
        :type  width:   int
        :type  height:  int

        .. versionadded:: 9.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.
        """
        gxapi_cy.WrapGUI._launch_geo_dotnetx_tool_ex(GXContext._get_tls_geo(), dll.encode(), func.encode(), meta, align, dock, width, height)
        



    @classmethod
    def launch_geo_x_tool_ex(cls, dll, func, meta, align, dock, width, height):
        """
        Launch a user created GEOXTOOL.
        
        :param dll:     DLL name
        :param func:    Function Name
        :param meta:    `GXMETA <geosoft.gxapi.GXMETA>` Handle (holding tool configuration data)
        :param align:   :ref:`XTOOL_ALIGN` (can specify one or more or `XTOOL_ALIGN_ANY <geosoft.gxapi.XTOOL_ALIGN_ANY>`)
        :param dock:    :ref:`XTOOL_DOCK`
        :param width:   Default width
        :param height:  Default height
        :type  dll:     str
        :type  func:    str
        :type  meta:    GXMETA
        :type  align:   int
        :type  dock:    int
        :type  width:   int
        :type  height:  int

        .. versionadded:: 9.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.
        """
        gxapi_cy.WrapGUI._launch_geo_x_tool_ex(GXContext._get_tls_geo(), dll.encode(), func.encode(), meta, align, dock, width, height)
        



    @classmethod
    def meta_data_viewer(cls, meta, root_token, schema):
        """
        View a `GXMETA <geosoft.gxapi.GXMETA>` object
        
        :param meta:        Meta object
        :param root_token:  Root token, `H_META_INVALID_TOKEN <geosoft.gxapi.H_META_INVALID_TOKEN>` for root
        :param schema:      Display schema information ?
        :type  meta:        GXMETA
        :type  root_token:  int
        :type  schema:      int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.
        """
        gxapi_cy.WrapGUI._meta_data_viewer(GXContext._get_tls_geo(), meta, root_token, schema)
        



    @classmethod
    def print_file(cls, file):
        """
        Prints a file to current printer
        
        :param file:  Filename string
        :type  file:  str

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Limitations:** May not be available while executing a command line program.
        """
        gxapi_cy.WrapGUI._print_file(GXContext._get_tls_geo(), file.encode())
        



    @classmethod
    def render_pattern(cls, hdc, left, bottom, right, top, pat, size, thick, dense, col, back_col, is_enabled, is_button, is_selected):
        """
        - Render a pattern.
        
        :param hdc:          DC handle
        :param left:         Left value of the render rect in Windows coordinates (bottom>top)
        :param bottom:       Bottom value
        :param right:        Right value
        :param top:          Top value
        :param pat:          Pattern number
        :param size:         Pattern size,           // input `GS_R8DM <geosoft.gxapi.GS_R8DM>` to use default
        :param thick:        Pattern thick (0-100)   // input `GS_S4DM <geosoft.gxapi.GS_S4DM>` to use default
        :param dense:        Pattern density,        // input `GS_R8DM <geosoft.gxapi.GS_R8DM>` to use default
        :param col:          Pattern color	  // input `GS_S4DM <geosoft.gxapi.GS_S4DM>` to use default
        :param back_col:     Pattern background color // input `GS_S4DM <geosoft.gxapi.GS_S4DM>` to use default; can be `C_TRANSPARENT <geosoft.gxapi.C_TRANSPARENT>`
        :param is_enabled:   Is this window enabled?
        :param is_button:    Is this a button?
        :param is_selected:  Is this window selected?
        :type  hdc:          int
        :type  left:         int
        :type  bottom:       int
        :type  right:        int
        :type  top:          int
        :type  pat:          int
        :type  size:         float
        :type  thick:        int
        :type  dense:        float
        :type  col:          int
        :type  back_col:     int
        :type  is_enabled:   int
        :type  is_button:    int
        :type  is_selected:  int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.

        **Note:** Renders a Geosoft pattern to a Windows DC.
        """
        gxapi_cy.WrapGUI._render_pattern(GXContext._get_tls_geo(), hdc, left, bottom, right, top, pat, size, thick, dense, col, back_col, is_enabled, is_button, is_selected)
        



    @classmethod
    def render_line_pattern(cls, hdc, left, bottom, right, top, pattern, thickness, pitch, col, is_enabled, is_button, is_selected):
        """
        Render a line pattern.
        
        :param hdc:          DC Handle
        :param left:         Left value of the render rect in Windows coordinates (bottom>top)
        :param bottom:       Bottom value
        :param right:        Right value
        :param top:          Top value
        :param pattern:      Pattern number
        :param thickness:    Pattern thickness
        :param pitch:        Pattern pitch
        :param col:          Pattern color
        :param is_enabled:   Is this window enabled?
        :param is_button:    Is this a button?
        :param is_selected:  Is this window selected?
        :type  hdc:          int
        :type  left:         int
        :type  bottom:       int
        :type  right:        int
        :type  top:          int
        :type  pattern:      int
        :type  thickness:    float
        :type  pitch:        float
        :type  col:          int
        :type  is_enabled:   int
        :type  is_button:    int
        :type  is_selected:  int

        .. versionadded:: 8.1

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.

        **Note:** Same as `render_pattern <geosoft.gxapi.GXGUI.render_pattern>` but for line patterns.
        """
        gxapi_cy.WrapGUI._render_line_pattern(GXContext._get_tls_geo(), hdc, left, bottom, right, top, pattern, thickness, pitch, col, is_enabled, is_button, is_selected)
        



    @classmethod
    def set_parent_wnd(cls, wnd):
        """
        Set the current parent WND
        
        :param wnd:  New Parent Window
        :type  wnd:  int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.

        **Note:** The parent WND is used by all modal dialogs as a
        parent to ensure the dialog is correctly modal.
        """
        gxapi_cy.WrapGUI._set_parent_wnd(GXContext._get_tls_geo(), wnd)
        



    @classmethod
    def set_printer(cls, printer):
        """
        Sets the Printer.
        
        :param printer:  Printer Name
        :type  printer:  str

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Limitations:** May not be available while executing a command line program.
        """
        gxapi_cy.WrapGUI._set_printer(GXContext._get_tls_geo(), printer.encode())
        



    @classmethod
    def set_prog_always_on(cls, on):
        """
        Ability to set the progress bar to stay visible even
        if main application is processing messages
        
        :param on:  Should progress bar remain visible
        :type  on:  bool

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.

        **Note:** In montaj the progress bar is hidden when the main window
        start processing messages. This is not always desirable
        in some 3rd party apps, hence this function.
        """
        gxapi_cy.WrapGUI._set_prog_always_on(GXContext._get_tls_geo(), on)
        



    @classmethod
    def show_direct_hist(cls, min, max, mean, std_dev, median, items, vv):
        """
        Display histogram of data directly
        
        :param min:      Min    Value to display
        :param max:      Max    Value to display
        :param mean:     Mean   Value to display
        :param std_dev:  StdDev Value to display
        :param median:   Median Value to display
        :param items:    Items  Number of items this comprises
        :param vv:       `GXVV <geosoft.gxapi.GXVV>` holding hist counts
        :type  min:      float
        :type  max:      float
        :type  mean:     float
        :type  std_dev:  float
        :type  median:   float
        :type  items:    int
        :type  vv:       GXVV

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Limitations:** May not be available while executing a command line program.
        """
        gxapi_cy.WrapGUI._show_direct_hist(GXContext._get_tls_geo(), min, max, mean, std_dev, median, items, vv)
        



    @classmethod
    def show_hist(cls, st):
        """
        Display Histogram of data from `GXST <geosoft.gxapi.GXST>`
        
        :param st:  Statistics obj
        :type  st:  GXST

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Limitations:** May not be available while executing a command line program.
        """
        gxapi_cy.WrapGUI._show_hist(GXContext._get_tls_geo(), st)
        



    @classmethod
    def simple_map_dialog(cls, map, title, help_id):
        """
        General purpose map display `GXGUI <geosoft.gxapi.GXGUI>` with no interaction.
        
        :param map:      `GXMAP <geosoft.gxapi.GXMAP>` object
        :param title:    Title
        :param help_id:  HelpID
        :type  map:      GXMAP
        :type  title:    str
        :type  help_id:  str

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.

        **Note:** This function displays a map in a simple resizable dialog that fits the map into it.
        It is generally useful to display temporary maps as graphs (e.g. variograms).
        """
        gxapi_cy.WrapGUI._simple_map_dialog(GXContext._get_tls_geo(), map, title.encode(), help_id.encode())
        



    @classmethod
    def thematic_voxel_info(cls, vox):
        """
        Display GX.Net thematic voxel info `GXGUI <geosoft.gxapi.GXGUI>`.
        
        :param vox:  `GXVOX <geosoft.gxapi.GXVOX>` object
        :type  vox:  GXVOX

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.

        **Note:** Displays the thematic voxel codes, colors, total volume for
        each code, and number of valid items (cubes) for each code.
        This is a replacement for the numeric stats done on normal
        numerical voxel grids.
        """
        gxapi_cy.WrapGUI._thematic_voxel_info(GXContext._get_tls_geo(), vox)
        



    @classmethod
    def show_3d_viewer_dialog(cls, title, o3dv):
        """
        Display a standalone 3D viewer
        
        :param title:  Title
        :param o3dv:   3D View name (.geosoft_3dv)
        :type  title:  str
        :type  o3dv:   str

        .. versionadded:: 9.3

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Limitations:** May not be available while executing a command line program.

        **Note:** Any changes made to the 3D View will be persisted.
        """
        gxapi_cy.WrapGUI._show_3d_viewer_dialog(GXContext._get_tls_geo(), title.encode(), o3dv.encode())
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer