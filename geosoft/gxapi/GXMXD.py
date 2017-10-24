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
class GXMXD:
    """
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._wrapper = None

    def __del__(self):
        self._wrapper = None

    def __init__(self, wrapper=None):
        self._wrapper = wrapper if wrapper else gxapi_cy.WrapMXD(GXContext._get_tls_geo(), 0)

    @classmethod
    def null(cls) -> 'GXMXD':
        """
        A null (undefined) instance of :class:`GXMXD`
        
        :returns: A null :class:`GX3DN`
        """
        return cls()

    def is_null(self) -> bool:
        """
        Check if the instance of :class:`GXMXD` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of :class:`GXMXD`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Miscellaneous


    @classmethod
    def create_metadata(cls, p1: str) -> None:
        gxapi_cy.WrapMXD.create_metadata(GXContext._get_tls_geo(), p1.encode())
        



    @classmethod
    def convert_to_map(cls, p1: str, p2: str) -> None:
        gxapi_cy.WrapMXD.convert_to_map(GXContext._get_tls_geo(), p1.encode(), p2.encode())
        



    @classmethod
    def sync(cls, p1: str) -> None:
        gxapi_cy.WrapMXD.sync(GXContext._get_tls_geo(), p1.encode())
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer