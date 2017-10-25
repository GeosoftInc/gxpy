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
class GXKGRD:
    """
    GXKGRD class.

    The :class:`GXKGRD` object is used as a storage place for the control
    parameters that the Krigrid program needs to execute. The
    Run_KGRD function executes the Krigrid program using the
    :class:`GXKGRD` object.
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._wrapper = None

    def __del__(self):
        self._wrapper = None

    def __init__(self, wrapper=None):
        self._wrapper = wrapper if wrapper else gxapi_cy.WrapKGRD(GXContext._get_tls_geo(), 0)

    @classmethod
    def null(cls) -> 'GXKGRD':
        """
        A null (undefined) instance of :class:`GXKGRD`
        
        :returns: A null :class:`GXKGRD`
        """
        return cls()

    def is_null(self) -> bool:
        """
        Check if the instance of :class:`GXKGRD` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of :class:`GXKGRD`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Miscellaneous



    def clear(self) -> None:
        self._wrapper.clear()
        



    @classmethod
    def create(cls) -> 'GXKGRD':
        ret_val = gxapi_cy.WrapKGRD.create(GXContext._get_tls_geo())
        return GXKGRD(ret_val)






    def load_parms(self, p2: str) -> int:
        ret_val = self._wrapper.load_parms(p2.encode())
        return ret_val




    def run(self, p2: str, p3: 'GXDAT', p4: 'GXDAT', p5: 'GXDAT', p6: str, p7: str, p8: int, p9: int, p10: int) -> int:
        ret_val = self._wrapper.run(p2.encode(), p3._wrapper, p4._wrapper, p5._wrapper, p6.encode(), p7.encode(), p8, p9, p10)
        return ret_val



    @classmethod
    def run2(cls, p1: 'GXDB', p2: str, p3: str, p4: str, p5: str, p6: str, p7: str, p8: str, p9: str, p10: int) -> int:
        ret_val = gxapi_cy.WrapKGRD.run2(GXContext._get_tls_geo(), p1._wrapper, p2.encode(), p3.encode(), p4.encode(), p5.encode(), p6.encode(), p7.encode(), p8.encode(), p9.encode(), p10)
        return ret_val



    @classmethod
    def run3(cls, p1: 'GXDB', p2: str, p3: str, p4: str, p5: str, p6: str, p7: str, p8: str, p9: str, p10: str, p11: int) -> int:
        ret_val = gxapi_cy.WrapKGRD.run3(GXContext._get_tls_geo(), p1._wrapper, p2.encode(), p3.encode(), p4.encode(), p5.encode(), p6.encode(), p7.encode(), p8.encode(), p9.encode(), p10.encode(), p11)
        return ret_val




    def save_parms(self, p2: str) -> int:
        ret_val = self._wrapper.save_parms(p2.encode())
        return ret_val





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer