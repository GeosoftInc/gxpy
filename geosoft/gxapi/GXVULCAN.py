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
class GXVULCAN:
    """
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
    def null(cls) -> 'GXVULCAN':
        """
        A null (undefined) instance of :class:`GXVULCAN`
        
        :returns: A null :class:`GX3DN`
        """
        return cls()

    def is_null(self) -> bool:
        """
        Check if the instance of :class:`GXVULCAN` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of :class:`GXVULCAN`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Miscellaneous


    @classmethod
    def is_valid_triangulation_file(cls, p1: str) -> int:
        ret_val = gxapi_cy.WrapVULCAN.is_valid_triangulation_file(GXContext._get_tls_geo(), p1.encode())
        return ret_val



    @classmethod
    def is_valid_block_model_file(cls, p1: str) -> int:
        ret_val = gxapi_cy.WrapVULCAN.is_valid_block_model_file(GXContext._get_tls_geo(), p1.encode())
        return ret_val



    @classmethod
    def triangulation_to_view(cls, p1: str, p2: 'GXIPJ', p3: 'GXMVIEW', p4: str) -> None:
        gxapi_cy.WrapVULCAN.triangulation_to_view(GXContext._get_tls_geo(), p1.encode(), p2._wrapper, p3._wrapper, p4.encode())
        



    @classmethod
    def get_block_model_variable_info(cls, p1: str, p2: int, p3: 'GXLST') -> None:
        gxapi_cy.WrapVULCAN.get_block_model_variable_info(GXContext._get_tls_geo(), p1.encode(), p2, p3._wrapper)
        



    @classmethod
    def get_block_model_string_variable_values(cls, p1: str, p2: str, p3: 'GXLST') -> None:
        gxapi_cy.WrapVULCAN.get_block_model_string_variable_values(GXContext._get_tls_geo(), p1.encode(), p2.encode(), p3._wrapper)
        



    @classmethod
    def block_model_to_voxel(cls, p1: str, p2: 'GXIPJ', p3: str, p4: str, p5: int, p6: str) -> None:
        gxapi_cy.WrapVULCAN.block_model_to_voxel(GXContext._get_tls_geo(), p1.encode(), p2._wrapper, p3.encode(), p4.encode(), p5, p6.encode())
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer