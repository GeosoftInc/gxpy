### extends 'class_empty.py'
from . import gxapi_cy

from geosoft.gxapi import GXContext, int_ref, float_ref, str_ref

### block Header
# NOTICE: The code generator will not replace the code in this block
### endblock Header

### block ClassImplementation
# NOTICE: Do not edit anything here, it is generated code
class GXLPT:
    """
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._wrapper = None

    def __del__(self):
        self._wrapper = None

    def __init__(self, wrapper=None):
        self._wrapper = wrapper if wrapper else gxapi_cy.WrapLPT(GXContext._get_tls_geo(), 0)

    @classmethod
    def null(cls) -> 'GXLPT':
        """
        A null (undefined) instance of :class:`GXLPT`
        
        :returns: A null :class:`GX3DN`
        """
        return cls()

    def is_null(self) -> bool:
        """
        Check if the instance of :class:`GXLPT` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of :class:`GXLPT`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Miscellaneous


    @classmethod
    def create(cls) -> 'GXLPT':
        ret_val = gxapi_cy.WrapLPT.create(GXContext._get_tls_geo())
        return GXLPT(ret_val)






    def get_lst(self, p2: 'GXLST') -> None:
        self._wrapper.get_lst(p2._wrapper)
        




    def get_standard_lst(self, p2: 'GXLST') -> None:
        self._wrapper.get_standard_lst(p2._wrapper)
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer