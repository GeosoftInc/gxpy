### extends 'class_empty.py'
from . import gxapi_cy

from geosoft.gxapi import GXContext, int_ref, float_ref, str_ref

### block Header
# NOTICE: The code generator will not replace the code in this block
### endblock Header

### block ClassImplementation
# NOTICE: Do not edit anything here, it is generated code
class GXSEMPLOT:
    """
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._wrapper = None

    def __del__(self):
        self._wrapper = None

    def __init__(self, wrapper=None):
        self._wrapper = wrapper if wrapper else gxapi_cy.WrapSEMPLOT(0)

    @classmethod
    def null(cls) -> 'GXSEMPLOT':
        """
        A null (undefined) instance of :class:`GXSEMPLOT`
        
        :returns: A null :class:`GX3DN`
        """
        return cls()

    def is_null(self) -> bool:
        """
        Check if the instance of :class:`GXSEMPLOT` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of :class:`GXSEMPLOT`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Miscellaneous


    @classmethod
    def apply_filter_to_mask(cls, p1: 'GXDB', p2: str, p3: str, p4: str, p5: str, p6: int) -> None:
        gxapi_cy.WrapSEMPLOT.apply_filter_to_mask(GXContext._get_tls_geo(), p1._wrapper, p2.encode(), p3.encode(), p4.encode(), p5.encode(), p6)
        



    @classmethod
    def convert_dummies(cls, p1: 'GXDB', p2: int) -> None:
        gxapi_cy.WrapSEMPLOT.convert_dummies(GXContext._get_tls_geo(), p1._wrapper, p2)
        



    @classmethod
    def create_groups(cls, p1: 'GXDB', p2: str) -> None:
        gxapi_cy.WrapSEMPLOT.create_groups(GXContext._get_tls_geo(), p1._wrapper, p2.encode())
        



    @classmethod
    def default_groups(cls, p1: 'GXDB') -> None:
        gxapi_cy.WrapSEMPLOT.default_groups(GXContext._get_tls_geo(), p1._wrapper)
        



    @classmethod
    def edit_map_plot_parameters(cls, p1: 'GXDB', p2: str, p3: str, p4: 'GXMAP', p5: str) -> None:
        gxapi_cy.WrapSEMPLOT.edit_map_plot_parameters(GXContext._get_tls_geo(), p1._wrapper, p2.encode(), p3.encode(), p4._wrapper, p5.encode())
        



    @classmethod
    def edit_plot_components(cls, p1: 'GXDB', p2: str) -> None:
        gxapi_cy.WrapSEMPLOT.edit_plot_components(GXContext._get_tls_geo(), p1._wrapper, p2.encode())
        



    @classmethod
    def edit_plot_parameters(cls, p1: 'GXDB', p2: str) -> None:
        gxapi_cy.WrapSEMPLOT.edit_plot_parameters(GXContext._get_tls_geo(), p1._wrapper, p2.encode())
        



    @classmethod
    def export_overlay(cls, p1: str, p2: str, p3: 'GXMVIEW', p4: str, p5: int, p6: str, p7: str, p8: str, p9: str, p10: str, p11: str, p12: int) -> None:
        gxapi_cy.WrapSEMPLOT.export_overlay(GXContext._get_tls_geo(), p1.encode(), p2.encode(), p3._wrapper, p4.encode(), p5, p6.encode(), p7.encode(), p8.encode(), p9.encode(), p10.encode(), p11.encode(), p12)
        



    @classmethod
    def export_view(cls, p1: 'GXDB', p2: 'GXLST', p3: 'GXDB', p4: int, p5: str, p6: str, p7: str) -> None:
        gxapi_cy.WrapSEMPLOT.export_view(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3._wrapper, p4, p5.encode(), p6.encode(), p7.encode())
        



    @classmethod
    def export_view2(cls, p1: 'GXDB', p2: 'GXLST', p3: 'GXDB', p4: int, p5: str, p6: str, p7: str, p8: int) -> None:
        gxapi_cy.WrapSEMPLOT.export_view2(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3._wrapper, p4, p5.encode(), p6.encode(), p7.encode(), p8)
        



    @classmethod
    def filter_lst(cls, p1: 'GXLST') -> None:
        gxapi_cy.WrapSEMPLOT.filter_lst(GXContext._get_tls_geo(), p1._wrapper)
        



    @classmethod
    def filter_mineral_pos_data(cls, p1: 'GXDB', p2: str, p3: str, p4: str, p5: int) -> None:
        gxapi_cy.WrapSEMPLOT.filter_mineral_pos_data(GXContext._get_tls_geo(), p1._wrapper, p2.encode(), p3.encode(), p4.encode(), p5)
        



    @classmethod
    def get_associated_lst(cls, p1: 'GXDB', p2: int, p3: 'GXLST') -> None:
        gxapi_cy.WrapSEMPLOT.get_associated_lst(GXContext._get_tls_geo(), p1._wrapper, p2, p3._wrapper)
        



    @classmethod
    def get_current_mineral_lst(cls, p1: 'GXDB', p2: str, p3: 'GXLST') -> None:
        gxapi_cy.WrapSEMPLOT.get_current_mineral_lst(GXContext._get_tls_geo(), p1._wrapper, p2.encode(), p3._wrapper)
        



    @classmethod
    def get_current_position_lst(cls, p1: 'GXDB', p2: 'GXLST') -> None:
        gxapi_cy.WrapSEMPLOT.get_current_position_lst(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper)
        



    @classmethod
    def get_full_mineral_lst(cls, p1: 'GXLST') -> None:
        gxapi_cy.WrapSEMPLOT.get_full_mineral_lst(GXContext._get_tls_geo(), p1._wrapper)
        



    @classmethod
    def get_full_position_lst(cls, p1: 'GXLST') -> None:
        gxapi_cy.WrapSEMPLOT.get_full_position_lst(GXContext._get_tls_geo(), p1._wrapper)
        



    @classmethod
    def get_grouping_lst(cls, p1: 'GXDB', p2: 'GXLST') -> None:
        gxapi_cy.WrapSEMPLOT.get_grouping_lst(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper)
        



    @classmethod
    def create_ascii_template(cls, p1: str, p2: str) -> int:
        ret_val = gxapi_cy.WrapSEMPLOT.create_ascii_template(GXContext._get_tls_geo(), p1.encode(), p2.encode())
        return ret_val



    @classmethod
    def create_database_template(cls, p1: str, p2: str) -> int:
        ret_val = gxapi_cy.WrapSEMPLOT.create_database_template(GXContext._get_tls_geo(), p1.encode(), p2.encode())
        return ret_val



    @classmethod
    def edit_filter(cls, p1: 'GXDB', p2: str, p3: str, p4: str, p5: str) -> int:
        ret_val = gxapi_cy.WrapSEMPLOT.edit_filter(GXContext._get_tls_geo(), p1._wrapper, p2.encode(), p3.encode(), p4.encode(), p5.encode())
        return ret_val



    @classmethod
    def get_mineral_channel_name(cls, p1: 'GXDB', p2: str_ref) -> None:
        p2.value = gxapi_cy.WrapSEMPLOT.get_mineral_channel_name(GXContext._get_tls_geo(), p1._wrapper, p2.value.encode())
        



    @classmethod
    def import_ascii_wizard(cls, p1: str, p2: str, p3: str_ref) -> None:
        p3.value = gxapi_cy.WrapSEMPLOT.import_ascii_wizard(GXContext._get_tls_geo(), p1.encode(), p2.encode(), p3.value.encode())
        



    @classmethod
    def import_database_odbc(cls, p1: str_ref, p3: str_ref) -> None:
        p1.value, p3.value = gxapi_cy.WrapSEMPLOT.import_database_odbc(GXContext._get_tls_geo(), p1.value.encode(), p3.value.encode())
        



    @classmethod
    def import_bin(cls, p1: 'GXDB', p2: str, p3: str, p4: str, p5: int, p6: float) -> None:
        gxapi_cy.WrapSEMPLOT.import_bin(GXContext._get_tls_geo(), p1._wrapper, p2.encode(), p3.encode(), p4.encode(), p5, p6)
        



    @classmethod
    def import_database_ado(cls, p1: str, p2: str) -> None:
        gxapi_cy.WrapSEMPLOT.import_database_ado(GXContext._get_tls_geo(), p1.encode(), p2.encode())
        



    @classmethod
    def init_group_symbols_used(cls, p1: 'GXDB') -> None:
        gxapi_cy.WrapSEMPLOT.init_group_symbols_used(GXContext._get_tls_geo(), p1._wrapper)
        



    @classmethod
    def template_type(cls, p1: str) -> int:
        ret_val = gxapi_cy.WrapSEMPLOT.template_type(GXContext._get_tls_geo(), p1.encode())
        return ret_val



    @classmethod
    def view_type(cls, p1: 'GXMAP', p2: str) -> int:
        ret_val = gxapi_cy.WrapSEMPLOT.view_type(GXContext._get_tls_geo(), p1._wrapper, p2.encode())
        return ret_val



    @classmethod
    def mineral_id(cls, p1: 'GXDB', p2: float, p3: int, p4: int) -> None:
        gxapi_cy.WrapSEMPLOT.mineral_id(GXContext._get_tls_geo(), p1._wrapper, p2, p3, p4)
        



    @classmethod
    def new_filter(cls, p1: str, p2: str) -> None:
        gxapi_cy.WrapSEMPLOT.new_filter(GXContext._get_tls_geo(), p1.encode(), p2.encode())
        



    @classmethod
    def new_template(cls, p1: str, p2: int, p3: str) -> None:
        gxapi_cy.WrapSEMPLOT.new_template(GXContext._get_tls_geo(), p1.encode(), p2, p3.encode())
        



    @classmethod
    def overlay_lst(cls, p1: 'GXLST', p2: int, p3: int) -> None:
        gxapi_cy.WrapSEMPLOT.overlay_lst(GXContext._get_tls_geo(), p1._wrapper, p2, p3)
        



    @classmethod
    def plot(cls, p1: 'GXDB', p2: str, p3: str, p4: str, p5: str, p6: int, p7: int) -> None:
        gxapi_cy.WrapSEMPLOT.plot(GXContext._get_tls_geo(), p1._wrapper, p2.encode(), p3.encode(), p4.encode(), p5.encode(), p6, p7)
        



    @classmethod
    def plot_symbol_legend(cls, p1: 'GXDB', p2: 'GXMVIEW', p3: float, p4: float, p5: float, p6: float) -> None:
        gxapi_cy.WrapSEMPLOT.plot_symbol_legend(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3, p4, p5, p6)
        



    @classmethod
    def prop_symb(cls, p1: 'GXDB', p2: 'GXMAP', p3: str, p4: str, p5: str, p6: str, p7: int, p8: int, p9: float, p10: float, p11: int, p12: int, p13: int, p14: int, p15: int) -> None:
        gxapi_cy.WrapSEMPLOT.prop_symb(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3.encode(), p4.encode(), p5.encode(), p6.encode(), p7, p8, p9, p10, p11, p12, p13, p14, p15)
        



    @classmethod
    def replot(cls, p1: 'GXDB', p2: str, p3: str, p4: 'GXMAP', p5: str) -> None:
        gxapi_cy.WrapSEMPLOT.replot(GXContext._get_tls_geo(), p1._wrapper, p2.encode(), p3.encode(), p4._wrapper, p5.encode())
        



    @classmethod
    def re_plot_symbol_legend(cls, p1: 'GXDB', p2: 'GXMVIEW') -> None:
        gxapi_cy.WrapSEMPLOT.re_plot_symbol_legend(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper)
        



    @classmethod
    def reset_groups(cls, p1: 'GXDB', p2: str) -> None:
        gxapi_cy.WrapSEMPLOT.reset_groups(GXContext._get_tls_geo(), p1._wrapper, p2.encode())
        



    @classmethod
    def reset_used_channel(cls, p1: 'GXDB') -> None:
        gxapi_cy.WrapSEMPLOT.reset_used_channel(GXContext._get_tls_geo(), p1._wrapper)
        



    @classmethod
    def select_poly(cls, p1: 'GXDB', p2: 'GXMVIEW', p3: str, p4: str, p5: 'GXPLY', p6: int) -> None:
        gxapi_cy.WrapSEMPLOT.select_poly(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3.encode(), p4.encode(), p5._wrapper, p6)
        



    @classmethod
    def set_channel_order(cls, p1: 'GXDB', p2: 'GXLST') -> None:
        gxapi_cy.WrapSEMPLOT.set_channel_order(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper)
        



    @classmethod
    def set_channel_units(cls, p1: 'GXDB') -> None:
        gxapi_cy.WrapSEMPLOT.set_channel_units(GXContext._get_tls_geo(), p1._wrapper)
        



    @classmethod
    def set_itr(cls, p1: 'GXDB', p2: int, p3: 'GXITR') -> None:
        gxapi_cy.WrapSEMPLOT.set_itr(GXContext._get_tls_geo(), p1._wrapper, p2, p3._wrapper)
        



    @classmethod
    def set_mask(cls, p1: 'GXDB', p2: str, p3: str, p4: str, p5: int, p6: int) -> None:
        gxapi_cy.WrapSEMPLOT.set_mask(GXContext._get_tls_geo(), p1._wrapper, p2.encode(), p3.encode(), p4.encode(), p5, p6)
        



    @classmethod
    def sort_data(cls, p1: 'GXDB', p2: int, p3: int) -> None:
        gxapi_cy.WrapSEMPLOT.sort_data(GXContext._get_tls_geo(), p1._wrapper, p2, p3)
        



    @classmethod
    def template_lst(cls, p1: 'GXLST', p2: int) -> None:
        gxapi_cy.WrapSEMPLOT.template_lst(GXContext._get_tls_geo(), p1._wrapper, p2)
        



    @classmethod
    def tile_windows(cls) -> None:
        gxapi_cy.WrapSEMPLOT.tile_windows(GXContext._get_tls_geo())
        



    @classmethod
    def total_oxides(cls, p1: 'GXDB', p2: str) -> None:
        gxapi_cy.WrapSEMPLOT.total_oxides(GXContext._get_tls_geo(), p1._wrapper, p2.encode())
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer