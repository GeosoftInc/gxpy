### extends 'class_empty.py'
from . import gxapi_cy

from geosoft.gxapi import GXContext, int_ref, float_ref, str_ref

### block Header
# NOTICE: The code generator will not replace the code in this block
### endblock Header

### block ClassImplementation
# NOTICE: Do not edit anything here, it is generated code
class GXSYS:
    """
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._wrapper = None

    def __del__(self):
        self._wrapper = None

    def __init__(self, wrapper=None):
        self._wrapper = wrapper if wrapper else gxapi_cy.WrapSYS(0)

    @classmethod
    def null(cls) -> 'GXSYS':
        """
        A null (undefined) instance of :class:`GXSYS`
        
        :returns: A null :class:`GX3DN`
        """
        return cls()

    def is_null(self) -> bool:
        """
        Check if the instance of :class:`GXSYS` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of :class:`GXSYS`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Date/Time


    @classmethod
    def break_date(cls, p1: float, p2: int_ref, p3: int_ref, p4: int_ref) -> None:
        p2.value, p3.value, p4.value = gxapi_cy.WrapSYS.break_date(GXContext._get_tls_geo(), p1, p2.value, p3.value, p4.value)
        



    @classmethod
    def dateto_long(cls, p1: float) -> int:
        ret_val = gxapi_cy.WrapSYS.dateto_long(GXContext._get_tls_geo(), p1)
        return ret_val



    @classmethod
    def timeto_long(cls, p1: float) -> int:
        ret_val = gxapi_cy.WrapSYS.timeto_long(GXContext._get_tls_geo(), p1)
        return ret_val



    @classmethod
    def date(cls) -> float:
        ret_val = gxapi_cy.WrapSYS.date(GXContext._get_tls_geo())
        return ret_val



    @classmethod
    def longto_date(cls, p1: int) -> float:
        ret_val = gxapi_cy.WrapSYS.longto_date(GXContext._get_tls_geo(), p1)
        return ret_val



    @classmethod
    def longto_time(cls, p1: int) -> float:
        ret_val = gxapi_cy.WrapSYS.longto_time(GXContext._get_tls_geo(), p1)
        return ret_val



    @classmethod
    def make_date(cls, p1: int, p2: int, p3: int) -> float:
        ret_val = gxapi_cy.WrapSYS.make_date(GXContext._get_tls_geo(), p1, p2, p3)
        return ret_val



    @classmethod
    def secondsto_time(cls, p1: float) -> float:
        ret_val = gxapi_cy.WrapSYS.secondsto_time(GXContext._get_tls_geo(), p1)
        return ret_val



    @classmethod
    def time(cls) -> float:
        ret_val = gxapi_cy.WrapSYS.time(GXContext._get_tls_geo())
        return ret_val



    @classmethod
    def timeto_seconds(cls, p1: float) -> float:
        ret_val = gxapi_cy.WrapSYS.timeto_seconds(GXContext._get_tls_geo(), p1)
        return ret_val



    @classmethod
    def utc_date(cls) -> float:
        ret_val = gxapi_cy.WrapSYS.utc_date(GXContext._get_tls_geo())
        return ret_val



    @classmethod
    def utc_time(cls) -> float:
        ret_val = gxapi_cy.WrapSYS.utc_time(GXContext._get_tls_geo())
        return ret_val




# Environment


    @classmethod
    def exist_env(cls, p1: str) -> int:
        ret_val = gxapi_cy.WrapSYS.exist_env(GXContext._get_tls_geo(), p1.encode())
        return ret_val



    @classmethod
    def get_env(cls, p1: str, p2: str_ref) -> None:
        p2.value = gxapi_cy.WrapSYS.get_env(GXContext._get_tls_geo(), p1.encode(), p2.value.encode())
        



    @classmethod
    def set_env(cls, p1: str, p2: str) -> None:
        gxapi_cy.WrapSYS.set_env(GXContext._get_tls_geo(), p1.encode(), p2.encode())
        




# Error Handling


    @classmethod
    def clear_err_ap(cls) -> int:
        ret_val = gxapi_cy.WrapSYS.clear_err_ap(GXContext._get_tls_geo())
        return ret_val



    @classmethod
    def get_top_error_ap(cls) -> int:
        ret_val = gxapi_cy.WrapSYS.get_top_error_ap(GXContext._get_tls_geo())
        return ret_val



    @classmethod
    def get_error_message_ap(cls, p1: int, p2: str_ref) -> None:
        p2.value = gxapi_cy.WrapSYS.get_error_message_ap(GXContext._get_tls_geo(), p1, p2.value.encode())
        



    @classmethod
    def num_errors_ap(cls) -> int:
        ret_val = gxapi_cy.WrapSYS.num_errors_ap(GXContext._get_tls_geo())
        return ret_val



    @classmethod
    def set_server_messages_ap(cls, p1: int) -> None:
        gxapi_cy.WrapSYS.set_server_messages_ap(GXContext._get_tls_geo(), p1)
        




# Execution


    @classmethod
    def run(cls, p1: str, p2: str, p3: int) -> int:
        ret_val = gxapi_cy.WrapSYS.run(GXContext._get_tls_geo(), p1.encode(), p2.encode(), p3)
        return ret_val



    @classmethod
    def run_gs(cls, p1: str) -> int:
        ret_val = gxapi_cy.WrapSYS.run_gs(GXContext._get_tls_geo(), p1.encode())
        return ret_val



    @classmethod
    def run_gx(cls, p1: str) -> int:
        ret_val = gxapi_cy.WrapSYS.run_gx(GXContext._get_tls_geo(), p1.encode())
        return ret_val



    @classmethod
    def run_gx_ex(cls, p1: str, p2: int_ref) -> int:
        ret_val, p2.value = gxapi_cy.WrapSYS.run_gx_ex(GXContext._get_tls_geo(), p1.encode(), p2.value)
        return ret_val



    @classmethod
    def run_pdf(cls, p1: str, p2: str) -> int:
        ret_val = gxapi_cy.WrapSYS.run_pdf(GXContext._get_tls_geo(), p1.encode(), p2.encode())
        return ret_val



    @classmethod
    def shell_execute(cls, p1: str, p2: str, p3: str, p4: str, p5: int) -> int:
        ret_val = gxapi_cy.WrapSYS.shell_execute(GXContext._get_tls_geo(), p1.encode(), p2.encode(), p3.encode(), p4.encode(), p5)
        return ret_val



    @classmethod
    def set_return(cls, p1: int) -> None:
        gxapi_cy.WrapSYS.set_return(GXContext._get_tls_geo(), p1)
        




# External DLL


    @classmethod
    def do_command(cls, p1: str) -> None:
        gxapi_cy.WrapSYS.do_command(GXContext._get_tls_geo(), p1.encode())
        



    @classmethod
    def error(cls, p1: str, p2: str, p3: int) -> None:
        gxapi_cy.WrapSYS.error(GXContext._get_tls_geo(), p1.encode(), p2.encode(), p3)
        



    @classmethod
    def error_tag(cls, p1: str, p2: str) -> None:
        gxapi_cy.WrapSYS.error_tag(GXContext._get_tls_geo(), p1.encode(), p2.encode())
        



    @classmethod
    def assert_gx(cls, p1: int, p2: str, p3: str) -> int:
        ret_val = gxapi_cy.WrapSYS.assert_gx(GXContext._get_tls_geo(), p1, p2.encode(), p3.encode())
        return ret_val



    @classmethod
    def ole_automation(cls, p1: str, p2: str, p3: int) -> int:
        ret_val = gxapi_cy.WrapSYS.ole_automation(GXContext._get_tls_geo(), p1.encode(), p2.encode(), p3)
        return ret_val



    @classmethod
    def save_log(cls, p1: str) -> None:
        gxapi_cy.WrapSYS.save_log(GXContext._get_tls_geo(), p1.encode())
        



    @classmethod
    def show_error(cls) -> None:
        gxapi_cy.WrapSYS.show_error(GXContext._get_tls_geo())
        



    @classmethod
    def terminate(cls, p1: str) -> None:
        gxapi_cy.WrapSYS.terminate(GXContext._get_tls_geo(), p1.encode())
        




# File System


    @classmethod
    def crc_file(cls, p1: str) -> int:
        ret_val = gxapi_cy.WrapSYS.crc_file(GXContext._get_tls_geo(), p1.encode())
        return ret_val



    @classmethod
    def crc_file_offset(cls, p1: str, p2: int) -> int:
        ret_val = gxapi_cy.WrapSYS.crc_file_offset(GXContext._get_tls_geo(), p1.encode(), p2)
        return ret_val



    @classmethod
    def file_ren(cls, p1: str, p2: str) -> None:
        gxapi_cy.WrapSYS.file_ren(GXContext._get_tls_geo(), p1.encode(), p2.encode())
        



    @classmethod
    def find_files_vv(cls, p1: 'GXVV', p2: str) -> None:
        gxapi_cy.WrapSYS.find_files_vv(GXContext._get_tls_geo(), p1._wrapper, p2.encode())
        



    @classmethod
    def absolute_file_name(cls, p1: str, p2: str_ref) -> None:
        p2.value = gxapi_cy.WrapSYS.absolute_file_name(GXContext._get_tls_geo(), p1.encode(), p2.value.encode())
        



    @classmethod
    def copy_file(cls, p1: str, p2: str) -> int:
        ret_val = gxapi_cy.WrapSYS.copy_file(GXContext._get_tls_geo(), p1.encode(), p2.encode())
        return ret_val



    @classmethod
    def delete_file(cls, p1: str) -> int:
        ret_val = gxapi_cy.WrapSYS.delete_file(GXContext._get_tls_geo(), p1.encode())
        return ret_val



    @classmethod
    def delete_gi_file(cls, p1: str) -> int:
        ret_val = gxapi_cy.WrapSYS.delete_gi_file(GXContext._get_tls_geo(), p1.encode())
        return ret_val



    @classmethod
    def delete_grid_file(cls, p1: str) -> int:
        ret_val = gxapi_cy.WrapSYS.delete_grid_file(GXContext._get_tls_geo(), p1.encode())
        return ret_val



    @classmethod
    def dir_exist(cls, p1: str) -> int:
        ret_val = gxapi_cy.WrapSYS.dir_exist(GXContext._get_tls_geo(), p1.encode())
        return ret_val



    @classmethod
    def file_exist(cls, p1: str) -> int:
        ret_val = gxapi_cy.WrapSYS.file_exist(GXContext._get_tls_geo(), p1.encode())
        return ret_val



    @classmethod
    def file_size(cls, p1: str) -> int:
        ret_val = gxapi_cy.WrapSYS.file_size(GXContext._get_tls_geo(), p1.encode())
        return ret_val



    @classmethod
    def file_writable(cls, p1: str) -> int:
        ret_val = gxapi_cy.WrapSYS.file_writable(GXContext._get_tls_geo(), p1.encode())
        return ret_val



    @classmethod
    def find_path(cls, p1: str, p2: int, p3: str_ref) -> int:
        ret_val, p3.value = gxapi_cy.WrapSYS.find_path(GXContext._get_tls_geo(), p1.encode(), p2, p3.value.encode())
        return ret_val



    @classmethod
    def find_path_ex(cls, p1: str, p2: int, p3: int, p4: str_ref) -> int:
        ret_val, p4.value = gxapi_cy.WrapSYS.find_path_ex(GXContext._get_tls_geo(), p1.encode(), p2, p3, p4.value.encode())
        return ret_val



    @classmethod
    def get_directory(cls, p1: int, p2: str_ref) -> None:
        p2.value = gxapi_cy.WrapSYS.get_directory(GXContext._get_tls_geo(), p1, p2.value.encode())
        



    @classmethod
    def get_path(cls, p1: int, p2: str_ref) -> None:
        p2.value = gxapi_cy.WrapSYS.get_path(GXContext._get_tls_geo(), p1, p2.value.encode())
        



    @classmethod
    def get_windows_dir(cls, p1: str_ref) -> None:
        p1.value = gxapi_cy.WrapSYS.get_windows_dir(GXContext._get_tls_geo(), p1.value.encode())
        



    @classmethod
    def make_dir(cls, p1: str) -> int:
        ret_val = gxapi_cy.WrapSYS.make_dir(GXContext._get_tls_geo(), p1.encode())
        return ret_val



    @classmethod
    def make_file_readonly(cls, p1: str) -> int:
        ret_val = gxapi_cy.WrapSYS.make_file_readonly(GXContext._get_tls_geo(), p1.encode())
        return ret_val



    @classmethod
    def make_file_writable(cls, p1: str) -> int:
        ret_val = gxapi_cy.WrapSYS.make_file_writable(GXContext._get_tls_geo(), p1.encode())
        return ret_val



    @classmethod
    def relative_file_name(cls, p1: str, p2: str_ref) -> None:
        p2.value = gxapi_cy.WrapSYS.relative_file_name(GXContext._get_tls_geo(), p1.encode(), p2.value.encode())
        



    @classmethod
    def short_path_file_name(cls, p1: str, p2: str_ref) -> None:
        p2.value = gxapi_cy.WrapSYS.short_path_file_name(GXContext._get_tls_geo(), p1.encode(), p2.value.encode())
        



    @classmethod
    def temp_file_ext(cls, p1: str, p2: str_ref) -> None:
        p2.value = gxapi_cy.WrapSYS.temp_file_ext(GXContext._get_tls_geo(), p1.encode(), p2.value.encode())
        



    @classmethod
    def temp_file_name(cls, p1: str, p2: str_ref) -> None:
        p2.value = gxapi_cy.WrapSYS.temp_file_name(GXContext._get_tls_geo(), p1.encode(), p2.value.encode())
        



    @classmethod
    def transfer_path(cls, p1: str, p2: str_ref) -> None:
        p2.value = gxapi_cy.WrapSYS.transfer_path(GXContext._get_tls_geo(), p1.encode(), p2.value.encode())
        



    @classmethod
    def valid_file_name(cls, p1: str) -> int:
        ret_val = gxapi_cy.WrapSYS.valid_file_name(GXContext._get_tls_geo(), p1.encode())
        return ret_val



    @classmethod
    def write_in_dir(cls, p1: str) -> int:
        ret_val = gxapi_cy.WrapSYS.write_in_dir(GXContext._get_tls_geo(), p1.encode())
        return ret_val



    @classmethod
    def file_date(cls, p1: str) -> float:
        ret_val = gxapi_cy.WrapSYS.file_date(GXContext._get_tls_geo(), p1.encode())
        return ret_val



    @classmethod
    def file_time(cls, p1: str) -> float:
        ret_val = gxapi_cy.WrapSYS.file_time(GXContext._get_tls_geo(), p1.encode())
        return ret_val



    @classmethod
    def utc_file_date(cls, p1: str) -> float:
        ret_val = gxapi_cy.WrapSYS.utc_file_date(GXContext._get_tls_geo(), p1.encode())
        return ret_val



    @classmethod
    def utc_file_time(cls, p1: str) -> float:
        ret_val = gxapi_cy.WrapSYS.utc_file_time(GXContext._get_tls_geo(), p1.encode())
        return ret_val




# Global Parameter


    @classmethod
    def get_settings_meta(cls, p1: 'GXMETA') -> None:
        gxapi_cy.WrapSYS.get_settings_meta(GXContext._get_tls_geo(), p1._wrapper)
        



    @classmethod
    def global_reset(cls, p1: str) -> None:
        gxapi_cy.WrapSYS.global_reset(GXContext._get_tls_geo(), p1.encode())
        



    @classmethod
    def global_set(cls, p1: str, p2: str) -> None:
        gxapi_cy.WrapSYS.global_set(GXContext._get_tls_geo(), p1.encode(), p2.encode())
        



    @classmethod
    def global_write(cls, p1: str) -> None:
        gxapi_cy.WrapSYS.global_write(GXContext._get_tls_geo(), p1.encode())
        



    @classmethod
    def global_(cls, p1: str, p2: str_ref) -> int:
        ret_val, p2.value = gxapi_cy.WrapSYS.global_(GXContext._get_tls_geo(), p1.encode(), p2.value.encode())
        return ret_val



    @classmethod
    def reset_settings(cls) -> None:
        gxapi_cy.WrapSYS.reset_settings(GXContext._get_tls_geo())
        



    @classmethod
    def set_settings_meta(cls, p1: 'GXMETA') -> None:
        gxapi_cy.WrapSYS.set_settings_meta(GXContext._get_tls_geo(), p1._wrapper)
        




# Licensing


    @classmethod
    def check_arc_license(cls) -> int:
        ret_val = gxapi_cy.WrapSYS.check_arc_license(GXContext._get_tls_geo())
        return ret_val



    @classmethod
    def check_arc_license_ex(cls, p1: str_ref) -> int:
        ret_val, p1.value = gxapi_cy.WrapSYS.check_arc_license_ex(GXContext._get_tls_geo(), p1.value.encode())
        return ret_val



    @classmethod
    def check_intrinsic(cls, p1: int, p2: str) -> int:
        ret_val = gxapi_cy.WrapSYS.check_intrinsic(GXContext._get_tls_geo(), p1, p2.encode())
        return ret_val



    @classmethod
    def get_geodist(cls) -> int:
        ret_val = gxapi_cy.WrapSYS.get_geodist(GXContext._get_tls_geo())
        return ret_val



    @classmethod
    def get_license_class(cls, p1: str_ref) -> None:
        p1.value = gxapi_cy.WrapSYS.get_license_class(GXContext._get_tls_geo(), p1.value.encode())
        



    @classmethod
    def get_licensed_user(cls, p1: str_ref, p3: str_ref) -> None:
        p1.value, p3.value = gxapi_cy.WrapSYS.get_licensed_user(GXContext._get_tls_geo(), p1.value.encode(), p3.value.encode())
        




# Lineage


    @classmethod
    def add_lineage_parameter(cls, p1: str, p2: str) -> None:
        gxapi_cy.WrapSYS.add_lineage_parameter(GXContext._get_tls_geo(), p1.encode(), p2.encode())
        



    @classmethod
    def add_lineage_source(cls, p1: int, p2: str) -> None:
        gxapi_cy.WrapSYS.add_lineage_source(GXContext._get_tls_geo(), p1, p2.encode())
        



    @classmethod
    def clear_lineage_parameters(cls) -> None:
        gxapi_cy.WrapSYS.clear_lineage_parameters(GXContext._get_tls_geo())
        



    @classmethod
    def clear_lineage_sources(cls) -> None:
        gxapi_cy.WrapSYS.clear_lineage_sources(GXContext._get_tls_geo())
        



    @classmethod
    def copy_geo_file(cls, p1: str, p2: str) -> None:
        gxapi_cy.WrapSYS.copy_geo_file(GXContext._get_tls_geo(), p1.encode(), p2.encode())
        



    @classmethod
    def backup_geo_file(cls, p1: str, p2: str_ref) -> None:
        p2.value = gxapi_cy.WrapSYS.backup_geo_file(GXContext._get_tls_geo(), p1.encode(), p2.value.encode())
        



    @classmethod
    def remove_lineage_output(cls, p1: str) -> None:
        gxapi_cy.WrapSYS.remove_lineage_output(GXContext._get_tls_geo(), p1.encode())
        



    @classmethod
    def remove_lineage_parameter(cls, p1: str) -> None:
        gxapi_cy.WrapSYS.remove_lineage_parameter(GXContext._get_tls_geo(), p1.encode())
        



    @classmethod
    def remove_lineage_source(cls, p1: str) -> None:
        gxapi_cy.WrapSYS.remove_lineage_source(GXContext._get_tls_geo(), p1.encode())
        



    @classmethod
    def restore_geo_file(cls, p1: str, p2: str) -> None:
        gxapi_cy.WrapSYS.restore_geo_file(GXContext._get_tls_geo(), p1.encode(), p2.encode())
        



    @classmethod
    def set_lineage_description(cls, p1: str) -> None:
        gxapi_cy.WrapSYS.set_lineage_description(GXContext._get_tls_geo(), p1.encode())
        



    @classmethod
    def set_lineage_display_name(cls, p1: str) -> None:
        gxapi_cy.WrapSYS.set_lineage_display_name(GXContext._get_tls_geo(), p1.encode())
        



    @classmethod
    def set_lineage_name(cls, p1: str) -> None:
        gxapi_cy.WrapSYS.set_lineage_name(GXContext._get_tls_geo(), p1.encode())
        




# Menus and Toolbar


    @classmethod
    def clear_menus(cls, p1: int) -> None:
        gxapi_cy.WrapSYS.clear_menus(GXContext._get_tls_geo(), p1)
        



    @classmethod
    def get_loaded_menus(cls, p1: 'GXLST', p2: 'GXLST', p3: 'GXLST') -> None:
        gxapi_cy.WrapSYS.get_loaded_menus(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3._wrapper)
        



    @classmethod
    def set_loaded_menus(cls, p1: 'GXLST', p2: 'GXLST', p3: 'GXLST') -> None:
        gxapi_cy.WrapSYS.set_loaded_menus(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3._wrapper)
        



    @classmethod
    def get_entitlement_rights(cls, p1: 'GXLST') -> None:
        gxapi_cy.WrapSYS.get_entitlement_rights(GXContext._get_tls_geo(), p1._wrapper)
        




# Misc


    @classmethod
    def generate_guid(cls, p1: str_ref) -> None:
        p1.value = gxapi_cy.WrapSYS.generate_guid(GXContext._get_tls_geo(), p1.value.encode())
        



    @classmethod
    def clipboard_to_file(cls, p1: str) -> None:
        gxapi_cy.WrapSYS.clipboard_to_file(GXContext._get_tls_geo(), p1.encode())
        



    @classmethod
    def create_clipboard_ra(cls) -> 'GXRA':
        ret_val = gxapi_cy.WrapSYS.create_clipboard_ra(GXContext._get_tls_geo())
        return GXRA(ret_val)



    @classmethod
    def create_clipboard_wa(cls) -> 'GXWA':
        ret_val = gxapi_cy.WrapSYS.create_clipboard_wa(GXContext._get_tls_geo())
        return GXWA(ret_val)



    @classmethod
    def emf_object_size(cls, p1: str, p2: float_ref, p3: float_ref) -> None:
        p2.value, p3.value = gxapi_cy.WrapSYS.emf_object_size(GXContext._get_tls_geo(), p1.encode(), p2.value, p3.value)
        



    @classmethod
    def file_to_clipboard(cls, p1: str) -> None:
        gxapi_cy.WrapSYS.file_to_clipboard(GXContext._get_tls_geo(), p1.encode())
        



    @classmethod
    def font_lst(cls, p1: 'GXLST', p2: int) -> None:
        gxapi_cy.WrapSYS.font_lst(GXContext._get_tls_geo(), p1._wrapper, p2)
        



    @classmethod
    def get_dot_net_gx_entries(cls, p1: str, p2: str_ref) -> int:
        ret_val, p2.value = gxapi_cy.WrapSYS.get_dot_net_gx_entries(GXContext._get_tls_geo(), p1.encode(), p2.value.encode())
        return ret_val



    @classmethod
    def send_general_message(cls, p1: str, p2: str) -> None:
        gxapi_cy.WrapSYS.send_general_message(GXContext._get_tls_geo(), p1.encode(), p2.encode())
        



    @classmethod
    def write_debug_log(cls, p1: str) -> None:
        gxapi_cy.WrapSYS.write_debug_log(GXContext._get_tls_geo(), p1.encode())
        



    @classmethod
    def log_script_run(cls, p1: str) -> None:
        gxapi_cy.WrapSYS.log_script_run(GXContext._get_tls_geo(), p1.encode())
        




# Multithreading


    @classmethod
    def get_thread_id(cls) -> int:
        ret_val = gxapi_cy.WrapSYS.get_thread_id(GXContext._get_tls_geo())
        return ret_val



    @classmethod
    def run_multi_user_script(cls, p1: str, p2: int, p3: int, p4: int, p5: int, p6: int) -> None:
        gxapi_cy.WrapSYS.run_multi_user_script(GXContext._get_tls_geo(), p1.encode(), p2, p3, p4, p5, p6)
        




# Parameter


    @classmethod
    def clear_group(cls, p1: str) -> None:
        gxapi_cy.WrapSYS.clear_group(GXContext._get_tls_geo(), p1.encode())
        



    @classmethod
    def clear_group_parm(cls, p1: str) -> None:
        gxapi_cy.WrapSYS.clear_group_parm(GXContext._get_tls_geo(), p1.encode())
        



    @classmethod
    def clear_parm(cls) -> None:
        gxapi_cy.WrapSYS.clear_parm(GXContext._get_tls_geo())
        



    @classmethod
    def default_int(cls, p1: str, p2: str, p3: int) -> None:
        gxapi_cy.WrapSYS.default_int(GXContext._get_tls_geo(), p1.encode(), p2.encode(), p3)
        



    @classmethod
    def default_double(cls, p1: str, p2: str, p3: float) -> None:
        gxapi_cy.WrapSYS.default_double(GXContext._get_tls_geo(), p1.encode(), p2.encode(), p3)
        



    @classmethod
    def default_string(cls, p1: str, p2: str, p3: str) -> None:
        gxapi_cy.WrapSYS.default_string(GXContext._get_tls_geo(), p1.encode(), p2.encode(), p3.encode())
        



    @classmethod
    def get_pattern(cls, p1: str, p2: int_ref, p3: float_ref, p4: int_ref, p5: float_ref, p6: int_ref, p7: int_ref) -> None:
        p2.value, p3.value, p4.value, p5.value, p6.value, p7.value = gxapi_cy.WrapSYS.get_pattern(GXContext._get_tls_geo(), p1.encode(), p2.value, p3.value, p4.value, p5.value, p6.value, p7.value)
        



    @classmethod
    def get_reg(cls, p1: 'GXREG', p2: str) -> None:
        gxapi_cy.WrapSYS.get_reg(GXContext._get_tls_geo(), p1._wrapper, p2.encode())
        



    @classmethod
    def gt_string(cls, p1: str, p2: str, p3: str_ref) -> None:
        p3.value = gxapi_cy.WrapSYS.gt_string(GXContext._get_tls_geo(), p1.encode(), p2.encode(), p3.value.encode())
        



    @classmethod
    def exist_int(cls, p1: str, p2: str) -> int:
        ret_val = gxapi_cy.WrapSYS.exist_int(GXContext._get_tls_geo(), p1.encode(), p2.encode())
        return ret_val



    @classmethod
    def exist_double(cls, p1: str, p2: str) -> int:
        ret_val = gxapi_cy.WrapSYS.exist_double(GXContext._get_tls_geo(), p1.encode(), p2.encode())
        return ret_val



    @classmethod
    def exist_string(cls, p1: str, p2: str) -> int:
        ret_val = gxapi_cy.WrapSYS.exist_string(GXContext._get_tls_geo(), p1.encode(), p2.encode())
        return ret_val



    @classmethod
    def get_int(cls, p1: str, p2: str) -> int:
        ret_val = gxapi_cy.WrapSYS.get_int(GXContext._get_tls_geo(), p1.encode(), p2.encode())
        return ret_val



    @classmethod
    def get_yes_no(cls, p1: str, p2: str) -> int:
        ret_val = gxapi_cy.WrapSYS.get_yes_no(GXContext._get_tls_geo(), p1.encode(), p2.encode())
        return ret_val



    @classmethod
    def replace_string(cls, p1: str, p2: str_ref, p4: str) -> None:
        p2.value = gxapi_cy.WrapSYS.replace_string(GXContext._get_tls_geo(), p1.encode(), p2.value.encode(), p4.encode())
        



    @classmethod
    def load_parm(cls, p1: str, p2: str) -> None:
        gxapi_cy.WrapSYS.load_parm(GXContext._get_tls_geo(), p1.encode(), p2.encode())
        



    @classmethod
    def get_double(cls, p1: str, p2: str) -> float:
        ret_val = gxapi_cy.WrapSYS.get_double(GXContext._get_tls_geo(), p1.encode(), p2.encode())
        return ret_val



    @classmethod
    def save_parm(cls, p1: str, p2: int, p3: str) -> None:
        gxapi_cy.WrapSYS.save_parm(GXContext._get_tls_geo(), p1.encode(), p2, p3.encode())
        



    @classmethod
    def filter_parm_group(cls, p1: str, p2: int) -> None:
        gxapi_cy.WrapSYS.filter_parm_group(GXContext._get_tls_geo(), p1.encode(), p2)
        



    @classmethod
    def set_int(cls, p1: str, p2: str, p3: int) -> None:
        gxapi_cy.WrapSYS.set_int(GXContext._get_tls_geo(), p1.encode(), p2.encode(), p3)
        



    @classmethod
    def set_pattern(cls, p1: str, p2: int, p3: float, p4: int, p5: float, p6: int, p7: int) -> None:
        gxapi_cy.WrapSYS.set_pattern(GXContext._get_tls_geo(), p1.encode(), p2, p3, p4, p5, p6, p7)
        



    @classmethod
    def set_double(cls, p1: str, p2: str, p3: float) -> None:
        gxapi_cy.WrapSYS.set_double(GXContext._get_tls_geo(), p1.encode(), p2.encode(), p3)
        



    @classmethod
    def set_reg(cls, p1: 'GXREG') -> None:
        gxapi_cy.WrapSYS.set_reg(GXContext._get_tls_geo(), p1._wrapper)
        



    @classmethod
    def set_string(cls, p1: str, p2: str, p3: str) -> None:
        gxapi_cy.WrapSYS.set_string(GXContext._get_tls_geo(), p1.encode(), p2.encode(), p3.encode())
        




# Progress Control


    @classmethod
    def check_stop(cls) -> int:
        ret_val = gxapi_cy.WrapSYS.check_stop(GXContext._get_tls_geo())
        return ret_val



    @classmethod
    def prog_state(cls) -> int:
        ret_val = gxapi_cy.WrapSYS.prog_state(GXContext._get_tls_geo())
        return ret_val



    @classmethod
    def prog_name(cls, p1: str, p2: int) -> None:
        gxapi_cy.WrapSYS.prog_name(GXContext._get_tls_geo(), p1.encode(), p2)
        



    @classmethod
    def progress(cls, p1: int) -> None:
        gxapi_cy.WrapSYS.progress(GXContext._get_tls_geo(), p1)
        



    @classmethod
    def prog_update(cls, p1: int) -> None:
        gxapi_cy.WrapSYS.prog_update(GXContext._get_tls_geo(), p1)
        



    @classmethod
    def prog_update_l(cls, p1: int, p2: int) -> None:
        gxapi_cy.WrapSYS.prog_update_l(GXContext._get_tls_geo(), p1, p2)
        




# Registry


    @classmethod
    def get_sys_info(cls, p1: int, p2: str_ref) -> None:
        p2.value = gxapi_cy.WrapSYS.get_sys_info(GXContext._get_tls_geo(), p1, p2.value.encode())
        



    @classmethod
    def registry_get_val(cls, p1: int, p2: str, p3: str, p4: str_ref) -> int:
        ret_val, p4.value = gxapi_cy.WrapSYS.registry_get_val(GXContext._get_tls_geo(), p1, p2.encode(), p3.encode(), p4.value.encode())
        return ret_val



    @classmethod
    def registry_delete_key(cls, p1: int, p2: str) -> int:
        ret_val = gxapi_cy.WrapSYS.registry_delete_key(GXContext._get_tls_geo(), p1, p2.encode())
        return ret_val



    @classmethod
    def registry_delete_val(cls, p1: int, p2: str, p3: str) -> int:
        ret_val = gxapi_cy.WrapSYS.registry_delete_val(GXContext._get_tls_geo(), p1, p2.encode(), p3.encode())
        return ret_val



    @classmethod
    def registry_set_val(cls, p1: int, p2: str, p3: str, p4: str) -> None:
        gxapi_cy.WrapSYS.registry_set_val(GXContext._get_tls_geo(), p1, p2.encode(), p3.encode(), p4.encode())
        




# Temporary File


    @classmethod
    def destroy_ptmp(cls, p1: int) -> None:
        gxapi_cy.WrapSYS.destroy_ptmp(GXContext._get_tls_geo(), p1)
        



    @classmethod
    def get_ptmp(cls, p1: int) -> None:
        gxapi_cy.WrapSYS.get_ptmp(GXContext._get_tls_geo(), p1)
        



    @classmethod
    def save_ptmp(cls, p1: str) -> int:
        ret_val = gxapi_cy.WrapSYS.save_ptmp(GXContext._get_tls_geo(), p1.encode())
        return ret_val




# Termination


    @classmethod
    def abort(cls, p1: str) -> None:
        gxapi_cy.WrapSYS.abort(GXContext._get_tls_geo(), p1.encode())
        



    @classmethod
    def assert_(cls, p1: int) -> None:
        gxapi_cy.WrapSYS.assert_(GXContext._get_tls_geo(), p1)
        



    @classmethod
    def exit_(cls) -> None:
        gxapi_cy.WrapSYS.exit_(GXContext._get_tls_geo())
        



    @classmethod
    def cancel_(cls) -> None:
        gxapi_cy.WrapSYS.cancel_(GXContext._get_tls_geo())
        




# Timing


    @classmethod
    def delay(cls, p1: float) -> int:
        ret_val = gxapi_cy.WrapSYS.delay(GXContext._get_tls_geo(), p1)
        return ret_val



    @classmethod
    def get_timer(cls, p1: int, p2: float_ref, p3: float_ref) -> int:
        ret_val, p2.value, p3.value = gxapi_cy.WrapSYS.get_timer(GXContext._get_tls_geo(), p1, p2.value, p3.value)
        return ret_val




# User Interaction


    @classmethod
    def display_help(cls, p1: str, p2: str) -> None:
        gxapi_cy.WrapSYS.display_help(GXContext._get_tls_geo(), p1.encode(), p2.encode())
        



    @classmethod
    def display_help_topic(cls, p1: str, p2: str) -> None:
        gxapi_cy.WrapSYS.display_help_topic(GXContext._get_tls_geo(), p1.encode(), p2.encode())
        



    @classmethod
    def display_int(cls, p1: str, p2: int) -> None:
        gxapi_cy.WrapSYS.display_int(GXContext._get_tls_geo(), p1.encode(), p2)
        



    @classmethod
    def display_message(cls, p1: str, p2: str) -> None:
        gxapi_cy.WrapSYS.display_message(GXContext._get_tls_geo(), p1.encode(), p2.encode())
        



    @classmethod
    def display_double(cls, p1: str, p2: float) -> None:
        gxapi_cy.WrapSYS.display_double(GXContext._get_tls_geo(), p1.encode(), p2)
        



    @classmethod
    def display_question(cls, p1: str, p2: str) -> int:
        ret_val = gxapi_cy.WrapSYS.display_question(GXContext._get_tls_geo(), p1.encode(), p2.encode())
        return ret_val



    @classmethod
    def display_question_with_cancel(cls, p1: str, p2: str) -> int:
        ret_val = gxapi_cy.WrapSYS.display_question_with_cancel(GXContext._get_tls_geo(), p1.encode(), p2.encode())
        return ret_val



    @classmethod
    def display_task_dialog_ui(cls, p1: str, p2: str, p3: str, p4: int, p5: 'GXLST', p6: int, p7: str, p8: int, p9: str, p10: int_ref, p11: str, p12: str, p13: str) -> int:
        ret_val, p10.value = gxapi_cy.WrapSYS.display_task_dialog_ui(GXContext._get_tls_geo(), p1.encode(), p2.encode(), p3.encode(), p4, p5._wrapper, p6, p7.encode(), p8, p9.encode(), p10.value, p11.encode(), p12.encode(), p13.encode())
        return ret_val



    @classmethod
    def interactive(cls) -> int:
        ret_val = gxapi_cy.WrapSYS.interactive(GXContext._get_tls_geo())
        return ret_val



    @classmethod
    def prompt(cls, p1: str, p2: str_ref) -> int:
        ret_val, p2.value = gxapi_cy.WrapSYS.prompt(GXContext._get_tls_geo(), p1.encode(), p2.value.encode())
        return ret_val



    @classmethod
    def script(cls) -> int:
        ret_val = gxapi_cy.WrapSYS.script(GXContext._get_tls_geo())
        return ret_val



    @classmethod
    def script_record(cls) -> int:
        ret_val = gxapi_cy.WrapSYS.script_record(GXContext._get_tls_geo())
        return ret_val



    @classmethod
    def set_cursor(cls, p1: str) -> None:
        gxapi_cy.WrapSYS.set_cursor(GXContext._get_tls_geo(), p1.encode())
        



    @classmethod
    def set_info_line(cls, p1: str) -> None:
        gxapi_cy.WrapSYS.set_info_line(GXContext._get_tls_geo(), p1.encode())
        



    @classmethod
    def set_interactive(cls, p1: int) -> None:
        gxapi_cy.WrapSYS.set_interactive(GXContext._get_tls_geo(), p1)
        




# Workspace


    @classmethod
    def get_workspace_reg(cls, p1: 'GXREG') -> None:
        gxapi_cy.WrapSYS.get_workspace_reg(GXContext._get_tls_geo(), p1._wrapper)
        



    @classmethod
    def set_workspace_reg(cls, p1: 'GXREG') -> None:
        gxapi_cy.WrapSYS.set_workspace_reg(GXContext._get_tls_geo(), p1._wrapper)
        




# String Encryption


    @classmethod
    def encrypt_string(cls, p1: str, p2: str_ref, p4: int) -> None:
        p2.value = gxapi_cy.WrapSYS.encrypt_string(GXContext._get_tls_geo(), p1.encode(), p2.value.encode(), p4)
        



    @classmethod
    def decrypt_string(cls, p1: str, p2: str_ref, p4: int) -> None:
        p2.value = gxapi_cy.WrapSYS.decrypt_string(GXContext._get_tls_geo(), p1.encode(), p2.value.encode(), p4)
        



    @classmethod
    def is_encrypted_string(cls, p1: str) -> int:
        ret_val = gxapi_cy.WrapSYS.is_encrypted_string(GXContext._get_tls_geo(), p1.encode())
        return ret_val




# GX Debugger


    @classmethod
    def disable_gx_debugger(cls) -> None:
        gxapi_cy.WrapSYS.disable_gx_debugger(GXContext._get_tls_geo())
        



    @classmethod
    def enable_gx_debugger(cls, p1: str, p2: str) -> None:
        gxapi_cy.WrapSYS.enable_gx_debugger(GXContext._get_tls_geo(), p1.encode(), p2.encode())
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer