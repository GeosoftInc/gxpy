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
class GXPGEXP(gxapi_cy.WrapPGEXP):
    """
    GXPGEXP class.

    The `GXPGEXP <geosoft.gxapi.GXPGEXP>` class is similar to the `GXEXP <geosoft.gxapi.GXEXP>` class, but is used
    to apply math expressions to pagers (`GXPG <geosoft.gxapi.GXPG>` objects).

    It works only on PGs of the same dimensions.
    """

    def __init__(self, handle=0):
        super().__init__(GXContext._get_tls_geo(), handle)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of `GXPGEXP <geosoft.gxapi.GXPGEXP>`
        
        :returns: A null `GXPGEXP <geosoft.gxapi.GXPGEXP>`
        :rtype:   GXPGEXP
        """
        return GXPGEXP()

    def is_null(self):
        """
        Check if this is a null (undefined) instance
        
        :returns: True if this is a null (undefined) instance, False otherwise.
        :rtype:   bool
        """
        return self._internal_handle() == 0



# Miscellaneous



    def add_pager(self, pg, var):
        """
        This method adds an pager to the `GXPGEXP <geosoft.gxapi.GXPGEXP>` object with a
        variable name.
        
        :param pg:     Pager to add
        :param var:    Variable name
        :type  pg:     GXPG
        :type  var:    str

        .. versionadded:: 7.1

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        self._add_pager(pg, var.encode())
        



    @classmethod
    def create(cls):
        """
        This method creates an `GXPGEXP <geosoft.gxapi.GXPGEXP>` object.
        

        :returns:    `GXPGEXP <geosoft.gxapi.GXPGEXP>` Object
        :rtype:      GXPGEXP

        .. versionadded:: 7.1

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        ret_val = gxapi_cy.WrapPGEXP._create(GXContext._get_tls_geo())
        return GXPGEXP(ret_val)






    def do_formula(self, formula, unused):
        """
        This method runs a formula on the pagers.
        
        :param formula:  Formula
        :param unused:   Legacy parameter, no longer used.
        :type  formula:  str
        :type  unused:   int

        .. versionadded:: 7.1

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