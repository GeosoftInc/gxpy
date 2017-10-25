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
class GXDAT:
    """
    GXDAT class.

    The :class:`GXDAT` object is used to access data from an variety of data sources
    using the same access functions. The :class:`GXDAT` interface supports data access
    on a point-by-point, of line-by-line basis.  For example,
    the Run_BIGRID function uses 2 :class:`GXDAT` objects - one :class:`GXDAT` associated with the
    input data source, which is read line-by-line, and a second associated with
    the output grid file output grid file.
    
    Use a specific :class:`GXDAT` creation method for an associated
    information source in order to make a :class:`GXDAT` as required
    by a specific processing function.  The gridding methods all use DATs.
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._wrapper = None

    def __del__(self):
        self._wrapper = None

    def __init__(self, wrapper=None):
        self._wrapper = wrapper if wrapper else gxapi_cy.WrapDAT(GXContext._get_tls_geo(), 0)

    @classmethod
    def null(cls) -> 'GXDAT':
        """
        A null (undefined) instance of :class:`GXDAT`
        
        :returns: A null :class:`GXDAT`
        """
        return cls()

    def is_null(self) -> bool:
        """
        Check if the instance of :class:`GXDAT` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of :class:`GXDAT`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Miscellaneous


    @classmethod
    def create_db(cls, p1: 'GXDB', p2: str, p3: str, p4: str) -> 'GXDAT':
        ret_val = gxapi_cy.WrapDAT.create_db(GXContext._get_tls_geo(), p1._wrapper, p2.encode(), p3.encode(), p4.encode())
        return GXDAT(ret_val)



    @classmethod
    def create_xgd(cls, p1: str, p2: int) -> 'GXDAT':
        ret_val = gxapi_cy.WrapDAT.create_xgd(GXContext._get_tls_geo(), p1.encode(), p2)
        return GXDAT(ret_val)





    @classmethod
    def get_lst(cls, p1: 'GXLST', p2: str, p3: int, p4: int) -> None:
        gxapi_cy.WrapDAT.get_lst(GXContext._get_tls_geo(), p1._wrapper, p2.encode(), p3, p4)
        




    def range_xyz(self, p2: float_ref, p3: float_ref, p4: float_ref, p5: float_ref, p6: float_ref, p7: float_ref, p8: int_ref) -> None:
        p2.value, p3.value, p4.value, p5.value, p6.value, p7.value, p8.value = self._wrapper.range_xyz(p2.value, p3.value, p4.value, p5.value, p6.value, p7.value, p8.value)
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer