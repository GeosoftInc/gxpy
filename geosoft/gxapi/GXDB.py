### extends 'class_empty.py'
from . import gxapi_cy

from geosoft.gxapi import GXContext, int_ref, float_ref, str_ref

### block Header
# NOTICE: The code generator will not replace the code in this block
### endblock Header

### block ClassImplementation
# NOTICE: Do not edit anything here, it is generated code
class GXDB:
    """
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._wrapper = None

    def __del__(self):
        self._wrapper = None

    def __init__(self, wrapper=None):
        self._wrapper = wrapper if wrapper else gxapi_cy.WrapDB(0)

    @classmethod
    def null(cls) -> 'GXDB':
        """
        A null (undefined) instance of :class:`GXDB`
        
        :returns: A null :class:`GX3DN`
        """
        return cls()

    def is_null(self) -> bool:
        """
        Check if the instance of :class:`GXDB` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of :class:`GXDB`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Channel



    def create_dup(self, p2: str) -> None:
        self._wrapper.create_dup(p2.encode())
        




    def create_dup_comp(self, p2: str, p3: int) -> None:
        self._wrapper.create_dup_comp(p2.encode(), p3)
        




    def dup_symb_across(self, p2: 'GXDB', p3: int) -> int:
        ret_val = self._wrapper.dup_symb_across(p2, p3)
        return ret_val




    def easy_maker_symb(self, p2: int, p3: str, p4: str) -> None:
        self._wrapper.easy_maker_symb(p2, p3.encode(), p4.encode())
        




    def get_chan_str(self, p2: int, p3: int, p4: int, p5: str_ref) -> None:
        p5.value = self._wrapper.get_chan_str(p2, p3, p4, p5.value.encode())
        




    def get_chan_vv(self, p2: int, p3: int, p4: 'GXVV') -> None:
        self._wrapper.get_chan_vv(p2, p3, p4)
        




    def get_chan_vv_expanded(self, p2: int, p3: int, p4: 'GXVV') -> None:
        self._wrapper.get_chan_vv_expanded(p2, p3, p4)
        




    def get_ipj(self, p2: int, p3: 'GXIPJ') -> None:
        self._wrapper.get_ipj(p2, p3)
        




    def get_itr(self, p2: int, p3: 'GXITR') -> None:
        self._wrapper.get_itr(p2, p3)
        




    def get_reg_symb(self, p2: int, p3: 'GXREG') -> None:
        self._wrapper.get_reg_symb(p2, p3)
        




    def get_reg_symb_setting(self, p2: int, p3: str, p4: str_ref) -> None:
        p4.value = self._wrapper.get_reg_symb_setting(p2, p3.encode(), p4.value.encode())
        




    def get_va_chan_vv(self, p2: int, p3: int, p4: 'GXVV', p5: int, p6: int) -> None:
        self._wrapper.get_va_chan_vv(p2, p3, p4, p5, p6)
        




    def blobs_max(self) -> int:
        ret_val = self._wrapper.blobs_max()
        return ret_val




    def chans_max(self) -> int:
        ret_val = self._wrapper.chans_max()
        return ret_val




    def format_chan(self, p2: int, p3: float, p4: str_ref) -> None:
        p4.value = self._wrapper.format_chan(p2, p3, p4.value.encode())
        




    def get_chan_array_size(self, p2: int) -> int:
        ret_val = self._wrapper.get_chan_array_size(p2)
        return ret_val




    def get_chan_class(self, p2: int, p3: str_ref) -> None:
        p3.value = self._wrapper.get_chan_class(p2, p3.value.encode())
        




    def get_chan_decimal(self, p2: int) -> int:
        ret_val = self._wrapper.get_chan_decimal(p2)
        return ret_val




    def get_chan_format(self, p2: int) -> int:
        ret_val = self._wrapper.get_chan_format(p2)
        return ret_val




    def get_chan_int(self, p2: int, p3: int, p4: int) -> int:
        ret_val = self._wrapper.get_chan_int(p2, p3, p4)
        return ret_val




    def get_chan_label(self, p2: int, p3: str_ref) -> None:
        p3.value = self._wrapper.get_chan_label(p2, p3.value.encode())
        




    def get_chan_name(self, p2: int, p3: str_ref) -> None:
        p3.value = self._wrapper.get_chan_name(p2, p3.value.encode())
        




    def get_chan_protect(self, p2: int) -> int:
        ret_val = self._wrapper.get_chan_protect(p2)
        return ret_val




    def get_chan_type(self, p2: int) -> int:
        ret_val = self._wrapper.get_chan_type(p2)
        return ret_val




    def get_chan_unit(self, p2: int, p3: str_ref) -> None:
        p3.value = self._wrapper.get_chan_unit(p2, p3.value.encode())
        




    def get_chan_width(self, p2: int) -> int:
        ret_val = self._wrapper.get_chan_width(p2)
        return ret_val




    def get_name(self, p2: int, p3: str_ref) -> None:
        p3.value = self._wrapper.get_name(p2, p3.value.encode())
        




    def get_reg_symb_setting(self, p2: int, p3: str) -> int:
        ret_val = self._wrapper.get_reg_symb_setting(p2, p3.encode())
        return ret_val




    def get_symb_name(self, p2: int, p3: str_ref) -> None:
        p3.value = self._wrapper.get_symb_name(p2, p3.value.encode())
        




    def have_itr(self, p2: int) -> int:
        ret_val = self._wrapper.have_itr(p2)
        return ret_val




    def coord_pair(self, p2: str, p3: str_ref) -> int:
        ret_val, p3.value = self._wrapper.coord_pair(p2.encode(), p3.value.encode())
        return ret_val




    def lines_max(self) -> int:
        ret_val = self._wrapper.lines_max()
        return ret_val




    def users_max(self) -> int:
        ret_val = self._wrapper.users_max()
        return ret_val




    def maker_symb(self, p2: int, p3: str, p4: str, p5: str) -> None:
        self._wrapper.maker_symb(p2, p3.encode(), p4.encode(), p5.encode())
        




    def put_chan_vv(self, p2: int, p3: int, p4: 'GXVV') -> None:
        self._wrapper.put_chan_vv(p2, p3, p4)
        




    def put_va_chan_vv(self, p2: int, p3: int, p4: 'GXVV', p5: int, p6: int) -> None:
        self._wrapper.put_va_chan_vv(p2, p3, p4, p5, p6)
        




    def read_blob_bf(self, p2: int, p3: 'GXBF') -> None:
        self._wrapper.read_blob_bf(p2, p3)
        




    def get_chan_double(self, p2: int, p3: int, p4: int) -> float:
        ret_val = self._wrapper.get_chan_double(p2, p3, p4)
        return ret_val




    def get_reg_symb_setting(self, p2: int, p3: str) -> float:
        ret_val = self._wrapper.get_reg_symb_setting(p2, p3.encode())
        return ret_val




    def set_all_chan_protect(self, p2: int) -> None:
        self._wrapper.set_all_chan_protect(p2)
        




    def set_chan_class(self, p2: int, p3: str) -> None:
        self._wrapper.set_chan_class(p2, p3.encode())
        




    def set_chan_decimal(self, p2: int, p3: int) -> None:
        self._wrapper.set_chan_decimal(p2, p3)
        




    def set_chan_format(self, p2: int, p3: int) -> None:
        self._wrapper.set_chan_format(p2, p3)
        




    def set_chan_int(self, p2: int, p3: int, p4: int, p5: int) -> None:
        self._wrapper.set_chan_int(p2, p3, p4, p5)
        




    def set_chan_label(self, p2: int, p3: str) -> None:
        self._wrapper.set_chan_label(p2, p3.encode())
        




    def set_chan_name(self, p2: int, p3: str) -> None:
        self._wrapper.set_chan_name(p2, p3.encode())
        




    def set_chan_protect(self, p2: int, p3: int) -> None:
        self._wrapper.set_chan_protect(p2, p3)
        




    def set_chan_double(self, p2: int, p3: int, p4: int, p5: float) -> None:
        self._wrapper.set_chan_double(p2, p3, p4, p5)
        




    def set_chan_str(self, p2: int, p3: int, p4: int, p5: str) -> None:
        self._wrapper.set_chan_str(p2, p3, p4, p5.encode())
        




    def set_chan_unit(self, p2: int, p3: str) -> None:
        self._wrapper.set_chan_unit(p2, p3.encode())
        




    def set_chan_width(self, p2: int, p3: int) -> None:
        self._wrapper.set_chan_width(p2, p3)
        




    def set_ipj(self, p2: int, p3: int, p4: 'GXIPJ') -> None:
        self._wrapper.set_ipj(p2, p3, p4)
        




    def set_itr(self, p2: int, p3: 'GXITR') -> None:
        self._wrapper.set_itr(p2, p3)
        




    def set_reg_symb(self, p2: int, p3: 'GXREG') -> None:
        self._wrapper.set_reg_symb(p2, p3)
        




    def set_reg_symb_setting(self, p2: int, p3: str, p4: str) -> None:
        self._wrapper.set_reg_symb_setting(p2, p3.encode(), p4.encode())
        




    def write_blob_bf(self, p2: int, p3: 'GXBF') -> None:
        self._wrapper.write_blob_bf(p2, p3)
        




# Control



    def commit(self) -> None:
        self._wrapper.commit()
        




    def compact(self) -> None:
        self._wrapper.compact()
        



    @classmethod
    def create(cls, p1: str, p2: int, p3: int, p4: int, p5: int, p6: int, p7: str, p8: str) -> None:
        gxapi_cy.WrapDB.create(GXContext._get_tls_geo(), p2, p3, p4, p5, p6, p7.encode(), p8.encode())
        



    @classmethod
    def create_comp(cls, p1: str, p2: int, p3: int, p4: int, p5: int, p6: int, p7: str, p8: str, p9: int, p10: int) -> None:
        gxapi_cy.WrapDB.create_comp(GXContext._get_tls_geo(), p2, p3, p4, p5, p6, p7.encode(), p8.encode(), p9, p10)
        



    @classmethod
    def create_ex(cls, p1: str, p2: int, p3: int, p4: int, p5: int, p6: int, p7: str, p8: str, p9: int) -> None:
        gxapi_cy.WrapDB.create_ex(GXContext._get_tls_geo(), p2, p3, p4, p5, p6, p7.encode(), p8.encode(), p9)
        




    def del_line0(self) -> None:
        self._wrapper.del_line0()
        






    def discard(self) -> None:
        self._wrapper.discard()
        



    @classmethod
    def grow(cls, p1: str, p2: int, p3: int, p4: int, p5: int, p6: int) -> None:
        gxapi_cy.WrapDB.grow(GXContext._get_tls_geo(), p2, p3, p4, p5, p6)
        



    @classmethod
    def can_open(cls, p1: str, p2: str, p3: str) -> int:
        ret_val = gxapi_cy.WrapDB.can_open(GXContext._get_tls_geo(), p2.encode(), p3.encode())
        return ret_val



    @classmethod
    def can_open_read_only(cls, p1: str, p2: str, p3: str) -> int:
        ret_val = gxapi_cy.WrapDB.can_open_read_only(GXContext._get_tls_geo(), p2.encode(), p3.encode())
        return ret_val




    def check(self) -> int:
        ret_val = self._wrapper.check()
        return ret_val




    def is_empty(self) -> int:
        ret_val = self._wrapper.is_empty()
        return ret_val




    def is_line_empty(self, p2: int) -> int:
        ret_val = self._wrapper.is_line_empty(p2)
        return ret_val



    @classmethod
    def open(cls, p1: str, p2: str, p3: str) -> 'GXDB':
        ret_val = gxapi_cy.WrapDB.open(GXContext._get_tls_geo(), p2.encode(), p3.encode())
        return GXDB(ret_val)



    @classmethod
    def open_read_only(cls, p1: str, p2: str, p3: str) -> 'GXDB':
        ret_val = gxapi_cy.WrapDB.open_read_only(GXContext._get_tls_geo(), p2.encode(), p3.encode())
        return GXDB(ret_val)



    @classmethod
    def repair(cls, p1: str) -> None:
        gxapi_cy.WrapDB.repair(GXContext._get_tls_geo())
        




    def sync(self) -> None:
        self._wrapper.sync()
        




# Data



    def copy_data(self, p2: int, p3: int, p4: int) -> None:
        self._wrapper.copy_data(p2, p3, p4)
        




    def get_col_va(self, p2: int) -> int:
        ret_val = self._wrapper.get_col_va(p2)
        return ret_val




    def get_channel_length(self, p2: int, p3: int) -> int:
        ret_val = self._wrapper.get_channel_length(p2, p3)
        return ret_val




    def get_fid_incr(self, p2: int, p3: int) -> float:
        ret_val = self._wrapper.get_fid_incr(p2, p3)
        return ret_val




    def get_fid_start(self, p2: int, p3: int) -> float:
        ret_val = self._wrapper.get_fid_start(p2, p3)
        return ret_val




    def set_fid(self, p2: int, p3: int, p4: float, p5: float) -> None:
        self._wrapper.set_fid(p2, p3, p4, p5)
        




    def window_va_ch(self, p2: int, p3: int, p4: int, p5: int, p6: int) -> None:
        self._wrapper.window_va_ch(p2, p3, p4, p5, p6)
        




    def window_va_ch2(self, p2: int, p3: int, p4: int, p5: 'GXVV') -> None:
        self._wrapper.window_va_ch2(p2, p3, p4, p5)
        




# Line



    def set_line_selection(self, p2: int, p3: int) -> None:
        self._wrapper.set_line_selection(p2, p3)
        




    def get_line_selection(self, p2: int) -> int:
        ret_val = self._wrapper.get_line_selection(p2)
        return ret_val




    def first_sel_line(self) -> int:
        ret_val = self._wrapper.first_sel_line()
        return ret_val




    def get_line_map_fid(self, p2: int, p3: float_ref, p4: float_ref) -> None:
        p3.value, p4.value = self._wrapper.get_line_map_fid(p2, p3.value, p4.value)
        




    def get_select(self) -> int:
        ret_val = self._wrapper.get_select()
        return ret_val




    def count_sel_lines(self) -> int:
        ret_val = self._wrapper.count_sel_lines()
        return ret_val



    @classmethod
    def is_chan_name(cls, p1: str) -> int:
        ret_val = gxapi_cy.WrapDB.is_chan_name(GXContext._get_tls_geo())
        return ret_val




    def is_chan_valid(self, p2: int) -> int:
        ret_val = self._wrapper.is_chan_valid(p2)
        return ret_val



    @classmethod
    def is_line_name(cls, p1: str) -> int:
        ret_val = gxapi_cy.WrapDB.is_line_name(GXContext._get_tls_geo())
        return ret_val




    def is_line_valid(self, p2: int) -> int:
        ret_val = self._wrapper.is_line_valid(p2)
        return ret_val




    def line_category(self, p2: int) -> int:
        ret_val = self._wrapper.line_category(p2)
        return ret_val




    def line_flight(self, p2: int) -> int:
        ret_val = self._wrapper.line_flight(p2)
        return ret_val




    def line_label(self, p2: int, p3: str_ref, p5: int) -> None:
        p3.value = self._wrapper.line_label(p2, p3.value.encode(), p5)
        




    def line_number(self, p2: int) -> int:
        ret_val = self._wrapper.line_number(p2)
        return ret_val




    def line_number2(self, p2: int, p3: str_ref) -> None:
        p3.value = self._wrapper.line_number2(p2, p3.value.encode())
        




    def line_type(self, p2: int) -> int:
        ret_val = self._wrapper.line_type(p2)
        return ret_val




    def line_version(self, p2: int) -> int:
        ret_val = self._wrapper.line_version(p2)
        return ret_val



    @classmethod
    def set_line_name(cls, p1: int, p2: int, p3: int, p4: str_ref) -> None:
        p4.value = gxapi_cy.WrapDB.set_line_name(GXContext._get_tls_geo(), p2, p3, p4.value.encode())
        



    @classmethod
    def set_line_name2(cls, p1: str, p2: int, p3: int, p4: str_ref) -> None:
        p4.value = gxapi_cy.WrapDB.set_line_name2(GXContext._get_tls_geo(), p2, p3, p4.value.encode())
        




    def load_select(self, p2: str) -> None:
        self._wrapper.load_select(p2.encode())
        




    def next_sel_line(self, p2: int) -> int:
        ret_val = self._wrapper.next_sel_line(p2)
        return ret_val




    def line_bearing(self, p2: int) -> float:
        ret_val = self._wrapper.line_bearing(p2)
        return ret_val




    def line_date(self, p2: int) -> float:
        ret_val = self._wrapper.line_date(p2)
        return ret_val




    def save_select(self, p2: str) -> None:
        self._wrapper.save_select(p2.encode())
        




    def select(self, p2: str, p3: int) -> None:
        self._wrapper.select(p2.encode(), p3)
        




    def set_line_bearing(self, p2: int, p3: float) -> None:
        self._wrapper.set_line_bearing(p2, p3)
        




    def set_line_date(self, p2: int, p3: float) -> None:
        self._wrapper.set_line_date(p2, p3)
        




    def set_line_flight(self, p2: int, p3: int) -> None:
        self._wrapper.set_line_flight(p2, p3)
        




    def set_line_map_fid(self, p2: int, p3: float, p4: float) -> None:
        self._wrapper.set_line_map_fid(p2, p3, p4)
        




    def set_line_num(self, p2: int, p3: int) -> None:
        self._wrapper.set_line_num(p2, p3)
        




    def set_line_type(self, p2: int, p3: int) -> None:
        self._wrapper.set_line_type(p2, p3)
        




    def set_line_ver(self, p2: int, p3: int) -> None:
        self._wrapper.set_line_ver(p2, p3)
        




    def set_select(self, p2: int) -> None:
        self._wrapper.set_select(p2)
        




# META



    def get_meta(self, p2: 'GXMETA') -> None:
        self._wrapper.get_meta(p2)
        




    def set_meta(self, p2: 'GXMETA') -> None:
        self._wrapper.set_meta(p2)
        




# Symbols



    def array_lst(self, p2: 'GXLST') -> None:
        self._wrapper.array_lst(p2)
        




    def array_size_lst(self, p2: int, p3: 'GXLST') -> None:
        self._wrapper.array_size_lst(p2, p3)
        




    def chan_lst(self, p2: 'GXLST') -> None:
        self._wrapper.chan_lst(p2)
        




    def normal_chan_lst(self, p2: 'GXLST') -> None:
        self._wrapper.normal_chan_lst(p2)
        




    def class_chan_lst(self, p2: 'GXLST', p3: str) -> None:
        self._wrapper.class_chan_lst(p2, p3.encode())
        




    def class_group_lst(self, p2: 'GXLST', p3: str) -> None:
        self._wrapper.class_group_lst(p2, p3.encode())
        




    def create_symb(self, p2: str, p3: int, p4: int, p5: int) -> int:
        ret_val = self._wrapper.create_symb(p2.encode(), p3, p4, p5)
        return ret_val




    def create_symb_ex(self, p2: str, p3: int, p4: int, p5: int, p6: int) -> int:
        ret_val = self._wrapper.create_symb_ex(p2.encode(), p3, p4, p5, p6)
        return ret_val




    def csv_chan_lst(self, p2: 'GXLST', p3: str) -> None:
        self._wrapper.csv_chan_lst(p2, p3.encode())
        




    def delete_symb(self, p2: int) -> None:
        self._wrapper.delete_symb(p2)
        




    def dup_line_symb(self, p2: int, p3: str) -> int:
        ret_val = self._wrapper.dup_line_symb(p2, p3.encode())
        return ret_val




    def dup_symb(self, p2: int, p3: str) -> int:
        ret_val = self._wrapper.dup_symb(p2, p3.encode())
        return ret_val




    def dup_symb_no_lock(self, p2: int, p3: str) -> int:
        ret_val = self._wrapper.dup_symb_no_lock(p2, p3.encode())
        return ret_val




    def find_chan(self, p2: str) -> int:
        ret_val = self._wrapper.find_chan(p2.encode())
        return ret_val




    def find_symb(self, p2: str, p3: int) -> int:
        ret_val = self._wrapper.find_symb(p2.encode(), p3)
        return ret_val




    def get_chan_order_lst(self, p2: 'GXLST') -> None:
        self._wrapper.get_chan_order_lst(p2)
        




    def get_xyz_chan_symb(self, p2: int) -> int:
        ret_val = self._wrapper.get_xyz_chan_symb(p2)
        return ret_val




    def class_chan_list(self, p2: 'GXVV', p3: str) -> int:
        ret_val = self._wrapper.class_chan_list(p2, p3.encode())
        return ret_val




    def exist_chan(self, p2: str) -> int:
        ret_val = self._wrapper.exist_chan(p2.encode())
        return ret_val




    def exist_symb(self, p2: str, p3: int) -> int:
        ret_val = self._wrapper.exist_symb(p2.encode(), p3)
        return ret_val




    def valid_symb(self, p2: int, p3: int) -> int:
        ret_val = self._wrapper.valid_symb(p2, p3)
        return ret_val




    def get_symb_lock(self, p2: int) -> int:
        ret_val = self._wrapper.get_symb_lock(p2)
        return ret_val




    def get_xyz_chan(self, p2: int, p3: str_ref) -> None:
        p3.value = self._wrapper.get_xyz_chan(p2, p3.value.encode())
        




    def symb_list(self, p2: 'GXVV', p3: int) -> int:
        ret_val = self._wrapper.symb_list(p2, p3)
        return ret_val




    def line_lst(self, p2: 'GXLST') -> None:
        self._wrapper.line_lst(p2)
        




    def lock_symb(self, p2: int, p3: int, p4: int) -> None:
        self._wrapper.lock_symb(p2, p3, p4)
        




    def mask_chan_lst(self, p2: 'GXLST') -> None:
        self._wrapper.mask_chan_lst(p2)
        




    def selected_line_lst(self, p2: 'GXLST') -> None:
        self._wrapper.selected_line_lst(p2)
        




    def set_chan_order_lst(self, p2: 'GXLST') -> None:
        self._wrapper.set_chan_order_lst(p2)
        




    def set_xyz_chan(self, p2: int, p3: str) -> None:
        self._wrapper.set_xyz_chan(p2, p3.encode())
        




    def string_chan_lst(self, p2: 'GXLST') -> None:
        self._wrapper.string_chan_lst(p2)
        




    def symb_lst(self, p2: 'GXLST', p3: int) -> None:
        self._wrapper.symb_lst(p2, p3)
        




    def un_lock_all_symb(self) -> None:
        self._wrapper.un_lock_all_symb()
        




    def un_lock_symb(self, p2: int) -> None:
        self._wrapper.un_lock_symb(p2)
        




# VA Channels



    def add_associated_load(self, p2: int, p3: int) -> None:
        self._wrapper.add_associated_load(p2, p3)
        




    def add_comment(self, p2: str, p3: str, p4: int) -> None:
        self._wrapper.add_comment(p2.encode(), p3.encode(), p4)
        




    def add_int_comment(self, p2: str, p3: int, p4: int) -> None:
        self._wrapper.add_int_comment(p2.encode(), p3, p4)
        




    def add_double_comment(self, p2: str, p3: float, p4: int) -> None:
        self._wrapper.add_double_comment(p2.encode(), p3, p4)
        




    def add_time_comment(self, p2: str, p3: int) -> None:
        self._wrapper.add_time_comment(p2.encode(), p3)
        




    def associate(self, p2: int, p3: int) -> None:
        self._wrapper.associate(p2, p3)
        




    def associate_all(self, p2: int) -> None:
        self._wrapper.associate_all(p2)
        




    def associate_class(self, p2: int, p3: str) -> None:
        self._wrapper.associate_class(p2, p3.encode())
        



    @classmethod
    def gen_valid_chan_symb(cls, p1: str, p2: str_ref) -> None:
        p2.value = gxapi_cy.WrapDB.gen_valid_chan_symb(GXContext._get_tls_geo(), p2.value.encode())
        



    @classmethod
    def gen_valid_line_symb(cls, p1: str, p2: str_ref) -> None:
        p2.value = gxapi_cy.WrapDB.gen_valid_line_symb(GXContext._get_tls_geo(), p2.value.encode())
        




    def get_chan_va(self, p2: int, p3: int, p4: 'GXVA') -> None:
        self._wrapper.get_chan_va(p2, p3, p4)
        




    def get_va_scaling(self, p2: int, p3: float_ref, p4: float_ref) -> None:
        p3.value, p4.value = self._wrapper.get_va_scaling(p2, p3.value, p4.value)
        




    def get_va_windows(self, p2: int, p3: int_ref, p4: int_ref) -> None:
        p3.value, p4.value = self._wrapper.get_va_windows(p2, p3.value, p4.value)
        




    def set_va_base_coordinate_info(self, p2: int, p3: int, p4: float, p5: 'GXVV', p6: str, p7: int) -> None:
        self._wrapper.set_va_base_coordinate_info(p2, p3, p4, p5, p6.encode(), p7)
        




    def get_va_base_coordinate_info(self, p2: int, p3: int_ref, p4: float_ref, p5: 'GXVV', p6: str_ref) -> None:
        p3.value, p4.value, p6.value = self._wrapper.get_va_base_coordinate_info(p2, p3.value, p4.value, p5, p6.value.encode())
        




    def get_group_class(self, p2: int, p3: str_ref) -> None:
        p3.value = self._wrapper.get_group_class(p2, p3.value.encode())
        




    def get_info(self, p2: int) -> int:
        ret_val = self._wrapper.get_info(p2)
        return ret_val




    def get_va_prof_color_file(self, p2: int, p3: str_ref) -> None:
        p3.value = self._wrapper.get_va_prof_color_file(p2, p3.value.encode())
        




    def get_va_prof_sect_option(self, p2: int, p3: str_ref) -> None:
        p3.value = self._wrapper.get_va_prof_sect_option(p2, p3.value.encode())
        




    def get_va_sect_color_file(self, p2: int, p3: str_ref) -> None:
        p3.value = self._wrapper.get_va_sect_color_file(p2, p3.value.encode())
        




    def is_associated(self, p2: int, p3: int) -> int:
        ret_val = self._wrapper.is_associated(p2, p3)
        return ret_val




    def is_wholeplot(self) -> int:
        ret_val = self._wrapper.is_wholeplot()
        return ret_val




    def put_chan_va(self, p2: int, p3: int, p4: 'GXVA') -> None:
        self._wrapper.put_chan_va(p2, p3, p4)
        




    def set_group_class(self, p2: int, p3: str) -> None:
        self._wrapper.set_group_class(p2, p3.encode())
        




    def set_va_prof_color_file(self, p2: int, p3: str) -> None:
        self._wrapper.set_va_prof_color_file(p2, p3.encode())
        




    def set_va_prof_sect_option(self, p2: int, p3: str) -> None:
        self._wrapper.set_va_prof_sect_option(p2, p3.encode())
        




    def set_va_scaling(self, p2: int, p3: float, p4: float) -> None:
        self._wrapper.set_va_scaling(p2, p3, p4)
        




    def set_va_sect_color_file(self, p2: int, p3: str) -> None:
        self._wrapper.set_va_sect_color_file(p2, p3.encode())
        




    def set_va_windows(self, p2: int, p3: int, p4: int) -> None:
        self._wrapper.set_va_windows(p2, p3, p4)
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer