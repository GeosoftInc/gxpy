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
class GXVULCAN:
    """
    GXVULCAN class.

    The `GXVULCAN` class is used for importing Maptek® Vulcan block and triangulation files.
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._wrapper = None

    def __del__(self):
        self._wrapper = None

    def __init__(self, wrapper=None):
        self._wrapper = wrapper if wrapper else gxapi_cy.WrapVULCAN(GXContext._get_tls_geo(), 0)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of `GXVULCAN`
        
        :returns: A null `GXVULCAN`
        """
        return cls()

    def is_null(self):
        """
        Check if the instance of `GXVULCAN` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of `GXVULCAN`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Miscellaneous


    @classmethod
    def is_valid_triangulation_file(cls, triangulation_file):
        """
        Check if the given file can be opened as a Vulcan triangulation file.
        """
        ret_val = gxapi_cy.WrapVULCAN.is_valid_triangulation_file(GXContext._get_tls_geo(), triangulation_file.encode())
        return ret_val



    @classmethod
    def is_valid_block_model_file(cls, block_model_file):
        """
        Check if the given file can be opened as a Vulcan block model file.
        """
        ret_val = gxapi_cy.WrapVULCAN.is_valid_block_model_file(GXContext._get_tls_geo(), block_model_file.encode())
        return ret_val



    @classmethod
    def triangulation_to_view(cls, triangulation_file, ipj, mview, new_group_name):
        """
        Draw triangle edges in a Vulcan triangulation file to a 3D view in a map.
        """
        gxapi_cy.WrapVULCAN.triangulation_to_view(GXContext._get_tls_geo(), triangulation_file.encode(), ipj._wrapper, mview._wrapper, new_group_name.encode())
        



    @classmethod
    def get_block_model_variable_info(cls, block_model_file, query, lst):
        """
        Query a block model for the variable names and descriptions.
        """
        gxapi_cy.WrapVULCAN.get_block_model_variable_info(GXContext._get_tls_geo(), block_model_file.encode(), query, lst._wrapper)
        



    @classmethod
    def get_block_model_string_variable_values(cls, block_model_file, variable_name, lst):
        """
        Query a block model for the values a string variable can assume.
        """
        gxapi_cy.WrapVULCAN.get_block_model_string_variable_values(GXContext._get_tls_geo(), block_model_file.encode(), variable_name.encode(), lst._wrapper)
        



    @classmethod
    def block_model_to_voxel(cls, block_model_file, ipj, variable_to_export, output_voxel_filename, remove_default_values, rock_code_filename):
        """
        Create a Geosoft voxel file from a Vulcan block model file.
        """
        gxapi_cy.WrapVULCAN.block_model_to_voxel(GXContext._get_tls_geo(), block_model_file.encode(), ipj._wrapper, variable_to_export.encode(), output_voxel_filename.encode(), remove_default_values, rock_code_filename.encode())
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer