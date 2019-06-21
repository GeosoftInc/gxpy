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
            Voxel         
            VoxelInversion
            GMS3D         
            GMS2D
        """
        ret_val = gxapi_cy.WrapPROJ._add_document_without_opening(GXContext._get_tls_geo(), name.encode(), type.encode())
        return ret_val



    @classmethod
    def get_command_environment(cls):
        """
        The current command environment
        

        :returns:    :ref:`COMMAND_ENV`

                  Notes									We are moving towards embedded tools and menus and this setting can be
                  queried from the project to determine how specific commands should react.
                  Only 3D viewer is currently making use of this.
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
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer