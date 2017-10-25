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



    def app_dens(self, p2, p3):
        """
        Appparent density filter
        """
        self._wrapper.app_dens(p2, p3)
        




    def app_susc(self, p2):
        """
        Apparent susceptiblity filter

        **Note:**

        Reduction to magnetic pole (`red_pol`) and downward continuation
        (`contin`) should be called BEFORE using `app_susc`.
        """
        self._wrapper.app_susc(p2)
        




    def band_pass(self, p2, p3, p4):
        """
        Bandpass filter (using low and high wavelength cutoffs)
        """
        self._wrapper.band_pass(p2, p3, p4)
        




    def b_worth(self, p2, p3, p4):
        """
        Butterworth filter
        """
        self._wrapper.b_worth(p2, p3, p4)
        




    def rc_filter(self, p2, p3):
        """
        RC filter
        """
        self._wrapper.rc_filter(p2, p3)
        




    def contin(self, p2):
        """
        Upward/Downward continuation filter
        """
        self._wrapper.contin(p2)
        




    def cos_roll(self, p2, p3, p4, p5):
        """
        Cosine roll-off filter
        """
        self._wrapper.cos_roll(p2, p3, p4, p5)
        



    @classmethod
    def create(cls, p1, p2, p3):
        """
        Create a New `GXFFT` with detrend options.

        **Note:**

        The detrending options control the removal of a trend from the data
        before the `GXFFT` is applied. The default data expansion is 10% before `GXFFT`.
        """
        ret_val = gxapi_cy.WrapFFT.create(GXContext._get_tls_geo(), p1._wrapper, p2, p3)
        return GXFFT(ret_val)



    @classmethod
    def create_ex(cls, p1, p2, p3, p4):
        """
        Create a New `GXFFT` with detrend and expansion options.

        **Note:**

        The detrending options control the removal of a trend from the data
        before the `GXFFT` is applied. The expansion options control the minimum
        data expansion before the `GXFFT` is applied.
        """
        ret_val = gxapi_cy.WrapFFT.create_ex(GXContext._get_tls_geo(), p1._wrapper, p2, p3, p4)
        return GXFFT(ret_val)



    @classmethod
    def create_ref(cls, p1, p2, p3):
        """
        Create `GXFFT` object with detrend options from reference (original) channel,
        but no `GXFFT` process.

        **Note:**

        This just creates an object.  It is intended to be called
        immediately after with `set_vv`.
        """
        ret_val = gxapi_cy.WrapFFT.create_ref(GXContext._get_tls_geo(), p1._wrapper, p2, p3)
        return GXFFT(ret_val)



    @classmethod
    def create_ref_ex(cls, p1, p2, p3, p4, p5):
        """
        Create `GXFFT` object with detrend and expansion options from reference (original) channel,
        but no `GXFFT` process.

        **Note:**

        This just creates an object.  It is intended to be called
        immediately after with `set_vv`.
        """
        ret_val = gxapi_cy.WrapFFT.create_ref_ex(GXContext._get_tls_geo(), p1._wrapper, p2, p3, p4, p5)
        return GXFFT(ret_val)






    def gaus(self, p2, p3):
        """
        Gaussian filter
        """
        self._wrapper.gaus(p2, p3)
        




    def get_vv(self, p2, p3):
        """
        Copies real and imaginary `GXVV`'s to user `GXVV`'s.
        """
        self._wrapper.get_vv(p2._wrapper, p3._wrapper)
        




    def h_drv(self, p2):
        """
        Horizontal derivative
        """
        self._wrapper.h_drv(p2)
        




    def high_pass(self, p2, p3):
        """
        High bandpass filter
        """
        self._wrapper.high_pass(p2, p3)
        




    def h_int(self):
        """
        Horizontal integration
        """
        self._wrapper.h_int()
        




    def inverse(self, p2, p3):
        """
        Inverse the `GXFFT` from wave number domain to space domain
        """
        self._wrapper.inverse(p2._wrapper, p3._wrapper)
        




    def low_pass(self, p2):
        """
        Low bandpass filter
        """
        self._wrapper.low_pass(p2)
        




    def red_pol(self, p2, p3, p4, p5):
        """
        Reduction to magnetic pole
        """
        self._wrapper.red_pol(p2, p3, p4, p5)
        




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




    def set_vv(self, p2, p3):
        """
        Sets real and imaginary VVs in `GXFFT`.

        **Note:**

        The `GXVV` must have been obtained from the same `GXFFT`
        using the `set_vv` method.
        """
        self._wrapper.set_vv(p2._wrapper, p3._wrapper)
        




    def spectrum(self, p2):
        """
        Calculates a power spectrum
        """
        self._wrapper.spectrum(p2._wrapper)
        




    def v_drv(self, p2):
        """
        Vertical derivative
        """
        self._wrapper.v_drv(p2)
        




    def v_int(self):
        """
        Vertical integration
        """
        self._wrapper.v_int()
        




    def write_spectrum(self, p2, p3):
        """
        Writes a power spectrum to a file
        """
        self._wrapper.write_spectrum(p2._wrapper, p3.encode())
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer