### extends 'class_empty.py'
### block ClassImports
# NOTICE: Do not edit anything here, it is generated code
from typing import NewType
from . import gxapi_cy
from geosoft.gxapi import GXContext, float_ref, int_ref, str_ref


### endblock ClassImports

### block Header
# NOTICE: The code generator will not replace the code in this block
### endblock Header

### block ClassImplementation
# NOTICE: Do not edit anything here, it is generated code
class GXGUI:
    """
    GXGUI class.

    These are graphical functions that typically create a
    dialog-style window for a specific function. Examples include
    file import wizards, and the Histogram and Scatter tools.
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._wrapper = None

    def __del__(self):
        self._wrapper = None

    def __init__(self, wrapper=None):
        self._wrapper = wrapper if wrapper else gxapi_cy.WrapGUI(GXContext._get_tls_geo(), 0)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of `GXGUI`
        
        :returns: A null `GXGUI`
        """
        return cls()

    def is_null(self):
        """
        Check if the instance of `GXGUI` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of `GXGUI`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Miscellaneous


    @classmethod
    def create_wnd_from_hwnd(cls, p1):
        """
        Create a standard WND object from an HWND.

        **Note:**

        The object returned must be destroyed by the
        destroy object call.
        """
        ret_val = gxapi_cy.WrapGUI.create_wnd_from_hwnd(GXContext._get_tls_geo(), p1)
        return ret_val



    @classmethod
    def fft2_spec_filter(cls, spec_file_name, con_file_name):
        """
        Interactive `GXFFT2` radially averaged power spectrum filter
        """
        gxapi_cy.WrapGUI.fft2_spec_filter(GXContext._get_tls_geo(), spec_file_name.encode(), con_file_name.encode())
        



    @classmethod
    def get_parent_wnd(cls):
        """
        Get the current parent window
        """
        ret_val = gxapi_cy.WrapGUI.get_parent_wnd(GXContext._get_tls_geo())
        return ret_val



    @classmethod
    def get_printer_lst(cls, lst):
        """
        Gets a list of all printers.
        """
        gxapi_cy.WrapGUI.get_printer_lst(GXContext._get_tls_geo(), lst._wrapper)
        



    @classmethod
    def get_window_state(cls):
        """
        Retrieve the current state of the Oasis montaj window
        """
        ret_val = gxapi_cy.WrapGUI.get_window_state(GXContext._get_tls_geo())
        return ret_val



    @classmethod
    def set_window_state(cls, state):
        """
        Changes the state of the Oasis montaj window
        """
        gxapi_cy.WrapGUI.set_window_state(GXContext._get_tls_geo(), state)
        



    @classmethod
    def get_window_position(cls, left, top, right, bottom, state):
        """
        Get the Oasis montaj window's position state
        """
        left.value, top.value, right.value, bottom.value, state.value = gxapi_cy.WrapGUI.get_window_position(GXContext._get_tls_geo(), left.value, top.value, right.value, bottom.value, state.value)
        



    @classmethod
    def set_window_position(cls, left, top, right, bottom, state):
        """
        Get the Oasis montaj window's position and state
        """
        gxapi_cy.WrapGUI.set_window_position(GXContext._get_tls_geo(), left, top, right, bottom, state)
        



    @classmethod
    def get_client_window_area(cls, min_x, min_y, max_x, max_y):
        """
        Get the location of the Oasis montaj client window.

        **Note:**

        Returns the coordinates of the client window area (where MDI document windows are placed).
        The returned coordinates are 0,0 for the minimum X and Y and the window width
        width and height for the maximum X and Y.
        """
        min_x.value, min_y.value, max_x.value, max_y.value = gxapi_cy.WrapGUI.get_client_window_area(GXContext._get_tls_geo(), min_x.value, min_y.value, max_x.value, max_y.value)
        



    @classmethod
    def grid_stat_hist(cls, grid_name):
        """
        Display Histogram of grid
        """
        gxapi_cy.WrapGUI.grid_stat_hist(GXContext._get_tls_geo(), grid_name.encode())
        



    @classmethod
    def voxel_stat_hist(cls, vox_name):
        """
        Display Histogram of Voxel
        """
        gxapi_cy.WrapGUI.voxel_stat_hist(GXContext._get_tls_geo(), vox_name.encode())
        



    @classmethod
    def color_form(cls, col, no_col):
        """
        Select a color.

        **Note:**

        Color value is set on input, and new value returned.
        If the input color type is `C_TRANSPARENT`, then the color
        is set to white, if any other type is input the output is
        guaranteed to be of the same type.
        
        If the third flag is `GS_TRUE` is used, then on exit, if white is
        selected, the user is prompted: 'Do you want white (Yes) or
        "None" (No) ?' and the color is converted as requested.
        If this is not the case, the `C_TRANSPARENT` is converted
        to white (if "Ok" is selected) and no choice is offered.
        """
        ret_val, col.value = gxapi_cy.WrapGUI.color_form(GXContext._get_tls_geo(), col.value, no_col)
        return ret_val



    @classmethod
    def color_transform(cls, itr, st):
        """
        Define an `GXITR` of up to 8 zones.

        **Note:**

        The statistics object is required in order to determine
        data ranges, percentiles, etc. Create it using
        `GXST.create_exact`, or be sure to enable histogram statistics.
        """
        ret_val = gxapi_cy.WrapGUI.color_transform(GXContext._get_tls_geo(), itr._wrapper, st._wrapper)
        return ret_val



    @classmethod
    def coord_sys_wizard(cls, ipj, editable, mode, source_label, source):
        """
        Launch the coordinate system definition/display `GXGUI`.

        **Note:**

        Launches the new GX.Net single-dialog coordinate system
        definition dialog. The input `GXIPJ` is modified on return
        if OK is selected (and the editable parameter is 1).
        The "Data source label" and "Data source" is information displayed
        in the dialog for the user to know where the `GXIPJ` came from (e.g. "Grid: X.grd")
        """
        ret_val = gxapi_cy.WrapGUI.coord_sys_wizard(GXContext._get_tls_geo(), ipj._wrapper, editable, mode, source_label.encode(), source.encode())
        return ret_val



    @classmethod
    def coord_sys_wizard_licensed(cls, ipj, editable, mode, source_label, source):
        """
        Launch the coordinate system definition/display `GXGUI`.

        **Note:**

        Same as `coord_sys_wizard_licensed` but will always be editable. The other
        method is not editable in the viewer while this one is.
        """
        ret_val = gxapi_cy.WrapGUI.coord_sys_wizard_licensed(GXContext._get_tls_geo(), ipj._wrapper, editable, mode, source_label.encode(), source.encode())
        return ret_val



    @classmethod
    def coord_sys_wizard_grid(cls, ipj, target_ipj, editable, mode, source_label, source, nx, ny, x0, y0, dx, dy, rot):
        """
        Launch the coordinate system definition/display `GXGUI`.

        **Note:**

        Same as `coord_sys_wizard_licensed` but allows the original grid info to be adjusted
        when projections on section or oriented plan grids are modified.
        In the tool, it is the "modified" orientation required to keep the edited projection's grid
        in the same location as it was in the target projection.
        """
        ret_val, x0.value, y0.value, dx.value, dy.value, rot.value = gxapi_cy.WrapGUI.coord_sys_wizard_grid(GXContext._get_tls_geo(), ipj._wrapper, target_ipj._wrapper, editable, mode, source_label.encode(), source.encode(), nx, ny, x0.value, y0.value, dx.value, dy.value, rot.value)
        return ret_val



    @classmethod
    def database_type(cls, name, type):
        """
        Returns the type string of an external DAO database.

        **Note:**

        If the file extension is "mdb", then an MSJET (Microsoft Access)
        database is assumed. If the file name is "ODBC", then "ODBC" is
        returned as the type. Otherwise, a dialog appears listing the
        other valid DAO database types.
        """
        ret_val, type.value = gxapi_cy.WrapGUI.database_type(GXContext._get_tls_geo(), name.encode(), type.value.encode())
        return ret_val



    @classmethod
    def datamine_type(cls, file, type):
        """
        Returns the type of a Datamine file.

        **Note:**

        Often, a Datamine file can be opened a number of different ways
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
        ret_val, type.value = gxapi_cy.WrapGUI.datamine_type(GXContext._get_tls_geo(), file.encode(), type.value)
        return ret_val



    @classmethod
    def export_xyz_template_editor(cls, db, template, size):
        """
        Allows the user to edit XYZ export template
        using a complex dialog. The Template name
        may change during editing.

        **Note:**

        Only uses the current `GXDB`. This function does
        not exactly work as supposed to. Instead of using
        the `GXEDB` handle passed to it, it only will use
        the current `GXDB`. Please see ExportXYXTemplateEditorEx_GUI
        for an updated function.
        """
        ret_val = gxapi_cy.WrapGUI.export_xyz_template_editor(GXContext._get_tls_geo(), db._wrapper, template.encode(), size)
        return ret_val



    @classmethod
    def export_xyz_template_editor_ex(cls, edb, template):
        """
        Allows the user to edit an XYZ export template
        using a complex dialog. The template name
        may change during editing.
        """
        ret_val, template.value = gxapi_cy.WrapGUI.export_xyz_template_editor_ex(GXContext._get_tls_geo(), edb._wrapper, template.value.encode())
        return ret_val



    @classmethod
    def file_filter_index(cls, filter):
        """
        Return the FILE_FILTER_XXX value for a file filter string.

        **Note:**

        For example, if "Database (``*.gdb``)" is input,
        then the `FILE_FILTER_GDB` value is returned.
        """
        ret_val = gxapi_cy.WrapGUI.file_filter_index(GXContext._get_tls_geo(), filter.encode())
        return ret_val



    @classmethod
    def gcs_datum_warning_shp(cls, data_source, ipj):
        """
        Launch the GCS Datum Warning dialog for `GXSHP` files.

        **Note:**

        Runs the GCS Warning dialog with one data source
        """
        ret_val = gxapi_cy.WrapGUI.gcs_datum_warning_shp(GXContext._get_tls_geo(), data_source.encode(), ipj._wrapper)
        return ret_val



    @classmethod
    def gcs_datum_warning_shpdb_ex(cls, source_lst, datum_from_lst, ldtlst, db):
        """
        Launch the GCS Datum Warning dialog for `GXSHP` files (Database).

        **Note:**

        Runs the GCS Warning dialog with multiple data sources (Database)
        """
        ret_val = gxapi_cy.WrapGUI.gcs_datum_warning_shpdb_ex(GXContext._get_tls_geo(), source_lst._wrapper, datum_from_lst._wrapper, ldtlst._wrapper, db._wrapper)
        return ret_val



    @classmethod
    def gcs_datum_warning_shp_ex(cls, source_lst, datum_from_lst, ldtlst, mview):
        """
        Launch the GCS Datum Warning dialog for `GXSHP` files.

        **Note:**

        Runs the GCS Warning dialog with multiple data sources
        """
        ret_val = gxapi_cy.WrapGUI.gcs_datum_warning_shp_ex(GXContext._get_tls_geo(), source_lst._wrapper, datum_from_lst._wrapper, ldtlst._wrapper, mview._wrapper)
        return ret_val



    @classmethod
    def get_area_of_interest(cls, min_x, min_y, max_x, max_y, ply, ipj):
        """
        Get the current area of interest from the application.

        **Note:**

        Depending on what is currently visible on screen and
        the defined coordinate system the user may be prompted
        by a warning and optionaly cancel the process.
        """
        ret_val, min_x.value, min_y.value, max_x.value, max_y.value = gxapi_cy.WrapGUI.get_area_of_interest(GXContext._get_tls_geo(), min_x.value, min_y.value, max_x.value, max_y.value, ply._wrapper, ipj._wrapper)
        return ret_val



    @classmethod
    def get_area_of_interest_3d(cls, min_x, min_y, min_z, max_x, max_y, max_z, ply, ipj):
        """
        Get the current area of interest from the application in 3D.

        **Note:**

        Depending on what is currently visible on screen and
        the defined coordinate system the user may be prompted
        by a warning and optionaly cancel the process.
        """
        ret_val, min_x.value, min_y.value, min_z.value, max_x.value, max_y.value, max_z.value = gxapi_cy.WrapGUI.get_area_of_interest_3d(GXContext._get_tls_geo(), min_x.value, min_y.value, min_z.value, max_x.value, max_y.value, max_z.value, ply._wrapper, ipj._wrapper)
        return ret_val



    @classmethod
    def get_dat_defaults(cls, flags, open, ext, qual):
        """
        Return the user default extension and qualifier for grids/images.

        **Note:**

        The default grid/image filters are normally stored in
        "MONTAJ.DEFAULT_XGD_IN" and "MONTAJ.DEFAULT_XGD_OUT"
        
        If no filter is defined, or the filter is not found
        then "grd" and "GRD" are returned as the default extension
        and qualifier.
        """
        ext.value, qual.value = gxapi_cy.WrapGUI.get_dat_defaults(GXContext._get_tls_geo(), flags, open, ext.value.encode(), qual.value.encode())
        



    @classmethod
    def get_file_filter(cls, file_filter, filter, mask, ext, path):
        """
        Return the defined filter, mask, extension and directory for an input filter.

        **Note:**

        Returns the four parts of the file filter;
        e.g. for `FILE_FILTER_GDB` it returns:
        
        Filter:    "Database (``*.gdb``)"
        Mask:      "``*.gdb``"
        Extension: "gdb"
        Directory: "`GS_DIRECTORY_NONE`"
        
        This function is useful for constuction open/save dialog
        file filters, especially in GX.Net functions.
        """
        filter.value, mask.value, ext.value, path.value = gxapi_cy.WrapGUI.get_file_filter(GXContext._get_tls_geo(), file_filter, filter.value.encode(), mask.value.encode(), ext.value.encode(), path.value)
        



    @classmethod
    def get_gs_directory(cls, path, dir):
        """
        Return the directory path for value of `GS_DIRECTORY`.

        **Note:**

        Works along with the `get_file_filter` function. Note that
        most values of FILE_FILTER_XXX will return `GS_DIRECTORY_NONE`,
        and give the current workspace directory.
        
        This function is useful for constuction open/save dialog
        file filters, especially in GX.Net functions.
        """
        dir.value = gxapi_cy.WrapGUI.get_gs_directory(GXContext._get_tls_geo(), path, dir.value.encode())
        



    @classmethod
    def browse_dir(cls, title, default, dir_path):
        """
        Browses for a specific directory.
        """
        ret_val, dir_path.value = gxapi_cy.WrapGUI.browse_dir(GXContext._get_tls_geo(), title.encode(), default.encode(), dir_path.value.encode())
        return ret_val



    @classmethod
    def color_transform_ex(cls, itr, st, zones, load_save, file):
        """
        Define an `GXITR` of up to 12 zones, with file load/save buttons.

        **Note:**

        The statistics object is required in order to determine
        data ranges, percentiles, etc. Create it using
        `GXST.create_exact`, or be sure to enable histogram statistics.
        The color transform file name is used as the default when the save
        button is pushed, and is updated both after the load and save buttons
        are pushed by the value input or selected by the user.
        """
        ret_val, file.value = gxapi_cy.WrapGUI.color_transform_ex(GXContext._get_tls_geo(), itr._wrapper, st._wrapper, zones, load_save, file.value.encode())
        return ret_val



    @classmethod
    def cumulative_percent(cls, file, itr):
        """
        Define a percent-based `GXITR` of up to 12 zones.

        **Note:**

        The `GXITR` values are interpreted as cumulative percent values, using
        the "PERCENT=1" value in the `GXITR`'s `GXREG`.
        
        Note that processes using ITRs do not automatically know to convert between
        percent values and "actual" data values. The `GXREG` "PERCENT" value is simply
        a flag to indicate to a user that the values are intended to be in the range
        from 0 < x < 100. The `GXITR` should not, therefore, be applied directly to data
        unless that data is already given in percent.
        
        If the file name is defined on input, the initial `GXITR` will be loaded from it.
        If it is left blank, a default 5-color transform with
        The color transform file name is used as the default when the save
        button is pushed, and is updated both after the load and save buttons
        are pushed by the value input or selected by the user.
        """
        ret_val, file.value = gxapi_cy.WrapGUI.cumulative_percent(GXContext._get_tls_geo(), file.value.encode(), itr._wrapper)
        return ret_val



    @classmethod
    def dat_file_form(cls, title, default, psz_file_path, type, validation_type, multi):
        """
        Grid and Image file Open/Save Form for Multiple/Single file selections

        **Note:**

        Remember to make the string size big enough for multiple file
        selections. In the case of multiple selections the names will be separated
        by a semicolon and only the first file will contain the full path.
        
        When using the multiple flag on any of these functions please be aware that
        the string returned will be in the format:
        drive:\\path1\\path2\\name.grid|name2.grid|name3.grid(QUALIFIERS)
        All grids are required to be of the same type.
        """
        ret_val, psz_file_path.value = gxapi_cy.WrapGUI.dat_file_form(GXContext._get_tls_geo(), title.encode(), default.encode(), psz_file_path.value.encode(), type, validation_type, multi)
        return ret_val



    @classmethod
    def gen_file_form(cls, title, filt_vv, filter, default, file_path, type, multi):
        """
        General file Open/Save Form for Multiple/Single file selections and multiple filter capability

        **Note:**

        Remember to make the string size big enough for multiple file
        selections. In the case of multiple selections the names will be separated
        by a semicolon and only the first file will contain the full path.
        
        Defined Functions     The following four functions are handy defines and simply pass the appropriate
        parameter.
        
        iFileOpen_GUI
        iFileSave_GUI
        iMultiFileOpen_GUI
        iMultiFileSave_GUI
        """
        ret_val, file_path.value = gxapi_cy.WrapGUI.gen_file_form(GXContext._get_tls_geo(), title.encode(), filt_vv._wrapper, filter, default.encode(), file_path.value.encode(), type, multi)
        return ret_val



    @classmethod
    def custom_file_form(cls, title, filter, default, file_path, type, multi):
        """
        General file Open/Save Form for Multiple/Single file selections and custom filter capability

        **Note:**

        Remember to make the string size big enough for multiple file
        selections. In the case of multiple selections the names will be separated
        by a semicolon and only the first file will contain the full path.
        """
        ret_val, file_path.value = gxapi_cy.WrapGUI.custom_file_form(GXContext._get_tls_geo(), title.encode(), filter.encode(), default.encode(), file_path.value.encode(), type, multi)
        return ret_val



    @classmethod
    def import_drill_database_ado2(cls, connect, temp, table, type, reg):
        """
        Same as `import_drill_database_ado`, but template name is returned.

        **Note:**

        If it is not defined on input, the template name is set
        to be the Wholeplot table name; e.g.
        "HOLESURVEY.i4" for "Project_HOLESURVEY"
        """
        ret_val, temp.value, table.value, type.value = gxapi_cy.WrapGUI.import_drill_database_ado2(GXContext._get_tls_geo(), connect.encode(), temp.value.encode(), table.value.encode(), type.value, reg._wrapper)
        return ret_val



    @classmethod
    def import_drill_database_esri(cls, connect, temp, table, type, geochem, reg):
        """
        Same as iImportDrillDatabaseADO2_GUI, but from an ArcGIS Geodatabase

        **Note:**

        If it is not defined on input, the template name is set
        to be the Wholeplot table name; e.g.
        "HOLESURVEY.i4" for "Project_HOLESURVEY"
        """
        ret_val, temp.value, table.value, type.value = gxapi_cy.WrapGUI.import_drill_database_esri(GXContext._get_tls_geo(), connect.encode(), temp.value.encode(), table.value.encode(), type.value, geochem, reg._wrapper)
        return ret_val



    @classmethod
    def import_drill_database_odbc(cls, connect, temp, table, type, reg):
        """
        Generate a template file for importing drill holes
        from ODBC database data.

        **Note:**

        If the input connection string is empty (""), then the ODBC connection dialogs
        will appear (e.g. to connect to a machine database) before the import wizard
        is run. The connect string used for this connection is then returned.
        This string can then be used on input to skip the ODBC connection dialogs and
        go straight to the Wholeplot import wizard.
        Because the name of the database is not necessarily known, the template name is created
        from the name of the table opened - e.g. "HOLELOCATION.i4".
        """
        ret_val, connect.value, temp.value, table.value, type.value = gxapi_cy.WrapGUI.import_drill_database_odbc(GXContext._get_tls_geo(), connect.value.encode(), temp.value.encode(), table.value.encode(), type.value, reg._wrapper)
        return ret_val



    @classmethod
    def import_drill_database_odbc_maxwell(cls, connect, temp, table, type, reg):
        """
        Same as `import_drill_database_odbc` but customized for Maxwell.

        **Note:**

        Same as `import_drill_database_odbc` but customized for Maxwell.
        """
        ret_val, connect.value, temp.value, table.value, type.value = gxapi_cy.WrapGUI.import_drill_database_odbc_maxwell(GXContext._get_tls_geo(), connect.value.encode(), temp.value.encode(), table.value.encode(), type.value, reg._wrapper)
        return ret_val



    @classmethod
    def import_ascii_wizard(cls, name, temp):
        """
        Generate a template file from a gui.
        """
        ret_val = gxapi_cy.WrapGUI.import_ascii_wizard(GXContext._get_tls_geo(), name.encode(), temp.encode())
        return ret_val



    @classmethod
    def import_chem_database(cls, name, temp, table, type):
        """
        Generate a template file for importing Geochems Database.
        """
        ret_val, table.value = gxapi_cy.WrapGUI.import_chem_database(GXContext._get_tls_geo(), name.encode(), temp.encode(), table.value.encode(), type)
        return ret_val



    @classmethod
    def import_chem_database_ado(cls, connect, temp, table, type):
        """
        Improved template creation for importing geochem database (ADO).

        **Note:**

        This is an improved version of ImportChemDatabase_GUI using the
        new ADO technology, as opposed to DAO. Use in conjuction with
        `GXDU.import_ado`. See also ImportDatabaseADO_GUI.
        """
        ret_val, table.value = gxapi_cy.WrapGUI.import_chem_database_ado(GXContext._get_tls_geo(), connect.encode(), temp.encode(), table.value.encode(), type)
        return ret_val



    @classmethod
    def import_database(cls, name, temp, table):
        """
        Create template to import an external database table.

        **Note:**

        This is used to select a single database table, and
        selected fields from that table. If the database is not
        Microsoft Access (type .mdb), an introductory dialog
        requests the file type.
        This function DOES NOT import the table itself, but
        creates an import template which may be used to import
        the table (see `GXDU.import_dao`()).
        """
        ret_val, table.value = gxapi_cy.WrapGUI.import_database(GXContext._get_tls_geo(), name.encode(), temp.encode(), table.value.encode())
        return ret_val



    @classmethod
    def import_database_ado(cls, connect, temp, table):
        """
        Create template to import an external database table (ADO Version).

        **Note:**

        1. This is used to select a single database table, and
           selected fields from that table.
        
        2. This function DOES NOT import the table itself, but
           creates an import template which may be used to import
           the table (see `GXDU.import_ado`()).
        
        3. If connection string is of type "FILENAME=..." the connection will attempt to resolve
           it as a file database. (see also ODBCFileConnect_GUI)
        """
        ret_val, table.value = gxapi_cy.WrapGUI.import_database_ado(GXContext._get_tls_geo(), connect.encode(), temp.encode(), table.value.encode())
        return ret_val



    @classmethod
    def import_database_sql(cls, name, sql, temp, line):
        """
        Create template to import an external database table,
        created using SQL.

        **Note:**

        1. This is used to build an Oasis montaj group (line) from
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
           the data (see `GXDU.import_dao`()).
        
        5. If connection string is of type "FILENAME=..." the connection will attempt to resolve
           it as a file database. (see also ODBCFileConnect_GUI)
        """
        ret_val, line.value = gxapi_cy.WrapGUI.import_database_sql(GXContext._get_tls_geo(), name.encode(), sql.encode(), temp.encode(), line.value.encode())
        return ret_val



    @classmethod
    def import_database_sqlado(cls, connect, sql, temp, line):
        """
        Create template to import an external database table,
        created using SQL (New ADO Version).

        **Note:**

        This is used to build an Oasis montaj group (line) from
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
        the data (see `GXDU.import_dao`()).
        """
        ret_val, line.value = gxapi_cy.WrapGUI.import_database_sqlado(GXContext._get_tls_geo(), connect.encode(), sql.encode(), temp.encode(), line.value.encode())
        return ret_val



    @classmethod
    def import_drill_database_ado(cls, connect, temp, table, type, reg):
        """
        Generate a template file for importing drill holes.

        **Note:**

        This is an improved version of ImportDrillDatabase_GUI using the
        new ADO technology, as opposed to DAO. Use in conjuction with
        `GXDU.import_ado`. See also ImportDatabaseADO_GUI.
        """
        ret_val, table.value, type.value = gxapi_cy.WrapGUI.import_drill_database_ado(GXContext._get_tls_geo(), connect.encode(), temp.encode(), table.value.encode(), type.value, reg._wrapper)
        return ret_val



    @classmethod
    def import_template_sql(cls, name, temp, sql, line):
        """
        Create template to import an external database table; provide query.

        **Note:**

        This is similar to ImportDatabaseSQL_GUI, but dispenses with
        the dialog offering a selection of queries. Instead, the
        user supplies the query as a string.
        
        This function DOES NOT import the table itself, but
        creates an import template which may be used to import
        the data (see `GXDU.import_dao`()).
        """
        ret_val = gxapi_cy.WrapGUI.import_template_sql(GXContext._get_tls_geo(), name.encode(), temp.encode(), sql.encode(), line.encode())
        return ret_val



    @classmethod
    def import_template_sqlado(cls, name, temp, sql, line):
        """
        Create template to import an external database table; provide query.

        **Note:**

        This is similar to ImportDatabaseSQL_GUI, but dispenses with
        the dialog offering a selection of queries. Instead, the
        user supplies the query as a string.
        
        This function DOES NOT import the table itself, but
        creates an import template which may be used to import
        the data (see `GXDU.import_ado`()).
        """
        ret_val = gxapi_cy.WrapGUI.import_template_sqlado(GXContext._get_tls_geo(), name.encode(), temp.encode(), sql.encode(), line.encode())
        return ret_val



    @classmethod
    def import_xyz_template_editor(cls, db, template, size, file):
        """
        Allows the user to edit XYZ import templates
        using a complex dialog. The Template name
        may change during editing.
        """
        ret_val = gxapi_cy.WrapGUI.import_xyz_template_editor(GXContext._get_tls_geo(), db._wrapper, template.encode(), size, file.encode())
        return ret_val



    @classmethod
    def odbc_file_connect(cls, file, connect, usage, table):
        """
        Get the connection string for a file database as well as optional table name and FileUsage attribute

        **Note:**

        If the file extension is "mdb" or "xls" then a Microsoft Access
        or Excel database is assumed. Otherwise, a dialog appears listing
        the installed ODBC file database drivers. If the driver takes a
        directory as a database (FileUsage==1) the table name is also
        returned. This is needed because the table name may or may not include
        the file extension.
        """
        ret_val, connect.value, table.value = gxapi_cy.WrapGUI.odbc_file_connect(GXContext._get_tls_geo(), file.encode(), connect.value.encode(), usage, table.value.encode())
        return ret_val



    @classmethod
    def symbol_form(cls, symb_font, geo_font, weight, symb_num, symb_size, symb_ang, edge_col, fill_col):
        """
        - Select a symbol.

        **Note:**

        Symbols are set on input, and new values returned.
        """
        ret_val, symb_font.value, geo_font.value, weight.value, symb_num.value, symb_size.value, symb_ang.value, edge_col.value, fill_col.value = gxapi_cy.WrapGUI.symbol_form(GXContext._get_tls_geo(), symb_font.value.encode(), geo_font.value, weight.value, symb_num.value, symb_size.value, symb_ang.value, edge_col.value, fill_col.value)
        return ret_val



    @classmethod
    def meta_data_tool(cls, meta, root_token, schema):
        """
        Edit a `GXMETA` object
        """
        ret_val = gxapi_cy.WrapGUI.meta_data_tool(GXContext._get_tls_geo(), meta._wrapper, root_token, schema)
        return ret_val



    @classmethod
    def import_chem_wizard(cls, name, temp, type):
        """
        Generate a template file for importing geochems.
        """
        gxapi_cy.WrapGUI.import_chem_wizard(GXContext._get_tls_geo(), name.encode(), temp.encode(), type)
        



    @classmethod
    def import_drill_wizard(cls, name, temp, table, type, reg):
        """
        Generate a template file for importing drill holes.
        """
        table.value, type.value = gxapi_cy.WrapGUI.import_drill_wizard(GXContext._get_tls_geo(), name.encode(), temp.encode(), table.value.encode(), type.value, reg._wrapper)
        



    @classmethod
    def internet_trust(cls):
        """
        Change the Internet Trust Relationships
        """
        gxapi_cy.WrapGUI.internet_trust(GXContext._get_tls_geo())
        



    @classmethod
    def pattern_form(cls, pat, size, thick, dense, col, back_col):
        """
        - Select a pattern.

        **Note:**

        Pattern values set on input, and new values returned.
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
        ret_val, pat.value, size.value, thick.value, dense.value, col.value, back_col.value = gxapi_cy.WrapGUI.pattern_form(GXContext._get_tls_geo(), pat.value, size.value, thick.value, dense.value, col.value, back_col.value)
        return ret_val



    @classmethod
    def line_pattern_form(cls, pattern, thickness, pitch, colour):
        """
        Select a line pattern.

        **Note:**

        Same as `pattern_form` but for line patterns.
        """
        ret_val, pattern.value, thickness.value, pitch.value, colour.value = gxapi_cy.WrapGUI.line_pattern_form(GXContext._get_tls_geo(), pattern.value, thickness.value, pitch.value, colour.value)
        return ret_val



    @classmethod
    def two_panel_selection(cls, ls_tf, ls_ts, title):
        """
        General purpose two-panel selection.

        **Note:**

        Takes as input two LSTs, one contains all available items,
        the second currently selected items. These are processed,
        and in the left panel are displayed all items in the first
        `GXLST` not in the selection `GXLST`, and on the right all items
        in the first `GXLST` which are in the selection `GXLST`. (Items in
        the selection `GXLST` NOT in the first `GXLST` are ignored).
        Once the user has finalized the selections, the final selections
        are returned in the selection `GXLST`.
        
        Selections and display are based on the `LST_ITEM_NAME` part of the
        `GXLST` item, but on export both the `LST_ITEM_NAME` and `LST_ITEM_VALUE`
        elements of the selected items from the first `GXLST` are transferred
        to the second list for output.
        
        The sConvertToCSV_LST and sConvertFromCSV_LST functions in lst.h
        can be used to convert the selection LSTs to forms that can be
        stored and retrieved from GX parameters (or `GXREG` or INI, etc.).
        """
        ret_val = gxapi_cy.WrapGUI.two_panel_selection(GXContext._get_tls_geo(), ls_tf._wrapper, ls_ts._wrapper, title.encode())
        return ret_val



    @classmethod
    def two_panel_selection2(cls, ls_tf, ls_ts, title):
        """
        Two-panel selection, items not sorted alphabetically.

        **Note:**

        Same as `two_panel_selection`, but the items in the
        two lists are not sorted alphabetically, but are ordered
        exactly as input, and when an item is selected it is
        added at the end of the lists.
        """
        ret_val = gxapi_cy.WrapGUI.two_panel_selection2(GXContext._get_tls_geo(), ls_tf._wrapper, ls_ts._wrapper, title.encode())
        return ret_val



    @classmethod
    def two_panel_selection_ex(cls, ls_tf, ls_ts, sorted, allow_no_select, title):
        """
        Two-panel selection; options for sort and ability to select no items.

        **Note:**

        Same as `two_panel_selection`, but the items in the
        two lists are not sorted alphabetically, but are ordered
        exactly as input, and when an item is selected it is
        added at the end of the lists.
        """
        ret_val = gxapi_cy.WrapGUI.two_panel_selection_ex(GXContext._get_tls_geo(), ls_tf._wrapper, ls_ts._wrapper, sorted, allow_no_select, title.encode())
        return ret_val



    @classmethod
    def two_panel_selection_ex2(cls, ls_tf, ls_ts, sorted, allow_no_select, title, help):
        """
        Two-panel selection; extended options including a help link.

        **Note:**

        Same as `two_panel_selection_ex`, but user can specify a help
        link.
        """
        ret_val = gxapi_cy.WrapGUI.two_panel_selection_ex2(GXContext._get_tls_geo(), ls_tf._wrapper, ls_ts._wrapper, sorted, allow_no_select, title.encode(), help.encode())
        return ret_val



    @classmethod
    def launch_single_geo_dotnetx_tool(cls, dll, func, meta):
        """
        Launch a user created .Net GEOXTOOL ensuring a single instance.
        """
        gxapi_cy.WrapGUI.launch_single_geo_dotnetx_tool(GXContext._get_tls_geo(), dll.encode(), func.encode(), meta._wrapper)
        



    @classmethod
    def launch_geo_dotnetx_tool(cls, dll, func, meta):
        """
        Launch a user created .Net GEOXTOOL.
        """
        gxapi_cy.WrapGUI.launch_geo_dotnetx_tool(GXContext._get_tls_geo(), dll.encode(), func.encode(), meta._wrapper)
        



    @classmethod
    def launch_geo_x_tool(cls, dll, func, meta):
        """
        Launch a user created GEOXTOOL.
        """
        gxapi_cy.WrapGUI.launch_geo_x_tool(GXContext._get_tls_geo(), dll.encode(), func.encode(), meta._wrapper)
        



    @classmethod
    def launch_single_geo_dotnetx_tool_ex(cls, dll, func, meta, align, dock, width, height):
        """
        Launch a user created .Net GEOXTOOL ensuring a single instance.
        """
        gxapi_cy.WrapGUI.launch_single_geo_dotnetx_tool_ex(GXContext._get_tls_geo(), dll.encode(), func.encode(), meta._wrapper, align, dock, width, height)
        



    @classmethod
    def launch_geo_dotnetx_tool_ex(cls, dll, func, meta, align, dock, width, height):
        """
        Launch a user created .Net GEOXTOOL.
        """
        gxapi_cy.WrapGUI.launch_geo_dotnetx_tool_ex(GXContext._get_tls_geo(), dll.encode(), func.encode(), meta._wrapper, align, dock, width, height)
        



    @classmethod
    def launch_geo_x_tool_ex(cls, dll, func, meta, align, dock, width, height):
        """
        Launch a user created GEOXTOOL.
        """
        gxapi_cy.WrapGUI.launch_geo_x_tool_ex(GXContext._get_tls_geo(), dll.encode(), func.encode(), meta._wrapper, align, dock, width, height)
        



    @classmethod
    def meta_data_viewer(cls, meta, root_token, schema):
        """
        View a `GXMETA` object
        """
        gxapi_cy.WrapGUI.meta_data_viewer(GXContext._get_tls_geo(), meta._wrapper, root_token, schema)
        



    @classmethod
    def print_file(cls, file):
        """
        Prints a file to current printer
        """
        gxapi_cy.WrapGUI.print_file(GXContext._get_tls_geo(), file.encode())
        



    @classmethod
    def render_pattern(cls, hdc, h_dc, left, bottom, right, top, pat, size, thick, col, back_col, p12, p13, p14):
        """
        - Render a pattern.

        **Note:**

        Renders a Geosoft pattern to a Windows DC.
        """
        gxapi_cy.WrapGUI.render_pattern(GXContext._get_tls_geo(), hdc, h_dc, left, bottom, right, top, pat, size, thick, col, back_col, p12, p13, p14)
        



    @classmethod
    def render_line_pattern(cls, hdc, h_dc, left, bottom, right, top, pattern, thickness, pitch, col, p11, p12):
        """
        Render a line pattern.

        **Note:**

        Same as `render_pattern` but for line patterns.
        """
        gxapi_cy.WrapGUI.render_line_pattern(GXContext._get_tls_geo(), hdc, h_dc, left, bottom, right, top, pattern, thickness, pitch, col, p11, p12)
        



    @classmethod
    def set_parent_wnd(cls, wnd):
        """
        Set the current parent WND

        **Note:**

        The parent WND is used by all modal dialogs as a
        parent to ensure the dialog is correctly modal.
        """
        gxapi_cy.WrapGUI.set_parent_wnd(GXContext._get_tls_geo(), wnd)
        



    @classmethod
    def set_printer(cls, printer):
        """
        Sets the Printer.
        """
        gxapi_cy.WrapGUI.set_printer(GXContext._get_tls_geo(), printer.encode())
        



    @classmethod
    def set_prog_always_on(cls, on):
        """
        Ability to set the progress bar to stay visible even
        if main application is processing messages

        **Note:**

        In montaj the progress bar is hidden when the main window
        start processing messages. This is not always desirable
        in some 3rd party apps, hence this function.
        """
        gxapi_cy.WrapGUI.set_prog_always_on(GXContext._get_tls_geo(), on)
        



    @classmethod
    def show_direct_hist(cls, min, max, mean, std_dev, median, items, vv):
        """
        Display histogram of data directly
        """
        gxapi_cy.WrapGUI.show_direct_hist(GXContext._get_tls_geo(), min, max, mean, std_dev, median, items, vv._wrapper)
        



    @classmethod
    def show_hist(cls, st):
        """
        Display Histogram of data from `GXST`
        """
        gxapi_cy.WrapGUI.show_hist(GXContext._get_tls_geo(), st._wrapper)
        



    @classmethod
    def simple_map_dialog(cls, map, title, help_id):
        """
        General purpose map display `GXGUI` with no interaction.

        **Note:**

        This function displays a map in a simple resizable dialog that fits the map into it.
        It is generally useful to display temporary maps as graphs (e.g. variograms).
        """
        gxapi_cy.WrapGUI.simple_map_dialog(GXContext._get_tls_geo(), map._wrapper, title.encode(), help_id.encode())
        



    @classmethod
    def thematic_voxel_info(cls, vox):
        """
        Display GX.Net thematic voxel info `GXGUI`.

        **Note:**

        Displays the thematic voxel codes, colors, total volume for
        each code, and number of valid items (cubes) for each code.
        This is a replacement for the numeric stats done on normal
        numerical voxel grids.
        """
        gxapi_cy.WrapGUI.thematic_voxel_info(GXContext._get_tls_geo(), vox._wrapper)
        



    @classmethod
    def show_3d_viewer_dialog(cls, title, o3dv):
        """
        Display a standalone 3D viewer

        **Note:**

        Any changes made to the 3D View will be persisted.
        """
        gxapi_cy.WrapGUI.show_3d_viewer_dialog(GXContext._get_tls_geo(), title.encode(), o3dv.encode())
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer