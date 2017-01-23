#include "stdafx.h"

using namespace boost::python;
using boost::python::init;


// Dummy classes


inline GXACQUIREPtr GXACQUIRE_wrap_create()
{
    GXACQUIREPtr ret = GXACQUIRE::create();
    return ret;
}
inline void GXACQUIRE_wrap_delete_empty_chan(GXACQUIREPtr self, GXDBPtr arg1)
{
    self->delete_empty_chan(arg1);
}
inline int32_t GXACQUIRE_wrap_import_hole(GXACQUIREPtr self, const gx_string_type& arg1, const gx_string_type& arg2, const gx_string_type& arg3, GXVVPtr arg4, int32_t arg5, int32_t arg6)
{
    int32_t ret = self->import_hole(arg1, arg2, arg3, arg4, arg5, arg6);
    return ret;
}
inline int32_t GXACQUIRE_wrap_import_point(GXACQUIREPtr self, GXDBPtr arg1, const gx_string_type& arg2, int32_t arg3)
{
    int32_t ret = self->import_point(arg1, arg2, arg3);
    return ret;
}
inline int32_t GXACQUIRE_wrap_selection_tool(GXACQUIREPtr self, const gx_string_type& arg1, int32_t arg2)
{
    int32_t ret = self->selection_tool(arg1, (ACQUIRE_SEL)arg2);
    return ret;
}

void gxPythonImportGXACQUIRE()
{

    class_<GXACQUIRE, GXACQUIREPtr> pyClass("GXACQUIRE",
                                            "\n.. parsed-literal::\n\n"
                                            "   This class is used to import Acquire data. It uses the\n"
                                            "   public Acquire API.\n\n"
                                            , no_init);

    pyClass.def("null", &GXACQUIRE::null, "null() -> GXACQUIRE\n\nA null (undefined) instance of :class:`geosoft.gxapi.GXACQUIRE`\n\n:returns: A null :class:`geosoft.gxapi.GXACQUIRE`\n:rtype: :class:`geosoft.gxapi.GXACQUIRE`\n").staticmethod("null");
    pyClass.def("is_null", &GXACQUIRE::is_null, "is_null() -> bool\n\nCheck if the instance of :class:`geosoft.gxapi.GXACQUIRE is null (undefined)`\n\n:returns: True if this is a null instance of :class:`geosoft.gxapi.GXACQUIRE`, False otherwise.\n:rtype: bool`\n");
    pyClass.def("_internal_handle", &GXACQUIRE::_internal_handle);
    pyClass.def("create", &GXACQUIRE_wrap_create,
                "create() -> GXACQUIRE:\n"

                "\n.. parsed-literal::\n\n"
                "   Create a ACQUIRE object\n\n"

                ":returns: ACQUIRE Object\n"
                ":rtype: :class:`geosoft.gxapi.GXACQUIRE`\n"
                "\n"

                "\n.. versionadded:: 6.0.0\n\n"
               ).staticmethod("create");
    pyClass.def("delete_empty_chan", &GXACQUIRE_wrap_delete_empty_chan,
                "delete_empty_chan((GXDB)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Delete empty channels\n\n"

                ":param arg1: Database\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.0.0\n\n"
               );
    pyClass.def("import_hole", &GXACQUIRE_wrap_import_hole,
                "import_hole((str)arg1, (str)arg2, (str)arg3, (GXVV)arg4, (int)arg5, (int)arg6) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Import Drillhole data acQuire database into a GDB\n\n"

                ":param arg1: project name\n"
                ":type arg1: str\n"
                ":param arg2: project directory\n"
                ":type arg2: str\n"
                ":param arg3: Parameter File\n"
                ":type arg3: str\n"
                ":param arg4: list of geology name database\n"
                ":type arg4: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg5: 0: Write to existing databases (overwrite holes), 1: Delete existing databases.\n"
                ":type arg5: int\n"
                ":param arg6: Convert Negatives (0,1)\n"
                ":type arg6: int\n"
                ":returns: 0 - Ok\n"
                "          1 - Error (Will not stop GX)\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 6.0.1\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Point data and polygon data are saved into D### lines in GDB,\n"
                "   ### representing incremental number starting from 0\n\n"
               );
    pyClass.def("import_point", &GXACQUIRE_wrap_import_point,
                "import_point((GXDB)arg1, (str)arg2, (int)arg3) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Import Point Sample data acQuire database into a GDB\n\n"

                ":param arg1: Geosoft GDB\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: Parameter File\n"
                ":type arg2: str\n"
                ":param arg3: Convert Negatives (0,1)\n"
                ":type arg3: int\n"
                ":returns: 0 - Ok\n"
                "          1 - Error (Will not stop GX)\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 6.0.1\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Data existing in the receiving GDB file will be over-written.\n"
                "   Point data and polygon data are saved into D### lines in GDB,\n"
                "   ### representing incremental number starting from 0\n\n"
               );
    pyClass.def("selection_tool", &GXACQUIRE_wrap_selection_tool,
                "selection_tool((str)arg1, (int)arg2) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Run the Acquire Selection Tool.\n\n"

                ":param arg1: Selection File Name\n"
                ":type arg1: str\n"
                ":param arg2: \\ :ref:`ACQUIRE_SEL`\\ \n"
                ":type arg2: int\n"
                ":returns: 0 - Ok\n"
                "          1 - if user cancels\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 6.0.1\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   The selection file will be loaded (if present) and then\n"
                "   the user can make selections then the selections are saved\n"
                "   back in the selection file.\n\n"
               );

    scope().attr("ACQUIRE_SEL_HOLES") = (int32_t)0;
    scope().attr("ACQUIRE_SEL_POINT") = (int32_t)1;

}
