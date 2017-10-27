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
class GXVVEXP:
    """
    GXVVEXP class.

    The `GXVVEXP <geosoft.gxapi.GXVVEXP>` class is similar to the `GXIEXP <geosoft.gxapi.GXIEXP>` class, but is used
    to apply math expressions to `GXVV <geosoft.gxapi.GXVV>` objects.
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._wrapper = None

    def __del__(self):
        self._wrapper = None

    def __init__(self, wrapper=None):
        self._wrapper = wrapper if wrapper else gxapi_cy.WrapVVEXP(GXContext._get_tls_geo(), 0)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of `GXVVEXP`
        
        :returns: A null `GXVVEXP`
        """
        return cls()

    def is_null(self):
        """
        Check if the instance of `GXVVEXP` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of `GXVVEXP`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Miscellaneous



    def add_vv(self, vv, var):
        """
        This method adds a `GXVV <geosoft.gxapi.GXVV>` to the `GXVVEXP <geosoft.gxapi.GXVVEXP>` object with a
        variable name.
        
        :param vv:     `GXVV <geosoft.gxapi.GXVV>` to add
        :param var:    Variable name
        :type  vv:     GXVV
        :type  var:    str

        .. versionadded:: 6.2
        """
        self._wrapper.add_vv(vv._wrapper, var.encode())
        



    @classmethod
    def create(cls):
        """
        This method creates an `GXVVEXP <geosoft.gxapi.GXVVEXP>` object.
        

        :returns:    `GXVVEXP <geosoft.gxapi.GXVVEXP>` Object
        :rtype:      GXVVEXP

        .. versionadded:: 6.2
        """
        ret_val = gxapi_cy.WrapVVEXP.create(GXContext._get_tls_geo())
        return GXVVEXP(ret_val)






    def do_formula(self, formula, max_len):
        """
        This method runs a formula on the grids.
        
        :param formula:  Formula
        :param max_len:  Max. Buff size
        :type  formula:  str
        :type  max_len:  int

        .. versionadded:: 6.2
        """
        self._wrapper.do_formula(formula.encode(), max_len)
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer