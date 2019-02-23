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
class GXVVEXP(gxapi_cy.WrapVVEXP):
    """
    GXVVEXP class.

    The `GXVVEXP <geosoft.gxapi.GXVVEXP>` class is similar to the `GXIEXP <geosoft.gxapi.GXIEXP>` class, but is used
    to apply math expressions to `GXVV <geosoft.gxapi.GXVV>` objects.
    """

    def __init__(self, handle=0):
        super().__init__(GXContext._get_tls_geo(), handle)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of `GXVVEXP <geosoft.gxapi.GXVVEXP>`
        
        :returns: A null `GXVVEXP <geosoft.gxapi.GXVVEXP>`
        :rtype:   GXVVEXP
        """
        return GXVVEXP()

    def is_null(self):
        """
        Check if this is a null (undefined) instance
        
        :returns: True if this is a null (undefined) instance, False otherwise.
        :rtype:   bool
        """
        return self._internal_handle() == 0



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

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        self._add_vv(vv, var.encode())
        



    @classmethod
    def create(cls):
        """
        This method creates an `GXVVEXP <geosoft.gxapi.GXVVEXP>` object.
        

        :returns:    `GXVVEXP <geosoft.gxapi.GXVVEXP>` Object
        :rtype:      GXVVEXP

        .. versionadded:: 6.2

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        ret_val = gxapi_cy.WrapVVEXP._create(GXContext._get_tls_geo())
        return GXVVEXP(ret_val)






    def do_formula(self, formula, unused):
        """
        This method runs a formula on the grids.
        
        :param formula:  Formula
        :param unused:   Legacy parameter, no longer used.
        :type  formula:  str
        :type  unused:   int

        .. versionadded:: 6.2

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        self._do_formula(formula.encode(), unused)
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer