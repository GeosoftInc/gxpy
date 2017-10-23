### extends 'class_empty.py'
from . import gxapi_cy

from geosoft.gxapi import GXContext, int_ref, float_ref, str_ref

### block Header
# NOTICE: The code generator will not replace the code in this block
### endblock Header

### block ClassImplementation
# NOTICE: Do not edit anything here, it is generated code
class GXMULTIVOXSET:
    """
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._wrapper = None

    def __del__(self):
        self._wrapper = None

    def __init__(self, wrapper=None):
        self._wrapper = wrapper if wrapper else gxapi_cy.WrapMULTIVOXSET(0)

    @classmethod
    def null(cls) -> 'GXMULTIVOXSET':
        """
        A null (undefined) instance of :class:`GXMULTIVOXSET`
        
        :returns: A null :class:`GX3DN`
        """
        return cls()

    def is_null(self) -> bool:
        """
        Check if the instance of :class:`GXMULTIVOXSET` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of :class:`GXMULTIVOXSET`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Miscellaneous


    @classmethod
    def import_from_xyz(cls, p1: str, p2: 'GXRA', p3: int, p4: 'GXIPJ') -> None:
        gxapi_cy.WrapMULTIVOXSET.import_from_xyz(GXContext._get_tls_geo(), p1.encode(), p2._wrapper, p3, p4._wrapper)
        



    @classmethod
    def export_to_xyz(cls, p1: str, p2: str, p3: int, p4: int, p5: int, p6: int, p7: int) -> None:
        gxapi_cy.WrapMULTIVOXSET.export_to_xyz(GXContext._get_tls_geo(), p1.encode(), p2.encode(), p3, p4, p5, p6, p7)
        



    @classmethod
    def export_to_binary(cls, p1: str, p2: str, p3: int, p4: int, p5: int, p6: int, p7: int, p8: int) -> None:
        gxapi_cy.WrapMULTIVOXSET.export_to_binary(GXContext._get_tls_geo(), p1.encode(), p2.encode(), p3, p4, p5, p6, p7, p8)
        



    @classmethod
    def export_to_xml(cls, p1: str, p2: str) -> None:
        gxapi_cy.WrapMULTIVOXSET.export_to_xml(GXContext._get_tls_geo(), p1.encode(), p2.encode())
        



    @classmethod
    def check_equal_to_legacy_voxel(cls, p1: str, p2: str) -> None:
        gxapi_cy.WrapMULTIVOXSET.check_equal_to_legacy_voxel(GXContext._get_tls_geo(), p1.encode(), p2.encode())
        



    @classmethod
    def import_from_ubc(cls, p1: str, p2: str, p3: str, p4: float, p5: 'GXIPJ') -> None:
        gxapi_cy.WrapMULTIVOXSET.import_from_ubc(GXContext._get_tls_geo(), p1.encode(), p2.encode(), p3.encode(), p4, p5._wrapper)
        



    @classmethod
    def import_from_gocad(cls, p1: str, p2: str, p3: str, p4: 'GXIPJ', p5: int) -> None:
        gxapi_cy.WrapMULTIVOXSET.import_from_gocad(GXContext._get_tls_geo(), p1.encode(), p2.encode(), p3.encode(), p4._wrapper, p5)
        



    @classmethod
    def list_properties_gocad(cls, p1: str, p2: 'GXLST') -> None:
        gxapi_cy.WrapMULTIVOXSET.list_properties_gocad(GXContext._get_tls_geo(), p1.encode(), p2._wrapper)
        



    @classmethod
    def import_from_gdb(cls, p1: str, p2: 'GXDB', p3: int) -> None:
        gxapi_cy.WrapMULTIVOXSET.import_from_gdb(GXContext._get_tls_geo(), p1.encode(), p2._wrapper, p3)
        



    @classmethod
    def import_from_vector_gdb(cls, p1: str, p2: 'GXDB', p3: int, p4: int, p5: int, p6: int, p7: float, p8: float) -> None:
        gxapi_cy.WrapMULTIVOXSET.import_from_vector_gdb(GXContext._get_tls_geo(), p1.encode(), p2._wrapper, p3, p4, p5, p6, p7, p8)
        



    @classmethod
    def export_to_segy(cls, p1: str, p2: str, p3: str, p4: float) -> None:
        gxapi_cy.WrapMULTIVOXSET.export_to_segy(GXContext._get_tls_geo(), p1.encode(), p2.encode(), p3.encode(), p4)
        



    @classmethod
    def export_to_gdb(cls, p1: str, p2: 'GXDB', p3: str, p4: int, p5: int, p6: int, p7: int, p8: int) -> None:
        gxapi_cy.WrapMULTIVOXSET.export_to_gdb(GXContext._get_tls_geo(), p1.encode(), p2._wrapper, p3.encode(), p4, p5, p6, p7, p8)
        



    @classmethod
    def export_to_wa(cls, p1: str, p2: 'GXWA', p3: int, p4: int, p5: int, p6: int, p7: str) -> None:
        gxapi_cy.WrapMULTIVOXSET.export_to_wa(GXContext._get_tls_geo(), p1.encode(), p2._wrapper, p3, p4, p5, p6, p7.encode())
        



    @classmethod
    def convert_double_to_vector(cls, p1: str, p2: str, p3: str, p4: str, p5: float, p6: float, p7: int) -> None:
        gxapi_cy.WrapMULTIVOXSET.convert_double_to_vector(GXContext._get_tls_geo(), p1.encode(), p2.encode(), p3.encode(), p4.encode(), p5, p6, p7)
        



    @classmethod
    def convert_vector_to_double(cls, p1: str, p2: str, p3: str, p4: str) -> None:
        gxapi_cy.WrapMULTIVOXSET.convert_vector_to_double(GXContext._get_tls_geo(), p1.encode(), p2.encode(), p3.encode(), p4.encode())
        



    @classmethod
    def create_double_constant(cls, p1: str, p2: float, p3: float, p4: float, p5: float, p6: float, p7: float, p8: float, p9: int, p10: int, p11: int, p12: 'GXIPJ') -> None:
        gxapi_cy.WrapMULTIVOXSET.create_double_constant(GXContext._get_tls_geo(), p1.encode(), p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12._wrapper)
        



    @classmethod
    def create_thematic_constant(cls, p1: str, p2: int, p3: float, p4: float, p5: float, p6: float, p7: float, p8: float, p9: int, p10: int, p11: int, p12: 'GXIPJ') -> None:
        gxapi_cy.WrapMULTIVOXSET.create_thematic_constant(GXContext._get_tls_geo(), p1.encode(), p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12._wrapper)
        



    @classmethod
    def create_vector_constant(cls, p1: str, p2: float, p3: float, p4: float, p5: float, p6: float, p7: float, p8: float, p9: float, p10: float, p11: int, p12: int, p13: int, p14: 'GXIPJ') -> None:
        gxapi_cy.WrapMULTIVOXSET.create_vector_constant(GXContext._get_tls_geo(), p1.encode(), p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14._wrapper)
        



    @classmethod
    def create_double_constant_vv(cls, p1: str, p2: float, p3: float, p4: float, p5: float, p6: 'GXVV', p7: 'GXVV', p8: 'GXVV', p9: 'GXIPJ') -> None:
        gxapi_cy.WrapMULTIVOXSET.create_double_constant_vv(GXContext._get_tls_geo(), p1.encode(), p2, p3, p4, p5, p6._wrapper, p7._wrapper, p8._wrapper, p9._wrapper)
        



    @classmethod
    def create_thematic_constant_vv(cls, p1: str, p2: int, p3: float, p4: float, p5: float, p6: 'GXVV', p7: 'GXVV', p8: 'GXVV', p9: 'GXIPJ') -> None:
        gxapi_cy.WrapMULTIVOXSET.create_thematic_constant_vv(GXContext._get_tls_geo(), p1.encode(), p2, p3, p4, p5, p6._wrapper, p7._wrapper, p8._wrapper, p9._wrapper)
        



    @classmethod
    def create_vector_constant_vv(cls, p1: str, p2: float, p3: float, p4: float, p5: float, p6: float, p7: float, p8: 'GXVV', p9: 'GXVV', p10: 'GXVV', p11: 'GXIPJ') -> None:
        gxapi_cy.WrapMULTIVOXSET.create_vector_constant_vv(GXContext._get_tls_geo(), p1.encode(), p2, p3, p4, p5, p6, p7, p8._wrapper, p9._wrapper, p10._wrapper, p11._wrapper)
        



    @classmethod
    def export_to_voxel(cls, p1: str, p2: str, p3: str, p4: str) -> None:
        gxapi_cy.WrapMULTIVOXSET.export_to_voxel(GXContext._get_tls_geo(), p1.encode(), p2.encode(), p3.encode(), p4.encode())
        



    @classmethod
    def import_from_voxel(cls, p1: str, p2: str, p3: str, p4: str_ref) -> None:
        p4.value = gxapi_cy.WrapMULTIVOXSET.import_from_voxel(GXContext._get_tls_geo(), p1.encode(), p2.encode(), p3.encode(), p4.value.encode())
        



    @classmethod
    def import_from_datamine(cls, p1: str, p2: str, p3: 'GXIPJ', p4: str) -> None:
        gxapi_cy.WrapMULTIVOXSET.import_from_datamine(GXContext._get_tls_geo(), p1.encode(), p2.encode(), p3._wrapper, p4.encode())
        



    @classmethod
    def compute_default_cell_size(cls, p1: float, p2: float, p3: float, p4: float, p5: float, p6: float) -> float:
        ret_val = gxapi_cy.WrapMULTIVOXSET.compute_default_cell_size(GXContext._get_tls_geo(), p1, p2, p3, p4, p5, p6)
        return ret_val



    @classmethod
    def filter(cls, p1: str, p2: str, p3: int, p4: str, p5: int, p6: int) -> None:
        gxapi_cy.WrapMULTIVOXSET.filter(GXContext._get_tls_geo(), p1.encode(), p2.encode(), p3, p4.encode(), p5, p6)
        



    @classmethod
    def grid_direct_from_gdb(cls, p1: str, p2: float, p3: float, p4: float, p5: int, p6: int, p7: int, p8: float, p9: float, p10: float, p11: int, p12: 'GXDB', p13: int, p14: int, p15: int, p16: int) -> None:
        gxapi_cy.WrapMULTIVOXSET.grid_direct_from_gdb(GXContext._get_tls_geo(), p1.encode(), p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12._wrapper, p13, p14, p15, p16)
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer