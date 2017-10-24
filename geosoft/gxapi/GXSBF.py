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
class GXSBF:
    """
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._wrapper = None

    def __del__(self):
        self._wrapper = None

    def __init__(self, wrapper=None):
        self._wrapper = wrapper if wrapper else gxapi_cy.WrapSBF(GXContext._get_tls_geo(), 0)

    @classmethod
    def null(cls) -> 'GXSBF':
        """
        A null (undefined) instance of :class:`GXSBF`
        
        :returns: A null :class:`GX3DN`
        """
        return cls()

    def is_null(self) -> bool:
        """
        Check if the instance of :class:`GXSBF` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of :class:`GXSBF`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Miscellaneous



    def create(self, p2: str, p3: int) -> 'GXSBF':
        ret_val = self._wrapper.create(p2.encode(), p3)
        return GXSBF(ret_val)




    def create_obj_list(self, p2: 'GXLST', p3: int) -> None:
        self._wrapper.create_obj_list(p2._wrapper, p3)
        




    def del_dir(self, p2: str) -> None:
        self._wrapper.del_dir(p2.encode())
        




    def del_file(self, p2: str) -> None:
        self._wrapper.del_file(p2.encode())
        





    @classmethod
    def h_get_db(cls, p1: 'GXDB') -> 'GXSBF':
        ret_val = gxapi_cy.WrapSBF.h_get_db(GXContext._get_tls_geo(), p1._wrapper)
        return GXSBF(ret_val)



    @classmethod
    def h_get_map(cls, p1: 'GXMAP') -> 'GXSBF':
        ret_val = gxapi_cy.WrapSBF.h_get_map(GXContext._get_tls_geo(), p1._wrapper)
        return GXSBF(ret_val)



    @classmethod
    def h_get_sys(cls) -> 'GXSBF':
        ret_val = gxapi_cy.WrapSBF.h_get_sys(GXContext._get_tls_geo())
        return GXSBF(ret_val)




    def exist_dir(self, p2: str) -> int:
        ret_val = self._wrapper.exist_dir(p2.encode())
        return ret_val




    def exist_file(self, p2: str) -> int:
        ret_val = self._wrapper.exist_file(p2.encode())
        return ret_val




    def save_log(self, p2: str, p3: str, p4: str, p5: int) -> None:
        self._wrapper.save_log(p2.encode(), p3.encode(), p4.encode(), p5)
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer