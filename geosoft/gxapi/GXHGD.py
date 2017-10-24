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
class GXHGD:
    """
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
    def null(cls) -> 'GXHGD':
        """
        A null (undefined) instance of :class:`GXHGD`
        
        :returns: A null :class:`GX3DN`
        """
        return cls()

    def is_null(self) -> bool:
        """
        Check if the instance of :class:`GXHGD` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of :class:`GXHGD`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Miscellaneous


    @classmethod
    def create(cls, p1: str) -> 'GXHGD':
        ret_val = gxapi_cy.WrapHGD.create(GXContext._get_tls_geo(), p1.encode())
        return GXHGD(ret_val)






    def export_img(self, p2: str) -> None:
        self._wrapper.export_img(p2.encode())
        




    def get_meta(self, p2: 'GXMETA') -> None:
        self._wrapper.get_meta(p2._wrapper)
        



    @classmethod
    def h_create_img(cls, p1: 'GXIMG', p2: str) -> 'GXHGD':
        ret_val = gxapi_cy.WrapHGD.h_create_img(GXContext._get_tls_geo(), p1._wrapper, p2.encode())
        return GXHGD(ret_val)




    def set_meta(self, p2: 'GXMETA') -> None:
        self._wrapper.set_meta(p2._wrapper)
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer