#include "stdafx.h"

using namespace boost::python;
using boost::python::init;


// Dummy classes


inline void GXAGG_wrap_set_model(GXAGGPtr self, int32_t arg1)
{
    self->set_model((AGG_MODEL)arg1);
}
inline void GXAGG_wrap_change_brightness(GXAGGPtr self, double arg1)
{
    self->change_brightness(arg1);
}
inline GXAGGPtr GXAGG_wrap_create()
{
    GXAGGPtr ret = GXAGG::create();
    return ret;
}
inline GXAGGPtr GXAGG_wrap_create_map(GXMAPPtr arg1, const gx_string_type& arg2)
{
    GXAGGPtr ret = GXAGG::create_map(arg1, arg2);
    return ret;
}
inline void GXAGG_wrap_get_layer_itr(GXAGGPtr self, int32_t arg1, GXITRPtr arg2)
{
    self->get_layer_itr(arg1, arg2);
}
inline int32_t GXAGG_wrap_list_img(GXAGGPtr self, GXVVPtr arg1)
{
    int32_t ret = self->list_img(arg1);
    return ret;
}
inline int32_t GXAGG_wrap_num_layers(GXAGGPtr self)
{
    int32_t ret = self->num_layers();
    return ret;
}
inline void GXAGG_wrap_layer_img(GXAGGPtr self, const gx_string_type& arg1, int32_t arg2, const gx_string_type& arg3, double arg4)
{
    self->layer_img(arg1, (AGG_LAYER_ZONE)arg2, arg3, arg4);
}
inline void GXAGG_wrap_layer_img_ex(GXAGGPtr self, const gx_string_type& arg1, int32_t arg2, const gx_string_type& arg3, double arg4, double arg5, double arg6)
{
    self->layer_img_ex(arg1, (AGG_LAYER_ZONE)arg2, arg3, arg4, arg5, arg6);
}
inline void GXAGG_wrap_layer_shade_img(GXAGGPtr self, const gx_string_type& arg1, const gx_string_type& arg2, double arg3, double arg4, float_ref& arg5)
{
    self->layer_shade_img(arg1, arg2, arg3, arg4, arg5);
}
inline double GXAGG_wrap_get_brightness(GXAGGPtr self)
{
    double ret = self->get_brightness();
    return ret;
}
inline void GXAGG_wrap_set_layer_itr(GXAGGPtr self, int32_t arg1, GXITRPtr arg2)
{
    self->set_layer_itr(arg1, arg2);
}
inline void GXAGG_wrap_set_render_method(GXAGGPtr self, int32_t arg1)
{
    self->set_render_method((AGG_RENDER)arg1);
}

void gxPythonImportGXAGG()
{

    class_<GXAGG, GXAGGPtr> pyClass("GXAGG",
                                    "\n.. parsed-literal::\n\n"
                                    "   \n"
                                    "   		The AGG class is used to handle image display on maps.\n"
                                    "   		An aggragate contains one or more image layers (LAY) with\n"
                                    "   		each layer representing a grid or image file. The AGG\n"
                                    "   		will combine all the layers to form one image\n"
                                    "   	\n\n"
                                    , no_init);

    pyClass.def("null", &GXAGG::null, "null() -> GXAGG\n\nA null (undefined) instance of :class:`geosoft.gxapi.GXAGG`\n\n:returns: A null :class:`geosoft.gxapi.GXAGG`\n:rtype: :class:`geosoft.gxapi.GXAGG`\n").staticmethod("null");
    pyClass.def("is_null", &GXAGG::is_null, "is_null() -> bool\n\nCheck if the instance of :class:`geosoft.gxapi.GXAGG is null (undefined)`\n\n:returns: True if this is a null instance of :class:`geosoft.gxapi.GXAGG`, False otherwise.\n:rtype: bool`\n");
    pyClass.def("_internal_handle", &GXAGG::_internal_handle);
    pyClass.def("set_model", &GXAGG_wrap_set_model,
                "set_model((int)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Sets the Color Model\n\n"

                ":param arg1: \\ :ref:`AGG_MODEL`\\ \n"
                ":type arg1: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("change_brightness", &GXAGG_wrap_change_brightness,
                "change_brightness((float)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Change the brightness.\n\n"

                ":param arg1: -1.0 - black; 0.0 no change; 1.0 white\n"
                ":type arg1: float\n"
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
    pyClass.def("create", &GXAGG_wrap_create,
                "create() -> GXAGG:\n"

                "\n.. parsed-literal::\n\n"
                "   Create an aggregate\n\n"

                ":returns: AGG Object\n"
                ":rtype: :class:`geosoft.gxapi.GXAGG`\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("create");
    pyClass.def("create_map", &GXAGG_wrap_create_map,
                "create_map((GXMAP)arg1, (str)arg2) -> GXAGG:\n"

                "\n.. parsed-literal::\n\n"
                "   Create AGG from Map with Group name.\n\n"

                ":param arg1: MAP on which to place the view\n"
                ":type arg1: :class:`geosoft.gxapi.GXMAP`\n"
                ":param arg2: Agg Group name\n"
                ":type arg2: str\n"
                ":returns: AGG Object\n"
                ":rtype: :class:`geosoft.gxapi.GXAGG`\n"
                "\n"

                "\n.. versionadded:: 5.0.5\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					The Agg Group name must include the View name with a\n"
                "   					backslash separating the view name and group name; e.g.\n"
                "   					\"Data\\\\AGG_test\" (when used as a string, the double slash\n"
                "   					represents as single \\).\n"
                "   				\n\n"
               ).staticmethod("create_map");
    pyClass.def("get_layer_itr", &GXAGG_wrap_get_layer_itr,
                "get_layer_itr((int)arg1, (GXITR)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get the ITR of a layer\n\n"

                ":param arg1: layer number\n"
                ":type arg1: int\n"
                ":param arg2: ITR\n"
                ":type arg2: :class:`geosoft.gxapi.GXITR`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Layers are numbered from 0, consecutively in the order they are\n"
                "   					placed in the aggregate.\n"
                "   \n"
                "   					An error will occur if the layer does not exist.\n"
                "   \n"
                "   					Caller must create/destroy ITR.\n"
                "   				\n\n"
               );
    pyClass.def("list_img", &GXAGG_wrap_list_img,
                "list_img((GXVV)arg1) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Lists file names of all the IMGs inside of the AGG.\n\n"

                ":param arg1: VV of type -STR_FILE\n"
                ":type arg1: :class:`geosoft.gxapi.GXVV`\n"
                ":returns: The number of Imgs.\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.6\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   The returned VV contains the file names.\n\n"
               );
    pyClass.def("num_layers", &GXAGG_wrap_num_layers,
                "num_layers() -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Get the number of layers in an aggregate.\n\n"

                ":returns: The number of layers in an aggregate.\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("layer_img", &GXAGG_wrap_layer_img,
                "layer_img((str)arg1, (int)arg2, (str)arg3, (float)arg4) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Add an image as a layer in an aggregate.\n\n"

                ":param arg1: grid name\n"
                ":type arg1: str\n"
                ":param arg2: \\ :ref:`AGG_LAYER_ZONE`\\  transform to use if colour table has none defined.\n"
                ":type arg2: int\n"
                ":param arg3: colour table name, \"\" for default This can be a .TBL .ZON .ITR or .AGG file .TBL is the default\n"
                ":type arg3: str\n"
                ":param arg4: colour contour interval or rDUMMY for default\n"
                ":type arg4: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n.. seealso::\n\n"
                "   \\ :func:`geosoft.gxapi.GXAGG.layer_shade_img`\\ \n\n"
               );
    pyClass.def("layer_img_ex", &GXAGG_wrap_layer_img_ex,
                "layer_img_ex((str)arg1, (int)arg2, (str)arg3, (float)arg4, (float)arg5, (float)arg6) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Add an image as a layer in an aggregate.\n\n"

                ":param arg1: grid name\n"
                ":type arg1: str\n"
                ":param arg2: \\ :ref:`AGG_LAYER_ZONE`\\  transform to use if colour table has none defined.\n"
                ":type arg2: int\n"
                ":param arg3: colour table name, \"\" for default This can be a .TBL .ZON .ITR or .AGG file .TBL is the default\n"
                ":type arg3: str\n"
                ":param arg4: minimum value or rDUMMY for default\n"
                ":type arg4: float\n"
                ":param arg5: maximum value or rDUMMY for default\n"
                ":type arg5: float\n"
                ":param arg6: colour contour interval or rDUMMY for default\n"
                ":type arg6: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 8.2\n\n"

                "\n.. seealso::\n\n"
                "   \\ :func:`geosoft.gxapi.GXAGG.layer_shade_img`\\ \n\n"
               );
    pyClass.def("layer_shade_img", &GXAGG_wrap_layer_shade_img,
                "layer_shade_img((str)arg1, (str)arg2, (float)arg3, (float)arg4, (float_ref)arg5) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Add a shaded image as a layer in an aggregate.\n\n"

                ":param arg1: grid name\n"
                ":type arg1: str\n"
                ":param arg2: colour table name, \"\" for default\n"
                ":type arg2: str\n"
                ":param arg3: inclination\n"
                ":type arg3: float\n"
                ":param arg4: declination\n"
                ":type arg4: float\n"
                ":param arg5: scale (rDUMMY for default, returns value used)\n"
                ":type arg5: :class:`geosoft.gxapi.float_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					A new grid file will be created to hold the shaded\n"
                "   					image data.  This file will have the same name as the\n"
                "   					original grid but with \"_s\" added to the root name.\n"
                "   					It will always be located in the workspace directory\n"
                "   					regardless of the location of the original source image.\n"
                "   					If the file already exists, it will replaced.\n"
                "   				\n\n"
               );
    pyClass.def("get_brightness", &GXAGG_wrap_get_brightness,
                "get_brightness() -> float:\n"

                "\n.. parsed-literal::\n\n"
                "   Get the brightness setting of the AGG\n\n"

                ":rtype: float\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Brightness can range from -1.0 (black) to 1.0 (white).\n"
                "   					This brightness control is relative to the normal colour\n"
                "   					when the AGG is created.\n"
                "   \n"
                "   					AGG brightness depends on the brightness of the ITR of each layer.\n"
                "   					Calling dGetBright_AGG will poll all layers, and if all have the same\n"
                "   					brightness, this is returned.  If any of the layers have a different\n"
                "   					brightness, the current brightness of each layer is changed to be\n"
                "   					the reference brightness (0.0)and the brightness value of 0.0 is\n"
                "   					returned.\n"
                "   				\n\n"

                "\n.. seealso::\n\n"
                "   \\ :func:`geosoft.gxapi.GXAGG.change_brightness`\\ , \\ :func:`geosoft.gxapi.GXAGG.get_brightness`\\ , \\ :func:`geosoft.gxapi.GXAGG.change_brightness`\\ \n\n"
               );
    pyClass.def("set_layer_itr", &GXAGG_wrap_set_layer_itr,
                "set_layer_itr((int)arg1, (GXITR)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set the ITR of a layer\n\n"

                ":param arg1: layer number\n"
                ":type arg1: int\n"
                ":param arg2: ITR\n"
                ":type arg2: :class:`geosoft.gxapi.GXITR`\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Layers are numbered from 0, consecutively in the order they are\n"
                "   					placed in the aggregate.\n"
                "   \n"
                "   					An error will occur if the layer does not exist.\n"
                "   \n"
                "   					Caller must create/destroy ITR.\n"
                "   				\n\n"
               );
    pyClass.def("set_render_method", &GXAGG_wrap_set_render_method,
                "set_render_method((int)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Sets the Rendering Method\n\n"

                ":param arg1: \\ :ref:`AGG_RENDER`\\ \n"
                ":type arg1: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.1\n\n"
               );

    scope().attr("AGG_LAYER_ZONE_DEFAULT") = (int32_t)0;
    scope().attr("AGG_LAYER_ZONE_LINEAR") = (int32_t)1;
    scope().attr("AGG_LAYER_ZONE_NORMAL") = (int32_t)2;
    scope().attr("AGG_LAYER_ZONE_EQUALAREA") = (int32_t)3;
    scope().attr("AGG_LAYER_ZONE_SHADE") = (int32_t)4;
    scope().attr("AGG_LAYER_ZONE_LOGLINEAR") = (int32_t)5;
    scope().attr("AGG_LAYER_ZONE_LAST") = (int32_t)6;
    scope().attr("AGG_MODEL_HSV") = (int32_t)1;
    scope().attr("AGG_MODEL_RGB") = (int32_t)2;
    scope().attr("AGG_MODEL_CMY") = (int32_t)3;
    scope().attr("AGG_RENDER_ADD") = (int32_t)0;
    scope().attr("AGG_RENDER_BLEND") = (int32_t)1;
    scope().attr("AGG_RENDER_BLEND_ALL") = (int32_t)2;
    scope().attr("AGG_RENDER_FADE") = (int32_t)3;

}
