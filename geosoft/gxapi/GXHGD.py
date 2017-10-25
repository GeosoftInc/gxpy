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
class GXHGD:
    """
    GXHGD class.

    High Performance Grid. Designed to place grid data
    on a DAP server. It produces a multi-resolution
    compressed object that supports multi-threading and
    allows for high-speed extraction of data at any
    resolution.
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._wrapper = None

    def __del__(self):
        self._wrapper = None

    def __init__(self, wrapper=None):
        self._wrapper = wrapper if wrapper else gxapi_cy.WrapHGD(GXContext._get_tls_geo(), 0)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of `GXHGD`
        
        :returns: A null `GXHGD`
        """
        return cls()

    def is_null(self):
        """
        Check if the instance of `GXHGD` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of `GXHGD`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Miscellaneous


    @classmethod
    def create(cls, p1):
        """
        Create a handle to an `GXHGD` object
        """
        ret_val = gxapi_cy.WrapHGD.create(GXContext._get_tls_geo(), p1.encode())
        return GXHGD(ret_val)






    def export_img(self, p2):
        """
        Export all layers of this `GXHGD` into grid files.
        """
        self._wrapper.export_img(p2.encode())
        




    def get_meta(self, p2):
        """
        Get the metadata of a grid.
        """
        self._wrapper.get_meta(p2._wrapper)
        



    @classmethod
    def h_create_img(cls, p1, p2):
        """
        Make an `GXHGD` from an `GXIMG`
        """
        ret_val = gxapi_cy.WrapHGD.h_create_img(GXContext._get_tls_geo(), p1._wrapper, p2.encode())
        return GXHGD(ret_val)




    def set_meta(self, p2):
        """
        Set the metadata of a grid.
        """
        self._wrapper.set_meta(p2._wrapper)
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer