#include "stdafx.h"

using namespace boost::python;
using boost::python::init;


// Dummy classes


inline void GXRGRD_wrap_clear(GXRGRDPtr self)
{
    self->clear();
}
inline GXRGRDPtr GXRGRD_wrap_create()
{
    GXRGRDPtr ret = GXRGRD::create();
    return ret;
}
inline GXIMGPtr GXRGRD_wrap_create_img(GXVVPtr arg1, GXVVPtr arg2, GXVVPtr arg3, GXIPJPtr arg4, const gx_string_type& arg5, const gx_string_type& arg6)
{
    GXIMGPtr ret = GXRGRD::create_img(arg1, arg2, arg3, arg4, arg5, arg6);
    return ret;
}
inline int32_t GXRGRD_wrap_default(GXRGRDPtr self, const gx_string_type& arg1, GXDATPtr arg2)
{
    int32_t ret = self->default(arg1, arg2);
    return ret;
}
inline int32_t GXRGRD_wrap_load_parms(GXRGRDPtr self, const gx_string_type& arg1)
{
    int32_t ret = self->load_parms(arg1);
    return ret;
}
inline int32_t GXRGRD_wrap_run(GXRGRDPtr self, GXDATPtr arg1, GXDATPtr arg2)
{
    int32_t ret = self->run(arg1, arg2);
    return ret;
}
inline int32_t GXRGRD_wrap_run2(GXDBPtr arg1, const gx_string_type& arg2, const gx_string_type& arg3, const gx_string_type& arg4, const gx_string_type& arg5, const gx_string_type& arg6)
{
    int32_t ret = GXRGRD::run2(arg1, arg2, arg3, arg4, arg5, arg6);
    return ret;
}
inline int32_t GXRGRD_wrap_save_parms(GXRGRDPtr self, const gx_string_type& arg1)
{
    int32_t ret = self->save_parms(arg1);
    return ret;
}
inline void GXRGRD_wrap_run_vv(GXVVPtr arg1, GXVVPtr arg2, GXVVPtr arg3, GXIPJPtr arg4, const gx_string_type& arg5, const gx_string_type& arg6)
{
    GXRGRD::run_vv(arg1, arg2, arg3, arg4, arg5, arg6);
}

void gxPythonImportGXRGRD()
{

    class_<GXRGRD, GXRGRDPtr> pyClass("GXRGRD",
                                      "\n.. parsed-literal::\n\n"
                                      "   The RGRD object is used as a storage place for the control\n"
                                      "   parameters which the Rangrid (minimum curvature) program needs to execute. The\n"
                                      "   Run_RGRD function executes the Rangrid program using the RGRD object.\n\n"
                                      , no_init);

    pyClass.def("null", &GXRGRD::null, "null() -> GXRGRD\n\nA null (undefined) instance of :class:`geosoft.gxapi.GXRGRD`\n\n:returns: A null :class:`geosoft.gxapi.GXRGRD`\n:rtype: :class:`geosoft.gxapi.GXRGRD`\n").staticmethod("null");
    pyClass.def("is_null", &GXRGRD::is_null, "is_null() -> bool\n\nCheck if the instance of :class:`geosoft.gxapi.GXRGRD is null (undefined)`\n\n:returns: True if this is a null instance of :class:`geosoft.gxapi.GXRGRD`, False otherwise.\n:rtype: bool`\n");
    pyClass.def("_internal_handle", &GXRGRD::_internal_handle);
    pyClass.def("clear", &GXRGRD_wrap_clear,
                "clear() -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Clears all the parameters in a RGRD object\n\n"

                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   DLL name \\ :func:`geosoft.gxapi.GXRGRD.clear`\\ \n\n"
               );
    pyClass.def("create", &GXRGRD_wrap_create,
                "create() -> GXRGRD:\n"

                "\n.. parsed-literal::\n\n"
                "   Create a handle to a Rangrid object\n\n"

                ":returns: RGRD Object\n"
                ":rtype: :class:`geosoft.gxapi.GXRGRD`\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   The Rangrid object is initially empty. It will store the\n"
                "   control file parameters which the Rangrid program needs\n"
                "   to execute. Use the LoadParms_RGRD method to get the\n"
                "   control file parameters into the RGRD object.\n\n"
               ).staticmethod("create");
    pyClass.def("create_img", &GXRGRD_wrap_create_img,
                "create_img((GXVV)arg1, (GXVV)arg2, (GXVV)arg3, (GXIPJ)arg4, (str)arg5, (str)arg6) -> GXIMG:\n"

                "\n.. parsed-literal::\n\n"
                "   Run Rangrid directly on XYZ VV data, output to an IMG.\n\n"

                ":param arg1: X data (any numeric VV type)\n"
                ":type arg1: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg2: Y data (any numeric VV type)\n"
                ":type arg2: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg3: Z (grid value) data (any numeric VV type)\n"
                ":type arg3: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg4: Projection to apply to the output IMG\n"
                ":type arg4: :class:`geosoft.gxapi.GXIPJ`\n"
                ":param arg5: RANGRID control file.\n"
                ":type arg5: str\n"
                ":param arg6: output grid name (optional)\n"
                ":type arg6: str\n"
                ":returns: IMG object\n"
                ":rtype: :class:`geosoft.gxapi.GXIMG`\n"
                "\n"

                "\n.. versionadded:: 7.0.1\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   If the grid file name is defined, the IMG is tied to a new output file.\n"
                "   If the grid file name is not defined, the IMG is memory-based; not\n"
                "   tied to a file.\n\n"
               ).staticmethod("create_img");
    pyClass.def("default", &GXRGRD_wrap_default,
                "default((str)arg1, (GXDAT)arg2) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Set the defaults.\n\n"

                ":param arg1: Name of Z Channel to perfrom gridding on\n"
                ":type arg1: str\n"
                ":param arg2: Handle to source DAT object (from database)\n"
                ":type arg2: :class:`geosoft.gxapi.GXDAT`\n"
                ":returns: 0 OK, 1 Error.\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 6.0.1\n\n"
               );
    pyClass.def("load_parms", &GXRGRD_wrap_load_parms,
                "load_parms((str)arg1) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Retrieves a Rangrid object's control parameters from a file,\n"
                "   or sets the parameters to default if the file doesn't exist.\n\n"

                ":param arg1: Name of file to get the parameter settings from\n"
                ":type arg1: str\n"
                ":returns: 0 OK, 1 Error.\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 6.0.1\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   If the control file name passed into this function is a file\n"
                "   which does not exist, then the defaults for a Rangrid control\n"
                "   file will be generated and put into the RGRD object.\n"
                "   Otherwise, the control file's settings are retrieved from\n"
                "   the file and loaded into the RGRD object.\n\n"
               );
    pyClass.def("run", &GXRGRD_wrap_run,
                "run((GXDAT)arg1, (GXDAT)arg2) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Executes the Rangrid program, using the input channel and\n"
                "   output file parameters.\n\n"

                ":param arg1: Handle to source DAT object (from database)\n"
                ":type arg1: :class:`geosoft.gxapi.GXDAT`\n"
                ":param arg2: Handle to output grid file DAT\n"
                ":type arg2: :class:`geosoft.gxapi.GXDAT`\n"
                ":returns: 0 OK, 1 Error.\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 6.0.1\n\n"
               );
    pyClass.def("run2", &GXRGRD_wrap_run2,
                "run2((GXDB)arg1, (str)arg2, (str)arg3, (str)arg4, (str)arg5, (str)arg6) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Executes the Rangrid program directly on a database.\n\n"

                ":param arg1: Handle to a database\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: Y Channel\n"
                ":type arg2: str\n"
                ":param arg3: X Channel\n"
                ":type arg3: str\n"
                ":param arg4: Data channel\n"
                ":type arg4: str\n"
                ":param arg5: RANGRID control file.\n"
                ":type arg5: str\n"
                ":param arg6: output grid name\n"
                ":type arg6: str\n"
                ":returns: 0, always.\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 6.0.1\n\n"
               ).staticmethod("run2");
    pyClass.def("save_parms", &GXRGRD_wrap_save_parms,
                "save_parms((str)arg1) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Puts the Rangrid object's control parameters back into\n"
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
    pyClass.def("run_vv", &GXRGRD_wrap_run_vv,
                "run_vv((GXVV)arg1, (GXVV)arg2, (GXVV)arg3, (GXIPJ)arg4, (str)arg5, (str)arg6) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Executes the Rangrid program directly on input data VVs.\n\n"

                ":param arg1: X data\n"
                ":type arg1: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg2: Y data\n"
                ":type arg2: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg3: Z (grid value) data\n"
                ":type arg3: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg4: Projection to put into grid\n"
                ":type arg4: :class:`geosoft.gxapi.GXIPJ`\n"
                ":param arg5: RANGRID control file.\n"
                ":type arg5: str\n"
                ":param arg6: output grid name\n"
                ":type arg6: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.3.0\n\n"
               ).staticmethod("run_vv");


}
