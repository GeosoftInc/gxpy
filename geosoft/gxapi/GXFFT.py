### extends 'class_empty.py'
### block ClassImports
# NOTICE: Do not edit anything here, it is generated code
from typing import NewType
from . import gxapi_cy
from geosoft.gxapi import GXContext, float_ref, int_ref, str_ref


### endblock ClassImports

### block Header
# NOTICE: The code generator will not replace the code in this block
### endblock Header

### block ClassImplementation
# NOTICE: Do not edit anything here, it is generated code
class GXFFT:
    """
    GXFFT class.

    This class allows for the application of predefined
    filters to data in an OASIS database. The system uses
    the Winograd algorithm to transform data in the spatial
    domain to the wavenumber or Fourier domain.
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._wrapper = None

    def __del__(self):
        self._wrapper = None

    def __init__(self, wrapper=None):
        self._wrapper = wrapper if wrapper else gxapi_cy.WrapFFT(GXContext._get_tls_geo(), 0)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of `GXFFT`
        
        :returns: A null `GXFFT`
        """
        return cls()

    def is_null(self):
        """
        Check if the instance of `GXFFT` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of `GXFFT`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Miscellaneous



    def app_dens(self, thick, dens):
        """
        Appparent density filter
        """
        self._wrapper.app_dens(thick, dens)
        




    def app_susc(self, strength):
        """
        Apparent susceptiblity filter

        **Note:**

        Reduction to magnetic pole (`red_pol`) and downward continuation
        (`contin`) should be called BEFORE using `app_susc`.
        """
        self._wrapper.app_susc(strength)
        




    def band_pass(self, llen, hlen, pass_defined):
        """
        Bandpass filter (using low and high wavelength cutoffs)
        """
        self._wrapper.band_pass(llen, hlen, pass_defined)
        




    def b_worth(self, clen, degree, filter_type):
        """
        Butterworth filter
        """
        self._wrapper.b_worth(clen, degree, filter_type)
        




    def rc_filter(self, clen, filter_type):
        """
        RC filter
        """
        self._wrapper.rc_filter(clen, filter_type)
        




    def contin(self, dist):
        """
        Upward/Downward continuation filter
        """
        self._wrapper.contin(dist)
        




    def cos_roll(self, llen, hlen, degree, type):
        """
        Cosine roll-off filter
        """
        self._wrapper.cos_roll(llen, hlen, degree, type)
        



    @classmethod
    def create(cls, gvv, interv, trend):
        """
        Create a New `GXFFT` with detrend options.

        **Note:**

        The detrending options control the removal of a trend from the data
        before the `GXFFT` is applied. The default data expansion is 10% before `GXFFT`.
        """
        ret_val = gxapi_cy.WrapFFT.create(GXContext._get_tls_geo(), gvv._wrapper, interv, trend)
        return GXFFT(ret_val)



    @classmethod
    def create_ex(cls, gvv, interv, trend, expansion):
        """
        Create a New `GXFFT` with detrend and expansion options.

        **Note:**

        The detrending options control the removal of a trend from the data
        before the `GXFFT` is applied. The expansion options control the minimum
        data expansion before the `GXFFT` is applied.
        """
        ret_val = gxapi_cy.WrapFFT.create_ex(GXContext._get_tls_geo(), gvv._wrapper, interv, trend, expansion)
        return GXFFT(ret_val)



    @classmethod
    def create_ref(cls, gvv, interv, trend):
        """
        Create `GXFFT` object with detrend options from reference (original) channel,
        but no `GXFFT` process.

        **Note:**

        This just creates an object.  It is intended to be called
        immediately after with `set_vv`.
        """
        ret_val = gxapi_cy.WrapFFT.create_ref(GXContext._get_tls_geo(), gvv._wrapper, interv, trend)
        return GXFFT(ret_val)



    @classmethod
    def create_ref_ex(cls, gvv, interv, trend, expansion, d_cmult):
        """
        Create `GXFFT` object with detrend and expansion options from reference (original) channel,
        but no `GXFFT` process.

        **Note:**

        This just creates an object.  It is intended to be called
        immediately after with `set_vv`.
        """
        ret_val = gxapi_cy.WrapFFT.create_ref_ex(GXContext._get_tls_geo(), gvv._wrapper, interv, trend, expansion, d_cmult)
        return GXFFT(ret_val)






    def gaus(self, dev, type):
        """
        Gaussian filter
        """
        self._wrapper.gaus(dev, type)
        




    def get_vv(self, gv_vr, gv_vi):
        """
        Copies real and imaginary `GXVV`'s to user `GXVV`'s.
        """
        self._wrapper.get_vv(gv_vr._wrapper, gv_vi._wrapper)
        




    def h_drv(self, order):
        """
        Horizontal derivative
        """
        self._wrapper.h_drv(order)
        




    def high_pass(self, wlen, fid_int):
        """
        High bandpass filter
        """
        self._wrapper.high_pass(wlen, fid_int)
        




    def h_int(self):
        """
        Horizontal integration
        """
        self._wrapper.h_int()
        




    def inverse(self, gvv, gv_vm):
        """
        Inverse the `GXFFT` from wave number domain to space domain
        """
        self._wrapper.inverse(gvv._wrapper, gv_vm._wrapper)
        




    def low_pass(self, wlen):
        """
        Low bandpass filter
        """
        self._wrapper.low_pass(wlen)
        




    def red_pol(self, inc, dec, incp, dir):
        """
        Reduction to magnetic pole
        """
        self._wrapper.red_pol(inc, dec, incp, dir)
        




    def nyquist(self):
        """
        Gets the Nyquist frequency (wavenumbers/sample unit).
        """
        ret_val = self._wrapper.nyquist()
        return ret_val




    def samp_incr(self):
        """
        Gets the original sample increment.
        """
        ret_val = self._wrapper.samp_incr()
        return ret_val




    def wave_incr(self):
        """
        Get the wave number increment.
        """
        ret_val = self._wrapper.wave_incr()
        return ret_val




    def set_vv(self, gv_vr, gv_vi):
        """
        Sets real and imaginary VVs in `GXFFT`.

        **Note:**

        The `GXVV` must have been obtained from the same `GXFFT`
        using the `set_vv` method.
        """
        self._wrapper.set_vv(gv_vr._wrapper, gv_vi._wrapper)
        




    def spectrum(self, gvv):
        """
        Calculates a power spectrum
        """
        self._wrapper.spectrum(gvv._wrapper)
        




    def v_drv(self, order):
        """
        Vertical derivative
        """
        self._wrapper.v_drv(order)
        




    def v_int(self):
        """
        Vertical integration
        """
        self._wrapper.v_int()
        




    def write_spectrum(self, gvv, out_file):
        """
        Writes a power spectrum to a file
        """
        self._wrapper.write_spectrum(gvv._wrapper, out_file.encode())
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer