### extends 'class_empty.py'
### block ClassImports
# NOTICE: Do not edit anything here, it is generated code
from typing import NewType
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
    GXSQLSRV class.

    SQL Server and MSDE utility functions
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
    def null(cls):
        """
        A null (undefined) instance of `GXSQLSRV`
        
        :returns: A null `GXSQLSRV`
        """
        return cls()

    def is_null(self):
        """
        Check if the instance of `GXSQLSRV` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of `GXSQLSRV`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Miscellaneous


    @classmethod
    def attach_mdf(cls, p1, p2, p3, p4, p5, p6):
        """
        Attaches an MDF SQL server file to a server.

        **Note:**

        The file's path need to be visible as local files on the server.
        Network drives and substitutes may not work.
        """
        ret_val = gxapi_cy.WrapSQLSRV.attach_mdf(GXContext._get_tls_geo(), p1.encode(), p2.encode(), p3.encode(), p4.encode(), p5.encode(), p6.encode())
        return ret_val



    @classmethod
    def detach_db(cls, p1, p2, p3, p4):
        """
        Detaches a SQL Server database from a server.
        """
        ret_val = gxapi_cy.WrapSQLSRV.detach_db(GXContext._get_tls_geo(), p1.encode(), p2.encode(), p3.encode(), p4.encode())
        return ret_val



    @classmethod
    def get_database_languages_lst(cls, p1, p2, p3, p4, p5):
        """
        Get a list of the languages into `GXLST`
        """
        ret_val = gxapi_cy.WrapSQLSRV.get_database_languages_lst(GXContext._get_tls_geo(), p1._wrapper, p2.encode(), p3.encode(), p4.encode(), p5)
        return ret_val



    @classmethod
    def get_databases_lst(cls, p1, p2, p3, p4, p5):
        """
        Get a list of the database into `GXLST`
        """
        ret_val = gxapi_cy.WrapSQLSRV.get_databases_lst(GXContext._get_tls_geo(), p1._wrapper, p2.encode(), p3.encode(), p4.encode(), p5)
        return ret_val



    @classmethod
    def get_login_gui(cls, p1, p2, p4, p6, p7):
        """
        Get/Test login information to SQL Server
        """
        p2.value, p4.value, p7.value = gxapi_cy.WrapSQLSRV.get_login_gui(GXContext._get_tls_geo(), p1.encode(), p2.value.encode(), p4.value.encode(), p6, p7.value)
        



    @classmethod
    def get_servers_lst(cls, p1):
        """
        Get a list of the visible servers into `GXLST`
        """
        ret_val = gxapi_cy.WrapSQLSRV.get_servers_lst(GXContext._get_tls_geo(), p1._wrapper)
        return ret_val





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer