### extends 'class_empty.py'
### block ClassImports
# NOTICE: Do not edit anything here, it is generated code
from typing import NewType
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

    :class:`geosoft.gxapi.GXEXP` objects are created from text strings that contain
    C-like math to be applied to channels in a database.
    It is used with the Math_DU function (see :class:`geosoft.gxapi.GXDU`). See also
    :class:`geosoft.gxapi.GXIEXP` for applying math expressions to images (grids).
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
    def null(cls):
        """
        A null (undefined) instance of :class:`geosoft.gxapi.GXEXP`
        
        :returns: A null :class:`geosoft.gxapi.GXEXP`
        """
        return cls()

    def is_null(self):
        """
        Check if the instance of :class:`geosoft.gxapi.GXEXP` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of :class:`geosoft.gxapi.GXEXP`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Miscellaneous


    @classmethod
    def create(cls, p1, p2, p3):
        """
        This method creates an :class:`geosoft.gxapi.GXEXP` object.

        **Note:**

        Expressions are strings that contain C-like math to be
        applied to channels in a database.  For example, following
        an expression:
        
        ::
        
           "@a = mag-64000; @b = gravity*100;
            $sRatio = @a/@b;
            MULT = @a *@b;"
        
        Rules:
        
           ``;``
             terminates a sub-expression
        
           ``@``
             prefix to a temporary name, which is a double precision
             floating point number to be used later in the same
             expression.
        
           ``$``
             prefix to a local GX variable name.  Such names will be
             evaluated to the variable value at the time Create_EXP
             is called.
        
        All other tokens are assumed to be channel names.
        """
        ret_val = gxapi_cy.WrapEXP.create(GXContext._get_tls_geo(), p1._wrapper, p2.encode(), p3)
        return GXEXP(ret_val)



    @classmethod
    def create_file(cls, p1, p2):
        """
        This method creates an :class:`geosoft.gxapi.GXEXP` object from a file
        """
        ret_val = gxapi_cy.WrapEXP.create_file(GXContext._get_tls_geo(), p1._wrapper, p2.encode())
        return GXEXP(ret_val)







### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer