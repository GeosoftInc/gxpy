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
class GXPRAGA3:
    """
    GXPRAGA3 class.

    :class:`GXPRAGA3` application methods

    **Note:**

    No notes
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._wrapper = None

    def __del__(self):
        self._wrapper = None

    def __init__(self, wrapper=None):
        self._wrapper = wrapper if wrapper else gxapi_cy.WrapPRAGA3(GXContext._get_tls_geo(), 0)

    @classmethod
    def null(cls) -> 'GXPRAGA3':
        """
        A null (undefined) instance of :class:`GXPRAGA3`
        
        :returns: A null :class:`GXPRAGA3`
        """
        return cls()

    def is_null(self) -> bool:
        """
        Check if the instance of :class:`GXPRAGA3` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of :class:`GXPRAGA3`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Miscellaneous


    @classmethod
    def launch(cls) -> int:
        ret_val = gxapi_cy.WrapPRAGA3.launch(GXContext._get_tls_geo())
        return ret_val





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer