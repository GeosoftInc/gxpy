#include "stdafx.h"

using namespace boost::python;
using boost::python::init;


// Dummy classes


inline GXSTKPtr GXMSTK_wrap_add_stk(GXMSTKPtr self)
{
    GXSTKPtr ret = self->add_stk();
    return ret;
}
inline void GXMSTK_wrap_chan_list_vv(GXMSTKPtr self, GXDBPtr arg1, GXVVPtr arg2, GXVVPtr arg3, GXVVPtr arg4, GXVVPtr arg5, GXVVPtr arg6)
{
    self->chan_list_vv(arg1, arg2, arg3, arg4, arg5, arg6);
}
inline GXMSTKPtr GXMSTK_wrap_create()
{
    GXMSTKPtr ret = GXMSTK::create();
    return ret;
}
inline void GXMSTK_wrap_draw_profile(GXMSTKPtr self, GXDBPtr arg1, int32_t arg2, GXMAPPtr arg3)
{
    self->draw_profile(arg1, arg2, arg3);
}
inline void GXMSTK_wrap_set_y_axis_direction(GXMSTKPtr self, int32_t arg1)
{
    self->set_y_axis_direction(arg1);
}
inline void GXMSTK_wrap_find_stk2(GXMSTKPtr self, const gx_string_type& arg1, int_ref& arg2, GXVVPtr arg3)
{
    self->find_stk2(arg1, arg2, arg3);
}
inline GXSTKPtr GXMSTK_wrap_get_stk(GXMSTKPtr self, int32_t arg1)
{
    GXSTKPtr ret = self->get_stk(arg1);
    return ret;
}
inline void GXMSTK_wrap_delete_stk(GXMSTKPtr self, int32_t arg1)
{
    self->delete_stk(arg1);
}
inline void GXMSTK_wrap_find_stk(GXMSTKPtr self, const gx_string_type& arg1, int_ref& arg2, str_ref& arg3, str_ref& arg4, str_ref& arg5)
{
    self->find_stk(arg1, arg2, arg3, arg4, arg5);
}
inline int32_t GXMSTK_wrap_get_num_stk(GXMSTKPtr self)
{
    int32_t ret = self->get_num_stk();
    return ret;
}
inline void GXMSTK_wrap_read_ini(GXMSTKPtr self, GXRAPtr arg1)
{
    self->read_ini(arg1);
}
inline void GXMSTK_wrap_save_profile(GXMSTKPtr self, GXWAPtr arg1)
{
    self->save_profile(arg1);
}

void gxPythonImportGXMSTK()
{

    class_<GXMSTK, GXMSTKPtr> pyClass("GXMSTK",
                                      "\n.. parsed-literal::\n\n"
                                      "   Multi-profile stack\n"
                                      "   This class is used for storing data of multiple profiles and\n"
                                      "   plotting profiles in a map. It is a container of STK class objects.\n"
                                      "   \n"
                                      "   See also:         STK class.\n\n"
                                      , no_init);

    pyClass.def("null", &GXMSTK::null, "null() -> GXMSTK\n\nA null (undefined) instance of :class:`geosoft.gxapi.GXMSTK`\n\n:returns: A null :class:`geosoft.gxapi.GXMSTK`\n:rtype: :class:`geosoft.gxapi.GXMSTK`\n").staticmethod("null");
    pyClass.def("is_null", &GXMSTK::is_null, "is_null() -> bool\n\nCheck if the instance of :class:`geosoft.gxapi.GXMSTK is null (undefined)`\n\n:returns: True if this is a null instance of :class:`geosoft.gxapi.GXMSTK`, False otherwise.\n:rtype: bool`\n");
    pyClass.def("_internal_handle", &GXMSTK::_internal_handle);
    pyClass.def("add_stk", &GXMSTK_wrap_add_stk,
                "add_stk() -> GXSTK:\n"

                "\n.. parsed-literal::\n\n"
                "   Create and add a STK object to MSTK\n\n"

                ":returns: STK, fail if error\n"
                ":rtype: :class:`geosoft.gxapi.GXSTK`\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Index to the added STK object is the last one in MSTK container.\n\n"
               );
    pyClass.def("chan_list_vv", &GXMSTK_wrap_chan_list_vv,
                "chan_list_vv((GXDB)arg1, (GXVV)arg2, (GXVV)arg3, (GXVV)arg4, (GXVV)arg5, (GXVV)arg6) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Save channel names in VVs based on channel types\n\n"

                ":param arg1: Database handle\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: List of names of numeric channels\n"
                ":type arg2: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg3: List of name of string channels\n"
                ":type arg3: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg4: List of channel names which can be used for X axis. Must be numeric channels but not VA channels\n"
                ":type arg4: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg5: List of profiles with channel names in both MSTK and DB\n"
                ":type arg5: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg6: List of profiles with channels in MSTK but not in database\n"
                ":type arg6: :class:`geosoft.gxapi.GXVV`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Terms 'used' and 'unused' indicate that the a channel name\n"
                "   in database also 'in' and 'not in' the MSTK object respectively\n\n"
               );
    pyClass.def("create", &GXMSTK_wrap_create,
                "create() -> GXMSTK:\n"

                "\n.. parsed-literal::\n\n"
                "   Create MSTK.\n\n"

                ":returns: MSTK, aborts if creation fails\n"
                ":rtype: :class:`geosoft.gxapi.GXMSTK`\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("create");
    pyClass.def("draw_profile", &GXMSTK_wrap_draw_profile,
                "draw_profile((GXDB)arg1, (int)arg2, (GXMAP)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Draw multiple profiles in map\n\n"

                ":param arg1: Database handle\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: Database line\n"
                ":type arg2: int\n"
                ":param arg3: MAP handle\n"
                ":type arg3: :class:`geosoft.gxapi.GXMAP`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("set_y_axis_direction", &GXMSTK_wrap_set_y_axis_direction,
                "set_y_axis_direction((int)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set the Y-axis direction - normal or inverted\n\n"

                ":param arg1: Y-axis direction: 0 - normal, 1 - inverted\n"
                ":type arg1: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 8.3.0\n\n"
               );
    pyClass.def("find_stk2", &GXMSTK_wrap_find_stk2,
                "find_stk2((str)arg1, (int_ref)arg2, (GXVV)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Find index of STK from a string of group names and X/Y channels\n\n"

                ":param arg1: Input string (see notes above). Will be modified on return\n"
                ":type arg1: str\n"
                ":param arg2: Index to the STK found, Must be greater than 0 if found, -1 if not found\n"
                ":type arg2: :class:`geosoft.gxapi.int_ref`\n"
                ":param arg3: Returned VV with names of Group, X channel and Y channel VV type must be of STRING\n"
                ":type arg3: :class:`geosoft.gxapi.GXVV`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Format of the input string:\n"
                "   \n"
                "   Map group name + \" ( \" + X channel name + \" , \" + Y channel name + \" )\"\n"
                "   \n"
                "   for example, string \"DATA ( DIST , MAG )\"  indicates a map group name of DATA,\n"
                "   X channel name of DIST and Y channel name of MAG.\n\n"
               );
    pyClass.def("get_stk", &GXMSTK_wrap_get_stk,
                "get_stk((int)arg1) -> GXSTK:\n"

                "\n.. parsed-literal::\n\n"
                "   Get a specific STK object from a MSTK object\n"
                "   (Index of 0 gets the first STK in the MSTK)\n\n"

                ":param arg1: Index to STK to get\n"
                ":type arg1: int\n"
                ":returns: x     - STK Object handle\n"
                ":rtype: :class:`geosoft.gxapi.GXSTK`\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("delete_stk", &GXMSTK_wrap_delete_stk,
                "delete_stk((int)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Delete a STK object\n\n"

                ":param arg1: Index to STK to delete (0 is first one)\n"
                ":type arg1: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   0 is the first one\n\n"
               );
    pyClass.def("find_stk", &GXMSTK_wrap_find_stk,
                "find_stk((str)arg1, (int_ref)arg2, (str_ref)arg3, (str_ref)arg4, (str_ref)arg5) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Find index of STK from a string of group names and X/Y channels\n\n"

                ":param arg1: Input string (see notes above). Will be modified on return\n"
                ":type arg1: str\n"
                ":param arg2: Index to the STK found, Must be greater than 0 if found, -1 if not found\n"
                ":type arg2: :class:`geosoft.gxapi.int_ref`\n"
                ":param arg3: output group name string\n"
                ":type arg3: :class:`geosoft.gxapi.str_ref`\n"
                ":param arg4: output X channel name string\n"
                ":type arg4: :class:`geosoft.gxapi.str_ref`\n"
                ":param arg5: output Y channel name string\n"
                ":type arg5: :class:`geosoft.gxapi.str_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Format of the input string:\n"
                "   \n"
                "   Map group name + \" ( \" + X channel name + \" , \" + Y channel name + \" )\"\n"
                "   \n"
                "   for example, string \"DATA ( DIST , MAG )\"  indicates a map group name of DATA,\n"
                "   X channel name of DIST and Y channel name of MAG.\n\n"
               );
    pyClass.def("get_num_stk", &GXMSTK_wrap_get_num_stk,
                "get_num_stk() -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Get the number of STK objects in a MSTK object\n\n"

                ":returns: The number of STK objects in a MSTK object\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("read_ini", &GXMSTK_wrap_read_ini,
                "read_ini((GXRA)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Read multiple profiles parameters from an INI file\n\n"

                ":param arg1: RA handle to an INI file\n"
                ":type arg1: :class:`geosoft.gxapi.GXRA`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("save_profile", &GXMSTK_wrap_save_profile,
                "save_profile((GXWA)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Save multiple profile INI parameters in a WA file of INI format\n\n"

                ":param arg1: WA handle to an INI file\n"
                ":type arg1: :class:`geosoft.gxapi.GXWA`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );


}
