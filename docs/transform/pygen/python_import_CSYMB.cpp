#include "stdafx.h"

using namespace boost::python;
using boost::python::init;


// Dummy classes


inline void GXCSYMB_wrap_set_angle(GXCSYMBPtr self, double arg1)
{
    self->set_angle(arg1);
}
inline void GXCSYMB_wrap_set_base(GXCSYMBPtr self, double arg1)
{
    self->set_base(arg1);
}
inline void GXCSYMB_wrap_set_dynamic_col(GXCSYMBPtr self, int32_t arg1)
{
    self->set_dynamic_col((CSYMB_COLOR)arg1);
}
inline void GXCSYMB_wrap_set_fixed(GXCSYMBPtr self, int32_t arg1)
{
    self->set_fixed(arg1);
}
inline void GXCSYMB_wrap_set_number(GXCSYMBPtr self, int32_t arg1)
{
    self->set_number(arg1);
}
inline void GXCSYMB_wrap_set_scale(GXCSYMBPtr self, double arg1)
{
    self->set_scale(arg1);
}
inline void GXCSYMB_wrap_add_data(GXCSYMBPtr self, GXVVPtr arg1, GXVVPtr arg2, GXVVPtr arg3)
{
    self->add_data(arg1, arg2, arg3);
}
inline GXCSYMBPtr GXCSYMB_wrap_create(const gx_string_type& arg1)
{
    GXCSYMBPtr ret = GXCSYMB::create(arg1);
    return ret;
}
inline void GXCSYMB_wrap_set_font(GXCSYMBPtr self, const gx_string_type& arg1, int32_t arg2, int32_t arg3, int32_t arg4)
{
    self->set_font(arg1, arg2, (MVIEW_FONT_WEIGHT)arg3, arg4);
}
inline void GXCSYMB_wrap_set_static_col(GXCSYMBPtr self, int32_t arg1, int32_t arg2)
{
    self->set_static_col(arg1, (CSYMB_COLOR)arg2);
}

void gxPythonImportGXCSYMB()
{

    class_<GXCSYMB, GXCSYMBPtr> pyClass("GXCSYMB",
                                        "\n.. parsed-literal::\n\n"
                                        "   This class is used for generating and modifying colored symbol objects.\n"
                                        "   Symbol fills are assigned colors based on their Z values and a zone, Aggregate\n"
                                        "   or ITR file which defines what colors are associated with different ranges\n"
                                        "   of Z values. The position of a symbol is defined by its X,Y coordinates.\n\n"
                                        , no_init);

    pyClass.def("null", &GXCSYMB::null, "null() -> GXCSYMB\n\nA null (undefined) instance of :class:`geosoft.gxapi.GXCSYMB`\n\n:returns: A null :class:`geosoft.gxapi.GXCSYMB`\n:rtype: :class:`geosoft.gxapi.GXCSYMB`\n").staticmethod("null");
    pyClass.def("is_null", &GXCSYMB::is_null, "is_null() -> bool\n\nCheck if the instance of :class:`geosoft.gxapi.GXCSYMB is null (undefined)`\n\n:returns: True if this is a null instance of :class:`geosoft.gxapi.GXCSYMB`, False otherwise.\n:rtype: bool`\n");
    pyClass.def("_internal_handle", &GXCSYMB::_internal_handle);
    pyClass.def("set_angle", &GXCSYMB_wrap_set_angle,
                "set_angle((float)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set the symbol angle.\n\n"

                ":param arg1: Symbol angle\n"
                ":type arg1: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("set_base", &GXCSYMB_wrap_set_base,
                "set_base((float)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set base value to subtract from Z values.\n\n"

                ":param arg1: Symbol Base\n"
                ":type arg1: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("set_dynamic_col", &GXCSYMB_wrap_set_dynamic_col,
                "set_dynamic_col((int)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Associate symbol edge or fill colors with Z data\n"
                "   and color transform.\n\n"

                ":param arg1: \\ :ref:`CSYMB_COLOR`\\ \n"
                ":type arg1: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Use this method after a call to \\ :func:`geosoft.gxapi.GXCSYMB.set_static_col`\\ . This method\n"
                "   reestablishes the symbol color association with their Z data\n"
                "   values and color transform.\n\n"
               );
    pyClass.def("set_fixed", &GXCSYMB_wrap_set_fixed,
                "set_fixed((int)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set symbol sizing to fixed (or proportionate)\n\n"

                ":param arg1: TRUE  = Fixed symbol sizing FALSE = Proportionate sizing\n"
                ":type arg1: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("set_number", &GXCSYMB_wrap_set_number,
                "set_number((int)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set the symbol number.\n\n"

                ":param arg1: Symbol number (0x1-0x1ffff)\n"
                ":type arg1: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   The lower 16 bits of the number is interpreted as UTF-16 with a valid Unicode character\n"
                "   code point. GFN fonts wil produce valid symbols depending on the font for 0x01-0x7f and the degree,\n"
                "   plus-minus and diameter symbol(latin small letter o with stroke) for 0xB0, 0xB1 and 0xF8 respectively.\n"
                "   \n"
                "   It is possible to check if a character is valid using \\ :func:`geosoft.gxapi.GXUNC.is_valid_utf16_char`\\ . The high 16-bits are reserved\n"
                "   for future use. Also see: \\ :func:`geosoft.gxapi.GXUNC.valid_symbol`\\  and \\ :func:`geosoft.gxapi.GXUNC.validate_symbols`\\ \n\n"
               );
    pyClass.def("set_scale", &GXCSYMB_wrap_set_scale,
                "set_scale((float)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set the symbol scale.\n\n"

                ":param arg1: Symbol scale (> 0.0)\n"
                ":type arg1: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("add_data", &GXCSYMB_wrap_add_data,
                "add_data((GXVV)arg1, (GXVV)arg2, (GXVV)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Add x,y,z data to a color symbol object.\n\n"

                ":param arg1: VV for X data\n"
                ":type arg1: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg2: VV for Y data\n"
                ":type arg2: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg3: VV for Z data\n"
                ":type arg3: :class:`geosoft.gxapi.GXVV`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("create", &GXCSYMB_wrap_create,
                "create((str)arg1) -> GXCSYMB:\n"

                "\n.. parsed-literal::\n\n"
                "   Create a CSYMB.\n\n"

                ":param arg1: ZON, AGG, or ITR file name\n"
                ":type arg1: str\n"
                ":returns: CSYMB handle\n"
                ":rtype: :class:`geosoft.gxapi.GXCSYMB`\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("create");
    pyClass.def("set_font", &GXCSYMB_wrap_set_font,
                "set_font((str)arg1, (int)arg2, (int)arg3, (int)arg4) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set the symbol font name.\n\n"

                ":param arg1: Font name\n"
                ":type arg1: str\n"
                ":param arg2: Geosoft font? (TRUE or FALSE)\n"
                ":type arg2: int\n"
                ":param arg3: \\ :ref:`MVIEW_FONT_WEIGHT`\\ \n"
                ":type arg3: int\n"
                ":param arg4: Italics? (TRUE or FALSE)\n"
                ":type arg4: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("set_static_col", &GXCSYMB_wrap_set_static_col,
                "set_static_col((int)arg1, (int)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set a static color for the symbol edge or fill.\n\n"

                ":param arg1: Color value\n"
                ":type arg1: int\n"
                ":param arg2: \\ :ref:`CSYMB_COLOR`\\ \n"
                ":type arg2: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Use this method to set a STATIC color for symbol edge or fill.\n"
                "   By default, both edge and fill colors vary according to their\n"
                "   Z data values and a color transform.\n\n"
               );

    scope().attr("CSYMB_COLOR_EDGE") = (int32_t)0;
    scope().attr("CSYMB_COLOR_FILL") = (int32_t)1;

}
