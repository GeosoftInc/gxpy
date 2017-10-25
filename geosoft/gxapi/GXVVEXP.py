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
class GXVVEXP:
    """
    GXVVEXP class.

    The :class:`geosoft.gxapi.GXVVEXP` class is similar to the :class:`geosoft.gxapi.GXIEXP` class, but is used
    to apply math expressions to :class:`geosoft.gxapi.GXVV` objects.
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._wrapper = None

    def __del__(self):
        self._wrapper = None

    def __init__(self, wrapper=None):
        self._wrapper = wrapper if wrapper else gxapi_cy.WrapVVEXP(GXContext._get_tls_geo(), 0)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of :class:`geosoft.gxapi.GXVVEXP`
        
        :returns: A null :class:`geosoft.gxapi.GXVVEXP`
        """
        return cls()

    def is_null(self):
        """
        Check if the instance of :class:`geosoft.gxapi.GXVVEXP` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of :class:`geosoft.gxapi.GXVVEXP`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Miscellaneous



    def add_vv(self, p2, p3):
        """
        This method adds a :class:`geosoft.gxapi.GXVV` to the :class:`geosoft.gxapi.GXVVEXP` object with a
        variable name.
        """
        self._wrapper.add_vv(p2._wrapper, p3.encode())
        



    @classmethod
    def create(cls):
        """
        This method creates an :class:`geosoft.gxapi.GXVVEXP` object.
        """
        ret_val = gxapi_cy.WrapVVEXP.create(GXContext._get_tls_geo())
        return GXVVEXP(ret_val)






    def do_formula(self, p2, p3):
        """
        This method runs a formula on the grids.
        """
        self._wrapper.do_formula(p2.encode(), p3)
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer