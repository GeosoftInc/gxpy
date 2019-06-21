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
class GXGU(gxapi_cy.WrapGU):
    """
    GXGU class.

    Not a class. A catch-all group of functions performing
    various geophysical processes, including the calculation
    of simple EM model responses, certain instrument dump
    file imports, and 2D Euler deconvolution.
    """

    def __init__(self, handle=0):
        super(GXGU, self).__init__(GXContext._get_tls_geo(), handle)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of `GXGU <geosoft.gxapi.GXGU>`
        
        :returns: A null `GXGU <geosoft.gxapi.GXGU>`
        :rtype:   GXGU
        """
        return GXGU()

    def is_null(self):
        """
        Check if this is a null (undefined) instance
        
        :returns: True if this is a null (undefined) instance, False otherwise.
        :rtype:   bool
        """
        return self._internal_handle() == 0



# Miscellaneous


    @classmethod
    def dipole_mag(cls, xyz_file, depth, inc, nx, ny, dx, dy):
        """
        Calculate a dipole magnetic field into XYZ file
        
        :param xyz_file:  sXYZ
        :param depth:     rDepth
        :param inc:       rInc
        :param nx:        iNX
        :param ny:        iNY
        :param dx:        rDX
        :param dy:        rDY
        :type  xyz_file:  str
        :type  depth:     float
        :type  inc:       float
        :type  nx:        int
        :type  ny:        int
        :type  dx:        float
        :type  dy:        float

        .. versionadded:: 5.1.6

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        gxapi_cy.WrapGU._dipole_mag(GXContext._get_tls_geo(), xyz_file.encode(), depth, inc, nx, ny, dx, dy)
        



    @classmethod
    def em_half_space_inv(cls, coil_spacing, coil_frequency, coil_configuration, tol, threshold, vv_height, vv_in_phase, vv_quadrature, vv_res, inv, err, start_val):
        """
        Inverts EM responses to the best halfspace model.
        
        :param coil_spacing:        Coil spacing: error if == 0
        :param coil_frequency:      Frequency
        :param coil_configuration:  :ref:`EMLAY_GEOMETRY`
        :param tol:                 Fractional error in best fit resistivity
        :param threshold:           Don't invert values below this
        :param vv_height:           Height above ground
        :param vv_in_phase:         In-phase part (ppm)
        :param vv_quadrature:       Quadrature part (ppm)
        :param vv_res:              On return - inverted halfspace resistivities
        :param inv:                 :ref:`EM_INV`
        :param err:                 :ref:`EM_ERR`
        :param start_val:           Starting value for inversion (can be `rDUMMY <geosoft.gxapi.rDUMMY>`)
        :type  coil_spacing:        float
        :type  coil_frequency:      float
        :type  coil_configuration:  int
        :type  tol:                 float
        :type  threshold:           float
        :type  vv_height:           GXVV
        :type  vv_in_phase:         GXVV
        :type  vv_quadrature:       GXVV
        :type  vv_res:              GXVV
        :type  inv:                 int
        :type  err:                 int
        :type  start_val:           float

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        gxapi_cy.WrapGU._em_half_space_inv(GXContext._get_tls_geo(), coil_spacing, coil_frequency, coil_configuration, tol, threshold, vv_height, vv_in_phase, vv_quadrature, vv_res, inv, err, start_val)
        



    @classmethod
    def em_half_space_vv(cls, coil_spacing, coil_frequency, coil_configuration, rvv, hvv, ivv, qvv):
        """
        EM Halfspace forward model response.
        
        :param coil_spacing:        Coil separation
        :param coil_frequency:      Frequency
        :param coil_configuration:  :ref:`EMLAY_GEOMETRY`
        :param rvv:                 Input resistivity values
        :param hvv:                 Input height values
        :param ivv:                 Output In-phase
        :param qvv:                 Output Quadrature-phase
        :type  coil_spacing:        float
        :type  coil_frequency:      float
        :type  coil_configuration:  int
        :type  rvv:                 GXVV
        :type  hvv:                 GXVV
        :type  ivv:                 GXVV
        :type  qvv:                 GXVV

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        gxapi_cy.WrapGU._em_half_space_vv(GXContext._get_tls_geo(), coil_spacing, coil_frequency, coil_configuration, rvv, hvv, ivv, qvv)
        



    @classmethod
    def geometrics2_db(cls, db, ra, log_wa, survey_mode, line_dir, corner, bi_uni, corner_x, corner_y, mark_space, line_space):
        """
        Convert a Geometrics STN file to a database.
        
        :param db:           `GXDB <geosoft.gxapi.GXDB>` handle
        :param ra:           `GXRA <geosoft.gxapi.GXRA>` handle, STN file
        :param log_wa:       Log file `GXWA <geosoft.gxapi.GXWA>` handle
        :param survey_mode:  Simple mode (1) or Mapped mode (2)
        :param line_dir:     Survey line orientation:  North-south - 0 East-west   - 1
        :param corner:       Starting survey position: SW - 0, NW - 1, SE - 2, NE - 3,
        :param bi_uni:       Bidirectional (0) or Unidirectional (1)
        :param corner_x:     Starting position X
        :param corner_y:     Starting position Y
        :param mark_space:   Mark spacing
        :param line_space:   Line spacing
        :type  db:           GXDB
        :type  ra:           GXRA
        :type  log_wa:       GXWA
        :type  survey_mode:  int
        :type  line_dir:     int
        :type  corner:       int
        :type  bi_uni:       int
        :type  corner_x:     float
        :type  corner_y:     float
        :type  mark_space:   float
        :type  line_space:   float

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** Assumes that the database is new and empty. If not, existing channels
        with names X, Y, Mag1, Mag2, Time, Date, and Mark will deleted and then created.  
        Existing lines will be erased and then created if they are the same as the new ones.
        """
        gxapi_cy.WrapGU._geometrics2_db(GXContext._get_tls_geo(), db, ra, log_wa, survey_mode, line_dir, corner, bi_uni, corner_x, corner_y, mark_space, line_space)
        



    @classmethod
    def geometrics2_tbl(cls, ra, wa, log_wa):
        """
        Convert a Geometrics station file (STN) to a table file (TBL)
        
        :param ra:      `GXRA <geosoft.gxapi.GXRA>` handle, input station file
        :param wa:      Output TBL file
        :param log_wa:  Log file `GXWA <geosoft.gxapi.GXWA>` handle
        :type  ra:      GXRA
        :type  wa:      GXWA
        :type  log_wa:  GXWA

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        gxapi_cy.WrapGU._geometrics2_tbl(GXContext._get_tls_geo(), ra, wa, log_wa)
        



    @classmethod
    def geometrics_qc(cls, wa, line, in_vv, tol, min_coord, max_coord, out_vv, flag_vv):
        """
        Correct reading positions in a database.
        
        :param wa:         Output error log file
        :param line:       Database line number. For output to log file only
        :param in_vv:      Input `GXVV <geosoft.gxapi.GXVV>`, `GS_DOUBLE <geosoft.gxapi.GS_DOUBLE>`
        :param tol:        Tolerance defined as percentage, say 50.0 means 50%. Must be >=0.0 Lower bound = (Normal Density) - (Normal Density)*Tolerance Upper bound = (Normal Density) + (Normal Density)*Tolerance
        :param min_coord:  Minimum coordinate (X or Y)
        :param max_coord:  Maximum coordinate (X or Y)
        :param out_vv:     Output `GXVV <geosoft.gxapi.GXVV>`, `GS_DOUBLE <geosoft.gxapi.GS_DOUBLE>`
        :param flag_vv:    Output Flag `GXVV <geosoft.gxapi.GXVV>`, `GS_LONG <geosoft.gxapi.GS_LONG>`
        :type  wa:         GXWA
        :type  line:       str
        :type  in_vv:      GXVV
        :type  tol:        float
        :type  min_coord:  float
        :type  max_coord:  float
        :type  out_vv:     GXVV
        :type  flag_vv:    GXVV

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** There are six cases to consider:

        ========    ====  =============  ========================================
        Case        Flag  Solutions      Symptoms
        ========    ====  =============  ========================================
        CASE 1A:    0     No correction  Recorded and actual Line lengths same
                                         Reading densities vary slightly (passed
                                         the tolerance test)
        --------    ----  -------------  ----------------------------------------
        CASE 1B     -1    No correction  Line lengths same
                                         Reading densities vary and cannot
                                         pass the tolerance test
        --------    ----  -------------  ----------------------------------------
        CASE 2A     1     Corrected by   Recorded line length too short
                          extension      Possible high readings in segment(s)
                                         Corrected (by extending) and actual
                                         lengths become the same
        --------    ----  -------------  ----------------------------------------
        CASE 2B     2     Corrected by   Recorded line length too short
                          interpolation  Possible high readings in segment(s)
                                         Corrected (by extending) and actual
                                         lengths are not same. Interpolation is
                                         then applied
        --------    ----  -------------  ----------------------------------------
        CASE 3A     1     Corrected by   Recorded line length too long
                          shifting or    Possible low readings in segment(s)
                          (shrank)       Corrected (by shifting) and actual
                                         lengths are same
        --------    ----  -------------  ----------------------------------------
        CASE 3B     2     Corrected by   Recorded line length too long
                          interpolation  Possible low readings in segment(s)
                                         Corrected (by shifting) and actual
                                         lengths are not same. Interpolation
                                         is then applied
        ========    ====  =============  ========================================


        TERMINOLOGY:

        Segments
             A segment refers to the distance and its contents between
             two adjacent fiducial markers

        Normal Density
             The density (number of readings) shared by the segments in
             a survey line. The number of segments with the density is greater 
             than the number of segments having a different density in a line.

        Tolerance and Bound:
             Tolerance is defined as a percentage, say ``50% (=0.5)``.
             Based on the tolerance, a lower bound and upper bound

             can be defined:

             ::

                 Lower bound = (Normal Density) - (Normal Density)*Tolerance
                 Upper bound = (Normal Density) - (Normal Density)*Tolerance

             Segments will pass the tolerance test if the number of readings
             falls within the Lower and Upper Bounds.
        """
        gxapi_cy.WrapGU._geometrics_qc(GXContext._get_tls_geo(), wa, line.encode(), in_vv, tol, min_coord, max_coord, out_vv, flag_vv)
        



    @classmethod
    def geonics3138_dump2_db(cls, db, r_ah, r_ad, log_wa, line_mult, stat_mult):
        """
        Convert a Geonics EM31/EM38 file in dump format to a database.
        
        :param db:         `GXDB <geosoft.gxapi.GXDB>` handle
        :param r_ah:       `GXRA <geosoft.gxapi.GXRA>` handle, Header file
        :param r_ad:       `GXRA <geosoft.gxapi.GXRA>` handle, Dump file
        :param log_wa:     Log file `GXWA <geosoft.gxapi.GXWA>` handle
        :param line_mult:  Line multiplier
        :param stat_mult:  Station multiplier
        :type  db:         GXDB
        :type  r_ah:       GXRA
        :type  r_ad:       GXRA
        :type  log_wa:     GXWA
        :type  line_mult:  float
        :type  stat_mult:  float

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** Assumes that the database is new and empty. If not, existing channels
        with names X, Y, Station, Conductivity, Inphase, Quadrature,
        and Time will deleted and then created.  Existing lines will
        be erased and then created if they are the same as the new ones.
        """
        gxapi_cy.WrapGU._geonics3138_dump2_db(GXContext._get_tls_geo(), db, r_ah, r_ad, log_wa, line_mult, stat_mult)
        



    @classmethod
    def geonics61_dump2_db(cls, db, ra, log_wa, line_mult, stat_mult):
        """
        Convert a Geonics EM61 file in dump format to a database.
        
        :param db:         `GXDB <geosoft.gxapi.GXDB>` handle
        :param ra:         `GXRA <geosoft.gxapi.GXRA>` handle, dump file
        :param log_wa:     Log file `GXWA <geosoft.gxapi.GXWA>` handle
        :param line_mult:  Line multiplier
        :param stat_mult:  Station multiplier - Not used in the calculation
        :type  db:         GXDB
        :type  ra:         GXRA
        :type  log_wa:     GXWA
        :type  line_mult:  float
        :type  stat_mult:  float

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** Assumes that the database is new and empty. If not, existing channels
        with names X, Y, Station, Conductivity, Inphase, Quadrature,
        and Time will deleted and then created.  Existing lines will
        be erased and then created if they are the same as the new ones.
        """
        gxapi_cy.WrapGU._geonics61_dump2_db(GXContext._get_tls_geo(), db, ra, log_wa, line_mult, stat_mult)
        



    @classmethod
    def geonics_dat2_db(cls, db, ra, log_wa, line_mult, stat_mult):
        """
        Convert a Geonics EM31/EM38/EM61 file in `GXDAT <geosoft.gxapi.GXDAT>` format to a database.
        
        :param db:         `GXDB <geosoft.gxapi.GXDB>` handle
        :param ra:         `GXRA <geosoft.gxapi.GXRA>` handle
        :param log_wa:     Log file `GXWA <geosoft.gxapi.GXWA>` handle
        :param line_mult:  Line multiplier
        :param stat_mult:  Station multiplier - Not used in the calculation
        :type  db:         GXDB
        :type  ra:         GXRA
        :type  log_wa:     GXWA
        :type  line_mult:  float
        :type  stat_mult:  float

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** Assumes that the database is new and empty. If not, existing channels
        with names X, Y, Station, Conductivity, Inphase, Quadrature,
        and Time will deleted and then created.  Existing lines will
        be erased and then created if they are the same as the new ones.
        """
        gxapi_cy.WrapGU._geonics_dat2_db(GXContext._get_tls_geo(), db, ra, log_wa, line_mult, stat_mult)
        



    @classmethod
    def gr_curv_cor(cls, vv_elev, vv_lat, vv_boug):
        """
        Gravity Curvature (Bullard B) Correction to Bouguer anomaly
        
        :param vv_elev:  Input Elevation `GXVV <geosoft.gxapi.GXVV>`
        :param vv_lat:   Input Latitude `GXVV <geosoft.gxapi.GXVV>`
        :param vv_boug:  Bouguer `GXVV <geosoft.gxapi.GXVV>` for Curvature Correction
        :type  vv_elev:  GXVV
        :type  vv_lat:   GXVV
        :type  vv_boug:  GXVV

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        gxapi_cy.WrapGU._gr_curv_cor(GXContext._get_tls_geo(), vv_elev, vv_lat, vv_boug)
        



    @classmethod
    def gr_curv_cor_ex(cls, vv_elev, vv_lat, vv_boug, rho):
        """
        Gravity Curvature (Bullard B) Correction to Bouguer anomaly, with user input cap density.
        
        :param vv_elev:  Input Elevation `GXVV <geosoft.gxapi.GXVV>`
        :param vv_lat:   Input Latitude `GXVV <geosoft.gxapi.GXVV>`
        :param vv_boug:  Bouguer `GXVV <geosoft.gxapi.GXVV>` for Curvature Correction
        :param rho:      Cap Density (g/cm^3
        :type  vv_elev:  GXVV
        :type  vv_lat:   GXVV
        :type  vv_boug:  GXVV
        :type  rho:      float

        .. versionadded:: 8.0.1

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        gxapi_cy.WrapGU._gr_curv_cor_ex(GXContext._get_tls_geo(), vv_elev, vv_lat, vv_boug, rho)
        



    @classmethod
    def gr_demvv(cls, im_gdem, vv_x, vv_y, vv_z):
        """
        Get gravity DEM grid `GXVV <geosoft.gxapi.GXVV>` for Bouguer anomaly
        
        :param im_gdem:  DEM grid
        :param vv_x:     Input X `GXVV <geosoft.gxapi.GXVV>`
        :param vv_y:     Input Y `GXVV <geosoft.gxapi.GXVV>`
        :param vv_z:     Output DEM `GXVV <geosoft.gxapi.GXVV>` for Bouguer Correction
        :type  im_gdem:  GXIMG
        :type  vv_x:     GXVV
        :type  vv_y:     GXVV
        :type  vv_z:     GXVV

        .. versionadded:: 6.2

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        gxapi_cy.WrapGU._gr_demvv(GXContext._get_tls_geo(), im_gdem, vv_x, vv_y, vv_z)
        



    @classmethod
    def gr_test(cls, xm, ym, zm, vv_x, vv_y, vv_g3, vv_g4, vv_g1, vv_g2):
        """
        Test triangular prism gravity calculation
        
        :param xm:     dXm  - model dimension x
        :param ym:     dYm  - model dimension y
        :param zm:     dZm  - model depth
        :param vv_x:   VVx  - stations x
        :param vv_y:   VVy  - stations y
        :param vv_g3:  VVg3 - 2 triangular prism gravity results
        :param vv_g4:  VVg4 - regtangular prism gravity results
        :param vv_g1:  VVg1 - lower triangular prism gravity results
        :param vv_g2:  VVg2 - upper triangular prism gravity results
        :type  xm:     float
        :type  ym:     float
        :type  zm:     float
        :type  vv_x:   GXVV
        :type  vv_y:   GXVV
        :type  vv_g3:  GXVV
        :type  vv_g4:  GXVV
        :type  vv_g1:  GXVV
        :type  vv_g2:  GXVV

        .. versionadded:: 5.1.4

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        gxapi_cy.WrapGU._gr_test(GXContext._get_tls_geo(), xm, ym, zm, vv_x, vv_y, vv_g3, vv_g4, vv_g1, vv_g2)
        



    @classmethod
    def gravity_still_reading_correction(cls, db, grav_in, date, time, still, grav_out):
        """
        Gravity Still Reading Correction on selected lines.
        
        :param db:        Database
        :param grav_in:   Input gravity channel handle [`DB_LOCK_READONLY <geosoft.gxapi.DB_LOCK_READONLY>`]
        :param date:      Input date channel handle [`DB_LOCK_READONLY <geosoft.gxapi.DB_LOCK_READONLY>`]
        :param time:      Input time channel handle [`DB_LOCK_READONLY <geosoft.gxapi.DB_LOCK_READONLY>`]
        :param still:     Still readings file
        :param grav_out:  Output gravity channel handle [`DB_LOCK_READWRITE <geosoft.gxapi.DB_LOCK_READWRITE>`]
        :type  db:        GXDB
        :type  grav_in:   int
        :type  date:      int
        :type  time:      int
        :type  still:     str
        :type  grav_out:  int

        .. versionadded:: 8.5

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        gxapi_cy.WrapGU._gravity_still_reading_correction(GXContext._get_tls_geo(), db, grav_in, date, time, still.encode(), grav_out)
        



    @classmethod
    def despike_em_array(cls, vv_in, vv_noise, vv_out, num_removed):
        """
        Despike a time-series with individual noise levels
        
        :param vv_in:        `GXVV <geosoft.gxapi.GXVV>` input time series)
        :param vv_noise:     `GXVV <geosoft.gxapi.GXVV>` individual noise values)
        :param vv_out:       `GXVV <geosoft.gxapi.GXVV>` despiked output time series
        :param num_removed:  Number of spikes removed - returned
        :type  vv_in:        GXVV
        :type  vv_noise:     GXVV
        :type  vv_out:       GXVV
        :type  num_removed:  int_ref

        .. versionadded:: 9.5

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** Remove spikes from a single EM time-series decay curve. Each point has its own noise level.
        The algorithm is to be determined.
        """
        num_removed.value = gxapi_cy.WrapGU._despike_em_array(GXContext._get_tls_geo(), vv_in, vv_noise, vv_out, num_removed.value)
        



    @classmethod
    def em_layer(cls, coil_spacing, coil_frequency, coil_height, coil_configuration, n_layers, vv_thickness, vv_sigma, in_phase, quadrature):
        """
        Calculate the EM response of a layered earth model.
        
        :param coil_spacing:        Coil spacing, error if == 0
        :param coil_frequency:      Coil frequency
        :param coil_height:         Coil height above layer [0]
        :param coil_configuration:  :ref:`EMLAY_GEOMETRY`
        :param n_layers:            Number of layers (including lower halfspace)
        :param vv_thickness:        sNLayer-1 thicknesses  [0] to [sNLayer-2]
        :param vv_sigma:            sNLayer conductivities [0] to [sNLayer-1]
        :param in_phase:            On return - in-phase part (ppm)
        :param quadrature:          On return - quadrature part (ppm)
        :type  coil_spacing:        float
        :type  coil_frequency:      float
        :type  coil_height:         float
        :type  coil_configuration:  int
        :type  n_layers:            int
        :type  vv_thickness:        GXVV
        :type  vv_sigma:            GXVV
        :type  in_phase:            float_ref
        :type  quadrature:          float_ref

        :returns:                   0 of OK
                                    1 if some error
        :rtype:                     int

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        ret_val, in_phase.value, quadrature.value = gxapi_cy.WrapGU._em_layer(GXContext._get_tls_geo(), coil_spacing, coil_frequency, coil_height, coil_configuration, n_layers, vv_thickness, vv_sigma, in_phase.value, quadrature.value)
        return ret_val



    @classmethod
    def em_plate(cls, strike_length, dip_length, strike, dip, plunge, x_off, y_off, z_off, plate_depth, n_spons, sig_tvv, tx_orient, tx_freq, tx_dt, params, xivv, yivv, zivv, xqvv, yqvv, zqvv):
        """
        Calculate the conductance of a thin plate model.
        
        :param strike_length:  Plate strike length (m)
        :param dip_length:     Plate dip length (m)
        :param strike:         Plate strike (degrees) from X axis
        :param dip:            Plate dip (degrees) from horizontal
        :param plunge:         Plate plunge (degrees) from horizontal
        :param x_off:          Rx offset in X from Tx
        :param y_off:          Rx offset in Y from Tx
        :param z_off:          Rx offset in Z from Tx (+'ve down)
        :param plate_depth:    Depth below Tx
        :param n_spons:        :ref:`EMPLATE_DOMAIN`
        :param sig_tvv:        The plate conductances (`GXVV <geosoft.gxapi.GXVV>` length <= 100)
        :param tx_orient:      :ref:`EMPLATE_TX`
        :param tx_freq:        Tx frequency (for `EMPLATE_TIME <geosoft.gxapi.EMPLATE_TIME>`)
        :param tx_dt:          Tx time window spacing (for `EMPLATE_TIME <geosoft.gxapi.EMPLATE_TIME>`)
        :param params:         The frequency/time parameters (SI units: f[Hz] or t[s])
        :param xivv:           On return - X in-phase part (ppm)
        :param yivv:           On return - Y in-phase part (ppm)
        :param zivv:           On return - Z in-phase part (ppm)
        :param xqvv:           On return - X quadrature part (ppm)
        :param yqvv:           On return - Y quadrature part (ppm)
        :param zqvv:           On return - Z quadrature part (ppm)
        :type  strike_length:  float
        :type  dip_length:     float
        :type  strike:         float
        :type  dip:            float
        :type  plunge:         float
        :type  x_off:          float
        :type  y_off:          float
        :type  z_off:          float
        :type  plate_depth:    float
        :type  n_spons:        int
        :type  sig_tvv:        GXVV
        :type  tx_orient:      int
        :type  tx_freq:        float
        :type  tx_dt:          float
        :type  params:         float
        :type  xivv:           GXVV
        :type  yivv:           GXVV
        :type  zivv:           GXVV
        :type  xqvv:           GXVV
        :type  yqvv:           GXVV
        :type  zqvv:           GXVV

        :returns:              0 of OK
                               1 if some error
        :rtype:                int

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        ret_val = gxapi_cy.WrapGU._em_plate(GXContext._get_tls_geo(), strike_length, dip_length, strike, dip, plunge, x_off, y_off, z_off, plate_depth, n_spons, sig_tvv, tx_orient, tx_freq, tx_dt, params, xivv, yivv, zivv, xqvv, yqvv, zqvv)
        return ret_val



    @classmethod
    def gen_ux_detect_symbols_group_name(cls, target_gdb, targets, ostr):
        """
        Generate a group name string for UX-Detect symbols
        
        :param target_gdb:  Input Targets database name
        :param targets:     Input Targets group (line) name
        :param ostr:        Output group name string
        :type  target_gdb:  str
        :type  targets:     str
        :type  ostr:        str_ref

        .. versionadded:: 6.3

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Start a new group for the symbols in the UX-Detect system.
        The Target GDB is often in the form "GDB_Targets", where
        "GDB" is the original data. Cut off the part including the
        underscore when creating the map, so you don't get map group
        Names like "SYMBOLS_UxData_Targets_Targets".

        .. seealso::

            `GXSTR.gen_group_name <geosoft.gxapi.GXSTR.gen_group_name>`
        """
        ostr.value = gxapi_cy.WrapGU._gen_ux_detect_symbols_group_name(GXContext._get_tls_geo(), target_gdb.encode(), targets.encode(), ostr.value.encode())
        



    @classmethod
    def import_daarc500_ethernet(cls, file, output, bytes):
        """
        Import Ethernet data from the RMS Instruments DAARC500.
        
        :param file:    File to import
        :param output:  Output binary file
        :param bytes:   Returned number of bytes per block
        :type  file:    str
        :type  output:  str
        :type  bytes:   int_ref

        .. versionadded:: 7.2

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Imports Ethernet data recorded
        by the RMS Instruments DAARC500 instrument, and outputs the data
        to a new binary file, returning the number of bytes per
        block, to make it easier to import the data using the regular binary import.
        """
        bytes.value = gxapi_cy.WrapGU._import_daarc500_ethernet(GXContext._get_tls_geo(), file.encode(), output.encode(), bytes.value)
        



    @classmethod
    def import_daarc500_serial(cls, file, channel, output, bytes):
        """
        Import Serial data from the RMS Instruments DAARC500.
        
        :param file:     File to import
        :param channel:  Channel to import, 1-8
        :param output:   Output binary file
        :param bytes:    Returned number of bytes per block
        :type  file:     str
        :type  channel:  int
        :type  output:   str
        :type  bytes:    int_ref

        .. versionadded:: 7.2

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Imports a single channel of the up to 8 serial data channels recorded
        by the RMS Instruments DAARC500 instrument, and outputs the data for
        that channel to a new binary file, returning the number of bytes per
        block, to make it easier to import the data using the regular binary import.
        """
        bytes.value = gxapi_cy.WrapGU._import_daarc500_serial(GXContext._get_tls_geo(), file.encode(), channel, output.encode(), bytes.value)
        



    @classmethod
    def import_p190(cls, db, file, rec_type, wa):
        """
        Import navigation data in the P190 format.
        
        :param db:        Database handle
        :param file:      P190 file name
        :param rec_type:  Single letter code, e.g. "C", "E", "S", "T" or "V", or blank for all records.
        :param wa:        Log file
        :type  db:        GXDB
        :type  file:      str
        :type  rec_type:  str
        :type  wa:        GXWA

        .. versionadded:: 6.3

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** Imports the data, and, if projection information is included
        set the "X" and "Y" channel projection info. (Note: the last file
        imported always takes precedence).
        Different record types are imported to separate lines, but in the
        same order as in the file. Data in existing lines is overwritten.
        If the record type is specified, only records beginning with that
        letter are imported, otherwise all records (except for the header "H"
        records) are imported.
        """
        gxapi_cy.WrapGU._import_p190(GXContext._get_tls_geo(), db, file.encode(), rec_type.encode(), wa)
        



    @classmethod
    def lag_daarc500_gps(cls, mag_fid_vv, mag_event_vv, gps_fid_vv):
        """
        Lag the GPS fid values for the DAARC500 import.
        
        :param mag_fid_vv:    Mag fid values   (`GS_DOUBLE <geosoft.gxapi.GS_DOUBLE>`)
        :param mag_event_vv:  Mag event values (`GS_LONG <geosoft.gxapi.GS_LONG>`)
        :param gps_fid_vv:    GPS fid values (`GS_DOUBLE <geosoft.gxapi.GS_DOUBLE>`, altered on return)
        :type  mag_fid_vv:    GXVV
        :type  mag_event_vv:  GXVV
        :type  gps_fid_vv:    GXVV

        .. versionadded:: 7.2

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** The fiducial times recorded for the GPS in the RMS Instrument DAARC500
        are delayed, and associated with the "wrong" fid value. They should actually
        be moved to the previous fid value in the mag data where the event flag is non-zero.
        """
        gxapi_cy.WrapGU._lag_daarc500_gps(GXContext._get_tls_geo(), mag_fid_vv, mag_event_vv, gps_fid_vv)
        



    @classmethod
    def maxwell_plate_corners(cls, x, y, z, dip, dip_dir, plunge, length, width, x1, y1, z1, x2, y2, z2, x3, y3, z3, x4, y4, z4):
        """
        Calculate the corner point locations for a Maxwell Plate.
        
        :param x:        Top-center point, X
        :param y:        Top-center point, Y
        :param z:        Top-center point, Z
        :param dip:      Dip
        :param dip_dir:  Dip-direction
        :param plunge:   Plunge
        :param length:   Length
        :param width:    Width (height)
        :param x1:       [returned] Corner 1 X
        :param y1:       [returned] Corner 1 Y
        :param z1:       [returned] Corner 1 Z
        :param x2:       [returned] Corner 2 X
        :param y2:       [returned] Corner 2 Y
        :param z2:       [returned] Corner 2 Z
        :param x3:       [returned] Corner 3 X
        :param y3:       [returned] Corner 3 Y
        :param z3:       [returned] Corner 3 Z
        :param x4:       [returned] Corner 4 X
        :param y4:       [returned] Corner 4 Y
        :param z4:       [returned] Corner 4 Z
        :type  x:        float
        :type  y:        float
        :type  z:        float
        :type  dip:      float
        :type  dip_dir:  float
        :type  plunge:   float
        :type  length:   float
        :type  width:    float
        :type  x1:       float_ref
        :type  y1:       float_ref
        :type  z1:       float_ref
        :type  x2:       float_ref
        :type  y2:       float_ref
        :type  z2:       float_ref
        :type  x3:       float_ref
        :type  y3:       float_ref
        :type  z3:       float_ref
        :type  x4:       float_ref
        :type  y4:       float_ref
        :type  z4:       float_ref

        .. versionadded:: 6.1

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** This routine calculates the corner locations of plates defined in the Maxwell Plate
        program, given the top-center location and plate geometry parameters.
        """
        x1.value, y1.value, z1.value, x2.value, y2.value, z2.value, x3.value, y3.value, z3.value, x4.value, y4.value, z4.value = gxapi_cy.WrapGU._maxwell_plate_corners(GXContext._get_tls_geo(), x, y, z, dip, dip_dir, plunge, length, width, x1.value, y1.value, z1.value, x2.value, y2.value, z2.value, x3.value, y3.value, z3.value, x4.value, y4.value, z4.value)
        



    @classmethod
    def scan_daarc500_ethernet(cls, file, type, items):
        """
        Scan Ethernet data from the RMS Instruments DAARC500.
        
        :param file:   File to import
        :param type:   Recognized type
        :param items:  Number of items
        :type  file:   str
        :type  type:   int_ref
        :type  items:  int_ref

        .. versionadded:: 7.2

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Scans the file to see what data type is in the Ethernet file.
        Currently only detects GR820 types.
        """
        type.value, items.value = gxapi_cy.WrapGU._scan_daarc500_ethernet(GXContext._get_tls_geo(), file.encode(), type.value, items.value)
        



    @classmethod
    def scan_daarc500_serial(cls, file, vv_type, vv_items):
        """
        Scan Serial data from the RMS Instruments DAARC500.
        
        :param file:      File to import
        :param vv_type:   8 Recognized types - `GS_LONG <geosoft.gxapi.GS_LONG>`
        :param vv_items:  8 Numbers of items - `GS_LONG <geosoft.gxapi.GS_LONG>`
        :type  file:      str
        :type  vv_type:   GXVV
        :type  vv_items:  GXVV

        .. versionadded:: 7.2

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Scans the file to see which of the 8 serial channels were used to store data.
        """
        gxapi_cy.WrapGU._scan_daarc500_serial(GXContext._get_tls_geo(), file.encode(), vv_type, vv_items)
        



    @classmethod
    def vv_euler(cls, vv_xin, vv_yin, img_data, imgx, imgy, imgz, vv_xout, vv_yout, vv_depth, vvdc, vv_zer, vvx_yer, wnd_sz, si, wt_pow, x_yfit):
        """
        Get Euler solutions of depth from VVs and grids.
        
        :param vv_xin:    Input X `GXVV <geosoft.gxapi.GXVV>`
        :param vv_yin:    Input Y `GXVV <geosoft.gxapi.GXVV>`
        :param img_data:  Field grid
        :param imgx:      dF/dX grid
        :param imgy:      dF/dY grid
        :param imgz:      dF/dZ grid
        :param vv_xout:   Output X `GXVV <geosoft.gxapi.GXVV>`
        :param vv_yout:   Output Y `GXVV <geosoft.gxapi.GXVV>`
        :param vv_depth:  Output depth `GXVV <geosoft.gxapi.GXVV>`
        :param vvdc:      Output background field `GXVV <geosoft.gxapi.GXVV>`
        :param vv_zer:    Output depth uncertainty `GXVV <geosoft.gxapi.GXVV>`
        :param vvx_yer:   Output XY uncertainty `GXVV <geosoft.gxapi.GXVV>`
        :param wnd_sz:    Window size
        :param si:        Structure index
        :param wt_pow:    Weighting factor
        :param x_yfit:    :ref:`PEAKEULER_XY`
        :type  vv_xin:    GXVV
        :type  vv_yin:    GXVV
        :type  img_data:  GXIMG
        :type  imgx:      GXIMG
        :type  imgy:      GXIMG
        :type  imgz:      GXIMG
        :type  vv_xout:   GXVV
        :type  vv_yout:   GXVV
        :type  vv_depth:  GXVV
        :type  vvdc:      GXVV
        :type  vv_zer:    GXVV
        :type  vvx_yer:   GXVV
        :type  wnd_sz:    int
        :type  si:        float
        :type  wt_pow:    float
        :type  x_yfit:    int

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** All VVs must be REAL

        The output X and Y values are the same as the inputs,
        except if `PEAKEULER_XY_FIT <geosoft.gxapi.PEAKEULER_XY_FIT>` is selected. All other
        output values are set to dummy if:

             a) The input X or Y is a dummy
             b) The derived window size is a dummy.
             c) The derived solution is outside the range
             d) The solution is invalid (singular matrix)
        """
        gxapi_cy.WrapGU._vv_euler(GXContext._get_tls_geo(), vv_xin, vv_yin, img_data, imgx, imgy, imgz, vv_xout, vv_yout, vv_depth, vvdc, vv_zer, vvx_yer, wnd_sz, si, wt_pow, x_yfit)
        



    @classmethod
    def vv_euler2(cls, vv_xin, vv_yin, img_data, imgx, imgy, imgz, vv_xout, vv_yout, vv_depth, vvdc, vv_zer, vvx_yer, vv_wnd, si, wt_pow, x_yfit):
        """
        Get Euler solutions of depth from VVs and grids (method 2).
        
        :param vv_xin:    Input X `GXVV <geosoft.gxapi.GXVV>`
        :param vv_yin:    Input Y `GXVV <geosoft.gxapi.GXVV>`
        :param img_data:  Field grid
        :param imgx:      dF/dX grid
        :param imgy:      dF/dY grid
        :param imgz:      dF/dZ grid
        :param vv_xout:   Output X `GXVV <geosoft.gxapi.GXVV>`
        :param vv_yout:   Output Y `GXVV <geosoft.gxapi.GXVV>`
        :param vv_depth:  Output depth `GXVV <geosoft.gxapi.GXVV>`
        :param vvdc:      Output background field `GXVV <geosoft.gxapi.GXVV>`
        :param vv_zer:    Output depth uncertainty `GXVV <geosoft.gxapi.GXVV>`
        :param vvx_yer:   Output XY uncertainty `GXVV <geosoft.gxapi.GXVV>`
        :param vv_wnd:    Window size (diameters of targets)
        :param si:        Structure index
        :param wt_pow:    Weighting factor
        :param x_yfit:    :ref:`PEAKEULER_XY`
        :type  vv_xin:    GXVV
        :type  vv_yin:    GXVV
        :type  img_data:  GXIMG
        :type  imgx:      GXIMG
        :type  imgy:      GXIMG
        :type  imgz:      GXIMG
        :type  vv_xout:   GXVV
        :type  vv_yout:   GXVV
        :type  vv_depth:  GXVV
        :type  vvdc:      GXVV
        :type  vv_zer:    GXVV
        :type  vvx_yer:   GXVV
        :type  vv_wnd:    GXVV
        :type  si:        float
        :type  wt_pow:    float
        :type  x_yfit:    int

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** All VVs must be REAL

        .. seealso::

            `vv_euler <geosoft.gxapi.GXGU.vv_euler>`
        """
        gxapi_cy.WrapGU._vv_euler2(GXContext._get_tls_geo(), vv_xin, vv_yin, img_data, imgx, imgy, imgz, vv_xout, vv_yout, vv_depth, vvdc, vv_zer, vvx_yer, vv_wnd, si, wt_pow, x_yfit)
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer