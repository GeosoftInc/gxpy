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
class GXEXP:
    """
    GXEXP class.

    :class:`GXEXP` objects are created from text strings that contain
    C-like math to be applied to channels in a database.
    It is used with the Math_DU function (see :class:`GXDU`). See also
    :class:`GXIEXP` for applying math expressions to images (grids).
    See also Math_DU applies expressions to the database
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._wrapper = None

    def __del__(self):
        self._wrapper = None

    def __init__(self, wrapper=None):
        self._wrapper = wrapper if wrapper else gxapi_cy.WrapEXP(GXContext._get_tls_geo(), 0)

    @classmethod
    def null(cls) -> 'GXEXP':
        """
        A null (undefined) instance of :class:`GXEXP`
        
        :returns: A null :class:`GXEXP`
        """
        return cls()

    def is_null(self) -> bool:
        """
        Check if the instance of :class:`GXEXP` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of :class:`GXEXP`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Miscellaneous


    @classmethod
    def create(cls, p1: 'GXDB', p2: str, p3: int) -> 'GXEXP':
        ret_val = gxapi_cy.WrapEXP.create(GXContext._get_tls_geo(), p1._wrapper, p2.encode(), p3)
        return GXEXP(ret_val)



    @classmethod
    def create_file(cls, p1: 'GXDB', p2: str) -> 'GXEXP':
        ret_val = gxapi_cy.WrapEXP.create_file(GXContext._get_tls_geo(), p1._wrapper, p2.encode())
        return GXEXP(ret_val)







### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer