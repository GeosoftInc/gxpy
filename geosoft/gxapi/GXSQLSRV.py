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
    def attach_mdf(cls, server, user, password, db, mdf_file_name, ldf_file_name):
        """
        Attaches an MDF SQL server file to a server.

        **Note:**

        The file's path need to be visible as local files on the server.
        Network drives and substitutes may not work.
        """
        ret_val = gxapi_cy.WrapSQLSRV.attach_mdf(GXContext._get_tls_geo(), server.encode(), user.encode(), password.encode(), db.encode(), mdf_file_name.encode(), ldf_file_name.encode())
        return ret_val



    @classmethod
    def detach_db(cls, server, user, password, db):
        """
        Detaches a SQL Server database from a server.
        """
        ret_val = gxapi_cy.WrapSQLSRV.detach_db(GXContext._get_tls_geo(), server.encode(), user.encode(), password.encode(), db.encode())
        return ret_val



    @classmethod
    def get_database_languages_lst(cls, lst, server, user, password, win_auth):
        """
        Get a list of the languages into `GXLST`
        """
        ret_val = gxapi_cy.WrapSQLSRV.get_database_languages_lst(GXContext._get_tls_geo(), lst._wrapper, server.encode(), user.encode(), password.encode(), win_auth)
        return ret_val



    @classmethod
    def get_databases_lst(cls, lst, server, user, password, win_auth):
        """
        Get a list of the database into `GXLST`
        """
        ret_val = gxapi_cy.WrapSQLSRV.get_databases_lst(GXContext._get_tls_geo(), lst._wrapper, server.encode(), user.encode(), password.encode(), win_auth)
        return ret_val



    @classmethod
    def get_login_gui(cls, server, user, password, mode, win_auth):
        """
        Get/Test login information to SQL Server
        """
        user.value, password.value, win_auth.value = gxapi_cy.WrapSQLSRV.get_login_gui(GXContext._get_tls_geo(), server.encode(), user.value.encode(), password.value.encode(), mode, win_auth.value)
        



    @classmethod
    def get_servers_lst(cls, lst):
        """
        Get a list of the visible servers into `GXLST`
        """
        ret_val = gxapi_cy.WrapSQLSRV.get_servers_lst(GXContext._get_tls_geo(), lst._wrapper)
        return ret_val





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer