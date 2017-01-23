#include "stdafx.h"

using namespace boost::python;
using boost::python::init;


// Dummy classes


inline void GXIGRF_wrap_calc(GXIGRFPtr self, double arg1, double arg2, double arg3, float_ref& arg4, float_ref& arg5, float_ref& arg6)
{
    self->calc(arg1, arg2, arg3, arg4, arg5, arg6);
}
inline void GXIGRF_wrap_calc_vv(GXIGRFPtr self, GXVVPtr arg1, GXVVPtr arg2, GXVVPtr arg3, GXVVPtr arg4, GXVVPtr arg5, GXVVPtr arg6)
{
    self->calc_vv(arg1, arg2, arg3, arg4, arg5, arg6);
}
inline GXIGRFPtr GXIGRF_wrap_create(double arg1, int32_t arg2, const gx_string_type& arg3)
{
    GXIGRFPtr ret = GXIGRF::create(arg1, arg2, arg3);
    return ret;
}
inline void GXIGRF_wrap_date_range(const gx_string_type& arg1, float_ref& arg2, float_ref& arg3)
{
    GXIGRF::date_range(arg1, arg2, arg3);
}

void gxPythonImportGXIGRF()
{

    class_<GXIGRF, GXIGRFPtr> pyClass("GXIGRF",
                                      "\n.. parsed-literal::\n\n"
                                      "   \n"
                                      "   		International Geomagnetic Reference Field\n"
                                      "   		Methods to work with IGRF objects. The IGRF object\n"
                                      "   		contains data for the IGRF model of the geomagnetic\n"
                                      "   		reference field.\n"
                                      "   	\n\n"
                                      , no_init);

    pyClass.def("null", &GXIGRF::null, "null() -> GXIGRF\n\nA null (undefined) instance of :class:`geosoft.gxapi.GXIGRF`\n\n:returns: A null :class:`geosoft.gxapi.GXIGRF`\n:rtype: :class:`geosoft.gxapi.GXIGRF`\n").staticmethod("null");
    pyClass.def("is_null", &GXIGRF::is_null, "is_null() -> bool\n\nCheck if the instance of :class:`geosoft.gxapi.GXIGRF is null (undefined)`\n\n:returns: True if this is a null instance of :class:`geosoft.gxapi.GXIGRF`, False otherwise.\n:rtype: bool`\n");
    pyClass.def("_internal_handle", &GXIGRF::_internal_handle);
    pyClass.def("calc", &GXIGRF_wrap_calc,
                "calc((float)arg1, (float)arg2, (float)arg3, (float_ref)arg4, (float_ref)arg5, (float_ref)arg6) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Calculate IGRF data for a given IGRF model.\n\n"

                ":param arg1: Elevation (metres)\n"
                ":type arg1: float\n"
                ":param arg2: Longitude (-180 to 180)\n"
                ":type arg2: float\n"
                ":param arg3: Latitude  (-90 to 90) Returns\n"
                ":type arg3: float\n"
                ":param arg4: Field strength\n"
                ":type arg4: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg5: Field inclination\n"
                ":type arg5: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg6: Field declination\n"
                ":type arg6: :class:`geosoft.gxapi.float_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Calculate IGRF data (total field, inclination, and declination)\n"
                "   					for a given IGRF model. The model used will be the same as that\n"
                "   					obtained with \\ :func:`geosoft.gxapi.GXIGRF.create`\\ .\n"
                "   				\n\n"
               );
    pyClass.def("calc_vv", &GXIGRF_wrap_calc_vv,
                "calc_vv((GXVV)arg1, (GXVV)arg2, (GXVV)arg3, (GXVV)arg4, (GXVV)arg5, (GXVV)arg6) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Calculate IGRF data VV's for a given IGRF model.\n\n"

                ":param arg1: Input elevation data (metres)\n"
                ":type arg1: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg2: Input longitude data (-180 to 180)\n"
                ":type arg2: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg3: Input latitude data  (-90 to 90)\n"
                ":type arg3: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg4: Output total field\n"
                ":type arg4: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg5: Output inclination\n"
                ":type arg5: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg6: Output declination\n"
                ":type arg6: :class:`geosoft.gxapi.GXVV`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Calculate IGRF data (total field, inclination, and declination)\n"
                "   					for a given IGRF model. The model used will be the same as that\n"
                "   					obtained with \\ :func:`geosoft.gxapi.GXIGRF.create`\\ .\n"
                "   					All of the VV's should be the same length. The function\n"
                "   					will abort if they are not.\n"
                "   \n"
                "   					No assumption is made on what data types are contained by\n"
                "   					any of the VV's. However, all total field, inclination, and\n"
                "   					declination values are internally calculated as real data.\n"
                "   					These values will be converted to the types contained in the\n"
                "   					output VV's.\n"
                "   				\n\n"
               );
    pyClass.def("create", &GXIGRF_wrap_create,
                "create((float)arg1, (int)arg2, (str)arg3) -> GXIGRF:\n"

                "\n.. parsed-literal::\n\n"
                "   Create an IGRF.\n\n"

                ":param arg1: Date required\n"
                ":type arg1: float\n"
                ":param arg2: Year of the IGRF model to use\n"
                ":type arg2: int\n"
                ":param arg3: Name of the IGRF reference data file\n"
                ":type arg3: str\n"
                ":returns: IGRF Object\n"
                ":rtype: :class:`geosoft.gxapi.GXIGRF`\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					If the year of the IGRF model is dummy, then\n"
                "   					the IGRF year nearest to the line's date will\n"
                "   					be used. Otherwise, the specified year is used.\n"
                "   				\n\n"
               ).staticmethod("create");
    pyClass.def("date_range", &GXIGRF_wrap_date_range,
                "date_range((str)arg1, (float_ref)arg2, (float_ref)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Determine the range of years covered by an IGRF or DGRF file\n\n"

                ":param arg1: Model data file name\n"
                ":type arg1: str\n"
                ":param arg2: Minimum year  (rMAX if none found)\n"
                ":type arg2: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg3: Maximum year  (rMIN if none found)\n"
                ":type arg3: :class:`geosoft.gxapi.float_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.1.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					This is useful when using a DGRF file, because the system is set\n"
                "   					up only to calculate for years within the date range, and will\n"
                "   					return an error otherwise.\n"
                "   				\n\n"
               ).staticmethod("date_range");


}
