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
class GXPROJ:
    """
    GXPROJ class.

    Project functions
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._wrapper = None

    def __del__(self):
        self._wrapper = None

    def __init__(self, wrapper=None):
        self._wrapper = wrapper if wrapper else gxapi_cy.WrapPROJ(GXContext._get_tls_geo(), 0)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of `GXPROJ`
        
        :returns: A null `GXPROJ`
        """
        return cls()

    def is_null(self):
        """
        Check if the instance of `GXPROJ` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of `GXPROJ`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Drag-and-drop methods


    @classmethod
    def drop_map_clip_data(cls, hglobal):
        """
        Drop Map clipboard data in the current project (workspace background)
        """
        gxapi_cy.WrapPROJ.drop_map_clip_data(GXContext._get_tls_geo(), hglobal)
        




# Miscellaneous


    @classmethod
    def add_document(cls, name, type, display):
        """
        Adds (and opens) a document file in the current project.

        **Note:**

        The passed file name must be a valid
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
        ret_val = gxapi_cy.WrapPROJ.add_document(GXContext._get_tls_geo(), name.encode(), type.encode(), display)
        return ret_val



    @classmethod
    def add_document_without_opening(cls, name, type):
        """
        Adds (and opens) a document file in the current project.

        **Note:**

        The passed file name must be a valid
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
        ret_val = gxapi_cy.WrapPROJ.add_document_without_opening(GXContext._get_tls_geo(), name.encode(), type.encode())
        return ret_val



    @classmethod
    def get_command_environment(cls):
        """
        The current command environment
        """
        ret_val = gxapi_cy.WrapPROJ.get_command_environment(GXContext._get_tls_geo())
        return ret_val



    @classmethod
    def list_documents(cls, gvv, type):
        """
        Fills a `GXVV` with documents of a certain type.

        **Note:**

        The type string can be one of the following:
        Database         List Databases.
        Grid             List Grids.
        Map              List Maps.
        3DView           List 3D Views.
        Voxel            List Voxels.
        VoxelInversion   List VOXI Documents.
        `GXMXD`              List ArcGIS MXDs.
        GMS3D            List GM-`GXSYS` 3D Models.
        GMS2D            List GM-`GXSYS` 2D Models.
        All              Lists all files.
        """
        ret_val = gxapi_cy.WrapPROJ.list_documents(GXContext._get_tls_geo(), gvv._wrapper, type.encode())
        return ret_val



    @classmethod
    def list_loaded_documents(cls, gvv, type):
        """
        Fills a `GXVV` with loaded documents of a certain type.

        **Note:**

        The type string can be one of the following:
        Database         List Databases.
        Grid             List Grids.
        Map              List Maps.
        3DView           List 3D Views.
        Voxel            List Voxels.
        VoxelInversion   List VOXI Documents.
        `GXMXD`              List ArcGIS MXDs.
        GMS3D            List GM-`GXSYS` 3D Models.
        GMS2D            List GM-`GXSYS` 2D Models.
        All              Lists all files.
        """
        ret_val = gxapi_cy.WrapPROJ.list_loaded_documents(GXContext._get_tls_geo(), gvv._wrapper, type.encode())
        return ret_val



    @classmethod
    def current_document(cls, name, type):
        """
        Get the name and type of the loaded document with focus.
        """
        name.value, type.value = gxapi_cy.WrapPROJ.current_document(GXContext._get_tls_geo(), name.value.encode(), type.value.encode())
        



    @classmethod
    def current_document_of_type(cls, name, type):
        """
        Get the name of a loaded document of a specific type.
        """
        name.value = gxapi_cy.WrapPROJ.current_document_of_type(GXContext._get_tls_geo(), name.value.encode(), type.encode())
        



    @classmethod
    def list_tools(cls, lst, type):
        """
        Fills an `GXLST` object with tools of a certain type and
        notes the current visibility setting.

        **Note:**

        GX will terminate if there is an error.
        
        `GXLST` object will hold the tool name in the name column and
        include whether the tool is currently visible in the value
        column (1=visible, 0-hidden).
        """
        ret_val = gxapi_cy.WrapPROJ.list_tools(GXContext._get_tls_geo(), lst._wrapper, type)
        return ret_val



    @classmethod
    def remove_document(cls, name):
        """
        Removes (and closes if visible) a document from the current project.

        **Note:**

        The passed file name must be a valid
        file name complete with an extension and
        qualifiers (if applicable).
        """
        ret_val = gxapi_cy.WrapPROJ.remove_document(GXContext._get_tls_geo(), name.encode())
        return ret_val



    @classmethod
    def remove_tool(cls, name):
        """
        Removes (and closes if visible) a auxiliary tool from the current project.

        **Note:**

        Nothing
        """
        ret_val = gxapi_cy.WrapPROJ.remove_tool(GXContext._get_tls_geo(), name.encode())
        return ret_val



    @classmethod
    def save_close_documents(cls, type):
        """
        Saves and closes (if visible) documents contained in the current project.

        **Note:**

        This wrapper brings up the save dialog tool to allow
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
        ret_val = gxapi_cy.WrapPROJ.save_close_documents(GXContext._get_tls_geo(), type.encode())
        return ret_val



    @classmethod
    def get_name(cls, name):
        """
        Return the name of the project file.

        **Note:**

        Return the name of the project file.
        """
        name.value = gxapi_cy.WrapPROJ.get_name(GXContext._get_tls_geo(), name.value.encode())
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer