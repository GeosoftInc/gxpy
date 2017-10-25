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

    The :class:`geosoft.gxapi.GXVULCAN` class is used for importing Maptek® Vulcan block and triangulation files.
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
        A null (undefined) instance of :class:`geosoft.gxapi.GXVULCAN`
        
        :returns: A null :class:`geosoft.gxapi.GXVULCAN`
        """
        return cls()

    def is_null(self):
        """
        Check if the instance of :class:`geosoft.gxapi.GXVULCAN` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of :class:`geosoft.gxapi.GXVULCAN`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Miscellaneous


    @classmethod
    def is_valid_triangulation_file(cls, p1):
        """
        Check if the given file can be opened as a Vulcan triangulation file.
        """
        ret_val = gxapi_cy.WrapVULCAN.is_valid_triangulation_file(GXContext._get_tls_geo(), p1.encode())
        return ret_val



    @classmethod
    def is_valid_block_model_file(cls, p1):
        """
        Check if the given file can be opened as a Vulcan block model file.
        """
        ret_val = gxapi_cy.WrapVULCAN.is_valid_block_model_file(GXContext._get_tls_geo(), p1.encode())
        return ret_val



    @classmethod
    def triangulation_to_view(cls, p1, p2, p3, p4):
        """
        Draw triangle edges in a Vulcan triangulation file to a 3D view in a map.
        """
        gxapi_cy.WrapVULCAN.triangulation_to_view(GXContext._get_tls_geo(), p1.encode(), p2._wrapper, p3._wrapper, p4.encode())
        



    @classmethod
    def get_block_model_variable_info(cls, p1, p2, p3):
        """
        Query a block model for the variable names and descriptions.
        """
        gxapi_cy.WrapVULCAN.get_block_model_variable_info(GXContext._get_tls_geo(), p1.encode(), p2, p3._wrapper)
        



    @classmethod
    def get_block_model_string_variable_values(cls, p1, p2, p3):
        """
        Query a block model for the values a string variable can assume.
        """
        gxapi_cy.WrapVULCAN.get_block_model_string_variable_values(GXContext._get_tls_geo(), p1.encode(), p2.encode(), p3._wrapper)
        



    @classmethod
    def block_model_to_voxel(cls, p1, p2, p3, p4, p5, p6):
        """
        Create a Geosoft voxel file from a Vulcan block model file.
        """
        gxapi_cy.WrapVULCAN.block_model_to_voxel(GXContext._get_tls_geo(), p1.encode(), p2._wrapper, p3.encode(), p4.encode(), p5, p6.encode())
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer