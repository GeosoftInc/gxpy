### extends 'class_empty.py'
from . import gxapi_cy

from geosoft.gxapi import GXContext, int_ref, float_ref, str_ref

### block Header
# NOTICE: The code generator will not replace the code in this block
### endblock Header

### block ClassImplementation
# NOTICE: Do not edit anything here, it is generated code
class GXIMG:
    """
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._wrapper = None

    def __del__(self):
        self._wrapper = None

    def __init__(self, wrapper=None):
        self._wrapper = wrapper if wrapper else gxapi_cy.WrapIMG(0)

    @classmethod
    def null(cls) -> 'GXIMG':
        """
        A null (undefined) instance of :class:`GXIMG`
        
        :returns: A null :class:`GX3DN`
        """
        return cls()

    def is_null(self) -> bool:
        """
        Check if the instance of :class:`GXIMG` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of :class:`GXIMG`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Miscellaneous


    @classmethod
    def average2(cls, p1: str, p2: str) -> None:
        gxapi_cy.WrapIMG.average2(GXContext._get_tls_geo(), p2.encode())
        




    def copy(self, p2: 'GXIMG') -> None:
        self._wrapper.copy(p2)
        



    @classmethod
    def create(cls, p1: int, p2: int, p3: int, p4: int) -> 'GXIMG':
        ret_val = gxapi_cy.WrapIMG.create(GXContext._get_tls_geo(), p2, p3, p4)
        return GXIMG(ret_val)



    @classmethod
    def create_file(cls, p1: int, p2: str, p3: int) -> 'GXIMG':
        ret_val = gxapi_cy.WrapIMG.create_file(GXContext._get_tls_geo(), p2.encode(), p3)
        return GXIMG(ret_val)



    @classmethod
    def create_mem(cls, p1: int, p2: int, p3: int, p4: int) -> 'GXIMG':
        ret_val = gxapi_cy.WrapIMG.create_mem(GXContext._get_tls_geo(), p2, p3, p4)
        return GXIMG(ret_val)



    @classmethod
    def create_new_file(cls, p1: int, p2: int, p3: int, p4: int, p5: str) -> 'GXIMG':
        ret_val = gxapi_cy.WrapIMG.create_new_file(GXContext._get_tls_geo(), p2, p3, p4, p5.encode())
        return GXIMG(ret_val)



    @classmethod
    def create_out_file(cls, p1: int, p2: str, p3: 'GXIMG') -> 'GXIMG':
        ret_val = gxapi_cy.WrapIMG.create_out_file(GXContext._get_tls_geo(), p2.encode(), p3)
        return GXIMG(ret_val)




    def create_projected(self, p2: 'GXIPJ') -> None:
        self._wrapper.create_projected(p2)
        




    def create_projected2(self, p2: 'GXIPJ', p3: float) -> None:
        self._wrapper.create_projected2(p2, p3)
        




    def create_projected3(self, p2: 'GXIPJ', p3: float, p4: float) -> None:
        self._wrapper.create_projected3(p2, p3, p4)
        






    def geth_pg(self) -> 'GXPG':
        ret_val = self._wrapper.geth_pg()
        return GXPG(ret_val)




    def get_info(self, p2: float_ref, p3: float_ref, p4: float_ref, p5: float_ref, p6: float_ref) -> None:
        p2.value, p3.value, p4.value, p5.value, p6.value = self._wrapper.get_info(p2.value, p3.value, p4.value, p5.value, p6.value)
        




    def get_ipj(self, p2: 'GXIPJ') -> None:
        self._wrapper.get_ipj(p2)
        




    def get_meta(self, p2: 'GXMETA') -> None:
        self._wrapper.get_meta(p2)
        




    def get_pg(self, p2: 'GXPG') -> None:
        self._wrapper.get_pg(p2)
        




    def get_projected_cell_size(self, p2: 'GXIPJ', p3: float_ref) -> None:
        p3.value = self._wrapper.get_projected_cell_size(p2, p3.value)
        




    def get_tr(self, p2: 'GXTR') -> None:
        self._wrapper.get_tr(p2)
        




    def element_type(self, p2: int) -> int:
        ret_val = self._wrapper.element_type(p2)
        return ret_val




    def e_type(self) -> int:
        ret_val = self._wrapper.e_type()
        return ret_val




    def get_def_itr(self, p2: 'GXITR') -> int:
        ret_val = self._wrapper.get_def_itr(p2)
        return ret_val




    def is_colour(self) -> int:
        ret_val = self._wrapper.is_colour()
        return ret_val



    @classmethod
    def is_valid_img_file(cls, p1: str) -> int:
        ret_val = gxapi_cy.WrapIMG.is_valid_img_file(GXContext._get_tls_geo())
        return ret_val



    @classmethod
    def is_valid_img_file_ex(cls, p1: str, p2: str_ref) -> int:
        ret_val, p2.value = gxapi_cy.WrapIMG.is_valid_img_file_ex(GXContext._get_tls_geo(), p2.value.encode())
        return ret_val




    def ne(self) -> int:
        ret_val = self._wrapper.ne()
        return ret_val




    def inherit(self, p2: 'GXIPJ', p3: float) -> None:
        self._wrapper.inherit(p2, p3)
        




    def inherit_img(self, p2: 'GXIMG') -> None:
        self._wrapper.inherit_img(p2)
        




    def nv(self) -> int:
        ret_val = self._wrapper.nv()
        return ret_val




    def nx(self) -> int:
        ret_val = self._wrapper.nx()
        return ret_val




    def ny(self) -> int:
        ret_val = self._wrapper.ny()
        return ret_val




    def query(self, p2: int) -> int:
        ret_val = self._wrapper.query(p2)
        return ret_val




    def query_kx(self) -> int:
        ret_val = self._wrapper.query_kx()
        return ret_val




    def set_def_itr(self, p2: 'GXITR') -> int:
        ret_val = self._wrapper.set_def_itr(p2)
        return ret_val



    @classmethod
    def user_preference_to_plot_as_colour_shaded_grid(cls) -> int:
        ret_val = gxapi_cy.WrapIMG.user_preference_to_plot_as_colour_shaded_grid(GXContext._get_tls_geo())
        return ret_val




    def load_img(self, p2: 'GXIMG') -> None:
        self._wrapper.load_img(p2)
        




    def load_into_pager(self) -> None:
        self._wrapper.load_into_pager()
        




    def opt_kx(self, p2: int) -> None:
        self._wrapper.opt_kx(p2)
        




    def read_v(self, p2: int, p3: int, p4: int, p5: 'GXVV') -> None:
        self._wrapper.read_v(p2, p3, p4, p5)
        




    def read_x(self, p2: int, p3: int, p4: int, p5: 'GXVV') -> None:
        self._wrapper.read_x(p2, p3, p4, p5)
        




    def read_y(self, p2: int, p3: int, p4: int, p5: 'GXVV') -> None:
        self._wrapper.read_y(p2, p3, p4, p5)
        



    @classmethod
    def refresh_gi(cls, p1: str) -> None:
        gxapi_cy.WrapIMG.refresh_gi(GXContext._get_tls_geo())
        




    def relocate(self, p2: float, p3: float, p4: float, p5: float, p6: int) -> None:
        self._wrapper.relocate(p2, p3, p4, p5, p6)
        



    @classmethod
    def report(cls, p1: str, p2: 'GXWA', p3: int, p4: int, p5: str) -> None:
        gxapi_cy.WrapIMG.report(GXContext._get_tls_geo(), p2, p3, p4, p5.encode())
        



    @classmethod
    def report_csv(cls, p1: str, p2: 'GXWA', p3: int, p4: int, p5: int) -> None:
        gxapi_cy.WrapIMG.report_csv(GXContext._get_tls_geo(), p2, p3, p4, p5)
        




    def get_z(self, p2: float, p3: float) -> float:
        ret_val = self._wrapper.get_z(p2, p3)
        return ret_val




    def query(self, p2: int) -> float:
        ret_val = self._wrapper.query(p2)
        return ret_val




    def set_grid_unchanged(self) -> None:
        self._wrapper.set_grid_unchanged()
        




    def set_info(self, p2: float, p3: float, p4: float, p5: float, p6: float) -> None:
        self._wrapper.set_info(p2, p3, p4, p5, p6)
        




    def set_ipj(self, p2: 'GXIPJ') -> None:
        self._wrapper.set_ipj(p2)
        




    def set_meta(self, p2: 'GXMETA') -> None:
        self._wrapper.set_meta(p2)
        




    def set_pg(self, p2: 'GXPG') -> None:
        self._wrapper.set_pg(p2)
        




    def set_tr(self, p2: 'GXTR') -> None:
        self._wrapper.set_tr(p2)
        



    @classmethod
    def sync(cls, p1: str) -> None:
        gxapi_cy.WrapIMG.sync(GXContext._get_tls_geo())
        




    def write_v(self, p2: int, p3: int, p4: int, p5: 'GXVV') -> None:
        self._wrapper.write_v(p2, p3, p4, p5)
        




    def write_x(self, p2: int, p3: int, p4: int, p5: 'GXVV') -> None:
        self._wrapper.write_x(p2, p3, p4, p5)
        




    def write_y(self, p2: int, p3: int, p4: int, p5: 'GXVV') -> None:
        self._wrapper.write_y(p2, p3, p4, p5)
        




    def set_double_parameter(self, p2: str, p3: float) -> None:
        self._wrapper.set_double_parameter(p2.encode(), p3)
        




    def get_double_parameter(self, p2: str) -> float:
        ret_val = self._wrapper.get_double_parameter(p2.encode())
        return ret_val





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer