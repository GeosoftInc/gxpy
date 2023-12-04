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
class GXPROJ(gxapi_cy.WrapPROJ):
    """
    GXPROJ class.

    Project functions
    """

    def __init__(self, handle=0):
        super(GXPROJ, self).__init__(GXContext._get_tls_geo(), handle)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of `GXPROJ <geosoft.gxapi.GXPROJ>`
        
        :returns: A null `GXPROJ <geosoft.gxapi.GXPROJ>`
        :rtype:   GXPROJ
        """
        return GXPROJ()

    def is_null(self):
        """
        Check if this is a null (undefined) instance
        
        :returns: True if this is a null (undefined) instance, False otherwise.
        :rtype:   bool
        """
        return self._internal_handle() == 0



# Drag-and-drop methods


    @classmethod
    def drop_map_clip_data(cls, hglobal):
        """
        Drop Map clipboard data in the current project (workspace background)
        
        :param hglobal:  Handle to Global Clipboard data
        :type  hglobal:  int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.
        """
        gxapi_cy.WrapPROJ._drop_map_clip_data(GXContext._get_tls_geo(), hglobal)
        




# Miscellaneous


    @classmethod
    def add_document(cls, name, type, display):
        """
        Adds (and opens) a document file in the current project.
        
        :param name:     Document name
        :param type:     Type of document to add
        :param display:  :ref:`PROJ_DISPLAY`
        :type  name:     str
        :type  type:     str
        :type  display:  int

        :returns:        0 - Ok
                         1 - Error
        :rtype:          int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.

        **Note:** The passed file name must be a valid
        file name complete with an extension and
        qualifiers (if applicable).

        The type string can be one of the following:

            Database      
            Grid          
            Map           
            3DView        
            Geosurface
            Voxel         
            VoxelInversion
            GMS3D         
            GMS2D
        """
        ret_val = gxapi_cy.WrapPROJ._add_document(GXContext._get_tls_geo(), name.encode(), type.encode(), display)
        return ret_val



    @classmethod
    def add_document_without_opening(cls, name, type):
        """
        Adds (and opens) a document file in the current project.
        
        :param name:  Document name
        :param type:  Type of document to add
        :type  name:  str
        :type  type:  str

        :returns:     0 - Ok
                      1 - Error
        :rtype:       int

        .. versionadded:: 8.5

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.

        **Note:** The passed file name must be a valid
        file name complete with an extension and
        qualifiers (if applicable).

        The type string can be one of the following:

            Database      
            Grid          
            Map           
            3DView        
            Geosurface
            Voxel         
            VoxelInversion
            GMS3D         
            GMS2D
        """
        ret_val = gxapi_cy.WrapPROJ._add_document_without_opening(GXContext._get_tls_geo(), name.encode(), type.encode())
        return ret_val



    @classmethod
    def add_document_include_meta(cls, name, type, meta, display):
        """
        Adds (and opens) a document file in the current project.
        
        :param name:     Document name
        :param type:     Type of document to add
        :param meta:     Meta file to load
        :param display:  :ref:`PROJ_DISPLAY`
        :type  name:     str
        :type  type:     str
        :type  meta:     str
        :type  display:  int

        :returns:        0 - Ok
                         1 - Error
        :rtype:          int

        .. versionadded:: 2022.1

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.

        **Note:** The passed file name must be a valid
        file name complete with an extension and
        qualifiers (if applicable).

        The type string can be one of the following:

            Database      
            Grid          
            Map           
            3DView        
            Geosurface
            Voxel         
            VoxelInversion
            GMS3D         
            GMS2D
        """
        ret_val = gxapi_cy.WrapPROJ._add_document_include_meta(GXContext._get_tls_geo(), name.encode(), type.encode(), meta.encode(), display)
        return ret_val



    @classmethod
    def add_grid_document(cls, name, colors, method, display):
        """
        Adds (and opens) a grid document file in the current project with a particular colour distribution and colour file.
        
        :param name:     Document name
        :param colors:   Colour zone file to use
        :param method:   Colour method to use - one of the ITR_ZONE_XXXX values
        :param display:  :ref:`PROJ_DISPLAY`
        :type  name:     str
        :type  colors:   str
        :type  method:   int
        :type  display:  int

        :returns:        0 - Ok
                         1 - Error
        :rtype:          int

        .. versionadded:: 9.7

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.

        **Note:** The passed file name must be a valid Grid document
        with an extension and qualifiers (if applicable).
        """
        ret_val = gxapi_cy.WrapPROJ._add_grid_document(GXContext._get_tls_geo(), name.encode(), colors.encode(), method, display)
        return ret_val



    @classmethod
    def get_command_environment(cls):
        """
        The current command environment
        

        :returns:    :ref:`COMMAND_ENV`

                  Notes									

                  We are moving towards embedded tools and menus and this setting can be
                  queried from the project to determine how specific commands should react.
                  Only 3D viewer is currently making use of this.

                  If new Command environment enum values are added, then update the iGetCommandEnvironment_PROJ() function
                  in geogxgui\\gxx_app.cpp and in the COMMAND_ENVIRONMENT enums in geoengine.core\\include\\obj\\objgp.h.
        :rtype:      int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.
        """
        ret_val = gxapi_cy.WrapPROJ._get_command_environment(GXContext._get_tls_geo())
        return ret_val



    @classmethod
    def list_documents(cls, gvv, type):
        """
        Fills a `GXVV <geosoft.gxapi.GXVV>` with documents of a certain type.
        
        :param gvv:   `GXVV <geosoft.gxapi.GXVV>` of type -`STR_FILE <geosoft.gxapi.STR_FILE>`
        :param type:  Type of document to obtain
        :type  gvv:   GXVV
        :type  type:  str

        :returns:     The number of documents listed in the `GXVV <geosoft.gxapi.GXVV>`.
        :rtype:       int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.

        **Note:** The type string can be one of the following:
        Database         List Databases.
        Grid             List Grids.
        Map              List Maps.
        3DView           List 3D Views.
        Geosurface       List Geosurfaces.
        Voxel            List Voxels.
        VoxelInversion   List VOXI Documents.
        `GXMXD <geosoft.gxapi.GXMXD>`              List ArcGIS MXDs.
        GMS3D            List GM-SYS 3D Models.
        GMS2D            List GM-SYS 2D Models.
        All              Lists all files.
        """
        ret_val = gxapi_cy.WrapPROJ._list_documents(GXContext._get_tls_geo(), gvv, type.encode())
        return ret_val



    @classmethod
    def list_loaded_documents(cls, gvv, type):
        """
        Fills a `GXVV <geosoft.gxapi.GXVV>` with loaded documents of a certain type.
        
        :param gvv:   `GXVV <geosoft.gxapi.GXVV>` of type -`STR_FILE <geosoft.gxapi.STR_FILE>`>
        :param type:  Type of document to obtain
        :type  gvv:   GXVV
        :type  type:  str

        :returns:     The number of loaded documents listed in the `GXVV <geosoft.gxapi.GXVV>`.
        :rtype:       int

        .. versionadded:: 9.2

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.

        **Note:** The type string can be one of the following:
        Database         List Databases.
        Grid             List Grids.
        Map              List Maps.
        3DView           List 3D Views.
        Geosurface       List Geosurfaces.
        Voxel            List Voxels.
        VoxelInversion   List VOXI Documents.
        `GXMXD <geosoft.gxapi.GXMXD>`              List ArcGIS MXDs.
        GMS3D            List GM-SYS 3D Models.
        GMS2D            List GM-SYS 2D Models.
        All              Lists all files.
        """
        ret_val = gxapi_cy.WrapPROJ._list_loaded_documents(GXContext._get_tls_geo(), gvv, type.encode())
        return ret_val



    @classmethod
    def current_document(cls, name, type):
        """
        Get the name and type of the loaded document with focus.
        
        :param name:  Name (empty if none currently loaded)
        :param type:  Type
        :type  name:  str_ref
        :type  type:  str_ref

        .. versionadded:: 9.2

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.
        """
        name.value, type.value = gxapi_cy.WrapPROJ._current_document(GXContext._get_tls_geo(), name.value.encode(), type.value.encode())
        



    @classmethod
    def current_document_of_type(cls, name, type):
        """
        Get the name of a loaded document of a specific type.
        
        :param name:  Name (empty if none currently loaded)
        :param type:  Type
        :type  name:  str_ref
        :type  type:  str

        .. versionadded:: 9.2

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.
        """
        name.value = gxapi_cy.WrapPROJ._current_document_of_type(GXContext._get_tls_geo(), name.value.encode(), type.encode())
        



    @classmethod
    def list_tools(cls, lst, type):
        """
        Fills an `GXLST <geosoft.gxapi.GXLST>` object with tools of a certain type and
        notes the current visibility setting.
        
        :param lst:   `GXLST <geosoft.gxapi.GXLST>` object to hold list
        :param type:  :ref:`TOOL_TYPE`
        :type  lst:   GXLST
        :type  type:  int

        :returns:     The number of tools found.
        :rtype:       int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.

        **Note:** GX will terminate if there is an error.

        `GXLST <geosoft.gxapi.GXLST>` object will hold the tool name in the name column and
        include whether the tool is currently visible in the value
        column (1=visible, 0-hidden).
        """
        ret_val = gxapi_cy.WrapPROJ._list_tools(GXContext._get_tls_geo(), lst, type)
        return ret_val



    @classmethod
    def remove_document(cls, name):
        """
        Removes (and closes if visible) a document from the current project.
        
        :param name:  Document name
        :type  name:  str

        :returns:     0 - Ok
                      1 - Document not found in project
        :rtype:       int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.

        **Note:** The passed file name must be a valid
        file name complete with an extension and
        qualifiers (if applicable).
        """
        ret_val = gxapi_cy.WrapPROJ._remove_document(GXContext._get_tls_geo(), name.encode())
        return ret_val



    @classmethod
    def remove_tool(cls, name):
        """
        Removes (and closes if visible) a auxiliary tool from the current project.
        
        :param name:  Tool name
        :type  name:  str

        :returns:     0 - Ok
                      1 - Tool not found in project
        :rtype:       int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.

        **Note:** Nothing
        """
        ret_val = gxapi_cy.WrapPROJ._remove_tool(GXContext._get_tls_geo(), name.encode())
        return ret_val



    @classmethod
    def save_close_documents(cls, type):
        """
        Saves and closes (if visible) documents contained in the current project.
        
        :param type:  Type of document to save / close
        :type  type:  str

        :returns:     0  - Ok
                      -1 - User hit cancel in save dialog
                      1  - Error
        :rtype:       int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.

        **Note:** This wrapper brings up the save dialog tool to allow
        the user to save the modified documents for this project.
        Only documents that have actually changed will be listed.

        The type string can be one of the following:

            Database      
            Grid          
            Map           
            3DView        
            Geosurface
            Voxel         
            VoxelInversion
            GMS3D         
            GMS2D
            All
        """
        ret_val = gxapi_cy.WrapPROJ._save_close_documents(GXContext._get_tls_geo(), type.encode())
        return ret_val



    @classmethod
    def get_name(cls, name):
        """
        Return the name of the project file.
        
        :param name:  name
        :type  name:  str_ref

        .. versionadded:: 8.4

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.

        **Note:** Return the name of the project file.
        """
        name.value = gxapi_cy.WrapPROJ._get_name(GXContext._get_tls_geo(), name.value.encode())
        



    @classmethod
    def get_server_and_project_guid(cls, server_id, project_id):
        """
        Return the unique identifier of the project and server.
        
        :param server_id:   Server ID
        :param project_id:  Project ID
        :type  server_id:   str_ref
        :type  project_id:  str_ref

        .. versionadded:: 2021.2

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.

        **Note:** Return the unique identifier of the project and server.
        """
        server_id.value, project_id.value = gxapi_cy.WrapPROJ._get_server_and_project_guid(GXContext._get_tls_geo(), server_id.value.encode(), project_id.value.encode())
        



    @classmethod
    def set_central_project_information(cls, server_guid, project_guid, branch_id, revision_id, cs_info):
        """
        Set Central project information.
        
        :param server_guid:   server guid
        :param project_guid:  project guid
        :param branch_id:     branch ID
        :param revision_id:   revision ID
        :param cs_info:       Coordinate system information, either EPSG or WKT
        :type  server_guid:   str
        :type  project_guid:  str
        :type  branch_id:     int
        :type  revision_id:   int
        :type  cs_info:       str

        .. versionadded:: 2021.2

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.

        **Note:** Set Central project information.
        """
        gxapi_cy.WrapPROJ._set_central_project_information(GXContext._get_tls_geo(), server_guid.encode(), project_guid.encode(), branch_id, revision_id, cs_info.encode())
        



    @classmethod
    def get_central_project_information(cls, instance, project, crs, branch, rev_id, rev_date, rev_note, rev_stage, rev_author, rev_server_url, rev_proj_url):
        """
        Get Central project information.
        
        :param instance:        Instance name
        :param project:         Project name
        :param crs:             Coordinate Reference System
        :param branch:          Branch name
        :param rev_id:          Revision Id
        :param rev_date:        Revision date
        :param rev_note:        Revision note
        :param rev_stage:       Revision stage
        :param rev_author:      Revision author
        :param rev_server_url:  Revision server url
        :param rev_proj_url:    Revision project url
        :type  instance:        str_ref
        :type  project:         str_ref
        :type  crs:             str_ref
        :type  branch:          str_ref
        :type  rev_id:          str_ref
        :type  rev_date:        str_ref
        :type  rev_note:        str_ref
        :type  rev_stage:       str_ref
        :type  rev_author:      str_ref
        :type  rev_server_url:  str_ref
        :type  rev_proj_url:    str_ref

        .. versionadded:: 2021.2

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.

        **Note:** Get Central project information.
        """
        instance.value, project.value, crs.value, branch.value, rev_id.value, rev_date.value, rev_note.value, rev_stage.value, rev_author.value, rev_server_url.value, rev_proj_url.value = gxapi_cy.WrapPROJ._get_central_project_information(GXContext._get_tls_geo(), instance.value.encode(), project.value.encode(), crs.value.encode(), branch.value.encode(), rev_id.value.encode(), rev_date.value.encode(), rev_note.value.encode(), rev_stage.value.encode(), rev_author.value.encode(), rev_server_url.value.encode(), rev_proj_url.value.encode())
        



    @classmethod
    def save_document_view(cls, name, meta_file):
        """
        Save document view to a file.
        
        :param name:       Document name
        :param meta_file:  save meta to file
        :type  name:       str
        :type  meta_file:  str

        .. versionadded:: 2022.1

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.

        **Note:** Save document view to a file.
        """
        gxapi_cy.WrapPROJ._save_document_view(GXContext._get_tls_geo(), name.encode(), meta_file.encode())
        



    @classmethod
    def get_default_project_path(cls, folder):
        """
        Get default project folder.
        
        :param folder:  Returned default path
        :type  folder:  str_ref

        .. versionadded:: 2022.1

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.

        **Note:** Get default project folder.
        """
        folder.value = gxapi_cy.WrapPROJ._get_default_project_path(GXContext._get_tls_geo(), folder.value.encode())
        



    @classmethod
    def set_default_project_path(cls, folder):
        """
        Set default project folder.
        
        :param folder:  Default path
        :type  folder:  str

        .. versionadded:: 2022.1

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.

        **Note:** Set default project folder.
        """
        gxapi_cy.WrapPROJ._set_default_project_path(GXContext._get_tls_geo(), folder.encode())
        



    @classmethod
    def has_pending_central_publish_event(cls):
        """
        Checks if there is a pending publish event.
        
        :rtype:      bool

        .. versionadded:: 2022.1

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.

        **Note:** Checks if there is a pending publish event.
        """
        ret_val = gxapi_cy.WrapPROJ._has_pending_central_publish_event(GXContext._get_tls_geo())
        return ret_val




# OMS_Scripting


    @classmethod
    def register_background_script(cls, name, name2, script, log, save_log, output_files, file_to_delete, process_id):
        """
        Register an OMS script launched from the project
        
        :param name:            Name for the process
        :param name2:           Secondary name for the process
        :param script:          file name of the script. Script should self-delete to indicate process has completed
        :param log:             file name of the output log (optional). Will contain info about this script run
        :param save_log:        1 - log file is temporary and deleted on OM close. 0 - do not delete on OM close
        :param output_files:    List of output documents created by the script.
        :param file_to_delete:  File to delete (optional). Will also delete files with same name and .tmp and .xml extensions
        :param process_id:      Process ID - used to check status or kill the process
        :type  name:            str
        :type  name2:           str
        :type  script:          str
        :type  log:             str
        :type  save_log:        int
        :type  output_files:    GXVV
        :type  file_to_delete:  str
        :type  process_id:      str

        .. versionadded:: 2022.2

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.

        **Note:** Allows the project to track the progress/failure/success of scripts launched in the background
        """
        gxapi_cy.WrapPROJ._register_background_script(GXContext._get_tls_geo(), name.encode(), name2.encode(), script.encode(), log.encode(), save_log, output_files, file_to_delete.encode(), process_id.encode())
        



    @classmethod
    def get_registered_background_script(cls, index, date_time, name, name2, script, log, output_files, process_id):
        """
        Retrieve info on a registered OMS script launched from the project
        
        :param index:         Index for the process (input) 0 to N-1
        :param date_time:     Date/Time string in format DD/MM/YYYY hh:mm:ss
        :param name:          Name for the process (output)
        :param name2:         Secondary name for the process (output)
        :param script:        file name of the script (output)
        :param log:           file name of the output log (returned, can be empty).
        :param output_files:  List of output documents created by the script. of size -`STR_FILE <geosoft.gxapi.STR_FILE>`
        :param process_id:    Process ID (returned)
        :type  index:         int
        :type  date_time:     str_ref
        :type  name:          str_ref
        :type  name2:         str_ref
        :type  script:        str_ref
        :type  log:           str_ref
        :type  output_files:  GXVV
        :type  process_id:    str_ref

        .. versionadded:: 2022.2

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.

        **Note:** reference by index
        """
        date_time.value, name.value, name2.value, script.value, log.value, process_id.value = gxapi_cy.WrapPROJ._get_registered_background_script(GXContext._get_tls_geo(), index, date_time.value.encode(), name.value.encode(), name2.value.encode(), script.value.encode(), log.value.encode(), output_files, process_id.value.encode())
        



    @classmethod
    def get_num_registered_background_scripts(cls):
        """
        Register a OMS script launched from the project
        

        :returns:    The number of registered background scripts: in progress, finished, failed, deleted etc.
        :rtype:      int

        .. versionadded:: 2022.2

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.

        **Note:** Allows the project to track the progress/failure/success of scripts launched in the background
        """
        ret_val = gxapi_cy.WrapPROJ._get_num_registered_background_scripts(GXContext._get_tls_geo())
        return ret_val





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer