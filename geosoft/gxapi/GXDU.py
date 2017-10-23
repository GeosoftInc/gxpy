### extends 'class_empty.py'
from . import gxapi_cy

from geosoft.gxapi import GXContext, int_ref, float_ref, str_ref

### block Header
# NOTICE: The code generator will not replace the code in this block
### endblock Header

### block ClassImplementation
# NOTICE: Do not edit anything here, it is generated code
class GXDU:
    """
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._wrapper = None

    def __del__(self):
        self._wrapper = None

    def __init__(self, wrapper=None):
        self._wrapper = wrapper if wrapper else gxapi_cy.WrapDU(0)

    @classmethod
    def null(cls) -> 'GXDU':
        """
        A null (undefined) instance of :class:`GXDU`
        
        :returns: A null :class:`GX3DN`
        """
        return cls()

    def is_null(self) -> bool:
        """
        Check if the instance of :class:`GXDU` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of :class:`GXDU`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Miscellaneous


    @classmethod
    def table_look1(cls, p1: 'GXDB', p2: int, p3: int, p4: int, p5: str, p6: str, p7: int, p8: float, p9: 'GXTB') -> None:
        gxapi_cy.WrapDU.table_look1(GXContext._get_tls_geo(), p2, p3, p4, p5.encode(), p6.encode(), p7, p8, p9)
        



    @classmethod
    def table_look2(cls, p1: 'GXDB', p2: int, p3: int, p4: int, p5: int, p6: str, p7: str, p8: str, p9: int, p10: float, p11: 'GXTB') -> None:
        gxapi_cy.WrapDU.table_look2(GXContext._get_tls_geo(), p2, p3, p4, p5, p6.encode(), p7.encode(), p8.encode(), p9, p10, p11)
        



    @classmethod
    def table_look_i2(cls, p1: 'GXDB', p2: int, p3: int, p4: int, p5: int, p6: str, p7: str, p8: str, p9: int, p10: float, p11: 'GXTB') -> None:
        gxapi_cy.WrapDU.table_look_i2(GXContext._get_tls_geo(), p2, p3, p4, p5, p6.encode(), p7.encode(), p8.encode(), p9, p10, p11)
        



    @classmethod
    def table_look_r2(cls, p1: 'GXDB', p2: int, p3: float, p4: int, p5: int, p6: str, p7: str, p8: str, p9: int, p10: float, p11: 'GXTB') -> None:
        gxapi_cy.WrapDU.table_look_r2(GXContext._get_tls_geo(), p2, p3, p4, p5, p6.encode(), p7.encode(), p8.encode(), p9, p10, p11)
        



    @classmethod
    def ado_table_names(cls, p1: str, p2: 'GXVV') -> None:
        gxapi_cy.WrapDU.ado_table_names(GXContext._get_tls_geo(), p2)
        



    @classmethod
    def an_sig(cls, p1: 'GXDB', p2: int, p3: int, p4: int) -> None:
        gxapi_cy.WrapDU.an_sig(GXContext._get_tls_geo(), p2, p3, p4)
        



    @classmethod
    def append(cls, p1: 'GXDB', p2: 'GXDB', p3: int) -> None:
        gxapi_cy.WrapDU.append(GXContext._get_tls_geo(), p2, p3)
        



    @classmethod
    def avg_azimuth(cls, p1: 'GXDB', p2: float, p3: float_ref) -> None:
        p3.value = gxapi_cy.WrapDU.avg_azimuth(GXContext._get_tls_geo(), p2, p3.value)
        



    @classmethod
    def base_data(cls, p1: 'GXDB', p2: int, p3: int, p4: int, p5: int, p6: 'GXTB') -> None:
        gxapi_cy.WrapDU.base_data(GXContext._get_tls_geo(), p2, p3, p4, p5, p6)
        



    @classmethod
    def base_data_ex(cls, p1: 'GXDB', p2: int, p3: int, p4: int, p5: int, p6: 'GXTB', p7: int) -> None:
        gxapi_cy.WrapDU.base_data_ex(GXContext._get_tls_geo(), p2, p3, p4, p5, p6, p7)
        



    @classmethod
    def bound_line(cls, p1: 'GXDB', p2: int, p3: int, p4: int, p5: 'GXPLY') -> None:
        gxapi_cy.WrapDU.bound_line(GXContext._get_tls_geo(), p2, p3, p4, p5)
        



    @classmethod
    def bp_filt(cls, p1: 'GXDB', p2: int, p3: int, p4: int, p5: float, p6: float, p7: int) -> None:
        gxapi_cy.WrapDU.bp_filt(GXContext._get_tls_geo(), p2, p3, p4, p5, p6, p7)
        



    @classmethod
    def break_line(cls, p1: 'GXDB', p2: int, p3: int) -> None:
        gxapi_cy.WrapDU.break_line(GXContext._get_tls_geo(), p2, p3)
        



    @classmethod
    def break_line2(cls, p1: 'GXDB', p2: int, p3: int, p4: int) -> None:
        gxapi_cy.WrapDU.break_line2(GXContext._get_tls_geo(), p2, p3, p4)
        



    @classmethod
    def break_line_to_groups(cls, p1: 'GXDB', p2: int, p3: int, p4: str) -> None:
        gxapi_cy.WrapDU.break_line_to_groups(GXContext._get_tls_geo(), p2, p3, p4.encode())
        



    @classmethod
    def break_line_to_groups2(cls, p1: 'GXDB', p2: int, p3: int, p4: str, p5: int) -> None:
        gxapi_cy.WrapDU.break_line_to_groups2(GXContext._get_tls_geo(), p2, p3, p4.encode(), p5)
        



    @classmethod
    def b_spline(cls, p1: 'GXDB', p2: int, p3: int, p4: int, p5: float, p6: float, p7: float) -> None:
        gxapi_cy.WrapDU.b_spline(GXContext._get_tls_geo(), p2, p3, p4, p5, p6, p7)
        



    @classmethod
    def closest_point(cls, p1: 'GXDB', p2: float, p3: float, p4: float_ref, p5: float_ref, p6: int_ref, p7: float_ref) -> None:
        p4.value, p5.value, p6.value, p7.value = gxapi_cy.WrapDU.closest_point(GXContext._get_tls_geo(), p2, p3, p4.value, p5.value, p6.value, p7.value)
        



    @classmethod
    def copy_line(cls, p1: 'GXDB', p2: int, p3: int) -> None:
        gxapi_cy.WrapDU.copy_line(GXContext._get_tls_geo(), p2, p3)
        



    @classmethod
    def copy_line_across(cls, p1: 'GXDB', p2: int, p3: 'GXDB', p4: int) -> None:
        gxapi_cy.WrapDU.copy_line_across(GXContext._get_tls_geo(), p2, p3, p4)
        



    @classmethod
    def copy_line_chan_across(cls, p1: 'GXDB', p2: int, p3: 'GXVV', p4: 'GXDB', p5: int) -> None:
        gxapi_cy.WrapDU.copy_line_chan_across(GXContext._get_tls_geo(), p2, p3, p4, p5)
        



    @classmethod
    def copy_line_masked(cls, p1: 'GXDB', p2: int, p3: int, p4: int, p5: int) -> None:
        gxapi_cy.WrapDU.copy_line_masked(GXContext._get_tls_geo(), p2, p3, p4, p5)
        



    @classmethod
    def dao_table_names(cls, p1: str, p2: str, p3: 'GXVV') -> None:
        gxapi_cy.WrapDU.dao_table_names(GXContext._get_tls_geo(), p2.encode(), p3)
        



    @classmethod
    def decimate(cls, p1: 'GXDB', p2: int, p3: int, p4: int, p5: int) -> None:
        gxapi_cy.WrapDU.decimate(GXContext._get_tls_geo(), p2, p3, p4, p5)
        



    @classmethod
    def diff(cls, p1: 'GXDB', p2: int, p3: int, p4: int, p5: int) -> None:
        gxapi_cy.WrapDU.diff(GXContext._get_tls_geo(), p2, p3, p4, p5)
        



    @classmethod
    def distance(cls, p1: 'GXDB', p2: int, p3: int, p4: int, p5: int) -> None:
        gxapi_cy.WrapDU.distance(GXContext._get_tls_geo(), p2, p3, p4, p5)
        



    @classmethod
    def distance_3d(cls, p1: 'GXDB', p2: int, p3: int, p4: int, p5: int, p6: int, p7: int) -> None:
        gxapi_cy.WrapDU.distance_3d(GXContext._get_tls_geo(), p2, p3, p4, p5, p6, p7)
        



    @classmethod
    def distline(cls, p1: 'GXDB', p2: int, p3: int, p4: int, p5: float_ref) -> None:
        p5.value = gxapi_cy.WrapDU.distline(GXContext._get_tls_geo(), p2, p3, p4, p5.value)
        



    @classmethod
    def dup_chan_locks(cls, p1: 'GXDB', p2: 'GXDB') -> None:
        gxapi_cy.WrapDU.dup_chan_locks(GXContext._get_tls_geo(), p2)
        



    @classmethod
    def dup_chans(cls, p1: 'GXDB', p2: 'GXDB') -> None:
        gxapi_cy.WrapDU.dup_chans(GXContext._get_tls_geo(), p2)
        



    @classmethod
    def edit_duplicates(cls, p1: 'GXDB', p2: int, p3: int, p4: int, p5: int, p6: int, p7: float) -> None:
        gxapi_cy.WrapDU.edit_duplicates(GXContext._get_tls_geo(), p2, p3, p4, p5, p6, p7)
        



    @classmethod
    def export(cls, p1: 'GXDB', p2: int, p3: str, p4: 'GXVV', p5: int, p6: str, p7: int, p8: int) -> None:
        gxapi_cy.WrapDU.export(GXContext._get_tls_geo(), p2, p3.encode(), p4, p5, p6.encode(), p7, p8)
        



    @classmethod
    def export2(cls, p1: 'GXDB', p2: int, p3: str, p4: 'GXVV', p5: int, p6: str, p7: int, p8: int, p9: int) -> None:
        gxapi_cy.WrapDU.export2(GXContext._get_tls_geo(), p2, p3.encode(), p4, p5, p6.encode(), p7, p8, p9)
        



    @classmethod
    def export_amira(cls, p1: 'GXDB', p2: 'GXWA', p3: str, p4: str, p5: str, p6: str, p7: str, p8: str, p9: str, p10: str, p11: str) -> None:
        gxapi_cy.WrapDU.export_amira(GXContext._get_tls_geo(), p2, p3.encode(), p4.encode(), p5.encode(), p6.encode(), p7.encode(), p8.encode(), p9.encode(), p10.encode(), p11.encode())
        



    @classmethod
    def export_aseg(cls, p1: 'GXDB', p2: str, p3: 'GXVV', p4: int, p5: str, p6: str) -> None:
        gxapi_cy.WrapDU.export_aseg(GXContext._get_tls_geo(), p2.encode(), p3, p4, p5.encode(), p6.encode())
        



    @classmethod
    def export_aseg_proj(cls, p1: 'GXDB', p2: str, p3: 'GXVV', p4: int, p5: str, p6: str, p7: str, p8: 'GXIPJ') -> None:
        gxapi_cy.WrapDU.export_aseg_proj(GXContext._get_tls_geo(), p2.encode(), p3, p4, p5.encode(), p6.encode(), p7.encode(), p8)
        



    @classmethod
    def export_chan_crc(cls, p1: 'GXDB', p2: int, p3: int_ref, p4: str) -> None:
        p3.value = gxapi_cy.WrapDU.export_chan_crc(GXContext._get_tls_geo(), p2, p3.value, p4.encode())
        



    @classmethod
    def export_csv(cls, p1: 'GXDB', p2: str, p3: 'GXVV', p4: int, p5: str, p6: int, p7: int) -> None:
        gxapi_cy.WrapDU.export_csv(GXContext._get_tls_geo(), p2.encode(), p3, p4, p5.encode(), p6, p7)
        



    @classmethod
    def export_database_crc(cls, p1: 'GXDB', p2: int_ref, p3: str) -> None:
        p2.value = gxapi_cy.WrapDU.export_database_crc(GXContext._get_tls_geo(), p2.value, p3.encode())
        



    @classmethod
    def export_gbn(cls, p1: 'GXDB', p2: 'GXVV', p3: str) -> None:
        gxapi_cy.WrapDU.export_gbn(GXContext._get_tls_geo(), p2, p3.encode())
        



    @classmethod
    def export_mdb(cls, p1: 'GXDB', p2: str, p3: 'GXVV', p4: int, p5: int, p6: str) -> None:
        gxapi_cy.WrapDU.export_mdb(GXContext._get_tls_geo(), p2.encode(), p3, p4, p5, p6.encode())
        



    @classmethod
    def export_geodatabase(cls, p1: 'GXDB', p2: str, p3: str, p4: 'GXVV', p5: int, p6: int, p7: int, p8: str) -> None:
        gxapi_cy.WrapDU.export_geodatabase(GXContext._get_tls_geo(), p2.encode(), p3.encode(), p4, p5, p6, p7, p8.encode())
        



    @classmethod
    def get_existing_feature_classes_in_geodatabase(cls, p1: 'GXDB', p2: str, p3: 'GXLST', p4: 'GXVV') -> int:
        ret_val = gxapi_cy.WrapDU.get_existing_feature_classes_in_geodatabase(GXContext._get_tls_geo(), p2.encode(), p3, p4)
        return ret_val



    @classmethod
    def export_shp(cls, p1: 'GXDB', p2: str, p3: 'GXVV', p4: int, p5: int, p6: str, p7: 'GXLST') -> None:
        gxapi_cy.WrapDU.export_shp(GXContext._get_tls_geo(), p2.encode(), p3, p4, p5, p6.encode(), p7)
        



    @classmethod
    def export_xyz(cls, p1: 'GXDB', p2: str, p3: str) -> None:
        gxapi_cy.WrapDU.export_xyz(GXContext._get_tls_geo(), p2.encode(), p3.encode())
        



    @classmethod
    def export_xyz2(cls, p1: 'GXDB', p2: 'GXWA', p3: 'GXRA') -> None:
        gxapi_cy.WrapDU.export_xyz2(GXContext._get_tls_geo(), p2, p3)
        



    @classmethod
    def fft(cls, p1: 'GXDB', p2: int, p3: int, p4: int, p5: int) -> None:
        gxapi_cy.WrapDU.fft(GXContext._get_tls_geo(), p2, p3, p4, p5)
        



    @classmethod
    def filter(cls, p1: 'GXDB', p2: int, p3: int, p4: int, p5: int) -> None:
        gxapi_cy.WrapDU.filter(GXContext._get_tls_geo(), p2, p3, p4, p5)
        



    @classmethod
    def gen_lev(cls, p1: 'GXDB', p2: str, p3: str, p4: float, p5: int) -> None:
        gxapi_cy.WrapDU.gen_lev(GXContext._get_tls_geo(), p2.encode(), p3.encode(), p4, p5)
        



    @classmethod
    def gen_lev_db(cls, p1: 'GXDB', p2: str, p3: float, p4: int) -> None:
        gxapi_cy.WrapDU.gen_lev_db(GXContext._get_tls_geo(), p2.encode(), p3, p4)
        



    @classmethod
    def gen_xyz_temp(cls, p1: str, p2: str) -> None:
        gxapi_cy.WrapDU.gen_xyz_temp(GXContext._get_tls_geo(), p2.encode())
        



    @classmethod
    def get_xyz_num_fields(cls, p1: str, p2: int_ref) -> None:
        p2.value = gxapi_cy.WrapDU.get_xyz_num_fields(GXContext._get_tls_geo(), p2.value)
        



    @classmethod
    def get_chan_data_lst(cls, p1: 'GXDB', p2: int, p3: int, p4: 'GXLST') -> None:
        gxapi_cy.WrapDU.get_chan_data_lst(GXContext._get_tls_geo(), p2, p3, p4)
        



    @classmethod
    def get_chan_data_vv(cls, p1: 'GXDB', p2: int, p3: int, p4: 'GXVV') -> None:
        gxapi_cy.WrapDU.get_chan_data_vv(GXContext._get_tls_geo(), p2, p3, p4)
        



    @classmethod
    def gradient(cls, p1: 'GXDB', p2: 'GXDB', p3: int, p4: int, p5: int, p6: int, p7: int, p8: int, p9: int, p10: float, p11: float) -> None:
        gxapi_cy.WrapDU.gradient(GXContext._get_tls_geo(), p2, p3, p4, p5, p6, p7, p8, p9, p10, p11)
        



    @classmethod
    def grav_drift(cls, p1: 'GXDB', p2: int, p3: int, p4: int, p5: int, p6: int, p7: int) -> None:
        gxapi_cy.WrapDU.grav_drift(GXContext._get_tls_geo(), p2, p3, p4, p5, p6, p7)
        



    @classmethod
    def grav_tide(cls, p1: 'GXDB', p2: int, p3: int, p4: int, p5: int, p6: int, p7: float, p8: int) -> None:
        gxapi_cy.WrapDU.grav_tide(GXContext._get_tls_geo(), p2, p3, p4, p5, p6, p7, p8)
        



    @classmethod
    def grid_load(cls, p1: 'GXDB', p2: 'GXIMG', p3: int, p4: int, p5: int, p6: int) -> None:
        gxapi_cy.WrapDU.grid_load(GXContext._get_tls_geo(), p2, p3, p4, p5, p6)
        



    @classmethod
    def grid_load_xyz(cls, p1: 'GXDB', p2: 'GXIMG', p3: int, p4: int, p5: int, p6: int, p7: int, p8: int, p9: int, p10: int) -> None:
        gxapi_cy.WrapDU.grid_load_xyz(GXContext._get_tls_geo(), p2, p3, p4, p5, p6, p7, p8, p9, p10)
        



    @classmethod
    def head(cls, p1: 'GXDB', p2: int, p3: int, p4: int, p5: 'GXTB', p6: float) -> None:
        gxapi_cy.WrapDU.head(GXContext._get_tls_geo(), p2, p3, p4, p5, p6)
        



    @classmethod
    def import_bin3(cls, p1: 'GXDB', p2: str, p3: str, p4: str_ref, p6: int, p7: float, p8: 'GXWA') -> None:
        p4.value = gxapi_cy.WrapDU.import_bin3(GXContext._get_tls_geo(), p2.encode(), p3.encode(), p4.value.encode(), p6, p7, p8)
        



    @classmethod
    def imp_cb_ply(cls, p1: 'GXDB', p2: 'GXPJ', p3: str, p4: int, p5: int) -> None:
        gxapi_cy.WrapDU.imp_cb_ply(GXContext._get_tls_geo(), p2, p3.encode(), p4, p5)
        



    @classmethod
    def import_ado(cls, p1: 'GXDB', p2: str, p3: str, p4: str, p5: str) -> None:
        gxapi_cy.WrapDU.import_ado(GXContext._get_tls_geo(), p2.encode(), p3.encode(), p4.encode(), p5.encode())
        



    @classmethod
    def import_all_ado(cls, p1: 'GXDB', p2: str, p3: int) -> None:
        gxapi_cy.WrapDU.import_all_ado(GXContext._get_tls_geo(), p2.encode(), p3)
        



    @classmethod
    def import_all_dao(cls, p1: 'GXDB', p2: str, p3: str, p4: int) -> None:
        gxapi_cy.WrapDU.import_all_dao(GXContext._get_tls_geo(), p2.encode(), p3.encode(), p4)
        



    @classmethod
    def import_amira(cls, p1: 'GXDB', p2: 'GXRA', p3: 'GXWA') -> None:
        gxapi_cy.WrapDU.import_amira(GXContext._get_tls_geo(), p2, p3)
        



    @classmethod
    def import_aseg(cls, p1: 'GXDB', p2: str, p3: str, p4: str, p5: str, p6: int) -> None:
        gxapi_cy.WrapDU.import_aseg(GXContext._get_tls_geo(), p2.encode(), p3.encode(), p4.encode(), p5.encode(), p6)
        



    @classmethod
    def import_aseg_proj(cls, p1: 'GXDB', p2: str, p3: str, p4: str, p5: str, p6: int, p7: str, p8: str, p9: str) -> None:
        gxapi_cy.WrapDU.import_aseg_proj(GXContext._get_tls_geo(), p2.encode(), p3.encode(), p4.encode(), p5.encode(), p6, p7.encode(), p8.encode(), p9.encode())
        



    @classmethod
    def import_bin(cls, p1: 'GXDB', p2: str, p3: str, p4: str, p5: int, p6: float) -> None:
        gxapi_cy.WrapDU.import_bin(GXContext._get_tls_geo(), p2.encode(), p3.encode(), p4.encode(), p5, p6)
        



    @classmethod
    def import_bin2(cls, p1: 'GXDB', p2: str, p3: str, p4: str, p5: int, p6: float, p7: 'GXWA') -> None:
        gxapi_cy.WrapDU.import_bin2(GXContext._get_tls_geo(), p2.encode(), p3.encode(), p4.encode(), p5, p6, p7)
        



    @classmethod
    def import_bin4(cls, p1: 'GXDB', p2: int, p3: str, p4: str, p5: str, p6: int, p7: float, p8: 'GXWA') -> None:
        gxapi_cy.WrapDU.import_bin4(GXContext._get_tls_geo(), p2, p3.encode(), p4.encode(), p5.encode(), p6, p7, p8)
        



    @classmethod
    def import_daarc500_serial(cls, p1: 'GXDB', p2: int, p3: str, p4: int, p5: int) -> None:
        gxapi_cy.WrapDU.import_daarc500_serial(GXContext._get_tls_geo(), p2, p3.encode(), p4, p5)
        



    @classmethod
    def import_daarc500_serial_gps(cls, p1: 'GXDB', p2: int, p3: str, p4: int) -> None:
        gxapi_cy.WrapDU.import_daarc500_serial_gps(GXContext._get_tls_geo(), p2, p3.encode(), p4)
        



    @classmethod
    def import_dao(cls, p1: 'GXDB', p2: str, p3: str, p4: str, p5: str, p6: str) -> None:
        gxapi_cy.WrapDU.import_dao(GXContext._get_tls_geo(), p2.encode(), p3.encode(), p4.encode(), p5.encode(), p6.encode())
        



    @classmethod
    def import_esri(cls, p1: 'GXDB', p2: str, p3: str, p4: str) -> None:
        gxapi_cy.WrapDU.import_esri(GXContext._get_tls_geo(), p2.encode(), p3.encode(), p4.encode())
        



    @classmethod
    def import_gbn(cls, p1: 'GXDB', p2: str) -> None:
        gxapi_cy.WrapDU.import_gbn(GXContext._get_tls_geo(), p2.encode())
        



    @classmethod
    def import_oddf(cls, p1: 'GXDB', p2: str) -> None:
        gxapi_cy.WrapDU.import_oddf(GXContext._get_tls_geo(), p2.encode())
        



    @classmethod
    def import_pico(cls, p1: 'GXDB', p2: str, p3: str, p4: int) -> None:
        gxapi_cy.WrapDU.import_pico(GXContext._get_tls_geo(), p2.encode(), p3.encode(), p4)
        



    @classmethod
    def import_ubc_mod_msh(cls, p1: 'GXDB', p2: str, p3: str, p4: int, p5: float) -> None:
        gxapi_cy.WrapDU.import_ubc_mod_msh(GXContext._get_tls_geo(), p2.encode(), p3.encode(), p4, p5)
        



    @classmethod
    def import_usgs_post(cls, p1: 'GXDB', p2: str) -> None:
        gxapi_cy.WrapDU.import_usgs_post(GXContext._get_tls_geo(), p2.encode())
        



    @classmethod
    def import_xyz(cls, p1: 'GXDB', p2: int, p3: str, p4: str) -> None:
        gxapi_cy.WrapDU.import_xyz(GXContext._get_tls_geo(), p2, p3.encode(), p4.encode())
        



    @classmethod
    def import_xyz2(cls, p1: 'GXDB', p2: int, p3: str, p4: str, p5: 'GXWA') -> None:
        gxapi_cy.WrapDU.import_xyz2(GXContext._get_tls_geo(), p2, p3.encode(), p4.encode(), p5)
        



    @classmethod
    def import_io_gas(cls, p1: 'GXDB', p2: str, p3: str) -> None:
        gxapi_cy.WrapDU.import_io_gas(GXContext._get_tls_geo(), p2.encode(), p3.encode())
        



    @classmethod
    def index_order(cls, p1: 'GXDB', p2: int, p3: int, p4: int) -> None:
        gxapi_cy.WrapDU.index_order(GXContext._get_tls_geo(), p2, p3, p4)
        



    @classmethod
    def interp(cls, p1: 'GXDB', p2: int, p3: int, p4: int, p5: int, p6: int) -> None:
        gxapi_cy.WrapDU.interp(GXContext._get_tls_geo(), p2, p3, p4, p5, p6)
        



    @classmethod
    def interp_gap(cls, p1: 'GXDB', p2: int, p3: int, p4: int, p5: int, p6: int, p7: int, p8: int) -> None:
        gxapi_cy.WrapDU.interp_gap(GXContext._get_tls_geo(), p2, p3, p4, p5, p6, p7, p8)
        



    @classmethod
    def intersect(cls, p1: 'GXDB', p2: int, p3: int, p4: int, p5: float, p6: str) -> None:
        gxapi_cy.WrapDU.intersect(GXContext._get_tls_geo(), p2, p3, p4, p5, p6.encode())
        



    @classmethod
    def intersect_all(cls, p1: 'GXDB', p2: int, p3: int, p4: int, p5: float, p6: str) -> None:
        gxapi_cy.WrapDU.intersect_all(GXContext._get_tls_geo(), p2, p3, p4, p5, p6.encode())
        



    @classmethod
    def intersect_gd_bto_tbl(cls, p1: str, p2: str) -> None:
        gxapi_cy.WrapDU.intersect_gd_bto_tbl(GXContext._get_tls_geo(), p2.encode())
        



    @classmethod
    def intersect_old(cls, p1: 'GXDB', p2: int, p3: int, p4: int, p5: str, p6: str) -> None:
        gxapi_cy.WrapDU.intersect_old(GXContext._get_tls_geo(), p2, p3, p4, p5.encode(), p6.encode())
        



    @classmethod
    def intersect_tb_lto_gdb(cls, p1: str, p2: str) -> None:
        gxapi_cy.WrapDU.intersect_tb_lto_gdb(GXContext._get_tls_geo(), p2.encode())
        



    @classmethod
    def lab_template(cls, p1: str, p2: str, p3: int, p4: str, p5: int, p6: int, p7: int, p8: int, p9: int) -> None:
        gxapi_cy.WrapDU.lab_template(GXContext._get_tls_geo(), p2.encode(), p3, p4.encode(), p5, p6, p7, p8, p9)
        



    @classmethod
    def load_gravity(cls, p1: 'GXDB', p2: 'GXREG', p3: int, p4: str) -> None:
        gxapi_cy.WrapDU.load_gravity(GXContext._get_tls_geo(), p2, p3, p4.encode())
        



    @classmethod
    def load_ltb(cls, p1: 'GXDB', p2: int, p3: 'GXLTB', p4: int) -> None:
        gxapi_cy.WrapDU.load_ltb(GXContext._get_tls_geo(), p2, p3, p4)
        



    @classmethod
    def make_fid(cls, p1: 'GXDB', p2: int, p3: int, p4: int) -> None:
        gxapi_cy.WrapDU.make_fid(GXContext._get_tls_geo(), p2, p3, p4)
        



    @classmethod
    def mask(cls, p1: 'GXDB', p2: int, p3: int, p4: int) -> None:
        gxapi_cy.WrapDU.mask(GXContext._get_tls_geo(), p2, p3, p4)
        



    @classmethod
    def math(cls, p1: 'GXDB', p2: int, p3: 'GXEXP') -> None:
        gxapi_cy.WrapDU.math(GXContext._get_tls_geo(), p2, p3)
        



    @classmethod
    def merge_line(cls, p1: 'GXDB', p2: int, p3: int, p4: int, p5: int) -> None:
        gxapi_cy.WrapDU.merge_line(GXContext._get_tls_geo(), p2, p3, p4, p5)
        



    @classmethod
    def mod_fid_range(cls, p1: 'GXDB', p2: int, p3: float, p4: float, p5: int, p6: int, p7: int) -> None:
        gxapi_cy.WrapDU.mod_fid_range(GXContext._get_tls_geo(), p2, p3, p4, p5, p6, p7)
        



    @classmethod
    def move(cls, p1: 'GXDB', p2: int, p3: int, p4: int, p5: int, p6: int) -> None:
        gxapi_cy.WrapDU.move(GXContext._get_tls_geo(), p2, p3, p4, p5, p6)
        



    @classmethod
    def nl_filt(cls, p1: 'GXDB', p2: int, p3: int, p4: int, p5: int, p6: float) -> None:
        gxapi_cy.WrapDU.nl_filt(GXContext._get_tls_geo(), p2, p3, p4, p5, p6)
        



    @classmethod
    def normal(cls, p1: 'GXDB', p2: int, p3: int) -> None:
        gxapi_cy.WrapDU.normal(GXContext._get_tls_geo(), p2, p3)
        



    @classmethod
    def poly_fill(cls, p1: 'GXDB', p2: int, p3: int, p4: int, p5: int, p6: 'GXPLY', p7: int) -> None:
        gxapi_cy.WrapDU.poly_fill(GXContext._get_tls_geo(), p2, p3, p4, p5, p6, p7)
        



    @classmethod
    def poly_mask(cls, p1: 'GXDB', p2: int, p3: int, p4: int, p5: int, p6: 'GXPLY', p7: int) -> None:
        gxapi_cy.WrapDU.poly_mask(GXContext._get_tls_geo(), p2, p3, p4, p5, p6, p7)
        



    @classmethod
    def project_data(cls, p1: 'GXDB', p2: int, p3: int, p4: int, p5: int, p6: int, p7: 'GXPJ') -> None:
        gxapi_cy.WrapDU.project_data(GXContext._get_tls_geo(), p2, p3, p4, p5, p6, p7)
        



    @classmethod
    def project_xyz(cls, p1: 'GXDB', p2: int, p3: int, p4: int, p5: int, p6: int, p7: int, p8: int, p9: 'GXPJ') -> None:
        gxapi_cy.WrapDU.project_xyz(GXContext._get_tls_geo(), p2, p3, p4, p5, p6, p7, p8, p9)
        



    @classmethod
    def proj_points(cls, p1: 'GXDB', p2: int, p3: int, p4: int, p5: int, p6: int, p7: int, p8: int, p9: int, p10: int, p11: int, p12: int, p13: int, p14: int, p15: int, p16: int, p17: int, p18: int, p19: int, p20: int) -> None:
        gxapi_cy.WrapDU.proj_points(GXContext._get_tls_geo(), p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16, p17, p18, p19, p20)
        



    @classmethod
    def qc_init_separation(cls, p1: 'GXDB', p2: float, p3: float) -> None:
        gxapi_cy.WrapDU.qc_init_separation(GXContext._get_tls_geo(), p2, p3)
        



    @classmethod
    def qc_survey_plan(cls, p1: 'GXDB', p2: 'GXWA', p3: 'GXPLY', p4: float, p5: float, p6: float, p7: float, p8: int, p9: int, p10: float, p11: float, p12: float, p13: float, p14: int, p15: int, p16: int, p17: float, p18: float) -> int:
        ret_val = gxapi_cy.WrapDU.qc_survey_plan(GXContext._get_tls_geo(), p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16, p17, p18)
        return ret_val



    @classmethod
    def direction(cls, p1: 'GXDB', p2: int, p3: int, p4: int) -> float:
        ret_val = gxapi_cy.WrapDU.direction(GXContext._get_tls_geo(), p2, p3, p4)
        return ret_val



    @classmethod
    def re_fid(cls, p1: 'GXDB', p2: int, p3: int, p4: int, p5: int, p6: int, p7: float, p8: float, p9: float) -> None:
        gxapi_cy.WrapDU.re_fid(GXContext._get_tls_geo(), p2, p3, p4, p5, p6, p7, p8, p9)
        



    @classmethod
    def re_fid_all_ch(cls, p1: 'GXDB', p2: int, p3: int) -> None:
        gxapi_cy.WrapDU.re_fid_all_ch(GXContext._get_tls_geo(), p2, p3)
        



    @classmethod
    def re_fid_ch(cls, p1: 'GXDB', p2: int, p3: int, p4: int) -> None:
        gxapi_cy.WrapDU.re_fid_ch(GXContext._get_tls_geo(), p2, p3, p4)
        



    @classmethod
    def rotate(cls, p1: 'GXDB', p2: int, p3: int, p4: int, p5: int, p6: int, p7: float, p8: float, p9: float) -> None:
        gxapi_cy.WrapDU.rotate(GXContext._get_tls_geo(), p2, p3, p4, p5, p6, p7, p8, p9)
        



    @classmethod
    def sample_gd(cls, p1: 'GXDB', p2: int, p3: int, p4: int, p5: int, p6: 'GXGD') -> None:
        gxapi_cy.WrapDU.sample_gd(GXContext._get_tls_geo(), p2, p3, p4, p5, p6)
        



    @classmethod
    def sample_img(cls, p1: 'GXDB', p2: int, p3: int, p4: int, p5: int, p6: 'GXIMG') -> None:
        gxapi_cy.WrapDU.sample_img(GXContext._get_tls_geo(), p2, p3, p4, p5, p6)
        



    @classmethod
    def sample_img_line_lst(cls, p1: 'GXDB', p2: 'GXLST', p3: int, p4: int, p5: int, p6: 'GXIMG') -> None:
        gxapi_cy.WrapDU.sample_img_line_lst(GXContext._get_tls_geo(), p2, p3, p4, p5, p6)
        



    @classmethod
    def scan_ado(cls, p1: str, p2: str, p3: str) -> None:
        gxapi_cy.WrapDU.scan_ado(GXContext._get_tls_geo(), p2.encode(), p3.encode())
        



    @classmethod
    def scan_aseg(cls, p1: str, p2: str, p3: str, p4: str) -> None:
        gxapi_cy.WrapDU.scan_aseg(GXContext._get_tls_geo(), p2.encode(), p3.encode(), p4.encode())
        



    @classmethod
    def scan_dao(cls, p1: str, p2: str, p3: str, p4: str) -> None:
        gxapi_cy.WrapDU.scan_dao(GXContext._get_tls_geo(), p2.encode(), p3.encode(), p4.encode())
        



    @classmethod
    def scan_pico(cls, p1: str, p2: str) -> None:
        gxapi_cy.WrapDU.scan_pico(GXContext._get_tls_geo(), p2.encode())
        



    @classmethod
    def sort(cls, p1: 'GXDB', p2: int, p3: int, p4: int) -> None:
        gxapi_cy.WrapDU.sort(GXContext._get_tls_geo(), p2, p3, p4)
        



    @classmethod
    def sort_index(cls, p1: 'GXDB', p2: int, p3: int, p4: int, p5: int) -> None:
        gxapi_cy.WrapDU.sort_index(GXContext._get_tls_geo(), p2, p3, p4, p5)
        



    @classmethod
    def sort_index2(cls, p1: 'GXDB', p2: int, p3: int, p4: int, p5: int, p6: int, p7: int) -> None:
        gxapi_cy.WrapDU.sort_index2(GXContext._get_tls_geo(), p2, p3, p4, p5, p6, p7)
        



    @classmethod
    def split_line(cls, p1: 'GXDB', p2: int, p3: int, p4: float) -> None:
        gxapi_cy.WrapDU.split_line(GXContext._get_tls_geo(), p2, p3, p4)
        



    @classmethod
    def split_line2(cls, p1: 'GXDB', p2: int, p3: int, p4: float, p5: int) -> None:
        gxapi_cy.WrapDU.split_line2(GXContext._get_tls_geo(), p2, p3, p4, p5)
        



    @classmethod
    def split_line_xy(cls, p1: 'GXDB', p2: int, p3: int, p4: int, p5: int, p6: float, p7: float, p8: int, p9: int_ref, p10: int) -> None:
        p9.value = gxapi_cy.WrapDU.split_line_xy(GXContext._get_tls_geo(), p2, p3, p4, p5, p6, p7, p8, p9.value, p10)
        



    @classmethod
    def split_line_xy2(cls, p1: 'GXDB', p2: int, p3: int, p4: int, p5: int, p6: float, p7: float, p8: int, p9: int_ref, p10: int, p11: int) -> None:
        p9.value = gxapi_cy.WrapDU.split_line_xy2(GXContext._get_tls_geo(), p2, p3, p4, p5, p6, p7, p8, p9.value, p10, p11)
        



    @classmethod
    def split_line_xy3(cls, p1: 'GXDB', p2: int, p3: int, p4: int, p5: int, p6: float, p7: float, p8: int, p9: int_ref, p10: int, p11: int, p12: int) -> None:
        p9.value = gxapi_cy.WrapDU.split_line_xy3(GXContext._get_tls_geo(), p2, p3, p4, p5, p6, p7, p8, p9.value, p10, p11, p12)
        



    @classmethod
    def split_line_by_direction(cls, p1: 'GXDB', p2: int, p3: int, p4: int, p5: float, p6: float, p7: float, p8: float, p9: int, p10: int, p11: int_ref, p12: int, p13: int) -> None:
        p11.value = gxapi_cy.WrapDU.split_line_by_direction(GXContext._get_tls_geo(), p2, p3, p4, p5, p6, p7, p8, p9, p10, p11.value, p12, p13)
        



    @classmethod
    def split_line_by_direction2(cls, p1: 'GXDB', p2: int, p3: int, p4: int, p5: float, p6: float, p7: float, p8: float, p9: int, p10: int, p11: int_ref, p12: int, p13: int, p14: int) -> None:
        p11.value = gxapi_cy.WrapDU.split_line_by_direction2(GXContext._get_tls_geo(), p2, p3, p4, p5, p6, p7, p8, p9, p10, p11.value, p12, p13, p14)
        



    @classmethod
    def stat(cls, p1: 'GXDB', p2: int, p3: int, p4: 'GXST') -> None:
        gxapi_cy.WrapDU.stat(GXContext._get_tls_geo(), p2, p3, p4)
        



    @classmethod
    def table_line_fid(cls, p1: 'GXDB', p2: int, p3: int, p4: 'GXTB', p5: int) -> None:
        gxapi_cy.WrapDU.table_line_fid(GXContext._get_tls_geo(), p2, p3, p4, p5)
        



    @classmethod
    def table_selected_lines_fid(cls, p1: 'GXDB', p2: int, p3: int, p4: 'GXTB', p5: int) -> None:
        gxapi_cy.WrapDU.table_selected_lines_fid(GXContext._get_tls_geo(), p2, p3, p4, p5)
        



    @classmethod
    def time_constant(cls, p1: 'GXDB', p2: int, p3: int, p4: int, p5: int, p6: int, p7: int, p8: int) -> None:
        gxapi_cy.WrapDU.time_constant(GXContext._get_tls_geo(), p2, p3, p4, p5, p6, p7, p8)
        



    @classmethod
    def trend(cls, p1: 'GXDB', p2: int, p3: int, p4: int, p5: int) -> None:
        gxapi_cy.WrapDU.trend(GXContext._get_tls_geo(), p2, p3, p4, p5)
        



    @classmethod
    def update_intersect_db(cls, p1: 'GXDB', p2: int, p3: int, p4: 'GXDB') -> None:
        gxapi_cy.WrapDU.update_intersect_db(GXContext._get_tls_geo(), p2, p3, p4)
        



    @classmethod
    def voxel_section(cls, p1: 'GXDB', p2: int, p3: int, p4: int, p5: 'GXVOX', p6: str, p7: float, p8: float, p9: int) -> None:
        gxapi_cy.WrapDU.voxel_section(GXContext._get_tls_geo(), p2, p3, p4, p5, p6.encode(), p7, p8, p9)
        



    @classmethod
    def write_wa(cls, p1: 'GXDB', p2: int, p3: 'GXLST', p4: 'GXWA') -> None:
        gxapi_cy.WrapDU.write_wa(GXContext._get_tls_geo(), p2, p3, p4)
        



    @classmethod
    def xyz_line(cls, p1: 'GXDB', p2: int, p3: int, p4: int, p5: int, p6: float) -> None:
        gxapi_cy.WrapDU.xyz_line(GXContext._get_tls_geo(), p2, p3, p4, p5, p6)
        



    @classmethod
    def xyz_line2(cls, p1: 'GXDB', p2: int, p3: int, p4: int, p5: int, p6: float, p7: float) -> None:
        gxapi_cy.WrapDU.xyz_line2(GXContext._get_tls_geo(), p2, p3, p4, p5, p6, p7)
        



    @classmethod
    def xyz_line3(cls, p1: 'GXDB', p2: int, p3: int, p4: int, p5: int, p6: float, p7: float, p8: int) -> None:
        gxapi_cy.WrapDU.xyz_line3(GXContext._get_tls_geo(), p2, p3, p4, p5, p6, p7, p8)
        



    @classmethod
    def z_mask(cls, p1: 'GXDB', p2: int, p3: int, p4: int, p5: float, p6: float) -> None:
        gxapi_cy.WrapDU.z_mask(GXContext._get_tls_geo(), p2, p3, p4, p5, p6)
        



    @classmethod
    def range_xy(cls, p1: 'GXDB', p2: float_ref, p3: float_ref, p4: float_ref, p5: float_ref) -> None:
        p2.value, p3.value, p4.value, p5.value = gxapi_cy.WrapDU.range_xy(GXContext._get_tls_geo(), p2.value, p3.value, p4.value, p5.value)
        



    @classmethod
    def range_xyz(cls, p1: 'GXDB', p2: int, p3: int, p4: int, p5: float_ref, p6: float_ref, p7: float_ref, p8: float_ref, p9: float_ref, p10: float_ref, p11: int_ref) -> None:
        p5.value, p6.value, p7.value, p8.value, p9.value, p10.value, p11.value = gxapi_cy.WrapDU.range_xyz(GXContext._get_tls_geo(), p2, p3, p4, p5.value, p6.value, p7.value, p8.value, p9.value, p10.value, p11.value)
        



    @classmethod
    def range_xyz_data(cls, p1: 'GXDB', p2: int, p3: int, p4: int, p5: int, p6: float_ref, p7: float_ref, p8: float_ref, p9: float_ref, p10: float_ref, p11: float_ref, p12: float_ref, p13: float_ref, p14: int_ref) -> None:
        p6.value, p7.value, p8.value, p9.value, p10.value, p11.value, p12.value, p13.value, p14.value = gxapi_cy.WrapDU.range_xyz_data(GXContext._get_tls_geo(), p2, p3, p4, p5, p6.value, p7.value, p8.value, p9.value, p10.value, p11.value, p12.value, p13.value, p14.value)
        



    @classmethod
    def create_drillhole_parameter_weight_constraint_database(cls, p1: 'GXDB', p2: int, p3: 'GXREG', p4: str) -> None:
        gxapi_cy.WrapDU.create_drillhole_parameter_weight_constraint_database(GXContext._get_tls_geo(), p2, p3, p4.encode())
        



    @classmethod
    def calculate_draped_survey_altitude(cls, p1: 'GXDB', p2: int, p3: int, p4: int, p5: 'GXIMG', p6: int, p7: float, p8: float, p9: float, p10: int, p11: float, p12: float) -> None:
        gxapi_cy.WrapDU.calculate_draped_survey_altitude(GXContext._get_tls_geo(), p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12)
        



    @classmethod
    def calculate_draped_survey_altitude2(cls, p1: 'GXDB', p2: int, p3: int, p4: int, p5: 'GXIMG', p6: int, p7: int, p8: float, p9: float, p10: float, p11: float, p12: int, p13: float, p14: float) -> None:
        gxapi_cy.WrapDU.calculate_draped_survey_altitude2(GXContext._get_tls_geo(), p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14)
        



    @classmethod
    def direct_grid_data_to_voxel(cls, p1: 'GXDB', p2: int, p3: int, p4: int, p5: int, p6: str, p7: float, p8: float, p9: float, p10: int, p11: int, p12: int, p13: float, p14: float, p15: float, p16: int) -> None:
        gxapi_cy.WrapDU.direct_grid_data_to_voxel(GXContext._get_tls_geo(), p2, p3, p4, p5, p6.encode(), p7, p8, p9, p10, p11, p12, p13, p14, p15, p16)
        



    @classmethod
    def direct_grid_item_counts_to_voxel(cls, p1: 'GXDB', p2: int, p3: int, p4: int, p5: int, p6: str, p7: float, p8: float, p9: float, p10: int, p11: int, p12: int, p13: float, p14: float, p15: float, p16: int) -> None:
        gxapi_cy.WrapDU.direct_grid_item_counts_to_voxel(GXContext._get_tls_geo(), p2, p3, p4, p5, p6.encode(), p7, p8, p9, p10, p11, p12, p13, p14, p15, p16)
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer