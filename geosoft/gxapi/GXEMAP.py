### extends 'class_empty.py'
from . import gxapi_cy

from geosoft.gxapi import GXContext, int_ref, float_ref, str_ref

### block Header
# NOTICE: The code generator will not replace the code in this block
### endblock Header

### block ClassImplementation
# NOTICE: Do not edit anything here, it is generated code
class GXEMAP:
    """
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._wrapper = None

    def __del__(self):
        self._wrapper = None

    def __init__(self, wrapper=None):
        self._wrapper = wrapper if wrapper else gxapi_cy.WrapEMAP(0)

    @classmethod
    def null(cls) -> 'GXEMAP':
        """
        A null (undefined) instance of :class:`GXEMAP`
        
        :returns: A null :class:`GX3DN`
        """
        return cls()

    def is_null(self) -> bool:
        """
        Check if the instance of :class:`GXEMAP` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of :class:`GXEMAP`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Drag-and-drop methods



    def drop_map_clip_data(self, p2: int) -> None:
        self._wrapper.drop_map_clip_data(p2)
        




    def drag_drop_enabled(self) -> int:
        ret_val = self._wrapper.drag_drop_enabled()
        return ret_val




    def set_drag_drop_enabled(self, p2: int) -> None:
        self._wrapper.set_drag_drop_enabled(p2)
        




# Drawing



    def copy_to_clip(self) -> None:
        self._wrapper.copy_to_clip()
        




    def draw_line(self, p2: float, p3: float, p4: float, p5: float) -> None:
        self._wrapper.draw_line(p2, p3, p4, p5)
        




    def draw_rect(self, p2: float, p3: float, p4: float, p5: float) -> None:
        self._wrapper.draw_rect(p2, p3, p4, p5)
        




    def draw_rect_3d(self, p2: float, p3: float, p4: float, p5: int) -> None:
        self._wrapper.draw_rect_3d(p2, p3, p4, p5)
        




    def get_display_area(self, p2: float_ref, p3: float_ref, p4: float_ref, p5: float_ref) -> None:
        p2.value, p3.value, p4.value, p5.value = self._wrapper.get_display_area(p2.value, p3.value, p4.value, p5.value)
        




    def get_display_area_raw(self, p2: float_ref, p3: float_ref, p4: float_ref, p5: float_ref) -> None:
        p2.value, p3.value, p4.value, p5.value = self._wrapper.get_display_area_raw(p2.value, p3.value, p4.value, p5.value)
        




    def get_map_layout_props(self, p2: int_ref, p3: float_ref, p4: int_ref, p5: int_ref, p6: int_ref, p7: int_ref, p8: int_ref, p9: int_ref) -> None:
        p2.value, p3.value, p4.value, p5.value, p6.value, p7.value, p8.value, p9.value = self._wrapper.get_map_layout_props(p2.value, p3.value, p4.value, p5.value, p6.value, p7.value, p8.value, p9.value)
        




    def get_map_snap(self, p2: float_ref) -> None:
        p2.value = self._wrapper.get_map_snap(p2.value)
        




    def get_window_state(self) -> int:
        ret_val = self._wrapper.get_window_state()
        return ret_val




    def set_display_area(self, p2: float, p3: float, p4: float, p5: float) -> None:
        self._wrapper.set_display_area(p2, p3, p4, p5)
        




    def set_map_layout_props(self, p2: int, p3: float, p4: int, p5: int, p6: int, p7: int, p8: int, p9: int) -> None:
        self._wrapper.set_map_layout_props(p2, p3, p4, p5, p6, p7, p8, p9)
        




    def set_map_snap(self, p2: float) -> None:
        self._wrapper.set_map_snap(p2)
        




    def set_window_state(self, p2: int) -> None:
        self._wrapper.set_window_state(p2)
        




# General



    def packed_files(self) -> int:
        ret_val = self._wrapper.packed_files()
        return ret_val




    def activate_group(self, p2: str) -> None:
        self._wrapper.activate_group(p2.encode())
        




    def activate_view(self, p2: str) -> None:
        self._wrapper.activate_view(p2.encode())
        



    @classmethod
    def current(cls) -> 'GXEMAP':
        ret_val = gxapi_cy.WrapEMAP.current(GXContext._get_tls_geo())
        return GXEMAP(ret_val)



    @classmethod
    def current_no_activate(cls) -> 'GXEMAP':
        ret_val = gxapi_cy.WrapEMAP.current_no_activate(GXContext._get_tls_geo())
        return GXEMAP(ret_val)



    @classmethod
    def current_if_exists(cls) -> 'GXEMAP':
        ret_val = gxapi_cy.WrapEMAP.current_if_exists(GXContext._get_tls_geo())
        return GXEMAP(ret_val)






    def destroy_view(self, p2: int) -> None:
        self._wrapper.destroy_view(p2)
        




    def font_lst(self, p2: 'GXLST', p3: int) -> None:
        self._wrapper.font_lst(p2._wrapper, p3)
        




    def change_current_view(self, p2: str) -> int:
        ret_val = self._wrapper.change_current_view(p2.encode())
        return ret_val




    def create_group_snapshot(self, p2: 'GXLST') -> int:
        ret_val = self._wrapper.create_group_snapshot(p2._wrapper)
        return ret_val




    def get_3d_view_name(self, p2: str_ref) -> None:
        p2.value = self._wrapper.get_3d_view_name(p2.value.encode())
        




    def get_current_group(self, p2: str_ref) -> None:
        p2.value = self._wrapper.get_current_group(p2.value.encode())
        




    def get_current_view(self, p2: str_ref) -> None:
        p2.value = self._wrapper.get_current_view(p2.value.encode())
        



    @classmethod
    def get_maps_lst(cls, p1: 'GXLST', p2: int) -> int:
        ret_val = gxapi_cy.WrapEMAP.get_maps_lst(GXContext._get_tls_geo(), p1._wrapper, p2)
        return ret_val




    def get_name(self, p2: str_ref) -> None:
        p2.value = self._wrapper.get_name(p2.value.encode())
        



    @classmethod
    def have_current(cls) -> int:
        ret_val = gxapi_cy.WrapEMAP.have_current(GXContext._get_tls_geo())
        return ret_val



    @classmethod
    def i_get_specified_map_name(cls, p1: str, p2: str, p3: str_ref) -> int:
        ret_val, p3.value = gxapi_cy.WrapEMAP.i_get_specified_map_name(GXContext._get_tls_geo(), p1.encode(), p2.encode(), p3.value.encode())
        return ret_val




    def is_grid(self) -> int:
        ret_val = self._wrapper.is_grid()
        return ret_val



    @classmethod
    def reload_grid(cls, p1: str) -> None:
        gxapi_cy.WrapEMAP.reload_grid(GXContext._get_tls_geo(), p1.encode())
        




    def is_3d_view(self) -> int:
        ret_val = self._wrapper.is_3d_view()
        return ret_val




    def get_e_3dv(self) -> 'GXE3DV':
        ret_val = self._wrapper.get_e_3dv()
        return GXE3DV(ret_val)




    def is_locked(self) -> int:
        ret_val = self._wrapper.is_locked()
        return ret_val



    @classmethod
    def loaded(cls, p1: str) -> int:
        ret_val = gxapi_cy.WrapEMAP.loaded(GXContext._get_tls_geo(), p1.encode())
        return ret_val




    def read_only(self) -> int:
        ret_val = self._wrapper.read_only()
        return ret_val




    def get_window_position(self, p2: int_ref, p3: int_ref, p4: int_ref, p5: int_ref, p6: int_ref, p7: int_ref) -> None:
        p2.value, p3.value, p4.value, p5.value, p6.value, p7.value = self._wrapper.get_window_position(p2.value, p3.value, p4.value, p5.value, p6.value, p7.value)
        




    def set_window_position(self, p2: int, p3: int, p4: int, p5: int, p6: int, p7: int) -> None:
        self._wrapper.set_window_position(p2, p3, p4, p5, p6, p7)
        




    def doubleize_group_snapshot(self, p2: 'GXLST') -> int:
        ret_val = self._wrapper.doubleize_group_snapshot(p2._wrapper)
        return ret_val




    def set_current_view(self, p2: str) -> int:
        ret_val = self._wrapper.set_current_view(p2.encode())
        return ret_val




    def get_view_ipj(self, p2: str, p3: 'GXIPJ') -> None:
        self._wrapper.get_view_ipj(p2.encode(), p3._wrapper)
        



    @classmethod
    def load(cls, p1: str) -> 'GXEMAP':
        ret_val = gxapi_cy.WrapEMAP.load(GXContext._get_tls_geo(), p1.encode())
        return GXEMAP(ret_val)



    @classmethod
    def load_no_activate(cls, p1: str) -> 'GXEMAP':
        ret_val = gxapi_cy.WrapEMAP.load_no_activate(GXContext._get_tls_geo(), p1.encode())
        return GXEMAP(ret_val)



    @classmethod
    def load_with_view(cls, p1: str, p2: 'GXEMAP') -> 'GXEMAP':
        ret_val = gxapi_cy.WrapEMAP.load_with_view(GXContext._get_tls_geo(), p1.encode(), p2._wrapper)
        return GXEMAP(ret_val)




    def lock(self) -> 'GXMAP':
        ret_val = self._wrapper.lock()
        return GXMAP(ret_val)




    def make_current(self) -> None:
        self._wrapper.make_current()
        




    def print_(self, p2: int, p3: int, p4: int, p5: int, p6: int, p7: int, p8: int, p9: int, p10: float, p11: int, p12: int, p13: int, p14: str) -> None:
        self._wrapper.print_(p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14.encode())
        




    def redraw(self) -> None:
        self._wrapper.redraw()
        




    def select_group(self, p2: str) -> None:
        self._wrapper.select_group(p2.encode())
        




    def set_redraw_flag(self, p2: int) -> None:
        self._wrapper.set_redraw_flag(p2)
        



    @classmethod
    def un_load(cls, p1: str) -> None:
        gxapi_cy.WrapEMAP.un_load(GXContext._get_tls_geo(), p1.encode())
        



    @classmethod
    def un_load_all(cls) -> None:
        gxapi_cy.WrapEMAP.un_load_all(GXContext._get_tls_geo())
        



    @classmethod
    def un_load_verify(cls, p1: str, p2: int) -> None:
        gxapi_cy.WrapEMAP.un_load_verify(GXContext._get_tls_geo(), p1.encode(), p2)
        




    def un_lock(self) -> None:
        self._wrapper.un_lock()
        




# Input



    def get_cur_point(self, p2: float_ref, p3: float_ref) -> None:
        p2.value, p3.value = self._wrapper.get_cur_point(p2.value, p3.value)
        




    def get_cur_point_mm(self, p2: float_ref, p3: float_ref) -> None:
        p2.value, p3.value = self._wrapper.get_cur_point_mm(p2.value, p3.value)
        




    def get_cursor(self, p2: float_ref, p3: float_ref) -> None:
        p2.value, p3.value = self._wrapper.get_cursor(p2.value, p3.value)
        




    def get_cursor_mm(self, p2: float_ref, p3: float_ref) -> None:
        p2.value, p3.value = self._wrapper.get_cursor_mm(p2.value, p3.value)
        




    def digitize(self, p2: 'GXWA', p3: 'GXIMG', p4: int, p5: str, p6: str, p7: str, p8: int) -> int:
        ret_val = self._wrapper.digitize(p2._wrapper, p3._wrapper, p4, p5.encode(), p6.encode(), p7.encode(), p8)
        return ret_val




    def digitize2(self, p2: 'GXVV', p3: 'GXVV', p4: 'GXVV', p5: 'GXIMG', p6: str, p7: int) -> int:
        ret_val = self._wrapper.digitize2(p2._wrapper, p3._wrapper, p4._wrapper, p5._wrapper, p6.encode(), p7)
        return ret_val




    def digitize_peaks(self, p2: 'GXVV', p3: 'GXVV', p4: 'GXVV', p5: 'GXIMG', p6: str, p7: int) -> int:
        ret_val = self._wrapper.digitize_peaks(p2._wrapper, p3._wrapper, p4._wrapper, p5._wrapper, p6.encode(), p7)
        return ret_val




    def digitize_polygon(self, p2: 'GXVV', p3: 'GXVV', p4: 'GXVV', p5: 'GXIMG', p6: str, p7: int, p8: int) -> int:
        ret_val = self._wrapper.digitize_polygon(p2._wrapper, p3._wrapper, p4._wrapper, p5._wrapper, p6.encode(), p7, p8)
        return ret_val




    def get_box(self, p2: str, p3: float_ref, p4: float_ref, p5: float_ref, p6: float_ref) -> int:
        ret_val, p3.value, p4.value, p5.value, p6.value = self._wrapper.get_box(p2.encode(), p3.value, p4.value, p5.value, p6.value)
        return ret_val




    def get_box2(self, p2: str, p3: float_ref, p4: float_ref, p5: float_ref, p6: float_ref, p7: float_ref, p8: float_ref, p9: float_ref, p10: float_ref) -> int:
        ret_val, p3.value, p4.value, p5.value, p6.value, p7.value, p8.value, p9.value, p10.value = self._wrapper.get_box2(p2.encode(), p3.value, p4.value, p5.value, p6.value, p7.value, p8.value, p9.value, p10.value)
        return ret_val




    def get_grid(self, p2: str, p3: int, p4: int, p5: float_ref, p6: float_ref, p7: float_ref, p8: float_ref, p9: float_ref) -> int:
        ret_val, p5.value, p6.value, p7.value, p8.value, p9.value = self._wrapper.get_grid(p2.encode(), p3, p4, p5.value, p6.value, p7.value, p8.value, p9.value)
        return ret_val




    def get_line(self, p2: str, p3: float_ref, p4: float_ref, p5: float_ref, p6: float_ref) -> int:
        ret_val, p3.value, p4.value, p5.value, p6.value = self._wrapper.get_line(p2.encode(), p3.value, p4.value, p5.value, p6.value)
        return ret_val




    def get_line_ex(self, p2: str, p3: float_ref, p4: float_ref, p5: float_ref, p6: float_ref) -> int:
        ret_val, p3.value, p4.value, p5.value, p6.value = self._wrapper.get_line_ex(p2.encode(), p3.value, p4.value, p5.value, p6.value)
        return ret_val




    def get_line_xyz(self, p2: str, p3: float_ref, p4: float_ref, p5: float_ref, p6: float_ref, p7: float_ref, p8: float_ref) -> int:
        ret_val, p3.value, p4.value, p5.value, p6.value, p7.value, p8.value = self._wrapper.get_line_xyz(p2.encode(), p3.value, p4.value, p5.value, p6.value, p7.value, p8.value)
        return ret_val




    def get_point(self, p2: str, p3: float_ref, p4: float_ref) -> int:
        ret_val, p3.value, p4.value = self._wrapper.get_point(p2.encode(), p3.value, p4.value)
        return ret_val




    def get_point_ex(self, p2: str, p3: float_ref, p4: float_ref) -> int:
        ret_val, p3.value, p4.value = self._wrapper.get_point_ex(p2.encode(), p3.value, p4.value)
        return ret_val




    def get_point_3d(self, p2: str, p3: float_ref, p4: float_ref, p5: float_ref) -> int:
        ret_val, p3.value, p4.value, p5.value = self._wrapper.get_point_3d(p2.encode(), p3.value, p4.value, p5.value)
        return ret_val




    def get_poly_line(self, p2: str, p3: 'GXVV', p4: 'GXVV') -> int:
        ret_val = self._wrapper.get_poly_line(p2.encode(), p3._wrapper, p4._wrapper)
        return ret_val




    def get_poly_line_xyz(self, p2: str, p3: 'GXVV', p4: 'GXVV', p5: 'GXVV') -> int:
        ret_val = self._wrapper.get_poly_line_xyz(p2.encode(), p3._wrapper, p4._wrapper, p5._wrapper)
        return ret_val




    def get_rect(self, p2: str, p3: float_ref, p4: float_ref, p5: float_ref, p6: float_ref) -> int:
        ret_val, p3.value, p4.value, p5.value, p6.value = self._wrapper.get_rect(p2.encode(), p3.value, p4.value, p5.value, p6.value)
        return ret_val




    def track_point(self, p2: int, p3: float_ref, p4: float_ref) -> int:
        ret_val, p3.value, p4.value = self._wrapper.track_point(p2, p3.value, p4.value)
        return ret_val




# Map Viewport Mode Methods



    def get_aoi_area(self, p2: float_ref, p3: float_ref, p4: float_ref, p5: float_ref) -> None:
        p2.value, p3.value, p4.value, p5.value = self._wrapper.get_aoi_area(p2.value, p3.value, p4.value, p5.value)
        




    def set_aoi_area(self, p2: float, p3: float, p4: float, p5: float) -> None:
        self._wrapper.set_aoi_area(p2, p3, p4, p5)
        




    def set_viewport_mode(self, p2: int) -> None:
        self._wrapper.set_viewport_mode(p2)
        




# Tracking Methods



    def get_selected_vertices(self, p2: 'GXVV', p3: 'GXVV') -> None:
        self._wrapper.get_selected_vertices(p2._wrapper, p3._wrapper)
        




# Virtual


    @classmethod
    def create_virtual(cls, p1: str) -> 'GXEMAP':
        ret_val = gxapi_cy.WrapEMAP.create_virtual(GXContext._get_tls_geo(), p1.encode())
        return GXEMAP(ret_val)




# External Window


    @classmethod
    def load_control(cls, p1: str, p2: int) -> None:
        gxapi_cy.WrapEMAP.load_control(GXContext._get_tls_geo(), p1.encode(), p2)
        



    @classmethod
    def load_with_view_control(cls, p1: str, p2: 'GXEMAP', p3: int) -> None:
        gxapi_cy.WrapEMAP.load_with_view_control(GXContext._get_tls_geo(), p1.encode(), p2._wrapper, p3)
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer