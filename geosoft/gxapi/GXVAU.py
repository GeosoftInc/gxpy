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
class GXVAU(gxapi_cy.WrapVAU):
    """
    GXVAU class.

    This is not a class. These are methods that work on
    data stored in `GXVA <geosoft.gxapi.GXVA>` objects
    """

    def __init__(self, handle=0):
        super(GXVAU, self).__init__(GXContext._get_tls_geo(), handle)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of `GXVAU <geosoft.gxapi.GXVAU>`
        
        :returns: A null `GXVAU <geosoft.gxapi.GXVAU>`
        :rtype:   GXVAU
        """
        return GXVAU()

    def is_null(self):
        """
        Check if this is a null (undefined) instance
        
        :returns: True if this is a null (undefined) instance, False otherwise.
        :rtype:   bool
        """
        return self._internal_handle() == 0



# Miscellaneous


    @classmethod
    def prune(cls, v_ap, vv_r, o):
        """
        Prune values from a `GXVA <geosoft.gxapi.GXVA>` based on reference `GXVA <geosoft.gxapi.GXVA>`
        
        :param v_ap:  `GXVA <geosoft.gxapi.GXVA>` to prune
        :param vv_r:  Reference `GXVV <geosoft.gxapi.GXVV>`
        :param o:     :ref:`VAU_PRUNE`
        :type  v_ap:  GXVA
        :type  vv_r:  GXVV
        :type  o:     int

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** Pruning will shorten the `GXVA <geosoft.gxapi.GXVA>` by removing values
        that are either dummy or non-dummy in the reference
        `GXVA <geosoft.gxapi.GXVA>`
        """
        gxapi_cy.WrapVAU._prune(GXContext._get_tls_geo(), v_ap, vv_r, o)
        



    @classmethod
    def total_vector(cls, xva, yva, zva, tva):
        """
        Calculate total vector for X,Y and Z components
        
        :param xva:  X Component object
        :param yva:  Y Component object
        :param zva:  Z Component object
        :param tva:  Returned total vector `GXVA <geosoft.gxapi.GXVA>` object
        :type  xva:  GXVA
        :type  yva:  GXVA
        :type  zva:  GXVA
        :type  tva:  GXVA

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        gxapi_cy.WrapVAU._total_vector(GXContext._get_tls_geo(), xva, yva, zva, tva)
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer