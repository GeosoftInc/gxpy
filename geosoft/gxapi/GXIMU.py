### extends 'class_empty.py'
### block ClassImports
# NOTICE: Do not edit anything here, it is generated code
from typing import NewType
from . import gxapi_cy
from geosoft.gxapi import GXContext, float_ref, int_ref, str_ref
from .GXIMG import GXIMG


### endblock ClassImports

### block Header
# NOTICE: The code generator will not replace the code in this block
### endblock Header

### block ClassImplementation
# NOTICE: Do not edit anything here, it is generated code
class GXIMU:
    """
    GXIMU class.

    Not a class. This is a catch-all group of functions working
    on `GXIMG <geosoft.gxapi.GXIMG>` objects (see `GXIMG <geosoft.gxapi.GXIMG>`). Grid operations include masking,
    trending, windowing, expanding and grid stitching.
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._wrapper = None

    def __del__(self):
        self._wrapper = None

    def __init__(self, wrapper=None):
        self._wrapper = wrapper if wrapper else gxapi_cy.WrapIMU(GXContext._get_tls_geo(), 0)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of `GXIMU`
        
        :returns: A null `GXIMU`
        """
        return cls()

    def is_null(self):
        """
        Check if the instance of `GXIMU` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of `GXIMU`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Miscellaneous


    @classmethod
    def agg_to_geo_color(cls, agg, grid, ipj, res):
        """
        Create a geosoft color grid from an aggregate.

        **Note:**

        This consumes a very small amount of memory
        """
        gxapi_cy.WrapIMU.agg_to_geo_color(GXContext._get_tls_geo(), agg._wrapper, grid.encode(), ipj._wrapper, res)
        



    @classmethod
    def crc(cls, img, pul_crc):
        """
        Computes a CRC Checksum on an image.
        """
        ret_val = gxapi_cy.WrapIMU.crc(GXContext._get_tls_geo(), img._wrapper, pul_crc)
        return ret_val



    @classmethod
    def crc_grid(cls, grid, pul_crc):
        """
        Computes a CRC Checksum on a grid.
        """
        ret_val = gxapi_cy.WrapIMU.crc_grid(GXContext._get_tls_geo(), grid.encode(), pul_crc)
        return ret_val



    @classmethod
    def crc_grid_inexact(cls, grid, pul_crc, float_bits, double_bits):
        """
        Computes a CRC Checksum on a grid and allows you to specify
        number of bits of floats/doubles to drop so that the CRC
        will be same even of this are changed.

        **Note:**

        Very usefull for testing where the last bits of accuracy
        are not as important.
        """
        ret_val = gxapi_cy.WrapIMU.crc_grid_inexact(GXContext._get_tls_geo(), grid.encode(), pul_crc, float_bits, double_bits)
        return ret_val



    @classmethod
    def crc_inexact(cls, img, pul_crc, float_bits, double_bits):
        """
        Computes a CRC Checksum on an image and allows you to specify
        number of bits of floats/doubles to drop so that the CRC
        will be same even of this are changed.

        **Note:**

        Very usefull for testing where the last bits of accuracy
        are not as important.
        """
        ret_val = gxapi_cy.WrapIMU.crc_inexact(GXContext._get_tls_geo(), img._wrapper, pul_crc, float_bits, double_bits)
        return ret_val



    @classmethod
    def export_grid_without_data_section_xml(cls, grid, crc, file):
        """
        Export a Grid minus the data section as an XML file.
        """
        crc.value = gxapi_cy.WrapIMU.export_grid_without_data_section_xml(GXContext._get_tls_geo(), grid.encode(), crc.value, file.encode())
        



    @classmethod
    def export_grid_xml(cls, grid, crc, file):
        """
        Export a Grid as an XML file.
        """
        crc.value = gxapi_cy.WrapIMU.export_grid_xml(GXContext._get_tls_geo(), grid.encode(), crc.value, file.encode())
        



    @classmethod
    def export_raw_xml(cls, img, crc, file):
        """
        Export a Grid as an XML file using a fast raw output.
        """
        crc.value = gxapi_cy.WrapIMU.export_raw_xml(GXContext._get_tls_geo(), img._wrapper, crc.value, file.encode())
        



    @classmethod
    def export_xml(cls, img, crc, file):
        """
        Export a Grid as an XML file.
        """
        crc.value = gxapi_cy.WrapIMU.export_xml(GXContext._get_tls_geo(), img._wrapper, crc.value, file.encode())
        



    @classmethod
    def get_zvv(cls, img, vv_x, vv_y, vv_z):
        """
        Extract an interpolated image value for given XY `GXVV <geosoft.gxapi.GXVV>` locations
        """
        gxapi_cy.WrapIMU.get_zvv(GXContext._get_tls_geo(), img._wrapper, vv_x._wrapper, vv_y._wrapper, vv_z._wrapper)
        



    @classmethod
    def get_z_peaks_vv(cls, img, vv_x, vv_y, vv_z):
        """
        Same as `get_zvv <geosoft.gxapi.GXIMU.get_zvv>`, but find the closest peak value to the input locations, and return
        				             the peak value and peak value location.

        **Note:**

        The returned locations will always be a grid point location; no interpolation is performed when locating the peaks. A simple search is
        				done of all neighbouring points from the starting point, and once no neighbours can be located with a higher value, the search stops.
        """
        gxapi_cy.WrapIMU.get_z_peaks_vv(GXContext._get_tls_geo(), img._wrapper, vv_x._wrapper, vv_y._wrapper, vv_z._wrapper)
        



    @classmethod
    def grid_add(cls, img1, m1, img2, m2, imgo):
        """
        Adds two Grid images together point-by-point.

        **Note:**

        The `GXIMG <geosoft.gxapi.GXIMG>` parameters MUST be of type `GS_DOUBLE <geosoft.gxapi.GS_DOUBLE>`!
        If not, the method will terminate.
        """
        gxapi_cy.WrapIMU.grid_add(GXContext._get_tls_geo(), img1._wrapper, m1, img2._wrapper, m2, imgo._wrapper)
        



    @classmethod
    def grid_agc(cls, i_img, o_img, width, max_gain, remove_background):
        """
        Automatic Gain Compensation of a grid.

        **Note:**

        The `GXIMG <geosoft.gxapi.GXIMG>` parameters MUST be of type `GS_FLOAT <geosoft.gxapi.GS_FLOAT>`!
        If not, the method will terminate.
        """
        gxapi_cy.WrapIMU.grid_agc(GXContext._get_tls_geo(), i_img._wrapper, o_img._wrapper, width, max_gain, remove_background)
        



    @classmethod
    def grid_bool(cls, img1, img2, out, bool, sizing, olap):
        """
        Mask one grid against another using boolean logic
        operations.

        **Note:**

        The `GXIMG <geosoft.gxapi.GXIMG>` parameters must be of type `GS_DOUBLE <geosoft.gxapi.GS_DOUBLE>`!
        If not, the method will terminate.
        """
        gxapi_cy.WrapIMU.grid_bool(GXContext._get_tls_geo(), img1._wrapper, img2._wrapper, out.encode(), bool, sizing, olap)
        



    @classmethod
    def grid_edge(cls, grid, vv_x, vv_y):
        """
        Get grid edge points
        """
        gxapi_cy.WrapIMU.grid_edge(GXContext._get_tls_geo(), grid.encode(), vv_x._wrapper, vv_y._wrapper)
        



    @classmethod
    def grid_edge_ply(cls, img, ply, min_points):
        """
        Get grid edge points

        **Note:**

        Unlike `grid_ply <geosoft.gxapi.GXIMU.grid_ply>` and GridPlyEx_IMU, the image is not
        altered. It just gives the `GXPLY <geosoft.gxapi.GXPLY>`.
        """
        gxapi_cy.WrapIMU.grid_edge_ply(GXContext._get_tls_geo(), img._wrapper, ply._wrapper, min_points)
        



    @classmethod
    def grid_expand(cls, im_gi, out, per, shape, x, y):
        """
        Expand a grid and place dummies in the area
        beyond the original edges.

        **Note:**

        The `GXIMG <geosoft.gxapi.GXIMG>` parameter MUST be of type `GS_FLOAT <geosoft.gxapi.GS_FLOAT>`!
        If not, the method will terminate.
        """
        gxapi_cy.WrapIMU.grid_expand(GXContext._get_tls_geo(), im_gi._wrapper, out.encode(), per, shape, x, y)
        



    @classmethod
    def grid_exp_fill(cls, in_grd, out_grd, p_ex, t_ex):
        """
        Extends and fills a grid for `GXFFT2 <geosoft.gxapi.GXFFT2>`.
        """
        gxapi_cy.WrapIMU.grid_exp_fill(GXContext._get_tls_geo(), in_grd.encode(), out_grd.encode(), p_ex, t_ex)
        



    @classmethod
    def grid_fill(cls, im_gi, im_go, rollopt, rolldist, mxf, mxp, rollbase, alimit, elimit, width, npass):
        """
        Interpolates to fill dummies, generates an output grid.

        **Note:**

        The `GXIMG <geosoft.gxapi.GXIMG>` parameters MUST be of type `GS_FLOAT <geosoft.gxapi.GS_FLOAT>`!
        If not, the method will terminate.
        """
        gxapi_cy.WrapIMU.grid_fill(GXContext._get_tls_geo(), im_gi._wrapper, im_go._wrapper, rollopt, rolldist, mxf, mxp, rollbase, alimit, elimit, width, npass)
        



    @classmethod
    def grid_filt(cls, img, imgo, passes, mult, dum, hz, usefile, file, vv):
        """
        Applies a filter to a grid any number
        of passes.

        **Note:**

        The `GXIMG <geosoft.gxapi.GXIMG>` parameters MUST be of type `GS_FLOAT <geosoft.gxapi.GS_FLOAT>`!
        If not, the method will terminate.
        """
        gxapi_cy.WrapIMU.grid_filt(GXContext._get_tls_geo(), img._wrapper, imgo._wrapper, passes, mult, dum, hz, usefile, file.encode(), vv._wrapper)
        



    @classmethod
    def grid_head(cls, grid, esep, vsep, x_orig, y_orig, rot):
        """
        Modifies Statistics contained in a grid header.
        """
        gxapi_cy.WrapIMU.grid_head(GXContext._get_tls_geo(), grid.encode(), esep, vsep, x_orig, y_orig, rot)
        



    @classmethod
    def grid_in_fill(cls, im_gi, out_grd, extend, iter):
        """
        Fill in a ribbon along the edge and inside hollow areas of the grid
        """
        gxapi_cy.WrapIMU.grid_in_fill(GXContext._get_tls_geo(), im_gi._wrapper, out_grd.encode(), extend, iter)
        



    @classmethod
    def grid_mask(cls, in_grid, m_grid, pply, mode):
        """
        Create a mask grid using a set of polygon
        coordinates defined in a separate file, then
        masking the polygon over an input grid.

        **Note:**

        The `GXIMG <geosoft.gxapi.GXIMG>` parameters MUST be of type `GS_DOUBLE <geosoft.gxapi.GS_DOUBLE>`!
        If not, the method will terminate.
        
        The `GXPLY <geosoft.gxapi.GXPLY>` will contain more than one polygon
        if it was loaded from a file containing
        coordinates of more than one polygon.
        """
        gxapi_cy.WrapIMU.grid_mask(GXContext._get_tls_geo(), in_grid.encode(), m_grid.encode(), pply._wrapper, mode)
        



    @classmethod
    def grid_peak(cls, grid, nlmt, v_vx, v_vy, v_vz):
        """
        Pick grid peaks.

        **Note:**

        Peak test directions defines how grid peaks are to be found.
        For example, with the 1, a grid point will be picked if its
        value is greater than it's two neighbors in at least one
        direction.  Up to 4 directions can be tested.
        """
        gxapi_cy.WrapIMU.grid_peak(GXContext._get_tls_geo(), grid.encode(), nlmt, v_vx._wrapper, v_vy._wrapper, v_vz._wrapper)
        



    @classmethod
    def grid_ply(cls, img, ply, refresh):
        """
        Get the grid edge in a `GXPLY <geosoft.gxapi.GXPLY>`

        **Note:**

        This will optionally refresh the grid boundary `GXPLY <geosoft.gxapi.GXPLY>` and return
        the `GXPLY <geosoft.gxapi.GXPLY>`.
        
        If the boundary is not refreshed and has never been calculated,
        the boundary will be the bounding rectangle of the grid.
        
        The grid `GXPLY <geosoft.gxapi.GXPLY>` will be added to existing ploygons in the passed `GXPLY <geosoft.gxapi.GXPLY>`.
        """
        gxapi_cy.WrapIMU.grid_ply(GXContext._get_tls_geo(), img._wrapper, ply._wrapper, refresh)
        



    @classmethod
    def grid_ply_ex(cls, img, ply, refresh, min_points):
        """
        Get the grid edge in a `GXPLY <geosoft.gxapi.GXPLY>` (with min points)

        **Note:**

        This will optionally refresh the grid boundary `GXPLY <geosoft.gxapi.GXPLY>` and return
        the `GXPLY <geosoft.gxapi.GXPLY>`.
        
        If the boundary is not refreshed and has never been calculated,
        the boundary will be the bounding rectangle of the grid.
        
        The grid `GXPLY <geosoft.gxapi.GXPLY>` will be added to existing ploygons in the passed `GXPLY <geosoft.gxapi.GXPLY>`.
        """
        gxapi_cy.WrapIMU.grid_ply_ex(GXContext._get_tls_geo(), img._wrapper, ply._wrapper, refresh, min_points)
        



    @classmethod
    def grid_reproject_and_window(cls, input_grid_filename, output_grid_filename, new_projection, min_x, max_x, min_y, max_y):
        """
        Create a new grid by reprojecting an existing grid and windowing its contents
        """
        gxapi_cy.WrapIMU.grid_reproject_and_window(GXContext._get_tls_geo(), input_grid_filename.encode(), output_grid_filename.encode(), new_projection._wrapper, min_x, max_x, min_y, max_y)
        



    @classmethod
    def grid_resample(cls, input_grid_filename, output_grid_filename, o_x, o_y, d_x, d_y, n_x, n_y):
        """
        Create a new grid by resampling an existing grid

        **Note:**

        Works only for un rotated grids.
        """
        gxapi_cy.WrapIMU.grid_resample(GXContext._get_tls_geo(), input_grid_filename.encode(), output_grid_filename.encode(), o_x, o_y, d_x, d_y, n_x, n_y)
        



    @classmethod
    def grid_resize(cls, in_grd, out_grd):
        """
        Resize a grid to reduce the size not cover the outside dummies.
        """
        gxapi_cy.WrapIMU.grid_resize(GXContext._get_tls_geo(), in_grd.encode(), out_grd.encode())
        



    @classmethod
    def grid_shad(cls, in_grid, sh_grid, inc, dec, scl):
        """
        Create a shadded relief image.

        **Note:**

        Pass `GS_R8DM <geosoft.gxapi.GS_R8DM>` as parameters to obtain default values.
        The default values are returned.
        """
        inc.value, dec.value, scl.value = gxapi_cy.WrapIMU.grid_shad(GXContext._get_tls_geo(), in_grid.encode(), sh_grid.encode(), inc.value, dec.value, scl.value)
        



    @classmethod
    def grid_st(cls, grid, st):
        """
        Update an `GXST <geosoft.gxapi.GXST>` object using a grid.

        **Note:**

        The input `GXST <geosoft.gxapi.GXST>` object is not initialized by `grid_st <geosoft.gxapi.GXIMU.grid_st>`,
        so this function can be used to accumulate statistical
        info on more than a single grid.
        See `GXST <geosoft.gxapi.GXST>`.
        """
        gxapi_cy.WrapIMU.grid_st(GXContext._get_tls_geo(), grid.encode(), st._wrapper)
        



    @classmethod
    def grid_stat(cls, grid, type, xelem, yelem, xsep, ysep, kx, x_orig, y_orig, rot, base, mult):
        """
        Reports statistics contained in a grid header.

        **Note:**

        Statistics are returned in the parameter set
        """
        type.value, xelem.value, yelem.value, xsep.value, ysep.value, kx.value, x_orig.value, y_orig.value, rot.value, base.value, mult.value = gxapi_cy.WrapIMU.grid_stat(GXContext._get_tls_geo(), grid.encode(), type.value, xelem.value, yelem.value, xsep.value, ysep.value, kx.value, x_orig.value, y_orig.value, rot.value, base.value, mult.value)
        



    @classmethod
    def grid_stat_comp(cls, grid, type, xelem, yelem, xsep, ysep, kx, x_orig, y_orig, rot, base, mult, comp):
        """
        Reports statistics contained in a grid header.

        **Note:**

        Statistics are returned in the parameter set
        """
        type.value, xelem.value, yelem.value, xsep.value, ysep.value, kx.value, x_orig.value, y_orig.value, rot.value, base.value, mult.value, comp.value = gxapi_cy.WrapIMU.grid_stat_comp(GXContext._get_tls_geo(), grid.encode(), type.value, xelem.value, yelem.value, xsep.value, ysep.value, kx.value, x_orig.value, y_orig.value, rot.value, base.value, mult.value, comp.value)
        



    @classmethod
    def grid_stat_ext(cls, grid, force, items, dums, min, max, mean, stddev):
        """
        Reports statistics of a grid's elements.

        **Note:**

        If the `IMU_STAT_FORCED_` value is set, the
        statistics will be recalculated.
        Statistics are returned in the parameter set.
        """
        items.value, dums.value, min.value, max.value, mean.value, stddev.value = gxapi_cy.WrapIMU.grid_stat_ext(GXContext._get_tls_geo(), grid.encode(), force, items.value, dums.value, min.value, max.value, mean.value, stddev.value)
        



    @classmethod
    def grid_stat_trend(cls, grid, trend_valid, co, cx, cy):
        """
        Reports Trend Info of a grid (for first order coefficients only).

        **Note:**

        Trend Info are returned in the parameter set
        """
        trend_valid.value, co.value, cx.value, cy.value = gxapi_cy.WrapIMU.grid_stat_trend(GXContext._get_tls_geo(), grid.encode(), trend_valid.value, co.value, cx.value, cy.value)
        



    @classmethod
    def grid_stat_trend_ext(cls, grid, order, num_coef, xo, yo, vm):
        """
        Reports Extended Trend Info of a grid (for up to third order coefficients).

        **Note:**

        Trend Info are returned in the parameter set
        """
        order.value, num_coef.value, xo.value, yo.value = gxapi_cy.WrapIMU.grid_stat_trend_ext(GXContext._get_tls_geo(), grid.encode(), order.value, num_coef.value, xo.value, yo.value, vm._wrapper)
        



    @classmethod
    def slope_standard_deviation(cls, img):
        """
        Return the standard deviation of the slopes.

        **Note:**

        This method calculates the standard deviation of the horizontal
        differences in the X and Y directions for the supplied
        image.  This is useful for shading routines.  A good
        default scaling factor is 2.5 / standard deviation.
        
        The image will be sub-sampled to a statistically meaningful number.
        
        The cell sizes are used to determine the slopes.
        """
        ret_val = gxapi_cy.WrapIMU.slope_standard_deviation(GXContext._get_tls_geo(), img._wrapper)
        return ret_val



    @classmethod
    def grid_stitch(cls, grid1, grid2, grid3, method, tr_order1, tr_order2, tr_calc, gap, spline, path, pply, weighting, width):
        """
        Stitches together too grids
        """
        gxapi_cy.WrapIMU.grid_stitch(GXContext._get_tls_geo(), grid1.encode(), grid2.encode(), grid3.encode(), method, tr_order1, tr_order2, tr_calc, gap, spline, path, pply._wrapper, weighting, width)
        



    @classmethod
    def grid_stitch_ctl(cls, ctl):
        """
        Stitches together two grids - control file for options.

        **Note:**

        Data validation is done internally, not in the GX.
        This is simply a way of avoiding writing a new GX wrapper
        every time an option is added.
        """
        gxapi_cy.WrapIMU.grid_stitch_ctl(GXContext._get_tls_geo(), ctl.encode())
        



    @classmethod
    def grid_tiff(cls, grds, tiff, bcol, red, green, blue, csize, reg, scale):
        """
        Generate a Tiff (Tagged-Image file format) file with up to 16 grids.

        **Note:**

        The background color can be either selected
        from one of 8 settings, or can be specified
        as a combination of Reg,Green, and Blue values.
        """
        gxapi_cy.WrapIMU.grid_tiff(GXContext._get_tls_geo(), grds.encode(), tiff.encode(), bcol.encode(), red, green, blue, csize, reg, scale)
        



    @classmethod
    def grid_trnd(cls, imgi, imgo, tr_option, edge, order, vm, num_coefs):
        """
        Remove a trend surface from a grid.

        **Note:**

        Both Images must be of type `GS_DOUBLE <geosoft.gxapi.GS_DOUBLE>`.
        The `GXVM <geosoft.gxapi.GXVM>` parameter must be of type REAL,
        and be of size 10 at most.
        
        The number of coefficients must be
        compatible with the order of the
        trend removed. Following is the
        number of coefficients which should
        be present for a given order
        
        Order            Number of Coefficients
        -----            ----------------------
        0                 1
        1                 3
        2                 6
        3                 10
        """
        gxapi_cy.WrapIMU.grid_trnd(GXContext._get_tls_geo(), imgi._wrapper, imgo._wrapper, tr_option, edge, order, vm._wrapper, num_coefs)
        



    @classmethod
    def grid_trns(cls, grid, tcon):
        """
        Transpose a grid by swapping the grid rows with
        the grid columns.

        **Note:**

        If the grid has a line orientation that does NOT
        match the `IMU_TRANS_` value, this method will
        not succeed.
        """
        gxapi_cy.WrapIMU.grid_trns(GXContext._get_tls_geo(), grid.encode(), tcon)
        



    @classmethod
    def grid_vd(cls, im_gi, im_go):
        """
        Apply vertical derivative convolution filter to a grid.
        """
        gxapi_cy.WrapIMU.grid_vd(GXContext._get_tls_geo(), im_gi._wrapper, im_go._wrapper)
        



    @classmethod
    def grid_vol(cls, img, rbase, mult, vol_a, vol_b, diff):
        """
        Calculates the grid volumes above and below a
        reference base.

        **Note:**

        Volumes are calculated above and below a
        reference base level, and reported as positive
        integers. A multiplier is applied to the final
        volume (to correct for units).
        
        The `GXIMG <geosoft.gxapi.GXIMG>` parameters MUST be of type `GS_FLOAT <geosoft.gxapi.GS_FLOAT>`!
        If not, the method will terminate.
        """
        vol_a.value, vol_b.value, diff.value = gxapi_cy.WrapIMU.grid_vol(GXContext._get_tls_geo(), img._wrapper, rbase, mult, vol_a.value, vol_b.value, diff.value)
        



    @classmethod
    def grid_wind(cls, img, out, coord, xmin, xmax, ymin, ymax, zmin, zmax, csize, clip, dec, mdf):
        """
        Create a grid using a defined area window
        within a larger grid.
        """
        gxapi_cy.WrapIMU.grid_wind(GXContext._get_tls_geo(), img._wrapper, out.encode(), coord, xmin, xmax, ymin, ymax, zmin, zmax, csize, clip, dec, mdf.encode())
        



    @classmethod
    def grid_wind2(cls, img, out, xmin, xmax, ymin, ymax, zmin, zmax, clip):
        """
        Window a grid.

        **Note:**

        To change the cell size or work in a different projection,
        first inherit the `GXIMG <geosoft.gxapi.GXIMG>` by calling
        
        The windowed grid will be adjusted/expanded to include the
        defined area and line up on an even grid cell.
        """
        gxapi_cy.WrapIMU.grid_wind2(GXContext._get_tls_geo(), img._wrapper, out.encode(), xmin, xmax, ymin, ymax, zmin, zmax, clip)
        



    @classmethod
    def grid_xyz(cls, img, xyz, index, dec_x, dec_y, lab):
        """
        Export a Grid image to an XYZ file.

        **Note:**

        The `GXIMG <geosoft.gxapi.GXIMG>` (image) of the grid to export must
        be of type `GS_FLOAT <geosoft.gxapi.GS_FLOAT>`. If not, this method will
        terminate with an error.
        """
        gxapi_cy.WrapIMU.grid_xyz(GXContext._get_tls_geo(), img._wrapper, xyz.encode(), index, dec_x, dec_y, lab)
        



    @classmethod
    def grid_type(cls, grid):
        """
        Reports the true data the of a grid (geosoft types)
        """
        ret_val = gxapi_cy.WrapIMU.grid_type(GXContext._get_tls_geo(), grid.encode())
        return ret_val



    @classmethod
    def make_mi_tab_file(cls, file):
        """
        Make a MapInfo tab file for this grid
        """
        gxapi_cy.WrapIMU.make_mi_tab_file(GXContext._get_tls_geo(), file.encode())
        



    @classmethod
    def make_mi_tabfrom_grid(cls, file):
        """
        Make a MapInfo tab file for this grid as rendered in a map
        """
        gxapi_cy.WrapIMU.make_mi_tabfrom_grid(GXContext._get_tls_geo(), file.encode())
        



    @classmethod
    def make_mi_tabfrom_map(cls, map):
        """
        Make a MapInfo tab file from this map
        """
        gxapi_cy.WrapIMU.make_mi_tabfrom_map(GXContext._get_tls_geo(), map.encode())
        



    @classmethod
    def mosaic(cls, grids, name, ipj, cell):
        """
        Create a mosaic image of an image list.

        **Note:**

        The images are simply placed on the output image, starting with
        the first image. Note that this function may require very large
        amounts of virtual memory.
        """
        ret_val = gxapi_cy.WrapIMU.mosaic(GXContext._get_tls_geo(), grids.encode(), name.encode(), ipj._wrapper, cell)
        return GXIMG(ret_val)



    @classmethod
    def peak_size(cls, grid, vv_x, vv_y, max, prec, v_vz):
        """
        Define the sizes of all the peaks in an image.

        **Note:**

        Extending from the peak location of an anomaly to the inflection
        points of the grid values along each of the 8 directions results in
        8 radii. Anomaly size is defined as the 2*mediam of the 8 radii.
        
        Precision factor is used to control definition of an inflection point.
        For points A,B, and C, B is an inflection point if (A+C)/2.0 > B. With
        the precision factor, B is an inflection point only when
        (A+C)/2.0 > B*(1.0+Precision factor).
        This factor must be within (-1.0,1.0).
        
        Note: `peak_size2 <geosoft.gxapi.GXIMU.peak_size2>` is probably a better routine...
        """
        gxapi_cy.WrapIMU.peak_size(GXContext._get_tls_geo(), grid.encode(), vv_x._wrapper, vv_y._wrapper, max, prec, v_vz._wrapper)
        



    @classmethod
    def peak_size2(cls, grid, vv_x, vv_y, max, v_vz):
        """
        Define the sizes of all the peaks in an image - new algorithm

        **Note:**

        Extending from the peak location of an anomaly to the inflection
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
        gxapi_cy.WrapIMU.peak_size2(GXContext._get_tls_geo(), grid.encode(), vv_x._wrapper, vv_y._wrapper, max, v_vz._wrapper)
        



    @classmethod
    def pigeon_hole(cls, img, vv_x, vv_y, put):
        """
        Pigeon-hole and count points by location into a grid.

        **Note:**

        X and Y location VVs are input. If a point (X, Y) is located within
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
        put.value = gxapi_cy.WrapIMU.pigeon_hole(GXContext._get_tls_geo(), img._wrapper, vv_x._wrapper, vv_y._wrapper, put.value)
        



    @classmethod
    def profile(cls, img, x1, y1, x2, y2, samsep, vv_z):
        """
        Extract a profile from a grid.

        **Note:**

        Returned `GXVV <geosoft.gxapi.GXVV>` will start at X1,Y1 and will sample
        up to X2,Y2 at the specified separation.
        """
        gxapi_cy.WrapIMU.profile(GXContext._get_tls_geo(), img._wrapper, x1, y1, x2, y2, samsep, vv_z._wrapper)
        



    @classmethod
    def profile_vv(cls, img, vv_x, vv_y, vv_z):
        """
        Extract a `GXVV <geosoft.gxapi.GXVV>` profile from a grid.

        .. seealso::

            iGetPolyLine_DBE
        """
        gxapi_cy.WrapIMU.profile_vv(GXContext._get_tls_geo(), img._wrapper, vv_x._wrapper, vv_y._wrapper, vv_z._wrapper)
        



    @classmethod
    def range_grids(cls, grids, ipj, min_x, min_y, max_x, max_y):
        """
        Determine bounding rectangle for a set of grids

        **Note:**

        If an `GXIPJ <geosoft.gxapi.GXIPJ>` is IPJ_CS_UNKNOWN, the
        `GXIPJ <geosoft.gxapi.GXIPJ>` of the first grid in the list will be used and
        the `GXIPJ <geosoft.gxapi.GXIPJ>` will be returned in this setting.
        Otherwise, the range in the requested `GXIPJ <geosoft.gxapi.GXIPJ>` will be
        determined.
        """
        min_x.value, min_y.value, max_x.value, max_y.value = gxapi_cy.WrapIMU.range_grids(GXContext._get_tls_geo(), grids.encode(), ipj._wrapper, min_x.value, min_y.value, max_x.value, max_y.value)
        



    @classmethod
    def range_ll(cls, img, min_lat, min_lon, max_lat, max_lon):
        """
        Determine the range in lat. and long. of a projected grid

        **Note:**

        This routine determines the latitude and longitudes along the
        edge of a grid and returns the minimal and maximal values.
        It scans each row and and column and finds the first non-dummy
        position at the start and end, and then determines the coordinates
        at those points.
        If the grid has no data, no `GXIPJ <geosoft.gxapi.GXIPJ>` object, or if the Source Type of
        the `GXIPJ <geosoft.gxapi.GXIPJ>` is not `IPJ_TYPE_PCS <geosoft.gxapi.IPJ_TYPE_PCS>` (projected coordinate system), then the
        returned values are dummies (`GS_R8DM <geosoft.gxapi.GS_R8DM>`).
        """
        min_lat.value, min_lon.value, max_lat.value, max_lon.value = gxapi_cy.WrapIMU.range_ll(GXContext._get_tls_geo(), img._wrapper, min_lat.value, min_lon.value, max_lat.value, max_lon.value)
        



    @classmethod
    def stat_window(cls, img, min_x, min_y, max_x, max_y, max, st):
        """
        Calculate grid statistics in a window

        **Note:**

        The maximum values needed will beused to
        decimate the sampling of the grid in order to
        improve performance.  100000 is often a good
        number when absolute precision is not
        required.
        """
        gxapi_cy.WrapIMU.stat_window(GXContext._get_tls_geo(), img._wrapper, min_x, min_y, max_x, max_y, max, st._wrapper)
        



    @classmethod
    def update_ply(cls, img, ply):
        """
        Update the grid boundary in the grid metadata

        **Note:**

        You can call the GridEdgePLY function to get an edge,
        perhaps alter the edge, such as thin it to a reasonable
        resolution, then put set it as the grid boundary by
        calling this funtion.  This is similar to the
        GridPLYEx function except that you get to alter the
        `GXPLY <geosoft.gxapi.GXPLY>` before it is placed back in the `GXIMG <geosoft.gxapi.GXIMG>`.
        """
        gxapi_cy.WrapIMU.update_ply(GXContext._get_tls_geo(), img._wrapper, ply._wrapper)
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer