### extends 'class_empty.py'
### block ClassImports
# NOTICE: Do not edit anything here, it is generated code
from . import gxapi_cy
from geosoft.gxapi import GXContext, float_ref, int_ref, str_ref

### endblock ClassImports

### block Header
# NOTICE: The code generator will not replace the code in this block
### endblock Header

### block ClassImplementation
# NOTICE: Do not edit anything here, it is generated code
class GXSQLSRV:
    """
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._wrapper = None

    def __del__(self):
        self._wrapper = None

    def __init__(self, wrapper=None):
        self._wrapper = wrapper if wrapper else gxapi_cy.WrapSQLSRV(GXContext._get_tls_geo(), 0)

    @classmethod
    def null(cls) -> 'GXSQLSRV':
        """
        A null (undefined) instance of :class:`GXSQLSRV`
        
        :returns: A null :class:`GX3DN`
        """
        return cls()

    def is_null(self) -> bool:
        """
        Check if the instance of :class:`GXSQLSRV` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of :class:`GXSQLSRV`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Miscellaneous


    @classmethod
    def attach_mdf(cls, p1: str, p2: str, p3: str, p4: str, p5: str, p6: str) -> int:
        ret_val = gxapi_cy.WrapSQLSRV.attach_mdf(GXContext._get_tls_geo(), p1.encode(), p2.encode(), p3.encode(), p4.encode(), p5.encode(), p6.encode())
        return ret_val



    @classmethod
    def detach_db(cls, p1: str, p2: str, p3: str, p4: str) -> int:
        ret_val = gxapi_cy.WrapSQLSRV.detach_db(GXContext._get_tls_geo(), p1.encode(), p2.encode(), p3.encode(), p4.encode())
        return ret_val



    @classmethod
    def get_database_languages_lst(cls, p1: 'GXLST', p2: str, p3: str, p4: str, p5: int) -> int:
        ret_val = gxapi_cy.WrapSQLSRV.get_database_languages_lst(GXContext._get_tls_geo(), p1._wrapper, p2.encode(), p3.encode(), p4.encode(), p5)
        return ret_val



    @classmethod
    def get_databases_lst(cls, p1: 'GXLST', p2: str, p3: str, p4: str, p5: int) -> int:
        ret_val = gxapi_cy.WrapSQLSRV.get_databases_lst(GXContext._get_tls_geo(), p1._wrapper, p2.encode(), p3.encode(), p4.encode(), p5)
        return ret_val



    @classmethod
    def get_login_gui(cls, p1: str, p2: str_ref, p4: str_ref, p6: int, p7: int_ref) -> None:
        p2.value, p4.value, p7.value = gxapi_cy.WrapSQLSRV.get_login_gui(GXContext._get_tls_geo(), p1.encode(), p2.value.encode(), p4.value.encode(), p6, p7.value)
        



    @classmethod
    def get_servers_lst(cls, p1: 'GXLST') -> int:
        ret_val = gxapi_cy.WrapSQLSRV.get_servers_lst(GXContext._get_tls_geo(), p1._wrapper)
        return ret_val





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer