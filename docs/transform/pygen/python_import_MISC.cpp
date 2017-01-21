#include "stdafx.h"

using namespace boost::python;
using boost::python::init;


// Dummy classes


inline void GXMISC_wrap_convert_cg3to_raw(const gx_string_type& arg1, const gx_string_type& arg2, int32_t arg3)
{
    GXMISC::convert_cg3to_raw(arg1, arg2, arg3);
}
inline void GXMISC_wrap_convert_cg5to_raw(const gx_string_type& arg1, const gx_string_type& arg2, int32_t arg3)
{
    GXMISC::convert_cg5to_raw(arg1, arg2, arg3);
}
inline void GXMISC_wrap_ukoa2_tbl(const gx_string_type& arg1, const gx_string_type& arg2, const gx_string_type& arg3)
{
    GXMISC::ukoa2_tbl(arg1, arg2, arg3);
}

void gxPythonImportGXMISC()
{

    class_<GXMISC, boost::noncopyable> pyClass("GXMISC",
            "\n.. parsed-literal::\n\n"
            "   Not a class. A catch-all for miscellaneous geophysical\n"
            "   methods, primarily file conversions.\n\n"
            , no_init);


    pyClass.def("convert_cg3to_raw", &GXMISC_wrap_convert_cg3to_raw,
                "convert_cg3to_raw((str)arg1, (str)arg2, (int)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Convert a CG3 dump to RAW format.\n\n"

                ":param arg1: name of the CG3 file\n"
                ":type arg1: str\n"
                ":param arg2: name of the RAW file\n"
                ":type arg2: str\n"
                ":param arg3: TideCorr Option: 1 - use geosoft, 0 - use CG3/CG5\n"
                ":type arg3: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 7.3.0\n\n"
               ).staticmethod("convert_cg3to_raw");
    pyClass.def("convert_cg5to_raw", &GXMISC_wrap_convert_cg5to_raw,
                "convert_cg5to_raw((str)arg1, (str)arg2, (int)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Convert a CG5 dump to RAW format.\n\n"

                ":param arg1: name of the CG5 file\n"
                ":type arg1: str\n"
                ":param arg2: name of the RAW file\n"
                ":type arg2: str\n"
                ":param arg3: TideCorr Option: 1 - use geosoft, 0 - use CG3/CG5\n"
                ":type arg3: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 7.3.0\n\n"
               ).staticmethod("convert_cg5to_raw");
    pyClass.def("ukoa2_tbl", &GXMISC_wrap_ukoa2_tbl,
                "ukoa2_tbl((str)arg1, (str)arg2, (str)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Convert a UKOA file to a location TBL file.\n\n"

                ":param arg1: name of the UKOA file\n"
                ":type arg1: str\n"
                ":param arg2: line name alias table\n"
                ":type arg2: str\n"
                ":param arg3: name of the output table\n"
                ":type arg3: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   The TBL file will contain the following fields:\n"
                "   \n"
                "   = Line:string16\n"
                "   = Station:long\n"
                "   = Latitude:double\n"
                "   = Longitude:double\n"
                "   = X:double\n"
                "   = Y:double\n"
                "   = Elevation:double\n\n"
               ).staticmethod("ukoa2_tbl");


}
