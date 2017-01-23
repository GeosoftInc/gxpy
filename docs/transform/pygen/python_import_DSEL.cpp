#include "stdafx.h"

using namespace boost::python;
using boost::python::init;


// Dummy classes


inline GXDSELPtr GXDSEL_wrap_create()
{
    GXDSELPtr ret = GXDSEL::create();
    return ret;
}
inline void GXDSEL_wrap_data_significant_figures(GXDSELPtr self, double arg1)
{
    self->data_significant_figures(arg1);
}
inline void GXDSEL_wrap_meta_query(GXDSELPtr self, const gx_string_type& arg1)
{
    self->meta_query(arg1);
}
inline void GXDSEL_wrap_picture_quality(GXDSELPtr self, int32_t arg1)
{
    self->picture_quality(arg1);
}
inline void GXDSEL_wrap_request_all_info(GXDSELPtr self, int32_t arg1)
{
    self->request_all_info(arg1);
}
inline void GXDSEL_wrap_select_area(GXDSELPtr self, GXPLYPtr arg1)
{
    self->select_area(arg1);
}
inline void GXDSEL_wrap_select_rect(GXDSELPtr self, double arg1, double arg2, double arg3, double arg4)
{
    self->select_rect(arg1, arg2, arg3, arg4);
}
inline void GXDSEL_wrap_select_resolution(GXDSELPtr self, double arg1, int32_t arg2)
{
    self->select_resolution(arg1, arg2);
}
inline void GXDSEL_wrap_select_size(GXDSELPtr self, int32_t arg1, int32_t arg2)
{
    self->select_size(arg1, arg2);
}
inline void GXDSEL_wrap_set_extract_as_document(GXDSELPtr self, int32_t arg1)
{
    self->set_extract_as_document(arg1);
}
inline void GXDSEL_wrap_set_ipj(GXDSELPtr self, GXIPJPtr arg1, int32_t arg2)
{
    self->set_ipj(arg1, arg2);
}
inline void GXDSEL_wrap_spatial_accuracy(GXDSELPtr self, double arg1)
{
    self->spatial_accuracy(arg1);
}

void gxPythonImportGXDSEL()
{

    class_<GXDSEL, GXDSELPtr> pyClass("GXDSEL",
                                      "\n.. parsed-literal::\n\n"
                                      "   The DSEL object is used to select subsets of data from the DATA object\n\n"
                                      , no_init);

    pyClass.def("null", &GXDSEL::null, "null() -> GXDSEL\n\nA null (undefined) instance of :class:`geosoft.gxapi.GXDSEL`\n\n:returns: A null :class:`geosoft.gxapi.GXDSEL`\n:rtype: :class:`geosoft.gxapi.GXDSEL`\n").staticmethod("null");
    pyClass.def("is_null", &GXDSEL::is_null, "is_null() -> bool\n\nCheck if the instance of :class:`geosoft.gxapi.GXDSEL is null (undefined)`\n\n:returns: True if this is a null instance of :class:`geosoft.gxapi.GXDSEL`, False otherwise.\n:rtype: bool`\n");
    pyClass.def("_internal_handle", &GXDSEL::_internal_handle);
    pyClass.def("create", &GXDSEL_wrap_create,
                "create() -> GXDSEL:\n"

                "\n.. parsed-literal::\n\n"
                "   Create a Selection object\n\n"

                ":returns: DSEL handle, terminates if creation fails\n"
                ":rtype: :class:`geosoft.gxapi.GXDSEL`\n"
                "\n"

                "\n.. versionadded:: 5.0.3\n\n"
               ).staticmethod("create");
    pyClass.def("data_significant_figures", &GXDSEL_wrap_data_significant_figures,
                "data_significant_figures((float)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Specify the data significant figures required\n\n"

                ":param arg1: Significant figures (positive, can be fractional)\n"
                ":type arg1: float\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.8\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					This is the number of significant figures that you require for the data.\n"
                "   					You can reduce this number to achieve better compression ratios.\n"
                "   					This should only be used when there is one data type in the data.\n"
                "   \n"
                "   					See sSpatialResolution_DSEL to set the desired spatial resolution.\n"
                "   				\n\n"
               );
    pyClass.def("meta_query", &GXDSEL_wrap_meta_query,
                "meta_query((str)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Specify a metadata query string.\n\n"

                ":param arg1: Meta query string\n"
                ":type arg1: str\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.3\n\n"
               );
    pyClass.def("picture_quality", &GXDSEL_wrap_picture_quality,
                "picture_quality((int)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Specify the quality of pictures being returned.\n\n"

                ":param arg1: Quality\n"
                ":type arg1: int\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.4\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Affected Data Types: PICTURE\n\n"
               );
    pyClass.def("request_all_info", &GXDSEL_wrap_request_all_info,
                "request_all_info((int)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Request that all meta-data info be sent\n\n"

                ":param arg1: TRUE to for all data, FALSE - for normal data\n"
                ":type arg1: int\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.3\n\n"
               );
    pyClass.def("select_area", &GXDSEL_wrap_select_area,
                "select_area((GXPLY)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Select a complex clipping area\n\n"

                ":param arg1: PLY containing complex area (must contain a projection)\n"
                ":type arg1: :class:`geosoft.gxapi.GXPLY`\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.3\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					The DAP server may not handle clipping and may return\n"
                "   					more data than requested.\n"
                "   				\n\n"
               );
    pyClass.def("select_rect", &GXDSEL_wrap_select_rect,
                "select_rect((float)arg1, (float)arg2, (float)arg3, (float)arg4) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Select a rectangular area.\n\n"

                ":param arg1: Min X\n"
                ":type arg1: float\n"
                ":param arg2: Min Y\n"
                ":type arg2: float\n"
                ":param arg3: Max X\n"
                ":type arg3: float\n"
                ":param arg4: Max Y\n"
                ":type arg4: float\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.3\n\n"
               );
    pyClass.def("select_resolution", &GXDSEL_wrap_select_resolution,
                "select_resolution((float)arg1, (int)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Specify the resolution desired\n\n"

                ":param arg1: Minimum Resolution\n"
                ":type arg1: float\n"
                ":param arg2: TRUE to force this resolution, if possible\n"
                ":type arg2: int\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.3\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Resolution must be specified in the units of the selection IPJ.\n"
                "   \n"
                "   					This will be the optimum data resoulution.  (grid cell for grids, data\n"
                "   					separation for other data types).\n"
                "   					You will normally get a reasonable resolution as near to or smaller than\n"
                "   					this unless sRequireResolution_DSEL has been set.\n"
                "   \n"
                "   					Call sRequireResolution_DSEL with TRUE to force the client to re-sample\n"
                "   					the data to the resolution requested.\n"
                "   				\n\n"
               );
    pyClass.def("select_size", &GXDSEL_wrap_select_size,
                "select_size((int)arg1, (int)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Specify the image size desired\n\n"

                ":param arg1: Image width in pixels\n"
                ":type arg1: int\n"
                ":param arg2: Image height in pixels\n"
                ":type arg2: int\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 7.0.0\n\n"
               );
    pyClass.def("set_extract_as_document", &GXDSEL_wrap_set_extract_as_document,
                "set_extract_as_document((int)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Specify that we want to extract this file as a document\n\n"

                ":param arg1: TRUE (1) if we want as a document\n"
                ":type arg1: int\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 8.0.0\n\n"
               );
    pyClass.def("set_ipj", &GXDSEL_wrap_set_ipj,
                "set_ipj((GXIPJ)arg1, (int)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set the desired projection\n\n"

                ":param arg1: IPJ to set\n"
                ":type arg1: :class:`geosoft.gxapi.GXIPJ`\n"
                ":param arg2: TRUE to force reprojection, if possible\n"
                ":type arg2: int\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.8\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					If the server supports reprojection, the data will be\n"
                "   					reprojected at the server.\n"
                "   \n"
                "   					If reprojection is not forced, the data may come in any projection.\n"
                "   \n"
                "   					The spatial resolution and accuracy are accumed to be in the\n"
                "   					coordinate system defined by this IPJ.\n"
                "   				\n\n"
               );
    pyClass.def("spatial_accuracy", &GXDSEL_wrap_spatial_accuracy,
                "spatial_accuracy((float)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Specify the spatial accuracy required.\n\n"

                ":param arg1: spatial accuracy desired\n"
                ":type arg1: float\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.8\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Must be specified in the units of the selection IPJ.\n"
                "   \n"
                "   					The spatial accuracy is used improve compression performance for\n"
                "   					the spatial component of the data returned.\n"
                "   					You can reduce this number to achieve better compression ratios.\n"
                "   					This should only be used when there is one data type in the data.\n"
                "   				\n\n"
               );

    scope().attr("DSEL_PICTURE_QUALITY_DEFAULT") = (int32_t)0;
    scope().attr("DSEL_PICTURE_QUALITY_LOSSLESS") = (int32_t)1;
    scope().attr("DSEL_PICTURE_QUALITY_SEMILOSSY") = (int32_t)2;
    scope().attr("DSEL_PICTURE_QUALITY_LOSSY") = (int32_t)3;
    scope().attr("DSEL_PICTURE_QUALITY_NATIVE") = (int32_t)4;
    scope().attr("DSEL_PICTURE_QUALITY_ECW") = (int32_t)5;
    scope().attr("DSEL_PICTURE_QUALITY_JPG") = (int32_t)6;
    scope().attr("DSEL_PICTURE_QUALITY_PNG") = (int32_t)7;
    scope().attr("DSEL_PICTURE_QUALITY_BMP") = (int32_t)8;
    scope().attr("DSEL_PICTURE_QUALITY_TIF") = (int32_t)9;

}
