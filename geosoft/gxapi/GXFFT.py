### extends 'class_empty.py'
### block ClassImports
# NOTICE: Do not edit anything here, it is generated code
from . import gxapi_cy
from geosoft.gxapi import GXContext, float_ref, int_ref, str_ref


### endblock ClassImports

### block Header
# NOTICE: The code generator will not replace the code in this block
### endblock Header

### block ClassImplementation
# NOTICE: Do not edit anything here, it is generated code
class GXFFT(gxapi_cy.WrapFFT):
    """
    GXFFT class.

    This class allows for the application of predefined
    filters to data in an OASIS database. The system uses
    the Winograd algorithm to transform data in the spatial
    domain to the wavenumber or Fourier domain.
    """

    def __init__(self, handle=0):
        super(GXFFT, self).__init__(GXContext._get_tls_geo(), handle)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of `GXFFT <geosoft.gxapi.GXFFT>`
        
        :returns: A null `GXFFT <geosoft.gxapi.GXFFT>`
        :rtype:   GXFFT
        """
        return GXFFT()

    def is_null(self):
        """
        Check if this is a null (undefined) instance
        
        :returns: True if this is a null (undefined) instance, False otherwise.
        :rtype:   bool
        """
        return self._internal_handle() == 0



# Miscellaneous



    def app_dens(self, thick, dens):
        """
        Appparent density filter
        
        :param thick:  Thickness (meters) of the earth model
        :param dens:   Background density (g/cm3) (default = 0)
        :type  thick:  float
        :type  dens:   float

        .. versionadded:: 5.0

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_
        """
        self._app_dens(thick, dens)
        




    def app_susc(self, strength):
        """
        Apparent susceptiblity filter
        
        :param strength:  Total magnetic field strength
        :type  strength:  float

        .. versionadded:: 5.0

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_

        **Note:** Reduction to magnetic pole (`red_pol <geosoft.gxapi.GXFFT.red_pol>`) and downward continuation
        (`contin <geosoft.gxapi.GXFFT.contin>`) should be called BEFORE using `app_susc <geosoft.gxapi.GXFFT.app_susc>`.
        """
        self._app_susc(strength)
        




    def band_pass(self, llen, hlen, pass_defined):
        """
        Bandpass filter (using low and high wavelength cutoffs)
        
        :param llen:          Low Cutoff wavelength (meters)
        :param hlen:          High Cutoff wavelength (meter)
        :param pass_defined:  1= Pass the defined band (default); 0= Reject the band
        :type  llen:          float
        :type  hlen:          float
        :type  pass_defined:  int

        .. versionadded:: 5.0

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_
        """
        self._band_pass(llen, hlen, pass_defined)
        




    def b_worth(self, clen, degree, filter_type):
        """
        Butterworth filter
        
        :param clen:         Central cutoff wavelength (meter)
        :param degree:       Degree of the filter function (default = 8.0)
        :param filter_type:  Filter type: 1= Low-pass (regional) filter (default) 0= High-pass (residual) filter
        :type  clen:         float
        :type  degree:       float
        :type  filter_type:  int

        .. versionadded:: 5.0

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_
        """
        self._b_worth(clen, degree, filter_type)
        




    def rc_filter(self, clen, filter_type):
        """
        RC filter
        
        :param clen:         Central cutoff wavelength (meter)
        :param filter_type:  Filter type: 1= Low-pass (regional) filter (default) 0= High-pass (residual) filter
        :type  clen:         float
        :type  filter_type:  int

        .. versionadded:: 8.5

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_
        """
        self._rc_filter(clen, filter_type)
        




    def contin(self, dist):
        """
        Upward/Downward continuation filter
        
        :param dist:  Distance to continue; positive = downwards negative = upwards
        :type  dist:  float

        .. versionadded:: 5.0

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_
        """
        self._contin(dist)
        




    def cos_roll(self, llen, hlen, degree, type):
        """
        Cosine roll-off filter
        
        :param llen:    Low wavelength start point (meters)
        :param hlen:    High wavelength end point (meters)
        :param degree:  Degree of the filter function (default = 2.0)
        :param type:    Filter type: 1= Low-pass (regional) filter (default) 0= High-pass (residual) filter
        :type  llen:    float
        :type  hlen:    float
        :type  degree:  float
        :type  type:    int

        .. versionadded:: 5.0

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_
        """
        self._cos_roll(llen, hlen, degree, type)
        



    @classmethod
    def create(cls, gvv, interv, trend):
        """
        Create a New `GXFFT <geosoft.gxapi.GXFFT>` with detrend options.
        
        :param gvv:     `GXVV <geosoft.gxapi.GXVV>` to transform.
        :param interv:  Element space interval
        :param trend:   :ref:`FFT_DETREND`
        :type  gvv:     GXVV
        :type  interv:  float
        :type  trend:   int

        :returns:       `GXFFT <geosoft.gxapi.GXFFT>` Object
        :rtype:         GXFFT

        .. versionadded:: 5.0

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_

        **Note:** The detrending options control the removal of a trend from the data
        before the `GXFFT <geosoft.gxapi.GXFFT>` is applied. The default data expansion is 10% before `GXFFT <geosoft.gxapi.GXFFT>`.
        """
        ret_val = gxapi_cy.WrapFFT._create(GXContext._get_tls_geo(), gvv, interv, trend)
        return GXFFT(ret_val)



    @classmethod
    def create_ex(cls, gvv, interv, trend, expansion):
        """
        Create a New `GXFFT <geosoft.gxapi.GXFFT>` with detrend and expansion options.
        
        :param gvv:        `GXVV <geosoft.gxapi.GXVV>` to transform.
        :param interv:     Element space interval
        :param trend:      :ref:`FFT_DETREND`
        :param expansion:  Minimum expansion %
        :type  gvv:        GXVV
        :type  interv:     float
        :type  trend:      int
        :type  expansion:  float

        :returns:          `GXFFT <geosoft.gxapi.GXFFT>` Object
        :rtype:            GXFFT

        .. versionadded:: 5.1.8

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_

        **Note:** The detrending options control the removal of a trend from the data
        before the `GXFFT <geosoft.gxapi.GXFFT>` is applied. The expansion options control the minimum
        data expansion before the `GXFFT <geosoft.gxapi.GXFFT>` is applied.
        """
        ret_val = gxapi_cy.WrapFFT._create_ex(GXContext._get_tls_geo(), gvv, interv, trend, expansion)
        return GXFFT(ret_val)



    @classmethod
    def create_ref(cls, gvv, interv, trend):
        """
        Create `GXFFT <geosoft.gxapi.GXFFT>` object with detrend options from reference (original) channel,
        but no `GXFFT <geosoft.gxapi.GXFFT>` process.
        
        :param gvv:     `GXVV <geosoft.gxapi.GXVV>` contains channel data to perform `GXFFT <geosoft.gxapi.GXFFT>` operations upon.
        :param interv:  Element space interval, should be the same as in `create_ex <geosoft.gxapi.GXFFT.create_ex>` call
        :param trend:   :ref:`FFT_DETREND`
        :type  gvv:     GXVV
        :type  interv:  float
        :type  trend:   int

        :returns:       `GXFFT <geosoft.gxapi.GXFFT>` Object
        :rtype:         GXFFT

        .. versionadded:: 5.0

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_

        **Note:** This just creates an object.  It is intended to be called
        immediately after with `set_vv <geosoft.gxapi.GXFFT.set_vv>`.
        """
        ret_val = gxapi_cy.WrapFFT._create_ref(GXContext._get_tls_geo(), gvv, interv, trend)
        return GXFFT(ret_val)



    @classmethod
    def create_ref_ex(cls, gvv, interv, trend, expansion, d_cmult):
        """
        Create `GXFFT <geosoft.gxapi.GXFFT>` object with detrend and expansion options from reference (original) channel,
        but no `GXFFT <geosoft.gxapi.GXFFT>` process.
        
        :param gvv:        `GXVV <geosoft.gxapi.GXVV>` contains channel data to perform `GXFFT <geosoft.gxapi.GXFFT>` operations upon.
        :param interv:     Element space interval, should be the same as in `create_ex <geosoft.gxapi.GXFFT.create_ex>` call
        :param trend:      :ref:`FFT_DETREND`
        :param expansion:  Minimum expansion %, should be the same as in `create_ex <geosoft.gxapi.GXFFT.create_ex>` call
        :param d_cmult:    DC level multiple
        :type  gvv:        GXVV
        :type  interv:     float
        :type  trend:      int
        :type  expansion:  float
        :type  d_cmult:    float

        :returns:          `GXFFT <geosoft.gxapi.GXFFT>` Object
        :rtype:            GXFFT

        .. versionadded:: 5.1.8

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_

        **Note:** This just creates an object.  It is intended to be called
        immediately after with `set_vv <geosoft.gxapi.GXFFT.set_vv>`.
        """
        ret_val = gxapi_cy.WrapFFT._create_ref_ex(GXContext._get_tls_geo(), gvv, interv, trend, expansion, d_cmult)
        return GXFFT(ret_val)






    def gaus(self, dev, type):
        """
        Gaussian filter
        
        :param dev:   Standard deviation cutoff of function (meters)
        :param type:  Filter type: 1= Low-pass (residual) filter (default) 0= High-pass (regional) filter
        :type  dev:   float
        :type  type:  int

        .. versionadded:: 5.0

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_
        """
        self._gaus(dev, type)
        




    def get_vv(self, gv_vr, gv_vi):
        """
        Copies real and imaginary `GXVV <geosoft.gxapi.GXVV>`'s to user `GXVV <geosoft.gxapi.GXVV>`'s.
        
        :param gv_vr:  Real component
        :param gv_vi:  Imaginary component
        :type  gv_vr:  GXVV
        :type  gv_vi:  GXVV

        .. versionadded:: 5.0

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_
        """
        self._get_vv(gv_vr, gv_vi)
        




    def h_drv(self, order):
        """
        Horizontal derivative
        
        :param order:  Order of differentiation (default = 1)
        :type  order:  float

        .. versionadded:: 5.0

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_
        """
        self._h_drv(order)
        




    def high_pass(self, wlen, fid_int):
        """
        High bandpass filter
        
        :param wlen:     Cutoff wavelength (meter)
        :param fid_int:  Fiducial increment of the `GXFFT <geosoft.gxapi.GXFFT>`'s channel data
        :type  wlen:     float
        :type  fid_int:  float

        .. versionadded:: 5.0

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_
        """
        self._high_pass(wlen, fid_int)
        




    def h_int(self):
        """
        Horizontal integration
        

        .. versionadded:: 5.1.4

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_
        """
        self._h_int()
        




    def inverse(self, gvv, gv_vm):
        """
        Inverse the `GXFFT <geosoft.gxapi.GXFFT>` from wave number domain to space domain
        
        :param gvv:    Output `GXVV <geosoft.gxapi.GXVV>`
        :param gv_vm:  Original `GXVV <geosoft.gxapi.GXVV>` which was used to create `GXFFT <geosoft.gxapi.GXFFT>` (will be used as mask for output `GXVV <geosoft.gxapi.GXVV>`; no masking if this parameter is NULL)
        :type  gvv:    GXVV
        :type  gv_vm:  GXVV

        .. versionadded:: 5.0

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_
        """
        self._inverse(gvv, gv_vm)
        




    def low_pass(self, wlen):
        """
        Low bandpass filter
        
        :param wlen:  Cutoff wavelength (meters)
        :type  wlen:  float

        .. versionadded:: 5.0

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_
        """
        self._low_pass(wlen)
        




    def red_pol(self, inc, dec, incp, dir):
        """
        Reduction to magnetic pole
        
        :param inc:   Geomagnetic inclination (degrees)
        :param dec:   Geomagnetic declination (degrees)
        :param incp:  Inclination (degrees) for amplitude correction (default = 20.0)
        :param dir:   Direction (degrees) of Line from North
        :type  inc:   float
        :type  dec:   float
        :type  incp:  float
        :type  dir:   float

        .. versionadded:: 5.0

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_
        """
        self._red_pol(inc, dec, incp, dir)
        




    def nyquist(self):
        """
        Gets the Nyquist frequency (wavenumbers/sample unit).
        

        :returns:    Nyquist frequency (wavenumbers/sample unit).
        :rtype:      float

        .. versionadded:: 5.0

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_
        """
        ret_val = self._nyquist()
        return ret_val




    def samp_incr(self):
        """
        Gets the original sample increment.
        

        :returns:    Original sample increment.
        :rtype:      float

        .. versionadded:: 5.0

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_
        """
        ret_val = self._samp_incr()
        return ret_val




    def wave_incr(self):
        """
        Get the wave number increment.
        

        :returns:    Wave number increment
        :rtype:      float

        .. versionadded:: 5.0

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_
        """
        ret_val = self._wave_incr()
        return ret_val




    def set_vv(self, gv_vr, gv_vi):
        """
        Sets real and imaginary VVs in `GXFFT <geosoft.gxapi.GXFFT>`.
        
        :param gv_vr:  Real component
        :param gv_vi:  Imaginary component
        :type  gv_vr:  GXVV
        :type  gv_vi:  GXVV

        .. versionadded:: 5.0

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_

        **Note:** The `GXVV <geosoft.gxapi.GXVV>` must have been obtained from the same `GXFFT <geosoft.gxapi.GXFFT>`
        using the `set_vv <geosoft.gxapi.GXFFT.set_vv>` method.
        """
        self._set_vv(gv_vr, gv_vi)
        




    def spectrum(self, gvv):
        """
        Calculates a power spectrum
        
        :param gvv:  Output power spectrum `GXVV <geosoft.gxapi.GXVV>`
        :type  gvv:  GXVV

        .. versionadded:: 5.0

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_
        """
        self._spectrum(gvv)
        




    def v_drv(self, order):
        """
        Vertical derivative
        
        :param order:  Order of differentiation (default = 1)
        :type  order:  float

        .. versionadded:: 5.0

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_
        """
        self._v_drv(order)
        




    def v_int(self):
        """
        Vertical integration
        

        .. versionadded:: 5.0

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_
        """
        self._v_int()
        




    def write_spectrum(self, gvv, out_file):
        """
        Writes a power spectrum to a file
        
        :param gvv:       Output power spectrum `GXVV <geosoft.gxapi.GXVV>`
        :param out_file:  File name for output spectrum
        :type  gvv:       GXVV
        :type  out_file:  str

        .. versionadded:: 5.0

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_
        """
        self._write_spectrum(gvv, out_file.encode())
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer