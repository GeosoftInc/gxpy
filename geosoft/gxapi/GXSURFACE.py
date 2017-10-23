### extends 'class_empty.py'
from . import gxapi_cy

from geosoft.gxapi import GXContext, int_ref, float_ref, str_ref

### block Header
# NOTICE: The code generator will not replace the code in this block
### endblock Header

### block ClassImplementation
# NOTICE: Do not edit anything here, it is generated code
class GXSURFACE:
    """
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._wrapper = None

    def __del__(self):
        self._wrapper = None

    def __init__(self, wrapper=None):
        self._wrapper = wrapper if wrapper else gxapi_cy.WrapSURFACE(0)

    @classmethod
    def null(cls) -> 'GXSURFACE':
        """
        A null (undefined) instance of :class:`GXSURFACE`
        
        :returns: A null :class:`GX3DN`
        """
        return cls()

    def is_null(self) -> bool:
        """
        Check if the instance of :class:`GXSURFACE` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of :class:`GXSURFACE`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Miscellaneous


    @classmethod
    def create(cls, p1: str, p2: 'GXIPJ') -> 'GXSURFACE':
        ret_val = gxapi_cy.WrapSURFACE.create(GXContext._get_tls_geo(), p1.encode(), p2._wrapper)
        return GXSURFACE(ret_val)



    @classmethod
    def open(cls, p1: str, p2: int) -> 'GXSURFACE':
        ret_val = gxapi_cy.WrapSURFACE.open(GXContext._get_tls_geo(), p1.encode(), p2)
        return GXSURFACE(ret_val)






    def get_ipj(self, p2: 'GXIPJ') -> None:
        self._wrapper.get_ipj(p2._wrapper)
        




    def set_ipj(self, p2: 'GXIPJ') -> None:
        self._wrapper.set_ipj(p2._wrapper)
        




    def get_surface_items(self, p2: 'GXLST') -> None:
        self._wrapper.get_surface_items(p2._wrapper)
        




    def get_surface_item(self, p2: str) -> 'GXSURFACEITEM':
        ret_val = self._wrapper.get_surface_item(p2.encode())
        return GXSURFACEITEM(ret_val)




    def add_surface_item(self, p2: 'GXSURFACEITEM') -> None:
        self._wrapper.add_surface_item(p2._wrapper)
        



    @classmethod
    def get_surface_names(cls, p1: str, p2: 'GXLST') -> None:
        gxapi_cy.WrapSURFACE.get_surface_names(GXContext._get_tls_geo(), p1.encode(), p2._wrapper)
        



    @classmethod
    def get_closed_surface_names(cls, p1: str, p2: 'GXLST') -> None:
        gxapi_cy.WrapSURFACE.get_closed_surface_names(GXContext._get_tls_geo(), p1.encode(), p2._wrapper)
        




    def get_extents(self, p2: float_ref, p3: float_ref, p4: float_ref, p5: float_ref, p6: float_ref, p7: float_ref) -> None:
        p2.value, p3.value, p4.value, p5.value, p6.value, p7.value = self._wrapper.get_extents(p2.value, p3.value, p4.value, p5.value, p6.value, p7.value)
        



    @classmethod
    def crc(cls, p1: str, p2: str, p3: int_ref) -> int:
        ret_val, p3.value = gxapi_cy.WrapSURFACE.crc(GXContext._get_tls_geo(), p1.encode(), p2.encode(), p3.value)
        return ret_val



    @classmethod
    def sync(cls, p1: str) -> None:
        gxapi_cy.WrapSURFACE.sync(GXContext._get_tls_geo(), p1.encode())
        



    @classmethod
    def create_from_dxf(cls, p1: 'GXIPJ', p2: str, p3: str) -> None:
        gxapi_cy.WrapSURFACE.create_from_dxf(GXContext._get_tls_geo(), p1._wrapper, p2.encode(), p3.encode())
        



    @classmethod
    def create_from_vulcan_triangulation(cls, p1: str, p2: 'GXIPJ', p3: str) -> None:
        gxapi_cy.WrapSURFACE.create_from_vulcan_triangulation(GXContext._get_tls_geo(), p1.encode(), p2._wrapper, p3.encode())
        



    @classmethod
    def append_vulcan_triangulation(cls, p1: str, p2: 'GXIPJ', p3: str) -> None:
        gxapi_cy.WrapSURFACE.append_vulcan_triangulation(GXContext._get_tls_geo(), p1.encode(), p2._wrapper, p3.encode())
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer