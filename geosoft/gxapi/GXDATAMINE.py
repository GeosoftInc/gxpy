### extends 'class_empty.py'
from . import gxapi_cy

from geosoft.gxapi import GXContext, int_ref, float_ref, str_ref

### block Header
# NOTICE: The code generator will not replace the code in this block
### endblock Header

### block ClassImplementation
# NOTICE: Do not edit anything here, it is generated code
class GXDATAMINE:
    """
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._wrapper = None

    def __del__(self):
        self._wrapper = None

    def __init__(self, wrapper=None):
        self._wrapper = wrapper if wrapper else gxapi_cy.WrapDATAMINE(GXContext._get_tls_geo(), 0)

    @classmethod
    def null(cls) -> 'GXDATAMINE':
        """
        A null (undefined) instance of :class:`GXDATAMINE`
        
        :returns: A null :class:`GX3DN`
        """
        return cls()

    def is_null(self) -> bool:
        """
        Check if the instance of :class:`GXDATAMINE` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of :class:`GXDATAMINE`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Miscellaneous


    @classmethod
    def create_voxel(cls, p1: str, p2: str, p3: 'GXIPJ', p4: 'GXMETA', p5: str) -> None:
        gxapi_cy.WrapDATAMINE.create_voxel(GXContext._get_tls_geo(), p1.encode(), p2.encode(), p3._wrapper, p4._wrapper, p5.encode())
        



    @classmethod
    def numeric_field_lst(cls, p1: str, p2: 'GXLST') -> None:
        gxapi_cy.WrapDATAMINE.numeric_field_lst(GXContext._get_tls_geo(), p1.encode(), p2._wrapper)
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer