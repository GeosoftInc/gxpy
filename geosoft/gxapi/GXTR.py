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
class GXTR:
    """
    GXTR class.

    The :class:`GXTR` object contains trend information about a grid or
    grid pager. Currently, it is used only in conjunction with
    the GetTR_IMG, SetTR_IMG, and Trend_PGU functions.
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._wrapper = None

    def __del__(self):
        self._wrapper = None

    def __init__(self, wrapper=None):
        self._wrapper = wrapper if wrapper else gxapi_cy.WrapTR(GXContext._get_tls_geo(), 0)

    @classmethod
    def null(cls) -> 'GXTR':
        """
        A null (undefined) instance of :class:`GXTR`
        
        :returns: A null :class:`GXTR`
        """
        return cls()

    def is_null(self) -> bool:
        """
        Check if the instance of :class:`GXTR` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of :class:`GXTR`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Miscellaneous


    @classmethod
    def create(cls, p1: int) -> 'GXTR':
        ret_val = gxapi_cy.WrapTR.create(GXContext._get_tls_geo(), p1)
        return GXTR(ret_val)






    def copy(self, p2: 'GXTR') -> None:
        self._wrapper.copy(p2._wrapper)
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer