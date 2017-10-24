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
class GXBIGRID:
    """
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._wrapper = None

    def __del__(self):
        self._wrapper = None

    def __init__(self, wrapper=None):
        self._wrapper = wrapper if wrapper else gxapi_cy.WrapBIGRID(GXContext._get_tls_geo(), 0)

    @classmethod
    def null(cls) -> 'GXBIGRID':
        """
        A null (undefined) instance of :class:`GXBIGRID`
        
        :returns: A null :class:`GX3DN`
        """
        return cls()

    def is_null(self) -> bool:
        """
        Check if the instance of :class:`GXBIGRID` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of :class:`GXBIGRID`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Miscellaneous



    def clear(self) -> None:
        self._wrapper.clear()
        



    @classmethod
    def create(cls) -> 'GXBIGRID':
        ret_val = gxapi_cy.WrapBIGRID.create(GXContext._get_tls_geo())
        return GXBIGRID(ret_val)






    def load_parms(self, p2: str) -> int:
        ret_val = self._wrapper.load_parms(p2.encode())
        return ret_val




    def load_warp(self, p2: str, p3: str, p4: str) -> int:
        ret_val = self._wrapper.load_warp(p2.encode(), p3.encode(), p4.encode())
        return ret_val




    def run(self, p2: str, p3: 'GXDAT', p4: 'GXDAT') -> None:
        self._wrapper.run(p2.encode(), p3._wrapper, p4._wrapper)
        




    def run2(self, p2: str, p3: 'GXDAT', p4: 'GXDAT', p5: 'GXIPJ') -> None:
        self._wrapper.run2(p2.encode(), p3._wrapper, p4._wrapper, p5._wrapper)
        




    def save_parms(self, p2: str) -> None:
        self._wrapper.save_parms(p2.encode())
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer