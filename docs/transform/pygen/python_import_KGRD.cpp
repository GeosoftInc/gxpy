#include "stdafx.h"

using namespace boost::python;
using boost::python::init;


// Dummy classes


inline void GXKGRD_wrap_clear(GXKGRDPtr self)
{
    self->clear();
}
inline GXKGRDPtr GXKGRD_wrap_create()
{
    GXKGRDPtr ret = GXKGRD::create();
    return ret;
}
inline int32_t GXKGRD_wrap_load_parms(GXKGRDPtr self, const gx_string_type& arg1)
{
    int32_t ret = self->load_parms(arg1);
    return ret;
}
inline int32_t GXKGRD_wrap_run(GXKGRDPtr self, const gx_string_type& arg1, GXDATPtr arg2, GXDATPtr arg3, GXDATPtr arg4, const gx_string_type& arg5, const gx_string_type& arg6, int32_t arg7, int32_t arg8, int32_t arg9)
{
    int32_t ret = self->run(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9);
    return ret;
}
inline int32_t GXKGRD_wrap_run2(GXDBPtr arg1, const gx_string_type& arg2, const gx_string_type& arg3, const gx_string_type& arg4, const gx_string_type& arg5, const gx_string_type& arg6, const gx_string_type& arg7, const gx_string_type& arg8, const gx_string_type& arg9, int32_t arg10)
{
    int32_t ret = GXKGRD::run2(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10);
    return ret;
}
inline int32_t GXKGRD_wrap_run3(GXDBPtr arg1, const gx_string_type& arg2, const gx_string_type& arg3, const gx_string_type& arg4, const gx_string_type& arg5, const gx_string_type& arg6, const gx_string_type& arg7, const gx_string_type& arg8, const gx_string_type& arg9, const gx_string_type& arg10, int32_t arg11)
{
    int32_t ret = GXKGRD::run3(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11);
    return ret;
}
inline int32_t GXKGRD_wrap_save_parms(GXKGRDPtr self, const gx_string_type& arg1)
{
    int32_t ret = self->save_parms(arg1);
    return ret;
}

void gxPythonImportGXKGRD()
{

    class_<GXKGRD, GXKGRDPtr> pyClass("GXKGRD",
                                      "\n.. parsed-literal::\n\n"
                                      "   The KGRD object is used as a storage place for the control\n"
                                      "   parameters that the Krigrid program needs to execute. The\n"
                                      "   Run_KGRD function executes the Krigrid program using the\n"
                                      "   KGRD object.\n\n"
                                      , no_init);

    pyClass.def("null", &GXKGRD::null, "null() -> GXKGRD\n\nA null (undefined) instance of :class:`geosoft.gxapi.GXKGRD`\n\n:returns: A null :class:`geosoft.gxapi.GXKGRD`\n:rtype: :class:`geosoft.gxapi.GXKGRD`\n").staticmethod("null");
    pyClass.def("is_null", &GXKGRD::is_null, "is_null() -> bool\n\nCheck if the instance of :class:`geosoft.gxapi.GXKGRD is null (undefined)`\n\n:returns: True if this is a null instance of :class:`geosoft.gxapi.GXKGRD`, False otherwise.\n:rtype: bool`\n");
    pyClass.def("_internal_handle", &GXKGRD::_internal_handle);
    pyClass.def("clear", &GXKGRD_wrap_clear,
                "clear() -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Clears all the parameters in a KGRD object\n\n"

                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("create", &GXKGRD_wrap_create,
                "create() -> GXKGRD:\n"

                "\n.. parsed-literal::\n\n"
                "   Create a handle to a Krigrid object\n\n"

                ":returns: KGRD Object\n"
                ":rtype: :class:`geosoft.gxapi.GXKGRD`\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   The Krigrid object is initially empty. It will store the\n"
                "   control file parameters which the Krigrid program needs\n"
                "   to execute. Use the LoadParms_KGRD method to get the\n"
                "   control file parameters into the KGRD object.\n\n"
               ).staticmethod("create");
    pyClass.def("load_parms", &GXKGRD_wrap_load_parms,
                "load_parms((str)arg1) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Retrieves a Krigrid object's control parameters from a file.\n\n"

                ":param arg1: Name of file to get the parameter settings from\n"
                ":type arg1: str\n"
                ":returns: 0 OK, 1 Error.\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 6.0.1\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   If the control file name passed into this function is a file\n"
                "   which does not exist, then the defaults for a Krigrid control\n"
                "   file will be generated and put into the KGRD object.\n"
                "   Otherwise, the control file's settings are retrieved from\n"
                "   the file and loaded into the KGRD object.\n\n"
               );
    pyClass.def("run", &GXKGRD_wrap_run,
                "run((str)arg1, (GXDAT)arg2, (GXDAT)arg3, (GXDAT)arg4, (str)arg5, (str)arg6, (int)arg7, (int)arg8, (int)arg9) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Executes the Krigrid program, using the input channel and\n"
                "   output file parameters.\n\n"

                ":param arg1: Name of Z Channel to perfrom gridding on\n"
                ":type arg1: str\n"
                ":param arg2: Handle to source DAT object (from database)\n"
                ":type arg2: :class:`geosoft.gxapi.GXDAT`\n"
                ":param arg3: Handle to output grid file DAT\n"
                ":type arg3: :class:`geosoft.gxapi.GXDAT`\n"
                ":param arg4: Handle to output error grid file DAT ((DAT)0) if no error grid required\n"
                ":type arg4: :class:`geosoft.gxapi.GXDAT`\n"
                ":param arg5: Name of input variogram file\n"
                ":type arg5: str\n"
                ":param arg6: Name of output variogram file\n"
                ":type arg6: str\n"
                ":param arg7: Flag of variogram only\n"
                ":type arg7: int\n"
                ":param arg8: Flag of input variogram\n"
                ":type arg8: int\n"
                ":param arg9: Flag of output variogram\n"
                ":type arg9: int\n"
                ":returns: 0 OK, 1 Error.\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 6.0.1\n\n"
               );
    pyClass.def("run2", &GXKGRD_wrap_run2,
                "run2((GXDB)arg1, (str)arg2, (str)arg3, (str)arg4, (str)arg5, (str)arg6, (str)arg7, (str)arg8, (str)arg9, (int)arg10) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Executes the Krigrid program directly on a database.\n\n"

                ":param arg1: Handle to a database\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: Y Channel\n"
                ":type arg2: str\n"
                ":param arg3: X Channel\n"
                ":type arg3: str\n"
                ":param arg4: Data channel\n"
                ":type arg4: str\n"
                ":param arg5: KRIGRID control file.\n"
                ":type arg5: str\n"
                ":param arg6: (output grid name (not required if variogram analysis only))\n"
                ":type arg6: str\n"
                ":param arg7: (output error file, \"\" for none)\n"
                ":type arg7: str\n"
                ":param arg8: (input variogram file, \"\" for none)\n"
                ":type arg8: str\n"
                ":param arg9: (output variogram file, \"\" for none)\n"
                ":type arg9: str\n"
                ":param arg10: 1 if Variogram Analysis Only, other wise 0\n"
                ":type arg10: int\n"
                ":returns: 0 OK, 1 Error.\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 6.0.1\n\n"
               ).staticmethod("run2");
    pyClass.def("run3", &GXKGRD_wrap_run3,
                "run3((GXDB)arg1, (str)arg2, (str)arg3, (str)arg4, (str)arg5, (str)arg6, (str)arg7, (str)arg8, (str)arg9, (str)arg10, (int)arg11) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Executes the Krigrid program directly on a database and specifies the log file\n\n"

                ":param arg1: Handle to a database\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: Y Channel\n"
                ":type arg2: str\n"
                ":param arg3: X Channel\n"
                ":type arg3: str\n"
                ":param arg4: Data channel\n"
                ":type arg4: str\n"
                ":param arg5: KRIGRID control file.\n"
                ":type arg5: str\n"
                ":param arg6: (output grid name (not required if variogram analysis only))\n"
                ":type arg6: str\n"
                ":param arg7: (output error file, \"\" for none)\n"
                ":type arg7: str\n"
                ":param arg8: (input variogram file, \"\" for none)\n"
                ":type arg8: str\n"
                ":param arg9: (output variogram file, \"\" for none)\n"
                ":type arg9: str\n"
                ":param arg10: (log file name, \"\" for default)\n"
                ":type arg10: str\n"
                ":param arg11: 1 if Variogram Analysis Only, other wise 0\n"
                ":type arg11: int\n"
                ":returns: 0 OK, 1 Error.\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 6.4.0\n\n"
               ).staticmethod("run3");
    pyClass.def("save_parms", &GXKGRD_wrap_save_parms,
                "save_parms((str)arg1) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Puts the Krigrid object's control parameters back into\n"
                "   its control file.\n\n"

                ":param arg1: Name of file to put the parameter settings into\n"
                ":type arg1: str\n"
                ":returns: 0 OK, 1 Error.\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 6.0.1\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   If the control file did not previously exist, it will be\n"
                "   created. Otherwise, the old file will be overwritten.\n\n"
               );


}
