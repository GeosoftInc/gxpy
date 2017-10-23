### extends 'class_empty.py'
from . import gxapi_cy

from geosoft.gxapi import GXContext, int_ref, float_ref, str_ref

### block Header
# NOTICE: The code generator will not replace the code in this block
### endblock Header

### block ClassImplementation
# NOTICE: Do not edit anything here, it is generated code
class GXGUI:
    """
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._wrapper = None

    def __del__(self):
        self._wrapper = None

    def __init__(self, wrapper=None):
        self._wrapper = wrapper if wrapper else gxapi_cy.WrapGUI(0)

    @classmethod
    def null(cls) -> 'GXGUI':
        """
        A null (undefined) instance of :class:`GXGUI`
        
        :returns: A null :class:`GX3DN`
        """
        return cls()

    def is_null(self) -> bool:
        """
        Check if the instance of :class:`GXGUI` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of :class:`GXGUI`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Miscellaneous


    @classmethod
    def create_wnd_from_hwnd(cls, p1: int) -> int:
        ret_val = gxapi_cy.WrapGUI.create_wnd_from_hwnd(GXContext._get_tls_geo())
        return ret_val



    @classmethod
    def fft2_spec_filter(cls, p1: str, p2: str) -> None:
        gxapi_cy.WrapGUI.fft2_spec_filter(GXContext._get_tls_geo(), p2.encode())
        



    @classmethod
    def get_parent_wnd(cls) -> int:
        ret_val = gxapi_cy.WrapGUI.get_parent_wnd(GXContext._get_tls_geo())
        return ret_val



    @classmethod
    def get_printer_lst(cls, p1: 'GXLST') -> None:
        gxapi_cy.WrapGUI.get_printer_lst(GXContext._get_tls_geo())
        



    @classmethod
    def get_window_state(cls) -> int:
        ret_val = gxapi_cy.WrapGUI.get_window_state(GXContext._get_tls_geo())
        return ret_val



    @classmethod
    def set_window_state(cls, p1: int) -> None:
        gxapi_cy.WrapGUI.set_window_state(GXContext._get_tls_geo())
        



    @classmethod
    def get_window_position(cls, p1: int_ref, p2: int_ref, p3: int_ref, p4: int_ref, p5: int_ref) -> None:
        p1.value, p2.value, p3.value, p4.value, p5.value = gxapi_cy.WrapGUI.get_window_position(GXContext._get_tls_geo(), p2.value, p3.value, p4.value, p5.value)
        



    @classmethod
    def set_window_position(cls, p1: int, p2: int, p3: int, p4: int, p5: int) -> None:
        gxapi_cy.WrapGUI.set_window_position(GXContext._get_tls_geo(), p2, p3, p4, p5)
        



    @classmethod
    def get_client_window_area(cls, p1: int_ref, p2: int_ref, p3: int_ref, p4: int_ref) -> None:
        p1.value, p2.value, p3.value, p4.value = gxapi_cy.WrapGUI.get_client_window_area(GXContext._get_tls_geo(), p2.value, p3.value, p4.value)
        



    @classmethod
    def grid_stat_hist(cls, p1: str) -> None:
        gxapi_cy.WrapGUI.grid_stat_hist(GXContext._get_tls_geo())
        



    @classmethod
    def voxel_stat_hist(cls, p1: str) -> None:
        gxapi_cy.WrapGUI.voxel_stat_hist(GXContext._get_tls_geo())
        



    @classmethod
    def color_form(cls, p1: int_ref, p2: int) -> int:
        ret_val, p1.value = gxapi_cy.WrapGUI.color_form(GXContext._get_tls_geo(), p2)
        return ret_val



    @classmethod
    def color_transform(cls, p1: 'GXITR', p2: 'GXST') -> int:
        ret_val = gxapi_cy.WrapGUI.color_transform(GXContext._get_tls_geo(), p2)
        return ret_val



    @classmethod
    def coord_sys_wizard(cls, p1: 'GXIPJ', p2: int, p3: int, p4: str, p5: str) -> int:
        ret_val = gxapi_cy.WrapGUI.coord_sys_wizard(GXContext._get_tls_geo(), p2, p3, p4.encode(), p5.encode())
        return ret_val



    @classmethod
    def coord_sys_wizard_licensed(cls, p1: 'GXIPJ', p2: int, p3: int, p4: str, p5: str) -> int:
        ret_val = gxapi_cy.WrapGUI.coord_sys_wizard_licensed(GXContext._get_tls_geo(), p2, p3, p4.encode(), p5.encode())
        return ret_val



    @classmethod
    def coord_sys_wizard_grid(cls, p1: 'GXIPJ', p2: 'GXIPJ', p3: int, p4: int, p5: str, p6: str, p7: int, p8: int, p9: float_ref, p10: float_ref, p11: float_ref, p12: float_ref, p13: float_ref) -> int:
        ret_val, p9.value, p10.value, p11.value, p12.value, p13.value = gxapi_cy.WrapGUI.coord_sys_wizard_grid(GXContext._get_tls_geo(), p2, p3, p4, p5.encode(), p6.encode(), p7, p8, p9.value, p10.value, p11.value, p12.value, p13.value)
        return ret_val



    @classmethod
    def database_type(cls, p1: str, p2: str_ref) -> int:
        ret_val, p2.value = gxapi_cy.WrapGUI.database_type(GXContext._get_tls_geo(), p2.value.encode())
        return ret_val



    @classmethod
    def datamine_type(cls, p1: str, p2: int_ref) -> int:
        ret_val, p2.value = gxapi_cy.WrapGUI.datamine_type(GXContext._get_tls_geo(), p2.value)
        return ret_val



    @classmethod
    def export_xyz_template_editor(cls, p1: 'GXDB', p2: str, p3: int) -> int:
        ret_val = gxapi_cy.WrapGUI.export_xyz_template_editor(GXContext._get_tls_geo(), p2.encode(), p3)
        return ret_val



    @classmethod
    def export_xyz_template_editor_ex(cls, p1: 'GXEDB', p2: str_ref) -> int:
        ret_val, p2.value = gxapi_cy.WrapGUI.export_xyz_template_editor_ex(GXContext._get_tls_geo(), p2.value.encode())
        return ret_val



    @classmethod
    def file_filter_index(cls, p1: str) -> int:
        ret_val = gxapi_cy.WrapGUI.file_filter_index(GXContext._get_tls_geo())
        return ret_val



    @classmethod
    def gcs_datum_warning_shp(cls, p1: str, p2: 'GXIPJ') -> int:
        ret_val = gxapi_cy.WrapGUI.gcs_datum_warning_shp(GXContext._get_tls_geo(), p2)
        return ret_val



    @classmethod
    def gcs_datum_warning_shpdb_ex(cls, p1: 'GXLST', p2: 'GXLST', p3: 'GXLST', p4: 'GXDB') -> int:
        ret_val = gxapi_cy.WrapGUI.gcs_datum_warning_shpdb_ex(GXContext._get_tls_geo(), p2, p3, p4)
        return ret_val



    @classmethod
    def gcs_datum_warning_shp_ex(cls, p1: 'GXLST', p2: 'GXLST', p3: 'GXLST', p4: 'GXMVIEW') -> int:
        ret_val = gxapi_cy.WrapGUI.gcs_datum_warning_shp_ex(GXContext._get_tls_geo(), p2, p3, p4)
        return ret_val



    @classmethod
    def get_area_of_interest(cls, p1: float_ref, p2: float_ref, p3: float_ref, p4: float_ref, p5: 'GXPLY', p6: 'GXIPJ') -> int:
        ret_val, p1.value, p2.value, p3.value, p4.value = gxapi_cy.WrapGUI.get_area_of_interest(GXContext._get_tls_geo(), p2.value, p3.value, p4.value, p5, p6)
        return ret_val



    @classmethod
    def get_area_of_interest_3d(cls, p1: float_ref, p2: float_ref, p3: float_ref, p4: float_ref, p5: float_ref, p6: float_ref, p7: 'GXPLY', p8: 'GXIPJ') -> int:
        ret_val, p1.value, p2.value, p3.value, p4.value, p5.value, p6.value = gxapi_cy.WrapGUI.get_area_of_interest_3d(GXContext._get_tls_geo(), p2.value, p3.value, p4.value, p5.value, p6.value, p7, p8)
        return ret_val



    @classmethod
    def get_dat_defaults(cls, p1: int, p2: int, p3: str_ref, p5: str_ref) -> None:
        p3.value, p5.value = gxapi_cy.WrapGUI.get_dat_defaults(GXContext._get_tls_geo(), p2, p3.value.encode(), p5.value.encode())
        



    @classmethod
    def get_file_filter(cls, p1: int, p2: str_ref, p4: str_ref, p6: str_ref, p8: int_ref) -> None:
        p2.value, p4.value, p6.value, p8.value = gxapi_cy.WrapGUI.get_file_filter(GXContext._get_tls_geo(), p2.value.encode(), p4.value.encode(), p6.value.encode(), p8.value)
        



    @classmethod
    def get_gs_directory(cls, p1: int, p2: str_ref) -> None:
        p2.value = gxapi_cy.WrapGUI.get_gs_directory(GXContext._get_tls_geo(), p2.value.encode())
        



    @classmethod
    def browse_dir(cls, p1: str, p2: str, p3: str_ref) -> int:
        ret_val, p3.value = gxapi_cy.WrapGUI.browse_dir(GXContext._get_tls_geo(), p2.encode(), p3.value.encode())
        return ret_val



    @classmethod
    def color_transform_ex(cls, p1: 'GXITR', p2: 'GXST', p3: int, p4: int, p5: str_ref) -> int:
        ret_val, p5.value = gxapi_cy.WrapGUI.color_transform_ex(GXContext._get_tls_geo(), p2, p3, p4, p5.value.encode())
        return ret_val



    @classmethod
    def cumulative_percent(cls, p1: str_ref, p3: 'GXITR') -> int:
        ret_val, p1.value = gxapi_cy.WrapGUI.cumulative_percent(GXContext._get_tls_geo(), p3)
        return ret_val



    @classmethod
    def dat_file_form(cls, p1: str, p2: str, p3: str_ref, p5: int, p6: int, p7: int) -> int:
        ret_val, p3.value = gxapi_cy.WrapGUI.dat_file_form(GXContext._get_tls_geo(), p2.encode(), p3.value.encode(), p5, p6, p7)
        return ret_val



    @classmethod
    def gen_file_form(cls, p1: str, p2: 'GXVV', p3: int, p4: str, p5: str_ref, p7: int, p8: int) -> int:
        ret_val, p5.value = gxapi_cy.WrapGUI.gen_file_form(GXContext._get_tls_geo(), p2, p3, p4.encode(), p5.value.encode(), p7, p8)
        return ret_val



    @classmethod
    def custom_file_form(cls, p1: str, p2: str, p3: str, p4: str_ref, p6: int, p7: int) -> int:
        ret_val, p4.value = gxapi_cy.WrapGUI.custom_file_form(GXContext._get_tls_geo(), p2.encode(), p3.encode(), p4.value.encode(), p6, p7)
        return ret_val



    @classmethod
    def import_drill_database_ado2(cls, p1: str, p2: str_ref, p4: str_ref, p6: int_ref, p7: 'GXREG') -> int:
        ret_val, p2.value, p4.value, p6.value = gxapi_cy.WrapGUI.import_drill_database_ado2(GXContext._get_tls_geo(), p2.value.encode(), p4.value.encode(), p6.value, p7)
        return ret_val



    @classmethod
    def import_drill_database_esri(cls, p1: str, p2: str_ref, p4: str_ref, p6: int_ref, p7: int, p8: 'GXREG') -> int:
        ret_val, p2.value, p4.value, p6.value = gxapi_cy.WrapGUI.import_drill_database_esri(GXContext._get_tls_geo(), p2.value.encode(), p4.value.encode(), p6.value, p7, p8)
        return ret_val



    @classmethod
    def import_drill_database_odbc(cls, p1: str_ref, p3: str_ref, p5: str_ref, p7: int_ref, p8: 'GXREG') -> int:
        ret_val, p1.value, p3.value, p5.value, p7.value = gxapi_cy.WrapGUI.import_drill_database_odbc(GXContext._get_tls_geo(), p3.value.encode(), p5.value.encode(), p7.value, p8)
        return ret_val



    @classmethod
    def import_drill_database_odbc_maxwell(cls, p1: str_ref, p3: str_ref, p5: str_ref, p7: int_ref, p8: 'GXREG') -> int:
        ret_val, p1.value, p3.value, p5.value, p7.value = gxapi_cy.WrapGUI.import_drill_database_odbc_maxwell(GXContext._get_tls_geo(), p3.value.encode(), p5.value.encode(), p7.value, p8)
        return ret_val



    @classmethod
    def import_ascii_wizard(cls, p1: str, p2: str) -> int:
        ret_val = gxapi_cy.WrapGUI.import_ascii_wizard(GXContext._get_tls_geo(), p2.encode())
        return ret_val



    @classmethod
    def import_chem_database(cls, p1: str, p2: str, p3: str_ref, p5: int) -> int:
        ret_val, p3.value = gxapi_cy.WrapGUI.import_chem_database(GXContext._get_tls_geo(), p2.encode(), p3.value.encode(), p5)
        return ret_val



    @classmethod
    def import_chem_database_ado(cls, p1: str, p2: str, p3: str_ref, p5: int) -> int:
        ret_val, p3.value = gxapi_cy.WrapGUI.import_chem_database_ado(GXContext._get_tls_geo(), p2.encode(), p3.value.encode(), p5)
        return ret_val



    @classmethod
    def import_database(cls, p1: str, p2: str, p3: str_ref) -> int:
        ret_val, p3.value = gxapi_cy.WrapGUI.import_database(GXContext._get_tls_geo(), p2.encode(), p3.value.encode())
        return ret_val



    @classmethod
    def import_database_ado(cls, p1: str, p2: str, p3: str_ref) -> int:
        ret_val, p3.value = gxapi_cy.WrapGUI.import_database_ado(GXContext._get_tls_geo(), p2.encode(), p3.value.encode())
        return ret_val



    @classmethod
    def import_database_sql(cls, p1: str, p2: str, p3: str, p4: str_ref) -> int:
        ret_val, p4.value = gxapi_cy.WrapGUI.import_database_sql(GXContext._get_tls_geo(), p2.encode(), p3.encode(), p4.value.encode())
        return ret_val



    @classmethod
    def import_database_sqlado(cls, p1: str, p2: str, p3: str, p4: str_ref) -> int:
        ret_val, p4.value = gxapi_cy.WrapGUI.import_database_sqlado(GXContext._get_tls_geo(), p2.encode(), p3.encode(), p4.value.encode())
        return ret_val



    @classmethod
    def import_drill_database_ado(cls, p1: str, p2: str, p3: str_ref, p5: int_ref, p6: 'GXREG') -> int:
        ret_val, p3.value, p5.value = gxapi_cy.WrapGUI.import_drill_database_ado(GXContext._get_tls_geo(), p2.encode(), p3.value.encode(), p5.value, p6)
        return ret_val



    @classmethod
    def import_template_sql(cls, p1: str, p2: str, p3: str, p4: str) -> int:
        ret_val = gxapi_cy.WrapGUI.import_template_sql(GXContext._get_tls_geo(), p2.encode(), p3.encode(), p4.encode())
        return ret_val



    @classmethod
    def import_template_sqlado(cls, p1: str, p2: str, p3: str, p4: str) -> int:
        ret_val = gxapi_cy.WrapGUI.import_template_sqlado(GXContext._get_tls_geo(), p2.encode(), p3.encode(), p4.encode())
        return ret_val



    @classmethod
    def import_xyz_template_editor(cls, p1: 'GXDB', p2: str, p3: int, p4: str) -> int:
        ret_val = gxapi_cy.WrapGUI.import_xyz_template_editor(GXContext._get_tls_geo(), p2.encode(), p3, p4.encode())
        return ret_val



    @classmethod
    def odbc_file_connect(cls, p1: str, p2: str_ref, p4: int, p5: str_ref) -> int:
        ret_val, p2.value, p5.value = gxapi_cy.WrapGUI.odbc_file_connect(GXContext._get_tls_geo(), p2.value.encode(), p4, p5.value.encode())
        return ret_val



    @classmethod
    def symbol_form(cls, p1: str_ref, p3: int_ref, p4: int_ref, p5: int_ref, p6: float_ref, p7: float_ref, p8: int_ref, p9: int_ref) -> int:
        ret_val, p1.value, p3.value, p4.value, p5.value, p6.value, p7.value, p8.value, p9.value = gxapi_cy.WrapGUI.symbol_form(GXContext._get_tls_geo(), p3.value, p4.value, p5.value, p6.value, p7.value, p8.value, p9.value)
        return ret_val



    @classmethod
    def meta_data_tool(cls, p1: 'GXMETA', p2: int, p3: int) -> int:
        ret_val = gxapi_cy.WrapGUI.meta_data_tool(GXContext._get_tls_geo(), p2, p3)
        return ret_val



    @classmethod
    def import_chem_wizard(cls, p1: str, p2: str, p3: int) -> None:
        gxapi_cy.WrapGUI.import_chem_wizard(GXContext._get_tls_geo(), p2.encode(), p3)
        



    @classmethod
    def import_drill_wizard(cls, p1: str, p2: str, p3: str, p4: int, p5: int_ref, p6: 'GXREG') -> None:
        p5.value = gxapi_cy.WrapGUI.import_drill_wizard(GXContext._get_tls_geo(), p2.encode(), p3.encode(), p4, p5.value, p6)
        



    @classmethod
    def internet_trust(cls) -> None:
        gxapi_cy.WrapGUI.internet_trust(GXContext._get_tls_geo())
        



    @classmethod
    def pattern_form(cls, p1: int_ref, p2: float_ref, p3: int_ref, p4: float_ref, p5: int_ref, p6: int_ref) -> int:
        ret_val, p1.value, p2.value, p3.value, p4.value, p5.value, p6.value = gxapi_cy.WrapGUI.pattern_form(GXContext._get_tls_geo(), p2.value, p3.value, p4.value, p5.value, p6.value)
        return ret_val



    @classmethod
    def line_pattern_form(cls, p1: int_ref, p2: float_ref, p3: float_ref, p4: int_ref) -> int:
        ret_val, p1.value, p2.value, p3.value, p4.value = gxapi_cy.WrapGUI.line_pattern_form(GXContext._get_tls_geo(), p2.value, p3.value, p4.value)
        return ret_val



    @classmethod
    def two_panel_selection(cls, p1: 'GXLST', p2: 'GXLST', p3: str) -> int:
        ret_val = gxapi_cy.WrapGUI.two_panel_selection(GXContext._get_tls_geo(), p2, p3.encode())
        return ret_val



    @classmethod
    def two_panel_selection2(cls, p1: 'GXLST', p2: 'GXLST', p3: str) -> int:
        ret_val = gxapi_cy.WrapGUI.two_panel_selection2(GXContext._get_tls_geo(), p2, p3.encode())
        return ret_val



    @classmethod
    def two_panel_selection_ex(cls, p1: 'GXLST', p2: 'GXLST', p3: int, p4: int, p5: str) -> int:
        ret_val = gxapi_cy.WrapGUI.two_panel_selection_ex(GXContext._get_tls_geo(), p2, p3, p4, p5.encode())
        return ret_val



    @classmethod
    def two_panel_selection_ex2(cls, p1: 'GXLST', p2: 'GXLST', p3: int, p4: int, p5: str, p6: str) -> int:
        ret_val = gxapi_cy.WrapGUI.two_panel_selection_ex2(GXContext._get_tls_geo(), p2, p3, p4, p5.encode(), p6.encode())
        return ret_val



    @classmethod
    def launch_single_geo_dotnetx_tool(cls, p1: str, p2: str, p3: 'GXMETA') -> None:
        gxapi_cy.WrapGUI.launch_single_geo_dotnetx_tool(GXContext._get_tls_geo(), p2.encode(), p3)
        



    @classmethod
    def launch_geo_dotnetx_tool(cls, p1: str, p2: str, p3: 'GXMETA') -> None:
        gxapi_cy.WrapGUI.launch_geo_dotnetx_tool(GXContext._get_tls_geo(), p2.encode(), p3)
        



    @classmethod
    def launch_geo_x_tool(cls, p1: str, p2: str, p3: 'GXMETA') -> None:
        gxapi_cy.WrapGUI.launch_geo_x_tool(GXContext._get_tls_geo(), p2.encode(), p3)
        



    @classmethod
    def launch_single_geo_dotnetx_tool_ex(cls, p1: str, p2: str, p3: 'GXMETA', p4: int, p5: int, p6: int, p7: int) -> None:
        gxapi_cy.WrapGUI.launch_single_geo_dotnetx_tool_ex(GXContext._get_tls_geo(), p2.encode(), p3, p4, p5, p6, p7)
        



    @classmethod
    def launch_geo_dotnetx_tool_ex(cls, p1: str, p2: str, p3: 'GXMETA', p4: int, p5: int, p6: int, p7: int) -> None:
        gxapi_cy.WrapGUI.launch_geo_dotnetx_tool_ex(GXContext._get_tls_geo(), p2.encode(), p3, p4, p5, p6, p7)
        



    @classmethod
    def launch_geo_x_tool_ex(cls, p1: str, p2: str, p3: 'GXMETA', p4: int, p5: int, p6: int, p7: int) -> None:
        gxapi_cy.WrapGUI.launch_geo_x_tool_ex(GXContext._get_tls_geo(), p2.encode(), p3, p4, p5, p6, p7)
        



    @classmethod
    def meta_data_viewer(cls, p1: 'GXMETA', p2: int, p3: int) -> None:
        gxapi_cy.WrapGUI.meta_data_viewer(GXContext._get_tls_geo(), p2, p3)
        



    @classmethod
    def print_file(cls, p1: str) -> None:
        gxapi_cy.WrapGUI.print_file(GXContext._get_tls_geo())
        



    @classmethod
    def render_pattern(cls, p1: int, p2: int, p3: int, p4: int, p5: int, p6: int, p7: float, p8: int, p9: float, p10: int, p11: int, p12: int, p13: int, p14: int) -> None:
        gxapi_cy.WrapGUI.render_pattern(GXContext._get_tls_geo(), p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14)
        



    @classmethod
    def render_line_pattern(cls, p1: int, p2: int, p3: int, p4: int, p5: int, p6: int, p7: float, p8: float, p9: int, p10: int, p11: int, p12: int) -> None:
        gxapi_cy.WrapGUI.render_line_pattern(GXContext._get_tls_geo(), p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12)
        



    @classmethod
    def set_parent_wnd(cls, p1: int) -> None:
        gxapi_cy.WrapGUI.set_parent_wnd(GXContext._get_tls_geo())
        



    @classmethod
    def set_printer(cls, p1: str) -> None:
        gxapi_cy.WrapGUI.set_printer(GXContext._get_tls_geo())
        



    @classmethod
    def set_prog_always_on(cls, p1: int) -> None:
        gxapi_cy.WrapGUI.set_prog_always_on(GXContext._get_tls_geo())
        



    @classmethod
    def show_direct_hist(cls, p1: float, p2: float, p3: float, p4: float, p5: float, p6: int, p7: 'GXVV') -> None:
        gxapi_cy.WrapGUI.show_direct_hist(GXContext._get_tls_geo(), p2, p3, p4, p5, p6, p7)
        



    @classmethod
    def show_hist(cls, p1: 'GXST') -> None:
        gxapi_cy.WrapGUI.show_hist(GXContext._get_tls_geo())
        



    @classmethod
    def simple_map_dialog(cls, p1: 'GXMAP', p2: str, p3: str) -> None:
        gxapi_cy.WrapGUI.simple_map_dialog(GXContext._get_tls_geo(), p2.encode(), p3.encode())
        



    @classmethod
    def thematic_voxel_info(cls, p1: 'GXVOX') -> None:
        gxapi_cy.WrapGUI.thematic_voxel_info(GXContext._get_tls_geo())
        



    @classmethod
    def show_3d_viewer_dialog(cls, p1: str, p2: str) -> None:
        gxapi_cy.WrapGUI.show_3d_viewer_dialog(GXContext._get_tls_geo(), p2.encode())
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer