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
class GXSQLSRV(gxapi_cy.WrapSQLSRV):
    """
    GXSQLSRV class.

    SQL Server and MSDE utility functions
    """

    def __init__(self, handle=0):
        super(GXSQLSRV, self).__init__(GXContext._get_tls_geo(), handle)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of `GXSQLSRV <geosoft.gxapi.GXSQLSRV>`
        
        :returns: A null `GXSQLSRV <geosoft.gxapi.GXSQLSRV>`
        :rtype:   GXSQLSRV
        """
        return GXSQLSRV()

    def is_null(self):
        """
        Check if this is a null (undefined) instance
        
        :returns: True if this is a null (undefined) instance, False otherwise.
        :rtype:   bool
        """
        return self._internal_handle() == 0



# Miscellaneous


    @classmethod
    def attach_mdf(cls, server, user, password, db, mdf_file_name, ldf_file_name):
        """
        Attaches an MDF SQL server file to a server.
        
        :param server:         SQL server to use
        :param user:           User name (if blank assume NT Integrated Security)
        :param password:       Password
        :param db:             `GXDB <geosoft.gxapi.GXDB>` name
        :param mdf_file_name:  MDF name
        :param ldf_file_name:  LDF name (if blank, tries single db attach)
        :type  server:         str
        :type  user:           str
        :type  password:       str
        :type  db:             str
        :type  mdf_file_name:  str
        :type  ldf_file_name:  str

        :returns:              0 - OK
                               1 - `GXDB <geosoft.gxapi.GXDB>` Operation Canceled
                               Terminates on Error
        :rtype:                int

        .. versionadded:: 5.1.8

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** The file's path need to be visible as local files on the server.
        Network drives and substitutes may not work.
        """
        ret_val = gxapi_cy.WrapSQLSRV._attach_mdf(GXContext._get_tls_geo(), server.encode(), user.encode(), password.encode(), db.encode(), mdf_file_name.encode(), ldf_file_name.encode())
        return ret_val



    @classmethod
    def detach_db(cls, server, user, password, db):
        """
        Detaches a SQL Server database from a server.
        
        :param server:    SQL server to use
        :param user:      User name (if blank assume NT Integrated Security)
        :param password:  Password
        :param db:        `GXDB <geosoft.gxapi.GXDB>` name
        :type  server:    str
        :type  user:      str
        :type  password:  str
        :type  db:        str

        :returns:         0 - OK
                          1 - `GXDB <geosoft.gxapi.GXDB>` Operation Canceled
        :rtype:           int

        .. versionadded:: 5.1.8

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        ret_val = gxapi_cy.WrapSQLSRV._detach_db(GXContext._get_tls_geo(), server.encode(), user.encode(), password.encode(), db.encode())
        return ret_val



    @classmethod
    def get_database_languages_lst(cls, lst, server, user, password, win_auth):
        """
        Get a list of the languages into `GXLST <geosoft.gxapi.GXLST>`
        
        :param server:    SQL server to use
        :param user:      User name
        :param password:  Password
        :param win_auth:  0 - SQL authentication, 1 - NT integrated securty
        :type  lst:       GXLST
        :type  server:    str
        :type  user:      str
        :type  password:  str
        :type  win_auth:  int

        :returns:         Number of languages
        :rtype:           int

        .. versionadded:: 5.1.8

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        ret_val = gxapi_cy.WrapSQLSRV._get_database_languages_lst(GXContext._get_tls_geo(), lst, server.encode(), user.encode(), password.encode(), win_auth)
        return ret_val



    @classmethod
    def get_databases_lst(cls, lst, server, user, password, win_auth):
        """
        Get a list of the database into `GXLST <geosoft.gxapi.GXLST>`
        
        :param server:    SQL server to use
        :param user:      User name
        :param password:  Password
        :param win_auth:  0 - SQL authentication, 1 - NT integrated securty
        :type  lst:       GXLST
        :type  server:    str
        :type  user:      str
        :type  password:  str
        :type  win_auth:  int

        :returns:         Number of database
        :rtype:           int

        .. versionadded:: 5.1.8

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        ret_val = gxapi_cy.WrapSQLSRV._get_databases_lst(GXContext._get_tls_geo(), lst, server.encode(), user.encode(), password.encode(), win_auth)
        return ret_val



    @classmethod
    def get_login_gui(cls, server, user, password, mode, win_auth):
        """
        Get/Test login information to SQL Server
        
        :param server:    SQL server to use
        :param user:      User name (default & returned)
        :param password:  Password (default & returned)
        :param mode:      :ref:`MFCSQL_DRIVER`
        :param win_auth:  Windows Authentication (default & returned)
        :type  server:    str
        :type  user:      str_ref
        :type  password:  str_ref
        :type  mode:      int
        :type  win_auth:  int_ref

        .. versionadded:: 5.1.8

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        user.value, password.value, win_auth.value = gxapi_cy.WrapSQLSRV._get_login_gui(GXContext._get_tls_geo(), server.encode(), user.value.encode(), password.value.encode(), mode, win_auth.value)
        



    @classmethod
    def get_servers_lst(cls, lst):
        """
        Get a list of the visible servers into `GXLST <geosoft.gxapi.GXLST>`
        
        :type  lst:  GXLST

        :returns:    Number of servers
        :rtype:      int

        .. versionadded:: 5.1.8

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        ret_val = gxapi_cy.WrapSQLSRV._get_servers_lst(GXContext._get_tls_geo(), lst)
        return ret_val





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer