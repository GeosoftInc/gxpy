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
class GXGD:
    """
    GXGD class.

    This class provides access to Geosoft grid files using an old interface.
    Only the `GXDU.sample_gd <geosoft.gxapi.GXDU.sample_gd>` function uses this class.  Use the `GXIMG <geosoft.gxapi.GXIMG>` class
    instead.
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._wrapper = None

    def __del__(self):
        self._wrapper = None

    def __init__(self, wrapper=None):
        self._wrapper = wrapper if wrapper else gxapi_cy.WrapGD(GXContext._get_tls_geo(), 0)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of `GXGD`
        
        :returns: A null `GXGD`
        """
        return cls()

    def is_null(self):
        """
        Check if the instance of `GXGD` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of `GXGD`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Miscellaneous


    @classmethod
    def create(cls, name, type):
        """
        This method creates a `GXGD <geosoft.gxapi.GXGD>` object.
        """
        ret_val = gxapi_cy.WrapGD.create(GXContext._get_tls_geo(), name.encode(), type)
        return GXGD(ret_val)







### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer