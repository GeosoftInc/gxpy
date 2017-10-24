### extends 'class_empty.py'
### block ClassImports
# NOTICE: Do not edit anything here, it is generated code
from . import gxapi_cy
from geosoft.gxapi import GXContext, float_ref, int_ref, str_ref
from .GXLPT import GXLPT
from .GXMETA import GXMETA
from .GXREG import GXREG
### endblock ClassImports

### block Header
# NOTICE: The code generator will not replace the code in this block
### endblock Header

### block ClassImplementation
# NOTICE: Do not edit anything here, it is generated code
class GXMAP:
    """
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._wrapper = None

    def __del__(self):
        self._wrapper = None

    def __init__(self, wrapper=None):
        self._wrapper = wrapper if wrapper else gxapi_cy.WrapMAP(GXContext._get_tls_geo(), 0)

    @classmethod
    def null(cls) -> 'GXMAP':
        """
        A null (undefined) instance of :class:`GXMAP`
        
        :returns: A null :class:`GX3DN`
        """
        return cls()

    def is_null(self) -> bool:
        """
        Check if the instance of :class:`GXMAP` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of :class:`GXMAP`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Export



    def export_all_in_view(self, p2: str, p3: str, p4: float, p5: float, p6: int, p7: int, p8: str, p9: str) -> None:
        self._wrapper.export_all_in_view(p2.encode(), p3.encode(), p4, p5, p6, p7, p8.encode(), p9.encode())
        




    def export_all_raster(self, p2: str, p3: str, p4: int, p5: int, p6: float, p7: int, p8: int, p9: str, p10: str) -> None:
        self._wrapper.export_all_raster(p2.encode(), p3.encode(), p4, p5, p6, p7, p8, p9.encode(), p10.encode())
        




    def export_area_in_view(self, p2: str, p3: str, p4: float, p5: float, p6: int, p7: int, p8: float, p9: float, p10: float, p11: float, p12: str, p13: str) -> None:
        self._wrapper.export_area_in_view(p2.encode(), p3.encode(), p4, p5, p6, p7, p8, p9, p10, p11, p12.encode(), p13.encode())
        




    def export_area_raster(self, p2: str, p3: str, p4: float, p5: float, p6: float, p7: float, p8: int, p9: int, p10: float, p11: int, p12: int, p13: str, p14: str) -> None:
        self._wrapper.export_area_raster(p2.encode(), p3.encode(), p4, p5, p6, p7, p8, p9, p10, p11, p12, p13.encode(), p14.encode())
        




    def render_bitmap(self, p2: str, p3: float, p4: float, p5: float, p6: float, p7: str, p8: int) -> None:
        self._wrapper.render_bitmap(p2.encode(), p3, p4, p5, p6, p7.encode(), p8)
        




# 3D View



    def create_linked_3d_view(self, p2: 'GXMVIEW', p3: str, p4: float, p5: float, p6: float, p7: float) -> None:
        self._wrapper.create_linked_3d_view(p2._wrapper, p3.encode(), p4, p5, p6, p7)
        




# Miscellaneous



    def agg_list(self, p2: 'GXLST', p3: int) -> None:
        self._wrapper.agg_list(p2._wrapper, p3)
        




    def agg_list_ex(self, p2: 'GXLST', p3: int, p4: int) -> None:
        self._wrapper.agg_list_ex(p2._wrapper, p3, p4)
        




    def clean(self) -> None:
        self._wrapper.clean()
        




    def commit(self) -> None:
        self._wrapper.commit()
        




    def copy_map_to_view(self, p2: str, p3: str) -> None:
        self._wrapper.copy_map_to_view(p2.encode(), p3.encode())
        




    def crc_map(self, p2: int_ref, p3: str) -> None:
        p2.value = self._wrapper.crc_map(p2.value, p3.encode())
        



    @classmethod
    def create(cls, p1: str, p2: int) -> 'GXMAP':
        ret_val = gxapi_cy.WrapMAP.create(GXContext._get_tls_geo(), p1.encode(), p2)
        return GXMAP(ret_val)



    @classmethod
    def current(cls) -> 'GXMAP':
        ret_val = gxapi_cy.WrapMAP.current(GXContext._get_tls_geo())
        return GXMAP(ret_val)




    def delete_view(self, p2: str) -> None:
        self._wrapper.delete_view(p2.encode())
        






    def discard(self) -> None:
        self._wrapper.discard()
        




    def dup_map(self, p2: 'GXMAP', p3: int) -> None:
        self._wrapper.dup_map(p2._wrapper, p3)
        




    def get_lpt(self) -> 'GXLPT':
        ret_val = self._wrapper.get_lpt()
        return GXLPT(ret_val)




    def get_map_size(self, p2: float_ref, p3: float_ref, p4: float_ref, p5: float_ref) -> None:
        p2.value, p3.value, p4.value, p5.value = self._wrapper.get_map_size(p2.value, p3.value, p4.value, p5.value)
        




    def get_meta(self) -> 'GXMETA':
        ret_val = self._wrapper.get_meta()
        return GXMETA(ret_val)




    def get_reg(self) -> 'GXREG':
        ret_val = self._wrapper.get_reg()
        return GXREG(ret_val)




    def group_list(self, p2: 'GXLST') -> None:
        self._wrapper.group_list(p2._wrapper)
        




    def group_list_ex(self, p2: 'GXLST', p3: int) -> None:
        self._wrapper.group_list_ex(p2._wrapper, p3)
        




    def duplicate_view(self, p2: str, p3: str_ref, p5: int) -> None:
        p3.value = self._wrapper.duplicate_view(p2.encode(), p3.value.encode(), p5)
        




    def exist_view(self, p2: str) -> int:
        ret_val = self._wrapper.exist_view(p2.encode())
        return ret_val




    def get_class_name(self, p2: str, p3: str_ref) -> None:
        p3.value = self._wrapper.get_class_name(p2.encode(), p3.value.encode())
        




    def get_file_name(self, p2: str_ref) -> None:
        p2.value = self._wrapper.get_file_name(p2.value.encode())
        




    def get_map_name(self, p2: str_ref) -> None:
        p2.value = self._wrapper.get_map_name(p2.value.encode())
        




    def packed_files(self) -> int:
        ret_val = self._wrapper.packed_files()
        return ret_val




    def un_pack_files_ex(self, p2: int, p3: str_ref) -> None:
        p3.value = self._wrapper.un_pack_files_ex(p2, p3.value.encode())
        




    def un_pack_files_to_folder(self, p2: int, p3: str, p4: str_ref) -> None:
        p4.value = self._wrapper.un_pack_files_to_folder(p2, p3.encode(), p4.value.encode())
        




    def pack_files(self) -> None:
        self._wrapper.pack_files()
        




    def render(self, p2: str) -> None:
        self._wrapper.render(p2.encode())
        




    def resize_all(self) -> None:
        self._wrapper.resize_all()
        




    def resize_all_ex(self, p2: int) -> None:
        self._wrapper.resize_all_ex(p2)
        




    def get_map_scale(self) -> float:
        ret_val = self._wrapper.get_map_scale()
        return ret_val




    def save_as_mxd(self, p2: str) -> None:
        self._wrapper.save_as_mxd(p2.encode())
        




    def set_class_name(self, p2: str, p3: str) -> None:
        self._wrapper.set_class_name(p2.encode(), p3.encode())
        




    def set_current(self) -> None:
        self._wrapper.set_current()
        




    def set_map_name(self, p2: str) -> None:
        self._wrapper.set_map_name(p2.encode())
        




    def set_map_scale(self, p2: float) -> None:
        self._wrapper.set_map_scale(p2)
        




    def set_map_size(self, p2: float, p3: float, p4: float, p5: float) -> None:
        self._wrapper.set_map_size(p2, p3, p4, p5)
        




    def set_meta(self, p2: 'GXMETA') -> None:
        self._wrapper.set_meta(p2._wrapper)
        




    def set_reg(self, p2: 'GXREG') -> None:
        self._wrapper.set_reg(p2._wrapper)
        



    @classmethod
    def sync(cls, p1: str) -> None:
        gxapi_cy.WrapMAP.sync(GXContext._get_tls_geo(), p1.encode())
        




    def un_pack_files(self) -> None:
        self._wrapper.un_pack_files()
        




    def view_list(self, p2: 'GXLST') -> None:
        self._wrapper.view_list(p2._wrapper)
        




    def view_list_ex(self, p2: 'GXLST', p3: int) -> None:
        self._wrapper.view_list_ex(p2._wrapper, p3)
        




    def get_data_proj(self) -> int:
        ret_val = self._wrapper.get_data_proj()
        return ret_val





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer