### extends 'class_empty.py'
from . import gxapi_cy

from geosoft.gxapi import GXContext, int_ref, float_ref, str_ref

### block Header
# NOTICE: The code generator will not replace the code in this block
### endblock Header

### block ClassImplementation
# NOTICE: Do not edit anything here, it is generated code
class GXINTERNET:
    """
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._wrapper = None

    def __del__(self):
        self._wrapper = None

    def __init__(self, wrapper=None):
        self._wrapper = wrapper if wrapper else gxapi_cy.WrapINTERNET(GXContext._get_tls_geo(), 0)

    @classmethod
    def null(cls) -> 'GXINTERNET':
        """
        A null (undefined) instance of :class:`GXINTERNET`
        
        :returns: A null :class:`GX3DN`
        """
        return cls()

    def is_null(self) -> bool:
        """
        Check if the instance of :class:`GXINTERNET` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of :class:`GXINTERNET`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Miscellaneous


    @classmethod
    def download_http(cls, p1: str, p2: str, p3: int) -> int:
        ret_val = gxapi_cy.WrapINTERNET.download_http(GXContext._get_tls_geo(), p1.encode(), p2.encode(), p3)
        return ret_val



    @classmethod
    def send_mail(cls, p1: str, p2: str, p3: str, p4: str, p5: str, p6: str, p7: str, p8: str) -> None:
        gxapi_cy.WrapINTERNET.send_mail(GXContext._get_tls_geo(), p1.encode(), p2.encode(), p3.encode(), p4.encode(), p5.encode(), p6.encode(), p7.encode(), p8.encode())
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer