### extends 'class_empty.py'
### block ClassImports
# NOTICE: Do not edit anything here, it is generated code
from . import gxapi_cy
from geosoft.gxapi import GXContext, float_ref, int_ref, str_ref
from .GXIMG import GXIMG


### endblock ClassImports

### block Header
# NOTICE: The code generator will not replace the code in this block
### endblock Header

### block ClassImplementation
# NOTICE: Do not edit anything here, it is generated code
class GXIMU(gxapi_cy.WrapIMU):
    """
    GXIMU class.

    Not a class. This is a catch-all group of functions working
    on `GXIMG <geosoft.gxapi.GXIMG>` objects (see `GXIMG <geosoft.gxapi.GXIMG>`). Grid operations include masking,
    trending, windowing, expanding and grid stitching.
    """

    def __init__(self, handle=0):
        super().__init__(GXContext._get_tls_geo(), handle)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of `GXIMU <geosoft.gxapi.GXIMU>`
        
        :returns: A null `GXIMU <geosoft.gxapi.GXIMU>`
        :rtype:   GXIMU
        """
        return GXIMU()

    def is_null(self):
        """
        Check if this is a null (undefined) instance
        
        :returns: True if this is a null (undefined) instance, False otherwise.
        :rtype:   bool
        """
        return self._internal_handle() == 0



# Miscellaneous


    @classmethod
    def agg_to_geo_color(cls, agg, grid, ipj, res):
        """
        Create a Geosoft color grid from an aggregate.
        
        :param agg:   Input Aggregate
        :param grid:  Output image name
        :param ipj:   Projection to use
        :param res:   Resolution (Cell Size) size to use
        :type  agg:   GXAGG
        :type  grid:  str
        :type  ipj:   GXIPJ
        :type  res:   float

        .. versionadded:: 5.1.6

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** This consumes a very small amount of memory
        """
        gxapi_cy.WrapIMU._agg_to_geo_color(GXContext._get_tls_geo(), agg, grid.encode(), ipj, res)
        



    @classmethod
    def crc(cls, img, pul_crc):
        """
        Computes a CRC Checksum on an image.
        
        :param img:      Input image
        :param pul_crc:  Starting CRC (use `CRC_INIT_VALUE <geosoft.gxapi.CRC_INIT_VALUE>` if none)
        :type  img:      GXIMG
        :type  pul_crc:  int

        :returns:        CRC value
        :rtype:          int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = gxapi_cy.WrapIMU._crc(GXContext._get_tls_geo(), img, pul_crc)
        return ret_val



    @classmethod
    def crc_grid(cls, grid, pul_crc):
        """
        Computes a CRC Checksum on a grid.
        
        :param grid:     Grid
        :param pul_crc:  Starting CRC (use `CRC_INIT_VALUE <geosoft.gxapi.CRC_INIT_VALUE>` if none)
        :type  grid:     str
        :type  pul_crc:  int

        :returns:        CRC value
        :rtype:          int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = gxapi_cy.WrapIMU._crc_grid(GXContext._get_tls_geo(), grid.encode(), pul_crc)
        return ret_val



    @classmethod
    def crc_grid_inexact(cls, grid, pul_crc, float_bits, double_bits):
        """
        Computes a CRC Checksum on a grid and allows you to specify
        number of bits of floats/doubles to drop so that the CRC
        will be same even of this are changed.
        
        :param grid:         Grid
        :param pul_crc:      Starting CRC (use `CRC_INIT_VALUE <geosoft.gxapi.CRC_INIT_VALUE>` if none)
        :param float_bits:   :ref:`IMU_FLOAT_CRC_BITS`
        :param double_bits:  :ref:`IMU_DOUBLE_CRC_BITS`
        :type  grid:         str
        :type  pul_crc:      int
        :type  float_bits:   int
        :type  double_bits:  int

        :returns:            CRC value
        :rtype:              int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Very useful for testing where the last bits of accuracy
        are not as important.
        """
        ret_val = gxapi_cy.WrapIMU._crc_grid_inexact(GXContext._get_tls_geo(), grid.encode(), pul_crc, float_bits, double_bits)
        return ret_val



    @classmethod
    def crc_inexact(cls, img, pul_crc, float_bits, double_bits):
        """
        Computes a CRC Checksum on an image and allows you to specify
        number of bits of floats/doubles to drop so that the CRC
        will be same even of this are changed.
        
        :param img:          Input image
        :param pul_crc:      Starting CRC (use `CRC_INIT_VALUE <geosoft.gxapi.CRC_INIT_VALUE>` if none)
        :param float_bits:   :ref:`IMU_FLOAT_CRC_BITS`
        :param double_bits:  :ref:`IMU_DOUBLE_CRC_BITS`
        :type  img:          GXIMG
        :type  pul_crc:      int
        :type  float_bits:   int
        :type  double_bits:  int

        :returns:            CRC value
        :rtype:              int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Very useful for testing where the last bits of accuracy
        are not as important.
        """
        ret_val = gxapi_cy.WrapIMU._crc_inexact(GXContext._get_tls_geo(), img, pul_crc, float_bits, double_bits)
        return ret_val



    @classmethod
    def export_grid_without_data_section_xml(cls, grid, crc, file):
        """
        Export a Grid minus the data section as an XML file.
        
        :param grid:  Grid
        :param crc:   CRC returned
        :param file:  Output XML file
        :type  grid:  str
        :type  crc:   int_ref
        :type  file:  str

        .. versionadded:: 7.2

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        crc.value = gxapi_cy.WrapIMU._export_grid_without_data_section_xml(GXContext._get_tls_geo(), grid.encode(), crc.value, file.encode())
        



    @classmethod
    def export_grid_xml(cls, grid, crc, file):
        """
        Export a Grid as an XML file.
        
        :param grid:  Grid
        :param crc:   CRC returned
        :param file:  Output XML file
        :type  grid:  str
        :type  crc:   int_ref
        :type  file:  str

        .. versionadded:: 6.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        crc.value = gxapi_cy.WrapIMU._export_grid_xml(GXContext._get_tls_geo(), grid.encode(), crc.value, file.encode())
        



    @classmethod
    def export_raw_xml(cls, img, crc, file):
        """
        Export a Grid as an XML file using a fast raw output.
        
        :param img:   Image
        :param crc:   CRC returned
        :param file:  Output XML file
        :type  img:   GXIMG
        :type  crc:   int_ref
        :type  file:  str

        .. versionadded:: 7.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        crc.value = gxapi_cy.WrapIMU._export_raw_xml(GXContext._get_tls_geo(), img, crc.value, file.encode())
        



    @classmethod
    def export_xml(cls, img, crc, file):
        """
        Export a Grid as an XML file.
        
        :param img:   Image
        :param crc:   CRC returned
        :param file:  Output XML file
        :type  img:   GXIMG
        :type  crc:   int_ref
        :type  file:  str

        .. versionadded:: 6.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        crc.value = gxapi_cy.WrapIMU._export_xml(GXContext._get_tls_geo(), img, crc.value, file.encode())
        



    @classmethod
    def get_zvv(cls, img, vv_x, vv_y, vv_z):
        """
        Extract an interpolated image value for given XY `GXVV <geosoft.gxapi.GXVV>` locations
        
        :param img:   Input grid
        :param vv_x:  X `GXVV <geosoft.gxapi.GXVV>`
        :param vv_y:  Y `GXVV <geosoft.gxapi.GXVV>`
        :param vv_z:  Z `GXVV <geosoft.gxapi.GXVV>` filled with values (set to be same size as X, Y)
        :type  img:   GXIMG
        :type  vv_x:  GXVV
        :type  vv_y:  GXVV
        :type  vv_z:  GXVV

        .. versionadded:: 5.0.8

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        gxapi_cy.WrapIMU._get_zvv(GXContext._get_tls_geo(), img, vv_x, vv_y, vv_z)
        



    @classmethod
    def get_z_peaks_vv(cls, img, vv_x, vv_y, vv_z):
        """
        Same as `get_zvv <geosoft.gxapi.GXIMU.get_zvv>`, but find the closest peak value to the input locations, and return
        				             the peak value and peak value location.
        
        :param img:   Input grid
        :param vv_x:  X `GXVV <geosoft.gxapi.GXVV>`
        :param vv_y:  Y `GXVV <geosoft.gxapi.GXVV>`
        :param vv_z:  Z `GXVV <geosoft.gxapi.GXVV>` filled with values (set to be same size as X, Y)
        :type  img:   GXIMG
        :type  vv_x:  GXVV
        :type  vv_y:  GXVV
        :type  vv_z:  GXVV

        .. versionadded:: 9.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** The returned locations will always be a grid point location; no interpolation is performed when locating the peaks. A simple search is
        				done of all neighbouring points from the starting point, and once no neighbours can be located with a higher value, the search stops.
        """
        gxapi_cy.WrapIMU._get_z_peaks_vv(GXContext._get_tls_geo(), img, vv_x, vv_y, vv_z)
        



    @classmethod
    def grid_add(cls, img1, m1, img2, m2, imgo):
        """
        Adds two Grid images together point-by-point.
        
        :param img1:  Image of first grid
        :param m1:    Multiplier to operate on first grid image
        :param img2:  Image of second grid
        :param m2:    Multiplier to operate on second grid image
        :param imgo:  Output grid image
        :type  img1:  GXIMG
        :type  m1:    float
        :type  img2:  GXIMG
        :type  m2:    float
        :type  imgo:  GXIMG

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** The `GXIMG <geosoft.gxapi.GXIMG>` parameters MUST be of type `GS_DOUBLE <geosoft.gxapi.GS_DOUBLE>`!
        If not, the method will terminate.
        """
        gxapi_cy.WrapIMU._grid_add(GXContext._get_tls_geo(), img1, m1, img2, m2, imgo)
        



    @classmethod
    def grid_agc(cls, i_img, o_img, width, max_gain, remove_background):
        """
        Automatic Gain Compensation of a grid.
        
        :param i_img:              Image of input grid
        :param o_img:              Image of output grid
        :param width:              Width of filter to separate signal from background.
        :param max_gain:           Maximum gain applied to the signal.
        :param remove_background:  Remove background before applying gain?
        :type  i_img:              GXIMG
        :type  o_img:              GXIMG
        :type  width:              int
        :type  max_gain:           float
        :type  remove_background:  int

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** The `GXIMG <geosoft.gxapi.GXIMG>` parameters MUST be of type `GS_FLOAT <geosoft.gxapi.GS_FLOAT>`!
        If not, the method will terminate.
        """
        gxapi_cy.WrapIMU._grid_agc(GXContext._get_tls_geo(), i_img, o_img, width, max_gain, remove_background)
        



    @classmethod
    def grid_bool(cls, img1, img2, out, bool, sizing, olap):
        """
        Mask one grid against another using boolean logic
        operations.
        
        :param img1:    Image of first input grid
        :param img2:    Image of second input grid
        :param out:     File name of output grid
        :param bool:    :ref:`IMU_BOOL_OPT`
        :param sizing:  :ref:`IMU_BOOL_SIZING`
        :param olap:    :ref:`IMU_BOOL_OLAP`
        :type  img1:    GXIMG
        :type  img2:    GXIMG
        :type  out:     str
        :type  bool:    int
        :type  sizing:  int
        :type  olap:    int

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** The `GXIMG <geosoft.gxapi.GXIMG>` parameters must be of type `GS_DOUBLE <geosoft.gxapi.GS_DOUBLE>`!
        If not, the method will terminate.
        """
        gxapi_cy.WrapIMU._grid_bool(GXContext._get_tls_geo(), img1, img2, out.encode(), bool, sizing, olap)
        



    @classmethod
    def grid_edge(cls, grid, vv_x, vv_y):
        """
        Get grid edge points
        
        :param grid:  Grid file name
        :param vv_x:  X coordinates of edge points
        :param vv_y:  Y coordinates of edge points
        :type  grid:  str
        :type  vv_x:  GXVV
        :type  vv_y:  GXVV

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        gxapi_cy.WrapIMU._grid_edge(GXContext._get_tls_geo(), grid.encode(), vv_x, vv_y)
        



    @classmethod
    def grid_edge_ply(cls, img, ply, min_points):
        """
        Get grid edge points
        
        :param img:         The Grid
        :param ply:         `GXPLY <geosoft.gxapi.GXPLY>` containing the edges.
        :param min_points:  Minimum number of points in polygons (0 for all)
        :type  img:         GXIMG
        :type  ply:         GXPLY
        :type  min_points:  int

        .. versionadded:: 5.1.8

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** Unlike `grid_ply <geosoft.gxapi.GXIMU.grid_ply>` and GridPlyEx_IMU, the image is not
        altered. It just gives the `GXPLY <geosoft.gxapi.GXPLY>`.
        """
        gxapi_cy.WrapIMU._grid_edge_ply(GXContext._get_tls_geo(), img, ply, min_points)
        



    @classmethod
    def grid_expand(cls, im_gi, out, per, shape, x, y):
        """
        Expand a grid and place dummies in the area
        beyond the original edges.
        
        :param im_gi:  Image of input grid
        :param out:    File name of output grid
        :param per:    Minimum percentage to expand the grid by
        :param shape:  :ref:`IMU_EXPAND_SHAPE`
        :param x:      X Dimension the output grid is expanded to
        :param y:      Y Dimension the output grid is expanded to
        :type  im_gi:  GXIMG
        :type  out:    str
        :type  per:    float
        :type  shape:  int
        :type  x:      int
        :type  y:      int

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** The `GXIMG <geosoft.gxapi.GXIMG>` parameter MUST be of type `GS_FLOAT <geosoft.gxapi.GS_FLOAT>`!
        If not, the method will terminate.
        """
        gxapi_cy.WrapIMU._grid_expand(GXContext._get_tls_geo(), im_gi, out.encode(), per, shape, x, y)
        



    @classmethod
    def grid_exp_fill(cls, in_grd, out_grd, p_ex, t_ex):
        """
        Extends and fills a grid for `GXFFT2 <geosoft.gxapi.GXFFT2>`.
        
        :param in_grd:   Name of the input grid
        :param out_grd:  Name of the output grid
        :param p_ex:     % expansion
        :param t_ex:     Shape of expansion: 0 - rectangle, 1 - square
        :type  in_grd:   str
        :type  out_grd:  str
        :type  p_ex:     float
        :type  t_ex:     int

        .. versionadded:: 7.2

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        gxapi_cy.WrapIMU._grid_exp_fill(GXContext._get_tls_geo(), in_grd.encode(), out_grd.encode(), p_ex, t_ex)
        



    @classmethod
    def grid_fill(cls, im_gi, im_go, rollopt, rolldist, mxf, mxp, rollbase, alimit, elimit, width, npass):
        """
        Interpolates to fill dummies, generates an output grid.
        
        :param im_gi:     Image of input grid
        :param im_go:     Image of output grid
        :param rollopt:   :ref:`IMU_FILL_ROLLOPT`
        :param rolldist:  Distance at which to roll off to 0
        :param mxf:       Maximum prediction filter length
        :param mxp:       Maximum prediction filter area
        :param rollbase:  Base value to roll off to
        :param alimit:    Maximum amplitude allowed in grid
        :param elimit:    Maximum edge amplitude allowed in grid
        :param width:     Width from edge to start limiting from
        :param npass:     Number of convolution passes to apply
        :type  im_gi:     GXIMG
        :type  im_go:     GXIMG
        :type  rollopt:   int
        :type  rolldist:  int
        :type  mxf:       int
        :type  mxp:       int
        :type  rollbase:  float
        :type  alimit:    float
        :type  elimit:    float
        :type  width:     int
        :type  npass:     int

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** The `GXIMG <geosoft.gxapi.GXIMG>` parameters MUST be of type `GS_FLOAT <geosoft.gxapi.GS_FLOAT>`!
        If not, the method will terminate.
        """
        gxapi_cy.WrapIMU._grid_fill(GXContext._get_tls_geo(), im_gi, im_go, rollopt, rolldist, mxf, mxp, rollbase, alimit, elimit, width, npass)
        



    @classmethod
    def grid_filt(cls, img, imgo, passes, mult, dum, hz, usefile, file, vv):
        """
        Applies a filter to a grid any number
        of passes.
        
        :param img:      Image of first grid
        :param imgo:     Image of second grid
        :param passes:   Number of passes to apply filter (>0)
        :param mult:     Multiplier to apply to grid values
        :param dum:      :ref:`IMU_FILT_DUMMY`
        :param hz:       :ref:`IMU_FILT_HZDRV`
        :param usefile:  :ref:`IMU_FILT_FILE`
        :param file:     Name of file containing filter values
        :param vv:       `GXVV <geosoft.gxapi.GXVV>` containing filter values (if not using a file for the values) MUST BE OF TYPE 'real'
        :type  img:      GXIMG
        :type  imgo:     GXIMG
        :type  passes:   int
        :type  mult:     float
        :type  dum:      int
        :type  hz:       int
        :type  usefile:  int
        :type  file:     str
        :type  vv:       GXVV

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** The `GXIMG <geosoft.gxapi.GXIMG>` parameters MUST be of type `GS_FLOAT <geosoft.gxapi.GS_FLOAT>`!
        If not, the method will terminate.
        """
        gxapi_cy.WrapIMU._grid_filt(GXContext._get_tls_geo(), img, imgo, passes, mult, dum, hz, usefile, file.encode(), vv)
        



    @classmethod
    def grid_head(cls, grid, esep, vsep, x_orig, y_orig, rot):
        """
        Modifies Statistics contained in a grid header.
        
        :param grid:    Name of the grid whose header is to be modified.
        :param esep:    Element separation
        :param vsep:    Vector separation
        :param x_orig:  Grid X Origin on ground
        :param y_orig:  Grid Y Origin on ground
        :param rot:     Grid Rotation
        :type  grid:    str
        :type  esep:    float
        :type  vsep:    float
        :type  x_orig:  float
        :type  y_orig:  float
        :type  rot:     float

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        gxapi_cy.WrapIMU._grid_head(GXContext._get_tls_geo(), grid.encode(), esep, vsep, x_orig, y_orig, rot)
        



    @classmethod
    def grid_in_fill(cls, im_gi, out_grd, extend, iter):
        """
        Fill in a ribbon along the edge and inside hollow areas of the grid
        
        :param im_gi:    Image of input grid
        :param out_grd:  Name of the output grid
        :param extend:   Number of cells to extend ribbon along the edge
        :param iter:     Number of iterations to fill inside hollow areas
        :type  im_gi:    GXIMG
        :type  out_grd:  str
        :type  extend:   int
        :type  iter:     int

        .. versionadded:: 7.2

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        gxapi_cy.WrapIMU._grid_in_fill(GXContext._get_tls_geo(), im_gi, out_grd.encode(), extend, iter)
        



    @classmethod
    def grid_mask(cls, in_grid, m_grid, pply, mode):
        """
        Create a mask grid using a set of polygon
        coordinates defined in a separate file, then
        masking the polygon over an input grid.
        
        :param in_grid:  Name of input grid
        :param m_grid:   Name of output mask grid file
        :param pply:     Polygon containing mask coordinates
        :param mode:     :ref:`IMU_MASK`
        :type  in_grid:  str
        :type  m_grid:   str
        :type  pply:     GXPLY
        :type  mode:     int

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** The `GXIMG <geosoft.gxapi.GXIMG>` parameters MUST be of type `GS_DOUBLE <geosoft.gxapi.GS_DOUBLE>`!
        If not, the method will terminate.

        The `GXPLY <geosoft.gxapi.GXPLY>` will contain more than one polygon
        if it was loaded from a file containing
        coordinates of more than one polygon.
        """
        gxapi_cy.WrapIMU._grid_mask(GXContext._get_tls_geo(), in_grid.encode(), m_grid.encode(), pply, mode)
        



    @classmethod
    def grid_peak(cls, grid, nlmt, v_vx, v_vy, v_vz):
        """
        Pick grid peaks.
        
        :param grid:  Grid file name
        :param nlmt:  Peak test directions (1 to 4)
        :param v_vx:  X of found peaks
        :param v_vy:  Y of found peaks
        :param v_vz:  Z values of found peaks
        :type  grid:  str
        :type  nlmt:  int
        :type  v_vx:  GXVV
        :type  v_vy:  GXVV
        :type  v_vz:  GXVV

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** Peak test directions defines how grid peaks are to be found.
        For example, with the 1, a grid point will be picked if its
        value is greater than it's two neighbors in at least one
        direction.  Up to 4 directions can be tested.
        """
        gxapi_cy.WrapIMU._grid_peak(GXContext._get_tls_geo(), grid.encode(), nlmt, v_vx, v_vy, v_vz)
        



    @classmethod
    def grid_ply(cls, img, ply, refresh):
        """
        Get the grid edge in a `GXPLY <geosoft.gxapi.GXPLY>`
        
        :param img:      The `GXIMG <geosoft.gxapi.GXIMG>`
        :param ply:      `GXPLY <geosoft.gxapi.GXPLY>` to which the bounding polygons will be added.
        :param refresh:  TRUE to force the boundary to be refreshed.
        :type  img:      GXIMG
        :type  ply:      GXPLY
        :type  refresh:  int

        .. versionadded:: 5.1

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** This will optionally refresh the grid boundary `GXPLY <geosoft.gxapi.GXPLY>` and return
        the `GXPLY <geosoft.gxapi.GXPLY>`.

        If the boundary is not refreshed and has never been calculated,
        the boundary will be the bounding rectangle of the grid.

        The grid `GXPLY <geosoft.gxapi.GXPLY>` will be added to existing ploygons in the passed `GXPLY <geosoft.gxapi.GXPLY>`.
        """
        gxapi_cy.WrapIMU._grid_ply(GXContext._get_tls_geo(), img, ply, refresh)
        



    @classmethod
    def grid_ply_ex(cls, img, ply, refresh, min_points):
        """
        Get the grid edge in a `GXPLY <geosoft.gxapi.GXPLY>` (with min points)
        
        :param img:         The `GXIMG <geosoft.gxapi.GXIMG>`
        :param ply:         `GXPLY <geosoft.gxapi.GXPLY>` to which the bounding polygons will be added.
        :param refresh:     TRUE to force the boundary to be refreshed.
        :param min_points:  Minimum number of points in polygons refreshed (0 for all)
        :type  img:         GXIMG
        :type  ply:         GXPLY
        :type  refresh:     int
        :type  min_points:  int

        .. versionadded:: 5.1.6

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** This will optionally refresh the grid boundary `GXPLY <geosoft.gxapi.GXPLY>` and return
        the `GXPLY <geosoft.gxapi.GXPLY>`.

        If the boundary is not refreshed and has never been calculated,
        the boundary will be the bounding rectangle of the grid.

        The grid `GXPLY <geosoft.gxapi.GXPLY>` will be added to existing ploygons in the passed `GXPLY <geosoft.gxapi.GXPLY>`.
        """
        gxapi_cy.WrapIMU._grid_ply_ex(GXContext._get_tls_geo(), img, ply, refresh, min_points)
        



    @classmethod
    def grid_reproject_and_window(cls, input_grid_filename, output_grid_filename, new_projection, min_x, max_x, min_y, max_y):
        """
        Create a new grid by reprojecting an existing grid and windowing its contents
        
        :param input_grid_filename:   Input grid filename
        :param output_grid_filename:  Output grid filename
        :param new_projection:        Output grid projection
        :param min_x:                 Window minX (in output projection)
        :param max_x:                 Window maxX (in output projection)
        :param min_y:                 Window minY (in output projection)
        :param max_y:                 Window maxY (in output projection)
        :type  input_grid_filename:   str
        :type  output_grid_filename:  str
        :type  new_projection:        GXIPJ
        :type  min_x:                 float
        :type  max_x:                 float
        :type  min_y:                 float
        :type  max_y:                 float

        .. versionadded:: 7.3

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        gxapi_cy.WrapIMU._grid_reproject_and_window(GXContext._get_tls_geo(), input_grid_filename.encode(), output_grid_filename.encode(), new_projection, min_x, max_x, min_y, max_y)
        



    @classmethod
    def grid_resample(cls, input_grid_filename, output_grid_filename, o_x, o_y, d_x, d_y, n_x, n_y):
        """
        Create a new grid by resampling an existing grid
        
        :param input_grid_filename:   Input grid filename
        :param output_grid_filename:  Output grid filename
        :param o_x:                   Origin X
        :param o_y:                   Origin Y
        :param d_x:                   Cell spacing X
        :param d_y:                   Cell spacing Y
        :param n_x:                   Elements in X
        :param n_y:                   Elements in Y
        :type  input_grid_filename:   str
        :type  output_grid_filename:  str
        :type  o_x:                   float
        :type  o_y:                   float
        :type  d_x:                   float
        :type  d_y:                   float
        :type  n_x:                   int
        :type  n_y:                   int

        .. versionadded:: 7.3

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Works only for un rotated grids.
        """
        gxapi_cy.WrapIMU._grid_resample(GXContext._get_tls_geo(), input_grid_filename.encode(), output_grid_filename.encode(), o_x, o_y, d_x, d_y, n_x, n_y)
        



    @classmethod
    def grid_resize(cls, in_grd, out_grd):
        """
        Resize a grid to reduce the size not cover the outside dummies.
        
        :param in_grd:   File name of input grid
        :param out_grd:  File name of output grid
        :type  in_grd:   str
        :type  out_grd:  str

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        gxapi_cy.WrapIMU._grid_resize(GXContext._get_tls_geo(), in_grd.encode(), out_grd.encode())
        



    @classmethod
    def grid_shad(cls, in_grid, sh_grid, inc, dec, scl):
        """
        Create a shaded relief image.
        
        :param in_grid:  Input image name
        :param sh_grid:  Output new shaded image
        :param inc:      Inclination 0-90 degrees (def. 45)
        :param dec:      Declination 0-360 degrees azimuth (def. 45)
        :param scl:      Vertical scale factor (distance/z unit)
        :type  in_grid:  str
        :type  sh_grid:  str
        :type  inc:      float_ref
        :type  dec:      float_ref
        :type  scl:      float_ref

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Pass `GS_R8DM <geosoft.gxapi.GS_R8DM>` as parameters to obtain default values.
        The default values are returned.
        """
        inc.value, dec.value, scl.value = gxapi_cy.WrapIMU._grid_shad(GXContext._get_tls_geo(), in_grid.encode(), sh_grid.encode(), inc.value, dec.value, scl.value)
        



    @classmethod
    def refresh_shad(cls, in_img, sh_img, inc, dec, scl):
        """
        Refresh a shaded relief image
        
        :param in_img:  Input grid object
        :param sh_img:  Output shaded grid object
        :param inc:     Inclination 0-90 degrees (def. 45)
        :param dec:     Declination 0-360 degrees azimuth (def. 45)
        :param scl:     Vertical scale factor (distance/z unit)
        :type  in_img:  GXIMG
        :type  sh_img:  GXIMG
        :type  inc:     float_ref
        :type  dec:     float_ref
        :type  scl:     float_ref

        .. versionadded:: 9.4

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Pass `GS_R8DM <geosoft.gxapi.GS_R8DM>` as parameters to obtain default values.
        The default values are returned.
        """
        inc.value, dec.value, scl.value = gxapi_cy.WrapIMU._refresh_shad(GXContext._get_tls_geo(), in_img, sh_img, inc.value, dec.value, scl.value)
        



    @classmethod
    def grid_st(cls, grid, st):
        """
        Update an `GXST <geosoft.gxapi.GXST>` object using a grid.
        
        :param grid:  Grid name
        :param st:    `GXST <geosoft.gxapi.GXST>` (statistics) object to fill/update
        :type  grid:  str
        :type  st:    GXST

        .. versionadded:: 5.1.2

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** The input `GXST <geosoft.gxapi.GXST>` object is not initialized by `grid_st <geosoft.gxapi.GXIMU.grid_st>`,
        so this function can be used to accumulate statistical
        info on more than a single grid.
        See `GXST <geosoft.gxapi.GXST>`.
        """
        gxapi_cy.WrapIMU._grid_st(GXContext._get_tls_geo(), grid.encode(), st)
        



    @classmethod
    def grid_stat(cls, grid, type, xelem, yelem, xsep, ysep, kx, x_orig, y_orig, rot, base, mult):
        """
        Reports statistics contained in a grid header.
        
        :param grid:    Name of the grid to get stats from
        :param type:    Element type in bytes
        :param xelem:   Elements in X direction
        :param yelem:   Elements in Y direction
        :param xsep:    X element separation
        :param ysep:    Y element separation
        :param kx:      KX (storage orientation)
        :param x_orig:  X origin
        :param y_orig:  Y origin
        :param rot:     Grid Rotation
        :param base:    Base removed
        :param mult:    Grid multiplier
        :type  grid:    str
        :type  type:    int_ref
        :type  xelem:   int_ref
        :type  yelem:   int_ref
        :type  xsep:    float_ref
        :type  ysep:    float_ref
        :type  kx:      int_ref
        :type  x_orig:  float_ref
        :type  y_orig:  float_ref
        :type  rot:     float_ref
        :type  base:    float_ref
        :type  mult:    float_ref

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Statistics are returned in the parameter set
        """
        type.value, xelem.value, yelem.value, xsep.value, ysep.value, kx.value, x_orig.value, y_orig.value, rot.value, base.value, mult.value = gxapi_cy.WrapIMU._grid_stat(GXContext._get_tls_geo(), grid.encode(), type.value, xelem.value, yelem.value, xsep.value, ysep.value, kx.value, x_orig.value, y_orig.value, rot.value, base.value, mult.value)
        



    @classmethod
    def grid_stat_comp(cls, grid, type, xelem, yelem, xsep, ysep, kx, x_orig, y_orig, rot, base, mult, comp):
        """
        Reports statistics contained in a grid header.
        
        :param grid:    Name of the grid to get stats from
        :param type:    Element type: 0 - byte 1 - USHORT 2 - SHORT 3 - LONG 4 - FLOAT 5 - DOUBLE 6 - 32 byte Color (RGBx)
        :param xelem:   Elements in X direction
        :param yelem:   Elements in Y direction
        :param xsep:    X element separation
        :param ysep:    Y element separation
        :param kx:      KX (storage orientation)
        :param x_orig:  X origin
        :param y_orig:  Y origin
        :param rot:     Grid Rotation
        :param base:    Base removed
        :param mult:    Grid multiplier
        :param comp:    Compression Ratio
        :type  grid:    str
        :type  type:    int_ref
        :type  xelem:   int_ref
        :type  yelem:   int_ref
        :type  xsep:    float_ref
        :type  ysep:    float_ref
        :type  kx:      int_ref
        :type  x_orig:  float_ref
        :type  y_orig:  float_ref
        :type  rot:     float_ref
        :type  base:    float_ref
        :type  mult:    float_ref
        :type  comp:    float_ref

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Statistics are returned in the parameter set
        """
        type.value, xelem.value, yelem.value, xsep.value, ysep.value, kx.value, x_orig.value, y_orig.value, rot.value, base.value, mult.value, comp.value = gxapi_cy.WrapIMU._grid_stat_comp(GXContext._get_tls_geo(), grid.encode(), type.value, xelem.value, yelem.value, xsep.value, ysep.value, kx.value, x_orig.value, y_orig.value, rot.value, base.value, mult.value, comp.value)
        



    @classmethod
    def grid_stat_ext(cls, grid, force, items, dums, min, max, mean, stddev):
        """
        Reports statistics of a grid's elements.
        
        :param grid:    Name of the grid to get stats from
        :param force:   :ref:`IMU_STAT_FORCED`
        :param items:   Number of valid elements in grid
        :param dums:    Number of dummies in grid
        :param min:     Minimum grid value
        :param max:     Maximum grid value
        :param mean:    Grid mean
        :param stddev:  Grid standard deviation
        :type  grid:    str
        :type  force:   int
        :type  items:   int_ref
        :type  dums:    int_ref
        :type  min:     float_ref
        :type  max:     float_ref
        :type  mean:    float_ref
        :type  stddev:  float_ref

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** If the :ref:`IMU_STAT_FORCED` value is set, the
        statistics will be recalculated.
        Statistics are returned in the parameter set.
        """
        items.value, dums.value, min.value, max.value, mean.value, stddev.value = gxapi_cy.WrapIMU._grid_stat_ext(GXContext._get_tls_geo(), grid.encode(), force, items.value, dums.value, min.value, max.value, mean.value, stddev.value)
        



    @classmethod
    def grid_stat_trend(cls, grid, trend_valid, co, cx, cy):
        """
        Reports Trend Info of a grid (for first order coefficients only).
        
        :param grid:         Name of the grid to get stats from
        :param trend_valid:  Trend Valid Flag
        :param co:           Trend coefficient rCo
        :param cx:           Trend coefficient rCx
        :param cy:           Trend coefficient rCy
        :type  grid:         str
        :type  trend_valid:  int_ref
        :type  co:           float_ref
        :type  cx:           float_ref
        :type  cy:           float_ref

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** Trend Info are returned in the parameter set
        """
        trend_valid.value, co.value, cx.value, cy.value = gxapi_cy.WrapIMU._grid_stat_trend(GXContext._get_tls_geo(), grid.encode(), trend_valid.value, co.value, cx.value, cy.value)
        



    @classmethod
    def grid_stat_trend_ext(cls, grid, order, num_coef, xo, yo, vm):
        """
        Reports Extended Trend Info of a grid (for up to third order coefficients).
        
        :param grid:      Grid name
        :param order:     Trend order
        :param num_coef:  Number of coefficients
        :param xo:        Trend origin Xo
        :param yo:        Trend origin Yo
        :param vm:        `GXVM <geosoft.gxapi.GXVM>` hold coefficient values MUST BE OF TYPE 'real'
        :type  grid:      str
        :type  order:     int_ref
        :type  num_coef:  int_ref
        :type  xo:        float_ref
        :type  yo:        float_ref
        :type  vm:        GXVM

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** Trend Info are returned in the parameter set
        """
        order.value, num_coef.value, xo.value, yo.value = gxapi_cy.WrapIMU._grid_stat_trend_ext(GXContext._get_tls_geo(), grid.encode(), order.value, num_coef.value, xo.value, yo.value, vm)
        



    @classmethod
    def slope_standard_deviation(cls, img):
        """
        Return the standard deviation of the slopes.
        
        :param img:  Grid object
        :type  img:  GXIMG

        :returns:    Standard deviation of grid slopes
        :rtype:      float

        .. versionadded:: 8.2

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** This method calculates the standard deviation of the horizontal
        differences in the X and Y directions for the supplied
        image.  This is useful for shading routines.  A good
        default scaling factor is 2.5 / standard deviation.

        The image will be sub-sampled to a statistically meaningful number.

        The cell sizes are used to determine the slopes.
        """
        ret_val = gxapi_cy.WrapIMU._slope_standard_deviation(GXContext._get_tls_geo(), img)
        return ret_val



    @classmethod
    def grid_stitch(cls, grid1, grid2, grid3, method, tr_order1, tr_order2, tr_calc, gap, spline, path, pply, weighting, width):
        """
        Stitches together too grids
        
        :param grid1:      Input Grid1 name
        :param grid2:      Input Grid2 name
        :param grid3:      Output Grid name
        :param method:     Stitching method
        :param tr_order1:  Grid 1 trend removal order
        :param tr_order2:  Grid 2 trend removal order
        :param tr_calc:    Trend removal type of points to use
        :param gap:        Gap for interpolation
        :param spline:     Interpolation spline method
        :param path:       Path selection
        :param pply:       `GXPLY <geosoft.gxapi.GXPLY>` object for user path
        :param weighting:  Correction weighting
        :param width:      Width of corrections, in grid cells (8 to 256)
        :type  grid1:      str
        :type  grid2:      str
        :type  grid3:      str
        :type  method:     int
        :type  tr_order1:  int
        :type  tr_order2:  int
        :type  tr_calc:    int
        :type  gap:        float
        :type  spline:     int
        :type  path:       int
        :type  pply:       GXPLY
        :type  weighting:  float
        :type  width:      int

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        gxapi_cy.WrapIMU._grid_stitch(GXContext._get_tls_geo(), grid1.encode(), grid2.encode(), grid3.encode(), method, tr_order1, tr_order2, tr_calc, gap, spline, path, pply, weighting, width)
        



    @classmethod
    def grid_stitch_ctl(cls, ctl):
        """
        Stitches together two grids - control file for options.
        
        :param ctl:  Control file containing all "GRIDSTCH" parameters
        :type  ctl:  str

        .. versionadded:: 5.1.4

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** Data validation is done internally, not in the GX.
        This is simply a way of avoiding writing a new GX wrapper
        every time an option is added.
        """
        gxapi_cy.WrapIMU._grid_stitch_ctl(GXContext._get_tls_geo(), ctl.encode())
        



    @classmethod
    def grid_tiff(cls, grds, tiff, bcol, red, green, blue, csize, reg, scale):
        """
        Generate a Tiff (Tagged-Image file format) file with up to 16 grids.
        
        :param grds:   Comma-delimited string containing names of all grids to use in Tiff generation Up to 16 grids allowed.
        :param tiff:   Name of Tiff file to create
        :param bcol:   Background color option. One of W (White)  K (Black) C (Cyan) M (Magenta) Y (Yellow) R (Red)  G (Green) B (Blue)
        :param red:    Background Red value (0-255)
        :param green:  Background Green (0-255)
        :param blue:   Background Blue  (0-255)
        :param csize:  New cell size
        :param reg:    Pixel size of registration marks
        :param scale:  Map scale
        :type  grds:   str
        :type  tiff:   str
        :type  bcol:   str
        :type  red:    int
        :type  green:  int
        :type  blue:   int
        :type  csize:  float
        :type  reg:    int
        :type  scale:  float

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** The background color can be either selected
        from one of 8 settings, or can be specified
        as a combination of Reg,Green, and Blue values.
        """
        gxapi_cy.WrapIMU._grid_tiff(GXContext._get_tls_geo(), grds.encode(), tiff.encode(), bcol.encode(), red, green, blue, csize, reg, scale)
        



    @classmethod
    def grid_trnd(cls, imgi, imgo, tr_option, edge, order, vm, num_coefs):
        """
        Remove a trend surface from a grid.
        
        :param imgi:       Handle to input image
        :param imgo:       Handle to output image
        :param tr_option:  0-calculate, 1-given, 2-replace
        :param edge:       :ref:`IMU_TREND`
        :param order:      Trend order
        :param vm:         `GXVM <geosoft.gxapi.GXVM>` holds coefficients
        :param num_coefs:  Number of coefficients
        :type  imgi:       GXIMG
        :type  imgo:       GXIMG
        :type  tr_option:  int
        :type  edge:       int
        :type  order:      int
        :type  vm:         GXVM
        :type  num_coefs:  int

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** Both Images must be of type `GS_DOUBLE <geosoft.gxapi.GS_DOUBLE>`.
        The `GXVM <geosoft.gxapi.GXVM>` parameter must be of type REAL,
        and be of size 10 at most.

        The number of coefficients must be
        compatible with the order of the
        trend removed. Following is the
        number of coefficients which should
        be present for a given order

        ===== ======================
        Order Number of Coefficients
        ----- ----------------------
        0      1
        1      3
        2      6
        3      10
        ===== ======================
        """
        gxapi_cy.WrapIMU._grid_trnd(GXContext._get_tls_geo(), imgi, imgo, tr_option, edge, order, vm, num_coefs)
        



    @classmethod
    def grid_trns(cls, grid, tcon):
        """
        Transpose a grid by swapping the grid rows with
        the grid columns.
        
        :param grid:  Name of the grid to transpose
        :param tcon:  Transpose condition value :ref:`IMU_TRANS`
        :type  grid:  str
        :type  tcon:  int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** If the grid has a line orientation that does NOT
        match the :ref:`IMU_TRANS` value, this method will
        not succeed.
        """
        gxapi_cy.WrapIMU._grid_trns(GXContext._get_tls_geo(), grid.encode(), tcon)
        



    @classmethod
    def grid_vd(cls, im_gi, im_go):
        """
        Apply vertical derivative convolution filter to a grid.
        
        :param im_gi:  Input image
        :param im_go:  Output image
        :type  im_gi:  GXIMG
        :type  im_go:  GXIMG

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        gxapi_cy.WrapIMU._grid_vd(GXContext._get_tls_geo(), im_gi, im_go)
        



    @classmethod
    def grid_vol(cls, img, rbase, mult, vol_a, vol_b, diff):
        """
        Calculates the grid volumes above and below a
        reference base.
        
        :param img:    Image of the grid to calculate volume for
        :param rbase:  Reference base
        :param mult:   Multiplier to final volume
        :param vol_a:  Grid Volume above reference base
        :param vol_b:  Grid Volume below reference base
        :param diff:   Differences between volumes
        :type  img:    GXIMG
        :type  rbase:  float
        :type  mult:   float
        :type  vol_a:  float_ref
        :type  vol_b:  float_ref
        :type  diff:   float_ref

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** Volumes are calculated above and below a
        reference base level, and reported as positive
        integers. A multiplier is applied to the final
        volume (to correct for units).

        The `GXIMG <geosoft.gxapi.GXIMG>` parameters MUST be of type `GS_FLOAT <geosoft.gxapi.GS_FLOAT>`!
        If not, the method will terminate.
        """
        vol_a.value, vol_b.value, diff.value = gxapi_cy.WrapIMU._grid_vol(GXContext._get_tls_geo(), img, rbase, mult, vol_a.value, vol_b.value, diff.value)
        



    @classmethod
    def grid_wind(cls, img, out, coord, xmin, xmax, ymin, ymax, zmin, zmax, csize, clip, dec, mdf):
        """
        Create a grid using a defined area window
        within a larger grid.
        
        :param img:    Image of input grid
        :param out:    Name of output grid file
        :param coord:  :ref:`IMU_WIND_COORD`
        :param xmin:   Min. limit of window in X direction (can be `rDUMMY <geosoft.gxapi.rDUMMY>`)
        :param xmax:   Max. limit of window in X direction (can be `rDUMMY <geosoft.gxapi.rDUMMY>`)
        :param ymin:   Min. limit of window in Y direction (can be `rDUMMY <geosoft.gxapi.rDUMMY>`)
        :param ymax:   Max. limit of window in Y direction (can be `rDUMMY <geosoft.gxapi.rDUMMY>`)
        :param zmin:   Minimum Z data value in output grid (can be `rDUMMY <geosoft.gxapi.rDUMMY>`)
        :param zmax:   Maximum Z data value in output grid (can be `rDUMMY <geosoft.gxapi.rDUMMY>`)
        :param csize:  New grid cell size
        :param clip:   :ref:`IMU_WIND_DUMMIES`
        :param dec:    Decimation factor
        :param mdf:    Name of .MDF file for data clipping
        :type  img:    GXIMG
        :type  out:    str
        :type  coord:  int
        :type  xmin:   float
        :type  xmax:   float
        :type  ymin:   float
        :type  ymax:   float
        :type  zmin:   float
        :type  zmax:   float
        :type  csize:  float
        :type  clip:   int
        :type  dec:    int
        :type  mdf:    str

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        gxapi_cy.WrapIMU._grid_wind(GXContext._get_tls_geo(), img, out.encode(), coord, xmin, xmax, ymin, ymax, zmin, zmax, csize, clip, dec, mdf.encode())
        



    @classmethod
    def grid_wind2(cls, img, out, xmin, xmax, ymin, ymax, zmin, zmax, clip):
        """
        Window a grid.
        
        :param img:   Image of input grid
        :param out:   Name of output grid file
        :param xmin:  Minimum X, ground units (can be `rDUMMY <geosoft.gxapi.rDUMMY>`)
        :param xmax:  Maximum X (can be `rDUMMY <geosoft.gxapi.rDUMMY>`)
        :param ymin:  Minimum Y (can be `rDUMMY <geosoft.gxapi.rDUMMY>`)
        :param ymax:  Maximum Y (can be `rDUMMY <geosoft.gxapi.rDUMMY>`)
        :param zmin:  Minimum Z (can be `rDUMMY <geosoft.gxapi.rDUMMY>`)
        :param zmax:  Maximum Z (can be `rDUMMY <geosoft.gxapi.rDUMMY>`)
        :param clip:  :ref:`IMU_WIND_DUMMIES`
        :type  img:   GXIMG
        :type  out:   str
        :type  xmin:  float
        :type  xmax:  float
        :type  ymin:  float
        :type  ymax:  float
        :type  zmin:  float
        :type  zmax:  float
        :type  clip:  int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** To change the cell size or work in a different projection,
        first inherit the `GXIMG <geosoft.gxapi.GXIMG>` by calling

        The windowed grid will be adjusted/expanded to include the
        defined area and line up on an even grid cell.
        """
        gxapi_cy.WrapIMU._grid_wind2(GXContext._get_tls_geo(), img, out.encode(), xmin, xmax, ymin, ymax, zmin, zmax, clip)
        



    @classmethod
    def grid_xyz(cls, img, xyz, index, dec_x, dec_y, lab):
        """
        Export a Grid image to an XYZ file.
        
        :param img:    Image of the grid to export
        :param xyz:    Name of new XYZ file
        :param index:  :ref:`IMU_XYZ_INDEX`
        :param dec_x:  X direction decimation factor
        :param dec_y:  Y direction decimation factor
        :param lab:    :ref:`IMU_XYZ_LABEL`
        :type  img:    GXIMG
        :type  xyz:    str
        :type  index:  int
        :type  dec_x:  int
        :type  dec_y:  int
        :type  lab:    int

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** The `GXIMG <geosoft.gxapi.GXIMG>` (image) of the grid to export must
        be of type `GS_FLOAT <geosoft.gxapi.GS_FLOAT>`. If not, this method will
        terminate with an error.
        """
        gxapi_cy.WrapIMU._grid_xyz(GXContext._get_tls_geo(), img, xyz.encode(), index, dec_x, dec_y, lab)
        



    @classmethod
    def grid_type(cls, grid):
        """
        Reports the true data the of a grid (geosoft types)
        
        :param grid:  Name of the Grid
        :type  grid:  str

        :returns:     :ref:`GS_TYPES`
        :rtype:       int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = gxapi_cy.WrapIMU._grid_type(GXContext._get_tls_geo(), grid.encode())
        return ret_val



    @classmethod
    def make_mi_tab_file(cls, file):
        """
        Make a MapInfo tab file for this grid
        
        :param file:  Grid file name
        :type  file:  str

        .. versionadded:: 5.1.6

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        gxapi_cy.WrapIMU._make_mi_tab_file(GXContext._get_tls_geo(), file.encode())
        



    @classmethod
    def make_mi_tabfrom_grid(cls, file):
        """
        Make a MapInfo tab file for this grid as rendered in a map
        
        :param file:  Grid file name
        :type  file:  str

        .. versionadded:: 5.1.5

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        gxapi_cy.WrapIMU._make_mi_tabfrom_grid(GXContext._get_tls_geo(), file.encode())
        



    @classmethod
    def make_mi_tabfrom_map(cls, map):
        """
        Make a MapInfo tab file from this map
        
        :param map:  Map file name
        :type  map:  str

        .. versionadded:: 5.1.5

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        gxapi_cy.WrapIMU._make_mi_tabfrom_map(GXContext._get_tls_geo(), map.encode())
        



    @classmethod
    def mosaic(cls, grids, name, ipj, cell):
        """
        Create a mosaic image of an image list.
        
        :param grids:  Image names ('|' separated)
        :param name:   Output image name ("" for a memory only image)
        :param ipj:    Projection to use (0 to use the first grid's projection)
        :param cell:   Cell size to use (rDummy to use first grid)
        :type  grids:  str
        :type  name:   str
        :type  ipj:    GXIPJ
        :type  cell:   float

        :returns:      `GXIMG <geosoft.gxapi.GXIMG>` Object
        :rtype:        GXIMG

        .. versionadded:: 5.1.8

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** The images are simply placed on the output image, starting with
        the first image. Note that this function may require very large
        amounts of virtual memory.
        """
        ret_val = gxapi_cy.WrapIMU._mosaic(GXContext._get_tls_geo(), grids.encode(), name.encode(), ipj, cell)
        return GXIMG(ret_val)



    @classmethod
    def peak_size(cls, grid, vv_x, vv_y, max, prec, v_vz):
        """
        Define the sizes of all the peaks in an image.
        
        :param grid:  Grid file name
        :param vv_x:  Peaks' X
        :param vv_y:  Peaks' Y
        :param max:   Maximum target diameter (window) in # of cells
        :param prec:  Precision factor (see note above)
        :param v_vz:  Returned peak (anomaly) sizes in data units
        :type  grid:  str
        :type  vv_x:  GXVV
        :type  vv_y:  GXVV
        :type  max:   int
        :type  prec:  float
        :type  v_vz:  GXVV

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** Extending from the peak location of an anomaly to the inflection
        points of the grid values along each of the 8 directions results in
        8 radii. Anomaly size is defined as the 2*mediam of the 8 radii.

        Precision factor is used to control definition of an inflection point.
        For points A,B, and C, B is an inflection point if (A+C)/2.0 > B. With
        the precision factor, B is an inflection point only when
        (A+C)/2.0 > B*(1.0+Precision factor).
        This factor must be within (-1.0,1.0).

        Note: `peak_size2 <geosoft.gxapi.GXIMU.peak_size2>` is probably a better routine...
        """
        gxapi_cy.WrapIMU._peak_size(GXContext._get_tls_geo(), grid.encode(), vv_x, vv_y, max, prec, v_vz)
        



    @classmethod
    def peak_size2(cls, grid, vv_x, vv_y, max, v_vz):
        """
        Define the sizes of all the peaks in an image - new algorithm
        
        :param grid:  Grid file name
        :param vv_x:  Peaks' X
        :param vv_y:  Peaks' Y
        :param max:   Maximum target diameter (window) in # of cells
        :param v_vz:  Returned peak (anomaly) sizes in data units
        :type  grid:  str
        :type  vv_x:  GXVV
        :type  vv_y:  GXVV
        :type  max:   int
        :type  v_vz:  GXVV

        .. versionadded:: 5.1.4

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** Extending from the peak location of an anomaly to the inflection
        points of the grid values along each of the 8 directions results in
        8 radii. Anomaly size is defined as the 2*mediam of the 8 radii.

        This algorithm uses 4 successive points d1, d2, d3 and d4 in any
        direction. Given slopes m1 = d2-d1, m2 = d3-d2 and m3 = d4-d3,
        an inflection point occurs between d2 and d3 if m1>m2 and m2<m3.
        The location index is given as i3 - s2/(s2-s1), where i3 is the index
        of d3, and s1=m2-m1 and s2=m3-m2.

        This algorithm tends to give much smaller (and more reasonable)
        results than `peak_size <geosoft.gxapi.GXIMU.peak_size>`.
        """
        gxapi_cy.WrapIMU._peak_size2(GXContext._get_tls_geo(), grid.encode(), vv_x, vv_y, max, v_vz)
        



    @classmethod
    def pigeon_hole(cls, img, vv_x, vv_y, put):
        """
        Pigeon-hole and count points by location into a grid.
        
        :param img:   Input grid
        :param vv_x:  X locations
        :param vv_y:  Y locations
        :param put:   Number of points located in the grid.
        :type  img:   GXIMG
        :type  vv_x:  GXVV
        :type  vv_y:  GXVV
        :type  put:   int_ref

        .. versionadded:: 5.0.8

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** X and Y location VVs are input. If a point (X, Y) is located within
        one-half cell width from a location in the grid, then the value of
        the grid at that location is incremented by 1.
        The cells are inclusive at the minima, and exclusive at the maxima:
        e.g. if dDx = dDy = 1, and dXo = dYo = 0, then the corner cell would
        accept values  -0.5 <= X < 0.5 and -0.5 <= Y < 0.5.
        The grid values should be set to 0 before calling this function.

        The number of points "pigeon-holed" is returned to the user.
        This function is useful, for instance, in determining the density of
        sample locations in a survey area.
        """
        put.value = gxapi_cy.WrapIMU._pigeon_hole(GXContext._get_tls_geo(), img, vv_x, vv_y, put.value)
        



    @classmethod
    def pigeon_hole_color(cls, img, color_img, vv_x, vv_y, itr, put):
        """
        Pigeon-hole and count points by location and color locations in another grid based on ITR information.
        
        :param img:        Input grid
        :param color_img:  Input color grid
        :param vv_x:       X locations
        :param vv_y:       Y locations
        :param itr:        Input color transform
        :param put:        Number of points located in the grid.
        :type  img:        GXIMG
        :type  color_img:  GXIMG
        :type  vv_x:       GXVV
        :type  vv_y:       GXVV
        :type  itr:        GXITR
        :type  put:        int_ref

        .. versionadded:: 9.6

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** X and Y location VVs are input. If a point (X, Y) is located within
                       one-half cell width from a location in the grid, then the value of
                       the grid at that location is incremented by 1.
                       The cells are inclusive at the minima, and exclusive at the maxima:
                       e.g. if dDx = dDy = 1, and dXo = dYo = 0, then the corner cell would
                       accept values  -0.5 <= X < 0.5 and -0.5 <= Y < 0.5.
                       The grid values should be set to 0 before calling this function.

        					The color grid locations are coloured by the number of items at each location,
        					with the colour being determined by the input ITR, which should map the integer
        					count values 1, 2, 3, etc. onto individual colours.				

                       The number of points "pigeon-holed" is returned to the user.
                       This function is useful, for instance, in determining the density of
                       sample locations in a survey area.
        """
        put.value = gxapi_cy.WrapIMU._pigeon_hole_color(GXContext._get_tls_geo(), img, color_img, vv_x, vv_y, itr, put.value)
        



    @classmethod
    def profile(cls, img, x1, y1, x2, y2, samsep, vv_z):
        """
        Extract a profile from a grid.
        
        :param img:     Input image
        :param x1:      X1
        :param y1:      Y1
        :param x2:      X2
        :param y2:      Y2
        :param samsep:  Sample separation, if 0.0, use grid cell size
        :param vv_z:    `GXVV <geosoft.gxapi.GXVV>` in which to place result
        :type  img:     GXIMG
        :type  x1:      float
        :type  y1:      float
        :type  x2:      float
        :type  y2:      float
        :type  samsep:  float
        :type  vv_z:    GXVV

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** Returned `GXVV <geosoft.gxapi.GXVV>` will start at X1,Y1 and will sample
        up to X2,Y2 at the specified separation.
        """
        gxapi_cy.WrapIMU._profile(GXContext._get_tls_geo(), img, x1, y1, x2, y2, samsep, vv_z)
        



    @classmethod
    def profile_vv(cls, img, vv_x, vv_y, vv_z):
        """
        Extract a `GXVV <geosoft.gxapi.GXVV>` profile from a grid.
        
        :param img:   Input image
        :param vv_x:  X `GXVV <geosoft.gxapi.GXVV>` coordinates
        :param vv_y:  Y `GXVV <geosoft.gxapi.GXVV>` coordinates
        :param vv_z:  `GXVV <geosoft.gxapi.GXVV>` in which to place result
        :type  img:   GXIMG
        :type  vv_x:  GXVV
        :type  vv_y:  GXVV
        :type  vv_z:  GXVV

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        .. seealso::

            iGetPolyLine_DBE
        """
        gxapi_cy.WrapIMU._profile_vv(GXContext._get_tls_geo(), img, vv_x, vv_y, vv_z)
        



    @classmethod
    def range_grids(cls, grids, ipj, min_x, min_y, max_x, max_y):
        """
        Determine bounding rectangle for a set of grids
        
        :param grids:  List of grid files, "|" delimited
        :param ipj:    Projection for the range - see notes
        :param min_x:  Min X - returned range in the projection
        :param min_y:  Min Y
        :param max_x:  Max X
        :param max_y:  Max Y
        :type  grids:  str
        :type  ipj:    GXIPJ
        :type  min_x:  float_ref
        :type  min_y:  float_ref
        :type  max_x:  float_ref
        :type  max_y:  float_ref

        .. versionadded:: 5.1.8

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** If an `GXIPJ <geosoft.gxapi.GXIPJ>` is IPJ_CS_UNKNOWN, the
        `GXIPJ <geosoft.gxapi.GXIPJ>` of the first grid in the list will be used and
        the `GXIPJ <geosoft.gxapi.GXIPJ>` will be returned in this setting.
        Otherwise, the range in the requested `GXIPJ <geosoft.gxapi.GXIPJ>` will be
        determined.
        """
        min_x.value, min_y.value, max_x.value, max_y.value = gxapi_cy.WrapIMU._range_grids(GXContext._get_tls_geo(), grids.encode(), ipj, min_x.value, min_y.value, max_x.value, max_y.value)
        



    @classmethod
    def range_ll(cls, img, min_lat, min_lon, max_lat, max_lon):
        """
        Determine the range in lat. and long. of a projected grid
        
        :param img:      Input image
        :param min_lat:  Min latitude
        :param min_lon:  Min longitude
        :param max_lat:  Max latitude
        :param max_lon:  Max longitude
        :type  img:      GXIMG
        :type  min_lat:  float_ref
        :type  min_lon:  float_ref
        :type  max_lat:  float_ref
        :type  max_lon:  float_ref

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** This routine determines the latitude and longitudes along the
        edge of a grid and returns the minimal and maximal values.
        It scans each row and and column and finds the first non-dummy
        position at the start and end, and then determines the coordinates
        at those points.
        If the grid has no data, no `GXIPJ <geosoft.gxapi.GXIPJ>` object, or if the Source Type of
        the `GXIPJ <geosoft.gxapi.GXIPJ>` is not `IPJ_TYPE_PCS <geosoft.gxapi.IPJ_TYPE_PCS>` (projected coordinate system), then the
        returned values are dummies (`GS_R8DM <geosoft.gxapi.GS_R8DM>`).
        """
        min_lat.value, min_lon.value, max_lat.value, max_lon.value = gxapi_cy.WrapIMU._range_ll(GXContext._get_tls_geo(), img, min_lat.value, min_lon.value, max_lat.value, max_lon.value)
        



    @classmethod
    def stat_window(cls, img, min_x, min_y, max_x, max_y, max, st):
        """
        Calculate grid statistics in a window
        
        :param img:    Name of the grid to get stats from
        :param min_x:  Min X window
        :param min_y:  Min Y window
        :param max_x:  Max X window
        :param max_y:  Max Y window
        :param max:    Maximum values needed, 0 for all
        :param st:     `GXST <geosoft.gxapi.GXST>` object, stats are accumulated
        :type  img:    GXIMG
        :type  min_x:  float
        :type  min_y:  float
        :type  max_x:  float
        :type  max_y:  float
        :type  max:    int
        :type  st:     GXST

        .. versionadded:: 5.0.5

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** The maximum values needed will beused to
        decimate the sampling of the grid in order to
        improve performance.  100000 is often a good
        number when absolute precision is not
        required.
        """
        gxapi_cy.WrapIMU._stat_window(GXContext._get_tls_geo(), img, min_x, min_y, max_x, max_y, max, st)
        



    @classmethod
    def update_ply(cls, img, ply):
        """
        Update the grid boundary in the grid metadata
        
        :param img:  The Grid
        :param ply:  `GXPLY <geosoft.gxapi.GXPLY>` containing the edges.
        :type  img:  GXIMG
        :type  ply:  GXPLY

        .. versionadded:: 6.2

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** You can call the GridEdgePLY function to get an edge,
        perhaps alter the edge, such as thin it to a reasonable
        resolution, then put set it as the grid boundary by
        calling this funtion.  This is similar to the
        GridPLYEx function except that you get to alter the
        `GXPLY <geosoft.gxapi.GXPLY>` before it is placed back in the `GXIMG <geosoft.gxapi.GXIMG>`.
        """
        gxapi_cy.WrapIMU._update_ply(GXContext._get_tls_geo(), img, ply)
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer