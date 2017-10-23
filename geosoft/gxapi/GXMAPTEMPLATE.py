### extends 'class_empty.py'
from . import gxapi_cy

from geosoft.gxapi import GXContext, int_ref, float_ref, str_ref

### block Header
# NOTICE: The code generator will not replace the code in this block
### endblock Header

### block ClassImplementation
# NOTICE: Do not edit anything here, it is generated code
class GXMAPTEMPLATE:
    """
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._wrapper = None

    def __del__(self):
        self._wrapper = None

    def __init__(self, wrapper=None):
        self._wrapper = wrapper if wrapper else gxapi_cy.WrapMAPTEMPLATE(0)

    @classmethod
    def null(cls) -> 'GXMAPTEMPLATE':
        """
        A null (undefined) instance of :class:`GXMAPTEMPLATE`
        
        :returns: A null :class:`GX3DN`
        """
        return cls()

    def is_null(self) -> bool:
        """
        Check if the instance of :class:`GXMAPTEMPLATE` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of :class:`GXMAPTEMPLATE`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Content Manipulation Methods



    def get_tmp_copy(self, p2: str_ref) -> None:
        p2.value = self._wrapper.get_tmp_copy(p2.value.encode())
        




    def update_from_tmp_copy(self, p2: str) -> None:
        self._wrapper.update_from_tmp_copy(p2.encode())
        




# File Methods



    def commit(self) -> None:
        self._wrapper.commit()
        



    @classmethod
    def create(cls, p1: str, p2: str, p3: int) -> 'GXMAPTEMPLATE':
        ret_val = gxapi_cy.WrapMAPTEMPLATE.create(GXContext._get_tls_geo(), p2.encode(), p3)
        return GXMAPTEMPLATE(ret_val)






    def discard(self) -> None:
        self._wrapper.discard()
        




    def get_file_name(self, p2: str_ref) -> None:
        p2.value = self._wrapper.get_file_name(p2.value.encode())
        




# Map Making



    def create_map(self, p2: str, p3: str) -> None:
        self._wrapper.create_map(p2.encode(), p3.encode())
        




# Render/Preview



    def refresh(self) -> None:
        self._wrapper.refresh()
        




    def render_preview(self, p2: int, p3: int, p4: int, p5: int, p6: int) -> None:
        self._wrapper.render_preview(p2, p3, p4, p5, p6)
        




    def render_preview_map_production(self, p2: int, p3: int_ref, p4: int_ref, p5: int_ref, p6: int_ref) -> None:
        p3.value, p4.value, p5.value, p6.value = self._wrapper.render_preview_map_production(p2, p3.value, p4.value, p5.value, p6.value)
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer