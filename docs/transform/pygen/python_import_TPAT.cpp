#include "stdafx.h"

using namespace boost::python;
using boost::python::init;


// Dummy classes


inline void GXTPAT_wrap_add_color(GXTPATPtr self, const gx_string_type& arg1, const gx_string_type& arg2, const gx_string_type& arg3, int32_t arg4)
{
    self->add_color(arg1, arg2, arg3, arg4);
}
inline GXTPATPtr GXTPAT_wrap_create()
{
    GXTPATPtr ret = GXTPAT::create();
    return ret;
}
inline int32_t GXTPAT_wrap_code(GXTPATPtr self, const gx_string_type& arg1)
{
    int32_t ret = self->code(arg1);
    return ret;
}
inline void GXTPAT_wrap_get_solid_pattern(GXTPATPtr self, int32_t arg1, str_ref& arg2, str_ref& arg3, str_ref& arg4, int_ref& arg5)
{
    self->get_solid_pattern(arg1, arg2, arg3, arg4, arg5);
}
inline int32_t GXTPAT_wrap_size(GXTPATPtr self)
{
    int32_t ret = self->size();
    return ret;
}
inline void GXTPAT_wrap_load_csv(GXTPATPtr self, const gx_string_type& arg1)
{
    self->load_csv(arg1);
}
inline void GXTPAT_wrap_setup_translation_vv(GXTPATPtr self, GXLTBPtr arg1, int32_t arg2, GXVVPtr arg3)
{
    self->setup_translation_vv(arg1, arg2, arg3);
}

void gxPythonImportGXTPAT()
{

    class_<GXTPAT, GXTPATPtr> pyClass("GXTPAT",
                                      "\n.. parsed-literal::\n\n"
                                      "   \n"
                                      "   		The full name of the pattern.\n"
                                      "   		ex: \"felsic volcanics\"\n"
                                      "   		Code:          Short-form of the pattern description. This is the value\n"
                                      "   		which typically appears (for instance) in the \"Rock code\"\n"
                                      "   		channel in a Wholeplot From-To data group.\n"
                                      "   		ex: \"FVOL\"\n"
                                      "   		The code is CASE-SENSITIVE.\n"
                                      "   \n"
                                      "   		Label:         Text to use as a short-form in labels, graphs etc.\n"
                                      "   		By default, this is the same as the code.\n"
                                      "   		ex: \"FVol.\"\n"
                                      "   		Pattern Attributes:  (See DEFAULT.PAT in \\src\\etc for more inforation)\n"
                                      "   		Pattern:       The Pattern Index; defined in DEFAULT.PAT, or in the user's\n"
                                      "   		USER.PAT file. If not specified, defaults to 0 (solid fill).\n"
                                      "   		Size:          The pattern tile size. If not specified, defaults to 2.0mm.\n"
                                      "   		Density:       The tiling density. If not specified, defaults to 1.0.\n"
                                      "   		Thickness:     The line thickness in the tile, expressed as a integer\n"
                                      "   		percentage (0-100) of the tile size.\n"
                                      "   		Colour:        The pattern line work colour. If not specified, defaults to black.\n"
                                      "   \n"
                                      "   		Background colour: The pattern background colour. If not specified, defaults to\n"
                                      "   		transparent (C_ANY_NONE)\n"
                                      "   \n"
                                      "   \n"
                                      "   		Symbols:\n"
                                      "   \n"
                                      "   		Symbol Font     The name of the symbol font to use for a given symbol index\n"
                                      "   \n"
                                      "   		Symbol Number   Index into the font.\n"
                                      "   \n"
                                      "   		Symbol Rotation: Rotation in degrees CCW.\n"
                                      "   \n"
                                      "   		Symbol Scaling  Additional scale factor to apply to symbol size (Default 1.0)\n"
                                      "   	\n\n"
                                      , no_init);

    pyClass.def("null", &GXTPAT::null, "null() -> GXTPAT\n\nA null (undefined) instance of :class:`geosoft.gxapi.GXTPAT`\n\n:returns: A null :class:`geosoft.gxapi.GXTPAT`\n:rtype: :class:`geosoft.gxapi.GXTPAT`\n").staticmethod("null");
    pyClass.def("is_null", &GXTPAT::is_null, "is_null() -> bool\n\nCheck if the instance of :class:`geosoft.gxapi.GXTPAT is null (undefined)`\n\n:returns: True if this is a null instance of :class:`geosoft.gxapi.GXTPAT`, False otherwise.\n:rtype: bool`\n");
    pyClass.def("_internal_handle", &GXTPAT::_internal_handle);
    pyClass.def("add_color", &GXTPAT_wrap_add_color,
                "add_color((str)arg1, (str)arg2, (str)arg3, (int)arg4) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Add a new color to the list\n\n"

                ":param arg1: Code (required - CASE SENSITIVE)\n"
                ":type arg1: str\n"
                ":param arg2: Label (optional, can be \"\")\n"
                ":type arg2: str\n"
                ":param arg3: Description (optional, can be \"\")\n"
                ":type arg3: str\n"
                ":param arg4: Color (use iColor_MVIEW to convert to int).\n"
                ":type arg4: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 7.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   The new code must be unique; not in the existing list.\n\n"
               );
    pyClass.def("create", &GXTPAT_wrap_create,
                "create() -> GXTPAT:\n"

                "\n.. parsed-literal::\n\n"
                "   Creates an empty thematic pattern object.\n\n"

                ":returns: TPAT object\n"
                ":rtype: :class:`geosoft.gxapi.GXTPAT`\n"
                "\n"

                "\n.. versionadded:: 7.0.0\n\n"
               ).staticmethod("create");
    pyClass.def("code", &GXTPAT_wrap_code,
                "code((str)arg1) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Find the index of a given thematic pattern\n\n"

                ":param arg1: Pattern code (case sensitive)\n"
                ":type arg1: str\n"
                ":returns: The code index, -1 if not found\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 7.0.0\n\n"
               );
    pyClass.def("get_solid_pattern", &GXTPAT_wrap_get_solid_pattern,
                "get_solid_pattern((int)arg1, (str_ref)arg2, (str_ref)arg3, (str_ref)arg4, (int_ref)arg5) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get solid pattern info from the TPAT.\n\n"

                ":param arg1: index\n"
                ":type arg1: int\n"
                ":param arg2: Returned Code\n"
                ":type arg2: :class:`geosoft.gxapi.str_ref`\n"
                ":param arg3: Returned Label\n"
                ":type arg3: :class:`geosoft.gxapi.str_ref`\n"
                ":param arg4: Returned Description\n"
                ":type arg4: :class:`geosoft.gxapi.str_ref`\n"
                ":param arg5: Color.\n"
                ":type arg5: :class:`geosoft.gxapi.int_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 7.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Returns the solid colour, pattern foreground color, or symbol\n"
                "   					color, along with the code, label and description.\n"
                "   				\n\n"
               );
    pyClass.def("size", &GXTPAT_wrap_size,
                "size() -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Returns the number of rows (items) in the TPAT object.\n\n"

                ":returns: Number of TPAT items.\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 7.0.0\n\n"
               );
    pyClass.def("load_csv", &GXTPAT_wrap_load_csv,
                "load_csv((str)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Load thematic patterns from a CSV file\n\n"

                ":param arg1: Thematic Pattern file name\n"
                ":type arg1: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 7.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					The type of thematic patterns file is recognized from the types\n"
                "   					of fields found inside it.\n"
                "   \n"
                "   					The following fields are identified. Only the \"CODE\" field is\n"
                "   					required, as the \"default\" thematic pattern is a solid black colour.\n"
                "   \n"
                "   					CODE   The pattern code (required by all types - CASE SENSITIVE)\n"
                "   					LABEL  Longer text identifier to use in legends etc. (up to 31 characters)\n"
                "   					DESCRIPTION Much longer text string (up to 127 characters).\n"
                "   \n"
                "   					COLOR  Line colour used in patterns, and for solid colours, the colour.\n"
                "   					If only this field is found (and none below), the pattern file\n"
                "   					is assumed to be type TPAT_TYPE_COLOR.\n"
                "   \n"
                "   					PATTERN         Geosoft pattern ID.\n"
                "   					PAT_SIZE        Pattern tile size, or symbol size (default 2mm)\n"
                "   					PAT_DENSITY     Pattern tile density (default 1.0)\n"
                "   					PAT_THICKNESS   Pattern line thickness as % of size (default 5)\n"
                "   					BACK_COLOR      Background color for the pattern. Also used for symbols\n"
                "   					(Default background is transparent).\n"
                "   \n"
                "   					SYMBFONT        Symbol font (e.g. \"symbols.gfn\")\n"
                "   					SYMBNUM         Symbol number of the current font\n"
                "   					SYMBROT         Symbol rotation\n"
                "   					SYMBSCL         Additional scaling factor applied to the current size\n"
                "   				\n\n"
               );
    pyClass.def("setup_translation_vv", &GXTPAT_wrap_setup_translation_vv,
                "setup_translation_vv((GXLTB)arg1, (int)arg2, (GXVV)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Initializes a VV used to map TPAT indices to output values\n\n"

                ":param arg1: Table containing TPAT codes as the key\n"
                ":type arg1: :class:`geosoft.gxapi.GXLTB`\n"
                ":param arg2: Field in LTB with the output values (numeric or string)\n"
                ":type arg2: int\n"
                ":param arg3: Returned values for each TPAT index\n"
                ":type arg3: :class:`geosoft.gxapi.GXVV`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 7.3.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					The input LTB object should have key values matching the TPAT codes.\n"
                "   					Whether the matches are case sensitive or not is dependent on how the\n"
                "   					LTB oject was created (see ltb.h).\n"
                "   					The LTB field values are converted to the output VV type.\n"
                "   				\n\n"
               );

    scope().attr("TPAT_CODE_SIZE") = (int32_t)21;
    scope().attr("TPAT_LABEL_SIZE") = (int32_t)32;
    scope().attr("TPAT_DESC_SIZE") = (int32_t)128;
    scope().attr("TPAT_SYMBFONT_SIZE") = (int32_t)32;

}
