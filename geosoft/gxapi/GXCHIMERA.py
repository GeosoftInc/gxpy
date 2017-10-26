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
class GXCHIMERA:
    """
    GXCHIMERA class.

    `GXCHIMERA` GX function library.
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._wrapper = None

    def __del__(self):
        self._wrapper = None

    def __init__(self, wrapper=None):
        self._wrapper = wrapper if wrapper else gxapi_cy.WrapCHIMERA(GXContext._get_tls_geo(), 0)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of `GXCHIMERA`
        
        :returns: A null `GXCHIMERA`
        """
        return cls()

    def is_null(self):
        """
        Check if the instance of `GXCHIMERA` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of `GXCHIMERA`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Miscellaneous


    @classmethod
    def bar_plot(cls, mview, data_group, offset_group, xvv, yvv, dvv, cvv, col, offset, offset_size, width):
        """
        Plot a Bar plot of up to 8 channels.

        **Note:**

        The number of channels is taken from the Data handles `GXVV`.
        Plots a bar plot with the center of the "X" axis at the symbol location.
        See the note on offset symbols in `rose_plot`
        """
        gxapi_cy.WrapCHIMERA.bar_plot(GXContext._get_tls_geo(), mview._wrapper, data_group.encode(), offset_group.encode(), xvv._wrapper, yvv._wrapper, dvv._wrapper, cvv._wrapper, col, offset, offset_size, width)
        



    @classmethod
    def categorize_by_value(cls, v_vr, v_vi, v_vo):
        """
        Transform values to the index of input data ranges.

        **Note:**

        A list of minima (e.g.  M1, M2, M3, M4, M5) is input.
        A list of values V is input and transformed to outputs N in the following manner:
        
        if(V) >= M5) N = 5
        else if(V) >= M4) N = 4
        ...
        ...
        else if(V) >= M1) N = 1
        else N = 0
        """
        gxapi_cy.WrapCHIMERA.categorize_by_value(GXContext._get_tls_geo(), v_vr._wrapper, v_vi._wrapper, v_vo._wrapper)
        



    @classmethod
    def categorize_by_value_det_limit(cls, v_vr, v_vi, det_limit, v_vo):
        """
        Transform values to the index of input data ranges, with detection limit.

        **Note:**

        Same as `categorize_by_value`, but if the
        input value is less than the detection limit,
        the output value is set to zero.
        """
        gxapi_cy.WrapCHIMERA.categorize_by_value_det_limit(GXContext._get_tls_geo(), v_vr._wrapper, v_vi._wrapper, det_limit, v_vo._wrapper)
        



    @classmethod
    def clip_to_detect_limit(cls, vv, det_limit, conv):
        """
        Apply detection limit clipping of data.

        **Note:**

        Flow:
        
        1. If auto-converting negatives, then all negative values
            are replaced by -0.5*value, and detection limit is ignored.
        
        2. If not auto-converting negatives, and the detection limit is not
           `rDUMMY`, then values less than the detection limit are converted to
           one-half the detection limit.
        """
        gxapi_cy.WrapCHIMERA.clip_to_detect_limit(GXContext._get_tls_geo(), vv._wrapper, det_limit, conv)
        



    @classmethod
    def draw_circle_offset_markers(cls, mview, v_vxi, v_vyi, v_vxo, v_vyo, off_size):
        """
        Plots location marker and joining line for circle offset symbols

        **Note:**

        Draws black filled circle (symbols.gfn #7) and a joining line.
        """
        gxapi_cy.WrapCHIMERA.draw_circle_offset_markers(GXContext._get_tls_geo(), mview._wrapper, v_vxi._wrapper, v_vyi._wrapper, v_vxo._wrapper, v_vyo._wrapper, off_size)
        



    @classmethod
    def draw_rectangle_offset_markers(cls, mview, v_vxi, v_vyi, v_vxo, v_vyo, off_size, x_size, y_size):
        """
        Plots location marker and joining line for rectangle offset symbols

        **Note:**

        Draws black filled circle (symbols.gfn #7) and a joining line.
        """
        gxapi_cy.WrapCHIMERA.draw_rectangle_offset_markers(GXContext._get_tls_geo(), mview._wrapper, v_vxi._wrapper, v_vyi._wrapper, v_vxo._wrapper, v_vyo._wrapper, off_size, x_size, y_size)
        



    @classmethod
    def duplicate_chem(cls, mview, vv, log, det_lim, old, vv_tol, p7, p8, p9, p10, p11, p12):
        """
        Plot an ASSAY Duplicate result in a graph window.
        """
        gxapi_cy.WrapCHIMERA.duplicate_chem(GXContext._get_tls_geo(), mview._wrapper, vv._wrapper, log, det_lim, old, vv_tol._wrapper, p7.encode(), p8.encode(), p9, p10, p11, p12)
        



    @classmethod
    def duplicate_chem_view(cls, map, view, group, ipj, vv, log, det_lim, old, vv_tol, p10, p11, p12, p13, p14, p15, p16, p17):
        """
        Plot an ASSAY Duplicate result in a new view.
        """
        p16.value, p17.value = gxapi_cy.WrapCHIMERA.duplicate_chem_view(GXContext._get_tls_geo(), map._wrapper, view.encode(), group.encode(), ipj._wrapper, vv._wrapper, log, det_lim, old, vv_tol._wrapper, p10.encode(), p11.encode(), p12._wrapper, p13._wrapper, p14._wrapper, p15._wrapper, p16.value, p17.value)
        



    @classmethod
    def get_expression_data_vv(cls, db, line, stage, exp, ini, gvv):
        """
        Get data from a line using a channel expression.

        **Note:**

        Input a channel expression. Units for individual channels
        are stored in the input INI. Returns a `GXVV` for the given line
        with the calculated expression values.
        """
        gxapi_cy.WrapCHIMERA.get_expression_data_vv(GXContext._get_tls_geo(), db._wrapper, line, stage.encode(), exp.encode(), ini.encode(), gvv._wrapper)
        



    @classmethod
    def get_lithogeochem_data(cls, db, lst, m_ch, v_vtrans, remove_dummy_rows, v_vdummy, warn, v_vd, v_vline, v_vn, v_vused, v_vindex, v_vfids, v_vfidi):
        """
        Get all rows of non-dummy data in a database.

        **Note:**

        This function is a quick way to get all rows
        of data, guaranteeing no dummy items.
        Book-keeping VVs returned let you easily
        write back results to new channels in the
        correct locations.
        Set the "Dummy Row" `GXVV` to 1 if you wish to
        remove any row where a value for the corresponding
        channel is a dummy.
        
        Transforms to apply:
        
        -1 - Channel default (will be either raw or log)
        0 - Raw Transform
        1 - Log transform: base e with log min = CHIMERA_LOG_MIN
        2 - Lambda transform
        """
        gxapi_cy.WrapCHIMERA.get_lithogeochem_data(GXContext._get_tls_geo(), db._wrapper, lst._wrapper, m_ch, v_vtrans._wrapper, remove_dummy_rows, v_vdummy._wrapper, warn, v_vd._wrapper, v_vline._wrapper, v_vn._wrapper, v_vused._wrapper, v_vindex._wrapper, v_vfids._wrapper, v_vfidi._wrapper)
        



    @classmethod
    def get_transform(cls, db, chan, trans_opt, trans, lda):
        """
        Get channel transform options and lambda values.

        **Note:**

        If the lambda transform is requested, the channel
        must have the lambda value defined.
        
        Input Transform options
        
        -1 - Channel default (will be either raw or log)
        0 - Raw Transform
        1 - Log transform: base e with log min = CHIMERA_LOG_MIN
        2 - Lambda transform
        """
        trans.value, lda.value = gxapi_cy.WrapCHIMERA.get_transform(GXContext._get_tls_geo(), db._wrapper, chan.encode(), trans_opt, trans.value, lda.value)
        



    @classmethod
    def is_acquire_chan(cls, input_chan, chan, units, factor, oxide):
        """
        Is this channel in acQuire format (e.g. "Ag_ppm_4AWR")

        **Note:**

        Expressions can take acQuire-type named channels
        if the exact element/oxide is not found. This function
        extracts the channel name, and units from an acQuire-formatted
        channel name.
        """
        ret_val, chan.value, units.value, factor.value, oxide.value = gxapi_cy.WrapCHIMERA.is_acquire_chan(GXContext._get_tls_geo(), input_chan.encode(), chan.value.encode(), units.value.encode(), factor.value, oxide.value)
        return ret_val



    @classmethod
    def is_element(cls, chan, case):
        """
        Tests a string to see if it is an element symbol

        **Note:**

        Suggested use - testing to see if a channel name is an
        element so that the "ASSAY" class can be set.
        """
        ret_val = gxapi_cy.WrapCHIMERA.is_element(GXContext._get_tls_geo(), chan.encode(), case)
        return ret_val



    @classmethod
    def launch_histogram(cls, db, chan):
        """
        Launch histogram tool on a database.

        **Note:**

        The database should be a currently open database.
        This function supercedes `GXEDB.launch_histogram`, (which now
        just gets the name of the `GXEDB` and calls this function).
        """
        gxapi_cy.WrapCHIMERA.launch_histogram(GXContext._get_tls_geo(), db.encode(), chan.encode())
        



    @classmethod
    def launch_probability(cls, db, chan):
        """
        Launch probability tool on a database.

        **Note:**

        The database should be a currently open database.
        """
        gxapi_cy.WrapCHIMERA.launch_probability(GXContext._get_tls_geo(), db.encode(), chan.encode())
        



    @classmethod
    def launch_scatter(cls, db):
        """
        Launch scatter tool on a database.

        **Note:**

        The scatter tool uses the following INI parameters
        
        SCATTER.STM       name of the scatter template, "none" for none
        SCATTER.STM_NAME  name of last template section, "" for none.
        SCATTER.X         name of channel to display in X
        SCATTER.Y         name of channel to display in Y
        SCATTER.MASK      name of channel to use for mask
        
        The database should be a currently open database.
        This function supercedes `GXEDB.launch_scatter`, (which now
        just gets the name of the `GXEDB` and calls this function).
        """
        gxapi_cy.WrapCHIMERA.launch_scatter(GXContext._get_tls_geo(), db.encode())
        



    @classmethod
    def launch_triplot(cls, db):
        """
        Launch Triplot tool on a database.

        **Note:**

        The Triplot tool uses the following INI parameters
        
                 TRIPLOT.TTM       name of the triplot template, "none" for none
                 TRIPLOT.TTM_NAME  name of last template section, "" for none.
                 TRIPLOT.X         name of channel to display in X
                 TRIPLOT.Y         name of channel to display in Y
                 TRIPLOT.Z         name of channel to display in Z
                 TRIPLOT.MASK      name of channel to use for mask
        
        The database should be a currently open database.
        """
        gxapi_cy.WrapCHIMERA.launch_triplot(GXContext._get_tls_geo(), db.encode())
        



    @classmethod
    def mask_chan_lst(cls, db, lst):
        """
        Load a `GXLST` with mask channels.

        **Note:**

        Loads a `GXLST` with all channels with CLASS "MASK", as well
        as all channels containing the string "MASK", as long
        as the CLASS for these channels is not set to something
        other than "" or "MASK".
        
        This function has been duplicated by `GXDB.mask_chan_lst`, which
        is safe to use in applications which do not have `GXCHIMERA` loaded.
        """
        gxapi_cy.WrapCHIMERA.mask_chan_lst(GXContext._get_tls_geo(), db._wrapper, lst._wrapper)
        



    @classmethod
    def ordered_channel_lst(cls, db, lst):
        """
        Fill a list with the channels in the preferred order.

        **Note:**

        Loads a `GXLST` with all channels in the preferred order:
        
        First:  Sample, E, N, assay channels,
        Middle: Data from survey (other channels),
        Last:   Duplicate, Standard, Chemmask (and other masks), weight, lab, batch
        
        If the input `GXLST` object has values, it is used as the channel `GXLST`,
        otherwise, get all the database channels. (This allows you to pass in
        the currently displayed channels and only reload those).
        """
        gxapi_cy.WrapCHIMERA.ordered_channel_lst(GXContext._get_tls_geo(), db._wrapper, lst._wrapper)
        



    @classmethod
    def pie_plot(cls, mview, data_group, offset_group, xvv, yvv, dvv, cvv, col, offset, offset_size, radius):
        """
        Plot a Pie plot of up to 8 channels.

        **Note:**

        The number of channels is taken from the Data handles `GXVV`.
        The values in each data `GXVV` are summed and the pie arc is
        is given by the percent contribution of each constituent.
        See the note on offset symbols in `rose_plot`
        """
        gxapi_cy.WrapCHIMERA.pie_plot(GXContext._get_tls_geo(), mview._wrapper, data_group.encode(), offset_group.encode(), xvv._wrapper, yvv._wrapper, dvv._wrapper, cvv._wrapper, col, offset, offset_size, radius)
        



    @classmethod
    def pie_plot2(cls, mview, data_group, offset_group, xvv, yvv, dvv, cvv, col, offset, offset_size, radius, start_angle):
        """
        Same as `pie_plot`, with a starting angle.

        **Note:**

        The starting angle is the location of the edge of the first pie
        slice, counted in degrees counter-clockwise from horizontal
        (3 o'clock). Zero degrees gives the same plot as `pie_plot`.
        """
        gxapi_cy.WrapCHIMERA.pie_plot2(GXContext._get_tls_geo(), mview._wrapper, data_group.encode(), offset_group.encode(), xvv._wrapper, yvv._wrapper, dvv._wrapper, cvv._wrapper, col, offset, offset_size, radius, start_angle)
        



    @classmethod
    def plot_string_classified_symbols_legend_from_class_file(cls, mview, title, x, y_min, y_max, class_file, index_vv):
        """
        Plot legend for the string classified symbols

        **Note:**

        Plot in a legend the classes in the class file found in the input class indices.
        """
        gxapi_cy.WrapCHIMERA.plot_string_classified_symbols_legend_from_class_file(GXContext._get_tls_geo(), mview._wrapper, title.encode(), x, y_min, y_max, class_file.encode(), index_vv._wrapper)
        



    @classmethod
    def atomic_weight(cls, element):
        """
        Return the atomic weight of a particular element.

        **Note:**

        If the input string is not an element symbol (elements in the range
        1-92, "H" to "U"), then returns a dummy (`GS_R8DM`).
        """
        ret_val = gxapi_cy.WrapCHIMERA.atomic_weight(GXContext._get_tls_geo(), element.encode())
        return ret_val



    @classmethod
    def rose_plot(cls, mview, data_group, offset_group, xvv, yvv, dvv, cvv, col, offset, offset_size):
        """
        Plot a Rose plot of up to 8 channels.

        **Note:**

        The number of channels is taken from the Data handles `GXVV`.
        The values in each data `GXVV` give the radius, in view units,
        of the sector arc to plots. Values <=0 or dummies are not
        plotted.
        
        Offset symbols: When selected, the symbols plot without
        overlap, away from the original locations. The original
        location is marked with a small symbol and a line joins the
        original position and the relocated symbol.
        Care should be taken when choosing the symbol size, because
        if the point density is too high, all the points will get
        pushed to the outside edge and your plot will look like a
        hedgehog (it also takes a lot longer!).
        """
        gxapi_cy.WrapCHIMERA.rose_plot(GXContext._get_tls_geo(), mview._wrapper, data_group.encode(), offset_group.encode(), xvv._wrapper, yvv._wrapper, dvv._wrapper, cvv._wrapper, col, offset, offset_size)
        



    @classmethod
    def rose_plot2(cls, mview, data_group, offset_group, xvv, yvv, dvv, cvv, col, offset, offset_size, start_angle):
        """
        Same as `rose_plot`, with a starting angle.

        **Note:**

        The starting angle is the location of the edge of the first pie
        slice, counted in degrees counter-clockwise from horizontal
        (3 o'clock). Zero degrees gives the same plot as `rose_plot`.
        """
        gxapi_cy.WrapCHIMERA.rose_plot2(GXContext._get_tls_geo(), mview._wrapper, data_group.encode(), offset_group.encode(), xvv._wrapper, yvv._wrapper, dvv._wrapper, cvv._wrapper, col, offset, offset_size, start_angle)
        



    @classmethod
    def scatter2(cls, mview, title, x1, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16, p17, p18, p19, p20, p21, p22, p23, p24, p25, p26, p27, p28, p29, p30, p31):
        """
        Plot the scatter plot on a map using symbol number, size and color VVs.

        **Note:**

        The view scaling is not altered with any projection. The base view
        is best as the input.
        """
        gxapi_cy.WrapCHIMERA.scatter2(GXContext._get_tls_geo(), mview._wrapper, title.encode(), x1, p4, p5, p6, p7._wrapper, p8._wrapper, p9.encode(), p10._wrapper, p11._wrapper, p12._wrapper, p13, p14.encode(), p15.encode(), p16.encode(), p17.encode(), p18, p19, p20, p21, p22, p23, p24, p25, p26, p27, p28, p29, p30, p31)
        



    @classmethod
    def fixed_symbol_scatter_plot(cls, mview, title, x1, y1, width, height, x_vv, y_vv, m_vv, mask_col, symbol_font, symbol_number, symbol_size, symbol_angle, symbol_color, symbol_fill, db, line_vv, fid_vv, annotn, x_chan, y_chan, x_units, y_units, x_min, x_max, y_min, y_max, x_lin, y_lin, overlay):
        """
        Plot a scatter plot using a single fixed symbol.
        Optional data masking with masking Color.
        Optional database linking.

        **Note:**

        Plot a scatter plot using a single fixed symbol.
        """
        gxapi_cy.WrapCHIMERA.fixed_symbol_scatter_plot(GXContext._get_tls_geo(), mview._wrapper, title.encode(), x1, y1, width, height, x_vv._wrapper, y_vv._wrapper, m_vv._wrapper, mask_col, symbol_font.encode(), symbol_number, symbol_size, symbol_angle, symbol_color, symbol_fill, db._wrapper, line_vv._wrapper, fid_vv._wrapper, annotn, x_chan.encode(), y_chan.encode(), x_units.encode(), y_units.encode(), x_min, x_max, y_min, y_max, x_lin, y_lin, overlay.encode())
        



    @classmethod
    def zone_coloured_scatter_plot(cls, mview, title, x1, y1, width, height, x_vv, y_vv, m_vv, mask_col, zone_data_vv, zone_file, symbol_font, symbol_number, symbol_size, symbol_angle, symbol_color, symbol_fill, fix_edge_color, db, line_vv, fid_vv, annotn, x_chan, y_chan, x_units, y_units, x_min, x_max, y_min, y_max, x_lin, y_lin, overlay):
        """
        Plot a scatter plot using colors based on a zone file.
        Optional data masking with masking color.
        Optional database linking.

        **Note:**

        Plot a scatter plot using colors based on a zone file.
        """
        gxapi_cy.WrapCHIMERA.zone_coloured_scatter_plot(GXContext._get_tls_geo(), mview._wrapper, title.encode(), x1, y1, width, height, x_vv._wrapper, y_vv._wrapper, m_vv._wrapper, mask_col, zone_data_vv._wrapper, zone_file.encode(), symbol_font.encode(), symbol_number, symbol_size, symbol_angle, symbol_color, symbol_fill, fix_edge_color, db._wrapper, line_vv._wrapper, fid_vv._wrapper, annotn, x_chan.encode(), y_chan.encode(), x_units.encode(), y_units.encode(), x_min, x_max, y_min, y_max, x_lin, y_lin, overlay.encode())
        



    @classmethod
    def string_classified_scatter_plot(cls, mview, title, x1, y1, width, height, x_vv, y_vv, m_vv, mask_col, class_vv, class_file, symbol_size_override, db, line_vv, fid_vv, annotn, x_chan, y_chan, x_units, y_units, x_min, x_max, y_min, y_max, x_lin, y_lin, overlay):
        """
        Plot a scatter plot using symbols based on a symbol class file.
        Optional data masking with masking color.
        Optional database linking.

        **Note:**

        Plot a scatter plot using symbols based on a symbol class file.
        """
        gxapi_cy.WrapCHIMERA.string_classified_scatter_plot(GXContext._get_tls_geo(), mview._wrapper, title.encode(), x1, y1, width, height, x_vv._wrapper, y_vv._wrapper, m_vv._wrapper, mask_col, class_vv._wrapper, class_file.encode(), symbol_size_override, db._wrapper, line_vv._wrapper, fid_vv._wrapper, annotn, x_chan.encode(), y_chan.encode(), x_units.encode(), y_units.encode(), x_min, x_max, y_min, y_max, x_lin, y_lin, overlay.encode())
        



    @classmethod
    def set_lithogeochem_data(cls, db, lst, v_vd, v_vline, v_vn, v_vused, v_vindex, v_vfids, v_vfidi, v_vdummy):
        """
        Set data back into a database.

        **Note:**

        This function would normally be called after
        AAGetLithogeochemData_CHIMERA to write processed values
        back into a database, in the correct lines,
        and in the correct fiducial locations wrt the
        other data. The book-keeping VVs would all be
        set up in AAGetLithogeochemData_CHIMERA.
        
        Values NOT in the data (missing indices) will
        be initialized to dummy if the channel is new,
        or if the value in the last `GXVV` below is set to 1.
        
        New channel types will be set using the data `GXVV` type.
        Any metadata (CLASS, display formats) should be set separately.
        """
        gxapi_cy.WrapCHIMERA.set_lithogeochem_data(GXContext._get_tls_geo(), db._wrapper, lst._wrapper, v_vd._wrapper, v_vline._wrapper, v_vn._wrapper, v_vused._wrapper, v_vindex._wrapper, v_vfids._wrapper, v_vfidi._wrapper, v_vdummy._wrapper)
        



    @classmethod
    def stacked_bar_plot(cls, mview, data_group, offset_group, xvv, yvv, dvv, cvv, col, offset, offset_size, width):
        """
        Plot a Bar plot of up to 8 channels, bars stacked on each other.

        **Note:**

        The number of channels is taken from the Data handles `GXVV`.
        Plots a bar plot with the center of the "X" axis at the symbol location.
        See the note on offset symbols in `rose_plot`
        """
        gxapi_cy.WrapCHIMERA.stacked_bar_plot(GXContext._get_tls_geo(), mview._wrapper, data_group.encode(), offset_group.encode(), xvv._wrapper, yvv._wrapper, dvv._wrapper, cvv._wrapper, col, offset, offset_size, width)
        



    @classmethod
    def standard(cls, mview, vv, old, tol, min, max, title, unit, x0, y0, xs, ys):
        """
        Plot ASSAY Standard result in a graph window.

        **Note:**

        If the tolerance is `rDUMMY`, then the minimum and maximum
        values are used, and must be specified.
        """
        gxapi_cy.WrapCHIMERA.standard(GXContext._get_tls_geo(), mview._wrapper, vv._wrapper, old, tol, min, max, title.encode(), unit.encode(), x0, y0, xs, ys)
        



    @classmethod
    def standard_view(cls, map, view, group, ipj, vvy, old, tol, min, max, title, unit, xs, vvx, vv_line, vv_fid, db, min_y, max_y):
        """
        Plot ASSAY Standard result in a graph window.

        **Note:**

        Same as `standard` but plot in a new view.
        """
        min_y.value, max_y.value = gxapi_cy.WrapCHIMERA.standard_view(GXContext._get_tls_geo(), map._wrapper, view.encode(), group.encode(), ipj._wrapper, vvy._wrapper, old, tol, min, max, title.encode(), unit.encode(), xs, vvx._wrapper, vv_line._wrapper, vv_fid._wrapper, db._wrapper, min_y.value, max_y.value)
        



    @classmethod
    def tri_plot2(cls, mview, title, x1, y1, width, height, x_vv, y_vv, z_vv, m_vv, sym_font, p12, p13, p14, p15, p16, p17, p18, p19, p20, p21, p22, p23, p24, p25, p26, p27, p28, p29, p30, p31, p32):
        """
        Plot the TriPlot on a map using symbol number, size and color VVs.

        **Note:**

        The mask channel `GXVV` is used for plotting precedence; those points with
        mask = dummy are plotted first, then overwritten with the non-masked
        values, so you don't get "good" points being covered up by masked values.
        The view scaling is not altered with any projection. The base view
        is best as the input.
        """
        gxapi_cy.WrapCHIMERA.tri_plot2(GXContext._get_tls_geo(), mview._wrapper, title.encode(), x1, y1, width, height, x_vv._wrapper, y_vv._wrapper, z_vv._wrapper, m_vv._wrapper, sym_font.encode(), p12._wrapper, p13._wrapper, p14._wrapper, p15.encode(), p16.encode(), p17.encode(), p18, p19, p20, p21, p22, p23, p24, p25, p26, p27, p28, p29, p30, p31, p32)
        



    @classmethod
    def fixed_symbol_tri_plot(cls, mview, title, x1, y1, side, x_vv, y_vv, z_vv, m_vv, mask_col, symbol_font, symbol_number, symbol_size, symbol_angle, symbol_color, symbol_fill, db, line_vv, fid_vv, x_chan, y_chan, z_chan, grid, tic, grid_inc, overlay):
        """
        Plot a tri-plot using a single fixed symbol.
        Optional data masking with masking color.
        Optional database linking.

        **Note:**

        Plot a tri plot using a single fixed symbol.
        """
        gxapi_cy.WrapCHIMERA.fixed_symbol_tri_plot(GXContext._get_tls_geo(), mview._wrapper, title.encode(), x1, y1, side, x_vv._wrapper, y_vv._wrapper, z_vv._wrapper, m_vv._wrapper, mask_col, symbol_font.encode(), symbol_number, symbol_size, symbol_angle, symbol_color, symbol_fill, db._wrapper, line_vv._wrapper, fid_vv._wrapper, x_chan.encode(), y_chan.encode(), z_chan.encode(), grid, tic, grid_inc, overlay.encode())
        



    @classmethod
    def zone_coloured_tri_plot(cls, mview, title, x1, y1, side, x_vv, y_vv, z_vv, m_vv, mask_col, zone_data_vv, zone_file, symbol_font, symbol_number, symbol_size, symbol_angle, symbol_color, symbol_fill, fix_edge_color, db, line_vv, fid_vv, x_chan, y_chan, z_chan, grid, tic, grid_inc, overlay):
        """
        Plot a tri-plot using colors based on a zone file.
        Optional data masking with masking color.
        Optional database linking.

        **Note:**

        Plot a tri plot using colors based on a zone file.
        """
        gxapi_cy.WrapCHIMERA.zone_coloured_tri_plot(GXContext._get_tls_geo(), mview._wrapper, title.encode(), x1, y1, side, x_vv._wrapper, y_vv._wrapper, z_vv._wrapper, m_vv._wrapper, mask_col, zone_data_vv._wrapper, zone_file.encode(), symbol_font.encode(), symbol_number, symbol_size, symbol_angle, symbol_color, symbol_fill, fix_edge_color, db._wrapper, line_vv._wrapper, fid_vv._wrapper, x_chan.encode(), y_chan.encode(), z_chan.encode(), grid, tic, grid_inc, overlay.encode())
        



    @classmethod
    def string_classified_tri_plot(cls, mview, title, x1, y1, side, x_vv, y_vv, z_vv, m_vv, mask_col, class_vv, class_file, symbol_size_override, db, line_vv, fid_vv, x_chan, y_chan, z_chan, grid, tic, grid_inc, overlay):
        """
        Plot a tri-plot using symbols based on a symbol class file.
        Optional data masking with masking color.
        Optional database linking.

        **Note:**

        Plot a tri-plot using symbols based on a symbol class file.
        """
        gxapi_cy.WrapCHIMERA.string_classified_tri_plot(GXContext._get_tls_geo(), mview._wrapper, title.encode(), x1, y1, side, x_vv._wrapper, y_vv._wrapper, z_vv._wrapper, m_vv._wrapper, mask_col, class_vv._wrapper, class_file.encode(), symbol_size_override, db._wrapper, line_vv._wrapper, fid_vv._wrapper, x_chan.encode(), y_chan.encode(), z_chan.encode(), grid, tic, grid_inc, overlay.encode())
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer