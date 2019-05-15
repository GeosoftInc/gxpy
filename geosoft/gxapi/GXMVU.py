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
class GXMVU(gxapi_cy.WrapMVU):
    """
    GXMVU class.

    A catchall library for methods using the `GXMAP <geosoft.gxapi.GXMAP>` and `GXMVIEW <geosoft.gxapi.GXMVIEW>` classes.
    These include drawing flight paths, legends, postings, and
    special objects such as histograms and bar charts.
    """

    def __init__(self, handle=0):
        super(GXMVU, self).__init__(GXContext._get_tls_geo(), handle)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of `GXMVU <geosoft.gxapi.GXMVU>`
        
        :returns: A null `GXMVU <geosoft.gxapi.GXMVU>`
        :rtype:   GXMVU
        """
        return GXMVU()

    def is_null(self):
        """
        Check if this is a null (undefined) instance
        
        :returns: True if this is a null (undefined) instance, False otherwise.
        :rtype:   bool
        """
        return self._internal_handle() == 0



# Miscellaneous


    @classmethod
    def arrow(cls, mview, hx, hy, tx, ty, ratio, angle, type):
        """
        Draw an arrow.
        
        :param mview:  View
        :param hx:     Head X location
        :param hy:     Head Y location
        :param tx:     Tail X location
        :param ty:     Tail Y location
        :param ratio:  See :ref:`MVU_ARROW` definitions for explanation
        :param angle:  Angle of barbs with respect to the tail in degrees.
        :param type:   :ref:`MVU_ARROW`
        :type  mview:  GXMVIEW
        :type  hx:     float
        :type  hy:     float
        :type  tx:     float
        :type  ty:     float
        :type  ratio:  float
        :type  angle:  float
        :type  type:   int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        gxapi_cy.WrapMVU._arrow(GXContext._get_tls_geo(), mview, hx, hy, tx, ty, ratio, angle, type)
        



    @classmethod
    def arrow_vector_vv(cls, mview, vv_x, vv_y, vv_dx, vv_dy, scale, pos, size, style, point, thickness):
        """
        Draw arrow vectors based on input VVs.
        
        :param mview:      View
        :param vv_x:       X locations
        :param vv_y:       Y locations
        :param vv_dx:      X Vector value (can be negative)
        :param vv_dy:      Y Vector value (can be negative)
        :param scale:      Scaling (units/mm)
        :param pos:        :ref:`MVU_VPOS`
        :param size:       :ref:`MVU_VSIZE`
        :param style:      :ref:`MVU_VSTYLE`
        :param point:      :ref:`MVU_VPOINT`
        :param thickness:  Line thickness (can be Dummy)
        :type  mview:      GXMVIEW
        :type  vv_x:       GXVV
        :type  vv_y:       GXVV
        :type  vv_dx:      GXVV
        :type  vv_dy:      GXVV
        :type  scale:      float
        :type  pos:        int
        :type  size:       int
        :type  style:      int
        :type  point:      int
        :type  thickness:  float

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** The locations are given in two VVs, and the directions
        in the two others. A wide range of sizes are available.
        If the scaling is set to `rDUMMY <geosoft.gxapi.rDUMMY>`, then arrows are automatically
        scaled so the largest is 1cm in length.
        If the line thickness is set to `rDUMMY <geosoft.gxapi.rDUMMY>`, the line thickness scales
        with the arrow size, and is 1/20 of the vector length.
        """
        gxapi_cy.WrapMVU._arrow_vector_vv(GXContext._get_tls_geo(), mview, vv_x, vv_y, vv_dx, vv_dy, scale, pos, size, style, point, thickness)
        



    @classmethod
    def bar_chart(cls, mview, group_name, data, line, x_chan, list, x_title, x_txt_size, y_title, y_txt_size, bar_title, bar_txt_size, bar_width, dist_fid, label, tick, right_axis, top_axis, bottom_axis, surround, left, bottom, right, top, xm, ym, widthm, heightm):
        """
        Plot bar chart on a map.
        
        :param mview:         View
        :param group_name:    Group name
        :param data:          Database handle
        :param line:          Line handle
        :param x_chan:        Horizontal (X) axis' channel name
        :param list:          List of channel names (comma separated)
        :param x_title:       X axis title
        :param x_txt_size:    Text size for X axis
        :param y_title:       Y axis title
        :param y_txt_size:    Text size for Y axis
        :param bar_title:     Overall chart title
        :param bar_txt_size:  Text size for overall title
        :param bar_width:     Bar width in mm
        :param dist_fid:      Distance based (1) or fiducial based (0)
        :param label:         :ref:`BARCHART_LABEL`
        :param tick:          Draw ticks along X axis (1) or not (0)
        :param right_axis:    Draw right vertical axis (1) or not
        :param top_axis:      Draw top horizontal axis (1)
        :param bottom_axis:   Draw bottom horizontal axis (1) or not
        :param surround:      Draw surronding box (1) or not (0) The following 4 parameters are required if drawing the surronding box
        :param left:          Width in mm between left Y axis of bar chart with left surronding line
        :param bottom:        Width in mm between bottom X axis of bar chart with bottom surronding line
        :param right:         Width in mm between right Y axis of bar chart with right surronding line
        :param top:           Width in mm between top X axis of bar chart with top surronding line
        :param xm:            X in mm (bottom left corner of bar chart)
        :param ym:            Y in mm (bottom left corner of bar chart)
        :param widthm:        Width of the bar chart in mm
        :param heightm:       Height of the bar chart in mm
        :type  mview:         GXMVIEW
        :type  group_name:    str
        :type  data:          GXDB
        :type  line:          int
        :type  x_chan:        str
        :type  list:          str
        :type  x_title:       str
        :type  x_txt_size:    float
        :type  y_title:       str
        :type  y_txt_size:    float
        :type  bar_title:     str
        :type  bar_txt_size:  float
        :type  bar_width:     float
        :type  dist_fid:      int
        :type  label:         int
        :type  tick:          int
        :type  right_axis:    int
        :type  top_axis:      int
        :type  bottom_axis:   int
        :type  surround:      int
        :type  left:          float
        :type  bottom:        float
        :type  right:         float
        :type  top:           float
        :type  xm:            float
        :type  ym:            float
        :type  widthm:        float
        :type  heightm:       float

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        gxapi_cy.WrapMVU._bar_chart(GXContext._get_tls_geo(), mview, group_name.encode(), data, line, x_chan.encode(), list.encode(), x_title.encode(), x_txt_size, y_title.encode(), y_txt_size, bar_title.encode(), bar_txt_size, bar_width, dist_fid, label, tick, right_axis, top_axis, bottom_axis, surround, left, bottom, right, top, xm, ym, widthm, heightm)
        



    @classmethod
    def cdi_pixel_plot(cls, mview, group, data_va, elev_va, xvv, itr):
        """
        Create a color pixel-style plot of CDI data.
        
        :param mview:    View
        :param group:    Name of the group to create
        :param data_va:  Data [lNR x lNC]
        :param elev_va:  Elevations (Y) [lNR x lNC]
        :param xvv:      Position (X) [lNC]
        :param itr:      Data color transform
        :type  mview:    GXMVIEW
        :type  group:    str
        :type  data_va:  GXVA
        :type  elev_va:  GXVA
        :type  xvv:      GXVV
        :type  itr:      GXITR

        .. versionadded:: 7.2

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** Draws a single colored rectangle for each data point in
        Conductivity-Depth data (for example). It is similar to the
        result you get if you plot a grid with Pixel=1, but in this
        data the row and column widths are not necessarily constant,
        and the data can move up and down with topography. The pixels
        are sized so that the boundaries are half-way between adjacent
        data, both vertically and horizontally.
        """
        gxapi_cy.WrapMVU._cdi_pixel_plot(GXContext._get_tls_geo(), mview, group.encode(), data_va, elev_va, xvv, itr)
        



    @classmethod
    def cdi_pixel_plot_3d(cls, mview, group, data_va, elev_va, xvv, yvv, itr):
        """
        Create a color pixel-style plot of CDI data in a 3D view.
        
        :param mview:    View
        :param group:    Name of the group to create
        :param data_va:  Data [lNR x lNC]
        :param elev_va:  Elevations (Z) [lNR x lNC]
        :param xvv:      Position (X) [lNC]
        :param yvv:      Position (Y) [lNC]
        :param itr:      Data color transform
        :type  mview:    GXMVIEW
        :type  group:    str
        :type  data_va:  GXVA
        :type  elev_va:  GXVA
        :type  xvv:      GXVV
        :type  yvv:      GXVV
        :type  itr:      GXITR

        .. versionadded:: 7.2

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** Similar to `cdi_pixel_plot <geosoft.gxapi.GXMVU.cdi_pixel_plot>`, but plotted onto a series of
        plotting planes which hang from the XY path in 3D. Each vertical plane azimuth
        is defined by two adjacent points on the path. The color "pixel" for each
        data point is plotted in two halves, with each half on adjacent plotting planes,
        with the bend at the data point.
        """
        gxapi_cy.WrapMVU._cdi_pixel_plot_3d(GXContext._get_tls_geo(), mview, group.encode(), data_va, elev_va, xvv, yvv, itr)
        



    @classmethod
    def color_bar(cls, mview, itr, decimal, ann, height, width, x, y):
        """
        Create a Color Bar in view
        
        :param mview:    View
        :param itr:      Itr
        :param decimal:  Decimals
        :param ann:      Annotation offset from box in mm.
        :param height:   Box height
        :param width:    Box width
        :param x:        X location (bottom left corner of color boxes)
        :param y:        Y location
        :type  mview:    GXMVIEW
        :type  itr:      GXITR
        :type  decimal:  int
        :type  ann:      float
        :type  height:   float
        :type  width:    float
        :type  x:        float
        :type  y:        float

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        gxapi_cy.WrapMVU._color_bar(GXContext._get_tls_geo(), mview, itr, decimal, ann, height, width, x, y)
        



    @classmethod
    def color_bar2(cls, mview, itr, itr2, decimal, ann, height, width, x, y):
        """
        Create a Color Bar from two `GXITR <geosoft.gxapi.GXITR>`
        
        :param mview:    View
        :param itr2:     Secondary `GXITR <geosoft.gxapi.GXITR>`
        :param decimal:  Decimals
        :param ann:      Annotation size
        :param height:   Box height
        :param width:    Box width
        :param x:        X location (bottom left corner of color boxes)
        :param y:        Y location
        :type  mview:    GXMVIEW
        :type  itr:      GXITR
        :type  itr2:     GXITR
        :type  decimal:  int
        :type  ann:      float
        :type  height:   float
        :type  width:    float
        :type  x:        float
        :type  y:        float

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** The secondary `GXITR <geosoft.gxapi.GXITR>` is used to blend horizontally with the
        primary `GXITR <geosoft.gxapi.GXITR>` in each box.
        """
        gxapi_cy.WrapMVU._color_bar2(GXContext._get_tls_geo(), mview, itr, itr2, decimal, ann, height, width, x, y)
        



    @classmethod
    def color_bar2_style(cls, mview, itr, itr2, decimal, ann, height, width, x, y, style):
        """
        Create a Color Bar from two ITRs with style options
        
        :param mview:    View
        :param itr2:     Secondary `GXITR <geosoft.gxapi.GXITR>`
        :param decimal:  Decimals
        :param ann:      Annotation size
        :param height:   Box height
        :param width:    Box width
        :param x:        X location (bottom left corner of color boxes)
        :param y:        Y location
        :param style:    :ref:`COLORBAR_STYLE`
        :type  mview:    GXMVIEW
        :type  itr:      GXITR
        :type  itr2:     GXITR
        :type  decimal:  int
        :type  ann:      float
        :type  height:   float
        :type  width:    float
        :type  x:        float
        :type  y:        float
        :type  style:    int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** The secondary `GXITR <geosoft.gxapi.GXITR>` is used to blend horizontally with the
        primary `GXITR <geosoft.gxapi.GXITR>` in each box.
        """
        gxapi_cy.WrapMVU._color_bar2_style(GXContext._get_tls_geo(), mview, itr, itr2, decimal, ann, height, width, x, y, style)
        



    @classmethod
    def color_bar_hor(cls, mview, itr, decimal, ann, width, height, x, y, label_orient):
        """
        Create a horizontal color bar in view
        
        :param mview:         View
        :param itr:           Itr
        :param decimal:       Decimals
        :param ann:           Annotation offset from box in mm (negative for labels below).
        :param width:         Box width in mm
        :param height:        Box height in mm
        :param x:             X location (bottom left corner of color boxes) in mm
        :param y:             Y location in mm
        :param label_orient:  :ref:`COLORBAR_LABEL`
        :type  mview:         GXMVIEW
        :type  itr:           GXITR
        :type  decimal:       int
        :type  ann:           float
        :type  width:         float
        :type  height:        float
        :type  x:             float
        :type  y:             float
        :type  label_orient:  int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** The sign of the annotation offset determines whether labels are
        plotted above or below the colorbar. Labels above are text-justified
        to the bottom of the text, and labels below are text-justified to
        the top of the text.

        .. seealso::

            `color_bar <geosoft.gxapi.GXMVU.color_bar>`
        """
        gxapi_cy.WrapMVU._color_bar_hor(GXContext._get_tls_geo(), mview, itr, decimal, ann, width, height, x, y, label_orient)
        



    @classmethod
    def color_bar_hor2(cls, mview, itr, itr2, decimal, ann, height, width, x, y, label_orient):
        """
        Create a Horizontal Color Bar from two ITRs
        
        :param mview:         View
        :param itr2:          Secondary `GXITR <geosoft.gxapi.GXITR>`
        :param decimal:       Decimals
        :param ann:           Annotation size
        :param height:        Box height
        :param width:         Box width
        :param x:             X location (bottom left corner of color boxes)
        :param y:             Y location
        :param label_orient:  :ref:`COLORBAR_LABEL`
        :type  mview:         GXMVIEW
        :type  itr:           GXITR
        :type  itr2:          GXITR
        :type  decimal:       int
        :type  ann:           float
        :type  height:        float
        :type  width:         float
        :type  x:             float
        :type  y:             float
        :type  label_orient:  int

        .. versionadded:: 5.1

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** The secondary `GXITR <geosoft.gxapi.GXITR>` is used to blend horizontally with the
        primary `GXITR <geosoft.gxapi.GXITR>` in each box.
        """
        gxapi_cy.WrapMVU._color_bar_hor2(GXContext._get_tls_geo(), mview, itr, itr2, decimal, ann, height, width, x, y, label_orient)
        



    @classmethod
    def color_bar_hor2_style(cls, mview, itr, itr2, decimal, ann, height, width, x, y, style, label_orient):
        """
        Create a Horizontal Color Bar from two ITRs with style options
        
        :param mview:         View
        :param itr2:          Secondary `GXITR <geosoft.gxapi.GXITR>`
        :param decimal:       Decimals
        :param ann:           Annotation size
        :param height:        Box height
        :param width:         Box width
        :param x:             X location (bottom left corner of color boxes)
        :param y:             Y location
        :param style:         :ref:`COLORBAR_STYLE`
        :param label_orient:  :ref:`COLORBAR_LABEL`
        :type  mview:         GXMVIEW
        :type  itr:           GXITR
        :type  itr2:          GXITR
        :type  decimal:       int
        :type  ann:           float
        :type  height:        float
        :type  width:         float
        :type  x:             float
        :type  y:             float
        :type  style:         int
        :type  label_orient:  int

        .. versionadded:: 5.1

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** The secondary `GXITR <geosoft.gxapi.GXITR>` is used to blend horizontally with the
        primary `GXITR <geosoft.gxapi.GXITR>` in each box.
        """
        gxapi_cy.WrapMVU._color_bar_hor2_style(GXContext._get_tls_geo(), mview, itr, itr2, decimal, ann, height, width, x, y, style, label_orient)
        



    @classmethod
    def color_bar_hor_style(cls, mview, itr, decimal, ann, height, width, x, y, style, label_orient):
        """
        Create a Horizontal Color Bar in view with style options
        
        :param mview:         View
        :param itr:           Itr
        :param decimal:       Decimals
        :param ann:           Annotation size
        :param height:        Box height
        :param width:         Box width
        :param x:             X location (bottom left corner of color boxes)
        :param y:             Y location
        :param style:         :ref:`COLORBAR_STYLE`
        :param label_orient:  :ref:`COLORBAR_LABEL`
        :type  mview:         GXMVIEW
        :type  itr:           GXITR
        :type  decimal:       int
        :type  ann:           float
        :type  height:        float
        :type  width:         float
        :type  x:             float
        :type  y:             float
        :type  style:         int
        :type  label_orient:  int

        .. versionadded:: 5.1

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        gxapi_cy.WrapMVU._color_bar_hor_style(GXContext._get_tls_geo(), mview, itr, decimal, ann, height, width, x, y, style, label_orient)
        



    @classmethod
    def color_bar_style(cls, mview, itr, decimal, ann, height, width, x, y, style):
        """
        Create a Color Bar in view with style options
        
        :param mview:    View
        :param itr:      Itr
        :param decimal:  Decimals
        :param ann:      Annotation size
        :param height:   Box height
        :param width:    Box width
        :param x:        X location (bottom left corner of color boxes)
        :param y:        Y location
        :param style:    :ref:`COLORBAR_STYLE`
        :type  mview:    GXMVIEW
        :type  itr:      GXITR
        :type  decimal:  int
        :type  ann:      float
        :type  height:   float
        :type  width:    float
        :type  x:        float
        :type  y:        float
        :type  style:    int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        gxapi_cy.WrapMVU._color_bar_style(GXContext._get_tls_geo(), mview, itr, decimal, ann, height, width, x, y, style)
        



    @classmethod
    def color_bar_reg(cls, mview, itr, itr2, reg):
        """
        Create a Color Bar in view
        
        :param mview:  View
        :param itr:    Itr
        :param itr2:   Optional 2nd Itr (can be null)
        :param reg:    Parameters
        :type  mview:  GXMVIEW
        :type  itr:    GXITR
        :type  itr2:   GXITR
        :type  reg:    GXREG

        .. versionadded:: 8.2

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** To allow for expansion, all parameters are passed inside the `GXREG <geosoft.gxapi.GXREG>` object.

        BAR_ORIENTATION        one of MVU_ORIENTATION_XXX (DEFAULT = `MVU_ORIENTATION_VERTICAL <geosoft.gxapi.MVU_ORIENTATION_VERTICAL>`)
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
        DIVISION_STYLE         One of MVU_DIVISION_STYLE_XXX (DEFAULT = `MVU_DIVISION_STYLE_LINES <geosoft.gxapi.MVU_DIVISION_STYLE_LINES>`)
        """
        gxapi_cy.WrapMVU._color_bar_reg(GXContext._get_tls_geo(), mview, itr, itr2, reg)
        



    @classmethod
    def contour(cls, mview, con, grid):
        """
        Creates a contour map.
        
        :param mview:  View
        :param con:    Control file name
        :param grid:   Grid file name
        :type  mview:  GXMVIEW
        :type  con:    str
        :type  grid:   str

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        gxapi_cy.WrapMVU._contour(GXContext._get_tls_geo(), mview, con.encode(), grid.encode())
        



    @classmethod
    def contour_ply(cls, mview, ply, con, grid):
        """
        Creates a contour map with clipped areas.
        
        :param mview:  View
        :param ply:    Clipping `GXPLY <geosoft.gxapi.GXPLY>`
        :param con:    Control file name
        :param grid:   Grid file name
        :type  mview:  GXMVIEW
        :type  ply:    GXPLY
        :type  con:    str
        :type  grid:   str

        .. versionadded:: 5.1.6

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** The clipping `GXPLY <geosoft.gxapi.GXPLY>` can include a surrounding inclusive polygon
        and zero, one or more interior exclusive polygons. Construct
        a `GXPLY <geosoft.gxapi.GXPLY>` object using the `GXPLY.add_polygon_ex <geosoft.gxapi.GXPLY.add_polygon_ex>` function, to add both
        inclusive (as the first `GXPLY <geosoft.gxapi.GXPLY>`) and exclusive interior regions.
        """
        gxapi_cy.WrapMVU._contour_ply(GXContext._get_tls_geo(), mview, ply, con.encode(), grid.encode())
        



    @classmethod
    def c_symb_legend(cls, mview, x1, y1, font_size, symb_scale, file, title, sub_title):
        """
        Plot a legend for the classified color symbols.
        
        :param mview:       `GXMVIEW <geosoft.gxapi.GXMVIEW>` object
        :param x1:          Plot origin X
        :param y1:          Plot origin Y
        :param font_size:   Label Font size (mm)
        :param symb_scale:  Symbol scale factor
        :param file:        `GXAGG <geosoft.gxapi.GXAGG>`, `GXITR <geosoft.gxapi.GXITR>` or ZON file name
        :param title:       Plot title
        :param sub_title:   Plot subtitle
        :type  mview:       GXMVIEW
        :type  x1:          float
        :type  y1:          float
        :type  font_size:   float
        :type  symb_scale:  float
        :type  file:        str
        :type  title:       str
        :type  sub_title:   str

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** If the symbol size, color, font etc are specified in
        the `GXITR <geosoft.gxapi.GXITR>`'s `GXREG <geosoft.gxapi.GXREG>`, then the Symbol scale factor is used
        allow the user to adjust the symbol sizes. They will be
        plotted at a size equal to the size in the `GXREG <geosoft.gxapi.GXREG>` times
        the scale factor.
        If no symbol size info can be found in the `GXREG <geosoft.gxapi.GXREG>`, then
        the symbol size is set equal to the Label Font Size.
        If no symbol font or number info is included in the
        `GXREG <geosoft.gxapi.GXREG>`, it is the programmer's responsibility to select
        the correct font and symbol before CSymbLegend is
        called. The same is true of the edge color.
        """
        gxapi_cy.WrapMVU._c_symb_legend(GXContext._get_tls_geo(), mview, x1, y1, font_size, symb_scale, file.encode(), title.encode(), sub_title.encode())
        



    @classmethod
    def decay_curve(cls, mview, vv_x, vv_y, v_ay, v_ax, log, log_min, angle, x_bar, y_bar, x_off_set, y_off_set, width, height, x_min, y_min, x_scale, y_scale, line_pitch, line_style, line_color):
        """
        Plot decay curves at survey locations
        
        :param mview:       View
        :param vv_x:        X coordinate `GXVV <geosoft.gxapi.GXVV>`
        :param vv_y:        Y coordinate `GXVV <geosoft.gxapi.GXVV>`
        :param v_ay:        `GXVA <geosoft.gxapi.GXVA>` channel to plot
        :param v_ax:        `GXVA <geosoft.gxapi.GXVA>` channel as horizontal axis (normally time channel)
        :param log:         Log option: 0 linear (default), 1 logarithm, 2 log/linear
        :param log_min:     Min value to apply log (must be > 0.0)
        :param angle:       Angle in degrees measured CCW from East of the map
        :param x_bar:       Draw horizontal bar: 0 none, 1 bottom, 2 top, 3 both
        :param y_bar:       Draw vertical bar:   0 none, 1 bottom, 2 top, 3 both
        :param x_off_set:   X offset in mm: Horizontal distance between survey location and origin of the box inside which decay curvey is drawn
        :param y_off_set:   Y offset in mm
        :param width:       Box width in mm:Decay curve at each survey location is drawn within this box
        :param height:      Box height in mm
        :param x_min:       Minimum value for X (horizontal axis)
        :param y_min:       Minimum value for Y (vertical axis)
        :param x_scale:     X scale
        :param y_scale:     Y scale
        :param line_pitch:  Line pitch, default is 5.0mm
        :param line_style:  Line style
        :param line_color:  Line color
        :type  mview:       GXMVIEW
        :type  vv_x:        GXVV
        :type  vv_y:        GXVV
        :type  v_ay:        GXVA
        :type  v_ax:        GXVA
        :type  log:         int
        :type  log_min:     float
        :type  angle:       float
        :type  x_bar:       int
        :type  y_bar:       int
        :type  x_off_set:   float
        :type  y_off_set:   float
        :type  width:       float
        :type  height:      float
        :type  x_min:       float
        :type  y_min:       float
        :type  x_scale:     float
        :type  y_scale:     float
        :type  line_pitch:  float
        :type  line_style:  int
        :type  line_color:  str

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Box width and height are used to draw horizontal and vertical
        bars. Curves outside the box are not clipped.
        """
        gxapi_cy.WrapMVU._decay_curve(GXContext._get_tls_geo(), mview, vv_x, vv_y, v_ay, v_ax, log, log_min, angle, x_bar, y_bar, x_off_set, y_off_set, width, height, x_min, y_min, x_scale, y_scale, line_pitch, line_style, line_color.encode())
        



    @classmethod
    def direction_plot(cls, mview, vv_x, vv_y, size, loc, align):
        """
        Plot an arrow to indicate the direction of a flight line
        
        :param mview:  View
        :param vv_x:   X `GXVV <geosoft.gxapi.GXVV>`
        :param vv_y:   Y `GXVV <geosoft.gxapi.GXVV>`
        :param size:   Arrow size in mm
        :param loc:    Location to draw in mm - can be X or Y depending on next parameter
        :param align:  :ref:`ARROW_ALIGNMENT`
        :type  mview:  GXMVIEW
        :type  vv_x:   GXVV
        :type  vv_y:   GXVV
        :type  size:   float
        :type  loc:    float
        :type  align:  int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** An arrow will be drawn in the direction from the first valid
        to the last points in the X and Y VVs.
        """
        gxapi_cy.WrapMVU._direction_plot(GXContext._get_tls_geo(), mview, vv_x, vv_y, size, loc, align)
        



    @classmethod
    def em_forward(cls, mview, xo, yo, size_x, size_y, coil_sep, coil_frequency, coil_configuration, r, h, i, q, rvv, hvv, ivv, qvv, lin_log, var):
        """
        Plot an EM forward model against inverted data.
        
        :param mview:               View
        :param xo:                  Plot X origin
        :param yo:                  Plot Y origin
        :param size_x:              Plot X size
        :param size_y:              Plot Y size
        :param coil_sep:            Coil Separation (m)
        :param coil_frequency:      Coil Frequency (Hz)
        :param coil_configuration:  :ref:`EMLAY_GEOMETRY`
        :param r:                   Inverted or current resistivity
        :param h:                   Inverted or current height
        :param i:                   In-phase datum
        :param q:                   Quadrature datum
        :param rvv:                 Forward model resistivities
        :param hvv:                 Forward model heights
        :param ivv:                 Forward model In-phase (ppm)
        :param qvv:                 Forward model Quadrature (ppm)
        :param lin_log:             Plot resistivity as linear (0) or log (1)
        :param var:                 Plot as function of resistivity (0) or height (1)
        :type  mview:               GXMVIEW
        :type  xo:                  float
        :type  yo:                  float
        :type  size_x:              float
        :type  size_y:              float
        :type  coil_sep:            float
        :type  coil_frequency:      float
        :type  coil_configuration:  int
        :type  r:                   float
        :type  h:                   float
        :type  i:                   float
        :type  q:                   float
        :type  rvv:                 GXVV
        :type  hvv:                 GXVV
        :type  ivv:                 GXVV
        :type  qvv:                 GXVV
        :type  lin_log:             int
        :type  var:                 int

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** This function is designed to display an inverted result beside
        the forward model curves. This is useful for trouble-shooting
        or understanding why a certain inversion result was obtained.
        The earth model is a simple halfspace.

        The forward model is plotted either as a function of
        resistivity at a single height, or as a function of height at
        a single resistivity. In either case, the relevant VVs must be
        completely filled (even if one is all the same value).
        """
        gxapi_cy.WrapMVU._em_forward(GXContext._get_tls_geo(), mview, xo, yo, size_x, size_y, coil_sep, coil_frequency, coil_configuration, r, h, i, q, rvv, hvv, ivv, qvv, lin_log, var)
        



    @classmethod
    def export_datamine_string(cls, mview, lst, file):
        """
        Export selected map groups in a map view to a Datamine coordinate string file.
        
        :param mview:  View
        :param lst:    `GXLST <geosoft.gxapi.GXLST>` with group names in the name part of the `GXLST <geosoft.gxapi.GXLST>`.
        :param file:   Datamine string file (``*.dm``) to export to
        :type  mview:  GXMVIEW
        :type  lst:    GXLST
        :type  file:   str

        .. versionadded:: 6.3

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** The lines, rectangles and polygons in the specified groups
        will be exported to a Datamine coordinate string (``*.dm``) file.
        The function attempts to duplicate the colors, etc. used.
        Complex polygon objects will be exported as independent
        single polygons.

        .. seealso::

            `GXLST <geosoft.gxapi.GXLST>` class
        """
        gxapi_cy.WrapMVU._export_datamine_string(GXContext._get_tls_geo(), mview, lst, file.encode())
        



    @classmethod
    def export_dxf_3d(cls, mview, lst, wa):
        """
        Export selected map groups in a map view to an AutoCAD 3D DXF file.
        
        :param mview:  View
        :param lst:    `GXLST <geosoft.gxapi.GXLST>` with group names in the name part of the `GXLST <geosoft.gxapi.GXLST>`.
        :param wa:     DXF file to export
        :type  mview:  GXMVIEW
        :type  lst:    GXLST
        :type  wa:     GXWA

        .. versionadded:: 6.2

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Supported objects exported include lines, polygons, text.

        .. seealso::

            `GXLST <geosoft.gxapi.GXLST>` class
        """
        gxapi_cy.WrapMVU._export_dxf_3d(GXContext._get_tls_geo(), mview, lst, wa)
        



    @classmethod
    def export_surpac_str(cls, mview, lst, str_wa, styles_wa):
        """
        Export selected map groups in a map view to a Surpac `GXSTR <geosoft.gxapi.GXSTR>` file.
        
        :param mview:      View
        :param lst:        `GXLST <geosoft.gxapi.GXLST>` with group names in the name part of the `GXLST <geosoft.gxapi.GXLST>`.
        :param str_wa:     `GXSTR <geosoft.gxapi.GXSTR>` file to export to
        :param styles_wa:  Styles file to export to
        :type  mview:      GXMVIEW
        :type  lst:        GXLST
        :type  str_wa:     GXWA
        :type  styles_wa:  GXWA

        .. versionadded:: 6.2

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** The lines, rectangles and polygons in the specified groups
        will be exported to a Surpac `GXSTR <geosoft.gxapi.GXSTR>` file. An accompanying styles
        file will be created which will attempt to duplicate the
        colors, etc. used.
        Complex polygon objects will be exported as independent
        single polygons.

        .. seealso::

            `GXLST <geosoft.gxapi.GXLST>` class
        """
        gxapi_cy.WrapMVU._export_surpac_str(GXContext._get_tls_geo(), mview, lst, str_wa, styles_wa)
        



    @classmethod
    def export_map_groups_to_gdb(cls, mview, lst, db):
        """
        Export map group(s) to database line(s).
        
        :param mview:  View
        :param lst:    `GXLST <geosoft.gxapi.GXLST>` with group names in the name part of the `GXLST <geosoft.gxapi.GXLST>`.
        :param db:     Database
        :type  mview:  GXMVIEW
        :type  lst:    GXLST
        :type  db:     GXDB

        .. versionadded:: 9.4

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        gxapi_cy.WrapMVU._export_map_groups_to_gdb(GXContext._get_tls_geo(), mview, lst, db)
        



    @classmethod
    def flight_plot(cls, mview, vv_x, vv_y, line, locate, vangle, up, loff, voff):
        """
        Draw a flight line
        
        :param mview:   View
        :param vv_x:    X
        :param vv_y:    Y
        :param line:    Line label
        :param locate:  :ref:`MVU_FLIGHT_LOCATE`
        :param vangle:  Lines steeper than this angle are considered vertical and the up label direction is used.
        :param up:      Up label direction:   1 up is right, -1 up is left
        :param loff:    Along line label offset in mm.
        :param voff:    Perpendicular label offset mm.
        :type  mview:   GXMVIEW
        :type  vv_x:    GXVV
        :type  vv_y:    GXVV
        :type  line:    str
        :type  locate:  int
        :type  vangle:  float
        :type  up:      int
        :type  loff:    float
        :type  voff:    float

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Current line color, thickness and style are used to
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

        .. seealso::

            `path_plot <geosoft.gxapi.GXMVU.path_plot>`
        """
        gxapi_cy.WrapMVU._flight_plot(GXContext._get_tls_geo(), mview, vv_x, vv_y, line.encode(), locate, vangle, up, loff, voff)
        



    @classmethod
    def gen_areas(cls, mview, lines, col_vv, pat_vv, pitch):
        """
        Generate areas from an line group.
        
        :param mview:   View
        :param lines:   Group with lines
        :param col_vv:  Colors  (color int)
        :param pat_vv:  Patterns (int), must be same length at colors
        :param pitch:   Pattern size
        :type  mview:   GXMVIEW
        :type  lines:   str
        :type  col_vv:  GXVV
        :type  pat_vv:  GXVV
        :type  pitch:   float

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** The specified line group will be used to create a new group that
        is composed of all the resolved polygonal areas in the line group.
        Each polygonal area is assigned a color/pattern as specified in the
        color and pattern `GXVV <geosoft.gxapi.GXVV>`'s.  Color/patterns are assigned in rotating
        sequence.

        .. seealso::

            `re_gen_areas <geosoft.gxapi.GXMVU.re_gen_areas>`
        """
        gxapi_cy.WrapMVU._gen_areas(GXContext._get_tls_geo(), mview, lines.encode(), col_vv, pat_vv, pitch)
        



    @classmethod
    def get_range_gocad_surface(cls, file, min_x, min_y, min_z, max_x, max_y, max_z):
        """
        Get the XYZ range of a GOCAD surface.
        
        :param file:   GOCAD file name
        :param min_x:  Min X value
        :param min_y:  Min Y value
        :param min_z:  Min Z value
        :param max_x:  Max X value
        :param max_y:  Max Y value
        :param max_z:  Max Z value
        :type  file:   str
        :type  min_x:  float_ref
        :type  min_y:  float_ref
        :type  min_z:  float_ref
        :type  max_x:  float_ref
        :type  max_y:  float_ref
        :type  max_z:  float_ref

        .. versionadded:: 6.4

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Required to set up a map view before doing the actual
        surface import.
        """
        min_x.value, min_y.value, min_z.value, max_x.value, max_y.value, max_z.value = gxapi_cy.WrapMVU._get_range_gocad_surface(GXContext._get_tls_geo(), file.encode(), min_x.value, min_y.value, min_z.value, max_x.value, max_y.value, max_z.value)
        



    @classmethod
    def histogram(cls, mview, st_data, st_hist, title, unit, xm, ym, widthm, heightm, xd, yd, widthd, heightd, sum_width, log, summ, fill_color, st_box):
        """
        Plot the histogram on a map.
        
        :param mview:       View
        :param st_data:     `GXST <geosoft.gxapi.GXST>` with summary stats of original data
        :param st_hist:     `GXST <geosoft.gxapi.GXST>` with histogram info of original or log10 data
        :param title:       Title
        :param unit:        Unit
        :param xm:          X in mm (bottom left corner of histogram box)
        :param ym:          Y in mm (bottom left corner of histogram box)
        :param widthm:      Box width in mm
        :param heightm:     Box height in mm
        :param xd:          Minimum X in data unit (bottom left corner of histogram boxes)
        :param yd:          Minimum Y in data unit
        :param widthd:      Box width in data unit
        :param heightd:     Box height in data unit
        :param sum_width:   Width (mm) of the additional box for summary stats
        :param log:         Log horizontal axis: 0 - Normal, 1 - Log
        :param summ:        Summary stats: 0 - do not draw, 1 - draw
        :param fill_color:  Fill color
        :param st_box:      `GXST <geosoft.gxapi.GXST>` with histogram for box-whisker plot (-1 for no plot)
        :type  mview:       GXMVIEW
        :type  st_data:     GXST
        :type  st_hist:     GXST
        :type  title:       str
        :type  unit:        str
        :type  xm:          float
        :type  ym:          float
        :type  widthm:      float
        :type  heightm:     float
        :type  xd:          float
        :type  yd:          float
        :type  widthd:      float
        :type  heightd:     float
        :type  sum_width:   float
        :type  log:         int
        :type  summ:        int
        :type  fill_color:  int
        :type  st_box:      GXST

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** This function just calls `histogram2 <geosoft.gxapi.GXMVU.histogram2>` with decimals set
        to -7 (7 significant figures).

        .. seealso::

            `histogram2 <geosoft.gxapi.GXMVU.histogram2>`, `histogram3 <geosoft.gxapi.GXMVU.histogram3>`
        """
        gxapi_cy.WrapMVU._histogram(GXContext._get_tls_geo(), mview, st_data, st_hist, title.encode(), unit.encode(), xm, ym, widthm, heightm, xd, yd, widthd, heightd, sum_width, log, summ, fill_color, st_box)
        



    @classmethod
    def histogram2(cls, mview, st_data, st_hist, x_title, y_title, xy_txt_size, title, plot_txt_size, unit, xm, ym, widthm, heightm, xd, yd, widthd, heightd, sum_width, log, summ, fill_color, st_box, x_marker):
        """
        Plot the histogram on a map.
        
        :param mview:          View
        :param st_data:        `GXST <geosoft.gxapi.GXST>` with summary stats of original data
        :param st_hist:        `GXST <geosoft.gxapi.GXST>` with histogram info of original or log10 data
        :param x_title:        X axis title
        :param y_title:        Y axis title
        :param xy_txt_size:    Text size in mm for X/Y axis' titles. Accept dummy
        :param title:          Overall title. Plotted below X axis if X axis title is not given
        :param plot_txt_size:  Text size in mm for plot overall title. Accept dummy
        :param unit:           Unit
        :param xm:             X in mm (bottom left corner of histogram box)
        :param ym:             Y in mm (bottom left corner of histogram box)
        :param widthm:         Box width in mm
        :param heightm:        Box height in mm
        :param xd:             Minimum X in data unit (bottom left corner of histogram boxes)
        :param yd:             Minimum Y in data unit
        :param widthd:         Box width in data unit
        :param heightd:        Box height in data unit
        :param sum_width:      Width (mm) of the additional box for summary stats
        :param log:            Log horizontal axis: 0 - Normal, 1 - Log
        :param summ:           Summary stats: 0 - do not draw, 1 - draw
        :param fill_color:     Fill color
        :param st_box:         `GXST <geosoft.gxapi.GXST>` with histogram for box-wisker plot (-1 for no plot)
        :param x_marker:       X value (threshold value) to draw a vertical line (see notes)
        :type  mview:          GXMVIEW
        :type  st_data:        GXST
        :type  st_hist:        GXST
        :type  x_title:        str
        :type  y_title:        str
        :type  xy_txt_size:    float
        :type  title:          str
        :type  plot_txt_size:  float
        :type  unit:           str
        :type  xm:             float
        :type  ym:             float
        :type  widthm:         float
        :type  heightm:        float
        :type  xd:             float
        :type  yd:             float
        :type  widthd:         float
        :type  heightd:        float
        :type  sum_width:      float
        :type  log:            int
        :type  summ:           int
        :type  fill_color:     int
        :type  st_box:         GXST
        :type  x_marker:       float

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** A vertical line through from bottom to top horizontal axis is drawn
        Also a label 'Threshold value' is plotted against this line. However,
        None of them will be plotted if threshold value is dummy or outside
        the X data range.
        """
        gxapi_cy.WrapMVU._histogram2(GXContext._get_tls_geo(), mview, st_data, st_hist, x_title.encode(), y_title.encode(), xy_txt_size, title.encode(), plot_txt_size, unit.encode(), xm, ym, widthm, heightm, xd, yd, widthd, heightd, sum_width, log, summ, fill_color, st_box, x_marker)
        



    @classmethod
    def histogram3(cls, mview, st_data, st_hist, title, unit, xm, ym, widthm, heightm, xd, yd, widthd, heightd, sum_width, log, summ, fill_color, data_decimal, stat_decimal, st_box):
        """
        Plot the histogram on a map, specify decimals.
        
        :param mview:         View
        :param st_data:       `GXST <geosoft.gxapi.GXST>` with summary stats of original data
        :param st_hist:       `GXST <geosoft.gxapi.GXST>` with histogram info of original or log10 data
        :param title:         Title
        :param unit:          Unit
        :param xm:            X in mm (bottom left corner of histogram box)
        :param ym:            Y in mm (bottom left corner of histogram box)
        :param widthm:        Box width in mm
        :param heightm:       Box height in mm
        :param xd:            Minimum X in data unit (bottom left corner of histogram boxes)
        :param yd:            Minimum Y in data unit
        :param widthd:        Box width in data unit
        :param heightd:       Box height in data unit
        :param sum_width:     Width (mm) of the additional box for summary stats
        :param log:           Log horizontal axis: 0 - Normal, 1 - Log
        :param summ:          Summary stats: 0 - do not draw, 1 - draw
        :param fill_color:    Fill color
        :param data_decimal:  Decimals for data, negative for sig. fig.
        :param stat_decimal:  Decimals for stats, negative for sig. fig.
        :param st_box:        `GXST <geosoft.gxapi.GXST>` with histogram for box-whisker plot (-1 for no plot)
        :type  mview:         GXMVIEW
        :type  st_data:       GXST
        :type  st_hist:       GXST
        :type  title:         str
        :type  unit:          str
        :type  xm:            float
        :type  ym:            float
        :type  widthm:        float
        :type  heightm:       float
        :type  xd:            float
        :type  yd:            float
        :type  widthd:        float
        :type  heightd:       float
        :type  sum_width:     float
        :type  log:           int
        :type  summ:          int
        :type  fill_color:    int
        :type  data_decimal:  int
        :type  stat_decimal:  int
        :type  st_box:        GXST

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        gxapi_cy.WrapMVU._histogram3(GXContext._get_tls_geo(), mview, st_data, st_hist, title.encode(), unit.encode(), xm, ym, widthm, heightm, xd, yd, widthd, heightd, sum_width, log, summ, fill_color, data_decimal, stat_decimal, st_box)
        



    @classmethod
    def histogram4(cls, mview, st_data, st_hist, title, unit, xm, ym, widthm, heightm, xd, yd, widthd, heightd, sum_width, log, summ, prob, fill_color, data_decimal, stat_decimal, st_box):
        """
        As `histogram3 <geosoft.gxapi.GXMVU.histogram3>`, but allow probability scaling of percents.
        
        :param mview:         View
        :param st_data:       `GXST <geosoft.gxapi.GXST>` with summary stats of original data
        :param st_hist:       `GXST <geosoft.gxapi.GXST>` with histogram info of original or log10 data
        :param title:         Title
        :param unit:          Unit
        :param xm:            X in mm (bottom left corner of histogram box)
        :param ym:            Y in mm (bottom left corner of histogram box)
        :param widthm:        Box width in mm
        :param heightm:       Box height in mm
        :param xd:            Minimum X in data unit (bottom left corner of histogram boxes)
        :param yd:            Minimum Y in data unit
        :param widthd:        Box width in data unit
        :param heightd:       Box height in data unit
        :param sum_width:     Width (mm) of the additional box for summary stats
        :param log:           Log horizontal axis: 0 - Normal, 1 - Log
        :param summ:          Summary stats: 0 - do not draw, 1 - draw
        :param prob:          Probability scaling: 0 - linear scale, 1 - scale as normal distribution
        :param fill_color:    Fill color
        :param data_decimal:  Decimals for data, negative for sig. fig.
        :param stat_decimal:  Decimals for stats, negative for sig. fig.
        :param st_box:        `GXST <geosoft.gxapi.GXST>` with histogram for box-whisker plot (-1 for no plot)
        :type  mview:         GXMVIEW
        :type  st_data:       GXST
        :type  st_hist:       GXST
        :type  title:         str
        :type  unit:          str
        :type  xm:            float
        :type  ym:            float
        :type  widthm:        float
        :type  heightm:       float
        :type  xd:            float
        :type  yd:            float
        :type  widthd:        float
        :type  heightd:       float
        :type  sum_width:     float
        :type  log:           int
        :type  summ:          int
        :type  prob:          int
        :type  fill_color:    int
        :type  data_decimal:  int
        :type  stat_decimal:  int
        :type  st_box:        GXST

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        gxapi_cy.WrapMVU._histogram4(GXContext._get_tls_geo(), mview, st_data, st_hist, title.encode(), unit.encode(), xm, ym, widthm, heightm, xd, yd, widthd, heightd, sum_width, log, summ, prob, fill_color, data_decimal, stat_decimal, st_box)
        



    @classmethod
    def histogram5(cls, mview, st_data, st_hist, title, unit, lmd, xm, ym, widthm, heightm, xd, yd, widthd, heightd, sum_width, log, summ, prob, fill_color, data_decimal, stat_decimal, st_box, itr):
        """
        As `histogram4 <geosoft.gxapi.GXMVU.histogram4>`, but allow `GXITR <geosoft.gxapi.GXITR>` to color bars.
        
        :param mview:         View
        :param st_data:       `GXST <geosoft.gxapi.GXST>` with summary stats of original data
        :param st_hist:       `GXST <geosoft.gxapi.GXST>` with histogram info of original or log10 data
        :param title:         Title
        :param unit:          Unit
        :param lmd:           [i] Lambda Value
        :param xm:            X in mm (bottom left corner of histogram box)
        :param ym:            Y in mm (bottom left corner of histogram box)
        :param widthm:        Box width in mm
        :param heightm:       Box height in mm
        :param xd:            Minimum X in data unit (bottom left corner of histogram boxes)
        :param yd:            Minimum Y in data unit
        :param widthd:        Box width in data unit
        :param heightd:       Box height in data unit
        :param sum_width:     Width (mm) of the additional box for summary stats
        :param log:           Log horizontal axis: 0 - Normal, 1 - Log, 2 - Lambda
        :param summ:          Summary stats: 0 - do not draw, 1 - draw
        :param prob:          Probability scaling: 0 - linear scale, 1 - scale as normal distribution
        :param fill_color:    Fill color
        :param data_decimal:  Decimals for data, negative for sig. fig.
        :param stat_decimal:  Decimals for stats, negative for sig. fig.
        :param st_box:        `GXST <geosoft.gxapi.GXST>` with histogram for box-whisker plot (-1 for no plot)
        :param itr:           `GXITR <geosoft.gxapi.GXITR>` to color bars.
        :type  mview:         GXMVIEW
        :type  st_data:       GXST
        :type  st_hist:       GXST
        :type  title:         str
        :type  unit:          str
        :type  lmd:           float
        :type  xm:            float
        :type  ym:            float
        :type  widthm:        float
        :type  heightm:       float
        :type  xd:            float
        :type  yd:            float
        :type  widthd:        float
        :type  heightd:       float
        :type  sum_width:     float
        :type  log:           int
        :type  summ:          int
        :type  prob:          int
        :type  fill_color:    int
        :type  data_decimal:  int
        :type  stat_decimal:  int
        :type  st_box:        GXST
        :type  itr:           GXITR

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** The `GXITR <geosoft.gxapi.GXITR>` can be empty (but must still be a valid `GXITR <geosoft.gxapi.GXITR>` object).
        """
        gxapi_cy.WrapMVU._histogram5(GXContext._get_tls_geo(), mview, st_data, st_hist, title.encode(), unit.encode(), lmd, xm, ym, widthm, heightm, xd, yd, widthd, heightd, sum_width, log, summ, prob, fill_color, data_decimal, stat_decimal, st_box, itr)
        



    @classmethod
    def exportable_dxf_3d_groups_lst(cls, mview, lst):
        """
        Return a `GXLST <geosoft.gxapi.GXLST>` of groups you can export using sExportDXF3D_MVU.
        
        :param mview:  View
        :param lst:    `GXLST <geosoft.gxapi.GXLST>` with group names in the name part of the `GXLST <geosoft.gxapi.GXLST>`.
        :type  mview:  GXMVIEW
        :type  lst:    GXLST

        :returns:      The number of groups in the `GXLST <geosoft.gxapi.GXLST>`.
        :rtype:        int

        .. versionadded:: 7.1

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Returns a list of visible groups that the DXF 3D export can
        export. Removes things like `GXVOXD <geosoft.gxapi.GXVOXD>`, `GXAGG <geosoft.gxapi.GXAGG>`, and target
        groups starting with "Dh", which are typically plotted in 3D
        views on a reference plan oriented toward the user, and thus
        not exportable.
        """
        ret_val = gxapi_cy.WrapMVU._exportable_dxf_3d_groups_lst(GXContext._get_tls_geo(), mview, lst)
        return ret_val



    @classmethod
    def mapset_test(cls, min_x, max_x, min_y, max_y, size, port, exact, scale, conv, marg_xmin, marg_xmax, marg_ymin, marg_ymax, inside):
        """
        Test function to ensure parameters to `mapset <geosoft.gxapi.GXMVU.mapset>` is sane
        
        :param min_x:      Minimum X of data area (data units)
        :param max_x:      Maximum X of data area (data units)
        :param min_y:      Minimum Y of data area (data units)
        :param max_y:      Maximum Y of data area (data units)
        :param size:       Media size as a string 'x_cm,y_cm', or a standard paper size (e.g. 'A4', 'E')
        :param port:       0 - landscape; 1 - portrait
        :param exact:      1 - map size fixed to media; 0 - map size adjusted to data and margins.
        :param scale:      Map scale (rDummy for default)
        :param conv:       Conversion factor (to units/meter) (rDummy for default)
        :param marg_xmin:  Left margin (cm)
        :param marg_xmax:  Right margin (cm)
        :param marg_ymin:  Bottom margin (cm)
        :param marg_ymax:  Top margin (cm)
        :param inside:     Inside data margin (cm)
        :type  min_x:      float
        :type  max_x:      float
        :type  min_y:      float
        :type  max_y:      float
        :type  size:       str
        :type  port:       int
        :type  exact:      int
        :type  scale:      float_ref
        :type  conv:       float
        :type  marg_xmin:  float
        :type  marg_xmax:  float
        :type  marg_ymin:  float
        :type  marg_ymax:  float
        :type  inside:     float

        :returns:          ``True`` if the parameters are good.
        :rtype:            bool

        .. versionadded:: 6.3

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Use `GXSYS.show_error <geosoft.gxapi.GXSYS.show_error>` to display errors that may have been encountered. This function can also be used
        to calculate the default scale without creating a map.
        """
        ret_val, scale.value = gxapi_cy.WrapMVU._mapset_test(GXContext._get_tls_geo(), min_x, max_x, min_y, max_y, size.encode(), port, exact, scale.value, conv, marg_xmin, marg_xmax, marg_ymin, marg_ymax, inside)
        return ret_val



    @classmethod
    def mapset2_test(cls, min_x, max_x, min_y, max_y, size, port, exact, scale, vert_exag, conv, marg_xmin, marg_xmax, marg_ymin, marg_ymax, inside):
        """
        Test function to ensure parameters to `mapset <geosoft.gxapi.GXMVU.mapset>` is sane
        
        :param min_x:      Minimum X of data area (data units)
        :param max_x:      Maximum X of data area (data units)
        :param min_y:      Minimum Y of data area (data units)
        :param max_y:      Maximum Y of data area (data units)
        :param size:       Media size as a string 'x_cm,y_cm', or a standard paper size (e.g. 'A4', 'E')
        :param port:       0 - landscape; 1 - portrait
        :param exact:      1 - map size fixed to media; 0 - map size adjusted to data and margins.
        :param scale:      Map scale (rDummy for default)
        :param vert_exag:  Vertical exaggeration (Normally 1.0)
        :param conv:       Conversion factor (to units/meter) (rDummy for default)
        :param marg_xmin:  Left margin (cm)
        :param marg_xmax:  Right margin (cm)
        :param marg_ymin:  Bottom margin (cm)
        :param marg_ymax:  Top margin (cm)
        :param inside:     Inside data margin (cm)
        :type  min_x:      float
        :type  max_x:      float
        :type  min_y:      float
        :type  max_y:      float
        :type  size:       str
        :type  port:       int
        :type  exact:      int
        :type  scale:      float_ref
        :type  vert_exag:  float
        :type  conv:       float
        :type  marg_xmin:  float
        :type  marg_xmax:  float
        :type  marg_ymin:  float
        :type  marg_ymax:  float
        :type  inside:     float

        :returns:          ``True`` if the parameters are good.
        :rtype:            bool

        .. versionadded:: 8.3

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Same as `mapset_test <geosoft.gxapi.GXMVU.mapset_test>`, with vertical exaggeration.
        """
        ret_val, scale.value = gxapi_cy.WrapMVU._mapset2_test(GXContext._get_tls_geo(), min_x, max_x, min_y, max_y, size.encode(), port, exact, scale.value, vert_exag, conv, marg_xmin, marg_xmax, marg_ymin, marg_ymax, inside)
        return ret_val



    @classmethod
    def import_gocad_surface(cls, mview, file, col):
        """
        Import and plot a GOCAD surface model.
        
        :param mview:  View
        :param file:   GOCAD file name
        :param col:    Color to plot (`C_TRANSPARENT <geosoft.gxapi.C_TRANSPARENT>` to use file-defined color).
        :type  mview:  GXMVIEW
        :type  file:   str
        :type  col:    int

        .. versionadded:: 6.4

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** The vertex normals are not included in the
        GOCAD import, but are calculated using
        the normal of each defined triangle, and taking the
        average when vertex is shared among more than one triangle.
        """
        gxapi_cy.WrapMVU._import_gocad_surface(GXContext._get_tls_geo(), mview, file.encode(), col)
        



    @classmethod
    def load_plot(cls, map, name):
        """
        Load a Geosoft PLT file into a `GXMAP <geosoft.gxapi.GXMAP>`.
        
        :param map:   Map handle
        :param name:  Plot file name
        :type  map:   GXMAP
        :type  name:  str

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        gxapi_cy.WrapMVU._load_plot(GXContext._get_tls_geo(), map, name.encode())
        



    @classmethod
    def map_from_plt(cls, map, base, data, plt, mpx, mpy):
        """
        Creates a new map from a PLT file.
        
        :param map:   `GXMAP <geosoft.gxapi.GXMAP>` Handle
        :param base:  Name to use for the base map view
        :param data:  Name to use for the data view
        :param plt:   Plot file name
        :param mpx:   Map paper size in X direction (cm)
        :param mpy:   Map paper size in Y direction (cm)
        :type  map:   GXMAP
        :type  base:  str
        :type  data:  str
        :type  plt:   str
        :type  mpx:   float
        :type  mpy:   float

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** This only creates a map, it does not read the PLT into
        the map.  The base view and data view will be the same
        size.

        .. seealso::

            `load_plot <geosoft.gxapi.GXMVU.load_plot>`
        """
        gxapi_cy.WrapMVU._map_from_plt(GXContext._get_tls_geo(), map, base.encode(), data.encode(), plt.encode(), mpx, mpy)
        



    @classmethod
    def map_mdf(cls, map, mdf, data):
        """
        Creates an MDF from a Map.
        
        :param map:   `GXMAP <geosoft.gxapi.GXMAP>` Handle
        :param mdf:   MDF file name
        :param data:  Data view name
        :type  map:   GXMAP
        :type  mdf:   str
        :type  data:  str

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        gxapi_cy.WrapMVU._map_mdf(GXContext._get_tls_geo(), map, mdf.encode(), data.encode())
        



    @classmethod
    def mapset(cls, map, base, data, min_x, max_x, min_y, max_y, size, port, exact, scale, conv, marg_xmin, marg_xmax, marg_ymin, marg_ymax, inside):
        """
        Creates a new map directly from parameters.
        
        :param map:        `GXMAP <geosoft.gxapi.GXMAP>` Handle
        :param base:       Name to use for the base map view
        :param data:       Name to use for the data view
        :param min_x:      Minimum X of data area (data units)
        :param max_x:      Maximum X of data area (data units)
        :param min_y:      Minimum Y of data area (data units)
        :param max_y:      Maximum Y of data area (data units)
        :param size:       Media size as a string 'x_cm,y_cm', or a standard paper size (e.g. 'A4', 'E')
        :param port:       0 - landscape; 1 - portrait
        :param exact:      1 - map size fixed to media; 0 - map size adjusted to data and margins.
        :param scale:      Map scale (rDummy for default)
        :param conv:       Conversion factor (to units/meter) (rDummy for default)
        :param marg_xmin:  Left margin (cm)
        :param marg_xmax:  Right margin (cm)
        :param marg_ymin:  Bottom margin (cm)
        :param marg_ymax:  Top margin (cm)
        :param inside:     Inside data margin (cm)
        :type  map:        GXMAP
        :type  base:       str
        :type  data:       str
        :type  min_x:      float
        :type  max_x:      float
        :type  min_y:      float
        :type  max_y:      float
        :type  size:       str
        :type  port:       int
        :type  exact:      int
        :type  scale:      float
        :type  conv:       float
        :type  marg_xmin:  float
        :type  marg_xmax:  float
        :type  marg_ymin:  float
        :type  marg_ymax:  float
        :type  inside:     float

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        gxapi_cy.WrapMVU._mapset(GXContext._get_tls_geo(), map, base.encode(), data.encode(), min_x, max_x, min_y, max_y, size.encode(), port, exact, scale, conv, marg_xmin, marg_xmax, marg_ymin, marg_ymax, inside)
        



    @classmethod
    def mapset2(cls, map, base, data, min_x, max_x, min_y, max_y, size, port, exact, scale, vert_exag, conv, marg_xmin, marg_xmax, marg_ymin, marg_ymax, inside):
        """
        Same as `mapset <geosoft.gxapi.GXMVU.mapset>`, with vertical exaggeration.
        
        :param map:        `GXMAP <geosoft.gxapi.GXMAP>` Handle
        :param base:       Name to use for the base map view
        :param data:       Name to use for the data view
        :param min_x:      Minimum X of data area (data units)
        :param max_x:      Maximum X of data area (data units)
        :param min_y:      Minimum Y of data area (data units)
        :param max_y:      Maximum Y of data area (data units)
        :param size:       Media size as a string 'x_cm,y_cm', or a standard paper size (e.g. 'A4', 'E')
        :param port:       0 - landscape; 1 - portrait
        :param exact:      1 - map size fixed to media; 0 - map size adjusted to data and margins.
        :param scale:      Map scale (rDummy for default)
        :param vert_exag:  Vertical Exaggeration (1.0 for none)
        :param conv:       Conversion factor (to units/meter) (rDummy for default)
        :param marg_xmin:  Left margin (cm)
        :param marg_xmax:  Right margin (cm)
        :param marg_ymin:  Bottom margin (cm)
        :param marg_ymax:  Top margin (cm)
        :param inside:     Inside data margin (cm)
        :type  map:        GXMAP
        :type  base:       str
        :type  data:       str
        :type  min_x:      float
        :type  max_x:      float
        :type  min_y:      float
        :type  max_y:      float
        :type  size:       str
        :type  port:       int
        :type  exact:      int
        :type  scale:      float
        :type  vert_exag:  float
        :type  conv:       float
        :type  marg_xmin:  float
        :type  marg_xmax:  float
        :type  marg_ymin:  float
        :type  marg_ymax:  float
        :type  inside:     float

        .. versionadded:: 8.3

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        gxapi_cy.WrapMVU._mapset2(GXContext._get_tls_geo(), map, base.encode(), data.encode(), min_x, max_x, min_y, max_y, size.encode(), port, exact, scale, vert_exag, conv, marg_xmin, marg_xmax, marg_ymin, marg_ymax, inside)
        



    @classmethod
    def mdf(cls, map, mdf, base, data):
        """
        Creates a new map from an MDF file.
        
        :param map:   `GXMAP <geosoft.gxapi.GXMAP>` Handle
        :param mdf:   MDF file name
        :param base:  Name to use for the base map view
        :param data:  Name to use for the data view
        :type  map:   GXMAP
        :type  mdf:   str
        :type  base:  str
        :type  data:  str

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        gxapi_cy.WrapMVU._mdf(GXContext._get_tls_geo(), map, mdf.encode(), base.encode(), data.encode())
        



    @classmethod
    def path_plot(cls, mview, vv_x, vv_y, line, locate, vangle, up, loff, voff, gap):
        """
        Draw a flight line
        
        :param mview:   View
        :param vv_x:    X
        :param vv_y:    Y
        :param line:    Line label
        :param locate:  :ref:`MVU_FLIGHT_LOCATE`
        :param vangle:  Lines steeper than this angle are considered vertical and the up label direction is used.
        :param up:      Up label direction:   1 up is right -1 up is left
        :param loff:    Along line label offset in mm.
        :param voff:    Perpendicular label offset mm.
        :param gap:     Maximum gap before breaking line, 0.0 for no breaks.
        :type  mview:   GXMVIEW
        :type  vv_x:    GXVV
        :type  vv_y:    GXVV
        :type  line:    str
        :type  locate:  int
        :type  vangle:  float
        :type  up:      int
        :type  loff:    float
        :type  voff:    float
        :type  gap:     float

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** See `flight_plot <geosoft.gxapi.GXMVU.flight_plot>`.  This is the same except for the
        additional line gap parameter.

        .. seealso::

            `flight_plot <geosoft.gxapi.GXMVU.flight_plot>`
        """
        gxapi_cy.WrapMVU._path_plot(GXContext._get_tls_geo(), mview, vv_x, vv_y, line.encode(), locate, vangle, up, loff, voff, gap)
        



    @classmethod
    def path_plot_ex(cls, mview, vv_x, vv_y, line, locate, compass, vangle, up, loff, voff, gap):
        """
        Draw a flight line
        
        :param mview:    View
        :param vv_x:     X
        :param vv_y:     Y
        :param line:     Line label
        :param locate:   :ref:`MVU_FLIGHT_LOCATE`
        :param compass:  :ref:`MVU_FLIGHT_COMPASS`
        :param vangle:   Lines steeper than this angle are considered vertical and the up label direction is used.
        :param up:       Up label direction:   1 up is right -1 up is left
        :param loff:     Along line label offset in mm.
        :param voff:     Perpendicular label offset mm.
        :param gap:      Maximum gap before breaking line, 0.0 for no breaks.
        :type  mview:    GXMVIEW
        :type  vv_x:     GXVV
        :type  vv_y:     GXVV
        :type  line:     str
        :type  locate:   int
        :type  compass:  int
        :type  vangle:   float
        :type  up:       int
        :type  loff:     float
        :type  voff:     float
        :type  gap:      float

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** This is the same except for the additional line compass parameter.

        .. seealso::

            `path_plot <geosoft.gxapi.GXMVU.path_plot>`
        """
        gxapi_cy.WrapMVU._path_plot_ex(GXContext._get_tls_geo(), mview, vv_x, vv_y, line.encode(), locate, compass, vangle, up, loff, voff, gap)
        



    @classmethod
    def path_plot_ex2(cls, mview, vv_x, vv_y, line, locate, compass, vangle, up, loff, voff, gap, dummies):
        """
        Draw a flight line
        
        :param mview:    View
        :param vv_x:     X
        :param vv_y:     Y
        :param line:     Line label
        :param locate:   :ref:`MVU_FLIGHT_LOCATE`
        :param compass:  :ref:`MVU_FLIGHT_COMPASS`
        :param vangle:   Lines steeper than this angle are considered vertical and the up label direction is used.
        :param up:       Up label direction:   1 up is right -1 up is left
        :param loff:     Along line label offset in mm.
        :param voff:     Perpendicular label offset mm.
        :param gap:      Maximum gap before breaking line, 0.0 for no breaks.
        :param dummies:  :ref:`MVU_FLIGHT_DUMMIES`
        :type  mview:    GXMVIEW
        :type  vv_x:     GXVV
        :type  vv_y:     GXVV
        :type  line:     str
        :type  locate:   int
        :type  compass:  int
        :type  vangle:   float
        :type  up:       int
        :type  loff:     float
        :type  voff:     float
        :type  gap:      float
        :type  dummies:  int

        .. versionadded:: 5.0.8

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** This is the same except for the additional line dummies parameter.

        .. seealso::

            `path_plot_ex <geosoft.gxapi.GXMVU.path_plot_ex>`
        """
        gxapi_cy.WrapMVU._path_plot_ex2(GXContext._get_tls_geo(), mview, vv_x, vv_y, line.encode(), locate, compass, vangle, up, loff, voff, gap, dummies)
        



    @classmethod
    def plot_voxel_surface(cls, mview, vox, value, col, line_thick):
        """
        Extract an iso-surface from a voxel and plot it to a 2D or 3D view.
        
        :param mview:       View
        :param vox:         Voxel model
        :param value:       Iso-surface value
        :param col:         Drawing color
        :param line_thick:  Line thickness for line drawing, and 2D views.
        :type  mview:       GXMVIEW
        :type  vox:         GXVOX
        :type  value:       float
        :type  col:         int
        :type  line_thick:  float

        .. versionadded:: 6.4

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** The Marching Cubes method of Lorensen and Cline, Computer Graphics, V21,
        Number 4, July 1987, is used to calculate a given iso-surface in a voxel
        model. The resulting surface is plotted to a 2D or 3D view. If the view
        is 2-D, then only the intersection of the surface with the 2D surface is
        plotted, using lines.
        """
        gxapi_cy.WrapMVU._plot_voxel_surface(GXContext._get_tls_geo(), mview, vox, value, col, line_thick)
        



    @classmethod
    def plot_voxel_surface2(cls, mview, vox, value, col, line_thick, transparency, surface_name):
        """
        Extract an iso-surface from a voxel and plot it to a 2D or 3D view.
        
        :param mview:         View
        :param vox:           Voxel model
        :param value:         Iso-surface value
        :param col:           Drawing color
        :param line_thick:    Line thickness for line drawing, and 2D views.
        :param transparency:  Transparency (0 - transparent, 1 - opaque).
        :param surface_name:  Iso-surface name
        :type  mview:         GXMVIEW
        :type  vox:           GXVOX
        :type  value:         float
        :type  col:           int
        :type  line_thick:    float
        :type  transparency:  float
        :type  surface_name:  str

        .. versionadded:: 7.3

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** The Marching Cubes method of Lorensen and Cline, Computer Graphics, V21,
        Number 4, July 1987, is used to calculate a given iso-surface in a voxel
        model. The resulting surface is plotted to a 2D or 3D view. If the view
        is 2-D, then only the intersection of the surface with the 2D surface is
        plotted, using lines.
        """
        gxapi_cy.WrapMVU._plot_voxel_surface2(GXContext._get_tls_geo(), mview, vox, value, col, line_thick, transparency, surface_name.encode())
        



    @classmethod
    def generate_surface_from_voxel(cls, mview, vox, method, option, min_value, max_value, col, line_thick, transparency, surface_name):
        """
        TODO...
        
        :param mview:         View
        :param vox:           Voxel model
        :param method:        :ref:`MVU_VOX_SURFACE_METHOD`
        :param option:        :ref:`MVU_VOX_SURFACE_OPTION`
        :param min_value:     Iso-surface value
        :param max_value:     For closed surfaces: close between the selected value and this value (set equal to the Iso-surface to close within nearest values below, DUMMY to close within nearest value above)
        :param col:           Drawing color
        :param line_thick:    Line thickness for line drawing, and 2D views.
        :param transparency:  Transparency (0 - transparent, 1 - opaque).
        :param surface_name:  Geosurface file
        :type  mview:         GXMVIEW
        :type  vox:           GXVOX
        :type  method:        int
        :type  option:        int
        :type  min_value:     float
        :type  max_value:     float
        :type  col:           int
        :type  line_thick:    float
        :type  transparency:  float
        :type  surface_name:  str

        .. versionadded:: 8.5

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** TODO... Move to `GXVOX <geosoft.gxapi.GXVOX>` method for surface generation only and use GeosurfaceD to display.
        """
        gxapi_cy.WrapMVU._generate_surface_from_voxel(GXContext._get_tls_geo(), mview, vox, method, option, min_value, max_value, col, line_thick, transparency, surface_name.encode())
        



    @classmethod
    def post(cls, mview, vv_x, vv_y, vv_z, dummy, size, format, decimals, ref, angle):
        """
        Post values on a map.
        
        :param mview:     View
        :param vv_x:      X locations
        :param vv_y:      Y locations
        :param vv_z:      Values to post
        :param dummy:     Do not plot dummy values?
        :param size:      Numb Size
        :param format:    Format
        :param decimals:  Decimals
        :param ref:       Reference point number
        :param angle:     Text angle
        :type  mview:     GXMVIEW
        :type  vv_x:      GXVV
        :type  vv_y:      GXVV
        :type  vv_z:      GXVV
        :type  dummy:     bool
        :type  size:      int
        :type  format:    int
        :type  decimals:  int
        :type  ref:       int
        :type  angle:     float

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        gxapi_cy.WrapMVU._post(GXContext._get_tls_geo(), mview, vv_x, vv_y, vv_z, dummy, size, format, decimals, ref, angle)
        



    @classmethod
    def post_ex(cls, mview, vv_x, vv_y, vv_z, vv_s, dummy, base, min_detect, size, format, decimals, offset_l, offset_p, alternate, mod, ref, angle, fixed, ref_ang, up):
        """
        Post values on a map with more paramters.
        
        :param mview:       View
        :param vv_x:        X locations
        :param vv_y:        Y locations
        :param vv_z:        Values to post
        :param vv_s:        Station
        :param dummy:       Do not plot dummy values?
        :param base:        Base to remove, default is 0.0
        :param min_detect:  Detection limit, can be `GS_R8DM <geosoft.gxapi.GS_R8DM>`
        :param size:        Numb Size
        :param format:      Format
        :param decimals:    Decimals
        :param offset_l:    Offset along line (right and above are positive)
        :param offset_p:    Offset perpendicular to line
        :param alternate:   TRUE - Positive above, Negative below FALSE - All above.
        :param mod:         Modulas on station vv
        :param ref:         Reference point number
        :param angle:       Text angle (degree, CCW from down-line)
        :param fixed:       Fixed angle ?
        :param ref_ang:     Vertical reference angle
        :param up:          1 up is right, -1 up is left
        :type  mview:       GXMVIEW
        :type  vv_x:        GXVV
        :type  vv_y:        GXVV
        :type  vv_z:        GXVV
        :type  vv_s:        GXVV
        :type  dummy:       bool
        :type  base:        float
        :type  min_detect:  float
        :type  size:        int
        :type  format:      int
        :type  decimals:    int
        :type  offset_l:    float
        :type  offset_p:    float
        :type  alternate:   int
        :type  mod:         float
        :type  ref:         int
        :type  angle:       float
        :type  fixed:       int
        :type  ref_ang:     float
        :type  up:          int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        gxapi_cy.WrapMVU._post_ex(GXContext._get_tls_geo(), mview, vv_x, vv_y, vv_z, vv_s, dummy, base, min_detect, size, format, decimals, offset_l, offset_p, alternate, mod, ref, angle, fixed, ref_ang, up)
        



    @classmethod
    def probability(cls, mview, st_data, st_hist, title, unit, transform, lmd, xm, ym, widthm, heightm, symb_size, sigma, sum_width, summ, data_decimal, stat_decimal, itr):
        """
        Plot a probability plot on a map.
        
        :param mview:         View
        :param st_data:       `GXST <geosoft.gxapi.GXST>` with summary stats of original data
        :param st_hist:       `GXST <geosoft.gxapi.GXST>` with histogram info of original or log10 data
        :param title:         Title
        :param unit:          Unit
        :param transform:     Transform type (0: Raw, 1: Log, 2: Lambda)
        :param lmd:           Lambda Value for lambda transform
        :param xm:            X in mm (bottom left corner of histogram box)
        :param ym:            Y in mm (bottom left corner of histogram box)
        :param widthm:        Box width in mm
        :param heightm:       Box height in mm
        :param symb_size:     Symbol size in mm
        :param sigma:         Sigma (X range is -sigma to sigma)
        :param sum_width:     Width (mm) of the additional box for summary stats
        :param summ:          Summary stats: 0 - do not draw, 1 - draw
        :param data_decimal:  Decimals for data, negative for sig. fig.
        :param stat_decimal:  Decimals for stats, negative for sig. fig.
        :param itr:           `GXITR <geosoft.gxapi.GXITR>` to color symbols.
        :type  mview:         GXMVIEW
        :type  st_data:       GXST
        :type  st_hist:       GXST
        :type  title:         str
        :type  unit:          str
        :type  transform:     int
        :type  lmd:           float
        :type  xm:            float
        :type  ym:            float
        :type  widthm:        float
        :type  heightm:       float
        :type  symb_size:     float
        :type  sigma:         float
        :type  sum_width:     float
        :type  summ:          int
        :type  data_decimal:  int
        :type  stat_decimal:  int
        :type  itr:           GXITR

        .. versionadded:: 5.1.8

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** The `GXITR <geosoft.gxapi.GXITR>` can be empty (but must still be a valid `GXITR <geosoft.gxapi.GXITR>` object).
        """
        gxapi_cy.WrapMVU._probability(GXContext._get_tls_geo(), mview, st_data, st_hist, title.encode(), unit.encode(), transform, lmd, xm, ym, widthm, heightm, symb_size, sigma, sum_width, summ, data_decimal, stat_decimal, itr)
        



    @classmethod
    def profile_plot(cls, mview, vv_x, vv_y, vv_z, vangle, up, gap, base, scale, join):
        """
        Draw a profile along line trace
        
        :param mview:   View
        :param vv_x:    X
        :param vv_y:    Y
        :param vv_z:    Z
        :param vangle:  Lines steeper than this angle are considered vertical and the up label direction is used.
        :param up:      Up label direction:   1 up is right -1 up is left
        :param gap:     Maximum gap in data to span (view units)
        :param base:    Z profile base, `rDUMMY <geosoft.gxapi.rDUMMY>` to use data minimum
        :param scale:   Z scale in view units/Z unit
        :param join:    1 to join profile to line ends.
        :type  mview:   GXMVIEW
        :type  vv_x:    GXVV
        :type  vv_y:    GXVV
        :type  vv_z:    GXVV
        :type  vangle:  float
        :type  up:      int
        :type  gap:     float
        :type  base:    float
        :type  scale:   float
        :type  join:    int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Profiles will be drawn in the current line style.
        """
        gxapi_cy.WrapMVU._profile_plot(GXContext._get_tls_geo(), mview, vv_x, vv_y, vv_z, vangle, up, gap, base, scale, join)
        



    @classmethod
    def profile_plot_ex(cls, mview, vv_x, vv_y, vv_z, vangle, up, gap, base, scale, join, log, log_base, smooth, pos_f_color, neg_f_color):
        """
        Draw a profile along line trace with more parameters
        
        :param mview:        View
        :param vv_x:         X
        :param vv_y:         Y
        :param vv_z:         Z
        :param vangle:       Lines steeper than this angle are considered vertical and the up label direction is used.
        :param up:           Up label direction:   1 up is right -1 up is left
        :param gap:          Maximum gap in data to span (view units)
        :param base:         Z profile base, `rDUMMY <geosoft.gxapi.rDUMMY>` to use data minimum
        :param scale:        Z scale in view units/Z unit
        :param join:         1 to join profile to line ends.
        :param log:          Log option: 0 linear (default), 1 logarithm, 2 log/linear
        :param log_base:     Log base
        :param smooth:       Smooth curve option: 0 no (default), 1 yes
        :param pos_f_color:  Positive fill color
        :param neg_f_color:  Negative fill color
        :type  mview:        GXMVIEW
        :type  vv_x:         GXVV
        :type  vv_y:         GXVV
        :type  vv_z:         GXVV
        :type  vangle:       float
        :type  up:           int
        :type  gap:          float
        :type  base:         float
        :type  scale:        float
        :type  join:         int
        :type  log:          int
        :type  log_base:     float
        :type  smooth:       int
        :type  pos_f_color:  str
        :type  neg_f_color:  str

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Profiles will be drawn in the current line style.
        """
        gxapi_cy.WrapMVU._profile_plot_ex(GXContext._get_tls_geo(), mview, vv_x, vv_y, vv_z, vangle, up, gap, base, scale, join, log, log_base, smooth, pos_f_color.encode(), neg_f_color.encode())
        



    @classmethod
    def prop_symb_legend(cls, mview, x1, y1, font_size, symb_scale, base, n_symb, start, increment, title, sub_title):
        """
        Draw a legend for proportional symbols.
        
        :param mview:       `GXMVIEW <geosoft.gxapi.GXMVIEW>` object
        :param x1:          Plot origin X
        :param y1:          Plot origin Y
        :param font_size:   Label Font size (mm)
        :param symb_scale:  Symbol scale factor (data value/mm)
        :param base:        Base value to remove before scaling
        :param n_symb:      Number of symbols
        :param start:       Starting symbol data value (>= Base value)
        :param increment:   Data value increment (>0.0)
        :param title:       Plot title
        :param sub_title:   Plot subtitle
        :type  mview:       GXMVIEW
        :type  x1:          float
        :type  y1:          float
        :type  font_size:   float
        :type  symb_scale:  float
        :type  base:        float
        :type  n_symb:      int
        :type  start:       float
        :type  increment:   float
        :type  title:       str
        :type  sub_title:   str

        .. versionadded:: 5.0.8

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** All symbol attributes, except for the size, are assumed
        to be defined (or defaults are used).
        Spacing is based on the maximum of the largest plotted symbol
        and the font size.
        """
        gxapi_cy.WrapMVU._prop_symb_legend(GXContext._get_tls_geo(), mview, x1, y1, font_size, symb_scale, base, n_symb, start, increment, title.encode(), sub_title.encode())
        



    @classmethod
    def re_gen_areas(cls, mview, lines):
        """
        Re-Generate from a line group and existing area group
        
        :param mview:  View
        :param lines:  Group with lines
        :type  mview:  GXMVIEW
        :type  lines:  str

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** The area group must exist and will be modified to match the current
        line group.

        All non-polygon entities in the current area group will remain in the
        new area group.  All existing polygon groups will be used to determine
        the most likely attributes for the new polygon groups.

        There must be existing polygon groups in the area group.

        .. seealso::

            `gen_areas <geosoft.gxapi.GXMVU.gen_areas>`
        """
        gxapi_cy.WrapMVU._re_gen_areas(GXContext._get_tls_geo(), mview, lines.encode())
        



    @classmethod
    def symb_off(cls, mview, vv_x, vv_y, vv_f, x_off, y_off):
        """
        Draws symbols with an offset and against a flag channel
        
        :param mview:  View
        :param vv_x:   X, must be type of REAL
        :param vv_y:   Y, must be type of REAL
        :param vv_f:   Flag `GXVV <geosoft.gxapi.GXVV>`, must be type of INT
        :param x_off:  X Offset
        :param y_off:  Y Offset
        :type  mview:  GXMVIEW
        :type  vv_x:   GXVV
        :type  vv_y:   GXVV
        :type  vv_f:   GXVV
        :type  x_off:  float
        :type  y_off:  float

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Symbols are not plotted for positions where the flag `GXVV <geosoft.gxapi.GXVV>`
        value is 0 or `iDUMMY <geosoft.gxapi.iDUMMY>`.
        """
        gxapi_cy.WrapMVU._symb_off(GXContext._get_tls_geo(), mview, vv_x, vv_y, vv_f, x_off, y_off)
        



    @classmethod
    def text_box(cls, mview, xmin, ymin, xmax, ymax, text, space, type):
        """
        Draw a wrapped text box
        
        :param mview:  View
        :param xmin:   Min X
        :param ymin:   Min Y
        :param xmax:   Max X
        :param ymax:   Max Y
        :param text:   Text
        :param space:  Line spacing (1.2 good)
        :param type:   :ref:`MVU_TEXTBOX`
        :type  mview:  GXMVIEW
        :type  xmin:   float
        :type  ymin:   float
        :type  xmax:   float
        :type  ymax:   float
        :type  text:   str
        :type  space:  float
        :type  type:   int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        gxapi_cy.WrapMVU._text_box(GXContext._get_tls_geo(), mview, xmin, ymin, xmax, ymax, text.encode(), space, type)
        



    @classmethod
    def tick(cls, mview, vv_x, vv_y, vv_s, size, mod, mt_size, mt_mod):
        """
        Draw line ticks on a map.
        
        :param mview:    View
        :param vv_x:     X locations
        :param vv_y:     Y locations
        :param vv_s:     Station
        :param size:     Tick size
        :param mod:      Tick modulus on station vv
        :param mt_size:  Major tick size
        :param mt_mod:   Major tick modulus on station vv
        :type  mview:    GXMVIEW
        :type  vv_x:     GXVV
        :type  vv_y:     GXVV
        :type  vv_s:     GXVV
        :type  size:     float
        :type  mod:      float
        :type  mt_size:  float
        :type  mt_mod:   float

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        gxapi_cy.WrapMVU._tick(GXContext._get_tls_geo(), mview, vv_x, vv_y, vv_s, size, mod, mt_size, mt_mod)
        



    @classmethod
    def tick_ex(cls, mview, vv_x, vv_y, vv_s, size, mod, mt_size, mt_mod, gap):
        """
        Same as `tick <geosoft.gxapi.GXMVU.tick>`, with gap allowance.
        
        :param mview:    View
        :param vv_x:     X locations
        :param vv_y:     Y locations
        :param vv_s:     Station
        :param size:     Tick size
        :param mod:      Tick modulus on station vv
        :param mt_size:  Major tick size
        :param mt_mod:   Major tick modulus on station vv
        :param gap:      Maximum gap to span; set to 0 or `rDUMMY <geosoft.gxapi.rDUMMY>` to ignore all gaps.
        :type  mview:    GXMVIEW
        :type  vv_x:     GXVV
        :type  vv_y:     GXVV
        :type  vv_s:     GXVV
        :type  size:     float
        :type  mod:      float
        :type  mt_size:  float
        :type  mt_mod:   float
        :type  gap:      float

        .. versionadded:: 6.3

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        gxapi_cy.WrapMVU._tick_ex(GXContext._get_tls_geo(), mview, vv_x, vv_y, vv_s, size, mod, mt_size, mt_mod, gap)
        



    @classmethod
    def trnd_path(cls, mview, vv_x, vv_y, min_sect, min_dist):
        """
        Plot min and max trend lines.
        
        :param mview:     View
        :param vv_x:      X
        :param vv_y:      Y
        :param min_sect:  Minimum number of sections
        :param min_dist:  Minimum length of sections
        :type  mview:     GXMVIEW
        :type  vv_x:      GXVV
        :type  vv_y:      GXVV
        :type  min_sect:  int
        :type  min_dist:  float

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Trend lines positions consist of X and Y VVs
        interspersed with dummies, which separate the
        individual trend sections.
        Set the minimum number of sections to > 0 to
        plot only the longer trend lines.
        (The number of sections in one trend section is
        equal to the number of points between dummies minus one.)
        Set the minimum distance to > 0 to
        plot only the longer trend lines.
        """
        gxapi_cy.WrapMVU._trnd_path(GXContext._get_tls_geo(), mview, vv_x, vv_y, min_sect, min_dist)
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer