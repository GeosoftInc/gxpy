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
class GXLMSG:
    """
    GXLMSG class.

    Message class methods.
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._wrapper = None

    def __del__(self):
        self._wrapper = None

    def __init__(self, wrapper=None):
        self._wrapper = wrapper if wrapper else gxapi_cy.WrapLMSG(GXContext._get_tls_geo(), 0)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of `GXLMSG`
        
        :returns: A null `GXLMSG`
        """
        return cls()

    def is_null(self):
        """
        Check if the instance of `GXLMSG` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of `GXLMSG`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Miscellaneous


    @classmethod
    def goto_point(cls, x, y, z, ipj):
        """
        Sends a move cursor message
        """
        gxapi_cy.WrapLMSG.goto_point(GXContext._get_tls_geo(), x, y, z, ipj._wrapper)
        



    @classmethod
    def view_area(cls, x0, y0, x1, y1, ipj):
        """
        Sends a view area message
        """
        gxapi_cy.WrapLMSG.view_area(GXContext._get_tls_geo(), x0, y0, x1, y1, ipj._wrapper)
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer