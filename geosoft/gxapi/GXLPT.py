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
class GXLPT(gxapi_cy.WrapLPT):
    """
    GXLPT class.

    This class allows access to the current default line patterns.
    It does not allow the definition of individual patterns. It is
    is used primarily with `GXMAP <geosoft.gxapi.GXMAP>` class functions.
    """

    def __init__(self, handle=0):
        super(GXLPT, self).__init__(GXContext._get_tls_geo(), handle)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of `GXLPT <geosoft.gxapi.GXLPT>`
        
        :returns: A null `GXLPT <geosoft.gxapi.GXLPT>`
        :rtype:   GXLPT
        """
        return GXLPT()

    def is_null(self):
        """
        Check if this is a null (undefined) instance
        
        :returns: True if this is a null (undefined) instance, False otherwise.
        :rtype:   bool
        """
        return self._internal_handle() == 0



# Miscellaneous


    @classmethod
    def create(cls):
        """
        Creates a line pattern object with current default patterns.
        

        :returns:    `GXLPT <geosoft.gxapi.GXLPT>` Object
        :rtype:      GXLPT

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = gxapi_cy.WrapLPT._create(GXContext._get_tls_geo())
        return GXLPT(ret_val)






    def get_lst(self, lst):
        """
        Copies all pattern names into a `GXLST <geosoft.gxapi.GXLST>` object.
        
        :param lst:  `GXLST <geosoft.gxapi.GXLST>` Handle
        :type  lst:  GXLST

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._get_lst(lst)
        




    def get_standard_lst(self, lst):
        """
        Copies the six standard line types into a `GXLST <geosoft.gxapi.GXLST>` object.
        
        :param lst:  `GXLST <geosoft.gxapi.GXLST>` Handle
        :type  lst:  GXLST

        .. versionadded:: 9.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** The six standard line types are "solid", "long dash", "dotted", "short dash", "long, short dash" and "dash dot".
        """
        self._get_standard_lst(lst)
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer