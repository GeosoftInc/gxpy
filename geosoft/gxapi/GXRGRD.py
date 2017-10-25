### extends 'class_empty.py'
### block ClassImports
# NOTICE: Do not edit anything here, it is generated code
from . import gxapi_cy
from geosoft.gxapi import GXContext, float_ref, int_ref, str_ref
from .GXIMG import GXIMG
### endblock ClassImports

### block Header
# NOTICE: The code generator will not replace the code in this block
### endblock Header

### block ClassImplementation
# NOTICE: Do not edit anything here, it is generated code
class GXRGRD:
    """
    GXRGRD class.

    The :class:`GXRGRD` object is used as a storage place for the control
    parameters which the Rangrid (minimum curvature) program needs to execute. The
    Run_RGRD function executes the Rangrid program using the :class:`GXRGRD` object.
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._wrapper = None

    def __del__(self):
        self._wrapper = None

    def __init__(self, wrapper=None):
        self._wrapper = wrapper if wrapper else gxapi_cy.WrapRGRD(GXContext._get_tls_geo(), 0)

    @classmethod
    def null(cls) -> 'GXRGRD':
        """
        A null (undefined) instance of :class:`GXRGRD`
        
        :returns: A null :class:`GXRGRD`
        """
        return cls()

    def is_null(self) -> bool:
        """
        Check if the instance of :class:`GXRGRD` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of :class:`GXRGRD`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Miscellaneous



    def clear(self) -> None:
        self._wrapper.clear()
        



    @classmethod
    def create(cls) -> 'GXRGRD':
        ret_val = gxapi_cy.WrapRGRD.create(GXContext._get_tls_geo())
        return GXRGRD(ret_val)



    @classmethod
    def create_img(cls, p1: 'GXVV', p2: 'GXVV', p3: 'GXVV', p4: 'GXIPJ', p5: str, p6: str) -> 'GXIMG':
        ret_val = gxapi_cy.WrapRGRD.create_img(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3._wrapper, p4._wrapper, p5.encode(), p6.encode())
        return GXIMG(ret_val)






    def default(self, p2: str, p3: 'GXDAT') -> int:
        ret_val = self._wrapper.default(p2.encode(), p3._wrapper)
        return ret_val




    def load_parms(self, p2: str) -> int:
        ret_val = self._wrapper.load_parms(p2.encode())
        return ret_val




    def run(self, p2: 'GXDAT', p3: 'GXDAT') -> int:
        ret_val = self._wrapper.run(p2._wrapper, p3._wrapper)
        return ret_val



    @classmethod
    def run2(cls, p1: 'GXDB', p2: str, p3: str, p4: str, p5: str, p6: str) -> int:
        ret_val = gxapi_cy.WrapRGRD.run2(GXContext._get_tls_geo(), p1._wrapper, p2.encode(), p3.encode(), p4.encode(), p5.encode(), p6.encode())
        return ret_val




    def save_parms(self, p2: str) -> int:
        ret_val = self._wrapper.save_parms(p2.encode())
        return ret_val



    @classmethod
    def run_vv(cls, p1: 'GXVV', p2: 'GXVV', p3: 'GXVV', p4: 'GXIPJ', p5: str, p6: str) -> None:
        gxapi_cy.WrapRGRD.run_vv(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3._wrapper, p4._wrapper, p5.encode(), p6.encode())
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer