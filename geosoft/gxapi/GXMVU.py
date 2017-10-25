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
class GXMVU:
    """
    GXMVU class.

    A catchall library for methods using the :class:`geosoft.gxapi.GXMAP` and :class:`geosoft.gxapi.GXMVIEW` classes.
    These include drawing flight paths, legends, postings, and
    special objects such as histograms and bar charts.
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._wrapper = None

    def __del__(self):
        self._wrapper = None

    def __init__(self, wrapper=None):
        self._wrapper = wrapper if wrapper else gxapi_cy.WrapMVU(GXContext._get_tls_geo(), 0)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of :class:`geosoft.gxapi.GXMVU`
        
        :returns: A null :class:`geosoft.gxapi.GXMVU`
        """
        return cls()

    def is_null(self):
        """
        Check if the instance of :class:`geosoft.gxapi.GXMVU` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of :class:`geosoft.gxapi.GXMVU`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Miscellaneous


    @classmethod
    def arrow(cls, p1, p2, p3, p4, p5, p6, p7, p8):
        """
        Draw an arrow.
        """
        gxapi_cy.WrapMVU.arrow(GXContext._get_tls_geo(), p1._wrapper, p2, p3, p4, p5, p6, p7, p8)
        



    @classmethod
    def arrow_vector_vv(cls, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11):
        """
        Draw arrow vectors based on input VVs.

        **Note:**

        The locations are given in two VVs, and the directions
        in the two others. A wide range of sizes are available.
        If the scaling is set to :attr:`geosoft.gxapi.rDUMMY`, then arrows are automatically
        scaled so the largest is 1cm in length.
        If the line thickness is set to :attr:`geosoft.gxapi.rDUMMY`, the line thickness scales
        with the arrow size, and is 1/20 of the vector length.
        """
        gxapi_cy.WrapMVU.arrow_vector_vv(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3._wrapper, p4._wrapper, p5._wrapper, p6, p7, p8, p9, p10, p11)
        



    @classmethod
    def bar_chart(cls, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16, p17, p18, p19, p20, p21, p22, p23, p24, p25, p26, p27, p28):
        """
        Plot bar chart on a map.
        """
        gxapi_cy.WrapMVU.bar_chart(GXContext._get_tls_geo(), p1._wrapper, p2.encode(), p3._wrapper, p4, p5.encode(), p6.encode(), p7.encode(), p8, p9.encode(), p10, p11.encode(), p12, p13, p14, p15, p16, p17, p18, p19, p20, p21, p22, p23, p24, p25, p26, p27, p28)
        



    @classmethod
    def cdi_pixel_plot(cls, p1, p2, p3, p4, p5, p6):
        """
        Create a color pixel-style plot of CDI data.

        **Note:**

        Draws a single colored rectangle for each data point in
        Conductivity-Depth data (for example). It is similar to the
        result you get if you plot a grid with Pixel=1, but in this
        data the row and column widths are not necessarily constant,
        and the data can move up and down with topography. The pixels
        are sized so that the boundaries are half-way between adjacent
        data, both vertically and horizontally.
        """
        gxapi_cy.WrapMVU.cdi_pixel_plot(GXContext._get_tls_geo(), p1._wrapper, p2.encode(), p3._wrapper, p4._wrapper, p5._wrapper, p6._wrapper)
        



    @classmethod
    def cdi_pixel_plot_3d(cls, p1, p2, p3, p4, p5, p6, p7):
        """
        Create a color pixel-style plot of CDI data in a 3D view.

        **Note:**

        Similar to CDIPixelPlot_MVU, but plotted onto a series of
        plotting planes which hang from the XY path in 3D. Each vertical plane azimuth
        is defined by two adjacent points on the path. The color "pixel" for each
        data point is plotted in two halves, with each half on adjacent plotting planes,
        with the bend at the data point.
        """
        gxapi_cy.WrapMVU.cdi_pixel_plot_3d(GXContext._get_tls_geo(), p1._wrapper, p2.encode(), p3._wrapper, p4._wrapper, p5._wrapper, p6._wrapper, p7._wrapper)
        



    @classmethod
    def color_bar(cls, p1, p2, p3, p4, p5, p6, p7, p8):
        """
        Create a Color Bar in view
        """
        gxapi_cy.WrapMVU.color_bar(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3, p4, p5, p6, p7, p8)
        



    @classmethod
    def color_bar2(cls, p1, p2, p3, p4, p5, p6, p7, p8, p9):
        """
        Create a Color Bar from two :class:`geosoft.gxapi.GXITR`

        **Note:**

        The secondary :class:`geosoft.gxapi.GXITR` is used to blend horizontally with the
        primary :class:`geosoft.gxapi.GXITR` in each box.
        """
        gxapi_cy.WrapMVU.color_bar2(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3._wrapper, p4, p5, p6, p7, p8, p9)
        



    @classmethod
    def color_bar2_style(cls, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10):
        """
        Create a Color Bar from two ITRs with style options

        **Note:**

        The secondary :class:`geosoft.gxapi.GXITR` is used to blend horizontally with the
        primary :class:`geosoft.gxapi.GXITR` in each box.
        """
        gxapi_cy.WrapMVU.color_bar2_style(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3._wrapper, p4, p5, p6, p7, p8, p9, p10)
        



    @classmethod
    def color_bar_hor(cls, p1, p2, p3, p4, p5, p6, p7, p8, p9):
        """
        Create a horizontal color bar in view

        **Note:**

        The sign of the annotation offset determines whether labels are
        plotted above or below the colorbar. Labels above are text-justified
        to the bottom of the text, and labels below are text-justified to
        the top of the text.
        """
        gxapi_cy.WrapMVU.color_bar_hor(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3, p4, p5, p6, p7, p8, p9)
        



    @classmethod
    def color_bar_hor2(cls, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10):
        """
        Create a Horizontal Color Bar from two ITRs

        **Note:**

        The secondary :class:`geosoft.gxapi.GXITR` is used to blend horizontally with the
        primary :class:`geosoft.gxapi.GXITR` in each box.
        """
        gxapi_cy.WrapMVU.color_bar_hor2(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3._wrapper, p4, p5, p6, p7, p8, p9, p10)
        



    @classmethod
    def color_bar_hor2_style(cls, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11):
        """
        Create a Horizontal Color Bar from two ITRs with style options

        **Note:**

        The secondary :class:`geosoft.gxapi.GXITR` is used to blend horizontally with the
        primary :class:`geosoft.gxapi.GXITR` in each box.
        """
        gxapi_cy.WrapMVU.color_bar_hor2_style(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3._wrapper, p4, p5, p6, p7, p8, p9, p10, p11)
        



    @classmethod
    def color_bar_hor_style(cls, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10):
        """
        Create a Horizontal Color Bar in view with style options
        """
        gxapi_cy.WrapMVU.color_bar_hor_style(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3, p4, p5, p6, p7, p8, p9, p10)
        



    @classmethod
    def color_bar_style(cls, p1, p2, p3, p4, p5, p6, p7, p8, p9):
        """
        Create a Color Bar in view with style options
        """
        gxapi_cy.WrapMVU.color_bar_style(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3, p4, p5, p6, p7, p8, p9)
        



    @classmethod
    def color_bar_reg(cls, p1, p2, p3, p4):
        """
        Create a Color Bar in view

        **Note:**

        To allow for expansion, all parameters are passed inside the :class:`geosoft.gxapi.GXREG` object.
        
        BAR_ORIENTATION        one of MVU_ORIENTATION_XXX (DEFAULT = :attr:`geosoft.gxapi.MVU_ORIENTATION_VERTICAL`)
        DECIMALS					decimals in plotted values (see sFormatStr_GS for rules) (DEFAULT = 1)
        ANNOFF						annotation offset from bar (+/- determines side of the bar left/right and below/above)
        BOX_SIZE               box height (mm) (width for horizontal color bar) (DEFAULT = 4)
        BAR_WIDTH              width (mm) (short dimension) of the color bar (DEFAULT = 8)
        MINIMUM_GAP            Minimum space between annotations, otherwise drop annotations (DEFAULT = 0 mm)
        The actual height is over-estimated, so even with zero gap there will normally always be some space between labels.
        FIXED_INTERVAL         Preset interval for annotations scale (DEFAULT = DUMMY, use color zones)
        FIXED_MINOR_INTERVAL   Preset minor interval for annotations scale (DEFAULT = DUMMY, if defined must be 1/10, 1/5, 1/4 or 1/2 of FIXED_INTERVAL)
        X								X location	(REQUIRED)
        Y								Y location	(REQUIRED)
        POST_MAXMIN            Post limit values at ends of the bar (0 or 1)? (DEFAULT = 0)
        DIVISION_STYLE         One of MVU_DIVISION_STYLE_XXX (DEFAULT = :attr:`geosoft.gxapi.MVU_DIVISION_STYLE_LINES`)
        """
        gxapi_cy.WrapMVU.color_bar_reg(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3._wrapper, p4._wrapper)
        



    @classmethod
    def contour(cls, p1, p2, p3):
        """
        Creates a contour map.
        """
        gxapi_cy.WrapMVU.contour(GXContext._get_tls_geo(), p1._wrapper, p2.encode(), p3.encode())
        



    @classmethod
    def contour_ply(cls, p1, p2, p3, p4):
        """
        Creates a contour map with clipped areas.

        **Note:**

        The clipping :class:`geosoft.gxapi.GXPLY` can include a surrounding inclusive polygon
        and zero, one or more interior exclusive polygons. Construct
        a :class:`geosoft.gxapi.GXPLY` object using the AddPolygonEx_PLY function, to add both
        inclusive (as the first :class:`geosoft.gxapi.GXPLY`) and exclusive interior regions.
        """
        gxapi_cy.WrapMVU.contour_ply(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3.encode(), p4.encode())
        



    @classmethod
    def c_symb_legend(cls, p1, p2, p3, p4, p5, p6, p7, p8):
        """
        Plot a legend for the classified color symbols.

        **Note:**

        If the symbol size, color, font etc are specified in
        the :class:`geosoft.gxapi.GXITR`'s :class:`geosoft.gxapi.GXREG`, then the Symbol scale factor is used
        allow the user to adjust the symbol sizes. They will be
        plotted at a size equal to the size in the :class:`geosoft.gxapi.GXREG` times
        the scale factor.
        If no symbol size info can be found in the :class:`geosoft.gxapi.GXREG`, then
        the symbol size is set equal to the Label Font Size.
        If no symbol font or number info is included in the
        :class:`geosoft.gxapi.GXREG`, it is the programmer's responsibility to select
        the correct font and symbol before CSymbLegend is
        called. The same is true of the edge color.
        """
        gxapi_cy.WrapMVU.c_symb_legend(GXContext._get_tls_geo(), p1._wrapper, p2, p3, p4, p5, p6.encode(), p7.encode(), p8.encode())
        



    @classmethod
    def decay_curve(cls, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16, p17, p18, p19, p20, p21):
        """
        Plot decay curves at survey locations

        **Note:**

        Box width and height are used to draw horizontal and vertical
        bars. Curves outside the box are not clipped.
        """
        gxapi_cy.WrapMVU.decay_curve(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3._wrapper, p4._wrapper, p5._wrapper, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16, p17, p18, p19, p20, p21.encode())
        



    @classmethod
    def direction_plot(cls, p1, p2, p3, p4, p5, p6):
        """
        Plot an arrow to indicate the direction of a flight line

        **Note:**

        An arrow will be drawn in the direction from the first valid
        to the last points in the X and Y VVs.
        """
        gxapi_cy.WrapMVU.direction_plot(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3._wrapper, p4, p5, p6)
        



    @classmethod
    def em_forward(cls, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16, p17, p18):
        """
        Plot an EM forward model against inverted data.

        **Note:**

        This function is designed to display an inverted result beside
        the forward model curves. This is useful for trouble-shooting
        or understanding why a certain inversion result was obtained.
        The earth model is a simple halfspace.
        The forward model is plotted either as a function of
        resistivity at a single height, or as a function of height at
        a single resistivity. In either case, the relevant VVs must be
        completely filled (even if one is all the same value).
        """
        gxapi_cy.WrapMVU.em_forward(GXContext._get_tls_geo(), p1._wrapper, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13._wrapper, p14._wrapper, p15._wrapper, p16._wrapper, p17, p18)
        



    @classmethod
    def export_datamine_string(cls, p1, p2, p3):
        """
        Export selected map groups in a map view to a Datamine coordinate string file.

        **Note:**

        The lines, rectangles and polygons in the specified groups
        will be exported to a Datamine coordinate string (*.dm) file.
        The function attemps to duplicate the colors, etc. used.
        Complex polygon objects will be exported as independent
        single polygons.
        """
        gxapi_cy.WrapMVU.export_datamine_string(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3.encode())
        



    @classmethod
    def export_dxf_3d(cls, p1, p2, p3):
        """
        Export selected map groups in a map view to an AutoCAD 3D DXF file.

        **Note:**

        Supported objects exported include lines, polygons, text.
        """
        gxapi_cy.WrapMVU.export_dxf_3d(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3._wrapper)
        



    @classmethod
    def export_surpac_str(cls, p1, p2, p3, p4):
        """
        Export selected map groups in a map view to a Surpac :class:`geosoft.gxapi.GXSTR` file.

        **Note:**

        The lines, rectangles and polygons in the specified groups
        will be exported to a Surpac :class:`geosoft.gxapi.GXSTR` file. An accompanying styles
        file will be created which will attempt to duplicate the
        colors, etc. used.
        Complex polygon objects will be exported as independent
        single polygons.
        """
        gxapi_cy.WrapMVU.export_surpac_str(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3._wrapper, p4._wrapper)
        



    @classmethod
    def flight_plot(cls, p1, p2, p3, p4, p5, p6, p7, p8, p9):
        """
        Draw a flight line

        **Note:**

        Current line color, thickness and style are used to
        draw the line.
        
        Current font, font color and font style are used to
        annotate the line labels.
        
        If current clipping is ON in the VIEW, lines will be
        clipped to the window before plotting.  In this case,
        labels should be located ABOVE or BELOW the line
        traces to prevent labels being clipped.
        
        The offsets dOffA and dOffB control the vertical and
        horizontal label offsets with respect to the ends of
        the line trace and depending on the label location.
        
        The vertical line reference angle dVerAng is used
        to determine if lines are considered vertical or
        horizontal.  Vertical lines use the sUp parameter
        to determine the label up direction.  Normally, use an
        angle of 60 degrees unless there are lines that run in
        this direction.
        """
        gxapi_cy.WrapMVU.flight_plot(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3._wrapper, p4.encode(), p5, p6, p7, p8, p9)
        



    @classmethod
    def gen_areas(cls, p1, p2, p3, p4, p5):
        """
        Generate areas from an line group.

        **Note:**

        The specified line group will be used to create a new group that
        is composed of all the resolved polygonal areas in the line group.
        Each polygonal area is assigned a color/pattern as specified in the
        color and pattern :class:`geosoft.gxapi.GXVV`'s.  Color/patterns are assigned in rotating
        sequence.
        """
        gxapi_cy.WrapMVU.gen_areas(GXContext._get_tls_geo(), p1._wrapper, p2.encode(), p3._wrapper, p4._wrapper, p5)
        



    @classmethod
    def get_range_gocad_surface(cls, p1, p2, p3, p4, p5, p6, p7):
        """
        Get the XYZ range of a GOCAD surface.

        **Note:**

        Required to set up a map view before doing the actual
        surface import.
        """
        p2.value, p3.value, p4.value, p5.value, p6.value, p7.value = gxapi_cy.WrapMVU.get_range_gocad_surface(GXContext._get_tls_geo(), p1.encode(), p2.value, p3.value, p4.value, p5.value, p6.value, p7.value)
        



    @classmethod
    def histogram(cls, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16, p17, p18):
        """
        Plot the histogram on a map.

        **Note:**

        This function just calls Histogram2_MVU with decimals set
        to -7 (7 significant figures).
        """
        gxapi_cy.WrapMVU.histogram(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3._wrapper, p4.encode(), p5.encode(), p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16, p17, p18._wrapper)
        



    @classmethod
    def histogram2(cls, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16, p17, p18, p19, p20, p21, p22, p23):
        """
        Plot the histogram on a map.

        **Note:**

        A vertical line through from bottom to top horizontal axis is drawn
        Also a label 'Threshold value' is plotted against this line. However,
        None of them will be plotted if threshold value is dummy or outside
        the X data range.
        """
        gxapi_cy.WrapMVU.histogram2(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3._wrapper, p4.encode(), p5.encode(), p6, p7.encode(), p8, p9.encode(), p10, p11, p12, p13, p14, p15, p16, p17, p18, p19, p20, p21, p22._wrapper, p23)
        



    @classmethod
    def histogram3(cls, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16, p17, p18, p19, p20):
        """
        Plot the histogram on a map, specify decimals.
        """
        gxapi_cy.WrapMVU.histogram3(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3._wrapper, p4.encode(), p5.encode(), p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16, p17, p18, p19, p20._wrapper)
        



    @classmethod
    def histogram4(cls, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16, p17, p18, p19, p20, p21):
        """
        As Histogram3_MVU, but allow probability scaling of percents.
        """
        gxapi_cy.WrapMVU.histogram4(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3._wrapper, p4.encode(), p5.encode(), p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16, p17, p18, p19, p20, p21._wrapper)
        



    @classmethod
    def histogram5(cls, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16, p17, p18, p19, p20, p21, p22, p23):
        """
        As Histogram4_MVU, but allow :class:`geosoft.gxapi.GXITR` to color bars.

        **Note:**

        The :class:`geosoft.gxapi.GXITR` can be empty (but must still be a valid :class:`geosoft.gxapi.GXITR` object).
        """
        gxapi_cy.WrapMVU.histogram5(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3._wrapper, p4.encode(), p5.encode(), p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16, p17, p18, p19, p20, p21, p22._wrapper, p23._wrapper)
        



    @classmethod
    def exportable_dxf_3d_groups_lst(cls, p1, p2):
        """
        Return a :class:`geosoft.gxapi.GXLST` of groups you can export using sExportDXF3D_MVU.

        **Note:**

        Returns a list of visible groups that the DXF 3D export can
        export. Removes things like :class:`geosoft.gxapi.GXVOXD`, :class:`geosoft.gxapi.GXAGG`, and target
        groups starting with "Dh", which are typically plotted in 3D
        views on a reference plan oriented toward the user, and thus
        not exportable.
        """
        ret_val = gxapi_cy.WrapMVU.exportable_dxf_3d_groups_lst(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper)
        return ret_val



    @classmethod
    def mapset_test(cls, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14):
        """
        Test function to ensure parameters to Mapset_MVU is sane

        **Note:**

        Use ShowError_SYS to display errors that may have been encountered. This function can also be used
        to calculate the default scale without creating a map.
        """
        ret_val, p8.value = gxapi_cy.WrapMVU.mapset_test(GXContext._get_tls_geo(), p1, p2, p3, p4, p5.encode(), p6, p7, p8.value, p9, p10, p11, p12, p13, p14)
        return ret_val



    @classmethod
    def mapset2_test(cls, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15):
        """
        Test function to ensure parameters to Mapset_MVU is sane

        **Note:**

        Same as iMapsetTest_MVU, with vertical exaggeration.
        """
        ret_val, p8.value = gxapi_cy.WrapMVU.mapset2_test(GXContext._get_tls_geo(), p1, p2, p3, p4, p5.encode(), p6, p7, p8.value, p9, p10, p11, p12, p13, p14, p15)
        return ret_val



    @classmethod
    def import_gocad_surface(cls, p1, p2, p3):
        """
        Import and plot a GOCAD surface model.

        **Note:**

        The vertex normals are not included in the
        GOCAD import, but are calculated using
        the normal of each defined triangle, and taking the
        average when vertex is shared among more than one triangle.
        """
        gxapi_cy.WrapMVU.import_gocad_surface(GXContext._get_tls_geo(), p1._wrapper, p2.encode(), p3)
        



    @classmethod
    def load_plot(cls, p1, p2):
        """
        Load a Geosoft PLT file into a :class:`geosoft.gxapi.GXMAP`.
        """
        gxapi_cy.WrapMVU.load_plot(GXContext._get_tls_geo(), p1._wrapper, p2.encode())
        



    @classmethod
    def map_from_plt(cls, p1, p2, p3, p4, p5, p6):
        """
        Creates a new map from a PLT file.

        **Note:**

        This only creates a map, it does not read the PLT into
        the map.  The base view and data view will be the same
        size.
        """
        gxapi_cy.WrapMVU.map_from_plt(GXContext._get_tls_geo(), p1._wrapper, p2.encode(), p3.encode(), p4.encode(), p5, p6)
        



    @classmethod
    def map_mdf(cls, p1, p2, p3):
        """
        Creates an MDF from a Map.
        """
        gxapi_cy.WrapMVU.map_mdf(GXContext._get_tls_geo(), p1._wrapper, p2.encode(), p3.encode())
        



    @classmethod
    def mapset(cls, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16, p17):
        """
        Creates a new map directly from parameters.
        """
        gxapi_cy.WrapMVU.mapset(GXContext._get_tls_geo(), p1._wrapper, p2.encode(), p3.encode(), p4, p5, p6, p7, p8.encode(), p9, p10, p11, p12, p13, p14, p15, p16, p17)
        



    @classmethod
    def mapset2(cls, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16, p17, p18):
        """
        Same as Mapset_MVU, with vertical exaggeration.
        """
        gxapi_cy.WrapMVU.mapset2(GXContext._get_tls_geo(), p1._wrapper, p2.encode(), p3.encode(), p4, p5, p6, p7, p8.encode(), p9, p10, p11, p12, p13, p14, p15, p16, p17, p18)
        



    @classmethod
    def mdf(cls, p1, p2, p3, p4):
        """
        Creates a new map from an MDF file.
        """
        gxapi_cy.WrapMVU.mdf(GXContext._get_tls_geo(), p1._wrapper, p2.encode(), p3.encode(), p4.encode())
        



    @classmethod
    def path_plot(cls, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10):
        """
        Draw a flight line

        **Note:**

        See FlightPlot_MVU.  This is the same except for the
        additional line gap parameter.
        """
        gxapi_cy.WrapMVU.path_plot(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3._wrapper, p4.encode(), p5, p6, p7, p8, p9, p10)
        



    @classmethod
    def path_plot_ex(cls, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11):
        """
        Draw a flight line

        **Note:**

        This is the same except for the additional line compass parameter.
        """
        gxapi_cy.WrapMVU.path_plot_ex(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3._wrapper, p4.encode(), p5, p6, p7, p8, p9, p10, p11)
        



    @classmethod
    def path_plot_ex2(cls, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12):
        """
        Draw a flight line

        **Note:**

        This is the same except for the additional line dummies parameter.
        """
        gxapi_cy.WrapMVU.path_plot_ex2(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3._wrapper, p4.encode(), p5, p6, p7, p8, p9, p10, p11, p12)
        



    @classmethod
    def plot_voxel_surface(cls, p1, p2, p3, p4, p5):
        """
        Extract an iso-surface from a voxel and plot it to a 2D or 3D view.

        **Note:**

        The Marching Cubes method of Lorensen and Cline, Computer Graphics, V21,
        Number 4, July 1987, is used to calculate a given iso-surface in a voxel
        model. The resulting surface is plotted to a 2D or 3D view. If the view
        is 2-D, then only the intersection of the surface with the 2D surface is
        plotted, using lines.
        """
        gxapi_cy.WrapMVU.plot_voxel_surface(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3, p4, p5)
        



    @classmethod
    def plot_voxel_surface2(cls, p1, p2, p3, p4, p5, p6, p7):
        """
        Extract an iso-surface from a voxel and plot it to a 2D or 3D view.

        **Note:**

        The Marching Cubes method of Lorensen and Cline, Computer Graphics, V21,
        Number 4, July 1987, is used to calculate a given iso-surface in a voxel
        model. The resulting surface is plotted to a 2D or 3D view. If the view
        is 2-D, then only the intersection of the surface with the 2D surface is
        plotted, using lines.
        """
        gxapi_cy.WrapMVU.plot_voxel_surface2(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3, p4, p5, p6, p7.encode())
        



    @classmethod
    def generate_surface_from_voxel(cls, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10):
        """
        TODO...

        **Note:**

        TODO... Move to :class:`geosoft.gxapi.GXVOX` method for surface generation only and use GeosurfaceD to display.
        """
        gxapi_cy.WrapMVU.generate_surface_from_voxel(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3, p4, p5, p6, p7, p8, p9, p10.encode())
        



    @classmethod
    def post(cls, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10):
        """
        Post values on a map.
        """
        gxapi_cy.WrapMVU.post(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3._wrapper, p4._wrapper, p5, p6, p7, p8, p9, p10)
        



    @classmethod
    def post_ex(cls, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16, p17, p18, p19, p20):
        """
        Post values on a map with more paramters.
        """
        gxapi_cy.WrapMVU.post_ex(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3._wrapper, p4._wrapper, p5._wrapper, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16, p17, p18, p19, p20)
        



    @classmethod
    def probability(cls, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16, p17, p18):
        """
        Plot a probability plot on a map.

        **Note:**

        The :class:`geosoft.gxapi.GXITR` can be empty (but must still be a valid :class:`geosoft.gxapi.GXITR` object).
        """
        gxapi_cy.WrapMVU.probability(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3._wrapper, p4.encode(), p5.encode(), p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16, p17, p18._wrapper)
        



    @classmethod
    def profile_plot(cls, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10):
        """
        Draw a profile along line trace

        **Note:**

        Profiles will be drawn in the current line style.
        """
        gxapi_cy.WrapMVU.profile_plot(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3._wrapper, p4._wrapper, p5, p6, p7, p8, p9, p10)
        



    @classmethod
    def profile_plot_ex(cls, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15):
        """
        Draw a profile along line trace with more parameters

        **Note:**

        Profiles will be drawn in the current line style.
        """
        gxapi_cy.WrapMVU.profile_plot_ex(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3._wrapper, p4._wrapper, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14.encode(), p15.encode())
        



    @classmethod
    def prop_symb_legend(cls, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11):
        """
        Draw a legend for proportional symbols.

        **Note:**

        All symbol attributes, except for the size, are assumed
        to be defined (or defaults are used).
        Spacing is based on the maximum of the largest plotted symbol
        and the font size.
        """
        gxapi_cy.WrapMVU.prop_symb_legend(GXContext._get_tls_geo(), p1._wrapper, p2, p3, p4, p5, p6, p7, p8, p9, p10.encode(), p11.encode())
        



    @classmethod
    def re_gen_areas(cls, p1, p2):
        """
        Re-Generate from a line group and existing area group

        **Note:**

        The area group must exist and will be modified to match the current
        line group.
        
        All non-polygon entities in the current area group will remain in the
        new area group.  All existing polygon groups will be used to determine
        the most likely attributes for the new polygon groups.
        
        There must be existing polygon groups in the area group.
        """
        gxapi_cy.WrapMVU.re_gen_areas(GXContext._get_tls_geo(), p1._wrapper, p2.encode())
        



    @classmethod
    def symb_off(cls, p1, p2, p3, p4, p5, p6):
        """
        Draws symbols with an offset and against a flag channel

        **Note:**

        Symbols are not plotted for positions where the flag :class:`geosoft.gxapi.GXVV`
        value is 0 or :attr:`geosoft.gxapi.iDUMMY`.
        """
        gxapi_cy.WrapMVU.symb_off(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3._wrapper, p4._wrapper, p5, p6)
        



    @classmethod
    def text_box(cls, p1, p2, p3, p4, p5, p6, p7, p8):
        """
        Draw a wrapped text box
        """
        gxapi_cy.WrapMVU.text_box(GXContext._get_tls_geo(), p1._wrapper, p2, p3, p4, p5, p6.encode(), p7, p8)
        



    @classmethod
    def tick(cls, p1, p2, p3, p4, p5, p6, p7, p8):
        """
        Draw line ticks on a map.
        """
        gxapi_cy.WrapMVU.tick(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3._wrapper, p4._wrapper, p5, p6, p7, p8)
        



    @classmethod
    def tick_ex(cls, p1, p2, p3, p4, p5, p6, p7, p8, p9):
        """
        Same as Tick_MVU, with gap allowance.
        """
        gxapi_cy.WrapMVU.tick_ex(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3._wrapper, p4._wrapper, p5, p6, p7, p8, p9)
        



    @classmethod
    def trnd_path(cls, p1, p2, p3, p4, p5):
        """
        Plot min and max trend lines.

        **Note:**

        Trend lines positions consist of X and Y VVs
        interspersed with dummies, which separate the
        individual trend sections.
        Set the minimum number of sections to > 0 to
        plot only the longer trend lines.
        (The number of sections in one trend section is
        equal to the number of points between dummies minus one.)
        Set the minimum distance to > 0 to
        plot only the longer trend lines.
        """
        gxapi_cy.WrapMVU.trnd_path(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3._wrapper, p4, p5)
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer