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
        A null (undefined) instance of :class:`geosoft.gxapi.GXGUI`
        
        :returns: A null :class:`geosoft.gxapi.GXGUI`
        """
        return cls()

    def is_null(self):
        """
        Check if the instance of :class:`geosoft.gxapi.GXGUI` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of :class:`geosoft.gxapi.GXGUI`, False otherwise.
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
    def fft2_spec_filter(cls, p1, p2):
        """
        Interactive :class:`geosoft.gxapi.GXFFT2` radially averaged power spectrum filter
        """
        gxapi_cy.WrapGUI.fft2_spec_filter(GXContext._get_tls_geo(), p1.encode(), p2.encode())
        



    @classmethod
    def get_parent_wnd(cls):
        """
        Get the current parent window
        """
        ret_val = gxapi_cy.WrapGUI.get_parent_wnd(GXContext._get_tls_geo())
        return ret_val



    @classmethod
    def get_printer_lst(cls, p1):
        """
        Gets a list of all printers.
        """
        gxapi_cy.WrapGUI.get_printer_lst(GXContext._get_tls_geo(), p1._wrapper)
        



    @classmethod
    def get_window_state(cls):
        """
        Retrieve the current state of the Oasis montaj window
        """
        ret_val = gxapi_cy.WrapGUI.get_window_state(GXContext._get_tls_geo())
        return ret_val



    @classmethod
    def set_window_state(cls, p1):
        """
        Changes the state of the Oasis montaj window
        """
        gxapi_cy.WrapGUI.set_window_state(GXContext._get_tls_geo(), p1)
        



    @classmethod
    def get_window_position(cls, p1, p2, p3, p4, p5):
        """
        Get the Oasis montaj window's position state
        """
        p1.value, p2.value, p3.value, p4.value, p5.value = gxapi_cy.WrapGUI.get_window_position(GXContext._get_tls_geo(), p1.value, p2.value, p3.value, p4.value, p5.value)
        



    @classmethod
    def set_window_position(cls, p1, p2, p3, p4, p5):
        """
        Get the Oasis montaj window's position and state
        """
        gxapi_cy.WrapGUI.set_window_position(GXContext._get_tls_geo(), p1, p2, p3, p4, p5)
        



    @classmethod
    def get_client_window_area(cls, p1, p2, p3, p4):
        """
        Get the location of the Oasis montaj client window.

        **Note:**

        Returns the coordinates of the client window area (where MDI document windows are placed).
        The returned coordinates are 0,0 for the minimum X and Y and the window width
        width and height for the maximum X and Y.
        """
        p1.value, p2.value, p3.value, p4.value = gxapi_cy.WrapGUI.get_client_window_area(GXContext._get_tls_geo(), p1.value, p2.value, p3.value, p4.value)
        



    @classmethod
    def grid_stat_hist(cls, p1):
        """
        Display Histogram of grid
        """
        gxapi_cy.WrapGUI.grid_stat_hist(GXContext._get_tls_geo(), p1.encode())
        



    @classmethod
    def voxel_stat_hist(cls, p1):
        """
        Display Histogram of Voxel
        """
        gxapi_cy.WrapGUI.voxel_stat_hist(GXContext._get_tls_geo(), p1.encode())
        



    @classmethod
    def color_form(cls, p1, p2):
        """
        Select a color.

        **Note:**

        Color value is set on input, and new value returned.
        If the input color type is :attr:`geosoft.gxapi.C_TRANSPARENT`, then the color
        is set to white, if any other type is input the output is
        guaranteed to be of the same type.
        
        If the third flag is :attr:`geosoft.gxapi.GS_TRUE` is used, then on exit, if white is
        selected, the user is prompted: 'Do you want white (Yes) or
        "None" (No) ?' and the color is converted as requested.
        If this is not the case, the :attr:`geosoft.gxapi.C_TRANSPARENT` is converted
        to white (if "Ok" is selected) and no choice is offered.
        """
        ret_val, p1.value = gxapi_cy.WrapGUI.color_form(GXContext._get_tls_geo(), p1.value, p2)
        return ret_val



    @classmethod
    def color_transform(cls, p1, p2):
        """
        Define an :class:`geosoft.gxapi.GXITR` of up to 8 zones.

        **Note:**

        The statistics object is required in order to determine
        data ranges, percentiles, etc. Create it using
        CreateExact_ST, or be sure to enable histogram statistics.
        """
        ret_val = gxapi_cy.WrapGUI.color_transform(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper)
        return ret_val



    @classmethod
    def coord_sys_wizard(cls, p1, p2, p3, p4, p5):
        """
        Launch the coordinate system definition/display :class:`geosoft.gxapi.GXGUI`.

        **Note:**

        Launches the new GX.Net single-dialog coordinate system
        definition dialog. The input :class:`geosoft.gxapi.GXIPJ` is modified on return
        if OK is selected (and the editable parameter is 1).
        The "Data source label" and "Data source" is information displayed
        in the dialog for the user to know where the :class:`geosoft.gxapi.GXIPJ` came from (e.g. "Grid: X.grd")
        """
        ret_val = gxapi_cy.WrapGUI.coord_sys_wizard(GXContext._get_tls_geo(), p1._wrapper, p2, p3, p4.encode(), p5.encode())
        return ret_val



    @classmethod
    def coord_sys_wizard_licensed(cls, p1, p2, p3, p4, p5):
        """
        Launch the coordinate system definition/display :class:`geosoft.gxapi.GXGUI`.

        **Note:**

        Same as iCoordSysWizardLicensed_GUI but will always be editable. The other
        method is not editable in the viewer while this one is.
        """
        ret_val = gxapi_cy.WrapGUI.coord_sys_wizard_licensed(GXContext._get_tls_geo(), p1._wrapper, p2, p3, p4.encode(), p5.encode())
        return ret_val



    @classmethod
    def coord_sys_wizard_grid(cls, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13):
        """
        Launch the coordinate system definition/display :class:`geosoft.gxapi.GXGUI`.

        **Note:**

        Same as iCoordSysWizardLicensed_GUI but allows the original grid info to be adjusted
        when projections on section or oriented plan grids are modified.
        In the tool, it is the "modified" orientation required to keep the edited projection's grid
        in the same location as it was in the target projection.
        """
        ret_val, p9.value, p10.value, p11.value, p12.value, p13.value = gxapi_cy.WrapGUI.coord_sys_wizard_grid(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3, p4, p5.encode(), p6.encode(), p7, p8, p9.value, p10.value, p11.value, p12.value, p13.value)
        return ret_val



    @classmethod
    def database_type(cls, p1, p2):
        """
        Returns the type string of an external DAO database.

        **Note:**

        If the file extension is "mdb", then an MSJET (Microsoft Access)
        database is assumed. If the file name is "ODBC", then "ODBC" is
        returned as the type. Otherwise, a dialog appears listing the
        other valid DAO database types.
        """
        ret_val, p2.value = gxapi_cy.WrapGUI.database_type(GXContext._get_tls_geo(), p1.encode(), p2.value.encode())
        return ret_val



    @classmethod
    def datamine_type(cls, p1, p2):
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
        ret_val, p2.value = gxapi_cy.WrapGUI.datamine_type(GXContext._get_tls_geo(), p1.encode(), p2.value)
        return ret_val



    @classmethod
    def export_xyz_template_editor(cls, p1, p2, p3):
        """
        Allows the user to edit XYZ export template
        using a complex dialog. The Template name
        may change during editing.

        **Note:**

        Only uses the current :class:`geosoft.gxapi.GXDB`. This function does
        not exactly work as supposed to. Instead of using
        the :class:`geosoft.gxapi.GXEDB` handle passed to it, it only will use
        the current :class:`geosoft.gxapi.GXDB`. Please see ExportXYXTemplateEditorEx_GUI
        for an updated function.
        """
        ret_val = gxapi_cy.WrapGUI.export_xyz_template_editor(GXContext._get_tls_geo(), p1._wrapper, p2.encode(), p3)
        return ret_val



    @classmethod
    def export_xyz_template_editor_ex(cls, p1, p2):
        """
        Allows the user to edit an XYZ export template
        using a complex dialog. The template name
        may change during editing.

        **Note:**

        Will use the :class:`geosoft.gxapi.GXEDB` passed in. This function replaces
        the 'buggy' function ExportXYZTemplateEditor_GUI.
        This extended function actually uses the :class:`geosoft.gxapi.GXEDB` handle
        passed to it and not just the current :class:`geosoft.gxapi.GXDB`.
        """
        ret_val, p2.value = gxapi_cy.WrapGUI.export_xyz_template_editor_ex(GXContext._get_tls_geo(), p1._wrapper, p2.value.encode())
        return ret_val



    @classmethod
    def file_filter_index(cls, p1):
        """
        Return the FILE_FILTER_XXX value for a file filter string.

        **Note:**

        For example, if "Database (``*.gdb``)" is input,
        then the :attr:`geosoft.gxapi.FILE_FILTER_GDB` value is returned.
        """
        ret_val = gxapi_cy.WrapGUI.file_filter_index(GXContext._get_tls_geo(), p1.encode())
        return ret_val



    @classmethod
    def gcs_datum_warning_shp(cls, p1, p2):
        """
        Launch the GCS Datum Warning dialog for :class:`geosoft.gxapi.GXSHP` files.

        **Note:**

        Runs the GCS Warning dialog with one data source
        """
        ret_val = gxapi_cy.WrapGUI.gcs_datum_warning_shp(GXContext._get_tls_geo(), p1.encode(), p2._wrapper)
        return ret_val



    @classmethod
    def gcs_datum_warning_shpdb_ex(cls, p1, p2, p3, p4):
        """
        Launch the GCS Datum Warning dialog for :class:`geosoft.gxapi.GXSHP` files (Database).

        **Note:**

        Runs the GCS Warning dialog with multiple data sources (Database)
        """
        ret_val = gxapi_cy.WrapGUI.gcs_datum_warning_shpdb_ex(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3._wrapper, p4._wrapper)
        return ret_val



    @classmethod
    def gcs_datum_warning_shp_ex(cls, p1, p2, p3, p4):
        """
        Launch the GCS Datum Warning dialog for :class:`geosoft.gxapi.GXSHP` files.

        **Note:**

        Runs the GCS Warning dialog with multiple data sources
        """
        ret_val = gxapi_cy.WrapGUI.gcs_datum_warning_shp_ex(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3._wrapper, p4._wrapper)
        return ret_val



    @classmethod
    def get_area_of_interest(cls, p1, p2, p3, p4, p5, p6):
        """
        Get the current area of interest from the application.

        **Note:**

        Depending on what is currently visible on screen and
        the defined coordinate system the user may be prompted
        by a warning and optionaly cancel the process.
        """
        ret_val, p1.value, p2.value, p3.value, p4.value = gxapi_cy.WrapGUI.get_area_of_interest(GXContext._get_tls_geo(), p1.value, p2.value, p3.value, p4.value, p5._wrapper, p6._wrapper)
        return ret_val



    @classmethod
    def get_area_of_interest_3d(cls, p1, p2, p3, p4, p5, p6, p7, p8):
        """
        Get the current area of interest from the application in 3D.

        **Note:**

        Depending on what is currently visible on screen and
        the defined coordinate system the user may be prompted
        by a warning and optionaly cancel the process.
        """
        ret_val, p1.value, p2.value, p3.value, p4.value, p5.value, p6.value = gxapi_cy.WrapGUI.get_area_of_interest_3d(GXContext._get_tls_geo(), p1.value, p2.value, p3.value, p4.value, p5.value, p6.value, p7._wrapper, p8._wrapper)
        return ret_val



    @classmethod
    def get_dat_defaults(cls, p1, p2, p3, p5):
        """
        Return the user default extension and qualifier for grids/images.

        **Note:**

        The default grid/image filters are normally stored in
        "MONTAJ.DEFAULT_XGD_IN" and "MONTAJ.DEFAULT_XGD_OUT"
        
        If no filter is defined, or the filter is not found
        then "grd" and "GRD" are returned as the default extension
        and qualifier.
        """
        p3.value, p5.value = gxapi_cy.WrapGUI.get_dat_defaults(GXContext._get_tls_geo(), p1, p2, p3.value.encode(), p5.value.encode())
        



    @classmethod
    def get_file_filter(cls, p1, p2, p4, p6, p8):
        """
        Return the defined filter, mask, extension and directory for an input filter.

        **Note:**

        Returns the four parts of the file filter;
        e.g. for :attr:`geosoft.gxapi.FILE_FILTER_GDB` it returns:
        
        Filter:    "Database (``*.gdb``)"
        Mask:      "``*.gdb``"
        Extension: "gdb"
        Directory: ":attr:`geosoft.gxapi.GS_DIRECTORY_NONE`"
        
        This function is useful for constuction open/save dialog
        file filters, especially in GX.Net functions.
        """
        p2.value, p4.value, p6.value, p8.value = gxapi_cy.WrapGUI.get_file_filter(GXContext._get_tls_geo(), p1, p2.value.encode(), p4.value.encode(), p6.value.encode(), p8.value)
        



    @classmethod
    def get_gs_directory(cls, p1, p2):
        """
        Return the directory path for value of `GS_DIRECTORY`.

        **Note:**

        Works along with the IGetFileFilter_GUI function. Note that
        most values of FILE_FILTER_XXX will return :attr:`geosoft.gxapi.GS_DIRECTORY_NONE`,
        and give the current workspace directory.
        
        This function is useful for constuction open/save dialog
        file filters, especially in GX.Net functions.
        """
        p2.value = gxapi_cy.WrapGUI.get_gs_directory(GXContext._get_tls_geo(), p1, p2.value.encode())
        



    @classmethod
    def browse_dir(cls, p1, p2, p3):
        """
        Browses for a specific directory.
        """
        ret_val, p3.value = gxapi_cy.WrapGUI.browse_dir(GXContext._get_tls_geo(), p1.encode(), p2.encode(), p3.value.encode())
        return ret_val



    @classmethod
    def color_transform_ex(cls, p1, p2, p3, p4, p5):
        """
        Define an :class:`geosoft.gxapi.GXITR` of up to 12 zones, with file load/save buttons.

        **Note:**

        The statistics object is required in order to determine
        data ranges, percentiles, etc. Create it using
        CreateExact_ST, or be sure to enable histogram statistics.
        The color transform file name is used as the default when the save
        button is pushed, and is updated both after the load and save buttons
        are pushed by the value input or selected by the user.
        """
        ret_val, p5.value = gxapi_cy.WrapGUI.color_transform_ex(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3, p4, p5.value.encode())
        return ret_val



    @classmethod
    def cumulative_percent(cls, p1, p3):
        """
        Define a percent-based :class:`geosoft.gxapi.GXITR` of up to 12 zones.

        **Note:**

        The :class:`geosoft.gxapi.GXITR` values are interpreted as cumulative percent values, using
        the "PERCENT=1" value in the :class:`geosoft.gxapi.GXITR`'s :class:`geosoft.gxapi.GXREG`.
        
        Note that processes using ITRs do not automatically know to convert between
        percent values and "actual" data values. The :class:`geosoft.gxapi.GXREG` "PERCENT" value is simply
        a flag to indicate to a user that the values are intended to be in the range
        from 0 < x < 100. The :class:`geosoft.gxapi.GXITR` should not, therefore, be applied directly to data
        unless that data is already given in percent.
        
        If the file name is defined on input, the initial :class:`geosoft.gxapi.GXITR` will be loaded from it.
        If it is left blank, a default 5-color transform with
        The color transform file name is used as the default when the save
        button is pushed, and is updated both after the load and save buttons
        are pushed by the value input or selected by the user.
        """
        ret_val, p1.value = gxapi_cy.WrapGUI.cumulative_percent(GXContext._get_tls_geo(), p1.value.encode(), p3._wrapper)
        return ret_val



    @classmethod
    def dat_file_form(cls, p1, p2, p3, p5, p6, p7):
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
        ret_val, p3.value = gxapi_cy.WrapGUI.dat_file_form(GXContext._get_tls_geo(), p1.encode(), p2.encode(), p3.value.encode(), p5, p6, p7)
        return ret_val



    @classmethod
    def gen_file_form(cls, p1, p2, p3, p4, p5, p7, p8):
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
        ret_val, p5.value = gxapi_cy.WrapGUI.gen_file_form(GXContext._get_tls_geo(), p1.encode(), p2._wrapper, p3, p4.encode(), p5.value.encode(), p7, p8)
        return ret_val



    @classmethod
    def custom_file_form(cls, p1, p2, p3, p4, p6, p7):
        """
        General file Open/Save Form for Multiple/Single file selections and custom filter capability

        **Note:**

        Remember to make the string size big enough for multiple file
        selections. In the case of multiple selections the names will be separated
        by a semicolon and only the first file will contain the full path.
        """
        ret_val, p4.value = gxapi_cy.WrapGUI.custom_file_form(GXContext._get_tls_geo(), p1.encode(), p2.encode(), p3.encode(), p4.value.encode(), p6, p7)
        return ret_val



    @classmethod
    def import_drill_database_ado2(cls, p1, p2, p4, p6, p7):
        """
        Same as iImportDrillDatabaseADO_GUI, but template name is returned.

        **Note:**

        If it is not defined on input, the template name is set
        to be the Wholeplot table name; e.g.
        "HOLESURVEY.i4" for "Project_HOLESURVEY"
        """
        ret_val, p2.value, p4.value, p6.value = gxapi_cy.WrapGUI.import_drill_database_ado2(GXContext._get_tls_geo(), p1.encode(), p2.value.encode(), p4.value.encode(), p6.value, p7._wrapper)
        return ret_val



    @classmethod
    def import_drill_database_esri(cls, p1, p2, p4, p6, p7, p8):
        """
        Same as iImportDrillDatabaseADO2_GUI, but from an ArcGIS Geodatabase

        **Note:**

        If it is not defined on input, the template name is set
        to be the Wholeplot table name; e.g.
        "HOLESURVEY.i4" for "Project_HOLESURVEY"
        """
        ret_val, p2.value, p4.value, p6.value = gxapi_cy.WrapGUI.import_drill_database_esri(GXContext._get_tls_geo(), p1.encode(), p2.value.encode(), p4.value.encode(), p6.value, p7, p8._wrapper)
        return ret_val



    @classmethod
    def import_drill_database_odbc(cls, p1, p3, p5, p7, p8):
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
        ret_val, p1.value, p3.value, p5.value, p7.value = gxapi_cy.WrapGUI.import_drill_database_odbc(GXContext._get_tls_geo(), p1.value.encode(), p3.value.encode(), p5.value.encode(), p7.value, p8._wrapper)
        return ret_val



    @classmethod
    def import_drill_database_odbc_maxwell(cls, p1, p3, p5, p7, p8):
        """
        Same as IiImportDrillDatabaseODBC_GUI but customized for Maxwell.

        **Note:**

        Same as IiImportDrillDatabaseODBC_GUI but customized for Maxwell.
        """
        ret_val, p1.value, p3.value, p5.value, p7.value = gxapi_cy.WrapGUI.import_drill_database_odbc_maxwell(GXContext._get_tls_geo(), p1.value.encode(), p3.value.encode(), p5.value.encode(), p7.value, p8._wrapper)
        return ret_val



    @classmethod
    def import_ascii_wizard(cls, p1, p2):
        """
        Generate a template file from a gui.
        """
        ret_val = gxapi_cy.WrapGUI.import_ascii_wizard(GXContext._get_tls_geo(), p1.encode(), p2.encode())
        return ret_val



    @classmethod
    def import_chem_database(cls, p1, p2, p3, p5):
        """
        Generate a template file for importing Geochems Database.
        """
        ret_val, p3.value = gxapi_cy.WrapGUI.import_chem_database(GXContext._get_tls_geo(), p1.encode(), p2.encode(), p3.value.encode(), p5)
        return ret_val



    @classmethod
    def import_chem_database_ado(cls, p1, p2, p3, p5):
        """
        Improved template creation for importing geochem database (ADO).

        **Note:**

        This is an improved version of ImportChemDatabase_GUI using the
        new ADO technology, as opposed to DAO. Use in conjuction with
        ImportADO_DU. See also ImportDatabaseADO_GUI.
        """
        ret_val, p3.value = gxapi_cy.WrapGUI.import_chem_database_ado(GXContext._get_tls_geo(), p1.encode(), p2.encode(), p3.value.encode(), p5)
        return ret_val



    @classmethod
    def import_database(cls, p1, p2, p3):
        """
        Create template to import an external database table.

        **Note:**

        This is used to select a single database table, and
        selected fields from that table. If the database is not
        Microsoft Access (type .mdb), an introductory dialog
        requests the file type.
        This function DOES NOT import the table itself, but
        creates an import template which may be used to import
        the table (see ImportDAO_DU()).
        """
        ret_val, p3.value = gxapi_cy.WrapGUI.import_database(GXContext._get_tls_geo(), p1.encode(), p2.encode(), p3.value.encode())
        return ret_val



    @classmethod
    def import_database_ado(cls, p1, p2, p3):
        """
        Create template to import an external database table (ADO Version).

        **Note:**

        1. This is used to select a single database table, and
           selected fields from that table.
        
        2. This function DOES NOT import the table itself, but
           creates an import template which may be used to import
           the table (see ImportADO_DU()).
        
        3. If connection string is of type "FILENAME=..." the connection will attempt to resolve
           it as a file database. (see also ODBCFileConnect_GUI)
        """
        ret_val, p3.value = gxapi_cy.WrapGUI.import_database_ado(GXContext._get_tls_geo(), p1.encode(), p2.encode(), p3.value.encode())
        return ret_val



    @classmethod
    def import_database_sql(cls, p1, p2, p3, p4):
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
           the data (see ImportDAO_DU()).
        
        5. If connection string is of type "FILENAME=..." the connection will attempt to resolve
           it as a file database. (see also ODBCFileConnect_GUI)
        """
        ret_val, p4.value = gxapi_cy.WrapGUI.import_database_sql(GXContext._get_tls_geo(), p1.encode(), p2.encode(), p3.encode(), p4.value.encode())
        return ret_val



    @classmethod
    def import_database_sqlado(cls, p1, p2, p3, p4):
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
        the data (see ImportDAO_DU()).
        """
        ret_val, p4.value = gxapi_cy.WrapGUI.import_database_sqlado(GXContext._get_tls_geo(), p1.encode(), p2.encode(), p3.encode(), p4.value.encode())
        return ret_val



    @classmethod
    def import_drill_database_ado(cls, p1, p2, p3, p5, p6):
        """
        Generate a template file for importing drill holes.

        **Note:**

        This is an improved version of ImportDrillDatabase_GUI using the
        new ADO technology, as opposed to DAO. Use in conjuction with
        ImportADO_DU. See also ImportDatabaseADO_GUI.
        """
        ret_val, p3.value, p5.value = gxapi_cy.WrapGUI.import_drill_database_ado(GXContext._get_tls_geo(), p1.encode(), p2.encode(), p3.value.encode(), p5.value, p6._wrapper)
        return ret_val



    @classmethod
    def import_template_sql(cls, p1, p2, p3, p4):
        """
        Create template to import an external database table; provide query.

        **Note:**

        This is similar to ImportDatabaseSQL_GUI, but dispenses with
        the dialog offering a selection of queries. Instead, the
        user supplies the query as a string.
        
        This function DOES NOT import the table itself, but
        creates an import template which may be used to import
        the data (see ImportDAO_DU()).
        """
        ret_val = gxapi_cy.WrapGUI.import_template_sql(GXContext._get_tls_geo(), p1.encode(), p2.encode(), p3.encode(), p4.encode())
        return ret_val



    @classmethod
    def import_template_sqlado(cls, p1, p2, p3, p4):
        """
        Create template to import an external database table; provide query.

        **Note:**

        This is similar to ImportDatabaseSQL_GUI, but dispenses with
        the dialog offering a selection of queries. Instead, the
        user supplies the query as a string.
        
        This function DOES NOT import the table itself, but
        creates an import template which may be used to import
        the data (see ImportADO_DU()).
        """
        ret_val = gxapi_cy.WrapGUI.import_template_sqlado(GXContext._get_tls_geo(), p1.encode(), p2.encode(), p3.encode(), p4.encode())
        return ret_val



    @classmethod
    def import_xyz_template_editor(cls, p1, p2, p3, p4):
        """
        Allows the user to edit XYZ import templates
        using a complex dialog. The Template name
        may change during editing.
        """
        ret_val = gxapi_cy.WrapGUI.import_xyz_template_editor(GXContext._get_tls_geo(), p1._wrapper, p2.encode(), p3, p4.encode())
        return ret_val



    @classmethod
    def odbc_file_connect(cls, p1, p2, p4, p5):
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
        ret_val, p2.value, p5.value = gxapi_cy.WrapGUI.odbc_file_connect(GXContext._get_tls_geo(), p1.encode(), p2.value.encode(), p4, p5.value.encode())
        return ret_val



    @classmethod
    def symbol_form(cls, p1, p3, p4, p5, p6, p7, p8, p9):
        """
        - Select a symbol.

        **Note:**

        Symbols are set on input, and new values returned.
        """
        ret_val, p1.value, p3.value, p4.value, p5.value, p6.value, p7.value, p8.value, p9.value = gxapi_cy.WrapGUI.symbol_form(GXContext._get_tls_geo(), p1.value.encode(), p3.value, p4.value, p5.value, p6.value, p7.value, p8.value, p9.value)
        return ret_val



    @classmethod
    def meta_data_tool(cls, p1, p2, p3):
        """
        Edit a :class:`geosoft.gxapi.GXMETA` object
        """
        ret_val = gxapi_cy.WrapGUI.meta_data_tool(GXContext._get_tls_geo(), p1._wrapper, p2, p3)
        return ret_val



    @classmethod
    def import_chem_wizard(cls, p1, p2, p3):
        """
        Generate a template file for importing geochems.
        """
        gxapi_cy.WrapGUI.import_chem_wizard(GXContext._get_tls_geo(), p1.encode(), p2.encode(), p3)
        



    @classmethod
    def import_drill_wizard(cls, p1, p2, p3, p4, p5, p6):
        """
        Generate a template file for importing drill holes.
        """
        p5.value = gxapi_cy.WrapGUI.import_drill_wizard(GXContext._get_tls_geo(), p1.encode(), p2.encode(), p3.encode(), p4, p5.value, p6._wrapper)
        



    @classmethod
    def internet_trust(cls):
        """
        Change the Internet Trust Relationships
        """
        gxapi_cy.WrapGUI.internet_trust(GXContext._get_tls_geo())
        



    @classmethod
    def pattern_form(cls, p1, p2, p3, p4, p5, p6):
        """
        - Select a pattern.

        **Note:**

        Pattern values set on input, and new values returned.
        Solid fill is indicated by Pattern number 0.
        
        Returned Values (not set on input)
        
        Size:    pattern tile size in mm.
        Thick:   pattern line thickness in percent of the tile size.
                 valid range is 0-100.
        Density: Tile spacing. A value of 1 means tiles are laid with no overlap.
                 A value of 2 means they overlap each other.
        
        The pattern Angle and Style parameters are not user-definable.
        """
        ret_val, p1.value, p2.value, p3.value, p4.value, p5.value, p6.value = gxapi_cy.WrapGUI.pattern_form(GXContext._get_tls_geo(), p1.value, p2.value, p3.value, p4.value, p5.value, p6.value)
        return ret_val



    @classmethod
    def line_pattern_form(cls, p1, p2, p3, p4):
        """
        Select a line pattern.

        **Note:**

        Same as iPatternForm_GUI but for line patterns.
        """
        ret_val, p1.value, p2.value, p3.value, p4.value = gxapi_cy.WrapGUI.line_pattern_form(GXContext._get_tls_geo(), p1.value, p2.value, p3.value, p4.value)
        return ret_val



    @classmethod
    def two_panel_selection(cls, p1, p2, p3):
        """
        General purpose two-panel selection.

        **Note:**

        Takes as input two LSTs, one contains all available items,
        the second currently selected items. These are processed,
        and in the left panel are displayed all items in the first
        :class:`geosoft.gxapi.GXLST` not in the selection :class:`geosoft.gxapi.GXLST`, and on the right all items
        in the first :class:`geosoft.gxapi.GXLST` which are in the selection :class:`geosoft.gxapi.GXLST`. (Items in
        the selection :class:`geosoft.gxapi.GXLST` NOT in the first :class:`geosoft.gxapi.GXLST` are ignored).
        Once the user has finalized the selections, the final selections
        are returned in the selection :class:`geosoft.gxapi.GXLST`.
        
        Selections and display are based on the :attr:`geosoft.gxapi.LST_ITEM_NAME` part of the
        :class:`geosoft.gxapi.GXLST` item, but on export both the :attr:`geosoft.gxapi.LST_ITEM_NAME` and :attr:`geosoft.gxapi.LST_ITEM_VALUE`
        elements of the selected items from the first :class:`geosoft.gxapi.GXLST` are transferred
        to the second list for output.
        
        The sConvertToCSV_LST and sConvertFromCSV_LST functions in lst.h
        can be used to convert the selection LSTs to forms that can be
        stored and retrieved from GX parameters (or :class:`geosoft.gxapi.GXREG` or INI, etc.).
        """
        ret_val = gxapi_cy.WrapGUI.two_panel_selection(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3.encode())
        return ret_val



    @classmethod
    def two_panel_selection2(cls, p1, p2, p3):
        """
        Two-panel selection, items not sorted alphabetically.

        **Note:**

        Same as iTwoPanelSelection_GUI, but the items in the
        two lists are not sorted alphabetically, but are ordered
        exactly as input, and when an item is selected it is
        added at the end of the lists.
        """
        ret_val = gxapi_cy.WrapGUI.two_panel_selection2(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3.encode())
        return ret_val



    @classmethod
    def two_panel_selection_ex(cls, p1, p2, p3, p4, p5):
        """
        Two-panel selection; options for sort and ability to select no items.

        **Note:**

        Same as iTwoPanelSelection_GUI, but the items in the
        two lists are not sorted alphabetically, but are ordered
        exactly as input, and when an item is selected it is
        added at the end of the lists.
        """
        ret_val = gxapi_cy.WrapGUI.two_panel_selection_ex(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3, p4, p5.encode())
        return ret_val



    @classmethod
    def two_panel_selection_ex2(cls, p1, p2, p3, p4, p5, p6):
        """
        Two-panel selection; extended options including a help link.

        **Note:**

        Same as iTwoPanelSelectionEx_GUI, but user can specify a help
        link.
        """
        ret_val = gxapi_cy.WrapGUI.two_panel_selection_ex2(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3, p4, p5.encode(), p6.encode())
        return ret_val



    @classmethod
    def launch_single_geo_dotnetx_tool(cls, p1, p2, p3):
        """
        Launch a user created .Net GEOXTOOL ensuring a single instance.
        """
        gxapi_cy.WrapGUI.launch_single_geo_dotnetx_tool(GXContext._get_tls_geo(), p1.encode(), p2.encode(), p3._wrapper)
        



    @classmethod
    def launch_geo_dotnetx_tool(cls, p1, p2, p3):
        """
        Launch a user created .Net GEOXTOOL.
        """
        gxapi_cy.WrapGUI.launch_geo_dotnetx_tool(GXContext._get_tls_geo(), p1.encode(), p2.encode(), p3._wrapper)
        



    @classmethod
    def launch_geo_x_tool(cls, p1, p2, p3):
        """
        Launch a user created GEOXTOOL.
        """
        gxapi_cy.WrapGUI.launch_geo_x_tool(GXContext._get_tls_geo(), p1.encode(), p2.encode(), p3._wrapper)
        



    @classmethod
    def launch_single_geo_dotnetx_tool_ex(cls, p1, p2, p3, p4, p5, p6, p7):
        """
        Launch a user created .Net GEOXTOOL ensuring a single instance.
        """
        gxapi_cy.WrapGUI.launch_single_geo_dotnetx_tool_ex(GXContext._get_tls_geo(), p1.encode(), p2.encode(), p3._wrapper, p4, p5, p6, p7)
        



    @classmethod
    def launch_geo_dotnetx_tool_ex(cls, p1, p2, p3, p4, p5, p6, p7):
        """
        Launch a user created .Net GEOXTOOL.
        """
        gxapi_cy.WrapGUI.launch_geo_dotnetx_tool_ex(GXContext._get_tls_geo(), p1.encode(), p2.encode(), p3._wrapper, p4, p5, p6, p7)
        



    @classmethod
    def launch_geo_x_tool_ex(cls, p1, p2, p3, p4, p5, p6, p7):
        """
        Launch a user created GEOXTOOL.
        """
        gxapi_cy.WrapGUI.launch_geo_x_tool_ex(GXContext._get_tls_geo(), p1.encode(), p2.encode(), p3._wrapper, p4, p5, p6, p7)
        



    @classmethod
    def meta_data_viewer(cls, p1, p2, p3):
        """
        View a :class:`geosoft.gxapi.GXMETA` object
        """
        gxapi_cy.WrapGUI.meta_data_viewer(GXContext._get_tls_geo(), p1._wrapper, p2, p3)
        



    @classmethod
    def print_file(cls, p1):
        """
        Prints a file to current printer
        """
        gxapi_cy.WrapGUI.print_file(GXContext._get_tls_geo(), p1.encode())
        



    @classmethod
    def render_pattern(cls, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14):
        """
        - Render a pattern.

        **Note:**

        Renders a Geosoft pattern to a Windows DC.
        """
        gxapi_cy.WrapGUI.render_pattern(GXContext._get_tls_geo(), p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14)
        



    @classmethod
    def render_line_pattern(cls, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12):
        """
        Render a line pattern.

        **Note:**

        Same as RenderPattern_GUI but for line patterns.
        """
        gxapi_cy.WrapGUI.render_line_pattern(GXContext._get_tls_geo(), p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12)
        



    @classmethod
    def set_parent_wnd(cls, p1):
        """
        Set the current parent WND

        **Note:**

        The parent WND is used by all modal dialogs as a
        parent to ensure the dialog is correctly modal.
        """
        gxapi_cy.WrapGUI.set_parent_wnd(GXContext._get_tls_geo(), p1)
        



    @classmethod
    def set_printer(cls, p1):
        """
        Sets the Printer.
        """
        gxapi_cy.WrapGUI.set_printer(GXContext._get_tls_geo(), p1.encode())
        



    @classmethod
    def set_prog_always_on(cls, p1):
        """
        Ability to set the progress bar to stay visible even
        if main application is processing messages

        **Note:**

        In montaj the progress bar is hidden when the main window
        start processing messages. This is not always desirable
        in some 3rd party apps, hence this function.
        """
        gxapi_cy.WrapGUI.set_prog_always_on(GXContext._get_tls_geo(), p1)
        



    @classmethod
    def show_direct_hist(cls, p1, p2, p3, p4, p5, p6, p7):
        """
        Display histogram of data directly
        """
        gxapi_cy.WrapGUI.show_direct_hist(GXContext._get_tls_geo(), p1, p2, p3, p4, p5, p6, p7._wrapper)
        



    @classmethod
    def show_hist(cls, p1):
        """
        Display Histogram of data from :class:`geosoft.gxapi.GXST`
        """
        gxapi_cy.WrapGUI.show_hist(GXContext._get_tls_geo(), p1._wrapper)
        



    @classmethod
    def simple_map_dialog(cls, p1, p2, p3):
        """
        General purpose map display :class:`geosoft.gxapi.GXGUI` with no interaction.

        **Note:**

        This function displays a map in a simple resizable dialog that fits the map into it.
        It is generally useful to display temporary maps as graphs (e.g. variograms).
        """
        gxapi_cy.WrapGUI.simple_map_dialog(GXContext._get_tls_geo(), p1._wrapper, p2.encode(), p3.encode())
        



    @classmethod
    def thematic_voxel_info(cls, p1):
        """
        Display GX.Net thematic voxel info :class:`geosoft.gxapi.GXGUI`.

        **Note:**

        Displays the thematic voxel codes, colors, total volume for
        each code, and number of valid items (cubes) for each code.
        This is a replacement for the numeric stats done on normal
        numerical voxel grids.
        """
        gxapi_cy.WrapGUI.thematic_voxel_info(GXContext._get_tls_geo(), p1._wrapper)
        



    @classmethod
    def show_3d_viewer_dialog(cls, p1, p2):
        """
        Display a standalone 3D viewer

        **Note:**

        Any changes made to the 3D View will be persisted.
        """
        gxapi_cy.WrapGUI.show_3d_viewer_dialog(GXContext._get_tls_geo(), p1.encode(), p2.encode())
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer