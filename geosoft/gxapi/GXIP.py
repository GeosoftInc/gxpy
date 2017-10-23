### extends 'class_empty.py'
from . import gxapi_cy

from geosoft.gxapi import GXContext, int_ref, float_ref, str_ref

### block Header
# NOTICE: The code generator will not replace the code in this block
### endblock Header

### block ClassImplementation
# NOTICE: Do not edit anything here, it is generated code
class GXIP:
    """
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._wrapper = None

    def __del__(self):
        self._wrapper = None

    def __init__(self, wrapper=None):
        self._wrapper = wrapper if wrapper else gxapi_cy.WrapIP(0)

    @classmethod
    def null(cls) -> 'GXIP':
        """
        A null (undefined) instance of :class:`GXIP`
        
        :returns: A null :class:`GX3DN`
        """
        return cls()

    def is_null(self) -> bool:
        """
        Check if the instance of :class:`GXIP` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of :class:`GXIP`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Plot Jobs


    @classmethod
    def convert_ubcip2_d_to_grid(cls, p1: str, p2: 'GXPG', p3: 'GXVV', p4: 'GXVV', p5: float, p6: float, p7: float, p8: float, p9: int) -> None:
        gxapi_cy.WrapIP.convert_ubcip2_d_to_grid(GXContext._get_tls_geo(), p1.encode(), p2._wrapper, p3._wrapper, p4._wrapper, p5, p6, p7, p8, p9)
        




    def create_default_job(self, p2: str, p3: int) -> None:
        self._wrapper.create_default_job(p2.encode(), p3)
        




    def export_ubcip3(self, p2: 'GXDB', p3: str, p4: str, p5: str, p6: str, p7: str, p8: float) -> None:
        self._wrapper.export_ubcip3(p2._wrapper, p3.encode(), p4.encode(), p5.encode(), p6.encode(), p7.encode(), p8)
        



    @classmethod
    def export_ubcip_control(cls, p1: str, p2: int, p3: int, p4: float, p5: str, p6: str, p7: str, p8: str, p9: str, p10: str, p11: str, p12: str) -> None:
        gxapi_cy.WrapIP.export_ubcip_control(GXContext._get_tls_geo(), p1.encode(), p2, p3, p4, p5.encode(), p6.encode(), p7.encode(), p8.encode(), p9.encode(), p10.encode(), p11.encode(), p12.encode())
        



    @classmethod
    def export_ubcip_control_v5(cls, p1: str, p2: int, p3: float, p4: str, p5: str, p6: int, p7: str, p8: int, p9: str, p10: int, p11: str, p12: int, p13: str, p14: int, p15: str, p16: str) -> None:
        gxapi_cy.WrapIP.export_ubcip_control_v5(GXContext._get_tls_geo(), p1.encode(), p2, p3, p4.encode(), p5.encode(), p6, p7.encode(), p8, p9.encode(), p10, p11.encode(), p12, p13.encode(), p14, p15.encode(), p16.encode())
        




    def export_ubc_res3(self, p2: 'GXDB', p3: str, p4: str, p5: str, p6: str, p7: str, p8: str, p9: float) -> None:
        self._wrapper.export_ubc_res3(p2._wrapper, p3.encode(), p4.encode(), p5.encode(), p6.encode(), p7.encode(), p8.encode(), p9)
        



    @classmethod
    def export_ubc_res_control(cls, p1: str, p2: int, p3: int, p4: float, p5: str, p6: str, p7: str, p8: str, p9: float, p10: str, p11: str) -> None:
        gxapi_cy.WrapIP.export_ubc_res_control(GXContext._get_tls_geo(), p1.encode(), p2, p3, p4, p5.encode(), p6.encode(), p7.encode(), p8.encode(), p9, p10.encode(), p11.encode())
        



    @classmethod
    def export_ubc_res_control_v5(cls, p1: str, p2: int, p3: float, p4: str, p5: str, p6: int, p7: str, p8: int, p9: str, p10: int, p11: str, p12: int, p13: str, p14: str) -> None:
        gxapi_cy.WrapIP.export_ubc_res_control_v5(GXContext._get_tls_geo(), p1.encode(), p2, p3, p4.encode(), p5.encode(), p6, p7.encode(), p8, p9.encode(), p10, p11.encode(), p12, p13.encode(), p14.encode())
        




    def export_data_to_ubc_3d(self, p2: 'GXDB', p3: 'GXLST', p4: int, p5: int, p6: str, p7: str, p8: str, p9: int, p10: str, p11: str) -> None:
        self._wrapper.export_data_to_ubc_3d(p2._wrapper, p3._wrapper, p4, p5, p6.encode(), p7.encode(), p8.encode(), p9, p10.encode(), p11.encode())
        



    @classmethod
    def import_ubc2_dmod(cls, p1: str, p2: int) -> 'GXPG':
        ret_val = gxapi_cy.WrapIP.import_ubc2_dmod(GXContext._get_tls_geo(), p1.encode(), p2)
        return GXPG(ret_val)



    @classmethod
    def import_ubc2_dmsh(cls, p1: str, p2: float_ref, p3: float_ref, p4: 'GXVV', p5: 'GXVV') -> None:
        p2.value, p3.value = gxapi_cy.WrapIP.import_ubc2_dmsh(GXContext._get_tls_geo(), p1.encode(), p2.value, p3.value, p4._wrapper, p5._wrapper)
        



    @classmethod
    def import_ubc2_d_topo(cls, p1: str, p2: float_ref, p3: 'GXVV', p4: 'GXVV') -> None:
        p2.value = gxapi_cy.WrapIP.import_ubc2_d_topo(GXContext._get_tls_geo(), p1.encode(), p2.value, p3._wrapper, p4._wrapper)
        




    def open_job(self, p2: str, p3: int) -> None:
        self._wrapper.open_job(p2.encode(), p3)
        




    def save_job(self, p2: str, p3: int) -> None:
        self._wrapper.save_job(p2.encode(), p3)
        



    @classmethod
    def trim_ubc2_d_model(cls, p1: 'GXPG', p2: int, p3: int, p4: int, p5: 'GXVV', p6: 'GXVV', p7: float_ref) -> 'GXPG':
        ret_val, p7.value = gxapi_cy.WrapIP.trim_ubc2_d_model(GXContext._get_tls_geo(), p1._wrapper, p2, p3, p4, p5._wrapper, p6._wrapper, p7.value)
        return GXPG(ret_val)




    def write_distant_electrodes(self, p2: 'GXDB') -> None:
        self._wrapper.write_distant_electrodes(p2._wrapper)
        




    def write_distant_electrodes_lst(self, p2: 'GXDB', p3: 'GXLST') -> None:
        self._wrapper.write_distant_electrodes_lst(p2._wrapper, p3._wrapper)
        




# Miscellaneous



    def average_duplicates_qc(self, p2: 'GXDB', p3: str, p4: str, p5: int) -> None:
        self._wrapper.average_duplicates_qc(p2._wrapper, p3.encode(), p4.encode(), p5)
        



    @classmethod
    def create(cls) -> 'GXIP':
        ret_val = gxapi_cy.WrapIP.create(GXContext._get_tls_geo())
        return GXIP(ret_val)






    def export_i2_x(self, p2: 'GXDB', p3: str, p4: str, p5: str, p6: str, p7: str, p8: str, p9: str, p10: str, p11: str, p12: str) -> None:
        self._wrapper.export_i2_x(p2._wrapper, p3.encode(), p4.encode(), p5.encode(), p6.encode(), p7.encode(), p8.encode(), p9.encode(), p10.encode(), p11.encode(), p12.encode())
        




    def export_ipdata(self, p2: 'GXDB', p3: str, p4: str) -> None:
        self._wrapper.export_ipdata(p2._wrapper, p3.encode(), p4.encode())
        




    def export_ipdata_dir(self, p2: 'GXDB', p3: str, p4: str, p5: str) -> None:
        self._wrapper.export_ipdata_dir(p2._wrapper, p3.encode(), p4.encode(), p5.encode())
        




    def export_ipred(self, p2: 'GXDB', p3: str, p4: str, p5: str, p6: int, p7: str, p8: float, p9: float, p10: int) -> None:
        self._wrapper.export_ipred(p2._wrapper, p3.encode(), p4.encode(), p5.encode(), p6, p7.encode(), p8, p9, p10)
        




    def export_ipred_dir(self, p2: 'GXDB', p3: str, p4: str, p5: str, p6: int, p7: str, p8: float, p9: float, p10: int, p11: str) -> None:
        self._wrapper.export_ipred_dir(p2._wrapper, p3.encode(), p4.encode(), p5.encode(), p6, p7.encode(), p8, p9, p10, p11.encode())
        




    def export_line_ipdata(self, p2: 'GXDB', p3: str, p4: str, p5: str) -> None:
        self._wrapper.export_line_ipdata(p2._wrapper, p3.encode(), p4.encode(), p5.encode())
        




    def export_sgdf(self, p2: 'GXDB', p3: str, p4: str, p5: str) -> None:
        self._wrapper.export_sgdf(p2._wrapper, p3.encode(), p4.encode(), p5.encode())
        




    def get_n_value_lst(self, p2: 'GXDB', p3: 'GXLST') -> None:
        self._wrapper.get_n_value_lst(p2._wrapper, p3._wrapper)
        




    def get_topo_line(self, p2: 'GXDB', p3: str, p4: float, p5: float, p6: float, p7: 'GXVV') -> None:
        self._wrapper.get_topo_line(p2._wrapper, p3.encode(), p4, p5, p6, p7._wrapper)
        




    def get_chan_domain(self, p2: 'GXDB', p3: str) -> int:
        ret_val = self._wrapper.get_chan_domain(p2._wrapper, p3.encode())
        return ret_val



    @classmethod
    def get_chan_label(cls, p1: str, p2: str_ref, p4: str_ref) -> None:
        p2.value, p4.value = gxapi_cy.WrapIP.get_chan_label(GXContext._get_tls_geo(), p1.encode(), p2.value.encode(), p4.value.encode())
        




    def get_channel_info(self, p2: 'GXDB', p3: str, p4: int_ref, p5: float_ref, p6: int_ref, p7: 'GXVV') -> None:
        p4.value, p5.value, p6.value = self._wrapper.get_channel_info(p2._wrapper, p3.encode(), p4.value, p5.value, p6.value, p7._wrapper)
        




    def set_channel_info(self, p2: 'GXDB', p3: str, p4: int, p5: float, p6: int, p7: 'GXVV') -> None:
        self._wrapper.set_channel_info(p2._wrapper, p3.encode(), p4, p5, p6, p7._wrapper)
        




    def import_dump(self, p2: int, p3: 'GXDB', p4: str) -> None:
        self._wrapper.import_dump(p2, p3._wrapper, p4.encode())
        




    def import_grid(self, p2: 'GXDB', p3: str, p4: str) -> None:
        self._wrapper.import_grid(p2._wrapper, p3.encode(), p4.encode())
        




    def import_i2_x(self, p2: 'GXDB', p3: str, p4: str, p5: str, p6: str, p7: str, p8: str, p9: str, p10: str, p11: str, p12: str, p13: int) -> None:
        self._wrapper.import_i2_x(p2._wrapper, p3.encode(), p4.encode(), p5.encode(), p6.encode(), p7.encode(), p8.encode(), p9.encode(), p10.encode(), p11.encode(), p12.encode(), p13)
        




    def import_i2_x_ex(self, p2: 'GXDB', p3: str, p4: str, p5: str, p6: str, p7: str, p8: str, p9: str, p10: str, p11: str, p12: str, p13: str, p14: str, p15: int) -> None:
        self._wrapper.import_i2_x_ex(p2._wrapper, p3.encode(), p4.encode(), p5.encode(), p6.encode(), p7.encode(), p8.encode(), p9.encode(), p10.encode(), p11.encode(), p12.encode(), p13.encode(), p14.encode(), p15)
        




    def import_instrumentation_gdd(self, p2: 'GXDB', p3: str) -> None:
        self._wrapper.import_instrumentation_gdd(p2._wrapper, p3.encode())
        




    def import_ipdata(self, p2: 'GXDB', p3: str, p4: str) -> None:
        self._wrapper.import_ipdata(p2._wrapper, p3.encode(), p4.encode())
        




    def import_ipdata2(self, p2: 'GXDB', p3: str, p4: str, p5: str) -> None:
        self._wrapper.import_ipdata2(p2._wrapper, p3.encode(), p4.encode(), p5.encode())
        




    def import_ipred(self, p2: 'GXDB', p3: str, p4: str) -> None:
        self._wrapper.import_ipred(p2._wrapper, p3.encode(), p4.encode())
        




    def import_merge_ipred(self, p2: 'GXDB', p3: str, p4: str) -> None:
        self._wrapper.import_merge_ipred(p2._wrapper, p3.encode(), p4.encode())
        




    def import_sgdf(self, p2: 'GXDB', p3: str) -> None:
        self._wrapper.import_sgdf(p2._wrapper, p3.encode())
        




    def import_topo_csv(self, p2: 'GXDB', p3: str) -> None:
        self._wrapper.import_topo_csv(p2._wrapper, p3.encode())
        




    def import_topo_grid(self, p2: 'GXDB', p3: str) -> None:
        self._wrapper.import_topo_grid(p2._wrapper, p3.encode())
        




    def import_zonge_avg(self, p2: 'GXDB', p3: str, p4: float, p5: int, p6: float) -> None:
        self._wrapper.import_zonge_avg(p2._wrapper, p3.encode(), p4, p5, p6)
        




    def import_zonge_fld(self, p2: 'GXDB', p3: str, p4: int, p5: float) -> None:
        self._wrapper.import_zonge_fld(p2._wrapper, p3.encode(), p4, p5)
        




    def new_xy_database(self, p2: 'GXDB', p3: 'GXDB', p4: 'GXVV', p5: str, p6: float) -> None:
        self._wrapper.new_xy_database(p2._wrapper, p3._wrapper, p4._wrapper, p5.encode(), p6)
        




    def pseudo_plot(self, p2: 'GXDB', p3: str, p4: str, p5: str) -> None:
        self._wrapper.pseudo_plot(p2._wrapper, p3.encode(), p4.encode(), p5.encode())
        




    def pseudo_plot2(self, p2: 'GXDB', p3: str, p4: str, p5: str, p6: str) -> None:
        self._wrapper.pseudo_plot2(p2._wrapper, p3.encode(), p4.encode(), p5.encode(), p6.encode())
        




    def pseudo_plot2_dir(self, p2: 'GXDB', p3: str, p4: str, p5: str, p6: str, p7: str) -> None:
        self._wrapper.pseudo_plot2_dir(p2._wrapper, p3.encode(), p4.encode(), p5.encode(), p6.encode(), p7.encode())
        




    def ps_stack(self, p2: 'GXDB', p3: str, p4: str, p5: str) -> None:
        self._wrapper.ps_stack(p2._wrapper, p3.encode(), p4.encode(), p5.encode())
        




    def ps_stack2(self, p2: 'GXDB', p3: str, p4: str, p5: int, p6: str) -> None:
        self._wrapper.ps_stack2(p2._wrapper, p3.encode(), p4.encode(), p5, p6.encode())
        




    def ps_stack2_dir(self, p2: 'GXDB', p3: str, p4: str, p5: int, p6: str, p7: str) -> None:
        self._wrapper.ps_stack2_dir(p2._wrapper, p3.encode(), p4.encode(), p5, p6.encode(), p7.encode())
        




    def qc_chan_lst(self, p2: 'GXDB', p3: 'GXLST') -> None:
        self._wrapper.qc_chan_lst(p2._wrapper, p3._wrapper)
        




    def recalculate(self, p2: 'GXDB') -> None:
        self._wrapper.recalculate(p2._wrapper)
        




    def recalculate_ex(self, p2: 'GXDB', p3: int) -> None:
        self._wrapper.recalculate_ex(p2._wrapper, p3)
        




    def recalculate_z(self, p2: 'GXDB') -> None:
        self._wrapper.recalculate_z(p2._wrapper)
        




    def set_import_line(self, p2: str) -> None:
        self._wrapper.set_import_line(p2.encode())
        




    def set_import_mode(self, p2: int) -> None:
        self._wrapper.set_import_mode(p2)
        




    def window(self, p2: 'GXDB', p3: str, p4: str, p5: str) -> None:
        self._wrapper.window(p2._wrapper, p3.encode(), p4.encode(), p5.encode())
        



    @classmethod
    def winnow_chan_list(cls, p1: 'GXLST') -> None:
        gxapi_cy.WrapIP.winnow_chan_list(GXContext._get_tls_geo(), p1._wrapper)
        



    @classmethod
    def winnow_chan_list2(cls, p1: 'GXLST', p2: 'GXDB') -> None:
        gxapi_cy.WrapIP.winnow_chan_list2(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper)
        




    def is_valid_line(self, p2: 'GXDB', p3: str) -> int:
        ret_val = self._wrapper.is_valid_line(p2._wrapper, p3.encode())
        return ret_val




    def line_array_type(self, p2: 'GXDB', p3: str) -> int:
        ret_val = self._wrapper.line_array_type(p2._wrapper, p3.encode())
        return ret_val




    def a_spacing(self, p2: 'GXDB', p3: str) -> float:
        ret_val = self._wrapper.a_spacing(p2._wrapper, p3.encode())
        return ret_val




    def pldp_convention(self) -> int:
        ret_val = self._wrapper.pldp_convention()
        return ret_val




    def get_electrode_locations_and_mask_values(self, p2: 'GXDB', p3: str, p4: int, p5: 'GXVV', p6: 'GXVV', p7: 'GXVV', p8: 'GXVV') -> None:
        self._wrapper.get_electrode_locations_and_mask_values(p2._wrapper, p3.encode(), p4, p5._wrapper, p6._wrapper, p7._wrapper, p8._wrapper)
        




    def get_electrode_locations_and_mask_values2(self, p2: 'GXDB', p3: str, p4: int, p5: 'GXVV', p6: 'GXVV', p7: 'GXVV', p8: 'GXVV', p9: 'GXVV') -> None:
        self._wrapper.get_electrode_locations_and_mask_values2(p2._wrapper, p3.encode(), p4, p5._wrapper, p6._wrapper, p7._wrapper, p8._wrapper, p9._wrapper)
        




    def set_electrode_mask_values(self, p2: 'GXDB', p3: str, p4: int, p5: 'GXVV', p6: 'GXVV', p7: 'GXVV', p8: 'GXVV') -> None:
        self._wrapper.set_electrode_mask_values(p2._wrapper, p3.encode(), p4, p5._wrapper, p6._wrapper, p7._wrapper, p8._wrapper)
        




    def set_electrode_mask_values_single_qc_channel(self, p2: 'GXDB', p3: str, p4: int, p5: int, p6: 'GXVV', p7: 'GXVV', p8: 'GXVV') -> None:
        self._wrapper.set_electrode_mask_values_single_qc_channel(p2._wrapper, p3.encode(), p4, p5, p6._wrapper, p7._wrapper, p8._wrapper)
        



    @classmethod
    def get_qc_channel(cls, p1: 'GXDB', p2: int, p3: str_ref) -> int:
        ret_val, p3.value = gxapi_cy.WrapIP.get_qc_channel(GXContext._get_tls_geo(), p1._wrapper, p2, p3.value.encode())
        return ret_val





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer