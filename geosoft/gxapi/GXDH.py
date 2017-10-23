### extends 'class_empty.py'
from . import gxapi_cy

from geosoft.gxapi import GXContext, int_ref, float_ref, str_ref

### block Header
# NOTICE: The code generator will not replace the code in this block
### endblock Header

### block ClassImplementation
# NOTICE: Do not edit anything here, it is generated code
class GXDH:
    """
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._wrapper = None

    def __del__(self):
        self._wrapper = None

    def __init__(self, wrapper=None):
        self._wrapper = wrapper if wrapper else gxapi_cy.WrapDH(0)

    @classmethod
    def null(cls) -> 'GXDH':
        """
        A null (undefined) instance of :class:`GXDH`
        
        :returns: A null :class:`GX3DN`
        """
        return cls()

    def is_null(self) -> bool:
        """
        Check if the instance of :class:`GXDH` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of :class:`GXDH`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# ArcGIS Target Functions


    @classmethod
    def is_esri(cls) -> int:
        ret_val = gxapi_cy.WrapDH.is_esri(GXContext._get_tls_geo())
        return ret_val




# Data processing/conversion methods



    def creat_chan_lst(self, p2: 'GXLST') -> None:
        self._wrapper.creat_chan_lst(p2)
        




    def depth_data_lst(self, p2: 'GXLST') -> None:
        self._wrapper.depth_data_lst(p2)
        




    def from_to_data_lst(self, p2: str, p3: 'GXLST') -> None:
        self._wrapper.from_to_data_lst(p2.encode(), p3)
        




    def get_geology_contacts(self, p2: 'GXLST', p3: str, p4: str, p5: int, p6: float, p7: 'GXVV', p8: 'GXVV', p9: 'GXVV') -> None:
        self._wrapper.get_geology_contacts(p2, p3.encode(), p4.encode(), p5, p6, p7, p8, p9)
        




    def get_oriented_core_dip_dir(self, p2: 'GXLST', p3: str, p4: str, p5: int, p6: str, p7: str) -> None:
        self._wrapper.get_oriented_core_dip_dir(p2, p3.encode(), p4.encode(), p5, p6.encode(), p7.encode())
        




    def get_unique_channel_items(self, p2: str, p3: int, p4: 'GXVV') -> None:
        self._wrapper.get_unique_channel_items(p2.encode(), p3, p4)
        




    def get_unique_channel_items_from_collar(self, p2: str, p3: int, p4: 'GXVV') -> None:
        self._wrapper.get_unique_channel_items_from_collar(p2.encode(), p3, p4)
        




    def chan_type(self, p2: str) -> int:
        ret_val = self._wrapper.chan_type(p2.encode())
        return ret_val




    def find_hole_intersection(self, p2: int, p3: 'GXIMG', p4: float_ref, p5: float_ref, p6: float_ref) -> int:
        ret_val, p4.value, p5.value, p6.value = self._wrapper.find_hole_intersection(p2, p3, p4.value, p5.value, p6.value)
        return ret_val




    def get_chan_code_info(self, p2: str, p3: int_ref, p4: str_ref) -> None:
        p3.value, p4.value = self._wrapper.get_chan_code_info(p2.encode(), p3.value, p4.value.encode())
        




    def grid_intersection(self, p2: float, p3: float, p4: float, p5: float, p6: float, p7: str, p8: float_ref, p9: float_ref, p10: float_ref) -> int:
        ret_val, p8.value, p9.value, p10.value = self._wrapper.grid_intersection(p2, p3, p4, p5, p6, p7.encode(), p8.value, p9.value, p10.value)
        return ret_val




    def litho_grid_3d(self, p2: str, p3: 'GXTPAT', p4: str, p5: float, p6: float, p7: float, p8: int, p9: 'GXREG', p10: int) -> None:
        self._wrapper.litho_grid_3d(p2.encode(), p3, p4.encode(), p5, p6, p7, p8, p9, p10)
        




    def numeric_chan_lst(self, p2: 'GXLST') -> None:
        self._wrapper.numeric_chan_lst(p2)
        




    def numeric_from_to_data_lst(self, p2: str, p3: 'GXLST') -> None:
        self._wrapper.numeric_from_to_data_lst(p2.encode(), p3)
        




    def punch_grid_holes(self, p2: 'GXIMG', p3: 'GXVV', p4: 'GXVV', p5: 'GXVV', p6: float) -> None:
        self._wrapper.punch_grid_holes(p2, p3, p4, p5, p6)
        




    def string_chan_lst(self, p2: 'GXLST') -> None:
        self._wrapper.string_chan_lst(p2)
        




    def string_from_to_data_lst(self, p2: str, p3: 'GXLST') -> None:
        self._wrapper.string_from_to_data_lst(p2.encode(), p3)
        




# Miscellaneous



    def h_assay_db(self, p2: int) -> 'GXDB':
        ret_val = self._wrapper.h_assay_db(p2)
        return GXDB(ret_val)




    def h_assay_symb(self, p2: int, p3: int) -> int:
        ret_val = self._wrapper.h_assay_symb(p2, p3)
        return ret_val




    def h_collar_db(self) -> 'GXDB':
        ret_val = self._wrapper.h_collar_db()
        return GXDB(ret_val)




    def h_collar_symb(self) -> int:
        ret_val = self._wrapper.h_collar_symb()
        return ret_val




    def h_dip_az_survey_db(self) -> 'GXDB':
        ret_val = self._wrapper.h_dip_az_survey_db()
        return GXDB(ret_val)




    def h_dip_az_survey_symb(self, p2: int) -> int:
        ret_val = self._wrapper.h_dip_az_survey_symb(p2)
        return ret_val




    def h_en_survey_db(self) -> 'GXDB':
        ret_val = self._wrapper.h_en_survey_db()
        return GXDB(ret_val)




    def h_en_survey_symb(self, p2: int) -> int:
        ret_val = self._wrapper.h_en_survey_symb(p2)
        return ret_val




    def add_survey_table(self, p2: int) -> None:
        self._wrapper.add_survey_table(p2)
        




    def assay_hole_lst(self, p2: int, p3: 'GXLST') -> None:
        self._wrapper.assay_hole_lst(p2, p3)
        




    def assay_lst(self, p2: 'GXLST') -> None:
        self._wrapper.assay_lst(p2)
        



    @classmethod
    def auto_select_holes(cls, p1: int) -> None:
        gxapi_cy.WrapDH.auto_select_holes(GXContext._get_tls_geo())
        




    def clean(self) -> None:
        self._wrapper.clean()
        




    def composite_db(self, p2: 'GXDB', p3: 'GXDB', p4: int, p5: int, p6: float, p7: str, p8: str, p9: str, p10: float, p11: float, p12: float, p13: int, p14: str) -> None:
        self._wrapper.composite_db(p2, p3, p4, p5, p6, p7.encode(), p8.encode(), p9.encode(), p10, p11, p12, p13, p14.encode())
        




    def compute_hole_xyz(self, p2: int) -> None:
        self._wrapper.compute_hole_xyz(p2)
        




    def compute_sel_extent(self, p2: float_ref, p3: float_ref, p4: float_ref, p5: float_ref, p6: float_ref, p7: float_ref) -> None:
        p2.value, p3.value, p4.value, p5.value, p6.value, p7.value = self._wrapper.compute_sel_extent(p2.value, p3.value, p4.value, p5.value, p6.value, p7.value)
        




    def compute_xyz(self) -> None:
        self._wrapper.compute_xyz()
        



    @classmethod
    def convert_old_line_names(cls, p1: 'GXDB', p2: 'GXLST') -> None:
        gxapi_cy.WrapDH.convert_old_line_names(GXContext._get_tls_geo(), p2)
        



    @classmethod
    def create(cls, p1: str) -> 'GXDH':
        ret_val = gxapi_cy.WrapDH.create(GXContext._get_tls_geo())
        return GXDH(ret_val)




    def create_default_job(self, p2: str, p3: int) -> None:
        self._wrapper.create_default_job(p2.encode(), p3)
        



    @classmethod
    def create_external(cls, p1: str) -> 'GXDH':
        ret_val = gxapi_cy.WrapDH.create_external(GXContext._get_tls_geo())
        return GXDH(ret_val)



    @classmethod
    def current(cls) -> 'GXDH':
        ret_val = gxapi_cy.WrapDH.current(GXContext._get_tls_geo())
        return GXDH(ret_val)



    @classmethod
    def datamine_to_csv(cls, p1: str, p2: str) -> None:
        gxapi_cy.WrapDH.datamine_to_csv(GXContext._get_tls_geo(), p2.encode())
        




    def delete_holes(self, p2: 'GXLST') -> None:
        self._wrapper.delete_holes(p2)
        






    def export(self, p2: str, p3: int) -> None:
        self._wrapper.export(p2.encode(), p3)
        




    def export_geodatabase_lst(self, p2: 'GXLST', p3: str, p4: str, p5: str_ref, p7: int) -> None:
        p5.value = self._wrapper.export_geodatabase_lst(p2, p3.encode(), p4.encode(), p5.value.encode(), p7)
        




    def export_las(self, p2: int, p3: int, p4: float, p5: str) -> None:
        self._wrapper.export_las(p2, p3, p4, p5.encode())
        




    def export_lst(self, p2: 'GXLST', p3: str, p4: int) -> None:
        self._wrapper.export_lst(p2, p3.encode(), p4)
        




    def flush_select(self) -> None:
        self._wrapper.flush_select()
        




    def get_databases_vv(self, p2: 'GXVV') -> None:
        self._wrapper.get_databases_vv(p2)
        




    def get_databases_sorted_vv(self, p2: 'GXVV') -> None:
        self._wrapper.get_databases_sorted_vv(p2)
        




    def get_data_type(self, p2: 'GXDB', p3: int_ref) -> None:
        p3.value = self._wrapper.get_data_type(p2, p3.value)
        




    def get_default_section(self, p2: float_ref, p3: float_ref, p4: float_ref, p5: float_ref, p6: float_ref) -> None:
        p2.value, p3.value, p4.value, p5.value, p6.value = self._wrapper.get_default_section(p2.value, p3.value, p4.value, p5.value, p6.value)
        




    def get_hole_group(self, p2: int, p3: str) -> int:
        ret_val = self._wrapper.get_hole_group(p2, p3.encode())
        return ret_val




    def get_hole_survey(self, p2: int, p3: 'GXVV', p4: 'GXVV', p5: 'GXVV', p6: 'GXVV') -> None:
        self._wrapper.get_hole_survey(p2, p3, p4, p5, p6)
        




    def get_ipj(self, p2: 'GXIPJ') -> None:
        self._wrapper.get_ipj(p2)
        




    def get_map_names_vv(self, p2: 'GXVV') -> None:
        self._wrapper.get_map_names_vv(p2)
        




    def get_map(self, p2: int) -> 'GXMAP':
        ret_val = self._wrapper.get_map(p2)
        return GXMAP(ret_val)




    def get_num_maps(self) -> int:
        ret_val = self._wrapper.get_num_maps()
        return ret_val




    def get_reg(self) -> 'GXREG':
        ret_val = self._wrapper.get_reg()
        return GXREG(ret_val)




    def get_selected_holes_vv(self, p2: 'GXVV') -> None:
        self._wrapper.get_selected_holes_vv(p2)
        



    @classmethod
    def get_table_default_chan_lst(cls, p1: 'GXLST', p2: int) -> None:
        gxapi_cy.WrapDH.get_table_default_chan_lst(GXContext._get_tls_geo(), p2)
        




    def hole_lst(self, p2: 'GXLST') -> None:
        self._wrapper.hole_lst(p2)
        




    def hole_lst2(self, p2: 'GXLST') -> None:
        self._wrapper.hole_lst2(p2)
        




    def add_hole(self, p2: str) -> int:
        ret_val = self._wrapper.add_hole(p2.encode())
        return ret_val




    def clean_will_delete_db(self) -> int:
        ret_val = self._wrapper.clean_will_delete_db()
        return ret_val




    def compositing_tool_gui(self, p2: 'GXMAP', p3: float, p4: float, p5: float) -> int:
        ret_val = self._wrapper.compositing_tool_gui(p2, p3, p4, p5)
        return ret_val



    @classmethod
    def create_collar_table(cls, p1: str, p2: int, p3: str_ref) -> None:
        p3.value = gxapi_cy.WrapDH.create_collar_table(GXContext._get_tls_geo(), p2, p3.value.encode())
        



    @classmethod
    def create_collar_table_dir(cls, p1: str, p2: str, p3: int, p4: str_ref) -> None:
        p4.value = gxapi_cy.WrapDH.create_collar_table_dir(GXContext._get_tls_geo(), p2.encode(), p3, p4.value.encode())
        




    def delete_will_delete_db(self, p2: 'GXLST') -> int:
        ret_val = self._wrapper.delete_will_delete_db(p2)
        return ret_val




    def find_hole(self, p2: str) -> int:
        ret_val = self._wrapper.find_hole(p2.encode())
        return ret_val




    def get_collar_table_db(self, p2: str_ref) -> None:
        p2.value = self._wrapper.get_collar_table_db(p2.value.encode())
        




    def get_info(self, p2: int, p3: str, p4: str_ref) -> None:
        p4.value = self._wrapper.get_info(p2, p3.encode(), p4.value.encode())
        




    def get_project_name(self, p2: str_ref) -> None:
        p2.value = self._wrapper.get_project_name(p2.value.encode())
        



    @classmethod
    def get_section_id(cls, p1: float, p2: float, p3: float, p4: str_ref) -> None:
        p4.value = gxapi_cy.WrapDH.get_section_id(GXContext._get_tls_geo(), p2, p3, p4.value.encode())
        



    @classmethod
    def get_template_blob(cls, p1: 'GXDB', p2: str, p3: int_ref) -> int:
        ret_val, p3.value = gxapi_cy.WrapDH.get_template_blob(GXContext._get_tls_geo(), p2.encode(), p3.value)
        return ret_val



    @classmethod
    def get_template_info(cls, p1: str, p2: int_ref, p3: str_ref, p5: str_ref) -> None:
        p2.value, p3.value, p5.value = gxapi_cy.WrapDH.get_template_info(GXContext._get_tls_geo(), p2.value, p3.value.encode(), p5.value.encode())
        



    @classmethod
    def get_template_info_ex(cls, p1: str, p2: int_ref, p3: str_ref, p5: str_ref, p7: 'GXLST') -> None:
        p2.value, p3.value, p5.value = gxapi_cy.WrapDH.get_template_info_ex(GXContext._get_tls_geo(), p2.value, p3.value.encode(), p5.value.encode(), p7)
        




    def get_units(self, p2: str_ref, p4: float_ref) -> None:
        p2.value, p4.value = self._wrapper.get_units(p2.value.encode(), p4.value)
        



    @classmethod
    def have_current(cls) -> int:
        ret_val = gxapi_cy.WrapDH.have_current(GXContext._get_tls_geo())
        return ret_val



    @classmethod
    def have_current2(cls, p1: str_ref) -> int:
        ret_val, p1.value = gxapi_cy.WrapDH.have_current2(GXContext._get_tls_geo())
        return ret_val




    def holes(self) -> int:
        ret_val = self._wrapper.holes()
        return ret_val



    @classmethod
    def hole_select_from_list_gui(cls, p1: 'GXLST', p2: 'GXLST') -> int:
        ret_val = gxapi_cy.WrapDH.hole_select_from_list_gui(GXContext._get_tls_geo(), p2)
        return ret_val




    def hole_selection_tool_gui(self) -> int:
        ret_val = self._wrapper.hole_selection_tool_gui()
        return ret_val




    def modify3d_gui(self, p2: str, p3: int_ref) -> int:
        ret_val, p3.value = self._wrapper.modify3d_gui(p2.encode(), p3.value)
        return ret_val




    def edit_classification_table_file_gui(self, p2: str, p3: str_ref, p5: int, p6: int) -> int:
        ret_val, p3.value = self._wrapper.edit_classification_table_file_gui(p2.encode(), p3.value.encode(), p5, p6)
        return ret_val




    def modify_crooked_section_holes_gui(self, p2: str, p3: int_ref) -> int:
        ret_val, p3.value = self._wrapper.modify_crooked_section_holes_gui(p2.encode(), p3.value)
        return ret_val




    def modify_fence_gui(self, p2: str, p3: int_ref) -> int:
        ret_val, p3.value = self._wrapper.modify_fence_gui(p2.encode(), p3.value)
        return ret_val




    def modify_hole_traces_3dgui(self, p2: str, p3: int_ref) -> int:
        ret_val, p3.value = self._wrapper.modify_hole_traces_3dgui(p2.encode(), p3.value)
        return ret_val




    def modify_hole_traces_gui(self, p2: str, p3: int_ref) -> int:
        ret_val, p3.value = self._wrapper.modify_hole_traces_gui(p2.encode(), p3.value)
        return ret_val




    def modify_hole_traces_gui2(self, p2: str, p3: int, p4: int_ref) -> int:
        ret_val, p4.value = self._wrapper.modify_hole_traces_gui2(p2.encode(), p3, p4.value)
        return ret_val




    def modify_plan_gui(self, p2: str, p3: int_ref) -> int:
        ret_val, p3.value = self._wrapper.modify_plan_gui(p2.encode(), p3.value)
        return ret_val




    def modify_plan_holes_gui(self, p2: str, p3: int_ref) -> int:
        ret_val, p3.value = self._wrapper.modify_plan_holes_gui(p2.encode(), p3.value)
        return ret_val



    @classmethod
    def modify_rock_codes_gui(cls, p1: str) -> int:
        ret_val = gxapi_cy.WrapDH.modify_rock_codes_gui(GXContext._get_tls_geo())
        return ret_val



    @classmethod
    def modify_rock_codes_gui2(cls, p1: 'GXDB', p2: str) -> int:
        ret_val = gxapi_cy.WrapDH.modify_rock_codes_gui2(GXContext._get_tls_geo(), p2.encode())
        return ret_val




    def modify_section_gui(self, p2: str, p3: int_ref) -> int:
        ret_val, p3.value = self._wrapper.modify_section_gui(p2.encode(), p3.value)
        return ret_val




    def modify_section_holes_gui(self, p2: str, p3: int_ref) -> int:
        ret_val, p3.value = self._wrapper.modify_section_holes_gui(p2.encode(), p3.value)
        return ret_val




    def modify_stacked_section_gui(self, p2: str, p3: int_ref) -> int:
        ret_val, p3.value = self._wrapper.modify_stacked_section_gui(p2.encode(), p3.value)
        return ret_val




    def modify_strip_log_gui(self, p2: str, p3: int_ref) -> int:
        ret_val, p3.value = self._wrapper.modify_strip_log_gui(p2.encode(), p3.value)
        return ret_val



    @classmethod
    def modify_structure_codes_gui(cls, p1: str) -> int:
        ret_val = gxapi_cy.WrapDH.modify_structure_codes_gui(GXContext._get_tls_geo())
        return ret_val



    @classmethod
    def modify_structure_codes_gui2(cls, p1: 'GXDB', p2: str) -> int:
        ret_val = gxapi_cy.WrapDH.modify_structure_codes_gui2(GXContext._get_tls_geo(), p2.encode())
        return ret_val



    @classmethod
    def import2(cls, p1: str, p2: 'GXDB', p3: int, p4: int, p5: str, p6: int, p7: str) -> None:
        gxapi_cy.WrapDH.import2(GXContext._get_tls_geo(), p2, p3, p4, p5.encode(), p6, p7.encode())
        




    def import_las(self, p2: str, p3: str, p4: float, p5: int, p6: 'GXWA') -> None:
        self._wrapper.import_las(p2.encode(), p3.encode(), p4, p5, p6)
        




    def num_assays(self) -> int:
        ret_val = self._wrapper.num_assays()
        return ret_val




    def num_selected_holes(self) -> int:
        ret_val = self._wrapper.num_selected_holes()
        return ret_val




    def qa_dip_az_curvature_lst(self, p2: 'GXLST', p3: float, p4: 'GXWA') -> int:
        ret_val = self._wrapper.qa_dip_az_curvature_lst(p2, p3, p4)
        return ret_val




    def qa_dip_az_survey_lst(self, p2: 'GXLST', p3: 'GXWA') -> int:
        ret_val = self._wrapper.qa_dip_az_survey_lst(p2, p3)
        return ret_val




    def qa_east_north_curvature_lst(self, p2: 'GXLST', p3: float, p4: 'GXWA') -> int:
        ret_val = self._wrapper.qa_east_north_curvature_lst(p2, p3, p4)
        return ret_val




    def qa_east_north_survey_lst(self, p2: 'GXLST', p3: 'GXWA') -> int:
        ret_val = self._wrapper.qa_east_north_survey_lst(p2, p3)
        return ret_val




    def slice_selection_tool_gui(self, p2: float, p3: float, p4: float, p5: float, p6: float, p7: float, p8: float, p9: float, p10: float_ref, p11: float_ref, p12: float_ref, p13: float_ref) -> int:
        ret_val, p10.value, p11.value, p12.value, p13.value = self._wrapper.slice_selection_tool_gui(p2, p3, p4, p5, p6, p7, p8, p9, p10.value, p11.value, p12.value, p13.value)
        return ret_val




    def update_survey_from_collar(self, p2: int) -> int:
        ret_val = self._wrapper.update_survey_from_collar(p2)
        return ret_val




    def load_data_parameters_ini(self, p2: 'GXDB', p3: str) -> None:
        self._wrapper.load_data_parameters_ini(p2, p3.encode())
        




    def load_plot_parameters(self, p2: str, p3: int) -> None:
        self._wrapper.load_plot_parameters(p2.encode(), p3)
        




    def load_select(self, p2: str) -> None:
        self._wrapper.load_select(p2.encode())
        




    def mask_ply(self, p2: 'GXPLY', p3: 'GXIPJ', p4: float, p5: str, p6: int, p7: int) -> None:
        self._wrapper.mask_ply(p2, p3, p4, p5.encode(), p6, p7)
        



    @classmethod
    def open(cls, p1: str) -> 'GXDH':
        ret_val = gxapi_cy.WrapDH.open(GXContext._get_tls_geo())
        return GXDH(ret_val)




    def open_job(self, p2: str, p3: int) -> None:
        self._wrapper.open_job(p2.encode(), p3)
        




    def plot_hole_traces(self, p2: 'GXMAP', p3: str) -> None:
        self._wrapper.plot_hole_traces(p2, p3.encode())
        




    def plot_hole_traces_3d(self, p2: 'GXMVIEW', p3: str) -> None:
        self._wrapper.plot_hole_traces_3d(p2, p3.encode())
        




    def plot_symbols_3d(self, p2: 'GXMVIEW', p3: str) -> None:
        self._wrapper.plot_symbols_3d(p2, p3.encode())
        




    def qa_collar(self, p2: 'GXWA') -> None:
        self._wrapper.qa_collar(p2)
        




    def qa_collar_lst(self, p2: 'GXLST', p3: 'GXWA') -> None:
        self._wrapper.qa_collar_lst(p2, p3)
        




    def qa_dip_az_curvature(self, p2: 'GXWA', p3: float) -> None:
        self._wrapper.qa_dip_az_curvature(p2, p3)
        




    def qa_dip_az_curvature2(self, p2: 'GXWA', p3: float, p4: str) -> None:
        self._wrapper.qa_dip_az_curvature2(p2, p3, p4.encode())
        




    def qa_dip_az_survey(self, p2: 'GXDB', p3: 'GXWA', p4: int, p5: str) -> None:
        self._wrapper.qa_dip_az_survey(p2, p3, p4, p5.encode())
        




    def qa_east_north_curvature(self, p2: 'GXWA', p3: float) -> None:
        self._wrapper.qa_east_north_curvature(p2, p3)
        




    def qa_east_north_curvature2(self, p2: 'GXWA', p3: float, p4: str) -> None:
        self._wrapper.qa_east_north_curvature2(p2, p3, p4.encode())
        




    def qa_east_north_survey(self, p2: 'GXDB', p3: 'GXWA', p4: int, p5: str) -> None:
        self._wrapper.qa_east_north_survey(p2, p3, p4, p5.encode())
        




    def qa_from_to_data(self, p2: 'GXDB', p3: 'GXWA', p4: int, p5: str) -> None:
        self._wrapper.qa_from_to_data(p2, p3, p4, p5.encode())
        




    def qa_point_data(self, p2: 'GXDB', p3: 'GXWA', p4: int, p5: str) -> None:
        self._wrapper.qa_point_data(p2, p3, p4, p5.encode())
        




    def qa_write_unregistered_holes(self, p2: 'GXDB', p3: 'GXWA') -> None:
        self._wrapper.qa_write_unregistered_holes(p2, p3)
        




    def replot_holes(self, p2: str, p3: int) -> None:
        self._wrapper.replot_holes(p2.encode(), p3)
        




    def plot_holes_on_section(self, p2: str, p3: int, p4: str) -> None:
        self._wrapper.plot_holes_on_section(p2.encode(), p3, p4.encode())
        




    def re_survey_east_north(self, p2: str, p3: 'GXVV', p4: 'GXVV', p5: 'GXVV', p6: 'GXVV', p7: float, p8: float, p9: float, p10: float, p11: float_ref) -> None:
        p11.value = self._wrapper.re_survey_east_north(p2.encode(), p3, p4, p5, p6, p7, p8, p9, p10, p11.value)
        




    def re_survey_pol_fit(self, p2: str, p3: 'GXVV', p4: 'GXVV', p5: 'GXVV', p6: float, p7: float, p8: float, p9: float, p10: float, p11: float, p12: int, p13: int, p14: 'GXVV', p15: 'GXVV', p16: 'GXVV', p17: 'GXVV') -> None:
        self._wrapper.re_survey_pol_fit(p2.encode(), p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16, p17)
        




    def re_survey_rad_curve(self, p2: str, p3: 'GXVV', p4: 'GXVV', p5: 'GXVV', p6: float, p7: float, p8: float, p9: float, p10: float, p11: float, p12: int, p13: 'GXVV', p14: 'GXVV', p15: 'GXVV', p16: 'GXVV') -> None:
        self._wrapper.re_survey_rad_curve(p2.encode(), p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16)
        




    def re_survey_straight(self, p2: str, p3: float, p4: float, p5: float, p6: float, p7: float, p8: float, p9: float, p10: float, p11: int, p12: 'GXVV', p13: 'GXVV', p14: 'GXVV', p15: 'GXVV') -> None:
        self._wrapper.re_survey_straight(p2.encode(), p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15)
        




    def re_survey_straight_seg(self, p2: str, p3: 'GXVV', p4: 'GXVV', p5: 'GXVV', p6: float, p7: float, p8: float, p9: float, p10: float, p11: float, p12: int, p13: 'GXVV', p14: 'GXVV', p15: 'GXVV', p16: 'GXVV') -> None:
        self._wrapper.re_survey_straight_seg(p2.encode(), p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16)
        




    def save_data_parameters_ini(self, p2: 'GXDB', p3: str) -> None:
        self._wrapper.save_data_parameters_ini(p2, p3.encode())
        




    def save_job(self, p2: str, p3: int) -> None:
        self._wrapper.save_job(p2.encode(), p3)
        




    def save_select(self, p2: str) -> None:
        self._wrapper.save_select(p2.encode())
        




    def section_window_size_mm(self, p2: float_ref, p3: float_ref) -> None:
        p2.value, p3.value = self._wrapper.section_window_size_mm(p2.value, p3.value)
        




    def select_all_holes(self) -> None:
        self._wrapper.select_all_holes()
        




    def select_holes(self, p2: 'GXVV', p3: int) -> None:
        self._wrapper.select_holes(p2, p3)
        




    def select_name(self, p2: str, p3: int, p4: int) -> None:
        self._wrapper.select_name(p2.encode(), p3, p4)
        




    def select_ply(self, p2: 'GXPLY') -> None:
        self._wrapper.select_ply(p2)
        




    def select_ply2(self, p2: 'GXPLY', p3: int, p4: int, p5: int) -> None:
        self._wrapper.select_ply2(p2, p3, p4, p5)
        




    def set_crooked_section_ipj(self, p2: 'GXIPJ') -> None:
        self._wrapper.set_crooked_section_ipj(p2)
        




    def set_current_view_name(self, p2: str) -> None:
        self._wrapper.set_current_view_name(p2.encode())
        




    def set_info(self, p2: int, p3: str, p4: str) -> None:
        self._wrapper.set_info(p2, p3.encode(), p4.encode())
        




    def set_ipj(self, p2: 'GXIPJ') -> None:
        self._wrapper.set_ipj(p2)
        




    def set_map(self, p2: 'GXMAP') -> None:
        self._wrapper.set_map(p2)
        




    def set_new_ipj(self, p2: str) -> None:
        self._wrapper.set_new_ipj(p2.encode())
        




    def set_selected_holes_vv(self, p2: 'GXVV', p3: int) -> None:
        self._wrapper.set_selected_holes_vv(p2, p3)
        



    @classmethod
    def set_template_blob(cls, p1: 'GXDB', p2: str, p3: int) -> None:
        gxapi_cy.WrapDH.set_template_blob(GXContext._get_tls_geo(), p2.encode(), p3)
        




    def significant_intersections_db(self, p2: 'GXDB', p3: 'GXDB', p4: int, p5: str, p6: float, p7: float, p8: float, p9: float, p10: float, p11: float, p12: float) -> None:
        self._wrapper.significant_intersections_db(p2, p3, p4, p5.encode(), p6, p7, p8, p9, p10, p11, p12)
        




    def test_import_las(self, p2: str, p3: str, p4: float, p5: 'GXWA', p6: int_ref) -> None:
        p6.value = self._wrapper.test_import_las(p2.encode(), p3.encode(), p4, p5, p6.value)
        




    def un_select_all_holes(self) -> None:
        self._wrapper.un_select_all_holes()
        




    def un_selected_hole_lst(self, p2: 'GXLST') -> None:
        self._wrapper.un_selected_hole_lst(p2)
        




    def update_collar_table(self) -> None:
        self._wrapper.update_collar_table()
        




    def update_hole_extent(self, p2: int) -> None:
        self._wrapper.update_hole_extent(p2)
        




    def wholeplot(self, p2: str, p3: int) -> None:
        self._wrapper.wholeplot(p2.encode(), p3)
        




    def surface_intersections(self, p2: 'GXDB', p3: str, p4: int) -> None:
        self._wrapper.surface_intersections(p2, p3.encode(), p4)
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer