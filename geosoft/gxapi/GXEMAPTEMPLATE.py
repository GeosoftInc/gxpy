### extends 'class_empty.py'
### block ClassImports
# NOTICE: Do not edit anything here, it is generated code
from . import gxapi_cy
from geosoft.gxapi import GXContext, float_ref, int_ref, str_ref
from .GXMAPTEMPLATE import GXMAPTEMPLATE
### endblock ClassImports

### block Header
# NOTICE: The code generator will not replace the code in this block
### endblock Header

### block ClassImplementation
# NOTICE: Do not edit anything here, it is generated code
class GXEMAPTEMPLATE:
    """
    GXEMAPTEMPLATE class.

    The :class:`GXEMAPTEMPLATE` class provides access to a map template as displayed within
    Oasis montaj, but does not change data within the template itself.
    It performs functions such as setting the currently displayed area,
    or drawing "tracking" lines or boxes on the template (which are not
    part of the template itself).

    **Note:**

    To obtain access to the map template itself, it is recommended practice
    to begin with an :class:`GXEMAPTEMPLATE` object, and use the Lock function to
    lock the underlying template to prevent external changes. The returned
    :class:`GXMAPTEMPLATE` object may then be safely used to make changes to the template itself.
    
    VIRTUAL :class:`GXEMAPTEMPLATE` SUPPORT
    
    These methods are only available when running in an external application.
    They allow the GX to open a map template and then create a Virtual :class:`GXEMAPTEMPLATE` from that
    map template. The GX can then call MakeCurrent and set the current :class:`GXEMAPTEMPLATE` so
    that code that follows sees this map template as the current :class:`GXMAPTEMPLATE`.
    
    Supported methods on Virtual EMAPTEMPLATEs are:
    
      Current_EMAPTEMPLATE
      CurrentNoActivate_EMAPTEMPLATE
      MakeCurrent_EMAPTEMPLATE
      iHaveCurrent_EMAPTEMPLATE
      CurrentIfExists_EMAPTEMPLATE
    
      Lock_EMAPTEMPLATE
      UnLock_EMAPTEMPLATE
    
      IGetName_EMAPTEMPLATE
    
      iLoaded_EMAPTEMPLATE
      Load_EMAPTEMPLATE
      LoadNoActivate_EMAPTEMPLATE
      UnLoadVerify_EMAPTEMPLATE
      UnLoad_EMAPTEMPLATE
    
      CreateVirtual_EMAPTEMPLATE
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._wrapper = None

    def __del__(self):
        self._wrapper = None

    def __init__(self, wrapper=None):
        self._wrapper = wrapper if wrapper else gxapi_cy.WrapEMAPTEMPLATE(GXContext._get_tls_geo(), 0)

    @classmethod
    def null(cls) -> 'GXEMAPTEMPLATE':
        """
        A null (undefined) instance of :class:`GXEMAPTEMPLATE`
        
        :returns: A null :class:`GXEMAPTEMPLATE`
        """
        return cls()

    def is_null(self) -> bool:
        """
        Check if the instance of :class:`GXEMAPTEMPLATE` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of :class:`GXEMAPTEMPLATE`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Drag-and-drop methods



    def drag_drop_enabled(self) -> int:
        ret_val = self._wrapper.drag_drop_enabled()
        return ret_val




    def set_drag_drop_enabled(self, p2: int) -> None:
        self._wrapper.set_drag_drop_enabled(p2)
        




# General


    @classmethod
    def current(cls) -> 'GXEMAPTEMPLATE':
        ret_val = gxapi_cy.WrapEMAPTEMPLATE.current(GXContext._get_tls_geo())
        return GXEMAPTEMPLATE(ret_val)



    @classmethod
    def current_no_activate(cls) -> 'GXEMAPTEMPLATE':
        ret_val = gxapi_cy.WrapEMAPTEMPLATE.current_no_activate(GXContext._get_tls_geo())
        return GXEMAPTEMPLATE(ret_val)



    @classmethod
    def current_if_exists(cls) -> 'GXEMAPTEMPLATE':
        ret_val = gxapi_cy.WrapEMAPTEMPLATE.current_if_exists(GXContext._get_tls_geo())
        return GXEMAPTEMPLATE(ret_val)





    @classmethod
    def get_map_templates_lst(cls, p1: 'GXLST', p2: int) -> int:
        ret_val = gxapi_cy.WrapEMAPTEMPLATE.get_map_templates_lst(GXContext._get_tls_geo(), p1._wrapper, p2)
        return ret_val




    def get_name(self, p2: str_ref) -> None:
        p2.value = self._wrapper.get_name(p2.value.encode())
        



    @classmethod
    def have_current(cls) -> int:
        ret_val = gxapi_cy.WrapEMAPTEMPLATE.have_current(GXContext._get_tls_geo())
        return ret_val



    @classmethod
    def i_get_specified_map_name(cls, p1: str, p2: str, p3: str_ref) -> int:
        ret_val, p3.value = gxapi_cy.WrapEMAPTEMPLATE.i_get_specified_map_name(GXContext._get_tls_geo(), p1.encode(), p2.encode(), p3.value.encode())
        return ret_val




    def is_locked(self) -> int:
        ret_val = self._wrapper.is_locked()
        return ret_val



    @classmethod
    def loaded(cls, p1: str) -> int:
        ret_val = gxapi_cy.WrapEMAPTEMPLATE.loaded(GXContext._get_tls_geo(), p1.encode())
        return ret_val




    def get_window_position(self, p2: int_ref, p3: int_ref, p4: int_ref, p5: int_ref, p6: int_ref, p7: int_ref) -> None:
        p2.value, p3.value, p4.value, p5.value, p6.value, p7.value = self._wrapper.get_window_position(p2.value, p3.value, p4.value, p5.value, p6.value, p7.value)
        




    def set_window_position(self, p2: int, p3: int, p4: int, p5: int, p6: int, p7: int) -> None:
        self._wrapper.set_window_position(p2, p3, p4, p5, p6, p7)
        




    def read_only(self) -> int:
        ret_val = self._wrapper.read_only()
        return ret_val



    @classmethod
    def load(cls, p1: str) -> 'GXEMAPTEMPLATE':
        ret_val = gxapi_cy.WrapEMAPTEMPLATE.load(GXContext._get_tls_geo(), p1.encode())
        return GXEMAPTEMPLATE(ret_val)



    @classmethod
    def load_no_activate(cls, p1: str) -> 'GXEMAPTEMPLATE':
        ret_val = gxapi_cy.WrapEMAPTEMPLATE.load_no_activate(GXContext._get_tls_geo(), p1.encode())
        return GXEMAPTEMPLATE(ret_val)




    def lock(self) -> 'GXMAPTEMPLATE':
        ret_val = self._wrapper.lock()
        return GXMAPTEMPLATE(ret_val)




    def make_current(self) -> None:
        self._wrapper.make_current()
        



    @classmethod
    def un_load(cls, p1: str) -> None:
        gxapi_cy.WrapEMAPTEMPLATE.un_load(GXContext._get_tls_geo(), p1.encode())
        



    @classmethod
    def un_load_all(cls) -> None:
        gxapi_cy.WrapEMAPTEMPLATE.un_load_all(GXContext._get_tls_geo())
        



    @classmethod
    def un_load_verify(cls, p1: str, p2: int) -> None:
        gxapi_cy.WrapEMAPTEMPLATE.un_load_verify(GXContext._get_tls_geo(), p1.encode(), p2)
        




    def un_lock(self) -> None:
        self._wrapper.un_lock()
        




# Input



    def get_box(self, p2: str, p3: float_ref, p4: float_ref, p5: float_ref, p6: float_ref) -> int:
        ret_val, p3.value, p4.value, p5.value, p6.value = self._wrapper.get_box(p2.encode(), p3.value, p4.value, p5.value, p6.value)
        return ret_val




    def get_line(self, p2: str, p3: float_ref, p4: float_ref, p5: float_ref, p6: float_ref) -> int:
        ret_val, p3.value, p4.value, p5.value, p6.value = self._wrapper.get_line(p2.encode(), p3.value, p4.value, p5.value, p6.value)
        return ret_val




    def get_point(self, p2: str, p3: float_ref, p4: float_ref) -> int:
        ret_val, p3.value, p4.value = self._wrapper.get_point(p2.encode(), p3.value, p4.value)
        return ret_val




    def get_rect(self, p2: str, p3: float_ref, p4: float_ref, p5: float_ref, p6: float_ref) -> int:
        ret_val, p3.value, p4.value, p5.value, p6.value = self._wrapper.get_rect(p2.encode(), p3.value, p4.value, p5.value, p6.value)
        return ret_val




    def track_point(self, p2: int, p3: float_ref, p4: float_ref) -> int:
        ret_val, p3.value, p4.value = self._wrapper.track_point(p2, p3.value, p4.value)
        return ret_val




# Selection Methods



    def get_item_selection(self, p2: str_ref) -> int:
        ret_val, p2.value = self._wrapper.get_item_selection(p2.value.encode())
        return ret_val




    def set_item_selection(self, p2: str) -> None:
        self._wrapper.set_item_selection(p2.encode())
        




# View Window



    def get_display_area(self, p2: float_ref, p3: float_ref, p4: float_ref, p5: float_ref) -> None:
        p2.value, p3.value, p4.value, p5.value = self._wrapper.get_display_area(p2.value, p3.value, p4.value, p5.value)
        




    def get_template_layout_props(self, p2: int_ref, p3: float_ref, p4: int_ref, p5: int_ref, p6: int_ref, p7: int_ref, p8: int_ref, p9: int_ref) -> None:
        p2.value, p3.value, p4.value, p5.value, p6.value, p7.value, p8.value, p9.value = self._wrapper.get_template_layout_props(p2.value, p3.value, p4.value, p5.value, p6.value, p7.value, p8.value, p9.value)
        




    def get_window_state(self) -> int:
        ret_val = self._wrapper.get_window_state()
        return ret_val




    def set_display_area(self, p2: float, p3: float, p4: float, p5: float) -> None:
        self._wrapper.set_display_area(p2, p3, p4, p5)
        




    def set_template_layout_props(self, p2: int, p3: float, p4: int, p5: int, p6: int, p7: int, p8: int, p9: int) -> None:
        self._wrapper.set_template_layout_props(p2, p3, p4, p5, p6, p7, p8, p9)
        




    def set_window_state(self, p2: int) -> None:
        self._wrapper.set_window_state(p2)
        




# Virtual


    @classmethod
    def create_virtual(cls, p1: str) -> 'GXEMAPTEMPLATE':
        ret_val = gxapi_cy.WrapEMAPTEMPLATE.create_virtual(GXContext._get_tls_geo(), p1.encode())
        return GXEMAPTEMPLATE(ret_val)





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer