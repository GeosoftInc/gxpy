### extends 'class_empty.py'
### block ClassImports
# NOTICE: Do not edit anything here, it is generated code
from typing import NewType
from . import gxapi_cy
from geosoft.gxapi import GXContext, float_ref, int_ref, str_ref
from .GXDB import GXDB
from .GXMAP import GXMAP
from .GXREG import GXREG


### endblock ClassImports

### block Header
# NOTICE: The code generator will not replace the code in this block
### endblock Header

### block ClassImplementation
# NOTICE: Do not edit anything here, it is generated code
class GXDH:
    """
    GXDH class.

    This class is used for importing and interacting with Drill Hole
    data files. For detailed information on Drill Hole data,
    see the documentation for Wholeplot.

    **Note:**

    The `GXDH` class has some defines not used by any functions.
        `DH_DEFINE_PLAN`
        `DH_DEFINE_SECT`
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._wrapper = None

    def __del__(self):
        self._wrapper = None

    def __init__(self, wrapper=None):
        self._wrapper = wrapper if wrapper else gxapi_cy.WrapDH(GXContext._get_tls_geo(), 0)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of `GXDH`
        
        :returns: A null `GXDH`
        """
        return cls()

    def is_null(self):
        """
        Check if the instance of `GXDH` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of `GXDH`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# ArcGIS Target Functions


    @classmethod
    def is_esri(cls):
        """
        Running inside ArcGIS?
        """
        ret_val = gxapi_cy.WrapDH.is_esri(GXContext._get_tls_geo())
        return ret_val




# Data processing/conversion methods



    def creat_chan_lst(self, p2):
        """
        Fills a `GXLST` with available string and numeric channel code values.

        **Note:**

        Channel codes are in the format "[Assay] Au", where the name in
        the square brackets is descriptive part of the project database
        containing the given channel name. The above code might refer to
        the "Au" channel in the "Tutorial_Assay.gdb" database.
        """
        self._wrapper.creat_chan_lst(p2._wrapper)
        




    def depth_data_lst(self, p2):
        """
        Fills a `GXLST` with available channel code values from Depth databases.

        **Note:**

        Channel codes are in the format "[Assay] Au", where the name in
        the square brackets is descriptive part of the project database
        containing the given channel name. The above code might refer to
        the "Au" channel in the "Tutorial_Assay.gdb" database.
        """
        self._wrapper.depth_data_lst(p2._wrapper)
        




    def from_to_data_lst(self, p2, p3):
        """
        Fills a `GXLST` with available string and numeric channel code values from From-To databases.

        **Note:**

        Channel codes are in the format "[Assay] Au", where the name in
        the square brackets is descriptive part of the project database
        containing the given channel name. The above code might refer to
        the "Au" channel in the "Tutorial_Assay.gdb" database.
        """
        self._wrapper.from_to_data_lst(p2.encode(), p3._wrapper)
        




    def get_geology_contacts(self, p2, p3, p4, p5, p6, p7, p8, p9):
        """
        Return XYZ locations of top or bottom geological surfaces

        **Note:**

        For the input `GXLST` of holes, returns XYZ location of top or bottom
        contact with the input geology. Those selected holes which do NOT
        have contacts, return `rDUMMY` for the corresponding locations.
        """
        self._wrapper.get_geology_contacts(p2._wrapper, p3.encode(), p4.encode(), p5, p6, p7._wrapper, p8._wrapper, p9._wrapper)
        




    def get_oriented_core_dip_dir(self, p2, p3, p4, p5, p6, p7):
        """
        Converted alpha/beta values in oriented cores to dip/dip direction.

        **Note:**

        The input data are the oriented core alpha and beta values, using either
        top or bottom reference. The values for each hole in the `GXLST` are converted
        to "absolute" dip and dip-direction values, using the resurveyed hole
        orientations at each depth.
        The alpha and beta data must be from the same database, and the output
        dip and dip/dir channels are written to the same database.
        """
        self._wrapper.get_oriented_core_dip_dir(p2._wrapper, p3.encode(), p4.encode(), p5, p6.encode(), p7.encode())
        




    def get_unique_channel_items(self, p2, p3, p4):
        """
        Return a `GXVV` with unique items in a channel.

        **Note:**

        Finds and sorts all the unique non-dummy items for the selected channel.
        """
        self._wrapper.get_unique_channel_items(p2.encode(), p3, p4._wrapper)
        




    def get_unique_channel_items_from_collar(self, p2, p3, p4):
        """
        Return a `GXVV` with unique items in a channel.

        **Note:**

        Finds and sorts all the unique non-dummy items for the selected channel.
        """
        self._wrapper.get_unique_channel_items_from_collar(p2.encode(), p3, p4._wrapper)
        




    def chan_type(self, p2):
        """
        Return the data type for a channel code.

        **Note:**

        Finds and sorts all the unique non-dummy items for the selected channel.
        """
        ret_val = self._wrapper.chan_type(p2.encode())
        return ret_val




    def find_hole_intersection(self, p2, p3, p4, p5, p6):
        """
        Return XYZ locations of the intersection of a hole with a DEM grid.

        **Note:**

        Input the hole index and an `GXIMG` object. Returns XYZ location
        of the hole intersection with the DEM. Interpolation inside the DEM
        uses the native `GXIMG` interp method. If no intersection is found the
        returned XYZ locations are `rDUMMY`.
        """
        ret_val, p4.value, p5.value, p6.value = self._wrapper.find_hole_intersection(p2, p3._wrapper, p4.value, p5.value, p6.value)
        return ret_val




    def get_chan_code_info(self, p2, p3, p4):
        """
        Return the assay database index and channel name from a channel code string.

        **Note:**

        The input channel code is in the form "[Assay] channel"
        """
        p3.value, p4.value = self._wrapper.get_chan_code_info(p2.encode(), p3.value, p4.value.encode())
        




    def grid_intersection(self, p2, p3, p4, p5, p6, p7, p8, p9, p10):
        """
        Algorithm to determine the intersection of a straight hole with a surface (DEM) grid.

        **Note:**

        Given a point on the hole and the straight hole dip and azimuth,
        ocate (an) intersection point with the input DEM grid.
        """
        ret_val, p8.value, p9.value, p10.value = self._wrapper.grid_intersection(p2, p3, p4, p5, p6, p7.encode(), p8.value, p9.value, p10.value)
        return ret_val




    def litho_grid_3d(self, p2, p3, p4, p5, p6, p7, p8, p9, p10):
        """
        Create a lithology voxel grid with lith codes mapped to single values.

        **Note:**

        Values in the input channel are assigned the index of the corresponding
        item found in the input `GXTPAT`.
        The compositing gap refers to the size of gaps in the data (either
        a blank lithology or missing from-to interval) which will be ignored
        when compositing lithologies into contiguous from-to intervals.
        The non-contact radius is used to dummy out the level grids around holes
        where the gridded lithology is not found. If not specified (dummy) then
        half the distance to the nearest contacting hole is used.
        """
        self._wrapper.litho_grid_3d(p2.encode(), p3._wrapper, p4.encode(), p5, p6, p7, p8, p9._wrapper, p10)
        




    def numeric_chan_lst(self, p2):
        """
        Fills a `GXLST` with available numeric channel code values.

        **Note:**

        Channel codes are in the format "[Assay] Au", where the name in
        the square brackets is descriptive part of the project database
        containing the given channel name. The above code might refer to
        the "Au" channel in the "Tutorial_Assay.gdb" database.
        """
        self._wrapper.numeric_chan_lst(p2._wrapper)
        




    def numeric_from_to_data_lst(self, p2, p3):
        """
        Fills a `GXLST` with available numeric channel code values from From-To databases..

        **Note:**

        Channel codes are in the format "[Assay] Au", where the name in
        the square brackets is descriptive part of the project database
        containing the given channel name. The above code might refer to
        the "Au" channel in the "Tutorial_Assay.gdb" database.
        """
        self._wrapper.numeric_from_to_data_lst(p2.encode(), p3._wrapper)
        




    def punch_grid_holes(self, p2, p3, p4, p5, p6):
        """
        Dummy out locations in a grid around non-contact holes.

        **Note:**

        Grid is dummied out to the blanking distance around holes where
        the input Z value is dummy. If a contacting hole is closer then
        twice the blanking distance, the blanking distance is reduced
        accordingly. Distances are measured horizontally (e.g. Z is ignored).
        If the blanking distance is zero or dummy, the distance is
        automatically set to half the distance to the closest hole intersection.
        """
        self._wrapper.punch_grid_holes(p2._wrapper, p3._wrapper, p4._wrapper, p5._wrapper, p6)
        




    def string_chan_lst(self, p2):
        """
        Fills a `GXLST` with available string channel code values.

        **Note:**

        Channel codes are in the format "[Assay] Au", where the name in
        the square brackets is descriptive part of the project database
        containing the given channel name. The above code might refer to
        the "Au" channel in the "Tutorial_Assay.gdb" database.
        """
        self._wrapper.string_chan_lst(p2._wrapper)
        




    def string_from_to_data_lst(self, p2, p3):
        """
        Fills a `GXLST` with available string-type channel code values from From-To databases.

        **Note:**

        Channel codes are in the format "[Geology] Lithology", where the name in
        the square brackets is descriptive part of the project database
        containing the given channel name. The above code might refer to
        the "Lithology" channel in the "Tutorial_Geology.gdb" database.
        """
        self._wrapper.string_from_to_data_lst(p2.encode(), p3._wrapper)
        




# Miscellaneous



    def h_assay_db(self, p2):
        """
        Database for an assay data set.

        **Note:**

        Works for both single and multiple `GXDB` Wholeplots.
        """
        ret_val = self._wrapper.h_assay_db(p2)
        return GXDB(ret_val)




    def h_assay_symb(self, p2, p3):
        """
        Line/Group symbol for a specific assay data set hole.

        **Note:**

        Works for both single and multiple `GXDB` Wholeplots.
        """
        ret_val = self._wrapper.h_assay_symb(p2, p3)
        return ret_val




    def h_collar_db(self):
        """
        Database for the collar table.

        **Note:**

        Works for both single and multiple `GXDB` Wholeplots.
        """
        ret_val = self._wrapper.h_collar_db()
        return GXDB(ret_val)




    def h_collar_symb(self):
        """
        Line/Group symbol for the collar table.

        **Note:**

        Works for both single and multiple `GXDB` Wholeplots.
        """
        ret_val = self._wrapper.h_collar_symb()
        return ret_val




    def h_dip_az_survey_db(self):
        """
        Database for the Dip-Azimuth survey data

        **Note:**

        Works for both single and multiple `GXDB` Wholeplots.
        """
        ret_val = self._wrapper.h_dip_az_survey_db()
        return GXDB(ret_val)




    def h_dip_az_survey_symb(self, p2):
        """
        Line/Group symbol for a specific hole Dip-Azimuth survey.

        **Note:**

        Works for both single and multiple `GXDB` Wholeplots.
        """
        ret_val = self._wrapper.h_dip_az_survey_symb(p2)
        return ret_val




    def h_en_survey_db(self):
        """
        Database for the East-North survey data

        **Note:**

        Works for both single and multiple `GXDB` Wholeplots.
        """
        ret_val = self._wrapper.h_en_survey_db()
        return GXDB(ret_val)




    def h_en_survey_symb(self, p2):
        """
        Line/Group symbol for a specific hole East-North survey.

        **Note:**

        Works for both single and multiple `GXDB` Wholeplots.
        """
        ret_val = self._wrapper.h_en_survey_symb(p2)
        return ret_val




    def add_survey_table(self, p2):
        """
        Add a survey table for a new hole.

        **Note:**

        The information is created from the collar table info.
        If the survey info already exists, does nothing.
        """
        self._wrapper.add_survey_table(p2)
        




    def assay_hole_lst(self, p2, p3):
        """
        Populate an `GXLST` with holes in an assay database
        """
        self._wrapper.assay_hole_lst(p2, p3._wrapper)
        




    def assay_lst(self, p2):
        """
        Return the `GXLST` of from-to and point assay datasets

        **Note:**

        Assay dataset name is given as `LST_ITEM_NAME`
        Assay dataset number is given as `LST_ITEM_VALUE`
        Returns an empty `GXLST` if no datasets.
        """
        self._wrapper.assay_lst(p2._wrapper)
        



    @classmethod
    def auto_select_holes(cls, p1):
        """
        Use automatic hole selection based on slice.
        """
        gxapi_cy.WrapDH.auto_select_holes(GXContext._get_tls_geo(), p1)
        




    def clean(self):
        """
        Delete extraneous holes from project databases.

        **Note:**

        Removes from Project databases any lines not connected to
        a line found in the collar table list.
        If all the database lines would be removed, the database is
        simply deleted.
        """
        self._wrapper.clean()
        




    def composite_db(self, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14):
        """
        Make a composite database
        """
        self._wrapper.composite_db(p2._wrapper, p3._wrapper, p4, p5, p6, p7.encode(), p8.encode(), p9.encode(), p10, p11, p12, p13, p14.encode())
        




    def compute_hole_xyz(self, p2):
        """
        Computes XYZ for survey and assay data for a single hole.
        """
        self._wrapper.compute_hole_xyz(p2)
        




    def compute_sel_extent(self, p2, p3, p4, p5, p6, p7):
        """
        Computes the extents for selected holes.
        """
        p2.value, p3.value, p4.value, p5.value, p6.value, p7.value = self._wrapper.compute_sel_extent(p2.value, p3.value, p4.value, p5.value, p6.value, p7.value)
        




    def compute_xyz(self):
        """
        Computes XYZ for survey and assay data.
        """
        self._wrapper.compute_xyz()
        



    @classmethod
    def convert_old_line_names(cls, p1, p2):
        """
        Convert old "DD001.Assay" type lines to "DD001"

        **Note:**

        The input `GXLST` must be filled using a function like `GXDB.symb_lst`, which
        puts the name and symbol into the `GXLST` items.
        Any names with a period are truncated at the period, and
        the line name in the database is changed to the new name
        (just the hole name).
        The `GXLST` is modified to have the new names.
        A value is put into the `GXDB` `GXREG` "DH_CONVERTED_NAMES" parameter so
        this process is done only once on a database.
        
        DO NOT use on old-style single-database Wholeplot projects.
        """
        gxapi_cy.WrapDH.convert_old_line_names(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper)
        



    @classmethod
    def create(cls, p1):
        """
        Create `GXDH`.
        """
        ret_val = gxapi_cy.WrapDH.create(GXContext._get_tls_geo(), p1.encode())
        return GXDH(ret_val)




    def create_default_job(self, p2, p3):
        """
        Create a default job from scratch.
        """
        self._wrapper.create_default_job(p2.encode(), p3)
        



    @classmethod
    def create_external(cls, p1):
        """
        Create a `GXDH` from an external process (no montaj running).

        **Note:**

        The regular `create` assumes a workspace is open and creates
        the project from the databases which are currently loaded.
        This function instead creates the project from all projects
        in the input databases's directory.
        """
        ret_val = gxapi_cy.WrapDH.create_external(GXContext._get_tls_geo(), p1.encode())
        return GXDH(ret_val)



    @classmethod
    def current(cls):
        """
        Creates a drill project from current environment.

        **Note:**

        If no `GXDH` database is open the Open `GXDH` Project `GXGUI` will be displayed which may be
        cancelled by the user in which case the GX will terminate with cancel.
        """
        ret_val = gxapi_cy.WrapDH.current(GXContext._get_tls_geo())
        return GXDH(ret_val)



    @classmethod
    def datamine_to_csv(cls, p1, p2):
        """
        Convert a Datamine drillhole file to CSV files ready for import.

        **Note:**

        Creates three CSV files and the accompanying template files
        ready for batch ASCII import into a drill project.
        
             Project_Collar.csv, .i3
             Project_Survey.csv, .i3
             Project_Assay.csv,  .i3
        """
        gxapi_cy.WrapDH.datamine_to_csv(GXContext._get_tls_geo(), p1.encode(), p2.encode())
        




    def delete_holes(self, p2):
        """
        Delete a list of holes from the project.

        **Note:**

        Removes all lines in the input `GXLST` from `GXDH` project databases.
        If all the database lines would be removed, the database is
        simply deleted.
        """
        self._wrapper.delete_holes(p2._wrapper)
        






    def export_file(self, p2, p3):
        """
        Exports a Drill Hole database to an external file.
        """
        self._wrapper.export_file(p2.encode(), p3)
        




    def export_geodatabase_lst(self, p2, p3, p4, p5, p7):
        """
        Exports whole or part of a Drill Hole database to an ArcGIS Geodatabase as feature class(es).

        **Note:**

        A table with metadata about the created feature classes will be written to the Geodatabase. This table will have the same
        name with the postfix "_Metadata" attached
        """
        p5.value = self._wrapper.export_geodatabase_lst(p2._wrapper, p3.encode(), p4.encode(), p5.value.encode(), p7)
        




    def export_las(self, p2, p3, p4, p5):
        """
        Exports a Drill Hole database to a LAS v2 file.
        """
        self._wrapper.export_las(p2, p3, p4, p5.encode())
        




    def export_lst(self, p2, p3, p4):
        """
        Exports a `GXLST` of holes in a Drill Hole database to an external file.

        **Note:**

        Use functions like `GXDB.selected_line_lst` to construct the `GXLST`
        """
        self._wrapper.export_lst(p2._wrapper, p3.encode(), p4)
        




    def flush_select(self):
        """
        Flush all selections to database selection engine.
        """
        self._wrapper.flush_select()
        




    def get_databases_vv(self, p2):
        """
        Get the names of the project databases in a `GXVV`.
        """
        self._wrapper.get_databases_vv(p2._wrapper)
        




    def get_databases_sorted_vv(self, p2):
        """
        Get the names of the project databases in a `GXVV`, same as `get_databases_vv` but the list is sorted alphabetically.
        """
        self._wrapper.get_databases_sorted_vv(p2._wrapper)
        




    def get_data_type(self, p2, p3):
        """
        Get the type of data in a Wholeplot database.

        **Note:**

        Returns `DH_DATA_UNKNOWN` if it can't determine the type.
        """
        p3.value = self._wrapper.get_data_type(p2._wrapper, p3.value)
        




    def get_default_section(self, p2, p3, p4, p5, p6):
        """
        Computes default section azimuths, extents for selected holes.
        """
        p2.value, p3.value, p4.value, p5.value, p6.value = self._wrapper.get_default_section(p2.value, p3.value, p4.value, p5.value, p6.value)
        




    def get_hole_group(self, p2, p3):
        """
        Get the Group symbol for this hole/table combination.
        """
        ret_val = self._wrapper.get_hole_group(p2, p3.encode())
        return ret_val




    def get_hole_survey(self, p2, p3, p4, p5, p6):
        """
        Get the Survey information of a Hole.
        """
        self._wrapper.get_hole_survey(p2, p3._wrapper, p4._wrapper, p5._wrapper, p6._wrapper)
        




    def get_ipj(self, p2):
        """
        Get the project `GXIPJ`.

        **Note:**

        The projection for the project is the projection stored
        in the DH_EAST channel in the collar table.
        """
        self._wrapper.get_ipj(p2._wrapper)
        




    def get_map_names_vv(self, p2):
        """
        Get plotted map names.

        **Note:**

        This will return the currently plotted map name(s)
        in a `GXVV`. This should only be called after a call
        to `wholeplot`. The `GXVV` size is set to the number
        of maps created.
        """
        self._wrapper.get_map_names_vv(p2._wrapper)
        




    def get_map(self, p2):
        """
        Get a plotting map
        """
        ret_val = self._wrapper.get_map(p2)
        return GXMAP(ret_val)




    def get_num_maps(self):
        """
        Get the number plotting maps
        """
        ret_val = self._wrapper.get_num_maps()
        return ret_val




    def get_reg(self):
        """
        Get the `GXREG` Object used in this project.
        """
        ret_val = self._wrapper.get_reg()
        return GXREG(ret_val)




    def get_selected_holes_vv(self, p2):
        """
        Populate a `GXVV` with the indices of all selected holes
        """
        self._wrapper.get_selected_holes_vv(p2._wrapper)
        



    @classmethod
    def get_table_default_chan_lst(cls, p1, p2):
        """
        Return list of default channels by collar/assay/survey table type.

        **Note:**

        Fills a `GXLST` with the default channel names created according to
        type (Collar, Survey, Assay). Value is in the `LST_ITEM_NAME` part.
        """
        gxapi_cy.WrapDH.get_table_default_chan_lst(GXContext._get_tls_geo(), p1._wrapper, p2)
        




    def hole_lst(self, p2):
        """
        Populate an `GXLST` with the list of the selected holes
        """
        self._wrapper.hole_lst(p2._wrapper)
        




    def hole_lst2(self, p2):
        """
        Populate an `GXLST` with the list of all the holes
        """
        self._wrapper.hole_lst2(p2._wrapper)
        




    def add_hole(self, p2):
        """
        Add a hole and return it's index.
        """
        ret_val = self._wrapper.add_hole(p2.encode())
        return ret_val




    def clean_will_delete_db(self):
        """
        See if "cleaning" will delete project databases.
        """
        ret_val = self._wrapper.clean_will_delete_db()
        return ret_val




    def compositing_tool_gui(self, p2, p3, p4, p5):
        """
        Annotate a strip log map using the compositing tool.

        **Note:**

        If any of the input X or Y values are dummies the tool uses default values.
        """
        ret_val = self._wrapper.compositing_tool_gui(p2._wrapper, p3, p4, p5)
        return ret_val



    @classmethod
    def create_collar_table(cls, p1, p2, p3):
        """
        Create a collar table `GXDB` with channels set up.

        **Note:**

        The database name will be of the form
        
        "d:\\directory\\Project_Collar.gdb"
        """
        p3.value = gxapi_cy.WrapDH.create_collar_table(GXContext._get_tls_geo(), p1.encode(), p2, p3.value.encode())
        



    @classmethod
    def create_collar_table_dir(cls, p1, p2, p3, p4):
        """
        Create a collar table in the specified directory.

        **Note:**

        The database name will be of the form
        
        "d:\\directory\\Project_Collar.gdb"
        """
        p4.value = gxapi_cy.WrapDH.create_collar_table_dir(GXContext._get_tls_geo(), p1.encode(), p2.encode(), p3, p4.value.encode())
        




    def delete_will_delete_db(self, p2):
        """
        See if deleting holes will delete project databases.
        """
        ret_val = self._wrapper.delete_will_delete_db(p2._wrapper)
        return ret_val




    def find_hole(self, p2):
        """
        Find a hole and return it's index.
        """
        ret_val = self._wrapper.find_hole(p2.encode())
        return ret_val




    def get_collar_table_db(self, p2):
        """
        Get the name of the database containing the collar table.
        """
        p2.value = self._wrapper.get_collar_table_db(p2.value.encode())
        




    def get_info(self, p2, p3, p4):
        """
        Get Collar Information.

        **Note:**

        If the DH_ELEV channel is requested it will also
        search for the DH_RL channel, which is the new
        name for the collar elevation.
        """
        p4.value = self._wrapper.get_info(p2, p3.encode(), p4.value.encode())
        




    def get_project_name(self, p2):
        """
        Get the Wholeplot project name.
        """
        p2.value = self._wrapper.get_project_name(p2.value.encode())
        



    @classmethod
    def get_section_id(cls, p1, p2, p3, p4):
        """
        Create a section ID based on its location
        """
        p4.value = gxapi_cy.WrapDH.get_section_id(GXContext._get_tls_geo(), p1, p2, p3, p4.value.encode())
        



    @classmethod
    def get_template_blob(cls, p1, p2, p3):
        """
        Retrieve the import template from the database.

        **Note:**

        The template can be retrieved in order to refresh the
        database with a call to the DHIMPORT.GX.
        
        The import types correspond to the DHIMPORT.IMPTYPE variable:
        0: ASCII, 1: Database/XLS, 2: ODBC
        
        If no template blob exists, templ
        """
        ret_val, p3.value = gxapi_cy.WrapDH.get_template_blob(GXContext._get_tls_geo(), p1._wrapper, p2.encode(), p3.value)
        return ret_val



    @classmethod
    def get_template_info(cls, p1, p2, p3, p5):
        """
        Retrieve the file, `GXDH` Table name and type from an import template.

        **Note:**

        As of version 6.0, the import templates (``*.i3, *.i4``) produced
        by the Wholeplot import wizards contain the following lines:
        
         FILE assay.txt  (except for ODBC)
         DRILLTYPE 3
         DRILLTABLE Assay
        
        The FILE is normally the input file name, except for ODBC, where it
        is not defined.
        The DRILLTYPE is one of DH_DATA_XXX, and the DRILLTABLE
        is the name of the Wholeplot database table; e.g. Project_Assay.gdb
        in the above case. The DRILLTABLE is only included in the template
        for `DH_DATA_FROMTO` and `DH_DATA_POINT`, but this function will
        return the appropriate table names (e.g. Collar, Survey, ENSurvey)
        for the other types.
        If the DRILLTYPE is NOT found in the template, a value of
        `DH_DATA_UNKNOWN` is returned for the data type; likely an indication that this
        is not a new-style template produced by Wholeplot.
        """
        p2.value, p3.value, p5.value = gxapi_cy.WrapDH.get_template_info(GXContext._get_tls_geo(), p1.encode(), p2.value, p3.value.encode(), p5.value.encode())
        



    @classmethod
    def get_template_info_ex(cls, p1, p2, p3, p5, p7):
        """
        Retrieve the file, `GXDH` Table name, type and channel list from an import template.

        **Note:**

        As of version 6.0, the import templates (``*.i3, *.i4``) produced
        by the Wholeplot import wizards contain the following lines:
        
         FILE assay.txt  (except for ODBC)
         DRILLTYPE 3
         DRILLTABLE Assay
        
        The FILE is normally the input file name, except for ODBC, where it
        is not defined.
        The DRILLTYPE is one of DH_DATA_XXX, and the DRILLTABLE
        is the name of the Wholeplot database table; e.g. Project_Assay.gdb
        in the above case. The DRILLTABLE is only included in the template
        for `DH_DATA_FROMTO` and `DH_DATA_POINT`, but this function will
        return the appropriate table names (e.g. Collar, Survey, ENSurvey)
        for the other types.
        If the DRILLTYPE is NOT found in the template, a value of
        `DH_DATA_UNKNOWN` is returned for the data type; likely an indication that this
        is not a new-style template produced by Wholeplot.
        This version also returns a list of the channels in the template checks can be made to
        see if the import will exceed the database channel limit.
        """
        p2.value, p3.value, p5.value = gxapi_cy.WrapDH.get_template_info_ex(GXContext._get_tls_geo(), p1.encode(), p2.value, p3.value.encode(), p5.value.encode(), p7._wrapper)
        




    def get_units(self, p2, p4):
        """
        Get the positional units and conversion factor to m.
        """
        p2.value, p4.value = self._wrapper.get_units(p2.value.encode(), p4.value)
        



    @classmethod
    def have_current(cls):
        """
        Returns true if a drill project is loaded
        """
        ret_val = gxapi_cy.WrapDH.have_current(GXContext._get_tls_geo())
        return ret_val



    @classmethod
    def have_current2(cls, p1):
        """
        Returns true if a drill project is loaded, and the collar database if it is loaded.
        """
        ret_val, p1.value = gxapi_cy.WrapDH.have_current2(GXContext._get_tls_geo(), p1.value.encode())
        return ret_val




    def holes(self):
        """
        Return number of holes.
        """
        ret_val = self._wrapper.holes()
        return ret_val



    @classmethod
    def hole_select_from_list_gui(cls, p1, p2):
        """
        Select/Deselect holes using the two-panel selection tool.
        """
        ret_val = gxapi_cy.WrapDH.hole_select_from_list_gui(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper)
        return ret_val




    def hole_selection_tool_gui(self):
        """
        Select/Deselect holes using plan map tool.
        """
        ret_val = self._wrapper.hole_selection_tool_gui()
        return ret_val




    def modify3d_gui(self, p2, p3):
        """
        Modify parameters for a 3D plot.
        """
        ret_val, p3.value = self._wrapper.modify3d_gui(p2.encode(), p3.value)
        return ret_val




    def edit_classification_table_file_gui(self, p2, p3, p5, p6):
        """
        Edit a symbol color/pattern CSV file
        """
        ret_val, p3.value = self._wrapper.edit_classification_table_file_gui(p2.encode(), p3.value.encode(), p5, p6)
        return ret_val




    def modify_crooked_section_holes_gui(self, p2, p3):
        """
        Modify parameters to replot holes and hole data to an existing crooked section map.

        **Note:**

        Will plot to an empty crooked section.
        """
        ret_val, p3.value = self._wrapper.modify_crooked_section_holes_gui(p2.encode(), p3.value)
        return ret_val




    def modify_fence_gui(self, p2, p3):
        """
        Modify parameters for a section plot.

        **Note:**

        The fence section function.
        """
        ret_val, p3.value = self._wrapper.modify_fence_gui(p2.encode(), p3.value)
        return ret_val




    def modify_hole_traces_3dgui(self, p2, p3):
        """
        Modify parameters for a hole traces plot to an existing 3D view.
        """
        ret_val, p3.value = self._wrapper.modify_hole_traces_3dgui(p2.encode(), p3.value)
        return ret_val




    def modify_hole_traces_gui(self, p2, p3):
        """
        Modify parameters for a hole traces plot to a current map.
        """
        ret_val, p3.value = self._wrapper.modify_hole_traces_gui(p2.encode(), p3.value)
        return ret_val




    def modify_hole_traces_gui2(self, p2, p3, p4):
        """
        Modify parameters for a hole traces plot to a current plan or section view.

        **Note:**

        Currently supports `DH_PLOT_PLAN` and `DH_PLOT_SECTION`
        """
        ret_val, p4.value = self._wrapper.modify_hole_traces_gui2(p2.encode(), p3, p4.value)
        return ret_val




    def modify_plan_gui(self, p2, p3):
        """
        Modify parameters for a plan plot.
        """
        ret_val, p3.value = self._wrapper.modify_plan_gui(p2.encode(), p3.value)
        return ret_val




    def modify_plan_holes_gui(self, p2, p3):
        """
        Modify parameters to replot holes and hole data to an existing plan map.

        **Note:**

        Modifies only hole trace, hole data, topo, voxel slice data.
        """
        ret_val, p3.value = self._wrapper.modify_plan_holes_gui(p2.encode(), p3.value)
        return ret_val



    @classmethod
    def modify_rock_codes_gui(cls, p1):
        """
        Modify/create a rock codes file.
        """
        ret_val = gxapi_cy.WrapDH.modify_rock_codes_gui(GXContext._get_tls_geo(), p1.encode())
        return ret_val



    @classmethod
    def modify_rock_codes_gui2(cls, p1, p2):
        """
        Modify/create a rock codes file, channel population option.

        **Note:**

        Same as above, but passes the current database so that
        the "Populate from channel" button can be used to
        automatically populate the rock code list. The database
        should be a Wholeplot database.
        """
        ret_val = gxapi_cy.WrapDH.modify_rock_codes_gui2(GXContext._get_tls_geo(), p1._wrapper, p2.encode())
        return ret_val




    def modify_section_gui(self, p2, p3):
        """
        Modify parameters for a section plot.

        **Note:**

        The stacked section function uses the same control file
        format, but the plotting of profiles and plan views is
        disabled, and if multiple sections are requested, they
        are plotted in a stack on the left side of the same map,
        not to individual maps.
        """
        ret_val, p3.value = self._wrapper.modify_section_gui(p2.encode(), p3.value)
        return ret_val




    def modify_section_holes_gui(self, p2, p3):
        """
        Modify parameters to replot holes and hole data to an existing section map.

        **Note:**

        Works for both regular and stacked sections.
        Modifies only hole trace, hole data, topo, voxel slice data.
        """
        ret_val, p3.value = self._wrapper.modify_section_holes_gui(p2.encode(), p3.value)
        return ret_val




    def modify_stacked_section_gui(self, p2, p3):
        """
        Modify parameters for a section plot.

        **Note:**

        The stacked section function uses the same control file
        format, but the plotting of profiles and plan views is
        disabled, and if multiple sections are requested, they
        are plotted in a stack on the left side of the same map,
        not to individual maps.
        """
        ret_val, p3.value = self._wrapper.modify_stacked_section_gui(p2.encode(), p3.value)
        return ret_val




    def modify_strip_log_gui(self, p2, p3):
        """
        Modify parameters for a strip log plot.
        """
        ret_val, p3.value = self._wrapper.modify_strip_log_gui(p2.encode(), p3.value)
        return ret_val



    @classmethod
    def modify_structure_codes_gui(cls, p1):
        """
        Modify/create a structure codes file.
        """
        ret_val = gxapi_cy.WrapDH.modify_structure_codes_gui(GXContext._get_tls_geo(), p1.encode())
        return ret_val



    @classmethod
    def modify_structure_codes_gui2(cls, p1, p2):
        """
        Modify/create a structure codes file, channel population option.

        **Note:**

        Same as above, but passes the current database so that
        the "Populate from channel" button can be used to
        automatically populate the structure code list. The database
        should be a Wholeplot database.
        """
        ret_val = gxapi_cy.WrapDH.modify_structure_codes_gui2(GXContext._get_tls_geo(), p1._wrapper, p2.encode())
        return ret_val



    @classmethod
    def import2(cls, p1, p2, p3, p4, p5, p6, p7):
        """
        Imports data into a Drill Hole Database (obsolete).
        """
        gxapi_cy.WrapDH.import2(GXContext._get_tls_geo(), p1.encode(), p2._wrapper, p3, p4, p5.encode(), p6, p7.encode())
        




    def import_las(self, p2, p3, p4, p5, p6):
        """
        Imports LAS Data into a `GXDH` database

        **Note:**

        The argument for the assay database is the file name
        without the project name and underscore, e.g. for
        "Project_Assay.gdb" use "Assay"
        """
        self._wrapper.import_las(p2.encode(), p3.encode(), p4, p5, p6._wrapper)
        




    def num_assays(self):
        """
        Number of assay datasets.

        **Note:**

        Works for both single and multiple `GXDB` Wholeplots.
        """
        ret_val = self._wrapper.num_assays()
        return ret_val




    def num_selected_holes(self):
        """
        Returns number of selected holes.
        """
        ret_val = self._wrapper.num_selected_holes()
        return ret_val




    def qa_dip_az_curvature_lst(self, p2, p3, p4):
        """
        Do QA/QC Curvature checking on Dip Azimuth data for holes in a `GXLST`.

        **Note:**

        Checks all holes with Dip-Azimuth survey data
        """
        ret_val = self._wrapper.qa_dip_az_curvature_lst(p2._wrapper, p3, p4._wrapper)
        return ret_val




    def qa_dip_az_survey_lst(self, p2, p3):
        """
        Do QA/QC on Dip/Az Survey data for holes in a `GXLST`.

        **Note:**

        Error if no Dip-Azimuth survey database, or if
        a requested hole does not exist in the drill project.
        """
        ret_val = self._wrapper.qa_dip_az_survey_lst(p2._wrapper, p3._wrapper)
        return ret_val




    def qa_east_north_curvature_lst(self, p2, p3, p4):
        """
        Do QA/QC Curvature checking on Dip Azimuth data for holes in a `GXLST`.

        **Note:**

        Checks all holes with East-North survey data
        """
        ret_val = self._wrapper.qa_east_north_curvature_lst(p2._wrapper, p3, p4._wrapper)
        return ret_val




    def qa_east_north_survey_lst(self, p2, p3):
        """
        Do QA/QC on East/North Survey data for holes in a `GXLST`.

        **Note:**

        Error if no East-North survey database, or if
        a requested hole does not exist in the drill project.
        """
        ret_val = self._wrapper.qa_east_north_survey_lst(p2._wrapper, p3._wrapper)
        return ret_val




    def slice_selection_tool_gui(self, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13):
        """
        Select a slice with the holes in context. An optional 4 point area of interest (AOI) can be added to be represented in the UI too.
        """
        ret_val, p10.value, p11.value, p12.value, p13.value = self._wrapper.slice_selection_tool_gui(p2, p3, p4, p5, p6, p7, p8, p9, p10.value, p11.value, p12.value, p13.value)
        return ret_val




    def update_survey_from_collar(self, p2):
        """
        Update the Survey table from the collar info.

        **Note:**

        Call when the collar values are edited to update the survey table
        values. If the survey contains more than one row, then no changes
        are applied, and no warning or error is registered.
        """
        ret_val = self._wrapper.update_survey_from_collar(p2)
        return ret_val




    def load_data_parameters_ini(self, p2, p3):
        """
        Load data parameters from INI files..

        **Note:**

        Wholeplot data graphing parameters for each channel are stored
        in the channel `GXREG`. This function lets a user transfer pre-defined
        settings to individual INI files (eg. cu.ini).
        """
        self._wrapper.load_data_parameters_ini(p2._wrapper, p3.encode())
        




    def load_plot_parameters(self, p2, p3):
        """
        Load parameters from a Job into the Drill object.
        """
        self._wrapper.load_plot_parameters(p2.encode(), p3)
        




    def load_select(self, p2):
        """
        Load selections to from a file.
        """
        self._wrapper.load_select(p2.encode())
        




    def mask_ply(self, p2, p3, p4, p5, p6, p7):
        """
        Set mask channel based on view selection polygon.

        **Note:**

        Data values inside the polygon area, and within the slice thickness
        have their mask channel values set to 1.
        If the specified mask channel does not exist, it is created.
        `DH_MASK_NEW` --- Mask is created new for each selected hole
        `DH_MASK_APPEND` --- Current selection is added to previous.
        """
        self._wrapper.mask_ply(p2._wrapper, p3._wrapper, p4, p5.encode(), p6, p7)
        



    @classmethod
    def open(cls, p1):
        """
        Open `GXDH` from collar database and load all associated databases.
        """
        ret_val = gxapi_cy.WrapDH.open(GXContext._get_tls_geo(), p1.encode())
        return GXDH(ret_val)




    def open_job(self, p2, p3):
        """
        Open a `GXDH` plotting job
        """
        self._wrapper.open_job(p2.encode(), p3)
        




    def plot_hole_traces(self, p2, p3):
        """
        Plot hole traces to a regular (plan) map.

        **Note:**

        Both the hole traces and data can be plotted.
        The DHPLANHOLES GX uses the default plan map parameter file
        "_plan.inp".
        """
        self._wrapper.plot_hole_traces(p2._wrapper, p3.encode())
        




    def plot_hole_traces_3d(self, p2, p3):
        """
        Plot hole traces to an existing 3D map view.

        **Note:**

        Both the hole traces and data can be plotted.
        The DH3DHOLES GX uses the default 3D map parameter file
        "_3D.in3".
        """
        self._wrapper.plot_hole_traces_3d(p2._wrapper, p3.encode())
        




    def plot_symbols_3d(self, p2, p3):
        """
        Plot 3D symbols to an existing 3D map view.
        """
        self._wrapper.plot_symbols_3d(p2._wrapper, p3.encode())
        




    def qa_collar(self, p2):
        """
        Do QA/QC on Hole Collar data.
        """
        self._wrapper.qa_collar(p2._wrapper)
        




    def qa_collar_lst(self, p2, p3):
        """
        Do QA/QC on Hole Collar data - `GXLST` of holes.
        """
        self._wrapper.qa_collar_lst(p2._wrapper, p3._wrapper)
        




    def qa_dip_az_curvature(self, p2, p3):
        """
        Do QA/QC Curvature checking on Dip Azimuth data.

        **Note:**

        Checks all holes with Dip-Azimuth survey data
        """
        self._wrapper.qa_dip_az_curvature(p2._wrapper, p3)
        




    def qa_dip_az_curvature2(self, p2, p3, p4):
        """
        Do QA/QC Curvature checking on Dip Azimuth data for a single hole.

        **Note:**

        Checks single hole with Dip-Azimuth survey data
        """
        self._wrapper.qa_dip_az_curvature2(p2._wrapper, p3, p4.encode())
        




    def qa_dip_az_survey(self, p2, p3, p4, p5):
        """
        Do QA/QC on Dip/Az Survey data.

        **Note:**

        Error if no Dip-Azimuth survey database, or if
        the requested line does not exist in the database.
        """
        self._wrapper.qa_dip_az_survey(p2._wrapper, p3._wrapper, p4, p5.encode())
        




    def qa_east_north_curvature(self, p2, p3):
        """
        Do QA/QC Curvature checking on Dip Azimuth data.

        **Note:**

        Checks all holes with East-North survey data
        """
        self._wrapper.qa_east_north_curvature(p2._wrapper, p3)
        




    def qa_east_north_curvature2(self, p2, p3, p4):
        """
        Do QA/QC Curvature checking on Dip Azimuth data for a single hole.

        **Note:**

        Checks single holes with East-North survey data
        """
        self._wrapper.qa_east_north_curvature2(p2._wrapper, p3, p4.encode())
        




    def qa_east_north_survey(self, p2, p3, p4, p5):
        """
        Do QA/QC on East/North Survey data.

        **Note:**

        Error if no East-North survey database, or if
        the requested line does not exist in the database.
        """
        self._wrapper.qa_east_north_survey(p2._wrapper, p3._wrapper, p4, p5.encode())
        




    def qa_from_to_data(self, p2, p3, p4, p5):
        """
        Do QA/QC on From/To data.
        """
        self._wrapper.qa_from_to_data(p2._wrapper, p3._wrapper, p4, p5.encode())
        




    def qa_point_data(self, p2, p3, p4, p5):
        """
        Do QA/QC on Point data.
        """
        self._wrapper.qa_point_data(p2._wrapper, p3._wrapper, p4, p5.encode())
        




    def qa_write_unregistered_holes(self, p2, p3):
        """
        Write out unregistered holes in a database.

        **Note:**

        Looks at each line in a database and sees if it is listed in
        the collar tables' hole list.
        """
        self._wrapper.qa_write_unregistered_holes(p2._wrapper, p3._wrapper)
        




    def replot_holes(self, p2, p3):
        """
        Replot holes on an existing drill map.

        **Note:**

        The parameter file must correspond to the plot Type.
        The hDH->hMAP value must be set first, using `set_map`().
        Overwrites existing hole and hole data groups.
        Replots the legend if the legend is enabled.
        This should only be used on a slightly modified version of the
        INI file used to create the existing map, or things may not
        work out (e.g. bad locations etc).
        """
        self._wrapper.replot_holes(p2.encode(), p3)
        




    def plot_holes_on_section(self, p2, p3, p4):
        """
        Plot the currently selected holes on an existing section view.

        **Note:**

        Plot the currently selected holes to a section view.
        """
        self._wrapper.plot_holes_on_section(p2.encode(), p3, p4.encode())
        




    def re_survey_east_north(self, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11):
        """
        Resurvey an East-North-RL survey.

        **Note:**

        Re-interpolates in X, Y and Z to proper depth interval
        and returns depths for each point
        """
        p11.value = self._wrapper.re_survey_east_north(p2.encode(), p3._wrapper, p4._wrapper, p5._wrapper, p6._wrapper, p7, p8, p9, p10, p11.value)
        




    def re_survey_pol_fit(self, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16, p17):
        """
        Use the polynomial fit resurveying method.

        **Note:**

        Uses the polynomial fit method to calculate (X, Y, Z)
        locations down the hole from azimuth, dip, depth values.
        The collar is assumed to be at zero depth, and depth is the
        measure distance down the hole (even if it's horizontal).
        A negative dip convention means vertical down is -90 degrees.
        The polynomial order must be in the range 1-20, with 5 being adequate
        for most smoothly curving holes. The order is reduced to no more than
        the number of input points.
        """
        self._wrapper.re_survey_pol_fit(p2.encode(), p3._wrapper, p4._wrapper, p5._wrapper, p6, p7, p8, p9, p10, p11, p12, p13, p14._wrapper, p15._wrapper, p16._wrapper, p17._wrapper)
        




    def re_survey_rad_curve(self, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16):
        """
        Use radius of curvature resurveying method.

        **Note:**

        Uses the Radius of curvature method to calculate (X, Y, Z)
        locations down the hole from azimuth, dip, depth values.
        The collar is assumed to be at zero depth, and depth is the
        measure distance down the hole (even if it's horizontal).
        A negative dip convention means vertical down is -90 degrees.
        """
        self._wrapper.re_survey_rad_curve(p2.encode(), p3._wrapper, p4._wrapper, p5._wrapper, p6, p7, p8, p9, p10, p11, p12, p13._wrapper, p14._wrapper, p15._wrapper, p16._wrapper)
        




    def re_survey_straight(self, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15):
        """
        Resurvey a straight hole.

        **Note:**

        Assumes a straight hole to calculate (X, Y, Z)
        locations down the hole from azimuth, dip, depth values.
        The collar is assumed to be at zero depth, and depth is the
        measure distance down the hole (even if it's horizontal).
        A negative dip convention means vertical down is -90 degrees.
        """
        self._wrapper.re_survey_straight(p2.encode(), p3, p4, p5, p6, p7, p8, p9, p10, p11, p12._wrapper, p13._wrapper, p14._wrapper, p15._wrapper)
        




    def re_survey_straight_seg(self, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16):
        """
        Resurvey a hole with straight segments between locations.

        **Note:**

        Calculate (X, Y, Z) locations down the hole from azimuth, dip,
        depth values, assuming each segment is straight, and the hole
        bends at each successive azimuth, dip, depth value.
        The collar is assumed to be at zero depth, and depth is the
        measure distance down the hole (even if it's horizontal).
        A negative dip convention means vertical down is -90 degrees.
        """
        self._wrapper.re_survey_straight_seg(p2.encode(), p3._wrapper, p4._wrapper, p5._wrapper, p6, p7, p8, p9, p10, p11, p12, p13._wrapper, p14._wrapper, p15._wrapper, p16._wrapper)
        




    def save_data_parameters_ini(self, p2, p3):
        """
        Save data parameters to INI files..

        **Note:**

        Wholeplot data graphing parameters for each channel are stored
        in the channel `GXREG`. This function lets a user transfer pre-defined
        settings to individual INI files (eg. cu.ini).
        As of v6.3, the `GXDH` object is NOT required for this function, and
        is, in fact, ignored.
        """
        self._wrapper.save_data_parameters_ini(p2._wrapper, p3.encode())
        




    def save_job(self, p2, p3):
        """
        Save a `GXDH` plotting job
        """
        self._wrapper.save_job(p2.encode(), p3)
        




    def save_select(self, p2):
        """
        Saves current selections to a file.
        """
        self._wrapper.save_select(p2.encode())
        




    def section_window_size_mm(self, p2, p3):
        """
        Deterine the size, in mm, of the section window

        **Note:**

        Given the current selection of windows (e.g. legend, plan),
        paper size and orientation, return the size in mm of the
        window used for plotting the section.
        """
        p2.value, p3.value = self._wrapper.section_window_size_mm(p2.value, p3.value)
        




    def select_all_holes(self):
        """
        Select all the holes in a Drill hole project.
        """
        self._wrapper.select_all_holes()
        




    def select_holes(self, p2, p3):
        """
        Select holes by hole indices.

        **Note:**

        Indices less than 0 are skipped. This lets you use this function
        after a call to `GXLST.find_items`, which returns -1 for indices not located.
        """
        self._wrapper.select_holes(p2._wrapper, p3)
        




    def select_name(self, p2, p3, p4):
        """
        Select holes using a name mask.

        **Note:**

        Overwrite mode - all selections tested and selected or not selected
        Append mode    - only holes matching the mask are selected or not selected.
        """
        self._wrapper.select_name(p2.encode(), p3, p4)
        




    def select_ply(self, p2):
        """
        Select all holes in `GXPLY` (Polygon) object.

        **Note:**

        This function operates the same as the call:
        
        `select_ply2`(Drill, 1, 0, 0);
        """
        self._wrapper.select_ply(p2._wrapper)
        




    def select_ply2(self, p2, p3, p4, p5):
        """
        Select holes in `GXPLY` (Polygon) object with options.

        **Note:**

        The various selection options give the following results:
        
        New/Select/inside: Unselect all holes, then
                           select all holes inside the polygon.
        New/Select/outside: Unselect all holes, then
                           select all holes outside the polygon.
        New/Deselect/inside: Select all holes, then
                           deselect all holes inside the polygon.
        New/Deselect/outside: Select all holes, then
                           deselect all holes outside the polygon.
        
        Append/Select/inside: Select all holes inside the polygon.
                              Leave selections outside as is.
        Append/Select/outside: Select all holes outside the polygon.
                              Leave selections inside as is.
        Append/Deselect/inside: Deselect all holes inside the polygon
                              Leave selections outside as is.
        Append/Deselect/outside: Deselect all holes outside the polygon.
                              Leave selections inside as is.
        """
        self._wrapper.select_ply2(p2._wrapper, p3, p4, p5)
        




    def set_crooked_section_ipj(self, p2):
        """
        Pass the Crooked projection required for plotting to a crooked section.

        **Note:**

        This might be extracted from an existing crooked section view, or created from a database line.
        """
        self._wrapper.set_crooked_section_ipj(p2._wrapper)
        




    def set_current_view_name(self, p2):
        """
        Set the current map view name.

        **Note:**

        Can be used to specify the name of the view to plot into.
        """
        self._wrapper.set_current_view_name(p2.encode())
        




    def set_info(self, p2, p3, p4):
        """
        Set Collar Information.

        **Note:**

        If the DH_ELEV channel is requested it will also
        search for the DH_RL channel, which is the new
        name for the collar elevation.
        """
        self._wrapper.set_info(p2, p3.encode(), p4.encode())
        




    def set_ipj(self, p2):
        """
        Set the project `GXIPJ`.

        **Note:**

        The projection for the project is the projection stored
        in the DH_EAST channel in the collar table. This
        function sets the projection of the (DH_EAST, DH_NORTH)
        channel pairs in each of the project databases to the
        input `GXIPJ`.
        The input `GXIPJ` cannot be a geographic coordinate system
        or this call will fail with an error message.
        """
        self._wrapper.set_ipj(p2._wrapper)
        




    def set_map(self, p2):
        """
        Store the current `GXMAP` to the `GXDH` object.

        **Note:**

        Use this before calling the ReplotHoles functions,
        so that, instead of creating a new map, the plotting
        functions use the existing one.
        """
        self._wrapper.set_map(p2._wrapper)
        




    def set_new_ipj(self, p2):
        """
        Set a new project database projection to collar table projection.

        **Note:**

        Gets the `GXIPJ` of the collar table current x channel and copies it
        into the named database (as long as it is in the project!)
        """
        self._wrapper.set_new_ipj(p2.encode())
        




    def set_selected_holes_vv(self, p2, p3):
        """
        Set hole selection using hole indices.
        """
        self._wrapper.set_selected_holes_vv(p2._wrapper, p3)
        



    @classmethod
    def set_template_blob(cls, p1, p2, p3):
        """
        Store the import template to the database.

        **Note:**

        The template can later be retrieved in order to refresh the
        database with a call to the DHIMPORT.GX.
        
        The import types correspond to the DHIMPORT.IMPTYPE variable:
        0: ASCII, 1: Database/XLS, 2: ODBC
        """
        gxapi_cy.WrapDH.set_template_blob(GXContext._get_tls_geo(), p1._wrapper, p2.encode(), p3)
        




    def significant_intersections_db(self, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12):
        """
        Make a report of Significant Intersections
        """
        self._wrapper.significant_intersections_db(p2._wrapper, p3._wrapper, p4, p5.encode(), p6, p7, p8, p9, p10, p11, p12)
        




    def test_import_las(self, p2, p3, p4, p5, p6):
        """
        Tests import of LAS Data for problems.

        **Note:**

        See `import_las`.
        Determines if the import of the LAS data will result in data
        being overwritten, interpolated or resampled. Warnings are written to a log
        file, as in sImportLAS_DH. Warnings are not registered in cases
        where data is merely extended at the start or the end with dummies
        to match a different interval down the hole.
        """
        p6.value = self._wrapper.test_import_las(p2.encode(), p3.encode(), p4, p5._wrapper, p6.value)
        




    def un_select_all_holes(self):
        """
        Unselect all the holes in a Drill hole project.
        """
        self._wrapper.un_select_all_holes()
        




    def un_selected_hole_lst(self, p2):
        """
        Populate an `GXLST` with the list of the unselected holes
        """
        self._wrapper.un_selected_hole_lst(p2._wrapper)
        




    def update_collar_table(self):
        """
        Update all collar table information.
        """
        self._wrapper.update_collar_table()
        




    def update_hole_extent(self, p2):
        """
        Update extents for one hole.
        """
        self._wrapper.update_hole_extent(p2)
        




    def wholeplot(self, p2, p3):
        """
        Run a Wholeplot plot job.

        **Note:**

        The parameter file must correspond to the plot Type. The INI file
        contains settings for all of the non-database data related
        parameters (e.g. Map template, scale, boundaries,
        section definitions, hole trace parameters etc...)
        """
        self._wrapper.wholeplot(p2.encode(), p3)
        




    def surface_intersections(self, p2, p3, p4):
        """
        Determine intersections of drillholes with a surface.
        """
        self._wrapper.surface_intersections(p2._wrapper, p3.encode(), p4)
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer