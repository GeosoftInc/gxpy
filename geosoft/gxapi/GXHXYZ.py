### extends 'class_empty.py'
from . import gxapi_cy

from geosoft.gxapi import GXContext, int_ref, float_ref, str_ref

### block Header
# NOTICE: The code generator will not replace the code in this block
### endblock Header

### block ClassImplementation
# NOTICE: Do not edit anything here, it is generated code
class GXHXYZ:
    """
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._wrapper = None

    def __del__(self):
        self._wrapper = None

    def __init__(self, wrapper=None):
        self._wrapper = wrapper if wrapper else gxapi_cy.WrapHXYZ(0)

    @classmethod
    def null(cls) -> 'GXHXYZ':
        """
        A null (undefined) instance of :class:`GXHXYZ`
        
        :returns: A null :class:`GX3DN`
        """
        return cls()

    def is_null(self) -> bool:
        """
        Check if the instance of :class:`GXHXYZ` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of :class:`GXHXYZ`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Miscellaneous


    @classmethod
    def create(cls, p1: str) -> 'GXHXYZ':
        ret_val = gxapi_cy.WrapHXYZ.create(GXContext._get_tls_geo())
        return GXHXYZ(ret_val)






    def get_meta(self, p2: 'GXMETA') -> None:
        self._wrapper.get_meta(p2)
        



    @classmethod
    def h_create_db(cls, p1: 'GXDB', p2: 'GXVV', p3: str) -> 'GXHXYZ':
        ret_val = gxapi_cy.WrapHXYZ.h_create_db(GXContext._get_tls_geo(), p2, p3.encode())
        return GXHXYZ(ret_val)



    @classmethod
    def h_create_sql(cls, p1: str, p2: str, p3: str, p4: str, p5: 'GXIPJ', p6: str) -> 'GXHXYZ':
        ret_val = gxapi_cy.WrapHXYZ.h_create_sql(GXContext._get_tls_geo(), p2.encode(), p3.encode(), p4.encode(), p5, p6.encode())
        return GXHXYZ(ret_val)




    def set_meta(self, p2: 'GXMETA') -> None:
        self._wrapper.set_meta(p2)
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer