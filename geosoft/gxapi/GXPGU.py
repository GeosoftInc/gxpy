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
class GXPGU(gxapi_cy.WrapPGU):
    """
    GXPGU class.

    A collection of methods applied to `GXPG <geosoft.gxapi.GXPG>` objects, including
    fills, trending and 2-D `GXFFT <geosoft.gxapi.GXFFT>` operations.
    """

    def __init__(self, handle=0):
        super(GXPGU, self).__init__(GXContext._get_tls_geo(), handle)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of `GXPGU <geosoft.gxapi.GXPGU>`
        
        :returns: A null `GXPGU <geosoft.gxapi.GXPGU>`
        :rtype:   GXPGU
        """
        return GXPGU()

    def is_null(self):
        """
        Check if this is a null (undefined) instance
        
        :returns: True if this is a null (undefined) instance, False otherwise.
        :rtype:   bool
        """
        return self._internal_handle() == 0



# General


    @classmethod
    def bool_mask(cls, pg, ref_fil):
        """
        Apply reference file boolean mask to pager
        
        :param pg:       Pager obj
        :param ref_fil:  sRefFil - reference file for boolean mask flag.
        :type  pg:       GXPG
        :type  ref_fil:  str

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        gxapi_cy.WrapPGU._bool_mask(GXContext._get_tls_geo(), pg, ref_fil.encode())
        



    @classmethod
    def expand(cls, pg_i, pg_o, ex_pcnt, ex_shp, ex_x, ex_y):
        """
        Expand a pager by filling the dummies for expanded edges
        
        :param pg_i:     Original pager obj
        :param pg_o:     Expanded pager obj
        :param ex_pcnt:  % expansion
        :param ex_shp:   Option  0 - rectangular, 1 - square
        :param ex_x:     X dimension to expand to (0 for expansion to FFT2D legal dimension)
        :param ex_y:     Y dimension to expand to (0 for expansion to FFT2D legal dimension)
        :type  pg_i:     GXPG
        :type  pg_o:     GXPG
        :type  ex_pcnt:  float
        :type  ex_shp:   int
        :type  ex_x:     int
        :type  ex_y:     int

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** 3D pagers are expanded in X,Y direction the number of slices(Z) is unchanged .
        """
        gxapi_cy.WrapPGU._expand(GXContext._get_tls_geo(), pg_i, pg_o, ex_pcnt, ex_shp, ex_x, ex_y)
        



    @classmethod
    def fill(cls, pg, fl_roll_wt, fl_roll_base, fl_roll_dist, fl_mxf, fl_mxp, fl_amp_lmt, fl_edge_lmt, fl_edge_wid, fl_npass, ref_fil):
        """
        Replace all dummies in a pager by predict values.
        
        :param pg:            Pager obj
        :param fl_roll_wt:    Roll off weighting option: 1 - linear, 2 - square
        :param fl_roll_base:  dRollBase - the value to roll off to, `GS_R8DM <geosoft.gxapi.GS_R8DM>` for roll off to mean value line by line.
        :param fl_roll_dist:  lRollDist - (at unit of cell dist.) for roll-off. 0 for no roll of, -1 for the default: 2 times of min. dummy edge dim.
        :param fl_mxf:        lMxf - max. filter length.  -1 for no max. entropy. 0 for the default of MIN(minimum dummy edge dim, 32).
        :param fl_mxp:        lMxp - max. pred. sample 0 for the default of 2*lMxf.
        :param fl_amp_lmt:    dAmpLmt - limit (abs. value) amplitudes to this level. Amplitudes are limited starting at half this value. <=0.0 for no amp limit.
        :param fl_edge_lmt:   dEdgeLmt - limit edge (abs. value) amplitudes to this level. <0.0 for no edge limit.
        :param fl_edge_wid:   lEdgeWidth - within this dist. (at unit of cell size) for amp. limited. -1 for no edge limit. 0 for the default of minimum dummy edge dim.
        :param fl_npass:      iNPass - number of time to pass smooth filter
        :param ref_fil:       sRefFil - reference file for smooth filter flag.
        :type  pg:            GXPG
        :type  fl_roll_wt:    int
        :type  fl_roll_base:  float
        :type  fl_roll_dist:  int
        :type  fl_mxf:        int
        :type  fl_mxp:        int
        :type  fl_amp_lmt:    float
        :type  fl_edge_lmt:   float
        :type  fl_edge_wid:   int
        :type  fl_npass:      int
        :type  ref_fil:       str

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        gxapi_cy.WrapPGU._fill(GXContext._get_tls_geo(), pg, fl_roll_wt, fl_roll_base, fl_roll_dist, fl_mxf, fl_mxp, fl_amp_lmt, fl_edge_lmt, fl_edge_wid, fl_npass, ref_fil.encode())
        



    @classmethod
    def fill_value(cls, pg, value):
        """
        Set all values in a pager to a single value.
        
        :param pg:     Pager obj
        :param value:  Value to set in pager
        :type  pg:     GXPG
        :type  value:  float

        .. versionadded:: 5.0.8

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        gxapi_cy.WrapPGU._fill_value(GXContext._get_tls_geo(), pg, value)
        



    @classmethod
    def filt_sym(cls, pg, npass, usefile, file, size, vv):
        """
        Apply 5x5, 7x7 or 9X9 symmetric convolution filter to a `GXPG <geosoft.gxapi.GXPG>`.
        
        :param pg:       Pager obj
        :param npass:    Number of time to pass smooth filter
        :param usefile:  Flag to use filter file
        :param file:     File for filter values
        :param size:     Size of filter window, 5/7/9
        :param vv:       Array of 6/10/15 filter coefficients
        :type  pg:       GXPG
        :type  npass:    int
        :type  usefile:  int
        :type  file:     str
        :type  size:     int
        :type  vv:       GXVV

        .. versionadded:: 5.1.5

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        gxapi_cy.WrapPGU._filt_sym(GXContext._get_tls_geo(), pg, npass, usefile, file.encode(), size, vv)
        



    @classmethod
    def filt_sym5(cls, pg, npass, usefile, file, vv):
        """
        Apply 5x5 symmetric convolution filter to a `GXPG <geosoft.gxapi.GXPG>`.
        
        :param pg:       Pager obj
        :param npass:    Number of time to pass smooth filter
        :param usefile:  Flag to use filter file
        :param file:     File for filter values
        :param vv:       Array of 6 filter coefficients at position 00, 10, 11, 20, 21, 22. Symmetric filters look like : 22 21 20 21 22 21 11 10 11 21 20 10 00 10 20 21 11 10 11 21 22 21 20 21 22
        :type  pg:       GXPG
        :type  npass:    int
        :type  usefile:  int
        :type  file:     str
        :type  vv:       GXVV

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        gxapi_cy.WrapPGU._filt_sym5(GXContext._get_tls_geo(), pg, npass, usefile, file.encode(), vv)
        



    @classmethod
    def grid_peak(cls, grid, nlmt, vv_x, vv_y, vv_z):
        """
        Pick grid peaks.
        
        :param grid:  Grid file name
        :param nlmt:  :ref:`BLAKEY_TEST`
        :param vv_x:  X of found peaks
        :param vv_y:  Y of found peaks
        :param vv_z:  Z values of found peaks
        :type  grid:  str
        :type  nlmt:  int
        :type  vv_x:  GXVV
        :type  vv_y:  GXVV
        :type  vv_z:  GXVV

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** Blakey test limit defines how grid peaks are to be found.
        For example, with the `BLAKEY_TEST_ONESIDE <geosoft.gxapi.BLAKEY_TEST_ONESIDE>`, a grid
        point will be picked if its grid value is greater than
        the value of one or more of its four neighouring points.
        """
        gxapi_cy.WrapPGU._grid_peak(GXContext._get_tls_geo(), grid.encode(), nlmt, vv_x, vv_y, vv_z)
        



    @classmethod
    def dw_gridding_dat(cls, pg, dat, reg):
        """
        `dw_gridding_dat <geosoft.gxapi.GXPGU.dw_gridding_dat>`     Inverse-distance weighting gridding method, `GXDAT <geosoft.gxapi.GXDAT>` version.
        
        :param pg:   Input grid
        :param dat:  `GXDAT <geosoft.gxapi.GXDAT>` source
        :param reg:  Parameters (see above)
        :type  pg:   GXPG
        :type  dat:  GXDAT
        :type  reg:  GXREG

        .. versionadded:: 7.3

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** See the notes for `dw_gridding_db <geosoft.gxapi.GXPGU.dw_gridding_db>`.
        """
        gxapi_cy.WrapPGU._dw_gridding_dat(GXContext._get_tls_geo(), pg, dat, reg)
        



    @classmethod
    def dw_gridding_dat_3d(cls, pg, dat, reg):
        """
        `dw_gridding_dat_3d <geosoft.gxapi.GXPGU.dw_gridding_dat_3d>`     Inverse-distance weighting gridding method, `GXDAT <geosoft.gxapi.GXDAT>` version, 3D.
        
        :param pg:   Input 3D `GXPG <geosoft.gxapi.GXPG>`
        :param dat:  `GXDAT <geosoft.gxapi.GXDAT>` source
        :param reg:  Parameters (see above)
        :type  pg:   GXPG
        :type  dat:  GXDAT
        :type  reg:  GXREG

        .. versionadded:: 8.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** See the notes for `dw_gridding_db_3d <geosoft.gxapi.GXPGU.dw_gridding_db_3d>`.
        """
        gxapi_cy.WrapPGU._dw_gridding_dat_3d(GXContext._get_tls_geo(), pg, dat, reg)
        



    @classmethod
    def dw_gridding_db(cls, pg, db, x, y, z, reg):
        """
        `dw_gridding_db <geosoft.gxapi.GXPGU.dw_gridding_db>`     Inverse-distance weighting gridding method, `GXDB <geosoft.gxapi.GXDB>` version.
        
        :param pg:   Input grid
        :param db:   Database
        :param x:    X Channel [READONLY]
        :param y:    Y Channel [READONLY]
        :param z:    Data Channel [READONLY]
        :param reg:  Parameters (see above)
        :type  pg:   GXPG
        :type  db:   GXDB
        :type  x:    int
        :type  y:    int
        :type  z:    int
        :type  reg:  GXREG

        .. versionadded:: 7.3

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** Grid cells take on the averaged values within a search radius, weighted inversely by distance.

        Weighting can be controlled using the power and slope properties;

        weighting = 1 / (distance^wtpower + 1/slope) where distance is in
        units of grid cells (X dimenstion). Default is 0.0,

        If the blanking distance is set, all cells whose center point is not within the blanking distance of
        at least one data point are set to dummy.

        `GXREG <geosoft.gxapi.GXREG>` Parameters:

        X0, Y0, DX, DY: Grid origin, and cell sizes (required)
        WT_POWER (default=2), WT_SLOPE (default=1) Weighting function parameters
        SEARCH_RADIUS: Distance weighting limit (default = 4 * SQRT(DX*DY))
        BLANKING_DISTANCE: Dummy values farther from data than this distance. (default = 4 * SQRT(DX*DY))
        LOG: Apply log transform to input data before gridding (0:No (default), 1:Yes)?
        LOG_BASE: One of `VV_LOG_BASE_10 <geosoft.gxapi.VV_LOG_BASE_10>` (default) or `VV_LOG_BASE_E <geosoft.gxapi.VV_LOG_BASE_E>`
        LOG_NEGATIVE: One of `VV_LOG_NEGATIVE_NO <geosoft.gxapi.VV_LOG_NEGATIVE_NO>` (default) or `VV_LOG_NEGATIVE_YES <geosoft.gxapi.VV_LOG_NEGATIVE_YES>`
        """
        gxapi_cy.WrapPGU._dw_gridding_db(GXContext._get_tls_geo(), pg, db, x, y, z, reg)
        



    @classmethod
    def dw_gridding_db_3d(cls, pg, db, x, y, z, data, reg):
        """
        `dw_gridding_db_3d <geosoft.gxapi.GXPGU.dw_gridding_db_3d>`     Inverse-distance weighting gridding method, `GXDB <geosoft.gxapi.GXDB>` version, 3D.
        
        :param pg:    Input 3D `GXPG <geosoft.gxapi.GXPG>`
        :param db:    Database
        :param x:     X Channel [READONLY]
        :param y:     Y Channel [READONLY]
        :param z:     Z Channel [READONLY]
        :param data:  Data Channel [READONLY]
        :param reg:   Parameters (see above)
        :type  pg:    GXPG
        :type  db:    GXDB
        :type  x:     int
        :type  y:     int
        :type  z:     int
        :type  data:  int
        :type  reg:   GXREG

        .. versionadded:: 8.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** 3D cells take on the averaged values within a search radius, weighted inversely by distance.

        Weighting can be controlled using the power and slope properties;

        weighting = 1 / (distance^wtpower + 1/slope) where distance is in
        units of grid cells (X dimenstion). Default is 0.0,

        If the blanking distance is set, all cells whose center point is not within the blanking distance of
        at least one data point are set to dummy.

        `GXREG <geosoft.gxapi.GXREG>` Parameters:

        X0, Y0, Z0, DX, DY, DZ: Grid origin, and cell sizes (required)
        WT_POWER (default=2), WT_SLOPE (default=1) Weighting function parameters
        SEARCH_RADIUS: Distance weighting limit (default = 4 * CUBE_ROOT(DX*DY*DZ))
        BLANKING_DISTANCE: Dummy values farther from data than this distance. (default = 4 * CUBE_ROOT(DX*DY*DZ))
        LOG: Apply log transform to input data before gridding (0:No (default), 1:Yes)?
        LOG_BASE: One of `VV_LOG_BASE_10 <geosoft.gxapi.VV_LOG_BASE_10>` (default) or `VV_LOG_BASE_E <geosoft.gxapi.VV_LOG_BASE_E>`
        LOG_NEGATIVE: One of `VV_LOG_NEGATIVE_NO <geosoft.gxapi.VV_LOG_NEGATIVE_NO>` (default) or `VV_LOG_NEGATIVE_YES <geosoft.gxapi.VV_LOG_NEGATIVE_YES>`
        """
        gxapi_cy.WrapPGU._dw_gridding_db_3d(GXContext._get_tls_geo(), pg, db, x, y, z, data, reg)
        



    @classmethod
    def dw_gridding_vv(cls, pg, vv_x, vv_y, vv_z, reg):
        """
        `dw_gridding_vv <geosoft.gxapi.GXPGU.dw_gridding_vv>`     Inverse-distance weighting gridding method, `GXVV <geosoft.gxapi.GXVV>` version.
        
        :param pg:    Input grid
        :param vv_x:  X locations
        :param vv_y:  Y locations
        :param vv_z:  Data values to grid
        :param reg:   Parameters (see above)
        :type  pg:    GXPG
        :type  vv_x:  GXVV
        :type  vv_y:  GXVV
        :type  vv_z:  GXVV
        :type  reg:   GXREG

        .. versionadded:: 7.3

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** See the notes for `dw_gridding_db <geosoft.gxapi.GXPGU.dw_gridding_db>`.
        """
        gxapi_cy.WrapPGU._dw_gridding_vv(GXContext._get_tls_geo(), pg, vv_x, vv_y, vv_z, reg)
        



    @classmethod
    def numeric_to_thematic(cls, pg_i, vv, pg_o):
        """
        `numeric_to_thematic <geosoft.gxapi.GXPGU.numeric_to_thematic>`    Set index values in a pager based on a numeric pager with translation `GXVV <geosoft.gxapi.GXVV>`.

        Returns			  Nothing
        
        :param pg_i:  Input numeric `GXPG <geosoft.gxapi.GXPG>`
        :param vv:    Translation `GXVV <geosoft.gxapi.GXVV>` (see notes above)
        :param pg_o:  Output thematic `GXPG <geosoft.gxapi.GXPG>`
        :type  pg_i:  GXPG
        :type  vv:    GXVV
        :type  pg_o:  GXPG

        .. versionadded:: 7.3

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** The values in the input data `GXVV <geosoft.gxapi.GXVV>` represent the center-of-range
        values of unique properties with indices 0 to N-1, where N
        is the number of items in the input `GXVV <geosoft.gxapi.GXVV>`.

        This `GXVV <geosoft.gxapi.GXVV>` is sorted from smallest to largest, and each value in
        in the input numeric `GXPG <geosoft.gxapi.GXPG>` is tested to see into which range it goes.
        The closest range value for each item is used, so the half-way point
        is the dividing point. The top and bottom-most range widths are determined
        by the "inside half-width" to the nearest range.

        The INDEX of the closest range is then inserted into the output `GXPG <geosoft.gxapi.GXPG>`, so
        it can be used in a thematic voxel (for instance).
        """
        gxapi_cy.WrapPGU._numeric_to_thematic(GXContext._get_tls_geo(), pg_i, vv, pg_o)
        



    @classmethod
    def peakedness(cls, grid, pkness, vv_x, vv_y, vv_z):
        """
        Find all peaks in peakedneess grid pager
        
        :param grid:    Grid file name
        :param pkness:  Cutoff limit for finding peaks
        :param vv_x:    X of found peaks
        :param vv_y:    Y of found peaks
        :param vv_z:    Z values of found peaks
        :type  grid:    str
        :type  pkness:  int
        :type  vv_x:    GXVV
        :type  vv_y:    GXVV
        :type  vv_z:    GXVV

        .. versionadded:: 5.0.8

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        gxapi_cy.WrapPGU._peakedness(GXContext._get_tls_geo(), grid.encode(), pkness, vv_x, vv_y, vv_z)
        



    @classmethod
    def peakedness_grid(cls, grdi, grdo, radius, percent_lesser):
        """
        Create peakedneess grid from input grid.
        
        :param grdi:            Input grid file name
        :param grdo:            Output grid (peakedness) file name
        :param radius:          Radius
        :param percent_lesser:  Percent Lesser value (see notes)
        :type  grdi:            str
        :type  grdo:            str
        :type  radius:          int
        :type  percent_lesser:  float

        .. versionadded:: 5.0.8

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** This function creates a peakedneess grid from input grid.
        Radius, is the maximum radius at which the value of the parent pixel is compared to
        the value of surrounding pixels.
        ``percent_lesser``, is used to indicate the percentage of pixels at each radii smaller than
        or equal to Radius that must have value lower than the parent pixel in order to call
        that radius true or equal to 1.
        Description:  For each pixel in the grid a series of radii are evaluated from 1 to Radius.
        If the percentage of pixels for a given radius is less than ``percent_lesser`` the parent pixel
        receives an additional 1.
        For examples if the Radius is set to 5 and the ``percent_lesser`` is set to 70%.
        And radius 1 = 90%, radius 2 = 85%, radius 3 = 75%, radius 4 = 70% and radius 5 = 65%
        then the parent pixel would receive 1+1+1+1+0 = 4.
        Use:  This function is useful in isolating the anomaly peaks in data that has a large
        value range for anomalies. For example the 1 mV anomaly could quite possibly have
        the same representation as the 100 mV anomaly using this function.
        """
        gxapi_cy.WrapPGU._peakedness_grid(GXContext._get_tls_geo(), grdi.encode(), grdo.encode(), radius, percent_lesser)
        



    @classmethod
    def ref_file(cls, pg, ref_fil):
        """
        Create a reference file (boolean mask flag) from pager.
        
        :param pg:       `GXPG <geosoft.gxapi.GXPG>` object
        :param ref_fil:  Reference file name
        :type  pg:       GXPG
        :type  ref_fil:  str

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** A reference file is a binary file with the following format:

        The first 8 bytes are the pager dimensions NX and NY as longs.
        The remaining bits, one bit per pager cell - (NX * NY)/8 bytes
        are zero where the pager is dummy, and 1 where the pager is defined.

        The reference file is used in various operations where it is
        necessary to mask some output to the original defined cells.
        """
        gxapi_cy.WrapPGU._ref_file(GXContext._get_tls_geo(), pg, ref_fil.encode())
        



    @classmethod
    def save_file(cls, pg, xo, yo, dx, dy, rot, tr, ipj, file):
        """
        Writes a `GXPG <geosoft.gxapi.GXPG>` to an image file.
        
        :param pg:    Input `GXPG <geosoft.gxapi.GXPG>` object
        :param xo:    X origin
        :param yo:    Y origin
        :param dx:    DX
        :param dy:    DY
        :param rot:   Rotation angle
        :param tr:    Trend information or NULL
        :param ipj:   Projection or NULL
        :param file:  Output file name
        :type  pg:    GXPG
        :type  xo:    float
        :type  yo:    float
        :type  dx:    float
        :type  dy:    float
        :type  rot:   float
        :type  tr:    GXTR
        :type  ipj:   GXIPJ
        :type  file:  str

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** The trend object and projection are optional.
        """
        gxapi_cy.WrapPGU._save_file(GXContext._get_tls_geo(), pg, xo, yo, dx, dy, rot, tr, ipj, file.encode())
        



    @classmethod
    def thematic_to_numeric(cls, pg_i, vv, pg_o):
        """
        Set numeric values in a pager based on an index pager with translation `GXVV <geosoft.gxapi.GXVV>`.

        Returns			  Nothing
        
        :param pg_i:  Input Index `GXPG <geosoft.gxapi.GXPG>`
        :param vv:    Translation `GXVV <geosoft.gxapi.GXVV>`
        :param pg_o:  Output Data `GXPG <geosoft.gxapi.GXPG>`
        :type  pg_i:  GXPG
        :type  vv:    GXVV
        :type  pg_o:  GXPG

        .. versionadded:: 7.3

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** The items in the input data `GXVV <geosoft.gxapi.GXVV>` are inserted into
        the output `GXPG <geosoft.gxapi.GXPG>` using the indices in the index `GXPG <geosoft.gxapi.GXPG>`.

        This function is useful when converting a thematic voxel, which is
        type `GS_LONG <geosoft.gxapi.GS_LONG>` and contains indices into its own internal `GXTPAT <geosoft.gxapi.GXTPAT>`
        object, and you provide a numeric mapping `GXVV <geosoft.gxapi.GXVV>`, calculated using
        SetupTranslateToNumericVV_TPAT.
        """
        gxapi_cy.WrapPGU._thematic_to_numeric(GXContext._get_tls_geo(), pg_i, vv, pg_o)
        



    @classmethod
    def trend(cls, pg_i, pg_o, tr, tr_opt, tr_pt_bs, xo, yo, dx, dy):
        """
        Trend remove or replace back in pager
        
        :param pg_i:      Original pager obj
        :param pg_o:      Trended pager obj
        :param tr:        Trend obj
        :param tr_opt:    Option  0 - calculate, 1 - given in `GXTR <geosoft.gxapi.GXTR>`, 2 - replace back from `GXTR <geosoft.gxapi.GXTR>`
        :param tr_pt_bs:  Trend base on: 0 - all points, 1 - edge points
        :param xo:        Trend origin  rXo,
        :param yo:        Trend origin  rYo,
        :param dx:        Increment in X direction  rDx,
        :param dy:        Increment in Y direction  rDy
        :type  pg_i:      GXPG
        :type  pg_o:      GXPG
        :type  tr:        GXTR
        :type  tr_opt:    int
        :type  tr_pt_bs:  int
        :type  xo:        float
        :type  yo:        float
        :type  dx:        float
        :type  dy:        float

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        gxapi_cy.WrapPGU._trend(GXContext._get_tls_geo(), pg_i, pg_o, tr, tr_opt, tr_pt_bs, xo, yo, dx, dy)
        




# Math Operations


    @classmethod
    def add_scalar(cls, pg, scalar):
        """
        Add a scalar value to a pager
        
        :param pg:      Pager
        :param scalar:  Scalar Value
        :type  pg:      GXPG
        :type  scalar:  float

        .. versionadded:: 7.1

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** Only available for FLOAT or DOUBLE pagers
        """
        gxapi_cy.WrapPGU._add_scalar(GXContext._get_tls_geo(), pg, scalar)
        



    @classmethod
    def multiply_scalar(cls, pg, scalar):
        """
        Multiply a scalar value and a pager
        
        :param pg:      Pager
        :param scalar:  Scalar Value
        :type  pg:      GXPG
        :type  scalar:  float

        .. versionadded:: 7.1

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** Only available for FLOAT or DOUBLE pagers
        """
        gxapi_cy.WrapPGU._multiply_scalar(GXContext._get_tls_geo(), pg, scalar)
        




# Matrix Operation


    @classmethod
    def correlation_matrix(cls, pg_u, pg_o):
        """
        Find the correlations between columns in a matrix
        
        :param pg_u:  Input matrix
        :param pg_o:  Returned correlation matrix
        :type  pg_u:  GXPG
        :type  pg_o:  GXPG

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** The input matrix is M rows by N columns. The returned matrix
        is a symmetric N by N matrix whose elements are the normalized
        dot products of the columns of the input matrix with themselves.
        The elements take on values from 0 (orthogonal) to 1 (parallel).
        """
        gxapi_cy.WrapPGU._correlation_matrix(GXContext._get_tls_geo(), pg_u, pg_o)
        



    @classmethod
    def correlation_matrix2(cls, pg_u, corr, pg_o):
        """
        Same as `correlation_matrix <geosoft.gxapi.GXPGU.correlation_matrix>`, but select correlation type.
        
        :param pg_u:  Input matrix
        :param corr:  :ref:`PGU_CORR`
        :param pg_o:  Returned correlation matrix
        :type  pg_u:  GXPG
        :type  corr:  int
        :type  pg_o:  GXPG

        .. versionadded:: 5.1.8

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        gxapi_cy.WrapPGU._correlation_matrix2(GXContext._get_tls_geo(), pg_u, corr, pg_o)
        



    @classmethod
    def invert_matrix(cls, pg_i, pg_o):
        """
        Inverts a square matrix using LU decomp. and back-substitution
        
        :param pg_i:  Input matrix
        :param pg_o:  Output inverted matrix (can be same as input).
        :type  pg_i:  GXPG
        :type  pg_o:  GXPG

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** This is an "in-place" operation, and set up so that the input and
        output pagers may be the same handle. (If they are different, the
        input pager remains unchanged).
        Pagers and VVs must be type `GS_DOUBLE <geosoft.gxapi.GS_DOUBLE>`.
        """
        gxapi_cy.WrapPGU._invert_matrix(GXContext._get_tls_geo(), pg_i, pg_o)
        



    @classmethod
    def jacobi(cls, pg_i, vv_d, pg_eigen):
        """
        Find eigenvalues, eigenvectors of a real symmetric matrix.
        
        :param pg_i:      Input Pager
        :param vv_d:      Eigenvalues (returned)
        :param pg_eigen:  Eigenvectors (returned)
        :type  pg_i:      GXPG
        :type  vv_d:      GXVV
        :type  pg_eigen:  GXPG

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** The number of rows must equal the number of columns.
        Eienvalues, vectors are sorted in descending order.
        """
        gxapi_cy.WrapPGU._jacobi(GXContext._get_tls_geo(), pg_i, vv_d, pg_eigen)
        



    @classmethod
    def lu_back_sub(cls, pg_a, vv_i, vv_b, vv_sol):
        """
        Solve a linear system using LU decomposition and back-substitution.
        
        :param pg_a:    LU decomposition of A
        :param vv_i:    Permutation vector (type INT)
        :param vv_b:    Right hand side vector B (input)
        :param vv_sol:  Solution vector (output)
        :type  pg_a:    GXPG
        :type  vv_i:    GXVV
        :type  vv_b:    GXVV
        :type  vv_sol:  GXVV

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** Solves the system Ax = b for a given b, using the LU decomposition
        of the matrix a
        The LU decomposition and the permutation vector are obtained
        from `lu_back_sub <geosoft.gxapi.GXPGU.lu_back_sub>`.
        Pagers and VVs must be type `GS_DOUBLE <geosoft.gxapi.GS_DOUBLE>` except for the permutation vector,
        which should be INT
        """
        gxapi_cy.WrapPGU._lu_back_sub(GXContext._get_tls_geo(), pg_a, vv_i, vv_b, vv_sol)
        



    @classmethod
    def lu_decomp(cls, pg_i, pg_o, vv_perm):
        """
        Perform an LU decomposition on a square pager.
        
        :param pg_i:     Input
        :param pg_o:     LU decomposition (may be same pager as input)
        :param vv_perm:  Permutation vector (type INT)
        :type  pg_i:     GXPG
        :type  pg_o:     GXPG
        :type  vv_perm:  GXVV

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** The L and U matrix are both contained in the returned pager; The
        "L" matrix is composed of the sub-diagonal elements of the output
        pager, as well as "1" values on the diagonal. The "U" matrix is
        composed of the diagonal elements (sub-diagonal elements set to 0).
        This is an "in-place" operation, and set up so that the input and
        output pagers may be the same handle. (If they are different, the
        input pager remains unchanged).
        The LU decomposition, and the permutation vector are used for
        `lu_back_sub <geosoft.gxapi.GXPGU.lu_back_sub>`.
        Pagers must be type `GS_DOUBLE <geosoft.gxapi.GS_DOUBLE>` and the permutation vector type INT
        """
        gxapi_cy.WrapPGU._lu_decomp(GXContext._get_tls_geo(), pg_i, pg_o, vv_perm)
        



    @classmethod
    def matrix_mult(cls, pg_u, transpose_u, pg_v, transpose, pg_uv):
        """
        Multiply two pagers as if they were matrices.
        
        :param pg_u:         Matrix U
        :param transpose_u:  TRUE (1) if U should be transposed before multiplication
        :param pg_v:         Matrix V
        :param transpose:    TRUE (1) if V should be transposed before multiplication
        :param pg_uv:        Returned matrix U*V
        :type  pg_u:         GXPG
        :type  transpose_u:  int
        :type  pg_v:         GXPG
        :type  transpose:    int
        :type  pg_uv:        GXPG

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** The matrices must be correctly dimensioned, taking into
        account whether transposition should occur before
        multiplication. The input matrices are not altered on output (even
        if transposition is requested).
        Assertions if: Matrices are not expected sizes
        Dummies are treated as 0 values.
        """
        gxapi_cy.WrapPGU._matrix_mult(GXContext._get_tls_geo(), pg_u, transpose_u, pg_v, transpose, pg_uv)
        



    @classmethod
    def matrix_vector_mult(cls, pg_u, vv_x, vv_o):
        """
        Multiply a `GXVV <geosoft.gxapi.GXVV>` by a pager like a matrix*vector multiply.
        
        :param pg_u:  Matrix U
        :param vv_x:  Vector x
        :param vv_o:  Returned vector U*x
        :type  pg_u:  GXPG
        :type  vv_x:  GXVV
        :type  vv_o:  GXVV

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** The matrix is input as an M rows (data) by N columns (variables) `GXPG <geosoft.gxapi.GXPG>`.
        The vector must be of length N. The output `GXVV <geosoft.gxapi.GXVV>` is set to length M.
        The `GXPG <geosoft.gxapi.GXPG>` and VVs must be type `GS_DOUBLE <geosoft.gxapi.GS_DOUBLE>`.

        Terminates if: 

             Matrices, `GXVV <geosoft.gxapi.GXVV>` are not expected sizes (taken from U)
             PGs are not `GS_DOUBLE <geosoft.gxapi.GS_DOUBLE>`.

        Dummies are treated as 0 values.
        """
        gxapi_cy.WrapPGU._matrix_vector_mult(GXContext._get_tls_geo(), pg_u, vv_x, vv_o)
        



    @classmethod
    def sv_decompose(cls, pg_a, pg_u, vv_w, pg_v):
        """
        Do a singular value decomposition on a matrix stored as a `GXPG <geosoft.gxapi.GXPG>`
        
        :param pg_a:  Input A matrix, M data (rows), N variables (columns)
        :param pg_u:  The returned U Matrix
        :param vv_w:  Returned weights (W)
        :param pg_v:  Returned V matrix
        :type  pg_a:  GXPG
        :type  pg_u:  GXPG
        :type  vv_w:  GXVV
        :type  pg_v:  GXPG

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** The matrix is input as an N rows (data) by M columns (variables) `GXPG <geosoft.gxapi.GXPG>`.
        On return, the matrix is decomposed to A = U * W * Vt. If M<N, then an error will 
        be registered. In this case, augment the "A" `GXPG <geosoft.gxapi.GXPG>` with rows of zero values.

        The input matrices must be A[M,N], U[M.N] and V[N,N]. The length of the W `GXVV <geosoft.gxapi.GXVV>`
        is set by sSVD_PGU to N.

        The Pagers must be type `GS_DOUBLE <geosoft.gxapi.GS_DOUBLE>`.

        Terminates if: 

             U is not M by N. (Taken from size of A)
             V is not N by N. (Taken from #columns in A).
             PGs, VV are not `GS_DOUBLE <geosoft.gxapi.GS_DOUBLE>`
        """
        gxapi_cy.WrapPGU._sv_decompose(GXContext._get_tls_geo(), pg_a, pg_u, vv_w, pg_v)
        



    @classmethod
    def sv_recompose(cls, pg_u, vv_w, pg_v, min_w, pg_a):
        """
        Reconstitute the original matrix from an SVD.
        
        :param pg_u:   U matrix
        :param vv_w:   Weights (W)
        :param pg_v:   V matrix
        :param min_w:  Minimum weight to use (Dummy for all)
        :param pg_a:   A matrix (returned)
        :type  pg_u:   GXPG
        :type  vv_w:   GXVV
        :type  pg_v:   GXPG
        :type  min_w:  float
        :type  pg_a:   GXPG

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** The matrix is input as an N rows (data) by M columns (variables) `GXPG <geosoft.gxapi.GXPG>`.
        On return, the matrix is decomposed to A = U * W * Vt.
        If M<N, then an error will be registered. In this case, augment the
        "A" `GXPG <geosoft.gxapi.GXPG>` with rows of zero values.
        The input matrices must be A[M,N], U[M.N] and V[N,N]. The length of the W `GXVV <geosoft.gxapi.GXVV>`
        is set by sSVDecompose_PGU to N.
        The Pagers must be type `GS_DOUBLE <geosoft.gxapi.GS_DOUBLE>`.

        Terminates if: 

             U is not M by N. (Taken from size of A)
             V is not N by N. (Taken from #columns in A).
             PGs, VV are not `GS_DOUBLE <geosoft.gxapi.GS_DOUBLE>`.

        Dummies are treated as 0 values.
        """
        gxapi_cy.WrapPGU._sv_recompose(GXContext._get_tls_geo(), pg_u, vv_w, pg_v, min_w, pg_a)
        




# Principal Component Analysis


    @classmethod
    def pc_communality(cls, pg_i, vv_c):
        """
        Determines principal component communalities.
        
        :param pg_i:  Input pager of the principal components
        :param vv_c:  Returned communality values
        :type  pg_i:  GXPG
        :type  vv_c:  GXVV

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** Calculate communalities (sums of the squares of the column
        values in each row)
        Pagers and VVs must be type `GS_DOUBLE <geosoft.gxapi.GS_DOUBLE>`.
        """
        gxapi_cy.WrapPGU._pc_communality(GXContext._get_tls_geo(), pg_i, vv_c)
        



    @classmethod
    def pc_loadings(cls, pg_x, pg_loadings):
        """
        Compute the principal component loadings from the standardized data.
        
        :param pg_x:         Standardized data matrix (M by N)
        :param pg_loadings:  Principal component loadings (N by N)
        :type  pg_x:         GXPG
        :type  pg_loadings:  GXPG

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** Works on columns of the `GXPG <geosoft.gxapi.GXPG>`.
        Calculates the correlation matrix from the columns of the
        standardized data, then computes the eigen values and eigenvectors
        of the correlation matrix. The loadings are the eigenvectors, ordered
        by descending eigenvalues, scaled by the square root of the
        eigenvalues. The returned pager must be sized the same as the
        input pager.
        Correlations are performed using "`PGU_CORR_SIMPLE <geosoft.gxapi.PGU_CORR_SIMPLE>`", so if you want
        Pearson correlations, or wish to use a modified correlation matrix,
        use `pc_loadings2 <geosoft.gxapi.GXPGU.pc_loadings2>` and input the correlation matrix directly.
        """
        gxapi_cy.WrapPGU._pc_loadings(GXContext._get_tls_geo(), pg_x, pg_loadings)
        



    @classmethod
    def pc_loadings2(cls, pg_c, pg_loadings):
        """
        Same as PCLoading_PGU, but input correlation matrix.
        
        :param pg_c:         Correllation matrix (N by N)
        :param pg_loadings:  Principal component loadings (N by N)
        :type  pg_c:         GXPG
        :type  pg_loadings:  GXPG

        .. versionadded:: 5.1.8

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** See `pc_loadings <geosoft.gxapi.GXPGU.pc_loadings>`.
        """
        gxapi_cy.WrapPGU._pc_loadings2(GXContext._get_tls_geo(), pg_c, pg_loadings)
        



    @classmethod
    def pc_scores(cls, pg_x, pg_loadings, pg_scores):
        """
        Compute the principal component scores from the standardized data.
        
        :param pg_x:         Standardized data matrix  (M by N)
        :param pg_loadings:  Principal component loadings (input) (N by L, L<=N)
        :param pg_scores:    Principal component scores (returned) (M by L, L<=N)
        :type  pg_x:         GXPG
        :type  pg_loadings:  GXPG
        :type  pg_scores:    GXPG

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** t  -1
        Forms the product X Ap (Ap Ap),  where X is the
        standardized data matrix, and Ap is the matrix of
        principal component loadings (see `pc_loadings <geosoft.gxapi.GXPGU.pc_loadings>`).
        The loadings must be input, and can be calculated by calling
        `pc_loadings <geosoft.gxapi.GXPGU.pc_loadings>`.
        Pagers and VVs must be type `GS_DOUBLE <geosoft.gxapi.GS_DOUBLE>`.
        """
        gxapi_cy.WrapPGU._pc_scores(GXContext._get_tls_geo(), pg_x, pg_loadings, pg_scores)
        



    @classmethod
    def pc_standardize(cls, pg, vv_m, vv_s, dir):
        """
        Remove/Replace mean and standard deviation
        
        :param pg:    Matrix to standardize
        :param vv_m:  Means
        :param vv_s:  Standard deviations
        :param dir:   :ref:`PGU_DIRECTION`
        :type  pg:    GXPG
        :type  vv_m:  GXVV
        :type  vv_s:  GXVV
        :type  dir:   int

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** Works on columns of the `GXPG <geosoft.gxapi.GXPG>`.
        """
        gxapi_cy.WrapPGU._pc_standardize(GXContext._get_tls_geo(), pg, vv_m, vv_s, dir)
        



    @classmethod
    def pc_standardize2(cls, pg, vv_mask, vv_m, vv_s, dir):
        """
        Remove/Replace mean and standard deviation, subset values.
        
        :param pg:       Matrix to standardize
        :param vv_mask:  Mask `GXVV <geosoft.gxapi.GXVV>` for data selection (forward only)
        :param vv_m:     Means
        :param vv_s:     Standard deviations
        :param dir:      Forward or reverse
        :type  pg:       GXPG
        :type  vv_mask:  GXVV
        :type  vv_m:     GXVV
        :type  vv_s:     GXVV
        :type  dir:      int

        .. versionadded:: 5.1.8

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** Like `pc_standardize <geosoft.gxapi.GXPGU.pc_standardize>`, except that not all the values are
        included in the calculation of the means and standard
        deviations. The inclusion is controlled by a mask `GXVV <geosoft.gxapi.GXVV>`,
        The rows where the mask is dummy are not included
        in the calculation, but ALL the values are standardized.
        """
        gxapi_cy.WrapPGU._pc_standardize2(GXContext._get_tls_geo(), pg, vv_mask, vv_m, vv_s, dir)
        



    @classmethod
    def pc_transform(cls, pg, vv_d, vv_f, vv_t, dir):
        """
        Transform/De-transform data.
        
        :param pg:    Matrix to transform
        :param vv_d:  Detection limits for the columns
        :param vv_f:  Maximum values for the columns
        :param vv_t:  :ref:`PGU_TRANS`
        :param dir:   :ref:`PGU_DIRECTION`
        :type  pg:    GXPG
        :type  vv_d:  GXVV
        :type  vv_f:  GXVV
        :type  vv_t:  GXVV
        :type  dir:   int

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** Works on columns of the `GXPG <geosoft.gxapi.GXPG>`.
        Forward direction: Applies the selected transform to the data.
        Backward direction: Applies the inverse transform to the data.
        The detection limits are input with a `GXVV <geosoft.gxapi.GXVV>`. In the forward
        transform, data values less than the detection limit are set
        to the limit.
        The factor limits are input with a `GXVV <geosoft.gxapi.GXVV>`. In the forward
        transform, data values greater than the maximum values are set
        to the maximum.
        """
        gxapi_cy.WrapPGU._pc_transform(GXContext._get_tls_geo(), pg, vv_d, vv_f, vv_t, dir)
        



    @classmethod
    def pc_varimax(cls, pg_i, pg_o):
        """
        Perform the Kaiser Varimax transformation on pr. comp. loadings
        
        :param pg_i:  Principal component loadings (input) (N by M, M<=N)
        :param pg_o:  Rotated principal component loadings (returned) (N by L, L<=M)
        :type  pg_i:  GXPG
        :type  pg_o:  GXPG

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** Rotates the principal components using the Kaiser's varimax
        scheme to move move each factor axis to positions so that
        projections from each variable on the factor axes are either
        near the extremities or near the origin.
        Pagers must be type `GS_DOUBLE <geosoft.gxapi.GS_DOUBLE>`.
        """
        gxapi_cy.WrapPGU._pc_varimax(GXContext._get_tls_geo(), pg_i, pg_o)
        




# Specialized Operations


    @classmethod
    def maximum_terrain_steepness(cls, pg, annular_size):
        """
        Compute the Maximum Steepness of a topography Pager
        
        :param pg:            Topography Pager
        :param annular_size:  Annular Size
        :type  pg:            GXPG
        :type  annular_size:  int

        :returns:             Maximum Terrain Steepness Computation.
        :rtype:               float

        .. versionadded:: 7.1

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** Calculates forward-looking slopes SX and SY in the X and Y directions
        using pager locations (ix, iy), (ix+size, iy), (ix, iy+isize)
        and returns SX*SX + SY*SY.
        The values in the last "size" rows and columns are not
        processed.
        The wrapper was created for testing and development purposes.
        """
        ret_val = gxapi_cy.WrapPGU._maximum_terrain_steepness(GXContext._get_tls_geo(), pg, annular_size)
        return ret_val




# Obsolete


    @classmethod
    def direct_gridding_db(cls, pg, xo, yo, dx, dy, rot, db, x, y, z, method):
        """
        Direct-gridding method, `GXDB <geosoft.gxapi.GXDB>` version.
        
        :param pg:      Input grid
        :param xo:      X origin of grid
        :param yo:      Y origin of grid
        :param dx:      X cell size
        :param dy:      Y cell size
        :param rot:     Rotation angle (degrees CCW).
        :param db:      Database
        :param x:       X Channel [READONLY]
        :param y:       Y Channel [READONLY]
        :param z:       Data Channel [READONLY]
        :param method:  :ref:`PGU_DIRECTGRID`
        :type  pg:      GXPG
        :type  xo:      float
        :type  yo:      float
        :type  dx:      float
        :type  dy:      float
        :type  rot:     float
        :type  db:      GXDB
        :type  x:       int
        :type  y:       int
        :type  z:       int
        :type  method:  int

        .. versionadded:: 7.3

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** Grid cells take on the specified statistic of the values inside the
        cell area. Grid cells containing no data values are set to dummy.
        """
        gxapi_cy.WrapPGU._direct_gridding_db(GXContext._get_tls_geo(), pg, xo, yo, dx, dy, rot, db, x, y, z, method)
        



    @classmethod
    def direct_gridding_db_3d(cls, pg, xo, yo, zo, dx, dy, dz, rot, db, x, y, z, data, method):
        """
        Direct-gridding method, `GXDB <geosoft.gxapi.GXDB>` version, 3D.
        
        :param pg:      Input 3D `GXPG <geosoft.gxapi.GXPG>`
        :param xo:      X origin of 3D grid
        :param yo:      Y origin of 3D grid
        :param zo:      Z origin of 3D grid
        :param dx:      X cell size
        :param dy:      Y cell size
        :param dz:      Z cell size
        :param rot:     Rotation angle (degrees CCW, vertical axis only).
        :param db:      Database
        :param x:       X Channel [READONLY]
        :param y:       Y Channel [READONLY]
        :param z:       Z Channel [READONLY]
        :param data:    Data Channel [READONLY]
        :param method:  :ref:`PGU_DIRECTGRID`
        :type  pg:      GXPG
        :type  xo:      float
        :type  yo:      float
        :type  zo:      float
        :type  dx:      float
        :type  dy:      float
        :type  dz:      float
        :type  rot:     float
        :type  db:      GXDB
        :type  x:       int
        :type  y:       int
        :type  z:       int
        :type  data:    int
        :type  method:  int

        .. versionadded:: 8.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** 3D grid cells take on the specified statistic of the values inside the
        cell area. Grid cells containing no data values are set to dummy.
        """
        gxapi_cy.WrapPGU._direct_gridding_db_3d(GXContext._get_tls_geo(), pg, xo, yo, zo, dx, dy, dz, rot, db, x, y, z, data, method)
        



    @classmethod
    def direct_gridding_vv(cls, pg, xo, yo, dx, dy, rot, v_vx, v_vy, v_vz, method):
        """
        Direct-gridding method, `GXVV <geosoft.gxapi.GXVV>` version.
        
        :param pg:      Input grid
        :param xo:      X origin of grid
        :param yo:      Y origin of grid
        :param dx:      X cell size
        :param dy:      Y cell size
        :param rot:     Rotation angle (degrees CCW).
        :param v_vx:    X locations of values
        :param v_vy:    Y locations of values
        :param v_vz:    Z values to grid
        :param method:  :ref:`PGU_DIRECTGRID`
        :type  pg:      GXPG
        :type  xo:      float
        :type  yo:      float
        :type  dx:      float
        :type  dy:      float
        :type  rot:     float
        :type  v_vx:    GXVV
        :type  v_vy:    GXVV
        :type  v_vz:    GXVV
        :type  method:  int

        .. versionadded:: 7.3

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** Grid cells take on the specified statistic of the values inside the
        cell area. Grid cells containing no data values are set to dummy.
        """
        gxapi_cy.WrapPGU._direct_gridding_vv(GXContext._get_tls_geo(), pg, xo, yo, dx, dy, rot, v_vx, v_vy, v_vz, method)
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer