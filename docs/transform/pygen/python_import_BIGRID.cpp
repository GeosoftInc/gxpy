#include "stdafx.h"

using namespace boost::python;
using boost::python::init;


// Dummy classes


inline void GXBIGRID_wrap_clear(GXBIGRIDPtr self)
{
    self->clear();
}
inline GXBIGRIDPtr GXBIGRID_wrap_create()
{
    GXBIGRIDPtr ret = GXBIGRID::create();
    return ret;
}
inline int32_t GXBIGRID_wrap_load_parms(GXBIGRIDPtr self, const gx_string_type& arg1)
{
    int32_t ret = self->load_parms(arg1);
    return ret;
}
inline int32_t GXBIGRID_wrap_load_warp(GXBIGRIDPtr self, const gx_string_type& arg1, const gx_string_type& arg2, const gx_string_type& arg3)
{
    int32_t ret = self->load_warp(arg1, arg2, arg3);
    return ret;
}
inline void GXBIGRID_wrap_run(GXBIGRIDPtr self, const gx_string_type& arg1, GXDATPtr arg2, GXDATPtr arg3)
{
    self->run(arg1, arg2, arg3);
}
inline void GXBIGRID_wrap_run2(GXBIGRIDPtr self, const gx_string_type& arg1, GXDATPtr arg2, GXDATPtr arg3, GXIPJPtr arg4)
{
    self->run2(arg1, arg2, arg3, arg4);
}
inline void GXBIGRID_wrap_save_parms(GXBIGRIDPtr self, const gx_string_type& arg1)
{
    self->save_parms(arg1);
}

void gxPythonImportGXBIGRID()
{

    class_<GXBIGRID, GXBIGRIDPtr> pyClass("GXBIGRID",
                                          "\n.. parsed-literal::\n\n"
                                          "   The Bigrid class is used to grid data using a optimized algorithm that\n"
                                          "   assumes data is collected in semi-straight lines.\n\n"
                                          , no_init);

    pyClass.def("null", &GXBIGRID::null, "null() -> GXBIGRID\n\nA null (undefined) instance of :class:`geosoft.gxapi.GXBIGRID`\n\n:returns: A null :class:`geosoft.gxapi.GXBIGRID`\n:rtype: :class:`geosoft.gxapi.GXBIGRID`\n").staticmethod("null");
    pyClass.def("is_null", &GXBIGRID::is_null, "is_null() -> bool\n\nCheck if the instance of :class:`geosoft.gxapi.GXBIGRID is null (undefined)`\n\n:returns: True if this is a null instance of :class:`geosoft.gxapi.GXBIGRID`, False otherwise.\n:rtype: bool`\n");
    pyClass.def("_internal_handle", &GXBIGRID::_internal_handle);
    pyClass.def("clear", &GXBIGRID_wrap_clear,
                "clear() -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Clears all the parameters in a BIGRID object\n\n"

                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("create", &GXBIGRID_wrap_create,
                "create() -> GXBIGRID:\n"

                "\n.. parsed-literal::\n\n"
                "   Create a handle to a Brigrid object\n\n"

                ":returns: BIGRID Object\n"
                ":rtype: :class:`geosoft.gxapi.GXBIGRID`\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   The Bigrid object is initially empty. It will store the\n"
                "   control file parameters which the Bigrid program needs\n"
                "   to execute. Use the LoadParms_BIGRID method to get the\n"
                "   control file parameters into the BIGRID object.\n\n"
               ).staticmethod("create");
    pyClass.def("load_parms", &GXBIGRID_wrap_load_parms,
                "load_parms((str)arg1) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Retrieves a Bigrid object's control parameters from a file,\n"
                "   or sets the parameters to default if the file doesn't exist.\n\n"

                ":param arg1: Name of file to get the parameter settings from\n"
                ":type arg1: str\n"
                ":returns: 0 - Ok\n"
                "          1 - Error\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   If the control file name passed into this function is a file\n"
                "   which does not exist, then the defaults for a Bigrid control\n"
                "   file will be generated and put into the BIGRID object.\n"
                "   Otherwise, the control file's settings are retrieved from\n"
                "   the file and loaded into the BIGRID object.\n\n"
               );
    pyClass.def("load_warp", &GXBIGRID_wrap_load_warp,
                "load_warp((str)arg1, (str)arg2, (str)arg3) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Load a warp projection.\n\n"

                ":param arg1: New grid title\n"
                ":type arg1: str\n"
                ":param arg2: New grid cell size as a string, blank for default\n"
                ":type arg2: str\n"
                ":param arg3: Warp projection file name\n"
                ":type arg3: str\n"
                ":returns: 0 - Ok\n"
                "          1 - Error\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("run", &GXBIGRID_wrap_run,
                "run((str)arg1, (GXDAT)arg2, (GXDAT)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Executes the Bigrid program, using the input channel and\n"
                "   output file parameters.\n\n"

                ":param arg1: not used, pass as \"\"\n"
                ":type arg1: str\n"
                ":param arg2: Handle to source DAT object (from database)\n"
                ":type arg2: :class:`geosoft.gxapi.GXDAT`\n"
                ":param arg3: Handle to output grid file DAT\n"
                ":type arg3: :class:`geosoft.gxapi.GXDAT`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("run2", &GXBIGRID_wrap_run2,
                "run2((str)arg1, (GXDAT)arg2, (GXDAT)arg3, (GXIPJ)arg4) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Executes the Bigrid program, using the input channel and\n"
                "   output file parameters with a projection handle.\n\n"

                ":param arg1: not used, pass as \"\"\n"
                ":type arg1: str\n"
                ":param arg2: Handle to source DAT object (from database)\n"
                ":type arg2: :class:`geosoft.gxapi.GXDAT`\n"
                ":param arg3: Handle to output grid file DAT\n"
                ":type arg3: :class:`geosoft.gxapi.GXDAT`\n"
                ":param arg4: IPJ handle of the projection system\n"
                ":type arg4: :class:`geosoft.gxapi.GXIPJ`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.3.0\n\n"
               );
    pyClass.def("save_parms", &GXBIGRID_wrap_save_parms,
                "save_parms((str)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Puts the Bigrid object's control parameters back into\n"
                "   its control file.\n\n"

                ":param arg1: Name of file to put the parameter settings into\n"
                ":type arg1: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   If the control file did not previously exist, it will be\n"
                "   created. Otherwise, the old file will be overwritten.\n\n"
               );


}
