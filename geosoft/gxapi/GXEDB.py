### extends 'class_empty.py'
from . import gxapi_cy

from geosoft.gxapi import GXContext, int_ref, float_ref, str_ref

### block Header
# NOTICE: The code generator will not replace the code in this block
### endblock Header

### block ClassImplementation
# NOTICE: Do not edit anything here, it is generated code
class GXEDB:
    """
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._wrapper = None

    def __del__(self):
        self._wrapper = None

    def __init__(self, wrapper=None):
        self._wrapper = wrapper if wrapper else gxapi_cy.WrapEDB(0)

    @classmethod
    def null(cls) -> 'GXEDB':
        """
        A null (undefined) instance of :class:`GXEDB`
        
        :returns: A null :class:`GX3DN`
        """
        return cls()

    def is_null(self) -> bool:
        """
        Check if the instance of :class:`GXEDB` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of :class:`GXEDB`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Miscellaneous



    def apply_formula_internal(self, p2: str) -> None:
        self._wrapper.apply_formula_internal(p2.encode())
        



    @classmethod
    def current(cls) -> 'GXEDB':
        ret_val = gxapi_cy.WrapEDB.current(GXContext._get_tls_geo())
        return GXEDB(ret_val)



    @classmethod
    def current_no_activate(cls) -> 'GXEDB':
        ret_val = gxapi_cy.WrapEDB.current_no_activate(GXContext._get_tls_geo())
        return GXEDB(ret_val)



    @classmethod
    def current_if_exists(cls) -> 'GXEDB':
        ret_val = gxapi_cy.WrapEDB.current_if_exists(GXContext._get_tls_geo())
        return GXEDB(ret_val)




    def del_line0(self) -> None:
        self._wrapper.del_line0()
        






    def destroy_view(self, p2: int) -> None:
        self._wrapper.destroy_view(p2)
        




    def get_cur_chan_symb(self) -> int:
        ret_val = self._wrapper.get_cur_chan_symb()
        return ret_val




    def get_cur_line_symb(self) -> int:
        ret_val = self._wrapper.get_cur_line_symb()
        return ret_val




    def get_displ_fid_range(self, p2: int_ref, p3: int_ref) -> None:
        p2.value, p3.value = self._wrapper.get_displ_fid_range(p2.value, p3.value)
        




    def get_cur_point(self, p2: float_ref, p3: float_ref, p4: float_ref) -> None:
        p2.value, p3.value, p4.value = self._wrapper.get_cur_point(p2.value, p3.value, p4.value)
        




    def get_fid_range(self, p2: float_ref, p3: float_ref, p4: int_ref) -> None:
        p2.value, p3.value, p4.value = self._wrapper.get_fid_range(p2.value, p3.value, p4.value)
        




    def get_next_line_symb(self) -> int:
        ret_val = self._wrapper.get_next_line_symb()
        return ret_val




    def get_prev_line_symb(self) -> int:
        ret_val = self._wrapper.get_prev_line_symb()
        return ret_val




    def get_profile_range_x(self, p2: float_ref, p3: float_ref, p4: int_ref) -> None:
        p2.value, p3.value, p4.value = self._wrapper.get_profile_range_x(p2.value, p3.value, p4.value)
        




    def get_profile_range_y(self, p2: int, p3: int, p4: float_ref, p5: float_ref, p6: int_ref) -> None:
        p4.value, p5.value, p6.value = self._wrapper.get_profile_range_y(p2, p3, p4.value, p5.value, p6.value)
        




    def get_profile_split(self, p2: float_ref, p3: float_ref) -> None:
        p2.value, p3.value = self._wrapper.get_profile_split(p2.value, p3.value)
        




    def get_profile_split5(self, p2: float_ref, p3: float_ref, p4: float_ref, p5: float_ref) -> None:
        p2.value, p3.value, p4.value, p5.value = self._wrapper.get_profile_split5(p2.value, p3.value, p4.value, p5.value)
        




    def get_profile_split_vv(self, p2: 'GXVV') -> None:
        self._wrapper.get_profile_split_vv(p2._wrapper)
        




    def get_profile_vertical_grid_lines(self, p2: int_ref, p3: float_ref) -> None:
        p2.value, p3.value = self._wrapper.get_profile_vertical_grid_lines(p2.value, p3.value)
        




    def get_profile_window(self, p2: int, p3: int_ref, p4: int_ref) -> None:
        p3.value, p4.value = self._wrapper.get_profile_window(p2, p3.value, p4.value)
        




    def goto_column(self, p2: int) -> None:
        self._wrapper.goto_column(p2)
        




    def goto_elem(self, p2: int) -> None:
        self._wrapper.goto_elem(p2)
        




    def goto_line(self, p2: int) -> None:
        self._wrapper.goto_line(p2)
        




    def histogram(self, p2: 'GXST', p3: float, p4: float, p5: int) -> None:
        self._wrapper.histogram(p2._wrapper, p3, p4, p5)
        




    def all_chan_list(self, p2: 'GXVV') -> int:
        ret_val = self._wrapper.all_chan_list(p2._wrapper)
        return ret_val




    def channels(self) -> int:
        ret_val = self._wrapper.channels()
        return ret_val




    def disp_chan_list(self, p2: 'GXVV') -> int:
        ret_val = self._wrapper.disp_chan_list(p2._wrapper)
        return ret_val




    def disp_chan_lst(self, p2: 'GXLST') -> int:
        ret_val = self._wrapper.disp_chan_lst(p2._wrapper)
        return ret_val




    def disp_class_chan_lst(self, p2: 'GXLST', p3: str) -> int:
        ret_val = self._wrapper.disp_class_chan_lst(p2._wrapper, p3.encode())
        return ret_val




    def find_channel_column(self, p2: str) -> int:
        ret_val = self._wrapper.find_channel_column(p2.encode())
        return ret_val




    def find_nearest(self, p2: float_ref, p3: float_ref, p4: float_ref, p5: 'GXIPJ') -> int:
        ret_val, p2.value, p3.value, p4.value = self._wrapper.find_nearest(p2.value, p3.value, p4.value, p5._wrapper)
        return ret_val




    def get_cur_chan(self, p2: str_ref) -> None:
        p2.value = self._wrapper.get_cur_chan(p2.value.encode())
        




    def get_cur_fid_string(self, p2: str_ref) -> None:
        p2.value = self._wrapper.get_cur_fid_string(p2.value.encode())
        




    def get_cur_line(self, p2: str_ref) -> None:
        p2.value = self._wrapper.get_cur_line(p2.value.encode())
        




    def get_cur_mark(self, p2: float_ref, p3: float_ref, p4: float_ref) -> int:
        ret_val, p2.value, p3.value, p4.value = self._wrapper.get_cur_mark(p2.value, p3.value, p4.value)
        return ret_val




    def get_current_selection(self, p2: str_ref, p4: str_ref, p6: str_ref, p8: str_ref) -> None:
        p2.value, p4.value, p6.value, p8.value = self._wrapper.get_current_selection(p2.value.encode(), p4.value.encode(), p6.value.encode(), p8.value.encode())
        



    @classmethod
    def get_databases_lst(cls, p1: 'GXLST', p2: int) -> int:
        ret_val = gxapi_cy.WrapEDB.get_databases_lst(GXContext._get_tls_geo(), p1._wrapper, p2)
        return ret_val




    def get_mark_chan_vv(self, p2: 'GXVV', p3: int) -> int:
        ret_val = self._wrapper.get_mark_chan_vv(p2._wrapper, p3)
        return ret_val




    def get_mark_chan_va(self, p2: 'GXVA', p3: int) -> int:
        ret_val = self._wrapper.get_mark_chan_va(p2._wrapper, p3)
        return ret_val




    def get_name(self, p2: str_ref) -> None:
        p2.value = self._wrapper.get_name(p2.value.encode())
        




    def get_profile_parm(self, p2: int, p3: int, p4: int) -> int:
        ret_val = self._wrapper.get_profile_parm(p2, p3, p4)
        return ret_val




    def get_window_state(self) -> int:
        ret_val = self._wrapper.get_window_state()
        return ret_val



    @classmethod
    def have_current(cls) -> int:
        ret_val = gxapi_cy.WrapEDB.have_current(GXContext._get_tls_geo())
        return ret_val




    def is_locked(self) -> int:
        ret_val = self._wrapper.is_locked()
        return ret_val



    @classmethod
    def loaded(cls, p1: str) -> int:
        ret_val = gxapi_cy.WrapEDB.loaded(GXContext._get_tls_geo(), p1.encode())
        return ret_val




    def profile_open(self, p2: int) -> int:
        ret_val = self._wrapper.profile_open(p2)
        return ret_val




    def read_only(self) -> int:
        ret_val = self._wrapper.read_only()
        return ret_val




    def get_window_position(self, p2: int_ref, p3: int_ref, p4: int_ref, p5: int_ref, p6: int_ref, p7: int_ref) -> None:
        p2.value, p3.value, p4.value, p5.value, p6.value, p7.value = self._wrapper.get_window_position(p2.value, p3.value, p4.value, p5.value, p6.value, p7.value)
        




    def set_window_position(self, p2: int, p3: int, p4: int, p5: int, p6: int, p7: int) -> None:
        self._wrapper.set_window_position(p2, p3, p4, p5, p6, p7)
        




    def show_profile_name(self, p2: int, p3: str) -> int:
        ret_val = self._wrapper.show_profile_name(p2, p3.encode())
        return ret_val




    def get_window_y_axis_direction(self, p2: int) -> int:
        ret_val = self._wrapper.get_window_y_axis_direction(p2)
        return ret_val




    def window_profiles(self, p2: int) -> int:
        ret_val = self._wrapper.window_profiles(p2)
        return ret_val




    def launch_histogram(self, p2: str) -> None:
        self._wrapper.launch_histogram(p2.encode())
        




    def launch_scatter(self) -> None:
        self._wrapper.launch_scatter()
        



    @classmethod
    def load(cls, p1: str) -> 'GXEDB':
        ret_val = gxapi_cy.WrapEDB.load(GXContext._get_tls_geo(), p1.encode())
        return GXEDB(ret_val)



    @classmethod
    def load_no_activate(cls, p1: str) -> 'GXEDB':
        ret_val = gxapi_cy.WrapEDB.load_no_activate(GXContext._get_tls_geo(), p1.encode())
        return GXEDB(ret_val)




    def load_all_chans(self) -> None:
        self._wrapper.load_all_chans()
        




    def load_chan(self, p2: str) -> None:
        self._wrapper.load_chan(p2.encode())
        



    @classmethod
    def load_new(cls, p1: str) -> 'GXEDB':
        ret_val = gxapi_cy.WrapEDB.load_new(GXContext._get_tls_geo(), p1.encode())
        return GXEDB(ret_val)



    @classmethod
    def load_pass(cls, p1: str, p2: str, p3: str) -> 'GXEDB':
        ret_val = gxapi_cy.WrapEDB.load_pass(GXContext._get_tls_geo(), p1.encode(), p2.encode(), p3.encode())
        return GXEDB(ret_val)



    @classmethod
    def load_with_view(cls, p1: str, p2: 'GXEDB') -> 'GXEDB':
        ret_val = gxapi_cy.WrapEDB.load_with_view(GXContext._get_tls_geo(), p1.encode(), p2._wrapper)
        return GXEDB(ret_val)




    def lock(self) -> 'GXDB':
        ret_val = self._wrapper.lock()
        return GXDB(ret_val)




    def make_current(self) -> None:
        self._wrapper.make_current()
        




    def remove_profile(self, p2: int, p3: int) -> None:
        self._wrapper.remove_profile(p2, p3)
        




    def get_cur_fid(self) -> float:
        ret_val = self._wrapper.get_cur_fid()
        return ret_val




    def get_profile_parm(self, p2: int, p3: int, p4: int) -> float:
        ret_val = self._wrapper.get_profile_parm(p2, p3, p4)
        return ret_val




    def get_split(self) -> float:
        ret_val = self._wrapper.get_split()
        return ret_val




    def run_channel_maker(self, p2: str) -> None:
        self._wrapper.run_channel_maker(p2.encode())
        




    def run_channel_makers(self) -> None:
        self._wrapper.run_channel_makers()
        




    def set_cur_line(self, p2: str) -> None:
        self._wrapper.set_cur_line(p2.encode())
        




    def set_cur_line_no_message(self, p2: str) -> None:
        self._wrapper.set_cur_line_no_message(p2.encode())
        




    def set_cur_mark(self, p2: float, p3: float) -> None:
        self._wrapper.set_cur_mark(p2, p3)
        




    def set_profile_parm_i(self, p2: int, p3: int, p4: int, p5: int) -> None:
        self._wrapper.set_profile_parm_i(p2, p3, p4, p5)
        




    def set_profile_parm_r(self, p2: int, p3: int, p4: int, p5: float) -> None:
        self._wrapper.set_profile_parm_r(p2, p3, p4, p5)
        




    def set_profile_range_x(self, p2: float, p3: float, p4: int) -> None:
        self._wrapper.set_profile_range_x(p2, p3, p4)
        




    def set_profile_range_y(self, p2: int, p3: int, p4: float, p5: float, p6: int) -> None:
        self._wrapper.set_profile_range_y(p2, p3, p4, p5, p6)
        




    def set_profile_split(self, p2: float, p3: float) -> None:
        self._wrapper.set_profile_split(p2, p3)
        




    def set_profile_split5(self, p2: float, p3: float, p4: float, p5: float) -> None:
        self._wrapper.set_profile_split5(p2, p3, p4, p5)
        




    def set_profile_split_vv(self, p2: 'GXVV') -> None:
        self._wrapper.set_profile_split_vv(p2._wrapper)
        




    def set_split(self, p2: float) -> None:
        self._wrapper.set_split(p2)
        




    def set_window_state(self, p2: int) -> None:
        self._wrapper.set_window_state(p2)
        




    def show_profile(self, p2: int, p3: int) -> None:
        self._wrapper.show_profile(p2, p3)
        




    def statistics(self, p2: 'GXST') -> None:
        self._wrapper.statistics(p2._wrapper)
        



    @classmethod
    def un_load(cls, p1: str) -> None:
        gxapi_cy.WrapEDB.un_load(GXContext._get_tls_geo(), p1.encode())
        



    @classmethod
    def un_load_all(cls) -> None:
        gxapi_cy.WrapEDB.un_load_all(GXContext._get_tls_geo())
        




    def un_load_all_chans(self) -> None:
        self._wrapper.un_load_all_chans()
        




    def un_load_chan(self, p2: str) -> None:
        self._wrapper.un_load_chan(p2.encode())
        



    @classmethod
    def un_load_discard(cls, p1: str) -> None:
        gxapi_cy.WrapEDB.un_load_discard(GXContext._get_tls_geo(), p1.encode())
        



    @classmethod
    def un_load_verify(cls, p1: str, p2: int) -> None:
        gxapi_cy.WrapEDB.un_load_verify(GXContext._get_tls_geo(), p1.encode(), p2)
        




    def un_lock(self) -> None:
        self._wrapper.un_lock()
        




# External Window


    @classmethod
    def load_control(cls, p1: str, p2: int) -> None:
        gxapi_cy.WrapEDB.load_control(GXContext._get_tls_geo(), p1.encode(), p2)
        



    @classmethod
    def load_new_control(cls, p1: str, p2: int) -> None:
        gxapi_cy.WrapEDB.load_new_control(GXContext._get_tls_geo(), p1.encode(), p2)
        



    @classmethod
    def load_pass_control(cls, p1: str, p2: str, p3: str, p4: int) -> None:
        gxapi_cy.WrapEDB.load_pass_control(GXContext._get_tls_geo(), p1.encode(), p2.encode(), p3.encode(), p4)
        



    @classmethod
    def load_with_view_control(cls, p1: str, p2: 'GXEDB', p3: int) -> None:
        gxapi_cy.WrapEDB.load_with_view_control(GXContext._get_tls_geo(), p1.encode(), p2._wrapper, p3)
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer