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
class GXPAT:
    """
    GXPAT class.

    A `GXPAT <geosoft.gxapi.GXPAT>` object is created from a Geosoft format pattern file.
    It contains all the individual patterns listed in the file.
    
    Notes: You may create your own fill patterns. They can be added to the "user.pat"
    file in the <geosoft>\\user\\etc directory. User pattern numbers should be in the 
    range between 20000 and 29999.
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._wrapper = None

    def __del__(self):
        self._wrapper = None

    def __init__(self, wrapper=None):
        self._wrapper = wrapper if wrapper else gxapi_cy.WrapPAT(GXContext._get_tls_geo(), 0)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of `GXPAT`
        
        :returns: A null `GXPAT`
        """
        return cls()

    def is_null(self):
        """
        Check if the instance of `GXPAT` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of `GXPAT`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Miscellaneous


    @classmethod
    def create(cls):
        """
        Creates a pattern object with current default patterns.
        """
        ret_val = gxapi_cy.WrapPAT.create(GXContext._get_tls_geo())
        return GXPAT(ret_val)






    def get_lst(self, cl, lst):
        """
        Copies all pattern names into a `GXLST <geosoft.gxapi.GXLST>` object.

        **Note:**

        Returns a list of the available patterns.
        There will always be at least two items,
        "None" and "Solid Fill"
        """
        self._wrapper.get_lst(cl.encode(), lst._wrapper)
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer