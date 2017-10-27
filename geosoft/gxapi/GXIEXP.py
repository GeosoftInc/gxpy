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
class GXIEXP:
    """
    GXIEXP class.

    The `GXIEXP <geosoft.gxapi.GXIEXP>` class is similar to the `GXEXP <geosoft.gxapi.GXEXP>` class, but is used
    to apply math expressions to grids (`GXIMG <geosoft.gxapi.GXIMG>` objects).
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
    def null(cls):
        """
        A null (undefined) instance of `GXIEXP`
        
        :returns: A null `GXIEXP`
        """
        return cls()

    def is_null(self):
        """
        Check if the instance of `GXIEXP` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of `GXIEXP`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Miscellaneous



    def add_grid(self, img, var):
        """
        This method adds an image to the `GXIEXP <geosoft.gxapi.GXIEXP>` object with a
        variable name.
        """
        self._wrapper.add_grid(img._wrapper, var.encode())
        



    @classmethod
    def create(cls):
        """
        This method creates an `GXIEXP <geosoft.gxapi.GXIEXP>` object.
        """
        ret_val = gxapi_cy.WrapIEXP.create(GXContext._get_tls_geo())
        return GXIEXP(ret_val)






    def do_formula(self, formula, max_len):
        """
        This method runs a formula on the grids.
        """
        self._wrapper.do_formula(formula.encode(), max_len)
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer