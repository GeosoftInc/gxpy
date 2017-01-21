#include "stdafx.h"

using namespace boost::python;
using boost::python::init;


// Dummy classes


inline int32_t GXSQLSRV_wrap_attach_mdf(const gx_string_type& arg1, const gx_string_type& arg2, const gx_string_type& arg3, const gx_string_type& arg4, const gx_string_type& arg5, const gx_string_type& arg6)
{
    int32_t ret = GXSQLSRV::attach_mdf(arg1, arg2, arg3, arg4, arg5, arg6);
    return ret;
}
inline int32_t GXSQLSRV_wrap_detach_db(const gx_string_type& arg1, const gx_string_type& arg2, const gx_string_type& arg3, const gx_string_type& arg4)
{
    int32_t ret = GXSQLSRV::detach_db(arg1, arg2, arg3, arg4);
    return ret;
}
inline int32_t GXSQLSRV_wrap_get_database_languages_lst(GXLSTPtr arg1, const gx_string_type& arg2, const gx_string_type& arg3, const gx_string_type& arg4, int32_t arg5)
{
    int32_t ret = GXSQLSRV::get_database_languages_lst(arg1, arg2, arg3, arg4, arg5);
    return ret;
}
inline int32_t GXSQLSRV_wrap_get_databases_lst(GXLSTPtr arg1, const gx_string_type& arg2, const gx_string_type& arg3, const gx_string_type& arg4, int32_t arg5)
{
    int32_t ret = GXSQLSRV::get_databases_lst(arg1, arg2, arg3, arg4, arg5);
    return ret;
}
inline void GXSQLSRV_wrap_get_login_gui(const gx_string_type& arg1, str_ref& arg2, str_ref& arg3, int32_t arg4, int_ref& arg5)
{
    GXSQLSRV::get_login_gui(arg1, arg2, arg3, (MFCSQL_DRIVER)arg4, arg5);
}
inline int32_t GXSQLSRV_wrap_get_servers_lst(GXLSTPtr arg1)
{
    int32_t ret = GXSQLSRV::get_servers_lst(arg1);
    return ret;
}

void gxPythonImportGXSQLSRV()
{

    class_<GXSQLSRV, boost::noncopyable> pyClass("GXSQLSRV",
            "\n.. parsed-literal::\n\n"
            "   SQL Server and MSDE utility functions\n\n"
            , no_init);


    pyClass.def("attach_mdf", &GXSQLSRV_wrap_attach_mdf,
                "attach_mdf((str)arg1, (str)arg2, (str)arg3, (str)arg4, (str)arg5, (str)arg6) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Attaches an MDF SQL server file to a server.\n\n"

                ":param arg1: SQL server to use\n"
                ":type arg1: str\n"
                ":param arg2: User name (if blank assume NT Integrated Security)\n"
                ":type arg2: str\n"
                ":param arg3: Password\n"
                ":type arg3: str\n"
                ":param arg4: DB name\n"
                ":type arg4: str\n"
                ":param arg5: MDF name\n"
                ":type arg5: str\n"
                ":param arg6: LDF name (if blank, tries single db attach)\n"
                ":type arg6: str\n"
                ":returns: 0 - OK\n"
                "          1 - DB Operation Canceled\n"
                "          Terminates on Error\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.1.8\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   The file's path need to be visible as local files on the server.\n"
                "   Network drives and substitutes may not work.\n\n"
               ).staticmethod("attach_mdf");
    pyClass.def("detach_db", &GXSQLSRV_wrap_detach_db,
                "detach_db((str)arg1, (str)arg2, (str)arg3, (str)arg4) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Detaches a SQL Server database from a server.\n\n"

                ":param arg1: SQL server to use\n"
                ":type arg1: str\n"
                ":param arg2: User name (if blank assume NT Integrated Security)\n"
                ":type arg2: str\n"
                ":param arg3: Password\n"
                ":type arg3: str\n"
                ":param arg4: DB name\n"
                ":type arg4: str\n"
                ":returns: 0 - OK\n"
                "          1 - DB Operation Canceled\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.1.8\n\n"
               ).staticmethod("detach_db");
    pyClass.def("get_database_languages_lst", &GXSQLSRV_wrap_get_database_languages_lst,
                "get_database_languages_lst((GXLST)arg1, (str)arg2, (str)arg3, (str)arg4, (int)arg5) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Get a list of the languages into LST\n\n"

                ":param arg1: LST\n"
                ":type arg1: :class:`geosoft.gxapi.GXLST`\n"
                ":param arg2: SQL server to use\n"
                ":type arg2: str\n"
                ":param arg3: User name\n"
                ":type arg3: str\n"
                ":param arg4: Password\n"
                ":type arg4: str\n"
                ":param arg5: 0 - SQL authentication, 1 - NT integrated securty\n"
                ":type arg5: int\n"
                ":returns: Number of languages\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.1.8\n\n"
               ).staticmethod("get_database_languages_lst");
    pyClass.def("get_databases_lst", &GXSQLSRV_wrap_get_databases_lst,
                "get_databases_lst((GXLST)arg1, (str)arg2, (str)arg3, (str)arg4, (int)arg5) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Get a list of the database into LST\n\n"

                ":param arg1: LST\n"
                ":type arg1: :class:`geosoft.gxapi.GXLST`\n"
                ":param arg2: SQL server to use\n"
                ":type arg2: str\n"
                ":param arg3: User name\n"
                ":type arg3: str\n"
                ":param arg4: Password\n"
                ":type arg4: str\n"
                ":param arg5: 0 - SQL authentication, 1 - NT integrated securty\n"
                ":type arg5: int\n"
                ":returns: Number of database\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.1.8\n\n"
               ).staticmethod("get_databases_lst");
    pyClass.def("get_login_gui", &GXSQLSRV_wrap_get_login_gui,
                "get_login_gui((str)arg1, (str_ref)arg2, (str_ref)arg3, (int)arg4, (int_ref)arg5) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get/Test login information to SQL Server\n\n"

                ":param arg1: SQL server to use\n"
                ":type arg1: str\n"
                ":param arg2: User name (default & returned)\n"
                ":type arg2: :class:`geosoft.gxapi.str_ref`\n"
                ":param arg3: Password (default & returned)\n"
                ":type arg3: :class:`geosoft.gxapi.str_ref`\n"
                ":param arg4: \\ :ref:`MFCSQL_DRIVER`\\ \n"
                ":type arg4: int\n"
                ":param arg5: Windows Authentication (default & returned)\n"
                ":type arg5: :class:`geosoft.gxapi.int_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.8\n\n"
               ).staticmethod("get_login_gui");
    pyClass.def("get_servers_lst", &GXSQLSRV_wrap_get_servers_lst,
                "get_servers_lst((GXLST)arg1) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Get a list of the visible servers into LST\n\n"

                ":param arg1: LST\n"
                ":type arg1: :class:`geosoft.gxapi.GXLST`\n"
                ":returns: Number of servers\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.1.8\n\n"
               ).staticmethod("get_servers_lst");

    scope().attr("MFCSQL_DRIVER_NOPROMPT") = (int32_t)0;
    scope().attr("MFCSQL_DRIVER_COMPLETE") = (int32_t)1;
    scope().attr("MFCSQL_DRIVER_PROMPT") = (int32_t)2;
    scope().attr("MFCSQL_DRIVER_COMPLETE_REQUIRED") = (int32_t)3;

}
