#  Copyright (c) 2025 Bentley Systems, Incorporated. All rights reserved.

### extends 'class_empty.py'
### block ClassImports
# NOTICE: Do not edit anything here, it is generated code
import warnings
from . import gxapi_cy
from geosoft.gxapi import GXContext, float_ref, int_ref, str_ref


### endblock ClassImports

### block Header
# NOTICE: The code generator will not replace the code in this block

### endblock Header

### block ClassImplementation
# NOTICE: Do not edit anything here, it is generated code
class GXRPS(gxapi_cy.WrapRPS):
    """
    GXRPS class.

    Not a class. A catch-all group of functions performing
    various Radiometric Processing System tasks.
    """

    def __init__(self, handle=0):
        super(GXRPS, self).__init__(GXContext._get_tls_geo(), handle)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of `GXRPS <geosoft.gxapi.GXRPS>`
        
        :returns: A null `GXRPS <geosoft.gxapi.GXRPS>`
        :rtype:   GXRPS
        """
        return GXRPS()

    def is_null(self):
        """
        Check if this is a null (undefined) instance
        
        :returns: True if this is a null (undefined) instance, False otherwise.
        :rtype:   bool
        """
        return self._internal_handle() == 0



# Miscellaneous


    @classmethod
    def window_spectrum_to_channel(cls, db, line, spectral_data, start_window, end_window, output_channel, channel_description):
        """
        
        Window radiometric data channel on a line in a database
        
        :param db:                   `GXDB <geosoft.gxapi.GXDB>` Object
        :param line:                 Line to process (NULLSYMB for all selected lines)
        :param spectral_data:        Spectral data channel handle (READONLY)
        :param start_window:         Starting fractional window index (0 to N)
        :param end_window:           Ending fractional window index (0 to N), >= Starting window
        :param output_channel:       Output channel handle (READWRITE)
        :param channel_description:  Output channel description for output/errors etc
        :type  db:                   GXDB
        :type  line:                 int
        :type  spectral_data:        int
        :type  start_window:         float
        :type  end_window:           float
        :type  output_channel:       int
        :type  channel_description:  str

        .. versionadded:: 2025.2.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** The average value of the windows in the given fractional index range is 
        written to the specified output channel.
        For instance, if you specified 0.5 to 1.5, then half values in the first
        window would be added to half the values in the second window. To specify
        a single window 'i' you need to specify the range i to i+1.

        Ref:  See the RPSWINDOW.GXC file for details and implementation of the algorithm.
        """
        
        gxapi_cy.WrapRPS._window_spectrum_to_channel(GXContext._get_tls_geo(), db, line, spectral_data, start_window, end_window, output_channel, channel_description.encode())
        



    @classmethod
    def full_spectral_analysis(cls, db, line, spectral_data_channel, livetime_channel, altitude_channel, mcf_file, fit_mode, output_channel_suffix):
        """
        
        Apply Medusa's Full Spectral Analysis algorithm to extract the radionuclide channels from the spectral data
        
        :param db:                     `GXDB <geosoft.gxapi.GXDB>` Object
        :param line:                   Line to process (NULLSYMB for all selected lines)
        :param spectral_data_channel:  Spectral data channel name
        :param livetime_channel:       Livetime channel name - assumes 1.0 if left blank
        :param altitude_channel:       Altitude (e.g. radar altimeter) channel name - assumes 0 if left blank
        :param mcf_file:               MCF file
        :param fit_mode:               :ref:`RPS_FITMODE`
        :param output_channel_suffix:  Suffix for output channels
        :type  db:                     GXDB
        :type  line:                   int
        :type  spectral_data_channel:  str
        :type  livetime_channel:       str
        :type  altitude_channel:       str
        :type  mcf_file:               str
        :type  fit_mode:               int
        :type  output_channel_suffix:  str

        .. versionadded:: 2026.1.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** 
        """
        
        gxapi_cy.WrapRPS._full_spectral_analysis(GXContext._get_tls_geo(), db, line, spectral_data_channel.encode(), livetime_channel.encode(), altitude_channel.encode(), mcf_file.encode(), fit_mode, output_channel_suffix.encode())
        



    @classmethod
    def dead_time_correction(cls, db, line, raw_channel, raw_tc_channel, deadtime_factor, deadtime_corr_channel):
        """
        
        Apply the Dead-time correction to a channel for a line in a database, assumes one second per pulse.
        
        :param db:                     `GXDB <geosoft.gxapi.GXDB>` Object
        :param line:                   Line to process (NULLSYMB for all selected lines)
        :param raw_channel:            Input raw channel name
        :param raw_tc_channel:         Input raw total count channel name
        :param deadtime_factor:        Dead time factor (microseconds/pulse
        :param deadtime_corr_channel:  Output deadtime corrected channel name
        :type  db:                     GXDB
        :type  line:                   int
        :type  raw_channel:            str
        :type  raw_tc_channel:         str
        :type  deadtime_factor:        float
        :type  deadtime_corr_channel:  str

        .. versionadded:: 2025.2.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** The output dead-time corrected channel is calculated using the formula:

        deadtime_corrected_value = raw_value / (1 - raw_TC * dead_time * 0.000001)

        where:

        deadtime_corrected_value = output dead-time corrected value
        raw_value = raw channel value (counts)
        raw_TC = raw total count channel value
        dead_time = dead-time factor (microseconds/pulse)

        Ref:  See the RPSFILT.GXC file for details and implementation of the algorithm.
        """
        
        gxapi_cy.WrapRPS._dead_time_correction(GXContext._get_tls_geo(), db, line, raw_channel.encode(), raw_tc_channel.encode(), deadtime_factor, deadtime_corr_channel.encode())
        



    @classmethod
    def dead_time_correction_acq_channel(cls, db, line, raw_channel, deadtime_channel, acqtime_channel, deadtime_corr_channel):
        """
        
        Apply the Dead-time correction to a channel for a line in a database, using an acquisition time channel.
        
        :param db:                     `GXDB <geosoft.gxapi.GXDB>` Object
        :param line:                   Line to process (NULLSYMB for all selected lines)
        :param raw_channel:            Input raw channel name
        :param deadtime_channel:       Dead time channel name (same units as the acquisition time channel)
        :param acqtime_channel:        Acquisition dead channel name (same units as the dead time channel)
        :param deadtime_corr_channel:  Output deadtime corrected channel name
        :type  db:                     GXDB
        :type  line:                   int
        :type  raw_channel:            str
        :type  deadtime_channel:       str
        :type  acqtime_channel:        str
        :type  deadtime_corr_channel:  str

        .. versionadded:: 2026.1.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** The output dead-time corrected channel is calculated using the formula:

        deadtime_corrected_value = raw_value * (acq_time_value / (acq_time_value - deadtime_value))

        where:

        deadtime_corrected_value = output dead-time corrected value
        raw_value = raw channel value (counts)
        acq_time_value = input acquisition-time channel value (same units as the dead time value)
        deadtime_value = dead time channel value (same units as the acquisition time value)

        Ref:  See the RPSFILT.GXC file for details and implementation of the algorithm.
        """
        
        gxapi_cy.WrapRPS._dead_time_correction_acq_channel(GXContext._get_tls_geo(), db, line, raw_channel.encode(), deadtime_channel.encode(), acqtime_channel.encode(), deadtime_corr_channel.encode())
        



    @classmethod
    def dead_time_correction_acq_value(cls, db, line, raw_channel, deadtime_channel, acqtime_constant_value, deadtime_corr_channel):
        """
        
        Apply the Dead-time correction to a channel for a line in a database, using a constant acquisition time value
        
        :param db:                      `GXDB <geosoft.gxapi.GXDB>` Object
        :param line:                    Line to process (NULLSYMB for all selected lines)
        :param raw_channel:             Input raw channel name
        :param deadtime_channel:        Dead time channel name (same units as acqtime_constant_value)
        :param acqtime_constant_value:  Acquisition time constant value (same units as livetime_channel)
        :param deadtime_corr_channel:   Output livetime corrected channel name
        :type  db:                      GXDB
        :type  line:                    int
        :type  raw_channel:             str
        :type  deadtime_channel:        str
        :type  acqtime_constant_value:  float
        :type  deadtime_corr_channel:   str

        .. versionadded:: 2026.1.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** The output dead-time corrected channel is calculated using the formula:

        deadtime_corrected_value = raw_value * (acq_time_value / (acq_time_value - deadtime_value))

        where:

        deadtime_corrected_value = output dead-time corrected value
        raw_value = raw channel value (counts)
        acq_time_value = input acquisition-time constant value (same units as the dead time value)
        deadtime_value = dead time channel (same units as the acquisition time value)
        """
        
        gxapi_cy.WrapRPS._dead_time_correction_acq_value(GXContext._get_tls_geo(), db, line, raw_channel.encode(), deadtime_channel.encode(), acqtime_constant_value, deadtime_corr_channel.encode())
        



    @classmethod
    def live_time_correction(cls, db, line, raw_channel, livetime_channel, livetime_corr_channel):
        """
        
        Apply the Live-time correction to a channel for a line in a database. Assumes one second per pulse.
        
        :param db:                     `GXDB <geosoft.gxapi.GXDB>` Object
        :param line:                   Line to process (NULLSYMB for all selected lines)
        :param raw_channel:            Input raw channel name
        :param livetime_channel:       Live time channel name (milliseconds)
        :param livetime_corr_channel:  Output livetime corrected channel name
        :type  db:                     GXDB
        :type  line:                   int
        :type  raw_channel:            str
        :type  livetime_channel:       str
        :type  livetime_corr_channel:  str

        .. versionadded:: 2025.2.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** The output live-time corrected channel is calculated using the formula:

        livetime_corrected_value = 1000 * raw_value / livetime_value

        where:

        livetime_corrected_value = output live-time corrected value
        raw_value = raw channel value (counts)
        livetime_value = live time channel value (milliseconds)

        Ref:  See the RPSFILT.GXC file for details and implementation of the algorithm.
        """
        
        gxapi_cy.WrapRPS._live_time_correction(GXContext._get_tls_geo(), db, line, raw_channel.encode(), livetime_channel.encode(), livetime_corr_channel.encode())
        



    @classmethod
    def live_time_correction_acq_channel(cls, db, line, raw_channel, livetime_channel, acqtime_channel, livetime_corr_channel):
        """
        
        Apply the Live-time correction to a channel for a line in a database, using an acquisition time channel
        
        :param db:                     `GXDB <geosoft.gxapi.GXDB>` Object
        :param line:                   Line to process (NULLSYMB for all selected lines)
        :param raw_channel:            Input raw channel name
        :param livetime_channel:       Live time channel name (same units as the acquisition time channel)
        :param acqtime_channel:        Acquisition time channel name (same units as the live time channel)
        :param livetime_corr_channel:  Output livetime corrected channel name
        :type  db:                     GXDB
        :type  line:                   int
        :type  raw_channel:            str
        :type  livetime_channel:       str
        :type  acqtime_channel:        str
        :type  livetime_corr_channel:  str

        .. versionadded:: 2026.1.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** The output live-time corrected channel is calculated using the formula:

        livetime_corrected_value = acq_time_value * raw_value / livetime_value

        where:

        livetime_corrected_value = output live-time corrected value
        acq_time_value = input acquisition-time channel value (same units as the live time value)
        raw_value = raw channel value (counts)
        livetime_value = live time channel value (same units as the acquisition time value)
        """
        
        gxapi_cy.WrapRPS._live_time_correction_acq_channel(GXContext._get_tls_geo(), db, line, raw_channel.encode(), livetime_channel.encode(), acqtime_channel.encode(), livetime_corr_channel.encode())
        



    @classmethod
    def live_time_correction_acq_value(cls, db, line, raw_channel, livetime_channel, acqtime_constant_value, livetime_corr_channel):
        """
        
        Apply the Live-time correction to a channel for a line in a database, using a constant acquisition time value
        
        :param db:                      `GXDB <geosoft.gxapi.GXDB>` Object
        :param line:                    Line to process (NULLSYMB for all selected lines)
        :param raw_channel:             Input raw channel name
        :param livetime_channel:        Live time channel name (same units as acqtime_constant_value)
        :param acqtime_constant_value:  Acquisition time constant value (same units as livetime_channel)
        :param livetime_corr_channel:   Output livetime corrected channel name
        :type  db:                      GXDB
        :type  line:                    int
        :type  raw_channel:             str
        :type  livetime_channel:        str
        :type  acqtime_constant_value:  float
        :type  livetime_corr_channel:   str

        .. versionadded:: 2026.1.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** The output live-time corrected channel is calculated using the formula:

        livetime_corrected_value = acq_time_value * raw_value / livetime_value

        where:

        livetime_corrected_value = output live-time corrected value
        acq_time_value = input acquisition-time constant value (same units as the live time value)
        raw_value = raw channel value (counts)
        livetime_value = live time channel value (same units as the acquisition time value)
        """
        
        gxapi_cy.WrapRPS._live_time_correction_acq_value(GXContext._get_tls_geo(), db, line, raw_channel.encode(), livetime_channel.encode(), acqtime_constant_value, livetime_corr_channel.encode())
        



    @classmethod
    def stp_correction_from_barometric_altitude(cls, db, line, raw_radar_altimeter, raw_barometric_altimeter_channel, temperature_channel, stp_alt_channel):
        """
        
        Apply the Standard Temperature/Pressure (STP) correction to the altimeter channel for a line in a database
        
        :param db:                                `GXDB <geosoft.gxapi.GXDB>` Object
        :param line:                              Line to process (NULLSYMB for all selected lines)
        :param raw_radar_altimeter:               Input (BP-filtered) radar altimeter channel name
        :param raw_barometric_altimeter_channel:  Input raw barometric altimeter channel name
        :param temperature_channel:               Input temperature channel name (degrees Celsius)
        :param stp_alt_channel:                   Output STP corrected altimeter channel name
        :type  db:                                GXDB
        :type  line:                              int
        :type  raw_radar_altimeter:               str
        :type  raw_barometric_altimeter_channel:  str
        :type  temperature_channel:               str
        :type  stp_alt_channel:                   str

        .. versionadded:: 2025.2.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** The output STP corrected altitude is calculated using the formula:

        STP_Altitude = (273.15 * radar_alt * exp(-1.0/8581.0 * barometric_alt))/(273.15 + temp)

        where:

        STP_Altitude = STP corrected altitude (m)
        radar_alt = raw radar altimeter channel value (m)
        barometric_alt = raw barometric altimeter channel value (m)
        temp = temperature channel value (degrees Celsius)

        Ref:  See the RPSFILT.GXC file for details and implementation of the algorithm.
        """
        
        gxapi_cy.WrapRPS._stp_correction_from_barometric_altitude(GXContext._get_tls_geo(), db, line, raw_radar_altimeter.encode(), raw_barometric_altimeter_channel.encode(), temperature_channel.encode(), stp_alt_channel.encode())
        



    @classmethod
    def stp_correction_from_pressure(cls, db, line, raw_radar_altimeter, pressure_channel, temperature_channel, stp_alt_channel):
        """
        
        Apply the Standard Temperature/Pressure (STP) correction to the altimeter channel for a line in a database
        
        :param db:                   `GXDB <geosoft.gxapi.GXDB>` Object
        :param line:                 Line to process (NULLSYMB for all selected lines)
        :param raw_radar_altimeter:  Input (BP-filtered) radar altimeter channel name
        :param pressure_channel:     Input pressure channel name (kPa)
        :param temperature_channel:  Input temperature channel name (degrees Celsius)
        :param stp_alt_channel:      Output STP corrected altimeter channel name
        :type  db:                   GXDB
        :type  line:                 int
        :type  raw_radar_altimeter:  str
        :type  pressure_channel:     str
        :type  temperature_channel:  str
        :type  stp_alt_channel:      str

        .. versionadded:: 2025.2.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** The output STP corrected altitude is calculated using the formula:

        STP_Altitude = (273.15 * radar_alt * P))/((273.15 + temp) * 101.325)

        where:

        STP_Altitude = STP corrected altitude (m)
        radar_alt = raw radar altimeter channel value (m)
        P = raw pressure channel value (kPa)
        temp = temperature channel value (degrees Celsius)
        """
        
        gxapi_cy.WrapRPS._stp_correction_from_pressure(GXContext._get_tls_geo(), db, line, raw_radar_altimeter.encode(), pressure_channel.encode(), temperature_channel.encode(), stp_alt_channel.encode())
        



    @classmethod
    def altitude_attenuation(cls, db, line, input_channel, height_att_coeff, nom_altimeter, stp_alt_channel, output_channel):
        """
        
        Apply altitude attenuation for a radioelement
        
        :param db:                `GXDB <geosoft.gxapi.GXDB>` Object
        :param line:              Line to process (NULLSYMB for all selected lines)
        :param input_channel:     Input channel name
        :param height_att_coeff:  Height attenuation coefficient (per metre at STP)
        :param nom_altimeter:     Nominal survey altitude (m)
        :param stp_alt_channel:   Input STP corrected altimeter channel name
        :param output_channel:    Output channel name (can be same channel as input)
        :type  db:                GXDB
        :type  line:              int
        :type  input_channel:     str
        :type  height_att_coeff:  float
        :type  nom_altimeter:     float
        :type  stp_alt_channel:   str
        :type  output_channel:    str

        .. versionadded:: 2025.2.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** The altitude attenuation is calculated using the formula:

        Ns = Nm * exp(k * (H0 - H)) => Ns = Nm * exp(-k * (H - H0))

        where:
        Ns = the count rate normalized to the nominal survey altitude, H0,
        Nm = the background corrected, stripped count rate at effective height H,
        k = height attenuation coefficient (per metre at STP)
        H = effective altitude (m)
        H0 = nominal survey altitude (m)

        The effective height was determined by applying Compton Stripping.

        HEIGHT ATTENUATION COEFF:   Total Count  (Recommended: -0.0070)
        (per metre at STP)          Potassium    (Recommended: -0.0088)
                                    Uranium      (Recommended: -0.0082)
                                    Thorium      (Recommended: -0.0070)

        Ref:  See the RPSCORR.GXC file for details and implementation of the algorithm.
        """
        
        gxapi_cy.WrapRPS._altitude_attenuation(GXContext._get_tls_geo(), db, line, input_channel.encode(), height_att_coeff, nom_altimeter, stp_alt_channel.encode(), output_channel.encode())
        



    @classmethod
    def compton_stripping(cls, db, line, stp_alt_channel, K_levl, U_levl, Th_levl, alpha, beta, gamma, a, b, g, k_strip, u_strip, th_strip):
        """
        
        Perform Compton Stripping
        
        :param db:               `GXDB <geosoft.gxapi.GXDB>` Object
        :param line:             Line to process (NULLSYMB for all selected lines)
        :param stp_alt_channel:  Input STP corrected altimeter channel name
        :param K_levl:           Input Postassium levelelled count channel
        :param U_levl:           Input Uranium levelelled count channel
        :param Th_levl:          Input Thorium levelelled count channel
        :param alpha:            Input Compton Stripping ratio alpha
        :param beta:             Input Compton Stripping ratio beta
        :param gamma:            Input Compton Stripping ratio gamma
        :param a:                Input Compton Stripping ratio a
        :param b:                Input Compton Stripping ratio b
        :param g:                Input Compton Stripping ratio g
        :param k_strip:          Output Compton Stripped Potassium channel (can be same channel as input)
        :param u_strip:          Output Compton Stripped Uranium channel (can be same channel as input)
        :param th_strip:         Output Compton Stripped Thorium channel (can be same channel as input)
        :type  db:               GXDB
        :type  line:             int
        :type  stp_alt_channel:  str
        :type  K_levl:           str
        :type  U_levl:           str
        :type  Th_levl:          str
        :type  alpha:            float
        :type  beta:             float
        :type  gamma:            float
        :type  a:                float
        :type  b:                float
        :type  g:                float
        :type  k_strip:          str
        :type  u_strip:          str
        :type  th_strip:         str

        .. versionadded:: 2025.2.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** Compton stripping is calculated using the formula:

        KSTRIP = (BK*THLEVL + CK*ULEVL + DK*KLEVL) / A
        USTRIP = (BU*THLEVL + CU*ULEVL + DU*KLEVL) / A
        THSTRIP = (BTH*THLEVL + CTH*ULEVL + DTH*KLEVL) / A

        where

        KSTRIP = Output Compton stripped potassium (can be same channel as input)
        USTRIP = Output Compton stripped uranium (can be same channel as input)
        THSTRIP = Output Compton stripped thorium (can be same channel as input)

        and where:

        KLEVL = Input potassium levelled count channel (e.g. "KLEVL")
        ULEVL = Input uranium levelled count channel (e.g. "ULEVL")
        THLEVL = Input thorium levelled count channel (e.g. "THLEVL")

        BK = ALPHA2*GAMMA2-BETA2;
        CK = ASTRIP*BETA2-GAMMA2;
        DK = 1-ASTRIP*ALPHA2;

        BU = GSTRIP*BETA-ALPHA
        CU = 1-BSTRIP*BETA
        DU = BSTRIP*ALPHA-GSTRIP

        BTH = 1-GSTRIP*GAMMA2;
        CTH = BSTRIP*GAMMA2-ASTRIP;
        DTH = ASTRIP*GSTRIP-BSTRIP;

        where:

        ALPHA2 = ALPHA + 0.0004895*RALTSTP
        BETA2 = BETA + 0.0006469*RALTSTP
        GAMMA2 = GAMMA + 0.0006874*RALTSTP

        and:

        RALTSTP = Input STP corrected radar altimeter channel value (m)
        ALPHA = Input Compton stripping alpha factor
        BETA = Input Compton stripping beta factor
        GAMMA = Input Compton stripping gamma factor
        ASTRIP = Input Compton stripping a factor
        BSTRIP = Input Compton stripping b factor
        GSTRIP = Input Compton stripping g factor

        and where:

        A = 1-GSTRIP*GAMMA2 - ASTRIP*(ALPHA2 - GSTRIP*BETA2) -
               BSTRIP*(BETA2-ALPHA2*GAMMA2)

        Ref:  See the RPSCORR.GXC file for details and implementation of the algorithm.
        """
        
        gxapi_cy.WrapRPS._compton_stripping(GXContext._get_tls_geo(), db, line, stp_alt_channel.encode(), K_levl.encode(), U_levl.encode(), Th_levl.encode(), alpha, beta, gamma, a, b, g, k_strip.encode(), u_strip.encode(), th_strip.encode())
        



    @classmethod
    def convert_to_elemental(cls, db, line, K, U, Th, TC, k_sens, u_sens, th_sens, tc_sens, k_conc, u_conc, th_conc, TC_conc):
        """
        
        Convert a radio-channels' data to ELemental concentrations
        
        :param db:       `GXDB <geosoft.gxapi.GXDB>` Object
        :param line:     Line to process (NULLSYMB for all selected lines)
        :param K:        Input Postassium count channel
        :param U:        Input Uranium count channel
        :param Th:       Input Thorium count channel
        :param TC:       Input Total Count channel
        :param k_sens:   Potassium broad source sensitivity (units (cps/%))
        :param u_sens:   Uranium broad source sensitivity (units (cps/ppm))
        :param th_sens:  Thorium broad source sensitivity (units (cps/ppm))
        :param tc_sens:  Total count broad source sensitivity (units (uR/hr))
        :param k_conc:   Output elemental concentration Potassium channel (can be same channel as input)
        :param u_conc:   Output elemental concentration Uranium channel (can be same channel as input)
        :param th_conc:  Output elemental concentration Thorium channel (can be same channel as input)
        :param TC_conc:  Output elemental concentration Total Count channel (can be same channel as input)
        :type  db:       GXDB
        :type  line:     int
        :type  K:        str
        :type  U:        str
        :type  Th:       str
        :type  TC:       str
        :type  k_sens:   float
        :type  u_sens:   float
        :type  th_sens:  float
        :type  tc_sens:  float
        :type  k_conc:   str
        :type  u_conc:   str
        :type  th_conc:  str
        :type  TC_conc:  str

        .. versionadded:: 2025.2.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** The conversions are calculated using the formulae:

        OutputK = InputK / SensK
        OutputU = InputU / SensU
        OutputTh = InputTh / SensTh
        OutputTC = Input TC / SensTC

        where:

        OutputK = Output potassium channel expressed in elemental concentration
        OutputU = Output uranium channel expressed in elemental concentration
        OutputTh = Output thorium channel expressed in elemental concentration
        OutputTC = Output total count channel expressed in elemental concentration

        InputK = Input potassium channel expressed in counts
        InputU = Input uranium channel expressed in counts
        InputTh = Input thorium channel expressed in counts
        InputTC = Input total count channel expressed in counts

        SensK = Input Potassium Broad source sensitivity (units: (cps/%))
        SensU = Input Uranium Broad source sensitivity (units: (cps/ppm))
        SensTh = Input Thorium Broad source sensitivity (units: (cps/ppm))
        SensTC = Input Total Count Broad source sensitivity (units: (uR/hr))

        Ref:  See the RPSCORR.GXC file for details and implementation of the algorithm.
        """
        
        gxapi_cy.WrapRPS._convert_to_elemental(GXContext._get_tls_geo(), db, line, K.encode(), U.encode(), Th.encode(), TC.encode(), k_sens, u_sens, th_sens, tc_sens, k_conc.encode(), u_conc.encode(), th_conc.encode(), TC_conc.encode())
        



    @classmethod
    def radon_background_table(cls, db, line, table, ref_field, K_field, U_field, Th_field, TC_field, ref_channel, K_channel, U_channel, Th_channel, TC_channel, interp_mode):
        """
        
        Calculate the Radon Background using a Background Table
        
        :param db:           `GXDB <geosoft.gxapi.GXDB>` Object
        :param line:         Line to process (NULLSYMB for all selected lines)
        :param table:        Reference background look-up table (e.g. "rpsbackg.tbl"
        :param ref_field:    Reference field name in table
        :param K_field:      Potassium field name in table
        :param U_field:      Uranium field name in table
        :param Th_field:     Thorium field name in table
        :param TC_field:     Total count field name in table
        :param ref_channel:  Reference channel handle (READONLY)
        :param K_channel:    Output potassium channel handle (READWRITE)
        :param U_channel:    Output uranium channel handle (READWRITE)
        :param Th_channel:   Output thorium channel handle (READWRITE)
        :param TC_channel:   Output total count channel handle (READWRITE)
        :param interp_mode:  :ref:`DU_LOOKUP`
        :type  db:           GXDB
        :type  line:         int
        :type  table:        GXTB
        :type  ref_field:    str
        :type  K_field:      str
        :type  U_field:      str
        :type  Th_field:     str
        :type  TC_field:     str
        :type  ref_channel:  int
        :type  K_channel:    int
        :type  U_channel:    int
        :type  Th_channel:   int
        :type  TC_channel:   int
        :type  interp_mode:  int

        .. versionadded:: 2025.2.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** Background levels for K, U, Th and TC are calculated obtained by table-lookup using a reference channel.

        Ref:  See the RPSLEVT.GXC file for details and implementation of the algorithm.
        """
        
        gxapi_cy.WrapRPS._radon_background_table(GXContext._get_tls_geo(), db, line, table, ref_field.encode(), K_field.encode(), U_field.encode(), Th_field.encode(), TC_field.encode(), ref_channel, K_channel, U_channel, Th_channel, TC_channel, interp_mode)
        



    @classmethod
    def radon_upward_removal_calculate(cls, db, line, U_filt, Th_filt, U_upward_filt, skyshine_A1, skyshine_A2, ak, ath, au, atc, bk, bu, bth, btc, K_back, U_back, Th_back, TC_back, U_upward_back):
        """
        
        Calculate the Radon Background to remove using the 'upward' method
        
        :param db:             `GXDB <geosoft.gxapi.GXDB>` Object
        :param line:           Line to process (NULLSYMB for all selected lines)
        :param U_filt:         Input Low-pass filtered uranium channel
        :param Th_filt:        Input Low-pass filtered thorium channel
        :param U_upward_filt:  Input Low-pass filtered upward uranium channel
        :param skyshine_A1:    Input Skyshine coefficient A1
        :param skyshine_A2:    Input Skyshine coefficient A2
        :param ak:             Input calibration factor ak - potassium
        :param ath:            Input calibration factor ath - thorium
        :param au:             Input calibration factor au - uranium
        :param atc:            Input calibration factor atc - total count
        :param bk:             Input calibration factor bk - potassium
        :param bu:             Input calibration factor bu - uranium
        :param bth:            Input calibration factor bth - thorium
        :param btc:            Input calibration factor btc - total count
        :param K_back:         Output potassium background to remove (channel)
        :param U_back:         Output uranium background to remove (channel)
        :param Th_back:        Output thorium channel background to remove (channel)
        :param TC_back:        Output total count background to remove (channel)
        :param U_upward_back:  Output upward uranium background to remove (channel)
        :type  db:             GXDB
        :type  line:           int
        :type  U_filt:         str
        :type  Th_filt:        str
        :type  U_upward_filt:  str
        :type  skyshine_A1:    float
        :type  skyshine_A2:    float
        :type  ak:             float
        :type  ath:            float
        :type  au:             float
        :type  atc:            float
        :type  bk:             float
        :type  bu:             float
        :type  bth:            float
        :type  btc:            float
        :type  K_back:         str
        :type  U_back:         str
        :type  Th_back:        str
        :type  TC_back:        str
        :type  U_upward_back:  str

        .. versionadded:: 2025.2.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** The Upward method of radon-removal is applied to the low-pass filtered data,
         using the formula:

        KRADREF   = AK * URADREF + BK       Output potassium background to remove (channel)
        THRADREF  = ATH * URADREF + BTH       Output thorium background to remove (channel)
        TCRADREF  = ATC * URADREF + BTC     Output total count background to remove (channel)
        UPURADREF = AU * URADREF + BU       Output upward uranium background to remove (channel)

        where:

         AK  = Input calibration factor ak
         BK  = Input calibration factor bk
         ATH  = Input calibration factor at
         BTH  = Input calibration factor bt
         ATC = Input calibration factor atc
         BTC = Input calibration factor btc
         AU  = Input calibration factor au
         BU  = Input calibration factor bu

        and:

         URADREF = Output uranium background to remove (channel)

        where

         URADREF = (UPUFILT - A1*UFILT - A2*THFILT + A2*BTH - BU)/
                                            (AU-A1 - A2*ATH)

         THFILT  = Input Low-pass filtered thorium channel
         UFILT   = Input Low-pass filtered uranium channel
         UPUFILT = Input Low-pass filtered upward uranium channel

        and

         A1 = Input Skyshine coefficient A1
         A2 = Input Skyshine coefficient A2

        Ref: See the RPSLEVLU.GXC file for details and implementation of the algorithm.
        """
        
        gxapi_cy.WrapRPS._radon_upward_removal_calculate(GXContext._get_tls_geo(), db, line, U_filt.encode(), Th_filt.encode(), U_upward_filt.encode(), skyshine_A1, skyshine_A2, ak, ath, au, atc, bk, bu, bth, btc, K_back.encode(), U_back.encode(), Th_back.encode(), TC_back.encode(), U_upward_back.encode())
        



    @classmethod
    def radon_upward_removal_apply(cls, db, line, K_filt, U_filt, Th_filt, TC_filt, U_upward_filt, K_back, U_back, Th_back, TC_back, U_upward_back, K_out, U_out, Th_out, TC_out, U_upward_out):
        """
        
        Remove the calculated Radon Background using the 'upward' method
        
        :param db:             `GXDB <geosoft.gxapi.GXDB>` Object
        :param line:           Line to process (NULLSYMB for all selected lines)
        :param K_filt:         Input Low-pass filtered potassium channel
        :param U_filt:         Input Low-pass filtered uranium channel
        :param Th_filt:        Input Low-pass filtered thorium channel
        :param TC_filt:        Input Low-pass filtered total count channel
        :param U_upward_filt:  Input Low-pass filtered upward uranium channel
        :param K_back:         Input potassium background to remove (channel)
        :param U_back:         Input uranium background to remove (channel)
        :param Th_back:        Input thorium channel background to remove (channel)
        :param TC_back:        Input total count background to remove (channel)
        :param U_upward_back:  Input upward uranium background to remove (channel)
        :param K_out:          Output potassium channel with background radon removed
        :param U_out:          Output uranium channel with background radon removed
        :param Th_out:         Output thorium channel with background radon removed
        :param TC_out:         Output total count channel with background radon removed
        :param U_upward_out:   Output upward uranium channel with background radon removed
        :type  db:             GXDB
        :type  line:           int
        :type  K_filt:         str
        :type  U_filt:         str
        :type  Th_filt:        str
        :type  TC_filt:        str
        :type  U_upward_filt:  str
        :type  K_back:         str
        :type  U_back:         str
        :type  Th_back:        str
        :type  TC_back:        str
        :type  U_upward_back:  str
        :type  K_out:          str
        :type  U_out:          str
        :type  Th_out:         str
        :type  TC_out:         str
        :type  U_upward_out:   str

        .. versionadded:: 2025.2.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** The calculated Radon Background to remove is applied to the data channels using the formula:

         KOUT = KFILT - KRADREF           Output potassium channel with radon background removed
         UOUT = UFILT - URADREF           Output uranium channel with radon background removed
         THOUT = THFILT - THRADREF        Output thorium channel with radon background removed
         TCOUT = TCFILT - TCRADREF        Output total count channel with radon background removed
         UPUOUT = UPUFILT - UPURADREF     Output upward uranium channel with radon background removed

         where:

         KFILT   = Input Low-pass filtered potassium channel
         UFILT   = Input Low-pass filtered uranium channel
         THFILT  = Input Low-pass filtered thorium channel
         TCFILT  = Input Low-pass filtered total count channel
         UPUFILT = Input Low-pass filtered upward uranium channel

         and the following calculated using the RadonUpwardRemovalCalculate_RPS method:

        KRADREF   = Input potassium background to remove (channel)
        URADREF   = Input uranium background to remove (channel)
        THRADREF  = Input uranium background to remove (channel)
        TCRADREF  = Input thorium background to remove (channel)
        UPURADREF = Input upward uranium background to remove (channel)

        Ref: See the RPSLEVLU.GXC file for details and implementation of the algorithm.
        """
        
        gxapi_cy.WrapRPS._radon_upward_removal_apply(GXContext._get_tls_geo(), db, line, K_filt.encode(), U_filt.encode(), Th_filt.encode(), TC_filt.encode(), U_upward_filt.encode(), K_back.encode(), U_back.encode(), Th_back.encode(), TC_back.encode(), U_upward_back.encode(), K_out.encode(), U_out.encode(), Th_out.encode(), TC_out.encode(), U_upward_out.encode())
        



    @classmethod
    def radon_overwater_reference_channels(cls, db, line, K_levl, U_levl, Th_levl, TC_levl, water_back_ref_channel, K_ref, U_ref, Th_ref, TC_ref):
        """
        
        Overwater Radon removel method: Calculate radon reference levels from the filtered data
        
        :param db:                      `GXDB <geosoft.gxapi.GXDB>` Object
        :param line:                    Line to process (NULLSYMB for all selected lines)
        :param K_levl:                  Input levelled Potassium data channel
        :param U_levl:                  Input levelled Uranium data channel
        :param Th_levl:                 Input levelled Thorium data channel
        :param TC_levl:                 Input levelled Total Count data channel
        :param water_back_ref_channel:  Input Water Background Reference channel name
        :param K_ref:                   Output Potassium Radon reference channel
        :param U_ref:                   Output Uranium Radon reference channel
        :param Th_ref:                  Output Thorium Radon reference channel
        :param TC_ref:                  Output Total Count Radon reference channel
        :type  db:                      GXDB
        :type  line:                    int
        :type  K_levl:                  str
        :type  U_levl:                  str
        :type  Th_levl:                 str
        :type  TC_levl:                 str
        :type  water_back_ref_channel:  str
        :type  K_ref:                   str
        :type  U_ref:                   str
        :type  Th_ref:                  str
        :type  TC_ref:                  str

        .. versionadded:: 2025.2.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** Radon reference channels are calculate via simple multiplication with the water background reference channel:

        KREF = KLEV * WREF     Output Potassium Radon reference channel
        UREF = ULEV * WREF     Output Uranium Radon reference channel 
        THREF = THLEV * WREF   Output Thorium Radon reference channel
        TCREF = TCLEV * WREF   Output Total Count Radon reference channe

        where

        KLEV = Input Potassium levelled count channel
        ULEV = Input Uranium levelled count channel
        THLEV = Input Thorium levelled count channel
        TCLEV = Input Total Count levelled count channel

        and

        WREF = Input Water Background Reference channel

        Ref:  See the RPSLEVT.GXC file for details and implementation of the algorithm.
        """
        
        gxapi_cy.WrapRPS._radon_overwater_reference_channels(GXContext._get_tls_geo(), db, line, K_levl.encode(), U_levl.encode(), Th_levl.encode(), TC_levl.encode(), water_back_ref_channel.encode(), K_ref.encode(), U_ref.encode(), Th_ref.encode(), TC_ref.encode())
        



    @classmethod
    def radon_overwater_create_background_table(cls, db, flight_ref_channel, water_back_ref_channel, K_ref, U_ref, Th_ref, TC_ref, fid_ref, table):
        """
        
        Create the table (TB) file used for the overwater radon removal method
        
        :param db:                      `GXDB <geosoft.gxapi.GXDB>` Object
        :param flight_ref_channel:      Input Flight Reference table column name (.e.g "_RpsFlight_"
        :param water_back_ref_channel:  Input Water Background Reference channel name
        :param K_ref:                   Input Potassium Radon reference channel
        :param U_ref:                   Input Uranium Radon reference channel
        :param Th_ref:                  Input Thorium Radon reference channel
        :param TC_ref:                  Input Total Count Radon reference channel
        :param fid_ref:                 Reference (e.g. FID) channel name (created)
        :param table:                   Output Radon reference table name
        :type  db:                      GXDB
        :type  flight_ref_channel:      str
        :type  water_back_ref_channel:  str
        :type  K_ref:                   str
        :type  U_ref:                   str
        :type  Th_ref:                  str
        :type  TC_ref:                  str
        :type  fid_ref:                 str
        :type  table:                   str

        .. versionadded:: 2025.2.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** The Radon reference channels are scanned to produce a table of background values.
        The table is created for all selected lines.

        Ref:  See the RPSLEVT.GXC file for details and implementation of the algorithm.
        """
        
        gxapi_cy.WrapRPS._radon_overwater_create_background_table(GXContext._get_tls_geo(), db, flight_ref_channel.encode(), water_back_ref_channel.encode(), K_ref.encode(), U_ref.encode(), Th_ref.encode(), TC_ref.encode(), fid_ref.encode(), table.encode())
        



    @classmethod
    def radon_overwater_background_correction(cls, db, line, K_bg, U_bg, Th_bg, TC_bg, K_ref, U_ref, Th_ref, TC_ref, K_rad, U_rad, Th_rad, TC_rad):
        """
        
        Overwater Radon correction method: Calculate radon correction levels from the reference channel
        
        :param db:      `GXDB <geosoft.gxapi.GXDB>` Object
        :param line:    Line to process (NULLSYMB for all selected lines)
        :param K_bg:    Input Potassium channel
        :param U_bg:    Input Uranium channel
        :param Th_bg:   Input Thorium channel
        :param TC_bg:   Input Total Count channel
        :param K_ref:   Input Potassium Radon reference channel
        :param U_ref:   Input Uranium Radon reference channel
        :param Th_ref:  Input Thorium Radon reference channel
        :param TC_ref:  Input Total Count Radon reference channel
        :param K_rad:   Output Potassium channel
        :param U_rad:   Output Uranium channel
        :param Th_rad:  Output Thorium channel
        :param TC_rad:  Output Total Count channel
        :type  db:      GXDB
        :type  line:    int
        :type  K_bg:    str
        :type  U_bg:    str
        :type  Th_bg:   str
        :type  TC_bg:   str
        :type  K_ref:   str
        :type  U_ref:   str
        :type  Th_ref:  str
        :type  TC_ref:  str
        :type  K_rad:   str
        :type  U_rad:   str
        :type  Th_rad:  str
        :type  TC_rad:  str

        .. versionadded:: 2025.2.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** Radon water background correction channel:

        K_rad = K_bg - KREF      Output Potassium Radon background correction channel
        U_rad = U_bg - UREF      Output Uranium Radon background correction channel 
        Th_rad = TH_bg - THREF   Output Thorium Radon background correction channel
        TC_rad = TC_bg - TCREF   Output Total Count Radon background correction channe

        where

        K_bg = Input Potassium levelled count channel
        U_bg = Input Uranium levelled count channel
        TH_bg = Input Thorium levelled count channel
        TC_bg = Input Total Count levelled count channel

        and

        KREF = Input Radon background reference channel
        UREF = Input Radon background reference channel
        THREF = Input Radon background reference channel
        TCREF = Input Radon background reference channel

        Ref:  See the RPSLEVT.GXC file for details and implementation of the algorithm.
        """
        
        gxapi_cy.WrapRPS._radon_overwater_background_correction(GXContext._get_tls_geo(), db, line, K_bg.encode(), U_bg.encode(), Th_bg.encode(), TC_bg.encode(), K_ref.encode(), U_ref.encode(), Th_ref.encode(), TC_ref.encode(), K_rad.encode(), U_rad.encode(), Th_rad.encode(), TC_rad.encode())
        



    @classmethod
    def radon_aircraft_cosmic_correction(cls, db, line, K_filt, U_filt, Th_filt, TC_filt, U_upward_filt, Cosmic_filt, aircraft_k, aircraft_u, aircraft_th, aircraft_tc, aircraft_upu, cosmic_k, cosmic_u, cosmic_th, cosmic_tc, cosmic_upu, K_levl, U_levl, Th_levl, TC_levl, U_upward_levl):
        """
        
        Remove effects of aircraft and cosmic stripping
        
        :param db:             `GXDB <geosoft.gxapi.GXDB>` Object
        :param line:           Line to process (NULLSYMB for all selected lines)
        :param K_filt:         Input filtered potassium channel
        :param U_filt:         Input filtered uranium channel
        :param Th_filt:        Input filtered thorium channel
        :param TC_filt:        Input filtered total count channel
        :param U_upward_filt:  Input filtered upward uranium channel (optional - can be left blank)
        :param Cosmic_filt:    Input filtered cosmic channel
        :param aircraft_k:     Aircraft background value for potassium (cps).
        :param aircraft_u:     Aircraft background value for uranium (cps).
        :param aircraft_th:    Aircraft background value for thorium (cps).
        :param aircraft_tc:    Aircraft background value for total count (cps).
        :param aircraft_upu:   Aircraft background value for upward uranium (cps) (optional - can be left blank if no upward channel is defined).
        :param cosmic_k:       Cosmic stripping ratio for potassium (cps/cosmic cps).
        :param cosmic_u:       Cosmic stripping ratio for uranium (cps/cosmic cps).
        :param cosmic_th:      Cosmic stripping ratio for thorium (cps/cosmic cps).
        :param cosmic_tc:      Cosmic stripping ratio for total count (cps/cosmic cps).
        :param cosmic_upu:     Cosmic stripping ratio for upward uranium (cps/cosmic cps) (optional - can be left blank if no upward channel is defined).
        :param K_levl:         Output levelled potassium channel
        :param U_levl:         Output levelled uranium channel
        :param Th_levl:        Output levelled thorium channel
        :param TC_levl:        Output levelled total count channel
        :param U_upward_levl:  Output levelled upward uranium channel (optional - can be left blank if no upward channel is defined)
        :type  db:             GXDB
        :type  line:           int
        :type  K_filt:         str
        :type  U_filt:         str
        :type  Th_filt:        str
        :type  TC_filt:        str
        :type  U_upward_filt:  str
        :type  Cosmic_filt:    str
        :type  aircraft_k:     float
        :type  aircraft_u:     float
        :type  aircraft_th:    float
        :type  aircraft_tc:    float
        :type  aircraft_upu:   float
        :type  cosmic_k:       float
        :type  cosmic_u:       float
        :type  cosmic_th:      float
        :type  cosmic_tc:      float
        :type  cosmic_upu:     float
        :type  K_levl:         str
        :type  U_levl:         str
        :type  Th_levl:        str
        :type  TC_levl:        str
        :type  U_upward_levl:  str

        .. versionadded:: 2025.2.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** This wrapper performs the following simple operation:

        LEVL = FILT - (AIRBACK + COS_STRIP * COSFILT)

        where:

        LEVL = Output levelled element channel
        FILT = Input filtered element channel
        AIRBACK = Input Air Background value for that element
        COS_STRIP = Input Cosmic Stripping factor for that element
        COSFILT = Input filtered cosmic channel

        The Upward uranium parameters are optional and can be left blank if not required,
        but all three should be defined for the Upward method.

        Ref:  See the RPSLEVU.GXC file for details and implementation of the algorithm.
        """
        
        gxapi_cy.WrapRPS._radon_aircraft_cosmic_correction(GXContext._get_tls_geo(), db, line, K_filt.encode(), U_filt.encode(), Th_filt.encode(), TC_filt.encode(), U_upward_filt.encode(), Cosmic_filt.encode(), aircraft_k, aircraft_u, aircraft_th, aircraft_tc, aircraft_upu, cosmic_k, cosmic_u, cosmic_th, cosmic_tc, cosmic_upu, K_levl.encode(), U_levl.encode(), Th_levl.encode(), TC_levl.encode(), U_upward_levl.encode())
        



    @classmethod
    def radio_element_bandpass_filter(cls, db, line, inputCh1, inputCh2, inputCh3, ch1_short_cutoff, ch1_high_cutoff, ch2_short_cutoff, ch2_high_cutoff, ch3_short_cutoff, ch3_high_cutoff, outputCh1, outputCh2, outputCh3):
        """
        
        Applies a band-pass filter for up to three elements simultaneously
        
        :param db:                `GXDB <geosoft.gxapi.GXDB>` Object
        :param line:              Line to process (NULLSYMB for all selected lines)
        :param inputCh1:          Input channel 1 handle (READONLY) (can be NULLSYMB to skip channel 1)
        :param inputCh2:          Input channel 2 handle (READONLY) (can be NULLSYMB to skip channel 2)
        :param inputCh3:          Input channel 3 handle (READONLY) (can be NULLSYMB to skip channel 3)
        :param ch1_short_cutoff:  Channel 1 short wavelength cutoff
        :param ch1_high_cutoff:   Channel 1 high wavelength cutoff
        :param ch2_short_cutoff:  Channel 2 short wavelength cutoff
        :param ch2_high_cutoff:   Channel 2 high wavelength cutoff
        :param ch3_short_cutoff:  Channel 3 short wavelength cutoff
        :param ch3_high_cutoff:   Channel 3 high wavelength cutoff
        :param outputCh1:         Output filtered channel 1 handle (READWRITE)
        :param outputCh2:         Output filtered channel 2 handle (READWRITE)
        :param outputCh3:         Output filtered channel 3 handle (READWRITE)
        :type  db:                GXDB
        :type  line:              int
        :type  inputCh1:          int
        :type  inputCh2:          int
        :type  inputCh3:          int
        :type  ch1_short_cutoff:  float
        :type  ch1_high_cutoff:   float
        :type  ch2_short_cutoff:  float
        :type  ch2_high_cutoff:   float
        :type  ch3_short_cutoff:  float
        :type  ch3_high_cutoff:   float
        :type  outputCh1:         int
        :type  outputCh2:         int
        :type  outputCh3:         int

        .. versionadded:: 2025.2.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** Use short wavelength = 0 for highpass.
        is simply copied to the output channel without filtering.       

        Ref: See the RPSFILT.GXC, RPSLEVLT.GXC, RPSLEVLU.GXC and RPSRATIO.GXC files
            for details and implementation of the algorithm.
        """
        
        gxapi_cy.WrapRPS._radio_element_bandpass_filter(GXContext._get_tls_geo(), db, line, inputCh1, inputCh2, inputCh3, ch1_short_cutoff, ch1_high_cutoff, ch2_short_cutoff, ch2_high_cutoff, ch3_short_cutoff, ch3_high_cutoff, outputCh1, outputCh2, outputCh3)
        



    @classmethod
    def radio_element_ratios(cls, db, line, K_in, U_in, Th_in, uk_ratio, uth_ratio, thk_ratio):
        """
        
        Calculate radioelement ratios
        
        :param db:         `GXDB <geosoft.gxapi.GXDB>` Object
        :param line:       Line to process (NULLSYMB for all selected lines)
        :param K_in:       Input filtered Postassium channel
        :param U_in:       Input filtered Uranium channel
        :param Th_in:      Input filtered Thorium channel
        :param uk_ratio:   Output Uranium/Potassium ratio channel name
        :param uth_ratio:  Output Uranium/Thorium ratio channel name
        :param thk_ratio:  Output Thorium/Potassium ratio channel name
        :type  db:         GXDB
        :type  line:       int
        :type  K_in:       str
        :type  U_in:       str
        :type  Th_in:      str
        :type  uk_ratio:   str
        :type  uth_ratio:  str
        :type  thk_ratio:  str

        .. versionadded:: 2025.2.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** The conversions are calculated using the formulae:

        OutputUKRatio = InputU /InputK
        OutputUThRatio = InputU / InputTh
        OutputThKRatio = InputTh /InputK

        where:

        InputK = Filtering Potassium
        InputU = Filtering Uranium
        InputTh = Filtering Thorium

        Ref: See the RPSRATIO.GXC file for details and implementation of the algorithm.
        """
        
        gxapi_cy.WrapRPS._radio_element_ratios(GXContext._get_tls_geo(), db, line, K_in.encode(), U_in.encode(), Th_in.encode(), uk_ratio.encode(), uth_ratio.encode(), thk_ratio.encode())
        



    @classmethod
    def radio_element_minimum_concentration_filter(cls, db, line, K, U, Th, potassium_percent, uranium_ppm, thorium_ppm, threshold_method):
        """
        
        Minimum Concentration Filtering
        
        :param db:                 `GXDB <geosoft.gxapi.GXDB>` Object
        :param line:               Line to process (NULLSYMB for all selected lines)
        :param K:                  Input/Output Postassium channel
        :param U:                  Input/Output Uranium channel
        :param Th:                 Input/Output Thorium channel
        :param potassium_percent:  Input min. potassium ratio (default: 1.0)
        :param uranium_ppm:        Input min. uranium ratio (default: 1.0)
        :param thorium_ppm:        Input min. thorium ratio (default: 1.0)
        :param threshold_method:   min. threshold method (0: Clip, 1: DUMMY)
        :type  db:                 GXDB
        :type  line:               int
        :type  K:                  str
        :type  U:                  str
        :type  Th:                 str
        :type  potassium_percent:  float
        :type  uranium_ppm:        float
        :type  thorium_ppm:        float
        :type  threshold_method:   int

        .. versionadded:: 2025.2.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** The conversions are calculated using the formulae: (Clip)
        if(( %s <= 0.0 || %s < %lf ) && %s != DUMMY)  %s = KMIN;
        if(( %s <= 0.0 || %s < %lf ) && %s != DUMMY)  %s = UMIN;
        if(( %s <= 0.0 || %s < %lf ) && %s != DUMMY)  %s = THMIN;


        The conversions are calculated using the formulae: (Dummy)
        if(( %s <= 0.0 || %s < %lf ) && %s != DUMMY)  %s = DUMMY;

        where:

        KMIN = Min Potassium in %K ppm (Default is 1.0)
        UMIN = Min Uranium in eU ppm (Default is 1.0)
        THMIN = Min Thorium in eTH ppm (Default is 1.0)

        Ref: See the RPSRATIO.GXC file for details and implementation of the algorithm.
        """
        
        gxapi_cy.WrapRPS._radio_element_minimum_concentration_filter(GXContext._get_tls_geo(), db, line, K.encode(), U.encode(), Th.encode(), potassium_percent, uranium_ppm, thorium_ppm, threshold_method)
        



    @classmethod
    def radio_element_ground_exposure_rate(cls, db, line, K, U, Th, Exposure):
        """
        
        Applies ground level exposure rate
        
        :param db:        `GXDB <geosoft.gxapi.GXDB>` Object
        :param line:      Line to process (NULLSYMB for all selected lines)
        :param K:         Input Potassium corrected channel
        :param U:         Input Uranium corrected channel
        :param Th:        Input Thorium corrected channel
        :param Exposure:  Output ground level exposure rate channel
        :type  db:        GXDB
        :type  line:      int
        :type  K:         str
        :type  U:         str
        :type  Th:        str
        :type  Exposure:  str

        .. versionadded:: 2025.2.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** Ground exposure rate gives the measure of the rate of ionizations
        produced in air by photon radiation, which is the amount of exposure received.       

        E = 1.505𝐾(%) + 0.653𝑒𝑈(𝑝𝑝𝑚)+ 0.287𝑒𝑇ℎ(𝑝𝑝𝑚) 

        where:

        𝐾 = Corrected Potassium
        𝑒𝑈 = Corrected Uranium
        𝑒𝑇ℎ = Corrected Thorium  

        Ref:  See the RPSCORR.GXC file for details and implementation of the algorithm.
        """
        
        gxapi_cy.WrapRPS._radio_element_ground_exposure_rate(GXContext._get_tls_geo(), db, line, K.encode(), U.encode(), Th.encode(), Exposure.encode())
        



    @classmethod
    def compress_spectrum(cls, va_dest, va_src, cosmic):
        """
        
        Represent a spectrum with a different number of bins
        
        :param va_dest:  `GXVA <geosoft.gxapi.GXVA>` to receive the compressed output
        :param va_src:   `GXVA <geosoft.gxapi.GXVA>` to compress
        :param cosmic:   Copy the cosmic counts bin without modification
        :type  va_dest:  GXVA
        :type  va_src:   GXVA
        :type  cosmic:   int

        .. versionadded:: 2026.1.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** In radiometric spectra, with n bins, the first n-1 bins represent counts from 0 to 3 MeV,
        while the last bin represents counts above 3 MeV (cosmic count). 
        This method uses fractional summation of bins to convert a spectrum with n bins into a spectrum with m bins,
        while maintaining the original 0 to 3 MeV range in the first m-1 bins and the cosmic count in the last bin.
        This method works even if n is not a multiple of m, or if n is less than m.
        """
        
        gxapi_cy.WrapRPS._compress_spectrum(GXContext._get_tls_geo(), va_dest, va_src, cosmic)
        



    @classmethod
    def stabilize_spectra(cls, db, line, data_channel, mcf_file, A1_channel, AverageSpectrum_channel, output_channel):
        """
        
        Calculate the A1 stabilization factor and output the stabilized spectra used for Full Spectrum Analysis
        
        :param db:                       `GXDB <geosoft.gxapi.GXDB>` Object
        :param line:                     Line to process (NULLSYMB for all selected lines)
        :param data_channel:             Input (unstabilized) spectrum channel name
        :param mcf_file:                 MCF file
        :param A1_channel:               Output A1 factor channel name (optional, can be blank)
        :param AverageSpectrum_channel:  Output averaged spectrum   channel name (optional, can be blank)
        :param output_channel:           Output (stabilized) spectrum channel name
        :type  db:                       GXDB
        :type  line:                     int
        :type  data_channel:             str
        :type  mcf_file:                 str
        :type  A1_channel:               str
        :type  AverageSpectrum_channel:  str
        :type  output_channel:           str

        .. versionadded:: 2026.1.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** Calculate the A1 stabilization factor and output the stabilized spectra used for Full Spectrum Analysis.
        The stabilization factor is calculated on a per-line basis. 
        The number of array elements in the output stabilized spectrum channel is less than the number of elements in the input
        """
        
        gxapi_cy.WrapRPS._stabilize_spectra(GXContext._get_tls_geo(), db, line, data_channel.encode(), mcf_file.encode(), A1_channel.encode(), AverageSpectrum_channel.encode(), output_channel.encode())
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block

### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer