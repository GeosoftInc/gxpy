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
class GXARCSYS:
    """
    GXARCSYS class.

    This library is not a class. It contains various general
    system utilities used by the Geosoft extensions for ArcGIS.
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._wrapper = None

    def __del__(self):
        self._wrapper = None

    def __init__(self, wrapper=None):
        self._wrapper = wrapper if wrapper else gxapi_cy.WrapARCSYS(GXContext._get_tls_geo(), 0)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of `GXARCSYS`
        
        :returns: A null `GXARCSYS`
        """
        return cls()

    def is_null(self):
        """
        Check if the instance of `GXARCSYS` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of `GXARCSYS`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Miscellaneous


    @classmethod
    def get_browse_loc(cls, path):
        """
        Get the current catalog browser location in ArcGIS
        
        :param path:  Path String
        :type  path:  str_ref

        .. versionadded:: 8.0

        **Note:**

        Gets the "local" directory (current catalog browser location in ArcGIS if map has not been saved,
        otherwise MxD path). We cannot mess with the CWD in ArcGIS because there MxD settings for
        relative/absolute paths depends on it.
        """
        path.value = gxapi_cy.WrapARCSYS.get_browse_loc(GXContext._get_tls_geo(), path.value.encode())
        



    @classmethod
    def get_current_doc(cls, path):
        """
        Get the current Mx Document file name
        
        :param path:  Path String
        :type  path:  str_ref

        .. versionadded:: 8.0

        **Note:**

        If the current document is not yet saved, this will return an empty string.
        """
        path.value = gxapi_cy.WrapARCSYS.get_current_doc(GXContext._get_tls_geo(), path.value.encode())
        



    @classmethod
    def set_browse_loc(cls, path):
        """
        Set the current catalog browser location in ArcGIS
        
        :param path:  Path String
        :type  path:  str

        .. versionadded:: 8.0

        **Note:**

        Will also set the current working directory (CWD) if the MxD has not been saved.
        We cannot mess with the CWD in ArcGIS because their MxD settings for relative/absolute paths depends on it.
        """
        gxapi_cy.WrapARCSYS.set_browse_loc(GXContext._get_tls_geo(), path.encode())
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer