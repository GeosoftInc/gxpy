### extends 'class_empty.py'
from . import gxapi_cy

from geosoft.gxapi import GXContext, int_ref, float_ref, str_ref

### block Header
# NOTICE: The code generator will not replace the code in this block
### endblock Header

### block ClassImplementation
# NOTICE: Do not edit anything here, it is generated code
class GXVVEXP:
    """
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._wrapper = None

    def __del__(self):
        self._wrapper = None

    def __init__(self, wrapper=None):
        self._wrapper = wrapper if wrapper else gxapi_cy.WrapVVEXP(0)

    @classmethod
    def null(cls) -> 'GXVVEXP':
        """
        A null (undefined) instance of :class:`GXVVEXP`
        
        :returns: A null :class:`GX3DN`
        """
        return cls()

    def is_null(self) -> bool:
        """
        Check if the instance of :class:`GXVVEXP` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of :class:`GXVVEXP`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Miscellaneous



    def add_vv(self, p2: 'GXVV', p3: str) -> None:
        self._wrapper.add_vv(p2._wrapper, p3.encode())
        



    @classmethod
    def create(cls) -> 'GXVVEXP':
        ret_val = gxapi_cy.WrapVVEXP.create(GXContext._get_tls_geo())
        return GXVVEXP(ret_val)






    def do_formula(self, p2: str, p3: int) -> None:
        self._wrapper.do_formula(p2.encode(), p3)
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer