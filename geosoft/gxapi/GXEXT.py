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
class GXEXT(gxapi_cy.WrapEXT):
    """
    GXEXT class.

    External (plug-in) image methods.
    """

    def __init__(self, handle=0):
        super(GXEXT, self).__init__(GXContext._get_tls_geo(), handle)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of `GXEXT <geosoft.gxapi.GXEXT>`
        
        :returns: A null `GXEXT <geosoft.gxapi.GXEXT>`
        :rtype:   GXEXT
        """
        return GXEXT()

    def is_null(self):
        """
        Check if this is a null (undefined) instance
        
        :returns: True if this is a null (undefined) instance, False otherwise.
        :rtype:   bool
        """
        return self._internal_handle() == 0



# Miscellaneous


    @classmethod
    def get_info(cls, img, xmin, ymin, xmax, ymax, ipj):
        """
        Retrieves information about an external image format.
        
        :param img:   Image Name
        :param xmin:  X Min
        :param ymin:  Y Min
        :param xmax:  X Max
        :param ymax:  Y Max
        :param ipj:   Projection Information
        :type  img:   str
        :type  xmin:  float_ref
        :type  ymin:  float_ref
        :type  xmax:  float_ref
        :type  ymax:  float_ref
        :type  ipj:   GXIPJ

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        xmin.value, ymin.value, xmax.value, ymax.value = gxapi_cy.WrapEXT._get_info(GXContext._get_tls_geo(), img.encode(), xmin.value, ymin.value, xmax.value, ymax.value, ipj)
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer