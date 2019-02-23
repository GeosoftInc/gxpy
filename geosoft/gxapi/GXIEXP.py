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
class GXIEXP(gxapi_cy.WrapIEXP):
    """
    GXIEXP class.

    The `GXIEXP <geosoft.gxapi.GXIEXP>` class is similar to the `GXEXP <geosoft.gxapi.GXEXP>` class, but is used
    to apply math expressions to grids (`GXIMG <geosoft.gxapi.GXIMG>` objects).
    """

    def __init__(self, handle=0):
        super().__init__(GXContext._get_tls_geo(), handle)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of `GXIEXP <geosoft.gxapi.GXIEXP>`
        
        :returns: A null `GXIEXP <geosoft.gxapi.GXIEXP>`
        :rtype:   GXIEXP
        """
        return GXIEXP()

    def is_null(self):
        """
        Check if this is a null (undefined) instance
        
        :returns: True if this is a null (undefined) instance, False otherwise.
        :rtype:   bool
        """
        return self._internal_handle() == 0



# Miscellaneous



    def add_grid(self, img, var):
        """
        This method adds an image to the `GXIEXP <geosoft.gxapi.GXIEXP>` object with a
        variable name.
        
        :param img:   Image to add
        :param var:   Variable name
        :type  img:   GXIMG
        :type  var:   str

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        self._add_grid(img, var.encode())
        



    @classmethod
    def create(cls):
        """
        This method creates an `GXIEXP <geosoft.gxapi.GXIEXP>` object.
        

        :returns:    `GXIEXP <geosoft.gxapi.GXIEXP>` Object
        :rtype:      GXIEXP

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        ret_val = gxapi_cy.WrapIEXP._create(GXContext._get_tls_geo())
        return GXIEXP(ret_val)






    def do_formula(self, formula, unused):
        """
        This method runs a formula on the grids.
        
        :param formula:  Formula
        :param unused:   Legacy parameter, no longer used.
        :type  formula:  str
        :type  unused:   int

        .. versionadded:: 5.0

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