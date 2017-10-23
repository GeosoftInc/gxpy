### extends 'class_empty.py'
from . import gxapi_cy

from geosoft.gxapi import GXContext, int_ref, float_ref, str_ref

### block Header
# NOTICE: The code generator will not replace the code in this block
### endblock Header

### block ClassImplementation
# NOTICE: Do not edit anything here, it is generated code
class GXPGEXP:
    """
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._wrapper = None

    def __del__(self):
        self._wrapper = None

    def __init__(self, wrapper=None):
        self._wrapper = wrapper if wrapper else gxapi_cy.WrapPGEXP(0)

    @classmethod
    def null(cls) -> 'GXPGEXP':
        """
        A null (undefined) instance of :class:`GXPGEXP`
        
        :returns: A null :class:`GX3DN`
        """
        return cls()

    def is_null(self) -> bool:
        """
        Check if the instance of :class:`GXPGEXP` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of :class:`GXPGEXP`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Miscellaneous



    def add_pager(self, p2: 'GXPG', p3: str) -> None:
        self._wrapper.add_pager(p2, p3.encode())
        



    @classmethod
    def create(cls) -> 'GXPGEXP':
        ret_val = gxapi_cy.WrapPGEXP.create(GXContext._get_tls_geo())
        return GXPGEXP(ret_val)






    def do_formula(self, p2: str, p3: int) -> None:
        self._wrapper.do_formula(p2.encode(), p3)
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer