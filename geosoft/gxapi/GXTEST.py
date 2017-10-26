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
class GXTEST:
    """
    GXTEST class.

    Used to place special testing methods
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._wrapper = None

    def __del__(self):
        self._wrapper = None

    def __init__(self, wrapper=None):
        self._wrapper = wrapper if wrapper else gxapi_cy.WrapTEST(GXContext._get_tls_geo(), 0)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of `GXTEST`
        
        :returns: A null `GXTEST`
        """
        return cls()

    def is_null(self):
        """
        Check if the instance of `GXTEST` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of `GXTEST`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Miscellaneous


    @classmethod
    def enable_disable_arc_engine_license(cls, enable):
        """
        Forcefully disable ArEngine license availability for testing purposes
        """
        gxapi_cy.WrapTEST.enable_disable_arc_engine_license(GXContext._get_tls_geo(), enable)
        



    @classmethod
    def arc_engine_license(cls):
        """
        Test availability of an ArEngine license on this system
        """
        ret_val = gxapi_cy.WrapTEST.arc_engine_license(GXContext._get_tls_geo())
        return ret_val



    @classmethod
    def test_mode(cls):
        """
        Checks to see if we are running inside testing system
        """
        ret_val = gxapi_cy.WrapTEST.test_mode(GXContext._get_tls_geo())
        return ret_val



    @classmethod
    def wrapper_test(cls, funcs, log):
        """
        Test to make sure all wrappers are valid linking
        """
        gxapi_cy.WrapTEST.wrapper_test(GXContext._get_tls_geo(), funcs.encode(), log.encode())
        



    @classmethod
    def core_class(cls, cl, log):
        """
        Generic Class Test Wrapper
        """
        gxapi_cy.WrapTEST.core_class(GXContext._get_tls_geo(), cl.encode(), log.encode())
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer