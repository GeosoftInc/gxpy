#include "stdafx.h"

using namespace boost::python;
using boost::python::init;


// Dummy classes


inline GXVOXDPtr GXVOXD_wrap_create(GXVOXPtr arg1, const gx_string_type& arg2, int32_t arg3, double arg4)
{
    GXVOXDPtr ret = GXVOXD::create(arg1, arg2, (ITR_ZONE)arg3, arg4);
    return ret;
}
inline GXVOXDPtr GXVOXD_wrap_create_itr(GXVOXPtr arg1, GXITRPtr arg2)
{
    GXVOXDPtr ret = GXVOXD::create_itr(arg1, arg2);
    return ret;
}
inline GXVOXDPtr GXVOXD_wrap_create_thematic(GXVOXPtr arg1)
{
    GXVOXDPtr ret = GXVOXD::create_thematic(arg1);
    return ret;
}
inline void GXVOXD_wrap_get_draw_controls(GXVOXDPtr self, int_ref& arg1, float_ref& arg2, float_ref& arg3, float_ref& arg4, float_ref& arg5, float_ref& arg6, float_ref& arg7, float_ref& arg8)
{
    self->get_draw_controls(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8);
}
inline void GXVOXD_wrap_get_name(GXVOXDPtr self, str_ref& arg1)
{
    self->get_name(arg1);
}
inline void GXVOXD_wrap_get_itr(GXVOXDPtr self, GXITRPtr arg1)
{
    self->get_itr(arg1);
}
inline void GXVOXD_wrap_get_shell_controls(GXVOXDPtr self, float_ref& arg1, float_ref& arg2)
{
    self->get_shell_controls(arg1, arg2);
}
inline void GXVOXD_wrap_set_draw_controls(GXVOXDPtr self, int32_t arg1, double arg2, double arg3, double arg4, double arg5, double arg6, double arg7, double arg8)
{
    self->set_draw_controls(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8);
}
inline void GXVOXD_wrap_set_itr(GXVOXDPtr self, GXITRPtr arg1)
{
    self->set_itr(arg1);
}
inline void GXVOXD_wrap_set_shell_controls(GXVOXDPtr self, double arg1, double arg2)
{
    self->set_shell_controls(arg1, arg2);
}

void gxPythonImportGXVOXD()
{

    class_<GXVOXD, GXVOXDPtr> pyClass("GXVOXD",
                                      "\n.. parsed-literal::\n\n"
                                      "   VOX Display object.\n\n"
                                      , no_init);

    pyClass.def("null", &GXVOXD::null, "null() -> GXVOXD\n\nA null (undefined) instance of :class:`geosoft.gxapi.GXVOXD`\n\n:returns: A null :class:`geosoft.gxapi.GXVOXD`\n:rtype: :class:`geosoft.gxapi.GXVOXD`\n").staticmethod("null");
    pyClass.def("is_null", &GXVOXD::is_null, "is_null() -> bool\n\nCheck if the instance of :class:`geosoft.gxapi.GXVOXD is null (undefined)`\n\n:returns: True if this is a null instance of :class:`geosoft.gxapi.GXVOXD`, False otherwise.\n:rtype: bool`\n");
    pyClass.def("_internal_handle", &GXVOXD::_internal_handle);
    pyClass.def("create", &GXVOXD_wrap_create,
                "create((GXVOX)arg1, (str)arg2, (int)arg3, (float)arg4) -> GXVOXD:\n"

                "\n.. parsed-literal::\n\n"
                "   Create a new VOXD\n\n"

                ":param arg1: VOX Object\n"
                ":type arg1: :class:`geosoft.gxapi.GXVOX`\n"
                ":param arg2: colour table name, \"\" for default\n"
                ":type arg2: str\n"
                ":param arg3: \\ :ref:`ITR_ZONE`\\ \n"
                ":type arg3: int\n"
                ":param arg4: colour contour interval or rDUMMY\n"
                ":type arg4: float\n"
                ":returns: VOXD handle, terminates if creation fails\n"
                ":rtype: :class:`geosoft.gxapi.GXVOXD`\n"
                "\n"

                "\n.. versionadded:: 6.2.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Fails if the VOX object is NOT thematic.\n"
                "   					(See the \\ :func:`geosoft.gxapi.GXVOXD.create_thematic`\\  function.)\n"
                "   				\n\n"
               ).staticmethod("create");
    pyClass.def("create_itr", &GXVOXD_wrap_create_itr,
                "create_itr((GXVOX)arg1, (GXITR)arg2) -> GXVOXD:\n"

                "\n.. parsed-literal::\n\n"
                "   Create a new VOXD with our own ITR\n\n"

                ":param arg1: VOX Object\n"
                ":type arg1: :class:`geosoft.gxapi.GXVOX`\n"
                ":param arg2: ITR Object\n"
                ":type arg2: :class:`geosoft.gxapi.GXITR`\n"
                ":returns: VOXD handle, terminates if creation fails\n"
                ":rtype: :class:`geosoft.gxapi.GXVOXD`\n"
                "\n"

                "\n.. versionadded:: 6.2.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Fails if the VOX object is thematic.\n"
                "   					(See the \\ :func:`geosoft.gxapi.GXVOXD.create_thematic`\\  function.)\n"
                "   				\n\n"
               ).staticmethod("create_itr");
    pyClass.def("create_thematic", &GXVOXD_wrap_create_thematic,
                "create_thematic((GXVOX)arg1) -> GXVOXD:\n"

                "\n.. parsed-literal::\n\n"
                "   Create a new VOXD for a thematic VOX object.\n\n"

                ":param arg1: VOX Object\n"
                ":type arg1: :class:`geosoft.gxapi.GXVOX`\n"
                ":returns: VOXD handle, terminates if creation fails\n"
                ":rtype: :class:`geosoft.gxapi.GXVOXD`\n"
                "\n"

                "\n.. versionadded:: 7.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					A thematic voxel is one where the stored integer values\n"
                "   					represent indices into an internally stored TPAT object.\n"
                "   					Thematic voxels contain their own color definitions, and\n"
                "   					normal numerical operations, such as applying ITRs for display,\n"
                "   					are not valid.\n"
                "   \n"
                "   					To determine if a VOX object is thematic, use the\n"
                "   					\\ :func:`geosoft.gxapi.GXVOX.is_thematic`\\  function.\n"
                "   \n"
                "   					Fails if the VOX object is NOT thematic.\n"
                "   				\n\n"
               ).staticmethod("create_thematic");
    pyClass.def("get_draw_controls", &GXVOXD_wrap_get_draw_controls,
                "get_draw_controls((int_ref)arg1, (float_ref)arg2, (float_ref)arg3, (float_ref)arg4, (float_ref)arg5, (float_ref)arg6, (float_ref)arg7, (float_ref)arg8) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get the draw controls\n\n"

                ":param arg1: Draw Bounding Box\n"
                ":type arg1: :class:`geosoft.gxapi.int_ref`\n"
                ":param arg2: Transparency\n"
                ":type arg2: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg3: Min X\n"
                ":type arg3: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg4: Min Y\n"
                ":type arg4: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg5: Min Z\n"
                ":type arg5: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg6: Max X\n"
                ":type arg6: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg7: Max Y\n"
                ":type arg7: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg8: Max Z\n"
                ":type arg8: :class:`geosoft.gxapi.float_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.2.0\n\n"
               );
    pyClass.def("get_name", &GXVOXD_wrap_get_name,
                "get_name((str_ref)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Gets the file name of the voxel.\n\n"

                ":param arg1: file name returned\n"
                ":type arg1: :class:`geosoft.gxapi.str_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 8.2.0\n\n"
               );
    pyClass.def("get_itr", &GXVOXD_wrap_get_itr,
                "get_itr((GXITR)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get the ITR of the VOXD\n\n"

                ":param arg1: ITR object\n"
                ":type arg1: :class:`geosoft.gxapi.GXITR`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.2.0\n\n"
               );
    pyClass.def("get_shell_controls", &GXVOXD_wrap_get_shell_controls,
                "get_shell_controls((float_ref)arg1, (float_ref)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get the shell controls\n\n"

                ":param arg1: Min Value (rDUMMY for no limit)\n"
                ":type arg1: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg2: Max Value (rDUMMY for no limit)\n"
                ":type arg2: :class:`geosoft.gxapi.float_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.2.0\n\n"
               );
    pyClass.def("set_draw_controls", &GXVOXD_wrap_set_draw_controls,
                "set_draw_controls((int)arg1, (float)arg2, (float)arg3, (float)arg4, (float)arg5, (float)arg6, (float)arg7, (float)arg8) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set the draw controls\n\n"

                ":param arg1: Draw Bounding Box\n"
                ":type arg1: int\n"
                ":param arg2: Transparency\n"
                ":type arg2: float\n"
                ":param arg3: Min X\n"
                ":type arg3: float\n"
                ":param arg4: Min Y\n"
                ":type arg4: float\n"
                ":param arg5: Min Z\n"
                ":type arg5: float\n"
                ":param arg6: Max X\n"
                ":type arg6: float\n"
                ":param arg7: Max Y\n"
                ":type arg7: float\n"
                ":param arg8: Max Z\n"
                ":type arg8: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.2.0\n\n"
               );
    pyClass.def("set_itr", &GXVOXD_wrap_set_itr,
                "set_itr((GXITR)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set the ITR of the VOXD\n\n"

                ":param arg1: ITR object\n"
                ":type arg1: :class:`geosoft.gxapi.GXITR`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.2.0\n\n"
               );
    pyClass.def("set_shell_controls", &GXVOXD_wrap_set_shell_controls,
                "set_shell_controls((float)arg1, (float)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set the shell controls\n\n"

                ":param arg1: Min Value (rDUMMY for no limit)\n"
                ":type arg1: float\n"
                ":param arg2: Max Value (rDUMMY for no limit)\n"
                ":type arg2: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.2.0\n\n"
               );


}
