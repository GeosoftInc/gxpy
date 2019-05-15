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
class GXSTK(gxapi_cy.WrapSTK):
    """
    GXSTK class.

    The `GXSTK <geosoft.gxapi.GXSTK>` class is used for plotting a single data profile in
    an `GXMVIEW <geosoft.gxapi.GXMVIEW>`. The `GXMSTK <geosoft.gxapi.GXMSTK>` class (see `GXMSTK <geosoft.gxapi.GXMSTK>`) is used to plot
    multiple `GXSTK <geosoft.gxapi.GXSTK>` objects to a single map.

    Use `GXMSTK.add_stk <geosoft.gxapi.GXMSTK.add_stk>` fuction to create a `GXSTK <geosoft.gxapi.GXSTK>` object before
    using functions in this file

    SEE `GXMSTK <geosoft.gxapi.GXMSTK>` FILE FOR DETAILED DESCRIPTIONS OF ALL FUNCTION PARAMETERS.
    """

    def __init__(self, handle=0):
        super(GXSTK, self).__init__(GXContext._get_tls_geo(), handle)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of `GXSTK <geosoft.gxapi.GXSTK>`
        
        :returns: A null `GXSTK <geosoft.gxapi.GXSTK>`
        :rtype:   GXSTK
        """
        return GXSTK()

    def is_null(self):
        """
        Check if this is a null (undefined) instance
        
        :returns: True if this is a null (undefined) instance, False otherwise.
        :rtype:   bool
        """
        return self._internal_handle() == 0



# Miscellaneous



    def get_trans_parms(self, x_trans_t, x_log_min, xvv_lev, xvv_cmp, y_trans_t, y_log_min, yvv_lev, yvv_cmp):
        """
        Get transformation parameters in `GXSTK <geosoft.gxapi.GXSTK>` object
        
        :param x_trans_t:  Type of transformation for horizontal axis
        :param x_log_min:  Minimum value to apply logarithmic
        :param xvv_lev:    Comma separated parameters defining linear compress data range
        :param xvv_cmp:    Comma separated parameters defining scaling factors for
        :param y_trans_t:  Type of scaling for vertical axis
        :param y_log_min:  Minimum value to apply logarithmic
        :param yvv_lev:    Comma separated parameters defining linear compress data range
        :param yvv_cmp:    Comma separated parameters defining scaling factors for
        :type  x_trans_t:  int_ref
        :type  x_log_min:  float_ref
        :type  xvv_lev:    GXVV
        :type  xvv_cmp:    GXVV
        :type  y_trans_t:  int_ref
        :type  y_log_min:  float_ref
        :type  yvv_lev:    GXVV
        :type  yvv_cmp:    GXVV

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** See above full description of each parameters
        `GXVV <geosoft.gxapi.GXVV>`'s for X channel transformation can be NULL if the
        transformation is log or loglinear. The same for Y channel.

        See `GXMSTK <geosoft.gxapi.GXMSTK>` for detailed description of all function parameters
        """
        x_trans_t.value, x_log_min.value, y_trans_t.value, y_log_min.value = self._get_trans_parms(x_trans_t.value, x_log_min.value, xvv_lev, xvv_cmp, y_trans_t.value, y_log_min.value, yvv_lev, yvv_cmp)
        




    def get_axis_format(self, xy):
        """
        Get axis number display format.
        
        :param xy:   :ref:`STK_AXIS`
        :type  xy:   int

        :returns:    The current format - :ref:`DB_CHAN_FORMAT`
        :rtype:      int

        .. versionadded:: 5.1.5

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** By default, `DB_CHAN_FORMAT_NORMAL <geosoft.gxapi.DB_CHAN_FORMAT_NORMAL>`
        """
        ret_val = self._get_axis_format(xy)
        return ret_val




    def get_axis_parms(self, bar_draw, min_loc, max_loc, thick, color, tick_interval, tick_size1, tick_size2, min_tick, xy):
        """
        Get parameters in `GXSTK <geosoft.gxapi.GXSTK>` object relating drawing X/Y axis
        
        :param bar_draw:       ?BARDRAW: Bottom and/or Top, or Left and/or Right
        :param min_loc:        Bottom Y/Left X location
        :param max_loc:        Top Y/Right X location
        :param thick:          ?BARLINETHICK  - Line thickness in mm. Default is 0.05
        :param color:          ?BARCOLOR      - Line color string in RGB model. Default is black
        :param tick_interval:  ?BARTICKINTEERVAL
        :param tick_size1:     Major tick size in mm for bottom/left axis bar.
        :param tick_size2:     Major tick size in mm for top/right axis bar.
        :param min_tick:       ?BARMINORTICK  - Number of minor ticks. (0) none, (-1) automatic
        :param xy:             :ref:`STK_AXIS`
        :type  bar_draw:       int_ref
        :type  min_loc:        float_ref
        :type  max_loc:        float_ref
        :type  thick:          float_ref
        :type  color:          str_ref
        :type  tick_interval:  float_ref
        :type  tick_size1:     float_ref
        :type  tick_size2:     float_ref
        :type  min_tick:       int_ref
        :type  xy:             int

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** See `GXMSTK <geosoft.gxapi.GXMSTK>` for detailed description of all function parameters
        ? mark in the note represent either X and Y
        """
        bar_draw.value, min_loc.value, max_loc.value, thick.value, color.value, tick_interval.value, tick_size1.value, tick_size2.value, min_tick.value = self._get_axis_parms(bar_draw.value, min_loc.value, max_loc.value, thick.value, color.value.encode(), tick_interval.value, tick_size1.value, tick_size2.value, min_tick.value, xy)
        




    def get_fid_parms(self, fid_y_loc, fid_tick_size, fid_interval, fid_text_font, fid_text_size, fid_text_color):
        """
        Get parameters in `GXSTK <geosoft.gxapi.GXSTK>` object relating drawing fid ticks
        
        :param fid_y_loc:       Y location in data unit to draw Fid ticks. Default is the bottom of the stack
        :param fid_tick_size:   Fid tick size in mm. Default is 2.0mm
        :param fid_interval:    Fid interval to draw ticks. Nice number is calculated by default
        :param fid_text_font:   Font to use to label fids. Default is use 'default' font set in Montaj
        :param fid_text_size:   Text size in mm to label fids. Default is 5mm
        :param fid_text_color:  Text color string in RGB model. Default is black
        :type  fid_y_loc:       float_ref
        :type  fid_tick_size:   float_ref
        :type  fid_interval:    float_ref
        :type  fid_text_font:   str_ref
        :type  fid_text_size:   float_ref
        :type  fid_text_color:  str_ref

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** See `GXMSTK <geosoft.gxapi.GXMSTK>` for detailed description of all function parameters
        """
        fid_y_loc.value, fid_tick_size.value, fid_interval.value, fid_text_font.value, fid_text_size.value, fid_text_color.value = self._get_fid_parms(fid_y_loc.value, fid_tick_size.value, fid_interval.value, fid_text_font.value.encode(), fid_text_size.value, fid_text_color.value.encode())
        




    def get_flag(self, part):
        """
        Get flag indicating part of `GXSTK <geosoft.gxapi.GXSTK>` object is to be drawn or not
        
        :param part:  :ref:`STK_FLAG`
        :type  part:  int

        :returns:     FALSE (0) if part of the object is not to be drawn
                      TRUE  (1) if part of the object is drawn
        :rtype:       int

        .. versionadded:: 6.0.1

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        ret_val = self._get_flag(part)
        return ret_val




    def get_gen_parms(self, x_ch, y_ch, grp_name, x_scale, y_scale, x_start, x_end, y_start, left, bottom, height):
        """
        Get general parameters in `GXSTK <geosoft.gxapi.GXSTK>` object
        
        :param x_ch:      X channel name, REQUIRED
        :param y_ch:      Y channel name, REQUIRED
        :param grp_name:  Group name
        :param x_scale:   X scale (map scale, units/metre), REQUIRED
        :param y_scale:   Y scale (plot scale, units/mm), REQUIRED
        :param x_start:   Minimum X value (data unit) to draw
        :param x_end:     Maximum X value (data unit) to draw
        :param y_start:   Minimum Y value (data unit) to draw
        :param left:      Minimum horizontal location in mm of the stack on the map
        :param bottom:    Minimum vertical location in mm on the map
        :param height:    Profile height in mm on the map, must be > 0.0
        :type  x_ch:      str_ref
        :type  y_ch:      str_ref
        :type  grp_name:  str_ref
        :type  x_scale:   float_ref
        :type  y_scale:   float_ref
        :type  x_start:   float_ref
        :type  x_end:     float_ref
        :type  y_start:   float_ref
        :type  left:      float_ref
        :type  bottom:    float_ref
        :type  height:    float_ref

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** See `GXMSTK <geosoft.gxapi.GXMSTK>` for detailed description of all function parameters
        """
        x_ch.value, y_ch.value, grp_name.value, x_scale.value, y_scale.value, x_start.value, x_end.value, y_start.value, left.value, bottom.value, height.value = self._get_gen_parms(x_ch.value.encode(), y_ch.value.encode(), grp_name.value.encode(), x_scale.value, y_scale.value, x_start.value, x_end.value, y_start.value, left.value, bottom.value, height.value)
        




    def get_grid_parms(self, grid, min_x, max_x, min_y, max_y, thick, cross, x_sep, y_sep, color, grid12):
        """
        Get background grid parameters in `GXSTK <geosoft.gxapi.GXSTK>` object
        
        :param grid:    Type of grid to draw:
        :param min_x:   Minimum X in ground unit to draw grid
        :param max_x:   Maximum X in ground unit to draw grid
        :param min_y:   Minimum Y in ground unit to draw grid
        :param max_y:   Maximum Y in ground unit to draw grid
        :param thick:   Line thickness in mm. Default is 0.01mm
        :param cross:   Cross size or separation between dots in mm.
        :param x_sep:   Separation between vertical grid lines.
        :param y_sep:   Separation between horizontal grid lines.
        :param color:   Grid line color string in RGB model. Default is black
        :param grid12:  :ref:`STK_GRID`
        :type  grid:    int_ref
        :type  min_x:   float_ref
        :type  max_x:   float_ref
        :type  min_y:   float_ref
        :type  max_y:   float_ref
        :type  thick:   float_ref
        :type  cross:   float_ref
        :type  x_sep:   float_ref
        :type  y_sep:   float_ref
        :type  color:   str_ref
        :type  grid12:  int

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** See `GXMSTK <geosoft.gxapi.GXMSTK>` for detailed description of all function parameters
        ? mark in the note represent either X and Y
        """
        grid.value, min_x.value, max_x.value, min_y.value, max_y.value, thick.value, cross.value, x_sep.value, y_sep.value, color.value = self._get_grid_parms(grid.value, min_x.value, max_x.value, min_y.value, max_y.value, thick.value, cross.value, x_sep.value, y_sep.value, color.value.encode(), grid12)
        




    def get_label_parms(self, axis, min_loc, min_orient, max_loc, max_orient, interval, font, text_size, color, bound, xy):
        """
        Get parameters in `GXSTK <geosoft.gxapi.GXSTK>` object relating X/Y axis labels
        
        :param axis:        Which axes to draw: Bottom/Top or Left/Right axes
        :param min_loc:     Bottom or Left axis label location
        :param min_orient:  Bottom or Left labels orientation.
        :param max_loc:     Top or Right axis label location
        :param max_orient:  Top or Right axis label orientation
        :param interval:    Label interval. Default is to use related axis tick interval
        :param font:        Font to use to label. Default is use 'default' font set in Montaj
        :param text_size:   Text size in mm to draw profile labels. Default is 5mm
        :param color:       Text color string in RGB model. Default is black
        :param bound:       ?LABELBOUND    - Edge bound.  0 - No
        :param xy:          :ref:`STK_AXIS`
        :type  axis:        int_ref
        :type  min_loc:     float_ref
        :type  min_orient:  int_ref
        :type  max_loc:     float_ref
        :type  max_orient:  int_ref
        :type  interval:    float_ref
        :type  font:        str_ref
        :type  text_size:   float_ref
        :type  color:       str_ref
        :type  bound:       int_ref
        :type  xy:          int

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** See `GXMSTK <geosoft.gxapi.GXMSTK>` for detailed description of all function parameters
        ? mark in the note represent either X and Y
        Sets the label format to GSF_NORMAL. To override this,
        use the `set_axis_format <geosoft.gxapi.GXSTK.set_axis_format>` function AFTER calling this.
        """
        axis.value, min_loc.value, min_orient.value, max_loc.value, max_orient.value, interval.value, font.value, text_size.value, color.value, bound.value = self._get_label_parms(axis.value, min_loc.value, min_orient.value, max_loc.value, max_orient.value, interval.value, font.value.encode(), text_size.value, color.value.encode(), bound.value, xy)
        




    def get_profile(self, prof_type, pitch, thick, ln_clr, wrap, clip, smooth, vv_ind, label, ref, font, text_size, text_clr, prof_va_num):
        """
        Get profile parameters in `GXSTK <geosoft.gxapi.GXSTK>` object
        
        :param prof_type:    Profile line type.    1 - solid (default)
        :param pitch:        Patterned line pitch in mm. Default is 10 mm
        :param thick:        Line thickness in mm. Default is 0.05mm
        :param ln_clr:       Color string in RGB model. Default is black
        :param wrap:         Wrap option
        :param clip:         Clip option
        :param smooth:       Plot smoothed polyline.
        :param vv_ind:       Only use for `GXVA <geosoft.gxapi.GXVA>` channels. NULL is acceptable which means all profiles in the `GXVA <geosoft.gxapi.GXVA>` are plotted. `GXVV <geosoft.gxapi.GXVV>` type of INT (integer)
        :param label:        Characters string to label profiles
        :param ref:          Reference location to draw label.
        :param font:         Font to use to draw profile labels. Default is use 'default' font set in Montaj
        :param text_size:    Text size in mm to draw profile labels. Default is 5mm
        :param text_clr:     Text color string in RGB model. Default is black
        :param prof_va_num:  Include `GXVA <geosoft.gxapi.GXVA>` column numbers as part of the profile label 0 - no, 1 - yes
        :type  prof_type:    int_ref
        :type  pitch:        float_ref
        :type  thick:        float_ref
        :type  ln_clr:       str_ref
        :type  wrap:         int_ref
        :type  clip:         int_ref
        :type  smooth:       int_ref
        :type  vv_ind:       GXVV
        :type  label:        str_ref
        :type  ref:          int_ref
        :type  font:         str_ref
        :type  text_size:    float_ref
        :type  text_clr:     str_ref
        :type  prof_va_num:  int_ref

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** See `GXMSTK <geosoft.gxapi.GXMSTK>` for detailed description of all function parameters
        """
        prof_type.value, pitch.value, thick.value, ln_clr.value, wrap.value, clip.value, smooth.value, label.value, ref.value, font.value, text_size.value, text_clr.value, prof_va_num.value = self._get_profile(prof_type.value, pitch.value, thick.value, ln_clr.value.encode(), wrap.value, clip.value, smooth.value, vv_ind, label.value.encode(), ref.value, font.value.encode(), text_size.value, text_clr.value.encode(), prof_va_num.value)
        




    def get_profile_ex(self, prof_type, pitch, thick, ln_clr, break_dum, wrap, clip, smooth, vv_ind, label, ref, font, text_size, text_clr, prof_va_num):
        """
        Get profile parameters in `GXSTK <geosoft.gxapi.GXSTK>` object (added Break on dummy option)
        
        :param prof_type:    Profile line type.    1 - solid (default)
        :param pitch:        Patterned line pitch in mm. Default is 10 mm
        :param thick:        Line thickness in mm. Default is 0.05mm
        :param ln_clr:       Color string in RGB model. Default is black
        :param break_dum:    Break on dummy option
        :param wrap:         Wrap option
        :param clip:         Clip option
        :param smooth:       Plot smoothed polyline.
        :param vv_ind:       Only use for `GXVA <geosoft.gxapi.GXVA>` channels. NULL is acceptable which means all profiles in the `GXVA <geosoft.gxapi.GXVA>` are plotted. `GXVV <geosoft.gxapi.GXVV>` type of INT (integer)
        :param label:        Characters string to label profiles
        :param ref:          Reference location to draw label.
        :param font:         Font to use to draw profile labels. Default is use 'default' font set in Montaj
        :param text_size:    Text size in mm to draw profile labels. Default is 5mm
        :param text_clr:     Text color string in RGB model. Default is black
        :param prof_va_num:  Include `GXVA <geosoft.gxapi.GXVA>` column numbers as part of the profile label 0 - no, 1 - yes
        :type  prof_type:    int_ref
        :type  pitch:        float_ref
        :type  thick:        float_ref
        :type  ln_clr:       str_ref
        :type  break_dum:    int_ref
        :type  wrap:         int_ref
        :type  clip:         int_ref
        :type  smooth:       int_ref
        :type  vv_ind:       GXVV
        :type  label:        str_ref
        :type  ref:          int_ref
        :type  font:         str_ref
        :type  text_size:    float_ref
        :type  text_clr:     str_ref
        :type  prof_va_num:  int_ref

        .. versionadded:: 5.0.3

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** See `GXMSTK <geosoft.gxapi.GXMSTK>` for detailed description of all function parameters
        """
        prof_type.value, pitch.value, thick.value, ln_clr.value, break_dum.value, wrap.value, clip.value, smooth.value, label.value, ref.value, font.value, text_size.value, text_clr.value, prof_va_num.value = self._get_profile_ex(prof_type.value, pitch.value, thick.value, ln_clr.value.encode(), break_dum.value, wrap.value, clip.value, smooth.value, vv_ind, label.value.encode(), ref.value, font.value.encode(), text_size.value, text_clr.value.encode(), prof_va_num.value)
        




    def get_symb_parms(self, symb_font, symb_size, line_clr, fill_clr, wrap, clip, symb_y_loc, no_levels, vv_level, vv_type, label, text_font, text_size, text_clr):
        """
        Get parameters in `GXSTK <geosoft.gxapi.GXSTK>` object relating drawing symbols
        
        :param symb_font:   Font to use to draw symbols. Default is use 'symbols.gfn' font
        :param symb_size:   Symbol size in mm. Default is 5mm
        :param line_clr:    Edge color string in RGB model. Default is black
        :param fill_clr:    Fill color string in RGB model. Default is black
        :param wrap:        Wrap option
        :param clip:        Clip option
        :param symb_y_loc:  Y location to draw symbols. Default is to use the data from Y channel
        :param no_levels:   Number of levels to draw symbols
        :param vv_level:    Y values to define data ranges for each symbol types Type of REAL
        :param vv_type:     Symbol numbers (given in the symbol font) to draw, default is 20 TYPE of INT
        :param label:       Draw symbols ID (1) or not (0)
        :param text_font:   Font to use to draw symbol ID (A,B,C...). Default is use 'default'
        :param text_size:   Text size in mm to draw profile labels. Default is 5mm
        :param text_clr:    Text color string in RGB model. Default is black
        :type  symb_font:   str_ref
        :type  symb_size:   float_ref
        :type  line_clr:    str_ref
        :type  fill_clr:    str_ref
        :type  wrap:        int_ref
        :type  clip:        int_ref
        :type  symb_y_loc:  float_ref
        :type  no_levels:   int_ref
        :type  vv_level:    GXVV
        :type  vv_type:     GXVV
        :type  label:       int_ref
        :type  text_font:   str_ref
        :type  text_size:   float_ref
        :type  text_clr:    str_ref

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** See `GXMSTK <geosoft.gxapi.GXMSTK>` for detailed description of all function parameters
        """
        symb_font.value, symb_size.value, line_clr.value, fill_clr.value, wrap.value, clip.value, symb_y_loc.value, no_levels.value, label.value, text_font.value, text_size.value, text_clr.value = self._get_symb_parms(symb_font.value.encode(), symb_size.value, line_clr.value.encode(), fill_clr.value.encode(), wrap.value, clip.value, symb_y_loc.value, no_levels.value, vv_level, vv_type, label.value, text_font.value.encode(), text_size.value, text_clr.value.encode())
        




    def get_title_parms(self, title1, title2, title1_orient, title1_x, title1_y, title2_orient, title2_x, title2_y, font, text_size, color, xy):
        """
        Get parameters in `GXSTK <geosoft.gxapi.GXSTK>` object relating X/Y axis titles
        
        :param title1:         Title for bottom X axis/left Y axis. Default is no title.
        :param title2:         Title for top X axis/right Y axis. Default is no title.
        :param title1_orient:  Bottom/Left axis title orientation.
        :param title1_x:       X location to draw bottom/left axis title
        :param title1_y:       Y location to draw bottom/left axis title
        :param title2_orient:  Top/Right axis title orientation.
        :param title2_x:       X location to draw top/right axis title
        :param title2_y:       Y location to draw top/right axis title
        :param font:           Font to draw titles. Default is use 'default' font set in Montaj
        :param text_size:      Text size in mm to draw titles. Default is 5mm
        :param color:          Text color string in RGB model. Default is black
        :param xy:             :ref:`STK_AXIS`
        :type  title1:         str_ref
        :type  title2:         str_ref
        :type  title1_orient:  int_ref
        :type  title1_x:       float_ref
        :type  title1_y:       float_ref
        :type  title2_orient:  int_ref
        :type  title2_x:       float_ref
        :type  title2_y:       float_ref
        :type  font:           str_ref
        :type  text_size:      float_ref
        :type  color:          str_ref
        :type  xy:             int

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** See `GXMSTK <geosoft.gxapi.GXMSTK>` for detailed description of all function parameters
        ? mark in the note represent either X and Y
        """
        title1.value, title2.value, title1_orient.value, title1_x.value, title1_y.value, title2_orient.value, title2_x.value, title2_y.value, font.value, text_size.value, color.value = self._get_title_parms(title1.value.encode(), title2.value.encode(), title1_orient.value, title1_x.value, title1_y.value, title2_orient.value, title2_x.value, title2_y.value, font.value.encode(), text_size.value, color.value.encode(), xy)
        




    def set_flag(self, flag, part):
        """
        Set flag indicating part of `GXSTK <geosoft.gxapi.GXSTK>` object is to be drawn or not
        
        :param flag:  Flag to set (0 or 1)
        :param part:  :ref:`STK_FLAG`
        :type  flag:  int
        :type  part:  int

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        self._set_flag(flag, part)
        




    def set_array_colors(self, itr):
        """
        Set colors for individual channels in a `GXVA <geosoft.gxapi.GXVA>`, via an `GXITR <geosoft.gxapi.GXITR>`
        
        :param itr:  `GXITR <geosoft.gxapi.GXITR>` object for colors
        :type  itr:  GXITR

        .. versionadded:: 5.0.1

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** The `GXITR <geosoft.gxapi.GXITR>` is consulted by taking the channel index and dividing
        by the number of channels; hence the `GXITR <geosoft.gxapi.GXITR>` maximum values should
        be in the range: 0 > values >= 1.0.
        """
        self._set_array_colors(itr)
        




    def set_axis_format(self, format, xy):
        """
        Set axis number display format.
        
        :param format:  :ref:`DB_CHAN_FORMAT`
        :param xy:      :ref:`STK_AXIS`
        :type  format:  int
        :type  xy:      int

        .. versionadded:: 5.1.5

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** By default, `DB_CHAN_FORMAT_NORMAL <geosoft.gxapi.DB_CHAN_FORMAT_NORMAL>` is used to display the values,
        or for values > 1.e7, `DB_CHAN_FORMAT_EXP <geosoft.gxapi.DB_CHAN_FORMAT_EXP>`.
        """
        self._set_axis_format(format, xy)
        




    def set_axis_parms(self, bar_draw, min_loc, max_loc, thick, color, tick_interval, tick_size1, tick_size2, min_tick, xy):
        """
        Set parameters in `GXSTK <geosoft.gxapi.GXSTK>` object relating drawing X/Y axis
        
        :param bar_draw:       ?BARDRAW
        :param min_loc:        Bottom Y/Left X location
        :param max_loc:        Top Y/Right X location
        :param thick:          ?BARLINETHICK  - Line thickness in mm. Default is 0.05
        :param color:          ?BARCOLOR      - Line color string in RGB model. Default is black
        :param tick_interval:  ?BARTICKINTEERVAL
        :param tick_size1:     Major tick size in mm for bottom/left axis bar.
        :param tick_size2:     Major tick size in mm for top/right axis bar.
        :param min_tick:       ?BARMINORTICK  - Number of minor ticks. (0) none, (-1) automatic
        :param xy:             :ref:`STK_AXIS`
        :type  bar_draw:       int
        :type  min_loc:        float
        :type  max_loc:        float
        :type  thick:          float
        :type  color:          str
        :type  tick_interval:  float
        :type  tick_size1:     float
        :type  tick_size2:     float
        :type  min_tick:       int
        :type  xy:             int

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** See `GXMSTK <geosoft.gxapi.GXMSTK>` for detailed description of all function parameters
        ? mark in the note represent either X and Y
        """
        self._set_axis_parms(bar_draw, min_loc, max_loc, thick, color.encode(), tick_interval, tick_size1, tick_size2, min_tick, xy)
        




    def set_fid_parms(self, fid_y_loc, fid_tick_size, fid_interval, fid_text_font, fid_text_size, fid_text_color):
        """
        Set parameters in `GXSTK <geosoft.gxapi.GXSTK>` object relating drawing fid ticks
        
        :param fid_y_loc:       Y location in data unit to draw Fid ticks. Default is the bottom of the stack
        :param fid_tick_size:   Fid tick size in mm. Default is 2.0mm
        :param fid_interval:    Fid interval to draw ticks. Nice number is calculated by default
        :param fid_text_font:   Font to use to label fids. Default is use 'default' font set in Montaj
        :param fid_text_size:   Text size in mm to label fids. Default is 5mm
        :param fid_text_color:  Text color string in RGB model. Default is black
        :type  fid_y_loc:       float
        :type  fid_tick_size:   float
        :type  fid_interval:    float
        :type  fid_text_font:   str
        :type  fid_text_size:   float
        :type  fid_text_color:  str

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** See `GXMSTK <geosoft.gxapi.GXMSTK>` for detailed description of all function parameters
        """
        self._set_fid_parms(fid_y_loc, fid_tick_size, fid_interval, fid_text_font.encode(), fid_text_size, fid_text_color.encode())
        




    def set_gen_parms(self, x_ch, y_ch, grp_name, x_scale, y_scale, x_start, x_end, y_start, left, bottom, height):
        """
        Set general parameters in `GXSTK <geosoft.gxapi.GXSTK>` object
        
        :param x_ch:      X channel name, REQUIRED
        :param y_ch:      Y channel name, REQUIRED
        :param grp_name:  Group name
        :param x_scale:   X scale (map scale, units/metre), REQUIRED
        :param y_scale:   Y scale (plot scale, units/mm), REQUIRED
        :param x_start:   Minimum X value (data unit) to draw
        :param x_end:     Maximum X value (data unit) to draw
        :param y_start:   Minimum Y value (data unit) to draw
        :param left:      Minimum horizontal location in mm of the stack on the map
        :param bottom:    Minimum vertical location in mm on the map
        :param height:    Profile height in mm on the map, must be > 0.0
        :type  x_ch:      str
        :type  y_ch:      str
        :type  grp_name:  str
        :type  x_scale:   float
        :type  y_scale:   float
        :type  x_start:   float
        :type  x_end:     float
        :type  y_start:   float
        :type  left:      float
        :type  bottom:    float
        :type  height:    float

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** See `GXMSTK <geosoft.gxapi.GXMSTK>` for detailed description of all function parameters
        """
        self._set_gen_parms(x_ch.encode(), y_ch.encode(), grp_name.encode(), x_scale, y_scale, x_start, x_end, y_start, left, bottom, height)
        




    def set_grid_parms(self, grid, min_x, max_x, min_y, max_y, thick, cross, x_sep, y_sep, color, grid12):
        """
        Set background grid parameters in `GXSTK <geosoft.gxapi.GXSTK>` object
        
        :param grid:    Type of grid to draw:
        :param min_x:   Minimum X in ground unit to draw grid
        :param max_x:   Maximum X in ground unit to draw grid
        :param min_y:   Minimum Y in ground unit to draw grid
        :param max_y:   Maximum Y in ground unit to draw grid
        :param thick:   Line thickness in mm. Default is 0.01mm
        :param cross:   Cross size or separation between dots in mm.
        :param x_sep:   Separation between vertical grid lines.
        :param y_sep:   Separation between horizontal grid lines.
        :param color:   Grid line color string in RGB model. Default is black
        :param grid12:  :ref:`STK_GRID`
        :type  grid:    int
        :type  min_x:   float
        :type  max_x:   float
        :type  min_y:   float
        :type  max_y:   float
        :type  thick:   float
        :type  cross:   float
        :type  x_sep:   float
        :type  y_sep:   float
        :type  color:   str
        :type  grid12:  int

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** See `GXMSTK <geosoft.gxapi.GXMSTK>` for detailed description of all function parameters
        ? mark in the note represent either X and Y
        """
        self._set_grid_parms(grid, min_x, max_x, min_y, max_y, thick, cross, x_sep, y_sep, color.encode(), grid12)
        




    def set_label_parms(self, axis, min_loc, min_orient, max_loc, max_orient, interval, font, text_size, color, bound, xy):
        """
        Set parameters in `GXSTK <geosoft.gxapi.GXSTK>` object relating X/Y axis labels
        
        :param axis:        Bottom/Top or Left/Right axes
        :param min_loc:     Bottom or Left axis label location
        :param min_orient:  Bottom or Left labels orientation.
        :param max_loc:     Top or Right axis label location
        :param max_orient:  Top or Right axis label orientation
        :param interval:    Label interval. Default is to use related axis tick interval
        :param font:        Font to use to label. Default is use 'default' font set in Montaj
        :param text_size:   Text size in mm to draw profile labels. Default is 5mm
        :param color:       Text color string in RGB model. Default is black
        :param bound:       ?LABELBOUND    - Edge bound.  0 - No
        :param xy:          :ref:`STK_AXIS`
        :type  axis:        int
        :type  min_loc:     float
        :type  min_orient:  int
        :type  max_loc:     float
        :type  max_orient:  int
        :type  interval:    float
        :type  font:        str
        :type  text_size:   float
        :type  color:       str
        :type  bound:       int
        :type  xy:          int

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** See `GXMSTK <geosoft.gxapi.GXMSTK>` for detailed description of all function parameters
        ? mark in the note represent either X and Y
        Sets the label format to GSF_NORMAL. To override this,
        use the `set_axis_format <geosoft.gxapi.GXSTK.set_axis_format>` function AFTER calling this.
        """
        self._set_label_parms(axis, min_loc, min_orient, max_loc, max_orient, interval, font.encode(), text_size, color.encode(), bound, xy)
        




    def set_line_parm(self, line):
        """
        Set line parameter (of Y Chan) in `GXSTK <geosoft.gxapi.GXSTK>` object
        
        :param line:  Line symb
        :type  line:  int

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** See `GXMSTK <geosoft.gxapi.GXMSTK>` for detailed description of all function parameters
        """
        self._set_line_parm(line)
        




    def set_profile(self, prof_type, pitch, thick, ln_clr, wrap, clip, smooth, vv_ind, label, ref, font, text_size, text_clr, prof_va_num):
        """
        Set profile parameters in `GXSTK <geosoft.gxapi.GXSTK>` object
        
        :param prof_type:    Profile line type.    1 - solid (default)
        :param pitch:        Patterned line pitch in mm. Default is 10 mm
        :param thick:        Line thickness in mm. Default is 0.05mm
        :param ln_clr:       Color string in RGB model. Default is black
        :param wrap:         Wrap option
        :param clip:         Clip option
        :param smooth:       Plot smoothed polyline.
        :param vv_ind:       Integers starting from 0 indicating windows in `GXVA <geosoft.gxapi.GXVA>` channel to draw `GXVV <geosoft.gxapi.GXVV>` type of INT (integer)
        :param label:        Characters string to label profiles
        :param ref:          Reference location to draw label.
        :param font:         Font to use to draw profile labels. Default is use 'default' font set in Montaj
        :param text_size:    Text size in mm to draw profile labels. Default is 5mm
        :param text_clr:     Text color string in RGB model. Default is black
        :param prof_va_num:  Include `GXVA <geosoft.gxapi.GXVA>` column numbers as part of the profile label 0 - no, 1 - yes
        :type  prof_type:    int
        :type  pitch:        float
        :type  thick:        float
        :type  ln_clr:       str
        :type  wrap:         int
        :type  clip:         int
        :type  smooth:       int
        :type  vv_ind:       GXVV
        :type  label:        str
        :type  ref:          int
        :type  font:         str
        :type  text_size:    float
        :type  text_clr:     str
        :type  prof_va_num:  int

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** See `GXMSTK <geosoft.gxapi.GXMSTK>` for detailed description of all function parameters
        """
        self._set_profile(prof_type, pitch, thick, ln_clr.encode(), wrap, clip, smooth, vv_ind, label.encode(), ref, font.encode(), text_size, text_clr.encode(), prof_va_num)
        




    def set_profile_ex(self, prof_type, pitch, thick, ln_clr, break_dum, wrap, clip, smooth, vv_ind, label, ref, font, text_size, text_clr, prof_va_num):
        """
        Set profile parameters in `GXSTK <geosoft.gxapi.GXSTK>` object (added Break on dummy option)
        
        :param prof_type:    Profile line type.    1 - solid (default)
        :param pitch:        Patterned line pitch in mm. Default is 10 mm
        :param thick:        Line thickness in mm. Default is 0.05mm
        :param ln_clr:       Color string in RGB model. Default is black
        :param break_dum:    Break on dummy option
        :param wrap:         Wrap option
        :param clip:         Clip option
        :param smooth:       Plot smoothed polyline.
        :param vv_ind:       Integers starting from 0 indicating windows in `GXVA <geosoft.gxapi.GXVA>` channel to draw `GXVV <geosoft.gxapi.GXVV>` type of INT (integer)
        :param label:        Characters string to label profiles
        :param ref:          Reference location to draw label.
        :param font:         Font to use to draw profile labels. Default is use 'default' font set in Montaj
        :param text_size:    Text size in mm to draw profile labels. Default is 5mm
        :param text_clr:     Text color string in RGB model. Default is black
        :param prof_va_num:  Include `GXVA <geosoft.gxapi.GXVA>` column numbers as part of the profile label 0 - no, 1 - yes
        :type  prof_type:    int
        :type  pitch:        float
        :type  thick:        float
        :type  ln_clr:       str
        :type  break_dum:    int
        :type  wrap:         int
        :type  clip:         int
        :type  smooth:       int
        :type  vv_ind:       GXVV
        :type  label:        str
        :type  ref:          int
        :type  font:         str
        :type  text_size:    float
        :type  text_clr:     str
        :type  prof_va_num:  int

        .. versionadded:: 5.0.3

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** See `GXMSTK <geosoft.gxapi.GXMSTK>` for detailed description of all function parameters
        """
        self._set_profile_ex(prof_type, pitch, thick, ln_clr.encode(), break_dum, wrap, clip, smooth, vv_ind, label.encode(), ref, font.encode(), text_size, text_clr.encode(), prof_va_num)
        




    def set_symb_parms(self, symb_font, symb_size, line_clr, fill_clr, wrap, clip, symb_y_loc, no_levels, vv_level, vv_type, label, text_font, text_size, text_clr):
        """
        Set parameters in `GXSTK <geosoft.gxapi.GXSTK>` object relating drawing symbols
        
        :param symb_font:   Font to use to draw symbols. Default is use 'symbols.gfn' font
        :param symb_size:   Symbol size in mm. Default is 5mm
        :param line_clr:    Edge color string in RGB model. Default is black
        :param fill_clr:    Fill color string in RGB model. Default is black
        :param wrap:        Wrap option
        :param clip:        Clip option
        :param symb_y_loc:  Y location to draw symbols. Default is to use the data from Y channel
        :param no_levels:   Number of symbols levels
        :param vv_level:    Y values to define data ranges for each symbol types Type of REAL
        :param vv_type:     Symbol numbers (given in the symbol font) to draw Type of INT
        :param label:       Draw symbols ID (1) or not (0)
        :param text_font:   Font to use to draw symbol ID (A,B,C...). Default is use 'default'
        :param text_size:   Text size in mm to draw profile labels. Default is 5mm
        :param text_clr:    Text color string in RGB model. Default is black
        :type  symb_font:   str
        :type  symb_size:   float
        :type  line_clr:    str
        :type  fill_clr:    str
        :type  wrap:        int
        :type  clip:        int
        :type  symb_y_loc:  float
        :type  no_levels:   int
        :type  vv_level:    GXVV
        :type  vv_type:     GXVV
        :type  label:       int
        :type  text_font:   str
        :type  text_size:   float
        :type  text_clr:    str

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** See `GXMSTK <geosoft.gxapi.GXMSTK>` for detailed description of all function parameters
        """
        self._set_symb_parms(symb_font.encode(), symb_size, line_clr.encode(), fill_clr.encode(), wrap, clip, symb_y_loc, no_levels, vv_level, vv_type, label, text_font.encode(), text_size, text_clr.encode())
        




    def set_title_parms(self, title1, title2, title1_orient, title1_x, title1_y, title2_orient, title2_x, title2_y, font, text_size, color, xy):
        """
        Set parameters in `GXSTK <geosoft.gxapi.GXSTK>` object relating X/Y axis titles
        
        :param title1:         Title for bottom X axis/left Y axis. Default is no title.
        :param title2:         Title for top X axis/right Y axis. Default is no title.
        :param title1_orient:  Bottom/Left axis title orientation.
        :param title1_x:       X location to draw bottom/left axis title
        :param title1_y:       Y location to draw bottom/left axis title
        :param title2_orient:  Top/Right axis title orientation.
        :param title2_x:       X location to draw top/right axis title
        :param title2_y:       Y location to draw top/right axis title
        :param font:           Font to draw titles. Default is use 'default' font set in Montaj
        :param text_size:      Text size in mm to draw titles. Default is 5mm
        :param color:          Text color string in RGB model. Default is black
        :param xy:             :ref:`STK_AXIS`
        :type  title1:         str
        :type  title2:         str
        :type  title1_orient:  int
        :type  title1_x:       float
        :type  title1_y:       float
        :type  title2_orient:  int
        :type  title2_x:       float
        :type  title2_y:       float
        :type  font:           str
        :type  text_size:      float
        :type  color:          str
        :type  xy:             int

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** See `GXMSTK <geosoft.gxapi.GXMSTK>` for detailed description of all function parameters
        ? mark in the note represent either X and Y
        """
        self._set_title_parms(title1.encode(), title2.encode(), title1_orient, title1_x, title1_y, title2_orient, title2_x, title2_y, font.encode(), text_size, color.encode(), xy)
        




    def set_trans_parms(self, x_trans_t, x_log_min, xvv_lev, xvv_cmp, y_trans_t, y_log_min, yvv_lev, yvv_cmp):
        """
        Set transformation parameters in `GXSTK <geosoft.gxapi.GXSTK>` object
        
        :param x_trans_t:  Type of transformation for horizontal axis
        :param x_log_min:  Minimum value to apply logarithmic
        :param xvv_lev:    Future use
        :param xvv_cmp:    Future use
        :param y_trans_t:  Type of scaling for vertical axis
        :param y_log_min:  Minimum value to apply logarithmic
        :param yvv_lev:    Future use
        :param yvv_cmp:    Future use
        :type  x_trans_t:  int
        :type  x_log_min:  float
        :type  xvv_lev:    int
        :type  xvv_cmp:    int
        :type  y_trans_t:  int
        :type  y_log_min:  float
        :type  yvv_lev:    int
        :type  yvv_cmp:    int

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** See above full description of each parameters
        `GXVV <geosoft.gxapi.GXVV>`'s for X channel transformation can be NULL if the
        transformation is log or loglinear. The same for Y channel.
        See `GXMSTK <geosoft.gxapi.GXMSTK>` for detailed description of all function parameters
        """
        self._set_trans_parms(x_trans_t, x_log_min, xvv_lev, xvv_cmp, y_trans_t, y_log_min, yvv_lev, yvv_cmp)
        




    def set_va_index_start(self, index0):
        """
        Start array profile index labels at 0 or 1.
        
        :param index0:  Starting index (0 or 1)
        :type  index0:  int

        .. versionadded:: 6.0.1

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** By default, the index labels for array channel profiles
        begin at 0. Use this function to start them at either 0
        or 1.
        """
        self._set_va_index_start(index0)
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer