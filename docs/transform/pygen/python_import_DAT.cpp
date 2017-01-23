#include "stdafx.h"

using namespace boost::python;
using boost::python::init;


// Dummy classes


inline GXDATPtr GXDAT_wrap_create_db(GXDBPtr arg1, const gx_string_type& arg2, const gx_string_type& arg3, const gx_string_type& arg4)
{
    GXDATPtr ret = GXDAT::create_db(arg1, arg2, arg3, arg4);
    return ret;
}
inline GXDATPtr GXDAT_wrap_create_xgd(const gx_string_type& arg1, int32_t arg2)
{
    GXDATPtr ret = GXDAT::create_xgd(arg1, (DAT_XGD)arg2);
    return ret;
}
inline void GXDAT_wrap_get_lst(GXLSTPtr arg1, const gx_string_type& arg2, int32_t arg3, int32_t arg4)
{
    GXDAT::get_lst(arg1, arg2, (DAT_FILE)arg3, (DAT_FILE_FORM)arg4);
}
inline void GXDAT_wrap_range_xyz(GXDATPtr self, float_ref& arg1, float_ref& arg2, float_ref& arg3, float_ref& arg4, float_ref& arg5, float_ref& arg6, int_ref& arg7)
{
    self->range_xyz(arg1, arg2, arg3, arg4, arg5, arg6, arg7);
}

void gxPythonImportGXDAT()
{

    class_<GXDAT, GXDATPtr> pyClass("GXDAT",
                                    "\n.. parsed-literal::\n\n"
                                    "   \n"
                                    "   		The DAT object is used to access data from an variety of data sources\n"
                                    "   		using the same access functions. The DAT interface supports data access\n"
                                    "   		on a point-by-point, of line-by-line basis.  For example,\n"
                                    "   		the \\ :func:`geosoft.gxapi.GXBIGRID.run`\\  function uses 2 DAT objects - one DAT associated with the\n"
                                    "   		input data source, which is read line-by-line, and a second associated with\n"
                                    "   		the output grid file output grid file.\n"
                                    "   \n"
                                    "   		Use a specific DAT creation method for an associated\n"
                                    "   		information source in order to make a DAT as required\n"
                                    "   		by a specific processing function.  The gridding methods all use DATs.\n"
                                    "   	\n\n"
                                    , no_init);

    pyClass.def("null", &GXDAT::null, "null() -> GXDAT\n\nA null (undefined) instance of :class:`geosoft.gxapi.GXDAT`\n\n:returns: A null :class:`geosoft.gxapi.GXDAT`\n:rtype: :class:`geosoft.gxapi.GXDAT`\n").staticmethod("null");
    pyClass.def("is_null", &GXDAT::is_null, "is_null() -> bool\n\nCheck if the instance of :class:`geosoft.gxapi.GXDAT is null (undefined)`\n\n:returns: True if this is a null instance of :class:`geosoft.gxapi.GXDAT`, False otherwise.\n:rtype: bool`\n");
    pyClass.def("_internal_handle", &GXDAT::_internal_handle);
    pyClass.def("create_db", &GXDAT_wrap_create_db,
                "create_db((GXDB)arg1, (str)arg2, (str)arg3, (str)arg4) -> GXDAT:\n"

                "\n.. parsed-literal::\n\n"
                "   Create a handle to a database DAT object\n\n"

                ":param arg1: Handle to database which DAT is connected with\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: Name of X channel in database\n"
                ":type arg2: str\n"
                ":param arg3: Name of Y channel in database\n"
                ":type arg3: str\n"
                ":param arg4: Name of Z channel in database\n"
                ":type arg4: str\n"
                ":returns: DAT Object\n"
                ":rtype: :class:`geosoft.gxapi.GXDAT`\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("create_db");
    pyClass.def("create_xgd", &GXDAT_wrap_create_xgd,
                "create_xgd((str)arg1, (int)arg2) -> GXDAT:\n"

                "\n.. parsed-literal::\n\n"
                "   Create a handle to a grid file DAT object\n\n"

                ":param arg1: Name of grid file to associate DAT with\n"
                ":type arg1: str\n"
                ":param arg2: \\ :ref:`DAT_XGD`\\ \n"
                ":type arg2: int\n"
                ":returns: DAT Object\n"
                ":rtype: :class:`geosoft.gxapi.GXDAT`\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("create_xgd");
    pyClass.def("get_lst", &GXDAT_wrap_get_lst,
                "get_lst((GXLST)arg1, (str)arg2, (int)arg3, (int)arg4) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Put available DAT filters and qualifiers in a LST\n\n"

                ":param arg1: LST object to populate\n"
                ":type arg1: :class:`geosoft.gxapi.GXLST`\n"
                ":param arg2: DAT interface name (\"XGD\" only support option currently)\n"
                ":type arg2: str\n"
                ":param arg3: \\ :ref:`DAT_FILE`\\ \n"
                ":type arg3: int\n"
                ":param arg4: \\ :ref:`DAT_FILE_FORM`\\ \n"
                ":type arg4: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.8\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					The filters displayed in the Grid/Image file browse dialog are put\n"
                "   					in the \"Name\" of the LST, while the file qualifiers are stored in\n"
                "   					the \"Value\".\n"
                "   				\n\n"
               ).staticmethod("get_lst");
    pyClass.def("range_xyz", &GXDAT_wrap_range_xyz,
                "range_xyz((float_ref)arg1, (float_ref)arg2, (float_ref)arg3, (float_ref)arg4, (float_ref)arg5, (float_ref)arg6, (int_ref)arg7) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Determine the range in X, Y and Z in the DAT source\n\n"

                ":param arg1: Minimum X (rMAX if none)\n"
                ":type arg1: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg2: Minimum Y (rMAX if none)\n"
                ":type arg2: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg3: Minimum Z (rMAX if none)\n"
                ":type arg3: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg4: Maximum X (rMIN if none)\n"
                ":type arg4: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg5: Maximum Y (rMIN if none)\n"
                ":type arg5: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg6: Maximum Z (rMIN if none)\n"
                ":type arg6: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg7: Number of non-dummy XYZ.\n"
                ":type arg7: :class:`geosoft.gxapi.int_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 7.3.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Terminates if unable to open an RPT DAT interface.\n\n"
               );

    scope().attr("DAT_FILE_GRID") = (int32_t)1;
    scope().attr("DAT_FILE_IMAGE") = (int32_t)2;
    scope().attr("DAT_FILE_FORM_OPEN") = (int32_t)0;
    scope().attr("DAT_FILE_FORM_SAVE") = (int32_t)1;
    scope().attr("DAT_XGD_READ") = (int32_t)0;
    scope().attr("DAT_XGD_NEW") = (int32_t)1;
    scope().attr("DAT_XGD_WRITE") = (int32_t)2;

}
