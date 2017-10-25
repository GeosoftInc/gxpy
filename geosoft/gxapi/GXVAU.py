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
class GXVAU:
    """
    GXVAU class.

    This is not a class. These are methods that work on
    data stored in :class:`geosoft.gxapi.GXVA` objects
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._wrapper = None

    def __del__(self):
        self._wrapper = None

    def __init__(self, wrapper=None):
        self._wrapper = wrapper if wrapper else gxapi_cy.WrapVAU(GXContext._get_tls_geo(), 0)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of :class:`geosoft.gxapi.GXVAU`
        
        :returns: A null :class:`geosoft.gxapi.GXVAU`
        """
        return cls()

    def is_null(self):
        """
        Check if the instance of :class:`geosoft.gxapi.GXVAU` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of :class:`geosoft.gxapi.GXVAU`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Miscellaneous


    @classmethod
    def prune(cls, p1, p2, p3):
        """
        Prune values from a :class:`geosoft.gxapi.GXVA` based on reference :class:`geosoft.gxapi.GXVA`

        **Note:**

        Pruning will shorten the :class:`geosoft.gxapi.GXVA` by removing values
        that are either dummy or non-dummy in the reference
        :class:`geosoft.gxapi.GXVA`
        """
        gxapi_cy.WrapVAU.prune(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3)
        



    @classmethod
    def total_vector(cls, p1, p2, p3, p4):
        """
        Calculate total vector for X,Y and Z components
        """
        gxapi_cy.WrapVAU.total_vector(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3._wrapper, p4._wrapper)
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer