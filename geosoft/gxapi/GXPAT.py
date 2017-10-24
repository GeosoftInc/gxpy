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
class GXPAT:
    """
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._wrapper = None

    def __del__(self):
        self._wrapper = None

    def __init__(self, wrapper=None):
        self._wrapper = wrapper if wrapper else gxapi_cy.WrapPAT(GXContext._get_tls_geo(), 0)

    @classmethod
    def null(cls) -> 'GXPAT':
        """
        A null (undefined) instance of :class:`GXPAT`
        
        :returns: A null :class:`GX3DN`
        """
        return cls()

    def is_null(self) -> bool:
        """
        Check if the instance of :class:`GXPAT` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of :class:`GXPAT`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Miscellaneous


    @classmethod
    def create(cls) -> 'GXPAT':
        ret_val = gxapi_cy.WrapPAT.create(GXContext._get_tls_geo())
        return GXPAT(ret_val)






    def get_lst(self, p2: str, p3: 'GXLST') -> None:
        self._wrapper.get_lst(p2.encode(), p3._wrapper)
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer