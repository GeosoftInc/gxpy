### extends 'class_empty.py'
from . import gxapi_cy

from geosoft.gxapi import GXContext, int_ref, float_ref, str_ref

### block Header
# NOTICE: The code generator will not replace the code in this block
### endblock Header

### block ClassImplementation
# NOTICE: Do not edit anything here, it is generated code
class GXHTTP:
    """
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._wrapper = None

    def __del__(self):
        self._wrapper = None

    def __init__(self, wrapper=None):
        self._wrapper = wrapper if wrapper else gxapi_cy.WrapHTTP(GXContext._get_tls_geo(), 0)

    @classmethod
    def null(cls) -> 'GXHTTP':
        """
        A null (undefined) instance of :class:`GXHTTP`
        
        :returns: A null :class:`GX3DN`
        """
        return cls()

    def is_null(self) -> bool:
        """
        Check if the instance of :class:`GXHTTP` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of :class:`GXHTTP`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Miscellaneous


    @classmethod
    def create(cls, p1: str, p2: str, p3: str, p4: str) -> 'GXHTTP':
        ret_val = gxapi_cy.WrapHTTP.create(GXContext._get_tls_geo(), p1.encode(), p2.encode(), p3.encode(), p4.encode())
        return GXHTTP(ret_val)






    def download(self, p2: str, p3: 'GXBF', p4: int) -> None:
        self._wrapper.download(p2.encode(), p3._wrapper, p4)
        




    def silent_download(self, p2: str, p3: 'GXBF', p4: int) -> None:
        self._wrapper.silent_download(p2.encode(), p3._wrapper, p4)
        




    def get(self, p2: str, p3: str, p4: 'GXBF', p5: 'GXBF') -> None:
        self._wrapper.get(p2.encode(), p3.encode(), p4._wrapper, p5._wrapper)
        




    def post(self, p2: str, p3: str, p4: 'GXBF') -> None:
        self._wrapper.post(p2.encode(), p3.encode(), p4._wrapper)
        




    def set_proxy_credentials(self, p2: str, p3: str) -> None:
        self._wrapper.set_proxy_credentials(p2.encode(), p3.encode())
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer