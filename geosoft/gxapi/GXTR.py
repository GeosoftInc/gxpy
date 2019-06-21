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
class GXTR(gxapi_cy.WrapTR):
    """
    GXTR class.

    The `GXTR <geosoft.gxapi.GXTR>` object contains trend information about a grid or
    grid pager. Currently, it is used only in conjunction with
    the `GXIMG.get_tr <geosoft.gxapi.GXIMG.get_tr>`, `GXIMG.set_tr <geosoft.gxapi.GXIMG.set_tr>`, and `GXPGU.trend <geosoft.gxapi.GXPGU.trend>` functions.
    """

    def __init__(self, handle=0):
        super(GXTR, self).__init__(GXContext._get_tls_geo(), handle)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of `GXTR <geosoft.gxapi.GXTR>`
        
        :returns: A null `GXTR <geosoft.gxapi.GXTR>`
        :rtype:   GXTR
        """
        return GXTR()

    def is_null(self):
        """
        Check if this is a null (undefined) instance
        
        :returns: True if this is a null (undefined) instance, False otherwise.
        :rtype:   bool
        """
        return self._internal_handle() == 0



# Miscellaneous


    @classmethod
    def create(cls, order):
        """
        Creates a Trend object
        
        :param order:  Trend order (must >=0 and <=3)
        :type  order:  int

        :returns:      `GXTR <geosoft.gxapi.GXTR>` Object
        :rtype:        GXTR

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        ret_val = gxapi_cy.WrapTR._create(GXContext._get_tls_geo(), order)
        return GXTR(ret_val)






    def copy(self, t_rs):
        """
        This method copies a table resource to another trend table resource.
        
        :param t_rs:  Source Trend Object to Copy
        :type  t_rs:  GXTR

        .. versionadded:: 8.1

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._copy(t_rs)
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer