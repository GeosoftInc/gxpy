### extends 'class_empty.py'
from . import gxapi_cy

from geosoft.gxapi import GXContext, int_ref, float_ref, str_ref

### block Header
# NOTICE: The code generator will not replace the code in this block
### endblock Header

### block ClassImplementation
# NOTICE: Do not edit anything here, it is generated code
class GXMISC:
    """
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._wrapper = None

    def __del__(self):
        self._wrapper = None

    def __init__(self, wrapper=None):
        self._wrapper = wrapper if wrapper else gxapi_cy.WrapMISC(0)

    @classmethod
    def null(cls) -> 'GXMISC':
        """
        A null (undefined) instance of :class:`GXMISC`
        
        :returns: A null :class:`GX3DN`
        """
        return cls()

    def is_null(self) -> bool:
        """
        Check if the instance of :class:`GXMISC` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of :class:`GXMISC`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Miscellaneous


    @classmethod
    def convert_cg3to_raw(cls, p1: str, p2: str, p3: int) -> None:
        gxapi_cy.WrapMISC.convert_cg3to_raw(GXContext._get_tls_geo(), p1.encode(), p2.encode(), p3)
        



    @classmethod
    def convert_cg5to_raw(cls, p1: str, p2: str, p3: int) -> None:
        gxapi_cy.WrapMISC.convert_cg5to_raw(GXContext._get_tls_geo(), p1.encode(), p2.encode(), p3)
        



    @classmethod
    def ukoa2_tbl(cls, p1: str, p2: str, p3: str) -> None:
        gxapi_cy.WrapMISC.ukoa2_tbl(GXContext._get_tls_geo(), p1.encode(), p2.encode(), p3.encode())
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer