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
class GXIEXP:
    """
    GXIEXP class.

    The :class:`GXIEXP` class is similar to the :class:`GXEXP` class, but is used
    to apply math expressions to grids (:class:`GXIMG` objects).
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._wrapper = None

    def __del__(self):
        self._wrapper = None

    def __init__(self, wrapper=None):
        self._wrapper = wrapper if wrapper else gxapi_cy.WrapIEXP(GXContext._get_tls_geo(), 0)

    @classmethod
    def null(cls) -> 'GXIEXP':
        """
        A null (undefined) instance of :class:`GXIEXP`
        
        :returns: A null :class:`GXIEXP`
        """
        return cls()

    def is_null(self) -> bool:
        """
        Check if the instance of :class:`GXIEXP` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of :class:`GXIEXP`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Miscellaneous



    def add_grid(self, p2: 'GXIMG', p3: str) -> None:
        self._wrapper.add_grid(p2._wrapper, p3.encode())
        



    @classmethod
    def create(cls) -> 'GXIEXP':
        ret_val = gxapi_cy.WrapIEXP.create(GXContext._get_tls_geo())
        return GXIEXP(ret_val)






    def do_formula(self, p2: str, p3: int) -> None:
        self._wrapper.do_formula(p2.encode(), p3)
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer