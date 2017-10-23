### extends 'class_empty.py'
from . import gxapi_cy

from geosoft.gxapi import GXContext, int_ref, float_ref, str_ref

### block Header
# NOTICE: The code generator will not replace the code in this block
### endblock Header

### block ClassImplementation
# NOTICE: Do not edit anything here, it is generated code
class GXST2:
    """
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._wrapper = None

    def __del__(self):
        self._wrapper = None

    def __init__(self, wrapper=None):
        self._wrapper = wrapper if wrapper else gxapi_cy.WrapST2(0)

    @classmethod
    def null(cls) -> 'GXST2':
        """
        A null (undefined) instance of :class:`GXST2`
        
        :returns: A null :class:`GX3DN`
        """
        return cls()

    def is_null(self) -> bool:
        """
        Check if the instance of :class:`GXST2` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of :class:`GXST2`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Miscellaneous


    @classmethod
    def create(cls) -> 'GXST2':
        ret_val = gxapi_cy.WrapST2.create(GXContext._get_tls_geo())
        return GXST2(ret_val)




    def data_vv(self, p2: 'GXVV', p3: 'GXVV') -> None:
        self._wrapper.data_vv(p2._wrapper, p3._wrapper)
        






    def items(self) -> int:
        ret_val = self._wrapper.items()
        return ret_val




    def reset(self) -> None:
        self._wrapper.reset()
        




    def get(self, p2: int) -> float:
        ret_val = self._wrapper.get(p2)
        return ret_val





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer