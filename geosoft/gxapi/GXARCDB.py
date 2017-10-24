### extends 'class_empty.py'
from . import gxapi_cy

from geosoft.gxapi import GXContext, int_ref, float_ref, str_ref

### block Header
# NOTICE: The code generator will not replace the code in this block
### endblock Header

### block ClassImplementation
# NOTICE: Do not edit anything here, it is generated code
class GXARCDB:
    """
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._wrapper = None

    def __del__(self):
        self._wrapper = None

    def __init__(self, wrapper=None):
        self._wrapper = wrapper if wrapper else gxapi_cy.WrapARCDB(GXContext._get_tls_geo(), 0)

    @classmethod
    def null(cls) -> 'GXARCDB':
        """
        A null (undefined) instance of :class:`GXARCDB`
        
        :returns: A null :class:`GX3DN`
        """
        return cls()

    def is_null(self) -> bool:
        """
        Check if the instance of :class:`GXARCDB` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of :class:`GXARCDB`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Miscellaneous



    def create_dat(self, p2: str, p3: str, p4: str) -> 'GXDAT':
        ret_val = self._wrapper.create_dat(p2.encode(), p3.encode(), p4.encode())
        return GXDAT(ret_val)




    def create_dat_3d(self, p2: str, p3: str, p4: str, p5: str) -> 'GXDAT':
        ret_val = self._wrapper.create_dat_3d(p2.encode(), p3.encode(), p4.encode(), p5.encode())
        return GXDAT(ret_val)



    @classmethod
    def current(cls) -> 'GXARCDB':
        ret_val = gxapi_cy.WrapARCDB.current(GXContext._get_tls_geo())
        return GXARCDB(ret_val)




    def export_to_db(self, p2: 'GXDB', p3: str, p4: str) -> None:
        self._wrapper.export_to_db(p2._wrapper, p3.encode(), p4.encode())
        




    def field_lst(self, p2: 'GXLST') -> None:
        self._wrapper.field_lst(p2._wrapper)
        



    @classmethod
    def from_i_unknown(cls, p1: int) -> 'GXARCDB':
        ret_val = gxapi_cy.WrapARCDB.from_i_unknown(GXContext._get_tls_geo(), p1)
        return GXARCDB(ret_val)




    def get_ipj(self, p2: 'GXIPJ') -> None:
        self._wrapper.get_ipj(p2._wrapper)
        




    def exist_field(self, p2: str) -> int:
        ret_val = self._wrapper.exist_field(p2.encode())
        return ret_val




    def get_i_unknown(self) -> int:
        ret_val = self._wrapper.get_i_unknown()
        return ret_val




    def import_chem_database_wizard(self, p2: str, p3: int) -> int:
        ret_val = self._wrapper.import_chem_database_wizard(p2.encode(), p3)
        return ret_val



    @classmethod
    def sel_tbl_ex_gui(cls, p1: int_ref) -> 'GXARCDB':
        ret_val, p1.value = gxapi_cy.WrapARCDB.sel_tbl_ex_gui(GXContext._get_tls_geo(), p1.value)
        return GXARCDB(ret_val)



    @classmethod
    def sel_tbl_gui(cls) -> 'GXARCDB':
        ret_val = gxapi_cy.WrapARCDB.sel_tbl_gui(GXContext._get_tls_geo())
        return GXARCDB(ret_val)





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer