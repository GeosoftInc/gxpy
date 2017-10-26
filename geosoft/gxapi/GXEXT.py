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
class GXEXT:
    """
    GXEXT class.

    External (plug-in) image methods.
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._wrapper = None

    def __del__(self):
        self._wrapper = None

    def __init__(self, wrapper=None):
        self._wrapper = wrapper if wrapper else gxapi_cy.WrapEXT(GXContext._get_tls_geo(), 0)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of `GXEXT`
        
        :returns: A null `GXEXT`
        """
        return cls()

    def is_null(self):
        """
        Check if the instance of `GXEXT` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of `GXEXT`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Miscellaneous


    @classmethod
    def get_info(cls, img, xmin, ymin, xmax, ymax, ipj):
        """
        Retrieves information about an external image format.
        """
        xmin.value, ymin.value, xmax.value, ymax.value = gxapi_cy.WrapEXT.get_info(GXContext._get_tls_geo(), img.encode(), xmin.value, ymin.value, xmax.value, ymax.value, ipj._wrapper)
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer