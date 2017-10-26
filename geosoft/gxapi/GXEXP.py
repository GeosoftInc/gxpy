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

    `GXEXP` objects are created from text strings that contain
    C-like math to be applied to channels in a database.
    It is used with the `GXDU.math` function (see `GXDU`). See also
    `GXIEXP` for applying math expressions to images (grids).
    See also `GXDU.math` applies expressions to the database
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
        A null (undefined) instance of `GXEXP`
        
        :returns: A null `GXEXP`
        """
        return cls()

    def is_null(self):
        """
        Check if the instance of `GXEXP` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of `GXEXP`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Miscellaneous


    @classmethod
    def create(cls, db, formula, max_len):
        """
        This method creates an `GXEXP` object.

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
             evaluated to the variable value at the time `create`
             is called.
        
        All other tokens are assumed to be channel names.
        """
        ret_val = gxapi_cy.WrapEXP.create(GXContext._get_tls_geo(), db._wrapper, formula.encode(), max_len)
        return GXEXP(ret_val)



    @classmethod
    def create_file(cls, db, file):
        """
        This method creates an `GXEXP` object from a file
        """
        ret_val = gxapi_cy.WrapEXP.create_file(GXContext._get_tls_geo(), db._wrapper, file.encode())
        return GXEXP(ret_val)







### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer