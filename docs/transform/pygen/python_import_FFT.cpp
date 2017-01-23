#include "stdafx.h"

using namespace boost::python;
using boost::python::init;


// Dummy classes


inline void GXFFT_wrap_app_dens(GXFFTPtr self, double arg1, double arg2)
{
    self->app_dens(arg1, arg2);
}
inline void GXFFT_wrap_app_susc(GXFFTPtr self, double arg1)
{
    self->app_susc(arg1);
}
inline void GXFFT_wrap_band_pass(GXFFTPtr self, double arg1, double arg2, int32_t arg3)
{
    self->band_pass(arg1, arg2, arg3);
}
inline void GXFFT_wrap_b_worth(GXFFTPtr self, double arg1, double arg2, int32_t arg3)
{
    self->b_worth(arg1, arg2, arg3);
}
inline void GXFFT_wrap_rc_filter(GXFFTPtr self, double arg1, int32_t arg2)
{
    self->rc_filter(arg1, arg2);
}
inline void GXFFT_wrap_contin(GXFFTPtr self, double arg1)
{
    self->contin(arg1);
}
inline void GXFFT_wrap_cos_roll(GXFFTPtr self, double arg1, double arg2, double arg3, int32_t arg4)
{
    self->cos_roll(arg1, arg2, arg3, arg4);
}
inline GXFFTPtr GXFFT_wrap_create(GXVVPtr arg1, double arg2, int32_t arg3)
{
    GXFFTPtr ret = GXFFT::create(arg1, arg2, (FFT_DETREND)arg3);
    return ret;
}
inline GXFFTPtr GXFFT_wrap_create_ex(GXVVPtr arg1, double arg2, int32_t arg3, double arg4)
{
    GXFFTPtr ret = GXFFT::create_ex(arg1, arg2, (FFT_DETREND)arg3, arg4);
    return ret;
}
inline GXFFTPtr GXFFT_wrap_create_ref(GXVVPtr arg1, double arg2, int32_t arg3)
{
    GXFFTPtr ret = GXFFT::create_ref(arg1, arg2, (FFT_DETREND)arg3);
    return ret;
}
inline GXFFTPtr GXFFT_wrap_create_ref_ex(GXVVPtr arg1, double arg2, int32_t arg3, double arg4, double arg5)
{
    GXFFTPtr ret = GXFFT::create_ref_ex(arg1, arg2, (FFT_DETREND)arg3, arg4, arg5);
    return ret;
}
inline void GXFFT_wrap_gaus(GXFFTPtr self, double arg1, int32_t arg2)
{
    self->gaus(arg1, arg2);
}
inline void GXFFT_wrap_get_vv(GXFFTPtr self, GXVVPtr arg1, GXVVPtr arg2)
{
    self->get_vv(arg1, arg2);
}
inline void GXFFT_wrap_h_drv(GXFFTPtr self, double arg1)
{
    self->h_drv(arg1);
}
inline void GXFFT_wrap_high_pass(GXFFTPtr self, double arg1, double arg2)
{
    self->high_pass(arg1, arg2);
}
inline void GXFFT_wrap_h_int(GXFFTPtr self)
{
    self->h_int();
}
inline void GXFFT_wrap_inverse(GXFFTPtr self, GXVVPtr arg1, GXVVPtr arg2)
{
    self->inverse(arg1, arg2);
}
inline void GXFFT_wrap_low_pass(GXFFTPtr self, double arg1)
{
    self->low_pass(arg1);
}
inline void GXFFT_wrap_red_pol(GXFFTPtr self, double arg1, double arg2, double arg3, double arg4)
{
    self->red_pol(arg1, arg2, arg3, arg4);
}
inline double GXFFT_wrap_nyquist(GXFFTPtr self)
{
    double ret = self->nyquist();
    return ret;
}
inline double GXFFT_wrap_samp_incr(GXFFTPtr self)
{
    double ret = self->samp_incr();
    return ret;
}
inline double GXFFT_wrap_wave_incr(GXFFTPtr self)
{
    double ret = self->wave_incr();
    return ret;
}
inline void GXFFT_wrap_set_vv(GXFFTPtr self, GXVVPtr arg1, GXVVPtr arg2)
{
    self->set_vv(arg1, arg2);
}
inline void GXFFT_wrap_spectrum(GXFFTPtr self, GXVVPtr arg1)
{
    self->spectrum(arg1);
}
inline void GXFFT_wrap_v_drv(GXFFTPtr self, double arg1)
{
    self->v_drv(arg1);
}
inline void GXFFT_wrap_v_int(GXFFTPtr self)
{
    self->v_int();
}
inline void GXFFT_wrap_write_spectrum(GXFFTPtr self, GXVVPtr arg1, const gx_string_type& arg2)
{
    self->write_spectrum(arg1, arg2);
}

void gxPythonImportGXFFT()
{

    class_<GXFFT, GXFFTPtr> pyClass("GXFFT",
                                    "\n.. parsed-literal::\n\n"
                                    "   This class allows for the application of predefined\n"
                                    "   filters to data in an OASIS database. The system uses\n"
                                    "   the Winograd algorithm to transform data in the spatial\n"
                                    "   domain to the wavenumber or Fourier domain.\n\n"
                                    , no_init);

    pyClass.def("null", &GXFFT::null, "null() -> GXFFT\n\nA null (undefined) instance of :class:`geosoft.gxapi.GXFFT`\n\n:returns: A null :class:`geosoft.gxapi.GXFFT`\n:rtype: :class:`geosoft.gxapi.GXFFT`\n").staticmethod("null");
    pyClass.def("is_null", &GXFFT::is_null, "is_null() -> bool\n\nCheck if the instance of :class:`geosoft.gxapi.GXFFT is null (undefined)`\n\n:returns: True if this is a null instance of :class:`geosoft.gxapi.GXFFT`, False otherwise.\n:rtype: bool`\n");
    pyClass.def("_internal_handle", &GXFFT::_internal_handle);
    pyClass.def("app_dens", &GXFFT_wrap_app_dens,
                "app_dens((float)arg1, (float)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Appparent density filter\n\n"

                ":param arg1: Thickness (meters) of the earth model\n"
                ":type arg1: float\n"
                ":param arg2: Background density (g/cm3) (default = 0)\n"
                ":type arg2: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("app_susc", &GXFFT_wrap_app_susc,
                "app_susc((float)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Apparent susceptiblity filter\n\n"

                ":param arg1: Total magnetic field strength\n"
                ":type arg1: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Reduction to magnetic pole (\\ :func:`geosoft.gxapi.GXFFT.red_pol`\\ ) and downward continuation\n"
                "   (\\ :func:`geosoft.gxapi.GXFFT.contin`\\ ) should be called BEFORE using \\ :func:`geosoft.gxapi.GXFFT.app_susc`\\ .\n\n"
               );
    pyClass.def("band_pass", &GXFFT_wrap_band_pass,
                "band_pass((float)arg1, (float)arg2, (int)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Bandpass filter (using low and high wavelength cutoffs)\n\n"

                ":param arg1: Low Cutoff wavelength (meters)\n"
                ":type arg1: float\n"
                ":param arg2: High Cutoff wavelength (meter)\n"
                ":type arg2: float\n"
                ":param arg3: 1= Pass the defined band (default); 0= Reject the band\n"
                ":type arg3: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("b_worth", &GXFFT_wrap_b_worth,
                "b_worth((float)arg1, (float)arg2, (int)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Butterworth filter\n\n"

                ":param arg1: Central cutoff wavelength (meter)\n"
                ":type arg1: float\n"
                ":param arg2: Degree of the filter function (default = 8.0)\n"
                ":type arg2: float\n"
                ":param arg3: Filter type: 1= Low-pass (regional) filter (default) 0= High-pass (residual) filter\n"
                ":type arg3: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("rc_filter", &GXFFT_wrap_rc_filter,
                "rc_filter((float)arg1, (int)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   RC filter\n\n"

                ":param arg1: Central cutoff wavelength (meter)\n"
                ":type arg1: float\n"
                ":param arg2: Filter type: 1= Low-pass (regional) filter (default) 0= High-pass (residual) filter\n"
                ":type arg2: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 8.5.0\n\n"
               );
    pyClass.def("contin", &GXFFT_wrap_contin,
                "contin((float)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Upward/Downward continuation filter\n\n"

                ":param arg1: Distance to continue; positive = downwards negative = upwards\n"
                ":type arg1: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("cos_roll", &GXFFT_wrap_cos_roll,
                "cos_roll((float)arg1, (float)arg2, (float)arg3, (int)arg4) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Cosine roll-off filter\n\n"

                ":param arg1: Low wavelength start point (meters)\n"
                ":type arg1: float\n"
                ":param arg2: High wavelength end point (meters)\n"
                ":type arg2: float\n"
                ":param arg3: Degree of the filter function (default = 2.0)\n"
                ":type arg3: float\n"
                ":param arg4: Filter type: 1= Low-pass (regional) filter (default) 0= High-pass (residual) filter\n"
                ":type arg4: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("create", &GXFFT_wrap_create,
                "create((GXVV)arg1, (float)arg2, (int)arg3) -> GXFFT:\n"

                "\n.. parsed-literal::\n\n"
                "   Create a New FFT with detrend options.\n\n"

                ":param arg1: VV to transform.\n"
                ":type arg1: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg2: Element space interval\n"
                ":type arg2: float\n"
                ":param arg3: \\ :ref:`FFT_DETREND`\\ \n"
                ":type arg3: int\n"
                ":returns: FFT Object\n"
                ":rtype: :class:`geosoft.gxapi.GXFFT`\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   The detrending options control the removal of a trend from the data\n"
                "   before the FFT is applied. The default data expansion is 10% before FFT.\n\n"
               ).staticmethod("create");
    pyClass.def("create_ex", &GXFFT_wrap_create_ex,
                "create_ex((GXVV)arg1, (float)arg2, (int)arg3, (float)arg4) -> GXFFT:\n"

                "\n.. parsed-literal::\n\n"
                "   Create a New FFT with detrend and expansion options.\n\n"

                ":param arg1: VV to transform.\n"
                ":type arg1: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg2: Element space interval\n"
                ":type arg2: float\n"
                ":param arg3: \\ :ref:`FFT_DETREND`\\ \n"
                ":type arg3: int\n"
                ":param arg4: minimum expansion %\n"
                ":type arg4: float\n"
                ":returns: FFT Object\n"
                ":rtype: :class:`geosoft.gxapi.GXFFT`\n"
                "\n"

                "\n.. versionadded:: 5.1.8\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   The detrending options control the removal of a trend from the data\n"
                "   before the FFT is applied. The expansion options control the minimum\n"
                "   data expansion before the FFT is applied.\n\n"
               ).staticmethod("create_ex");
    pyClass.def("create_ref", &GXFFT_wrap_create_ref,
                "create_ref((GXVV)arg1, (float)arg2, (int)arg3) -> GXFFT:\n"

                "\n.. parsed-literal::\n\n"
                "   Create FFT object with detrend options from reference (original) channel,\n"
                "   but no FFT process.\n\n"

                ":param arg1: VV contains channel data to perform FFT operations upon.\n"
                ":type arg1: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg2: Element space interval, should be the same as in Create(Ex)_FFT() call\n"
                ":type arg2: float\n"
                ":param arg3: \\ :ref:`FFT_DETREND`\\ \n"
                ":type arg3: int\n"
                ":returns: FFT Object\n"
                ":rtype: :class:`geosoft.gxapi.GXFFT`\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   This just creates an object.  It is intended to be called\n"
                "   immediately after with \\ :func:`geosoft.gxapi.GXFFT.set_vv`\\ .\n\n"
               ).staticmethod("create_ref");
    pyClass.def("create_ref_ex", &GXFFT_wrap_create_ref_ex,
                "create_ref_ex((GXVV)arg1, (float)arg2, (int)arg3, (float)arg4, (float)arg5) -> GXFFT:\n"

                "\n.. parsed-literal::\n\n"
                "   Create FFT object with detrend and expansion options from reference (original) channel,\n"
                "   but no FFT process.\n\n"

                ":param arg1: VV contains channel data to perform FFT operations upon.\n"
                ":type arg1: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg2: Element space interval, should be the same as in Create(Ex)_FFT() call\n"
                ":type arg2: float\n"
                ":param arg3: \\ :ref:`FFT_DETREND`\\ \n"
                ":type arg3: int\n"
                ":param arg4: minimum expansion %, should be the same as in CreateEx_FFT() call\n"
                ":type arg4: float\n"
                ":param arg5: DC level multiple\n"
                ":type arg5: float\n"
                ":returns: FFT Object\n"
                ":rtype: :class:`geosoft.gxapi.GXFFT`\n"
                "\n"

                "\n.. versionadded:: 5.1.8\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   This just creates an object.  It is intended to be called\n"
                "   immediately after with \\ :func:`geosoft.gxapi.GXFFT.set_vv`\\ .\n\n"
               ).staticmethod("create_ref_ex");
    pyClass.def("gaus", &GXFFT_wrap_gaus,
                "gaus((float)arg1, (int)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Gaussian filter\n\n"

                ":param arg1: Standard deviation cutoff of function (meters)\n"
                ":type arg1: float\n"
                ":param arg2: Filter type: 1= Low-pass (residual) filter (default) 0= High-pass (regional) filter\n"
                ":type arg2: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("get_vv", &GXFFT_wrap_get_vv,
                "get_vv((GXVV)arg1, (GXVV)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Copies real and imaginary VV's to user VV's.\n\n"

                ":param arg1: real component\n"
                ":type arg1: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg2: imaginary component\n"
                ":type arg2: :class:`geosoft.gxapi.GXVV`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("h_drv", &GXFFT_wrap_h_drv,
                "h_drv((float)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Horizontal derivative\n\n"

                ":param arg1: Order of differentiation (default = 1)\n"
                ":type arg1: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("high_pass", &GXFFT_wrap_high_pass,
                "high_pass((float)arg1, (float)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   High bandpass filter\n\n"

                ":param arg1: Cutoff wavelength (meter)\n"
                ":type arg1: float\n"
                ":param arg2: Fiducial increment of the FFT's channel data\n"
                ":type arg2: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("h_int", &GXFFT_wrap_h_int,
                "h_int() -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Horizontal integration\n\n"

                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.4\n\n"
               );
    pyClass.def("inverse", &GXFFT_wrap_inverse,
                "inverse((GXVV)arg1, (GXVV)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Inverse the FFT from wave number domain to space domain\n\n"

                ":param arg1: Output VV\n"
                ":type arg1: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg2: Original VV which was used to create FFT (will be used as mask for output VV; no masking if this parameter is NULL)\n"
                ":type arg2: :class:`geosoft.gxapi.GXVV`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("low_pass", &GXFFT_wrap_low_pass,
                "low_pass((float)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Low bandpass filter\n\n"

                ":param arg1: Cutoff wavelength (meters)\n"
                ":type arg1: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("red_pol", &GXFFT_wrap_red_pol,
                "red_pol((float)arg1, (float)arg2, (float)arg3, (float)arg4) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Reduction to magnetic pole\n\n"

                ":param arg1: Geomagnetic inclination (degrees)\n"
                ":type arg1: float\n"
                ":param arg2: Geomagnetic declination (degrees)\n"
                ":type arg2: float\n"
                ":param arg3: Inclination (degrees) for amplitude correction (default = 20.0)\n"
                ":type arg3: float\n"
                ":param arg4: Direction (degrees) of Line from North\n"
                ":type arg4: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("nyquist", &GXFFT_wrap_nyquist,
                "nyquist() -> float:\n"

                "\n.. parsed-literal::\n\n"
                "   Gets the Nyquist frequency (wavenumbers/sample unit).\n\n"

                ":returns: Nyquist frequency (wavenumbers/sample unit).\n"
                ":rtype: float\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("samp_incr", &GXFFT_wrap_samp_incr,
                "samp_incr() -> float:\n"

                "\n.. parsed-literal::\n\n"
                "   Gets the original sample increment.\n\n"

                ":returns: Original sample increment.\n"
                ":rtype: float\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("wave_incr", &GXFFT_wrap_wave_incr,
                "wave_incr() -> float:\n"

                "\n.. parsed-literal::\n\n"
                "   Get the wave number increment.\n\n"

                ":returns: Wave number increment\n"
                ":rtype: float\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("set_vv", &GXFFT_wrap_set_vv,
                "set_vv((GXVV)arg1, (GXVV)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Sets real and imaginary VVs in FFT.\n\n"

                ":param arg1: real component\n"
                ":type arg1: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg2: imaginary component\n"
                ":type arg2: :class:`geosoft.gxapi.GXVV`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   The VV must have been obtained from the same FFT\n"
                "   using the \\ :func:`geosoft.gxapi.GXFFT.set_vv`\\  method.\n\n"
               );
    pyClass.def("spectrum", &GXFFT_wrap_spectrum,
                "spectrum((GXVV)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Calculates a power spectrum\n\n"

                ":param arg1: Output power spectrum VV\n"
                ":type arg1: :class:`geosoft.gxapi.GXVV`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("v_drv", &GXFFT_wrap_v_drv,
                "v_drv((float)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Vertical derivative\n\n"

                ":param arg1: Order of differentiation (default = 1)\n"
                ":type arg1: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("v_int", &GXFFT_wrap_v_int,
                "v_int() -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Vertical integration\n\n"

                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("write_spectrum", &GXFFT_wrap_write_spectrum,
                "write_spectrum((GXVV)arg1, (str)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Writes a power spectrum to a file\n\n"

                ":param arg1: Output power spectrum VV\n"
                ":type arg1: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg2: File name for output spectrum\n"
                ":type arg2: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );

    scope().attr("FFT_DETREND_NONE") = (int32_t)0;
    scope().attr("FFT_DETREND_ENDS") = (int32_t)1;
    scope().attr("FFT_DETREND_ALL") = (int32_t)2;
    scope().attr("FFT_DETREND_MEAN") = (int32_t)3;

}
