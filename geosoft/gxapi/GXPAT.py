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
class GXPAT(gxapi_cy.WrapPAT):
    """
    GXPAT class.

    A `GXPAT <geosoft.gxapi.GXPAT>` object is created from a Geosoft format pattern file.
    It contains all the individual patterns listed in the file.

    Notes: You may create your own fill patterns. They can be added to the "user.pat"
    file in the <geosoft>\\user\\etc directory. User pattern numbers should be in the 
    range between 20000 and 29999.
    """

    def __init__(self, handle=0):
        super(GXPAT, self).__init__(GXContext._get_tls_geo(), handle)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of `GXPAT <geosoft.gxapi.GXPAT>`
        
        :returns: A null `GXPAT <geosoft.gxapi.GXPAT>`
        :rtype:   GXPAT
        """
        return GXPAT()

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
        Creates a pattern object with current default patterns.
        

        :returns:    `GXPAT <geosoft.gxapi.GXPAT>` object
        :rtype:      GXPAT

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = gxapi_cy.WrapPAT._create(GXContext._get_tls_geo())
        return GXPAT(ret_val)






    def get_lst(self, cl, lst):
        """
        Copies all pattern names into a `GXLST <geosoft.gxapi.GXLST>` object.
        
        :param cl:   Class name ("" for all classes)
        :param lst:  `GXLST <geosoft.gxapi.GXLST>` Handle
        :type  cl:   str
        :type  lst:  GXLST

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Returns a list of the available patterns.
        There will always be at least two items,
        "None" and "Solid Fill"
        """
        self._get_lst(cl.encode(), lst)
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer