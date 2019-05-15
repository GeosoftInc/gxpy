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
class GXTEST(gxapi_cy.WrapTEST):
    """
    GXTEST class.

    Used to place special testing methods
    """

    def __init__(self, handle=0):
        super(GXTEST, self).__init__(GXContext._get_tls_geo(), handle)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of `GXTEST <geosoft.gxapi.GXTEST>`
        
        :returns: A null `GXTEST <geosoft.gxapi.GXTEST>`
        :rtype:   GXTEST
        """
        return GXTEST()

    def is_null(self):
        """
        Check if this is a null (undefined) instance
        
        :returns: True if this is a null (undefined) instance, False otherwise.
        :rtype:   bool
        """
        return self._internal_handle() == 0



# Miscellaneous


    @classmethod
    def enable_disable_arc_engine_license(cls, enable):
        """
        Forcefully disable ArEngine license availability for testing purposes
        
        :param enable:  Enable/disable?
        :type  enable:  bool

        .. versionadded:: 6.4.2

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        gxapi_cy.WrapTEST._enable_disable_arc_engine_license(GXContext._get_tls_geo(), enable)
        



    @classmethod
    def arc_engine_license(cls):
        """
        Test availability of an ArEngine license on this system
        

        :returns:    0 - Not available, 1 - Available
        :rtype:      int

        .. versionadded:: 6.4

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = gxapi_cy.WrapTEST._arc_engine_license(GXContext._get_tls_geo())
        return ret_val



    @classmethod
    def test_mode(cls):
        """
        Checks to see if we are running inside testing system
        
        :rtype:      bool

        .. versionadded:: 6.4.2

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = gxapi_cy.WrapTEST._test_mode(GXContext._get_tls_geo())
        return ret_val



    @classmethod
    def wrapper_test(cls, funcs, log):
        """
        Test to make sure all wrappers are valid linking
        
        :param funcs:  List of functions to test
        :param log:    Output log file
        :type  funcs:  str
        :type  log:    str

        .. versionadded:: 6.1

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        gxapi_cy.WrapTEST._wrapper_test(GXContext._get_tls_geo(), funcs.encode(), log.encode())
        



    @classmethod
    def core_class(cls, cl, log):
        """
        Generic Class Test Wrapper
        
        :param cl:   Name of class to test
        :param log:  Output log file
        :type  cl:   str
        :type  log:  str

        .. versionadded:: 9.2

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        gxapi_cy.WrapTEST._core_class(GXContext._get_tls_geo(), cl.encode(), log.encode())
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer