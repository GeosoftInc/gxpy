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
class GXSTK:
    """
    GXSTK class.

    The `GXSTK` class is used for plotting a single data profile in
    an `GXMVIEW`. The `GXMSTK` class (see `GXMSTK`) is used to plot
    multiple `GXSTK` objects to a single map.
    
    Use `GXMSTK.add_stk` fuction to create a `GXSTK` object before
    using functions in this file
    
    SEE `GXMSTK` FILE FOR DETAILED DESCRIPTIONS OF ALL FUNCTION PARAMETERS.
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._wrapper = None

    def __del__(self):
        self._wrapper = None

    def __init__(self, wrapper=None):
        self._wrapper = wrapper if wrapper else gxapi_cy.WrapSTK(GXContext._get_tls_geo(), 0)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of `GXSTK`
        
        :returns: A null `GXSTK`
        """
        return cls()

    def is_null(self):
        """
        Check if the instance of `GXSTK` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of `GXSTK`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Miscellaneous



    def get_trans_parms(self, x_trans_t, x_log_min, xvv_lev, xvv_cmp, y_trans_t, y_log_min, yvv_lev, yvv_cmp):
        """
        Get transformation parameters in `GXSTK` object

        **Note:**

        See above full description of each parameters
        `GXVV`'s for X channel transformation can be NULL if the
        transformation is log or loglinear. The same for Y channel.
        
        See `GXMSTK` for detailed description of all function parameters
        """
        x_trans_t.value, x_log_min.value, y_trans_t.value, y_log_min.value = self._wrapper.get_trans_parms(x_trans_t.value, x_log_min.value, xvv_lev._wrapper, xvv_cmp._wrapper, y_trans_t.value, y_log_min.value, yvv_lev._wrapper, yvv_cmp._wrapper)
        




    def get_axis_format(self, xy):
        """
        Get axis number display format.

        **Note:**

        By default, `DB_CHAN_FORMAT_NORMAL`
        """
        ret_val = self._wrapper.get_axis_format(xy)
        return ret_val




    def get_axis_parms(self, bar_draw, min_loc, max_loc, thick, color, tick_interval, tick_size1, tick_size2, min_tick, xy):
        """
        Get parameters in `GXSTK` object relating drawing X/Y axis

        **Note:**

        See `GXMSTK` for detailed description of all function parameters
        ? mark in the note represent either X and Y
        """
        bar_draw.value, min_loc.value, max_loc.value, thick.value, color.value, tick_interval.value, tick_size1.value, tick_size2.value, min_tick.value = self._wrapper.get_axis_parms(bar_draw.value, min_loc.value, max_loc.value, thick.value, color.value.encode(), tick_interval.value, tick_size1.value, tick_size2.value, min_tick.value, xy)
        




    def get_fid_parms(self, fid_y_loc, fid_tick_size, fid_interval, fid_text_font, fid_text_size, fid_text_color):
        """
        Get parameters in `GXSTK` object relating drawing fid ticks

        **Note:**

        See `GXMSTK` for detailed description of all function parameters
        """
        fid_y_loc.value, fid_tick_size.value, fid_interval.value, fid_text_font.value, fid_text_size.value, fid_text_color.value = self._wrapper.get_fid_parms(fid_y_loc.value, fid_tick_size.value, fid_interval.value, fid_text_font.value.encode(), fid_text_size.value, fid_text_color.value.encode())
        




    def get_flag(self, part):
        """
        Get flag indicating part of `GXSTK` object is to be drawn or not
        """
        ret_val = self._wrapper.get_flag(part)
        return ret_val




    def get_gen_parms(self, x_ch, y_ch, grp_name, x_scale, p9, p10, p11, p12, p13, p14, p15):
        """
        Get general parameters in `GXSTK` object

        **Note:**

        See `GXMSTK` for detailed description of all function parameters
        """
        x_ch.value, y_ch.value, grp_name.value, x_scale.value, p9.value, p10.value, p11.value, p12.value, p13.value, p14.value, p15.value = self._wrapper.get_gen_parms(x_ch.value.encode(), y_ch.value.encode(), grp_name.value.encode(), x_scale.value, p9.value, p10.value, p11.value, p12.value, p13.value, p14.value, p15.value)
        




    def get_grid_parms(self, grid, min_x, max_x, min_y, max_y, thick, cross, x_sep, y_sep, color, grid12):
        """
        Get background grid parameters in `GXSTK` object

        **Note:**

        See `GXMSTK` for detailed description of all function parameters
        ? mark in the note represent either X and Y
        """
        grid.value, min_x.value, max_x.value, min_y.value, max_y.value, thick.value, cross.value, x_sep.value, y_sep.value, color.value = self._wrapper.get_grid_parms(grid.value, min_x.value, max_x.value, min_y.value, max_y.value, thick.value, cross.value, x_sep.value, y_sep.value, color.value.encode(), grid12)
        




    def get_label_parms(self, axis, min_loc, min_orient, max_loc, max_orient, interval, font, text_size, color, bound, xy):
        """
        Get parameters in `GXSTK` object relating X/Y axis labels

        **Note:**

        See `GXMSTK` for detailed description of all function parameters
        ? mark in the note represent either X and Y
        Sets the label format to GSF_NORMAL. To override this,
        use the `set_axis_format` function AFTER calling this.
        """
        axis.value, min_loc.value, min_orient.value, max_loc.value, max_orient.value, interval.value, font.value, text_size.value, color.value, bound.value = self._wrapper.get_label_parms(axis.value, min_loc.value, min_orient.value, max_loc.value, max_orient.value, interval.value, font.value.encode(), text_size.value, color.value.encode(), bound.value, xy)
        




    def get_profile(self, prof_type, p3, p4, p5, p7, p8, p9, p10, p11, p13, p14, p16, p17, p19):
        """
        Get profile parameters in `GXSTK` object

        **Note:**

        See `GXMSTK` for detailed description of all function parameters
        """
        prof_type.value, p3.value, p4.value, p5.value, p7.value, p8.value, p9.value, p11.value, p13.value, p14.value, p16.value, p17.value, p19.value = self._wrapper.get_profile(prof_type.value, p3.value, p4.value, p5.value.encode(), p7.value, p8.value, p9.value, p10._wrapper, p11.value.encode(), p13.value, p14.value.encode(), p16.value, p17.value.encode(), p19.value)
        




    def get_profile_ex(self, prof_type, p3, p4, p5, p7, p8, p9, p10, p11, p12, p14, p15, p17, p18, p20):
        """
        Get profile parameters in `GXSTK` object (added Break on dummy option)

        **Note:**

        See `GXMSTK` for detailed description of all function parameters
        """
        prof_type.value, p3.value, p4.value, p5.value, p7.value, p8.value, p9.value, p10.value, p12.value, p14.value, p15.value, p17.value, p18.value, p20.value = self._wrapper.get_profile_ex(prof_type.value, p3.value, p4.value, p5.value.encode(), p7.value, p8.value, p9.value, p10.value, p11._wrapper, p12.value.encode(), p14.value, p15.value.encode(), p17.value, p18.value.encode(), p20.value)
        




    def get_symb_parms(self, symb_font, symb_size, line_clr, fill_clr, wrap, clip, symb_y_loc, no_levels, vv_level, vv_type, p15, p16, p18, p19):
        """
        Get parameters in `GXSTK` object relating drawing symbols

        **Note:**

        See `GXMSTK` for detailed description of all function parameters
        """
        symb_font.value, symb_size.value, line_clr.value, fill_clr.value, wrap.value, clip.value, symb_y_loc.value, no_levels.value, p15.value, p16.value, p18.value, p19.value = self._wrapper.get_symb_parms(symb_font.value.encode(), symb_size.value, line_clr.value.encode(), fill_clr.value.encode(), wrap.value, clip.value, symb_y_loc.value, no_levels.value, vv_level._wrapper, vv_type._wrapper, p15.value, p16.value.encode(), p18.value, p19.value.encode())
        




    def get_title_parms(self, title1, title2, title1_orient, title1_x, title1_y, title2_orient, title2_x, title2_y, font, text_size, color, xy):
        """
        Get parameters in `GXSTK` object relating X/Y axis titles

        **Note:**

        See `GXMSTK` for detailed description of all function parameters
        ? mark in the note represent either X and Y
        """
        title1.value, title2.value, title1_orient.value, title1_x.value, title1_y.value, title2_orient.value, title2_x.value, title2_y.value, font.value, text_size.value, color.value = self._wrapper.get_title_parms(title1.value.encode(), title2.value.encode(), title1_orient.value, title1_x.value, title1_y.value, title2_orient.value, title2_x.value, title2_y.value, font.value.encode(), text_size.value, color.value.encode(), xy)
        




    def set_flag(self, flag, part):
        """
        Set flag indicating part of `GXSTK` object is to be drawn or not
        """
        self._wrapper.set_flag(flag, part)
        




    def set_array_colors(self, itr):
        """
        Set colors for individual channels in a `GXVA`, via an `GXITR`

        **Note:**

        The `GXITR` is consulted by taking the channel index and dividing
        by the number of channels; hence the `GXITR` maximum values should
        be in the range: 0 > values >= 1.0.
        """
        self._wrapper.set_array_colors(itr._wrapper)
        




    def set_axis_format(self, format, xy):
        """
        Set axis number display format.

        **Note:**

        By default, `DB_CHAN_FORMAT_NORMAL` is used to display the values,
        or for values > 1.e7, `DB_CHAN_FORMAT_EXP`.
        """
        self._wrapper.set_axis_format(format, xy)
        




    def set_axis_parms(self, bar_draw, min_loc, max_loc, thick, color, tick_interval, tick_size1, tick_size2, min_tick, xy):
        """
        Set parameters in `GXSTK` object relating drawing X/Y axis

        **Note:**

        See `GXMSTK` for detailed description of all function parameters
        ? mark in the note represent either X and Y
        """
        self._wrapper.set_axis_parms(bar_draw, min_loc, max_loc, thick, color.encode(), tick_interval, tick_size1, tick_size2, min_tick, xy)
        




    def set_fid_parms(self, fid_y_loc, fid_tick_size, fid_interval, fid_text_font, fid_text_size, fid_text_color):
        """
        Set parameters in `GXSTK` object relating drawing fid ticks

        **Note:**

        See `GXMSTK` for detailed description of all function parameters
        """
        self._wrapper.set_fid_parms(fid_y_loc, fid_tick_size, fid_interval, fid_text_font.encode(), fid_text_size, fid_text_color.encode())
        




    def set_gen_parms(self, x_ch, y_ch, grp_name, x_scale, p6, p7, p8, p9, p10, p11, p12):
        """
        Set general parameters in `GXSTK` object

        **Note:**

        See `GXMSTK` for detailed description of all function parameters
        """
        self._wrapper.set_gen_parms(x_ch.encode(), y_ch.encode(), grp_name.encode(), x_scale, p6, p7, p8, p9, p10, p11, p12)
        




    def set_grid_parms(self, grid, min_x, max_x, min_y, max_y, thick, cross, x_sep, y_sep, color, grid12):
        """
        Set background grid parameters in `GXSTK` object

        **Note:**

        See `GXMSTK` for detailed description of all function parameters
        ? mark in the note represent either X and Y
        """
        self._wrapper.set_grid_parms(grid, min_x, max_x, min_y, max_y, thick, cross, x_sep, y_sep, color.encode(), grid12)
        




    def set_label_parms(self, axis, min_loc, min_orient, max_loc, max_orient, interval, font, text_size, color, bound, xy):
        """
        Set parameters in `GXSTK` object relating X/Y axis labels

        **Note:**

        See `GXMSTK` for detailed description of all function parameters
        ? mark in the note represent either X and Y
        Sets the label format to GSF_NORMAL. To override this,
        use the `set_axis_format` function AFTER calling this.
        """
        self._wrapper.set_label_parms(axis, min_loc, min_orient, max_loc, max_orient, interval, font.encode(), text_size, color.encode(), bound, xy)
        




    def set_line_parm(self, line):
        """
        Set line parameter (of Y Chan) in `GXSTK` object

        **Note:**

        See `GXMSTK` for detailed description of all function parameters
        """
        self._wrapper.set_line_parm(line)
        




    def set_profile(self, prof_type, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15):
        """
        Set profile parameters in `GXSTK` object

        **Note:**

        See `GXMSTK` for detailed description of all function parameters
        """
        self._wrapper.set_profile(prof_type, p3, p4, p5.encode(), p6, p7, p8, p9._wrapper, p10.encode(), p11, p12.encode(), p13, p14.encode(), p15)
        




    def set_profile_ex(self, prof_type, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16):
        """
        Set profile parameters in `GXSTK` object (added Break on dummy option)

        **Note:**

        See `GXMSTK` for detailed description of all function parameters
        """
        self._wrapper.set_profile_ex(prof_type, p3, p4, p5.encode(), p6, p7, p8, p9, p10._wrapper, p11.encode(), p12, p13.encode(), p14, p15.encode(), p16)
        




    def set_symb_parms(self, symb_font, symb_size, line_clr, fill_clr, wrap, clip, symb_y_loc, no_levels, vv_level, vv_type, p12, p13, p14, p15):
        """
        Set parameters in `GXSTK` object relating drawing symbols

        **Note:**

        See `GXMSTK` for detailed description of all function parameters
        """
        self._wrapper.set_symb_parms(symb_font.encode(), symb_size, line_clr.encode(), fill_clr.encode(), wrap, clip, symb_y_loc, no_levels, vv_level._wrapper, vv_type._wrapper, p12, p13.encode(), p14, p15.encode())
        




    def set_title_parms(self, title1, title2, title1_orient, title1_x, title1_y, title2_orient, title2_x, title2_y, font, text_size, color, xy):
        """
        Set parameters in `GXSTK` object relating X/Y axis titles

        **Note:**

        See `GXMSTK` for detailed description of all function parameters
        ? mark in the note represent either X and Y
        """
        self._wrapper.set_title_parms(title1.encode(), title2.encode(), title1_orient, title1_x, title1_y, title2_orient, title2_x, title2_y, font.encode(), text_size, color.encode(), xy)
        




    def set_trans_parms(self, x_trans_t, x_log_min, xvv_lev, xvv_cmp, y_trans_t, y_log_min, yvv_lev, yvv_cmp):
        """
        Set transformation parameters in `GXSTK` object

        **Note:**

        See above full description of each parameters
        `GXVV`'s for X channel transformation can be NULL if the
        transformation is log or loglinear. The same for Y channel.
        See `GXMSTK` for detailed description of all function parameters
        """
        self._wrapper.set_trans_parms(x_trans_t, x_log_min, xvv_lev, xvv_cmp, y_trans_t, y_log_min, yvv_lev, yvv_cmp)
        




    def set_va_index_start(self, index0):
        """
        Start array profile index labels at 0 or 1.

        **Note:**

        By default, the index labels for array channel profiles
        begin at 0. Use this function to start them at either 0
        or 1.
        """
        self._wrapper.set_va_index_start(index0)
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer