### extends 'class_empty.py'
from . import gxapi_cy

from geosoft.gxapi import GXContext, int_ref, float_ref, str_ref

### block Header
# NOTICE: The code generator will not replace the code in this block
### endblock Header

### block ClassImplementation
# NOTICE: Do not edit anything here, it is generated code
class GXACQUIRE:
    """
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._wrapper = None

    def __del__(self):
        self._wrapper = None

    def __init__(self, wrapper=None):
        self._wrapper = wrapper if wrapper else gxapi_cy.WrapACQUIRE(0)

    @classmethod
    def null(cls) -> 'GXACQUIRE':
        """
        A null (undefined) instance of :class:`GXACQUIRE`
        
        :returns: A null :class:`GX3DN`
        """
        return cls()

    def is_null(self) -> bool:
        """
        Check if the instance of :class:`GXACQUIRE` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of :class:`GXACQUIRE`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Miscellaneous


    @classmethod
    def create(cls) -> 'GXACQUIRE':
        ret_val = gxapi_cy.WrapACQUIRE.create(GXContext._get_tls_geo())
        return GXACQUIRE(ret_val)




    def delete_empty_chan(self, p2: 'GXDB') -> None:
        self._wrapper.delete_empty_chan(p2._wrapper)
        






    def import_hole(self, p2: str, p3: str, p4: str, p5: 'GXVV', p6: int, p7: int) -> int:
        ret_val = self._wrapper.import_hole(p2.encode(), p3.encode(), p4.encode(), p5._wrapper, p6, p7)
        return ret_val




    def import_point(self, p2: 'GXDB', p3: str, p4: int) -> int:
        ret_val = self._wrapper.import_point(p2._wrapper, p3.encode(), p4)
        return ret_val




    def selection_tool(self, p2: str, p3: int) -> int:
        ret_val = self._wrapper.selection_tool(p2.encode(), p3)
        return ret_val





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer