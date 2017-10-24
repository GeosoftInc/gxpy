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
class GXVECTOR3D:
    """
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._wrapper = None

    def __del__(self):
        self._wrapper = None

    def __init__(self, wrapper=None):
        self._wrapper = wrapper if wrapper else gxapi_cy.WrapVECTOR3D(GXContext._get_tls_geo(), 0)

    @classmethod
    def null(cls) -> 'GXVECTOR3D':
        """
        A null (undefined) instance of :class:`GXVECTOR3D`
        
        :returns: A null :class:`GX3DN`
        """
        return cls()

    def is_null(self) -> bool:
        """
        Check if the instance of :class:`GXVECTOR3D` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of :class:`GXVECTOR3D`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Miscellaneous





    def get_itr(self, p2: 'GXITR') -> None:
        self._wrapper.get_itr(p2._wrapper)
        




    def set_itr(self, p2: 'GXITR') -> None:
        self._wrapper.set_itr(p2._wrapper)
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer