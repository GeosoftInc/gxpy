#include "stdafx.h"

using namespace boost::python;
using boost::python::init;


// Dummy classes


inline GXDGWPtr GXDGW_wrap_create(const gx_string_type& arg1)
{
    GXDGWPtr ret = GXDGW::create(arg1);
    return ret;
}
inline void GXDGW_wrap_get_info_meta(GXDGWPtr self, int32_t arg1, int32_t arg2, GXMETAPtr arg3, int32_t arg4, int32_t arg5)
{
    self->get_info_meta(arg1, (DGW_OBJECT)arg2, arg3, arg4, arg5);
}
inline void GXDGW_wrap_get_info_sys(GXDGWPtr self, int32_t arg1, int32_t arg2, const gx_string_type& arg3, const gx_string_type& arg4)
{
    self->get_info_sys(arg1, (DGW_OBJECT)arg2, arg3, arg4);
}
inline GXLSTPtr GXDGW_wrap_get_list(GXDGWPtr self, int32_t arg1)
{
    GXLSTPtr ret = self->get_list(arg1);
    return ret;
}
inline void GXDGW_wrap_gt_info(GXDGWPtr self, int32_t arg1, int32_t arg2, str_ref& arg3)
{
    self->gt_info(arg1, (DGW_OBJECT)arg2, arg3);
}
inline int32_t GXDGW_wrap_run_dialogue(GXDGWPtr self)
{
    int32_t ret = self->run_dialogue();
    return ret;
}
inline void GXDGW_wrap_set_info(GXDGWPtr self, int32_t arg1, int32_t arg2, const gx_string_type& arg3)
{
    self->set_info(arg1, (DGW_OBJECT)arg2, arg3);
}
inline void GXDGW_wrap_set_info_meta(GXDGWPtr self, int32_t arg1, int32_t arg2, GXMETAPtr arg3, int32_t arg4, int32_t arg5)
{
    self->set_info_meta(arg1, (DGW_OBJECT)arg2, arg3, arg4, arg5);
}
inline void GXDGW_wrap_set_info_sys(GXDGWPtr self, int32_t arg1, int32_t arg2, const gx_string_type& arg3, const gx_string_type& arg4)
{
    self->set_info_sys(arg1, (DGW_OBJECT)arg2, arg3, arg4);
}
inline void GXDGW_wrap_set_title(GXDGWPtr self, const gx_string_type& arg1)
{
    self->set_title(arg1);
}

void gxPythonImportGXDGW()
{

    class_<GXDGW, GXDGWPtr> pyClass("GXDGW",
                                    "\n.. parsed-literal::\n\n"
                                    "   Provides access to dialog boxes for user I/O. You can\n"
                                    "   use this class to store to, or retrieve information from\n"
                                    "   the current workspace parameter block via dialog boxes\n\n"

                                    "\n\n**Note:**\n\n"

                                    "\n.. parsed-literal::\n\n"
                                    "   Setting Fonts in GX dialogs.\n"
                                    "   \n"
                                    "   By default, \"new look\" GX dialogs uses the \"Tahoma\" font. This font can be\n"
                                    "   overridden by updating the application settings. This can be done programmatically\n"
                                    "   using the \\ :func:`geosoft.gxapi.GXSYS.global_set`\\  function using the following parameters:\n"
                                    "   \n"
                                    "   MONTAJ.GX_FONT=\"Font_name\"\n"
                                    "   \n"
                                    "   This sets the default font to \"Font_name\". It applies to text in all\n"
                                    "   components of the dialog.\n"
                                    "   \n"
                                    "   Additional customization of individual components can be accomplished\n"
                                    "   using the following parameters:\n"
                                    "   \n"
                                    "   MONTAJ.GX_CAPTION_FONT=\"Caption_Font\": Font for the field captions (labels)\n"
                                    "   MONTAJ.GX_BUTTON_FONT=\"Button_Font\"  : Font for buttons, including the \"Browse\"\n"
                                    "                                   button\n"
                                    "   MONTAJ.GX_TITLE_FONT=\"Title_Font\"    : Font for special titles (see \\ :func:`geosoft.gxapi.GXDGW.set_title`\\ ).\n"
                                    "   \n"
                                    "   The font used for the text in edit windows remains the default, or the\n"
                                    "   value specified using MONTAJ.GX_FONT.\n"
                                    "   \n"
                                    "   Note that the \"OK\" button, and the Title, use \"Bold\" versions of the\n"
                                    "   specified font. If the bolded version does not exist as a normal font,\n"
                                    "   then the operating system may provide its own alternative which may not\n"
                                    "   appear the same as you expect.\n"
                                    "   \n"
                                    "   Before version 6.2. there used to be a parameter, MONTAJ.GX_CHARSET, that\n"
                                    "   affected characters above ASCII 127. 6.2. introduced Unicode in the core\n"
                                    "   montaj engine that eliminated the need for such a setting. All strings\n"
                                    "   on the GX API level are encoded in UTF8 during runtime which makes it possible\n"
                                    "   to represent all possible characters without using character sets.\n\n"
                                    , no_init);

    pyClass.def("null", &GXDGW::null, "null() -> GXDGW\n\nA null (undefined) instance of :class:`geosoft.gxapi.GXDGW`\n\n:returns: A null :class:`geosoft.gxapi.GXDGW`\n:rtype: :class:`geosoft.gxapi.GXDGW`\n").staticmethod("null");
    pyClass.def("is_null", &GXDGW::is_null, "is_null() -> bool\n\nCheck if the instance of :class:`geosoft.gxapi.GXDGW is null (undefined)`\n\n:returns: True if this is a null instance of :class:`geosoft.gxapi.GXDGW`, False otherwise.\n:rtype: bool`\n");
    pyClass.def("_internal_handle", &GXDGW::_internal_handle);
    pyClass.def("create", &GXDGW_wrap_create,
                "create((str)arg1) -> GXDGW:\n"

                "\n.. parsed-literal::\n\n"
                "   This method creates a Dialogue window from a specified\n"
                "   resource. The Resource is loaded into memory but not displayed.\n\n"

                ":param arg1: Name of the Window Resource to use\n"
                ":type arg1: str\n"
                ":returns: Handle to the DGW object.\n"
                ":rtype: :class:`geosoft.gxapi.GXDGW`\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("create");
    pyClass.def("get_info_meta", &GXDGW_wrap_get_info_meta,
                "get_info_meta((int)arg1, (int)arg2, (GXMETA)arg3, (int)arg4, (int)arg5) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Copies the Dialogue information to a META attribute.\n\n"

                ":param arg1: Dialogue Object\n"
                ":type arg1: int\n"
                ":param arg2: \\ :ref:`DGW_OBJECT`\\ \n"
                ":type arg2: int\n"
                ":param arg3: META\n"
                ":type arg3: :class:`geosoft.gxapi.GXMETA`\n"
                ":param arg4: Object\n"
                ":type arg4: int\n"
                ":param arg5: Attribute\n"
                ":type arg5: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("get_info_sys", &GXDGW_wrap_get_info_sys,
                "get_info_sys((int)arg1, (int)arg2, (str)arg3, (str)arg4) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   This method uses the information in a Dialogue box to\n"
                "   set a SYS variable.\n\n"

                ":param arg1: Dialogue Object\n"
                ":type arg1: int\n"
                ":param arg2: \\ :ref:`DGW_OBJECT`\\ \n"
                ":type arg2: int\n"
                ":param arg3: Group name of the Variable\n"
                ":type arg3: str\n"
                ":param arg4: Variable name\n"
                ":type arg4: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("get_list", &GXDGW_wrap_get_list,
                "get_list((int)arg1) -> GXLST:\n"

                "\n.. parsed-literal::\n\n"
                "   This method retrieves the list (LST) object associated\n"
                "   with a Dialogue object.\n\n"

                ":param arg1: Dialogue Object\n"
                ":type arg1: int\n"
                ":returns: The List Object\n"
                ":rtype: :class:`geosoft.gxapi.GXLST`\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("gt_info", &GXDGW_wrap_gt_info,
                "gt_info((int)arg1, (int)arg2, (str_ref)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   This method fills the specified string with the text from\n"
                "   the text object specified.\n\n"

                ":param arg1: Handle to the TEXT Object\n"
                ":type arg1: int\n"
                ":param arg2: \\ :ref:`DGW_OBJECT`\\ \n"
                ":type arg2: int\n"
                ":param arg3: Where to place the String\n"
                ":type arg3: :class:`geosoft.gxapi.str_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("run_dialogue", &GXDGW_wrap_run_dialogue,
                "run_dialogue() -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   This method runs the Dialogue window.\n\n"

                ":returns: The Exit Code of the Dialogue window.\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("set_info", &GXDGW_wrap_set_info,
                "set_info((int)arg1, (int)arg2, (str)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   This method sets the string of a text object. If the string\n"
                "   is too long it will be truncated.\n\n"

                ":param arg1: Handle to the TEXT Object\n"
                ":type arg1: int\n"
                ":param arg2: \\ :ref:`DGW_OBJECT`\\ \n"
                ":type arg2: int\n"
                ":param arg3: String to set the Text To\n"
                ":type arg3: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("set_info_meta", &GXDGW_wrap_set_info_meta,
                "set_info_meta((int)arg1, (int)arg2, (GXMETA)arg3, (int)arg4, (int)arg5) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   This sets a text object to the text found in a META attribute.\n\n"

                ":param arg1: Dialogue Object\n"
                ":type arg1: int\n"
                ":param arg2: \\ :ref:`DGW_OBJECT`\\ \n"
                ":type arg2: int\n"
                ":param arg3: META\n"
                ":type arg3: :class:`geosoft.gxapi.GXMETA`\n"
                ":param arg4: Object\n"
                ":type arg4: int\n"
                ":param arg5: Attribute\n"
                ":type arg5: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("set_info_sys", &GXDGW_wrap_set_info_sys,
                "set_info_sys((int)arg1, (int)arg2, (str)arg3, (str)arg4) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   This sets a text object to the text found in a system\n"
                "   parameter variable. If the variable has not been set,\n"
                "   the text is not set.\n\n"

                ":param arg1: Dialogue Object\n"
                ":type arg1: int\n"
                ":param arg2: \\ :ref:`DGW_OBJECT`\\ \n"
                ":type arg2: int\n"
                ":param arg3: Group name of the Variable\n"
                ":type arg3: str\n"
                ":param arg4: Variable name\n"
                ":type arg4: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("set_title", &GXDGW_wrap_set_title,
                "set_title((str)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Changes the title of the dialog.\n\n"

                ":param arg1: Title to set\n"
                ":type arg1: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   A \"Special\", additional title can be added to a dialog by using\n"
                "   the following syntax:\n"
                "   \n"
                "   \\ :func:`geosoft.gxapi.GXDGW.set_title`\\ (Diag, \"Window Title\\nAdditional Title\");\n"
                "   \n"
                "   In the title argument, a line break character '\\n' is used to\n"
                "   separate the parts.\n"
                "   \n"
                "   The window title free_appears as the title in the upper bar of the dialog.\n"
                "   The additional title free_appears below this, in the main body of the\n"
                "   dialog, and is separated from the rest of the fields by a horizontal\n"
                "   line. It is printed in the bold version of the default font (or of the\n"
                "   special font specified using the MONTAJ.GX_TITLE_FONT parameter noted\n"
                "   above in \"Setting Fonts in GX dialogs.\"\n\n"
               );

    scope().attr("DGW_LABEL") = (int32_t)0;
    scope().attr("DGW_TEXT") = (int32_t)1;
    scope().attr("DGW_PATH") = (int32_t)2;
    scope().attr("DGW_FILEPATH") = (int32_t)3;
    scope().attr("DGW_LISTVAL") = (int32_t)4;
    scope().attr("DGW_LISTALIAS") = (int32_t)5;
    scope().attr("DGW_EXT") = (int32_t)7;
    scope().attr("DGW_HIDE") = (int32_t)8;

}
