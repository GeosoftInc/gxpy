#include "stdafx.h"

using namespace boost::python;
using boost::python::init;


// Dummy classes


inline void GXFFT2_wrap_fft2_in(GXIMGPtr arg1, const gx_string_type& arg2, const gx_string_type& arg3)
{
    GXFFT2::fft2_in(arg1, arg2, arg3);
}
inline void GXFFT2_wrap_filter_pg(GXPGPtr arg1, const gx_string_type& arg2, GXTRPtr arg3, double arg4, double arg5, double arg6)
{
    GXFFT2::filter_pg(arg1, arg2, arg3, arg4, arg5, arg6);
}
inline void GXFFT2_wrap_flt(GXIMGPtr arg1, const gx_string_type& arg2, const gx_string_type& arg3)
{
    GXFFT2::flt(arg1, arg2, arg3);
}
inline void GXFFT2_wrap_flt_inv(GXIMGPtr arg1, const gx_string_type& arg2, const gx_string_type& arg3)
{
    GXFFT2::flt_inv(arg1, arg2, arg3);
}
inline void GXFFT2_wrap_pow_spc(GXIMGPtr arg1, const gx_string_type& arg2)
{
    GXFFT2::pow_spc(arg1, arg2);
}
inline void GXFFT2_wrap_rad_spc(GXIMGPtr arg1, const gx_string_type& arg2)
{
    GXFFT2::rad_spc(arg1, arg2);
}
inline void GXFFT2_wrap_rad_spc1(GXIMGPtr arg1, GXVVPtr arg2)
{
    GXFFT2::rad_spc1(arg1, arg2);
}
inline void GXFFT2_wrap_rad_spc2(GXIMGPtr arg1, GXIMGPtr arg2, GXVVPtr arg3, GXVVPtr arg4, int32_t arg5)
{
    GXFFT2::rad_spc2(arg1, arg2, arg3, arg4, arg5);
}
inline void GXFFT2_wrap_td_xd_y(GXIMGPtr arg1, GXIMGPtr arg2, const gx_string_type& arg3, int32_t arg4)
{
    GXFFT2::td_xd_y(arg1, arg2, arg3, arg4);
}
inline void GXFFT2_wrap_trans_pg(GXPGPtr arg1, int32_t arg2)
{
    GXFFT2::trans_pg(arg1, (FFT2_PG)arg2);
}

void gxPythonImportGXFFT2()
{

    class_<GXFFT2, boost::noncopyable> pyClass("GXFFT2",
            "\n.. parsed-literal::\n\n"
            "   2-D Fast Fourier Transforms\n"
            "   These methods now work with an IMG object, instead of creating\n"
            "   their own FFT2 object.\n\n"
            , no_init);


    pyClass.def("fft2_in", &GXFFT2_wrap_fft2_in,
                "fft2_in((GXIMG)arg1, (str)arg2, (str)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   FFT2 transform\n\n"

                ":param arg1: Input image\n"
                ":type arg1: :class:`geosoft.gxapi.GXIMG`\n"
                ":param arg2: Output Transform file name string\n"
                ":type arg2: str\n"
                ":param arg3: Output Power Spectrum file name string\n"
                ":type arg3: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("fft2_in");
    pyClass.def("filter_pg", &GXFFT2_wrap_filter_pg,
                "filter_pg((GXPG)arg1, (str)arg2, (GXTR)arg3, (float)arg4, (float)arg5, (float)arg6) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Apply 2D FFT filters to data in pager\n\n"

                ":param arg1: pager obj\n"
                ":type arg1: :class:`geosoft.gxapi.GXPG`\n"
                ":param arg2: sConFil - FFT filter control file\n"
                ":type arg2: str\n"
                ":param arg3: TR obj\n"
                ":type arg3: :class:`geosoft.gxapi.GXTR`\n"
                ":param arg4: rDx - X increment\n"
                ":type arg4: float\n"
                ":param arg5: rDy - Y increment\n"
                ":type arg5: float\n"
                ":param arg6: rRot- Rotation degree\n"
                ":type arg6: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("filter_pg");
    pyClass.def("flt", &GXFFT2_wrap_flt,
                "flt((GXIMG)arg1, (str)arg2, (str)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   FFT2 filter\n\n"

                ":param arg1: Input image (Transform grid)\n"
                ":type arg1: :class:`geosoft.gxapi.GXIMG`\n"
                ":param arg2: Output file (Transform grid)\n"
                ":type arg2: str\n"
                ":param arg3: Control file\n"
                ":type arg3: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("flt");
    pyClass.def("flt_inv", &GXFFT2_wrap_flt_inv,
                "flt_inv((GXIMG)arg1, (str)arg2, (str)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   FFT2 filter and inverse\n\n"

                ":param arg1: Input image (Transform grid)\n"
                ":type arg1: :class:`geosoft.gxapi.GXIMG`\n"
                ":param arg2: Output file\n"
                ":type arg2: str\n"
                ":param arg3: Control file\n"
                ":type arg3: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("flt_inv");
    pyClass.def("pow_spc", &GXFFT2_wrap_pow_spc,
                "pow_spc((GXIMG)arg1, (str)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   FFT2 transform power spectrum\n\n"

                ":param arg1: Input image (Transform grid)\n"
                ":type arg1: :class:`geosoft.gxapi.GXIMG`\n"
                ":param arg2: Output Power Spectrum file name string\n"
                ":type arg2: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("pow_spc");
    pyClass.def("rad_spc", &GXFFT2_wrap_rad_spc,
                "rad_spc((GXIMG)arg1, (str)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   FFT2 transform Radially averaged power spectrum\n\n"

                ":param arg1: Input image (Transform grid)\n"
                ":type arg1: :class:`geosoft.gxapi.GXIMG`\n"
                ":param arg2: Output Radial Spectrum file name string\n"
                ":type arg2: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("rad_spc");
    pyClass.def("rad_spc1", &GXFFT2_wrap_rad_spc1,
                "rad_spc1((GXIMG)arg1, (GXVV)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   FFT2 transform Radially averaged power spectrum for one IMG\n\n"

                ":param arg1: Input image (Transform grid)\n"
                ":type arg1: :class:`geosoft.gxapi.GXIMG`\n"
                ":param arg2: Output Radial Spectrum VV\n"
                ":type arg2: :class:`geosoft.gxapi.GXVV`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 7.2.0\n\n"
               ).staticmethod("rad_spc1");
    pyClass.def("rad_spc2", &GXFFT2_wrap_rad_spc2,
                "rad_spc2((GXIMG)arg1, (GXIMG)arg2, (GXVV)arg3, (GXVV)arg4, (int)arg5) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   FFT2 transform Radially averaged power spectrum for two IMGs\n\n"

                ":param arg1: Input image1 (Transform grid1 - G)\n"
                ":type arg1: :class:`geosoft.gxapi.GXIMG`\n"
                ":param arg2: Input image2 (Transform grid2 - H)\n"
                ":type arg2: :class:`geosoft.gxapi.GXIMG`\n"
                ":param arg3: Output Radial Spectrum VV\n"
                ":type arg3: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg4: Output Radial Spectrum Standard deviation VVst	(Null: no calc)\n"
                ":type arg4: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg5: lOpt - 1: <Re(GH\\ `*`\\ /HH\\ `*`\\ )> VV;  0: <Re(GH\\ `*`\\ )> VV\n"
                ":type arg5: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 7.2.0\n\n"
               ).staticmethod("rad_spc2");
    pyClass.def("td_xd_y", &GXFFT2_wrap_td_xd_y,
                "td_xd_y((GXIMG)arg1, (GXIMG)arg2, (str)arg3, (int)arg4) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   FFT2 filter (calculate T from the derivatives Tx and Ty)\n\n"

                ":param arg1: Input dX image (Transform grid)\n"
                ":type arg1: :class:`geosoft.gxapi.GXIMG`\n"
                ":param arg2: Input dY image (Transform grid)\n"
                ":type arg2: :class:`geosoft.gxapi.GXIMG`\n"
                ":param arg3: Output T file name\n"
                ":type arg3: str\n"
                ":param arg4: 0 - no invers, 1 - invers FFT applied\n"
                ":type arg4: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.1\n\n"
               ).staticmethod("td_xd_y");
    pyClass.def("trans_pg", &GXFFT2_wrap_trans_pg,
                "trans_pg((GXPG)arg1, (int)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Apply 2D FFT transform to data in pager\n\n"

                ":param arg1: pager obj\n"
                ":type arg1: :class:`geosoft.gxapi.GXPG`\n"
                ":param arg2: \\ :ref:`FFT2_PG`\\ \n"
                ":type arg2: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("trans_pg");

    scope().attr("FFT2_PG_FORWARD") = (int32_t)0;
    scope().attr("FFT2_PG_INVERSE") = (int32_t)1;

}
