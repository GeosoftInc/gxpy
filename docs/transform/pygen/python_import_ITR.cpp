#include "stdafx.h"

using namespace boost::python;
using boost::python::init;


// Dummy classes


inline void GXITR_wrap_change_brightness(GXITRPtr self, double arg1)
{
    self->change_brightness(arg1);
}
inline void GXITR_wrap_color_vv(GXITRPtr self, GXVVPtr arg1, GXVVPtr arg2)
{
    self->color_vv(arg1, arg2);
}
inline void GXITR_wrap_copy(GXITRPtr self, GXITRPtr arg1)
{
    self->copy(arg1);
}
inline GXITRPtr GXITR_wrap_create()
{
    GXITRPtr ret = GXITR::create();
    return ret;
}
inline GXITRPtr GXITR_wrap_create_file(const gx_string_type& arg1)
{
    GXITRPtr ret = GXITR::create_file(arg1);
    return ret;
}
inline GXITRPtr GXITR_wrap_create_img(GXIMGPtr arg1, const gx_string_type& arg2, int32_t arg3, double arg4)
{
    GXITRPtr ret = GXITR::create_img(arg1, arg2, (ITR_ZONE)arg3, arg4);
    return ret;
}
inline GXITRPtr GXITR_wrap_create_map(GXMAPPtr arg1, const gx_string_type& arg2)
{
    GXITRPtr ret = GXITR::create_map(arg1, arg2);
    return ret;
}
inline GXITRPtr GXITR_wrap_create_s(GXBFPtr arg1)
{
    GXITRPtr ret = GXITR::create_s(arg1);
    return ret;
}
inline void GXITR_wrap_equal_area(GXITRPtr self, GXSTPtr arg1, double arg2)
{
    self->equal_area(arg1, arg2);
}
inline void GXITR_wrap_get_data_limits(GXITRPtr self, float_ref& arg1, float_ref& arg2)
{
    self->get_data_limits(arg1, arg2);
}
inline GXREGPtr GXITR_wrap_get_reg(GXITRPtr self)
{
    GXREGPtr ret = self->get_reg();
    return ret;
}
inline void GXITR_wrap_get_zone_color(GXITRPtr self, int32_t arg1, int_ref& arg2)
{
    self->get_zone_color(arg1, (MVIEW_COLOR&)arg2);
}
inline int32_t GXITR_wrap_color_value(GXITRPtr self, double arg1)
{
    MVIEW_COLOR ret = self->color_value(arg1);
    return ret;
}
inline int32_t GXITR_wrap_get_size(GXITRPtr self)
{
    int32_t ret = self->get_size();
    return ret;
}
inline int32_t GXITR_wrap_get_zone_model_type(GXITRPtr self)
{
    ITR_ZONE_MODEL ret = self->get_zone_model_type();
    return ret;
}
inline void GXITR_wrap_linear(GXITRPtr self, double arg1, double arg2, double arg3)
{
    self->linear(arg1, arg2, arg3);
}
inline void GXITR_wrap_load_a(GXITRPtr self, const gx_string_type& arg1)
{
    self->load_a(arg1);
}
inline void GXITR_wrap_log_linear(GXITRPtr self, double arg1, double arg2, double arg3)
{
    self->log_linear(arg1, arg2, arg3);
}
inline void GXITR_wrap_normal(GXITRPtr self, double arg1, double arg2, double arg3, double arg4)
{
    self->normal(arg1, arg2, arg3, arg4);
}
inline void GXITR_wrap_power_zone(GXITRPtr self, int32_t arg1)
{
    self->power_zone((ITR_POWER)arg1);
}
inline double GXITR_wrap_get_brightness(GXITRPtr self)
{
    double ret = self->get_brightness();
    return ret;
}
inline double GXITR_wrap_get_zone_value(GXITRPtr self, int32_t arg1)
{
    double ret = self->get_zone_value(arg1);
    return ret;
}
inline void GXITR_wrap_save_a(GXITRPtr self, const gx_string_type& arg1)
{
    self->save_a(arg1);
}
inline void GXITR_wrap_save_file(GXITRPtr self, const gx_string_type& arg1)
{
    self->save_file(arg1);
}
inline void GXITR_wrap_serial(GXITRPtr self, GXBFPtr arg1)
{
    self->serial(arg1);
}
inline void GXITR_wrap_set_agg_map(GXMAPPtr arg1, const gx_string_type& arg2, GXITRPtr arg3)
{
    GXITR::set_agg_map(arg1, arg2, arg3);
}
inline void GXITR_wrap_set_bright_contrast(GXITRPtr self, double arg1, double arg2)
{
    self->set_bright_contrast(arg1, arg2);
}
inline void GXITR_wrap_set_color_model(GXITRPtr self, int32_t arg1)
{
    self->set_color_model((ITR_COLOR_MODEL)arg1);
}
inline void GXITR_wrap_set_data_limits(GXITRPtr self, double arg1, double arg2)
{
    self->set_data_limits(arg1, arg2);
}
inline void GXITR_wrap_set_size(GXITRPtr self, int32_t arg1)
{
    self->set_size(arg1);
}
inline void GXITR_wrap_set_zone_color(GXITRPtr self, int32_t arg1, int32_t arg2)
{
    self->set_zone_color(arg1, (MVIEW_COLOR)arg2);
}
inline void GXITR_wrap_set_zone_value(GXITRPtr self, int32_t arg1, double arg2)
{
    self->set_zone_value(arg1, arg2);
}

void gxPythonImportGXITR()
{

    class_<GXITR, GXITRPtr> pyClass("GXITR",
                                    "\n.. parsed-literal::\n\n"
                                    "   \n"
                                    "   		The ITR class provides access to ITR files. An ITR file maps\n"
                                    "   		ranges of values to specific colours. The ITR object is typically\n"
                                    "   		used in conjunction with MVIEW objects (see MVIEW and MVU).\n"
                                    "   	\n\n"

                                    "\n\n**Note:**\n\n"

                                    "\n.. parsed-literal::\n\n"
                                    "   \n"
                                    "   		Histogram ranges and colour zone ranges\n"
                                    "   \n"
                                    "   		Histogram bins are defined with inclusive minima and exclusive maxima;\n"
                                    "   		for instance if Min = 0 and Inc = 1, then the second bin would include\n"
                                    "   		all values z such that  0 <= z < 1 (the first bin has all values < 0).\n"
                                    "   \n"
                                    "   		Colour zones used in displaying grids (ITR, ZON etc...) are the\n"
                                    "   		opposite, with exclusive minima and inclusive maxima.\n"
                                    "   		For instance, if a zone is defined from 0 to 1, then it would\n"
                                    "   		contain all values of z such that 0 < z <= 1.\n"
                                    "   \n"
                                    "   		These definitions mean that it is impossible to perfectly assign\n"
                                    "   		ITR colours to individual bars of a histogram. The best work-around\n"
                                    "   		when the data values are integers is to define the colour zones using\n"
                                    "   		0.5 values between the integers. A general work-around is to make the\n"
                                    "   		number of histogram bins much larger than the number of colour zones.\n"
                                    "   \n"
                                    "   		The \\ :func:`geosoft.gxapi.GXITR.null()`\\  is used to hold a NULL handle to an ITR class.\n"
                                    "   	\n\n"
                                    , no_init);

    pyClass.def("null", &GXITR::null, "null() -> GXITR\n\nA null (undefined) instance of :class:`geosoft.gxapi.GXITR`\n\n:returns: A null :class:`geosoft.gxapi.GXITR`\n:rtype: :class:`geosoft.gxapi.GXITR`\n").staticmethod("null");
    pyClass.def("is_null", &GXITR::is_null, "is_null() -> bool\n\nCheck if the instance of :class:`geosoft.gxapi.GXITR is null (undefined)`\n\n:returns: True if this is a null instance of :class:`geosoft.gxapi.GXITR`, False otherwise.\n:rtype: bool`\n");
    pyClass.def("_internal_handle", &GXITR::_internal_handle);
    pyClass.def("change_brightness", &GXITR_wrap_change_brightness,
                "change_brightness((float)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Change the brightness.\n\n"

                ":param arg1: -1.0 - black; 0.0 no change; 1.0 white\n"
                ":type arg1: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					0.0 brightness does nothing.\n"
                "   					-1.0 to 0.0 makes colours darker, -1.0 is black\n"
                "   					0.0 to 1.0 makes colours lighter, 1.0 is white\n"
                "   				\n\n"
               );
    pyClass.def("color_vv", &GXITR_wrap_color_vv,
                "color_vv((GXVV)arg1, (GXVV)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get color transform of a VV.\n\n"

                ":param arg1: Input VV of values (none-string)\n"
                ":type arg1: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg2: Output VV of colours (type INT)\n"
                ":type arg2: :class:`geosoft.gxapi.GXVV`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.6\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					If the input value is a dummy, then the output colour\n"
                "   					is 0 (no colour).\n"
                "   				\n\n"
               );
    pyClass.def("copy", &GXITR_wrap_copy,
                "copy((GXITR)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Copies ITRs\n\n"

                ":param arg1: ITR Source\n"
                ":type arg1: :class:`geosoft.gxapi.GXITR`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("create", &GXITR_wrap_create,
                "create() -> GXITR:\n"

                "\n.. parsed-literal::\n\n"
                "   Create an ITR Object\n\n"

                ":returns: ITR Object\n"
                ":rtype: :class:`geosoft.gxapi.GXITR`\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("create");
    pyClass.def("create_file", &GXITR_wrap_create_file,
                "create_file((str)arg1) -> GXITR:\n"

                "\n.. parsed-literal::\n\n"
                "   Create an ITR Object from an itr, tbl, zon, lut file.\n\n"

                ":param arg1: file name, type determined from extension\n"
                ":type arg1: str\n"
                ":returns: ITR Object\n"
                ":rtype: :class:`geosoft.gxapi.GXITR`\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("create_file");
    pyClass.def("create_img", &GXITR_wrap_create_img,
                "create_img((GXIMG)arg1, (str)arg2, (int)arg3, (float)arg4) -> GXITR:\n"

                "\n.. parsed-literal::\n\n"
                "   Create an ITR for an image.\n\n"

                ":param arg1: \n"
                ":type arg1: :class:`geosoft.gxapi.GXIMG`\n"
                ":param arg2: colour table name, NULL for default\n"
                ":type arg2: str\n"
                ":param arg3: \\ :ref:`ITR_ZONE`\\ \n"
                ":type arg3: int\n"
                ":param arg4: colour contour interval or rDUMMY\n"
                ":type arg4: float\n"
                ":returns: ITR Object\n"
                ":rtype: :class:`geosoft.gxapi.GXITR`\n"
                "\n"

                "\n.. versionadded:: 5.1.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					The ITR_ZONE_DEFAULT model will ask the IMG to provide\n"
                "   					a model if it can.\n"
                "   \n"
                "   					If a shaded relief model is selected, a shaded image\n"
                "   					will be created and a shaded image file will be created with\n"
                "   					the same name as the original grid but with the suffux \"_s\"\n"
                "   					added to the name part of the grid.\n"
                "   				\n\n"
               ).staticmethod("create_img");
    pyClass.def("create_map", &GXITR_wrap_create_map,
                "create_map((GXMAP)arg1, (str)arg2) -> GXITR:\n"

                "\n.. parsed-literal::\n\n"
                "   Create ITR from Map with Agg Group name.\n\n"

                ":param arg1: MAP on which to place the view\n"
                ":type arg1: :class:`geosoft.gxapi.GXMAP`\n"
                ":param arg2: Agg Group name\n"
                ":type arg2: str\n"
                ":returns: ITR Object\n"
                ":rtype: :class:`geosoft.gxapi.GXITR`\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("create_map");
    pyClass.def("create_s", &GXITR_wrap_create_s,
                "create_s((GXBF)arg1) -> GXITR:\n"

                "\n.. parsed-literal::\n\n"
                "   Create an ITR Object from a BF\n\n"

                ":param arg1: BF to serialize from\n"
                ":type arg1: :class:`geosoft.gxapi.GXBF`\n"
                ":returns: ITR Object\n"
                ":rtype: :class:`geosoft.gxapi.GXITR`\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("create_s");
    pyClass.def("equal_area", &GXITR_wrap_equal_area,
                "equal_area((GXST)arg1, (float)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Calculate an equal area transform.\n\n"

                ":param arg1: Stat object with a histogram\n"
                ":type arg1: :class:`geosoft.gxapi.GXST`\n"
                ":param arg2: colour contour interval or dummy for none\n"
                ":type arg2: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.2\n\n"
               );
    pyClass.def("get_data_limits", &GXITR_wrap_get_data_limits,
                "get_data_limits((float_ref)arg1, (float_ref)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get ITR max/min data limits.\n\n"

                ":param arg1: Data minimum value (or rDUMMY if not set)\n"
                ":type arg1: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg2: Data maximum value (or rDUMMY if not set)\n"
                ":type arg2: :class:`geosoft.gxapi.float_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					In some ITRs, especially those defined and\n"
                "   					embedded inside grid (IMG) objects, the\n"
                "   					actual data minimum and maximum values are\n"
                "   					stored. This function retrieves those values.\n"
                "   					This is NOT true of all ITR objects, and in\n"
                "   					those cases dummy values will be returned.\n"
                "   				\n\n"
               );
    pyClass.def("get_reg", &GXITR_wrap_get_reg,
                "get_reg() -> GXREG:\n"

                "\n.. parsed-literal::\n\n"
                "   Get the ITR's REG\n\n"

                ":returns: REG object\n"
                ":rtype: :class:`geosoft.gxapi.GXREG`\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("get_zone_color", &GXITR_wrap_get_zone_color,
                "get_zone_color((int)arg1, (int_ref)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get the colour in a zone of the ITR\n\n"

                ":param arg1: Number of the zone to set.\n"
                ":type arg1: int\n"
                ":param arg2: \\ :ref:`MVIEW_COLOR`\\ \n"
                ":type arg2: :class:`geosoft.gxapi.int_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Valid indices are 0 to N-1, where N is the size of the ITR.\n\n"
               );
    pyClass.def("color_value", &GXITR_wrap_color_value,
                "color_value((float)arg1) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Transform single data value to color\n\n"

                ":param arg1: Data value\n"
                ":type arg1: float\n"
                ":returns: \\ :ref:`MVIEW_COLOR`\\ \n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.1.0\n\n"
               );
    pyClass.def("get_size", &GXITR_wrap_get_size,
                "get_size() -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Get the number of zones in an ITR\n\n"

                ":returns: The number of zones.\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("get_zone_model_type", &GXITR_wrap_get_zone_model_type,
                "get_zone_model_type() -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Get the ITR zone model (e.g. Linear, LogLin, Equal Area).\n\n"

                ":returns: \\ :ref:`ITR_ZONE_MODEL`\\ \n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 6.4.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					This function may be used to determine if a colour\n"
                "   					transform is included in an ITR.\n"
                "   				\n\n"
               );
    pyClass.def("linear", &GXITR_wrap_linear,
                "linear((float)arg1, (float)arg2, (float)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Calculate a linear transform.\n\n"

                ":param arg1: minimum\n"
                ":type arg1: float\n"
                ":param arg2: maximum\n"
                ":type arg2: float\n"
                ":param arg3: colour contour interval or dummy for none\n"
                ":type arg3: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("load_a", &GXITR_wrap_load_a,
                "load_a((str)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Load to an ASCII file, ZON, TBL or ER-Mapper LUT\n\n"

                ":param arg1: file name\n"
                ":type arg1: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.6\n\n"
               );
    pyClass.def("log_linear", &GXITR_wrap_log_linear,
                "log_linear((float)arg1, (float)arg2, (float)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Calculate a log transform.\n\n"

                ":param arg1: minimum ( > 0)\n"
                ":type arg1: float\n"
                ":param arg2: maximum ( > minimum)\n"
                ":type arg2: float\n"
                ":param arg3: colour contour interval or dummy for none\n"
                ":type arg3: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   The function name is a misnomer. This is a pure log transform.\n\n"
               );
    pyClass.def("normal", &GXITR_wrap_normal,
                "normal((float)arg1, (float)arg2, (float)arg3, (float)arg4) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Calculate a normal distribution transform.\n\n"

                ":param arg1: Standard deviation\n"
                ":type arg1: float\n"
                ":param arg2: mean\n"
                ":type arg2: float\n"
                ":param arg3: expansion, normally 1.0\n"
                ":type arg3: float\n"
                ":param arg4: colour contour interval or dummy for none\n"
                ":type arg4: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.2\n\n"
               );
    pyClass.def("power_zone", &GXITR_wrap_power_zone,
                "power_zone((int)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Modified ITR zone values to 10 (or e) raized to the power of the values\n\n"

                ":param arg1: \\ :ref:`ITR_POWER`\\ \n"
                ":type arg1: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("get_brightness", &GXITR_wrap_get_brightness,
                "get_brightness() -> float:\n"

                "\n.. parsed-literal::\n\n"
                "   Get the brightness setting of the ITR\n\n"

                ":returns: The brightness setting of the ITR\n"
                ":rtype: float\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Brightness can range from -1.0 (black) to 1.0 (white).\n"
                "   					This brightness control is relative to the normal colour\n"
                "   					when the ITR is created.\n"
                "   				\n\n"

                "\n.. seealso::\n\n"
                "   \\ :func:`geosoft.gxapi.GXITR.change_brightness`\\ , \\ :func:`geosoft.gxapi.GXAGG.get_brightness`\\ , \\ :func:`geosoft.gxapi.GXAGG.change_brightness`\\ \n\n"
               );
    pyClass.def("get_zone_value", &GXITR_wrap_get_zone_value,
                "get_zone_value((int)arg1) -> float:\n"

                "\n.. parsed-literal::\n\n"
                "   Get the value in a zone of the ITR\n\n"

                ":param arg1: Number of the zone to set.\n"
                ":type arg1: int\n"
                ":returns: The value of the specified zone.\n"
                ":rtype: float\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Valid indices are 0 to N-2, where N is the size of the ITR.\n\n"
               );
    pyClass.def("save_a", &GXITR_wrap_save_a,
                "save_a((str)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Save to an ASCII file, ZON, TBL or ER-Mapper LUT\n\n"

                ":param arg1: file name\n"
                ":type arg1: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.2\n\n"
               );
    pyClass.def("save_file", &GXITR_wrap_save_file,
                "save_file((str)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Save to any type (based on the extension of the input file name).\n\n"

                ":param arg1: file name\n"
                ":type arg1: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 8.2\n\n"
               );
    pyClass.def("serial", &GXITR_wrap_serial,
                "serial((GXBF)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Serialize an ITR to a BF\n\n"

                ":param arg1: BF to serialize to\n"
                ":type arg1: :class:`geosoft.gxapi.GXBF`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("set_agg_map", &GXITR_wrap_set_agg_map,
                "set_agg_map((GXMAP)arg1, (str)arg2, (GXITR)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set ITR to an Agg in map\n\n"

                ":param arg1: MAP on which to place the view\n"
                ":type arg1: :class:`geosoft.gxapi.GXMAP`\n"
                ":param arg2: Agg group name\n"
                ":type arg2: str\n"
                ":param arg3: ITR object to set\n"
                ":type arg3: :class:`geosoft.gxapi.GXITR`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   See the \\ :func:`geosoft.gxapi.GXITR.create_map`\\  function\n\n"
               ).staticmethod("set_agg_map");
    pyClass.def("set_bright_contrast", &GXITR_wrap_set_bright_contrast,
                "set_bright_contrast((float)arg1, (float)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set the brightness of the ITR colours\n\n"

                ":param arg1: 0.0 - black; 0.5 normal; 1.0 white\n"
                ":type arg1: float\n"
                ":param arg2: 0.0 - flat; 1.0 normal\n"
                ":type arg2: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Brightness settings:\n"
                "   					0.0   - black\n"
                "   					0.5   - normal (no change)\n"
                "   					1.0   - white\n"
                "   \n"
                "   					Contrast\n"
                "   					0.0   - flat\n"
                "   					1.0   - full contrast (normal)\n"
                "   				\n\n"
               );
    pyClass.def("set_color_model", &GXITR_wrap_set_color_model,
                "set_color_model((int)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set the color model of an ITR.\n\n"

                ":param arg1: \\ :ref:`ITR_COLOR_MODEL`\\ \n"
                ":type arg1: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.2\n\n"
               );
    pyClass.def("set_data_limits", &GXITR_wrap_set_data_limits,
                "set_data_limits((float)arg1, (float)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set ITR max/min data limits.\n\n"

                ":param arg1: Data minimum value\n"
                ":type arg1: float\n"
                ":param arg2: Data maximum value\n"
                ":type arg2: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.3.0\n\n"
               );
    pyClass.def("set_size", &GXITR_wrap_set_size,
                "set_size((int)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set the number of zones in an ITR\n\n"

                ":param arg1: Number of zones to set ITR to.\n"
                ":type arg1: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("set_zone_color", &GXITR_wrap_set_zone_color,
                "set_zone_color((int)arg1, (int)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set the colour in a zone of the ITR\n\n"

                ":param arg1: Number of the zone to set.\n"
                ":type arg1: int\n"
                ":param arg2: \\ :ref:`MVIEW_COLOR`\\ \n"
                ":type arg2: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Valid indices are 0 to N-1, where N is the size of the ITR.\n\n"
               );
    pyClass.def("set_zone_value", &GXITR_wrap_set_zone_value,
                "set_zone_value((int)arg1, (float)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set the value in a zone of the ITR\n\n"

                ":param arg1: Number of the zone to set.\n"
                ":type arg1: int\n"
                ":param arg2: The value to set\n"
                ":type arg2: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Valid indices are 0 to N-2, where N is the size of the ITR.\n\n"
               );

    scope().attr("ITR_COLOR_MODEL_HSV") = (int32_t)1;
    scope().attr("ITR_COLOR_MODEL_RGB") = (int32_t)2;
    scope().attr("ITR_COLOR_MODEL_CMY") = (int32_t)3;
    scope().attr("ITR_POWER_10") = (int32_t)0;
    scope().attr("ITR_POWER_EXP") = (int32_t)1;
    scope().attr("ITR_ZONE_DEFAULT") = (int32_t)0;
    scope().attr("ITR_ZONE_LINEAR") = (int32_t)1;
    scope().attr("ITR_ZONE_NORMAL") = (int32_t)2;
    scope().attr("ITR_ZONE_EQUALAREA") = (int32_t)3;
    scope().attr("ITR_ZONE_SHADE") = (int32_t)4;
    scope().attr("ITR_ZONE_LOGLINEAR") = (int32_t)5;
    scope().attr("ITR_ZONE_MODEL_NOZONE") = (int32_t)-1;
    scope().attr("ITR_ZONE_MODEL_NONE") = (int32_t)0;
    scope().attr("ITR_ZONE_MODEL_LINEAR") = (int32_t)1;
    scope().attr("ITR_ZONE_MODEL_NORMAL") = (int32_t)2;
    scope().attr("ITR_ZONE_MODEL_EQUAL") = (int32_t)3;
    scope().attr("ITR_MODEL_LOGLIN") = (int32_t)4;

}
