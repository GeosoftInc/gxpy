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
class GXCHIMERA(gxapi_cy.WrapCHIMERA):
    """
    GXCHIMERA class.

    `GXCHIMERA <geosoft.gxapi.GXCHIMERA>` GX function library.
    """

    def __init__(self, handle=0):
        super().__init__(GXContext._get_tls_geo(), handle)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of `GXCHIMERA <geosoft.gxapi.GXCHIMERA>`
        
        :returns: A null `GXCHIMERA <geosoft.gxapi.GXCHIMERA>`
        :rtype:   GXCHIMERA
        """
        return GXCHIMERA()

    def is_null(self):
        """
        Check if this is a null (undefined) instance
        
        :returns: True if this is a null (undefined) instance, False otherwise.
        :rtype:   bool
        """
        return self._internal_handle() == 0



# Miscellaneous


    @classmethod
    def bar_plot(cls, mview, data_group, offset_group, xvv, yvv, dvv, cvv, col, offset, offset_size, width):
        """
        Plot a Bar plot of up to 8 channels.
        
        :param mview:         View object to plot to
        :param data_group:    Data group name
        :param offset_group:  Offset group name
        :param xvv:           X locations
        :param yvv:           Y locations
        :param dvv:           Data handles, stored as INT values
        :param cvv:           Colors
        :param col:           Color for edges
        :param offset:        Offset symbols (0: No, 1: Yes)
        :param offset_size:   Offset symbol size
        :param width:         Single bar width in data units.
        :type  mview:         GXMVIEW
        :type  data_group:    str
        :type  offset_group:  str
        :type  xvv:           GXVV
        :type  yvv:           GXVV
        :type  dvv:           GXVV
        :type  cvv:           GXVV
        :type  col:           int
        :type  offset:        int
        :type  offset_size:   float
        :type  width:         float

        .. versionadded:: 5.0.7

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_

        **Note:** The number of channels is taken from the Data handles `GXVV <geosoft.gxapi.GXVV>`.
        Plots a bar plot with the center of the "X" axis at the symbol location.
        See the note on offset symbols in `rose_plot <geosoft.gxapi.GXCHIMERA.rose_plot>`
        """
        gxapi_cy.WrapCHIMERA._bar_plot(GXContext._get_tls_geo(), mview, data_group.encode(), offset_group.encode(), xvv, yvv, dvv, cvv, col, offset, offset_size, width)
        



    @classmethod
    def categorize_by_value(cls, vv_r, vv_i, vv_o):
        """
        Transform values to the index of input data ranges.
        
        :param vv_r:  Input range minima
        :param vv_i:  Input data `GXVV <geosoft.gxapi.GXVV>`.      (REAL)
        :param vv_o:  Output (altered) `GXVV <geosoft.gxapi.GXVV>`.(REAL)
        :type  vv_r:  GXVV
        :type  vv_i:  GXVV
        :type  vv_o:  GXVV

        .. versionadded:: 6.1

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_

        **Note:** A list of minima (e.g.  M1, M2, M3, M4, M5) is input.
        A list of values V is input and transformed to outputs N in the following manner:

        if(V) >= M5) N = 5
        else if(V) >= M4) N = 4
        ...
        ...
        else if(V) >= M1) N = 1
        else N = 0
        """
        gxapi_cy.WrapCHIMERA._categorize_by_value(GXContext._get_tls_geo(), vv_r, vv_i, vv_o)
        



    @classmethod
    def categorize_by_value_det_limit(cls, vv_r, vv_i, det_limit, vv_o):
        """
        Transform values to the index of input data ranges, with detection limit.
        
        :param vv_r:       Input range minima
        :param vv_i:       Input data `GXVV <geosoft.gxapi.GXVV>`.      (REAL)
        :param det_limit:  Detection limit (can be `rDUMMY <geosoft.gxapi.rDUMMY>`)
        :param vv_o:       Output (altered) `GXVV <geosoft.gxapi.GXVV>`.(REAL)
        :type  vv_r:       GXVV
        :type  vv_i:       GXVV
        :type  det_limit:  float
        :type  vv_o:       GXVV

        .. versionadded:: 6.2

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_

        **Note:** Same as `categorize_by_value <geosoft.gxapi.GXCHIMERA.categorize_by_value>`, but if the
        input value is less than the detection limit,
        the output value is set to zero.
        """
        gxapi_cy.WrapCHIMERA._categorize_by_value_det_limit(GXContext._get_tls_geo(), vv_r, vv_i, det_limit, vv_o)
        



    @classmethod
    def clip_to_detect_limit(cls, vv, det_limit, conv):
        """
        Apply detection limit clipping of data.
        
        :param vv:         Input data vv (altered).
        :param det_limit:  Detection limit
        :param conv:       Auto-convert negatives?
        :type  vv:         GXVV
        :type  det_limit:  float
        :type  conv:       int

        .. versionadded:: 5.0.8

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_

        **Note:** Flow:

        1. If auto-converting negatives, then all negative values
            are replaced by -0.5*value, and detection limit is ignored.

        2. If not auto-converting negatives, and the detection limit is not
           `rDUMMY <geosoft.gxapi.rDUMMY>`, then values less than the detection limit are converted to
           one-half the detection limit.
        """
        gxapi_cy.WrapCHIMERA._clip_to_detect_limit(GXContext._get_tls_geo(), vv, det_limit, conv)
        



    @classmethod
    def draw_circle_offset_markers(cls, mview, vv_xi, vv_yi, vv_xo, vv_yo, off_size):
        """
        Plots location marker and joining line for circle offset symbols
        
        :param mview:     View
        :param vv_xi:     Original (marker) X location
        :param vv_yi:     Original (marker) Y location
        :param vv_xo:     Offset (new) X location
        :param vv_yo:     Offset (new) Y location
        :param off_size:  Marker symbol radius
        :type  mview:     GXMVIEW
        :type  vv_xi:     GXVV
        :type  vv_yi:     GXVV
        :type  vv_xo:     GXVV
        :type  vv_yo:     GXVV
        :type  off_size:  float

        .. versionadded:: 5.0.7

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_

        **Note:** Draws black filled circle (symbols.gfn #7) and a joining line.
        """
        gxapi_cy.WrapCHIMERA._draw_circle_offset_markers(GXContext._get_tls_geo(), mview, vv_xi, vv_yi, vv_xo, vv_yo, off_size)
        



    @classmethod
    def draw_rectangle_offset_markers(cls, mview, vv_xi, vv_yi, vv_xo, vv_yo, off_size, x_size, y_size):
        """
        Plots location marker and joining line for rectangle offset symbols
        
        :param mview:     View
        :param vv_xi:     Original (marker) X location
        :param vv_yi:     Original (marker) Y location
        :param vv_xo:     Offset (new) X location
        :param vv_yo:     Offset (new) Y location
        :param off_size:  Offset symbol width
        :param x_size:    Offset symbol height
        :param y_size:    Marker symbol radius
        :type  mview:     GXMVIEW
        :type  vv_xi:     GXVV
        :type  vv_yi:     GXVV
        :type  vv_xo:     GXVV
        :type  vv_yo:     GXVV
        :type  off_size:  float
        :type  x_size:    float
        :type  y_size:    float

        .. versionadded:: 5.0.7

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_

        **Note:** Draws black filled circle (symbols.gfn #7) and a joining line.
        """
        gxapi_cy.WrapCHIMERA._draw_rectangle_offset_markers(GXContext._get_tls_geo(), mview, vv_xi, vv_yi, vv_xo, vv_yo, off_size, x_size, y_size)
        



    @classmethod
    def duplicate_chem(cls, mview, vv, log, det_lim, old, vv_tol, title, unit, x0, y0, xs, ys):
        """
        Plot an ASSAY Duplicate result in a graph window.
        
        :param mview:    View
        :param vv:       Duplicate data
        :param log:      Log-transform: 0 - linear, 1 - log
        :param det_lim:  Detect Limit
        :param old:      Number of old samples in the `GXVV <geosoft.gxapi.GXVV>`
        :param vv_tol:   Tolerances (1-5 values)
        :param title:    Title
        :param unit:     Unit
        :param x0:       X location (bottom left corner of graph)
        :param y0:       Y location
        :param xs:       Graph width
        :param ys:       Graph height
        :type  mview:    GXMVIEW
        :type  vv:       GXVV
        :type  log:      int
        :type  det_lim:  float
        :type  old:      int
        :type  vv_tol:   GXVV
        :type  title:    str
        :type  unit:     str
        :type  x0:       float
        :type  y0:       float
        :type  xs:       float
        :type  ys:       float

        .. versionadded:: 5.0.7

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_
        """
        gxapi_cy.WrapCHIMERA._duplicate_chem(GXContext._get_tls_geo(), mview, vv, log, det_lim, old, vv_tol, title.encode(), unit.encode(), x0, y0, xs, ys)
        



    @classmethod
    def duplicate_chem_view(cls, map, view, group, ipj, vv, log, det_lim, old, vv_tol, title, unit, vvx, vv_line, vv_fid, db, min_y, max_y):
        """
        Plot an ASSAY Duplicate result in a new view.
        
        :param map:      Map
        :param view:     New view name
        :param group:    New group name
        :param vv:       Duplicate data
        :param log:      Log-transform: 0 - linear, 1 - log
        :param det_lim:  Detect Limit
        :param old:      Number of old samples in the `GXVV <geosoft.gxapi.GXVV>`
        :param vv_tol:   Tolerances (1-5 values)
        :param title:    Title
        :param unit:     Unit
        :param vvx:      `GXVV <geosoft.gxapi.GXVV>` X
        :param vv_line:  `GXVV <geosoft.gxapi.GXVV>` Line
        :param vv_fid:   `GXVV <geosoft.gxapi.GXVV>` Fid
        :param db:       Database
        :param min_y:    Returned MinY
        :param max_y:    Returned MaxY
        :type  map:      GXMAP
        :type  view:     str
        :type  group:    str
        :type  ipj:      GXIPJ
        :type  vv:       GXVV
        :type  log:      int
        :type  det_lim:  float
        :type  old:      int
        :type  vv_tol:   GXVV
        :type  title:    str
        :type  unit:     str
        :type  vvx:      GXVV
        :type  vv_line:  GXVV
        :type  vv_fid:   GXVV
        :type  db:       GXDB
        :type  min_y:    float_ref
        :type  max_y:    float_ref

        .. versionadded:: 8.3

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_
        """
        min_y.value, max_y.value = gxapi_cy.WrapCHIMERA._duplicate_chem_view(GXContext._get_tls_geo(), map, view.encode(), group.encode(), ipj, vv, log, det_lim, old, vv_tol, title.encode(), unit.encode(), vvx, vv_line, vv_fid, db, min_y.value, max_y.value)
        



    @classmethod
    def get_expression_data_vv(cls, db, line, stage, exp, ini, gvv):
        """
        Get data from a line using a channel expression.
        
        :param db:     Database
        :param line:   Line to read
        :param stage:  Geochem stage (just "raw data stage" for now).
        :param exp:    Channel expression
        :param ini:    INI file name with required units (e.g. PARAMETER.CU="ppm") (optional)
        :param gvv:    Returned data
        :type  db:     GXDB
        :type  line:   int
        :type  stage:  str
        :type  exp:    str
        :type  ini:    str
        :type  gvv:    GXVV

        .. versionadded:: 6.4

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_

        **Note:** Input a channel expression. Units for individual channels
        are stored in the input INI. Returns a `GXVV <geosoft.gxapi.GXVV>` for the given line
        with the calculated expression values.
        """
        gxapi_cy.WrapCHIMERA._get_expression_data_vv(GXContext._get_tls_geo(), db, line, stage.encode(), exp.encode(), ini.encode(), gvv)
        



    @classmethod
    def get_lithogeochem_data(cls, db, lst, m_ch, vv_trans, remove_dummy_rows, vv_dummy, warn, vv_d, vv_line, vv_n, vv_used, vv_index, vv_fids, vv_fidi):
        """
        Get all rows of non-dummy data in a database.
        
        :param db:                 [i] database handle
        :param lst:                [i] channels of data to get
        :param m_ch:               [i] mask channel (can be `NULLSYMB <geosoft.gxapi.NULLSYMB>`)
        :param vv_trans:           [i] transforms to apply
        :param remove_dummy_rows:  [i] remove dummy rows?
        :param vv_dummy:           [i] dummy row if this channel value is dummy (0:No, 1:Yes)? Effective only if "remove dummy rows" value is TRUE
        :param warn:               [i] warn if rows removed because of dummy data items?
        :param vv_d:               [o] (INT) returned data - one `GXVV <geosoft.gxapi.GXVV>` handle per channel
        :param vv_line:            [o] line symbols selected
        :param vv_n:               [o] number of original data items in each line
        :param vv_used:            [o] number of non-dummy rows
        :param vv_index:           [o] indices into original data
        :param vv_fids:            [o] Fid Starts (REAL)
        :param vv_fidi:            [o] Fid Increments (REAL)
        :type  db:                 GXDB
        :type  lst:                GXLST
        :type  m_ch:               int
        :type  vv_trans:           GXVV
        :type  remove_dummy_rows:  int
        :type  vv_dummy:           GXVV
        :type  warn:               int
        :type  vv_d:               GXVV
        :type  vv_line:            GXVV
        :type  vv_n:               GXVV
        :type  vv_used:            GXVV
        :type  vv_index:           GXVV
        :type  vv_fids:            GXVV
        :type  vv_fidi:            GXVV

        .. versionadded:: 6.2

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_

        **Note:** This function is a quick way to get all rows
        of data, guaranteeing no dummy items.
        Book-keeping VVs returned let you easily
        write back results to new channels in the
        correct locations.
        Set the "Dummy Row" `GXVV <geosoft.gxapi.GXVV>` to 1 if you wish to
        remove any row where a value for the corresponding
        channel is a dummy.

        Transforms to apply:

        -1 - Channel default (will be either raw or log)
        0 - Raw Transform
        1 - Log transform: base e with log min = CHIMERA_LOG_MIN
        2 - Lambda transform
        """
        gxapi_cy.WrapCHIMERA._get_lithogeochem_data(GXContext._get_tls_geo(), db, lst, m_ch, vv_trans, remove_dummy_rows, vv_dummy, warn, vv_d, vv_line, vv_n, vv_used, vv_index, vv_fids, vv_fidi)
        



    @classmethod
    def get_transform(cls, db, chan, trans_opt, trans, lda):
        """
        Get channel transform options and lambda values.
        
        :param db:         `GXDB <geosoft.gxapi.GXDB>` handle
        :param chan:       Channel name
        :param trans_opt:  Transform option: -1, 0, 1 or 2
        :param trans:      Returned transform used
        :param lda:        Returned lambda value for option==2
        :type  db:         GXDB
        :type  chan:       str
        :type  trans_opt:  int
        :type  trans:      int_ref
        :type  lda:        float_ref

        .. versionadded:: 6.2

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_

        **Note:** If the lambda transform is requested, the channel
        must have the lambda value defined.

        Input Transform options

        -1 - Channel default (will be either raw or log)
        0 - Raw Transform
        1 - Log transform: base e with log min = CHIMERA_LOG_MIN
        2 - Lambda transform
        """
        trans.value, lda.value = gxapi_cy.WrapCHIMERA._get_transform(GXContext._get_tls_geo(), db, chan.encode(), trans_opt, trans.value, lda.value)
        



    @classmethod
    def is_acquire_chan(cls, input_chan, chan, units, factor, oxide):
        """
        Is this channel in acQuire format (e.g. "Ag_ppm_4AWR")
        
        :param input_chan:  String to test
        :param chan:        Returned channel name
        :param units:       Returned units
        :param factor:      Buffer factor (e.g. ppm = 1.e-6)
        :param oxide:       is this an oxide?
        :type  input_chan:  str
        :type  chan:        str_ref
        :type  units:       str_ref
        :type  factor:      float_ref
        :type  oxide:       bool_ref
        :rtype:             bool

        .. versionadded:: 7.2

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_

        **Note:** Expressions can take acQuire-type named channels
        if the exact element/oxide is not found. This function
        extracts the channel name, and units from an acQuire-formatted
        channel name.
        """
        ret_val, chan.value, units.value, factor.value, oxide.value = gxapi_cy.WrapCHIMERA._is_acquire_chan(GXContext._get_tls_geo(), input_chan.encode(), chan.value.encode(), units.value.encode(), factor.value, oxide.value)
        return ret_val



    @classmethod
    def is_element(cls, chan, case):
        """
        Tests a string to see if it is an element symbol
        
        :param chan:  String to test
        :param case:  :ref:`STR_CASE`
        :type  chan:  str
        :type  case:  int
        :rtype:       bool

        .. versionadded:: 5.0.7

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_

        **Note:** Suggested use - testing to see if a channel name is an
        element so that the "ASSAY" class can be set.
        """
        ret_val = gxapi_cy.WrapCHIMERA._is_element(GXContext._get_tls_geo(), chan.encode(), case)
        return ret_val



    @classmethod
    def launch_histogram(cls, db, chan):
        """
        Launch histogram tool on a database.
        
        :param db:    Database name
        :param chan:  First chan name
        :type  db:    str
        :type  chan:  str

        .. versionadded:: 5.0.6

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_

        **Note:** The database should be a currently open database.
        This function supercedes `GXEDB.launch_histogram <geosoft.gxapi.GXEDB.launch_histogram>`, (which now
        just gets the name of the `GXEDB <geosoft.gxapi.GXEDB>` and calls this function).
        """
        gxapi_cy.WrapCHIMERA._launch_histogram(GXContext._get_tls_geo(), db.encode(), chan.encode())
        



    @classmethod
    def launch_probability(cls, db, chan):
        """
        Launch probability tool on a database.
        
        :param db:    Database name
        :param chan:  First chan name
        :type  db:    str
        :type  chan:  str

        .. versionadded:: 5.1.8

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_

        **Note:** The database should be a currently open database.
        """
        gxapi_cy.WrapCHIMERA._launch_probability(GXContext._get_tls_geo(), db.encode(), chan.encode())
        



    @classmethod
    def launch_scatter(cls, db):
        """
        Launch scatter tool on a database.
        
        :param db:  Database name
        :type  db:  str

        .. versionadded:: 5.0.6

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_

        **Note:** The scatter tool uses the following INI parameters

        ================  ===============================================
        SCATTER.STM       name of the scatter template, "none" for none
        ----------------  -----------------------------------------------
        SCATTER.STM_NAME  name of last template section, "" for none.
        ----------------  -----------------------------------------------
        SCATTER.X         name of channel to display in X
        ----------------  -----------------------------------------------
        SCATTER.Y         name of channel to display in Y
        ----------------  -----------------------------------------------
        SCATTER.MASK      name of channel to use for mask
        ================  ===============================================

        The database should be a currently open database.
        This function supercedes `GXEDB.launch_scatter <geosoft.gxapi.GXEDB.launch_scatter>`, (which now
        just gets the name of the `GXEDB <geosoft.gxapi.GXEDB>` and calls this function).
        """
        gxapi_cy.WrapCHIMERA._launch_scatter(GXContext._get_tls_geo(), db.encode())
        



    @classmethod
    def launch_triplot(cls, db):
        """
        Launch Triplot tool on a database.
        
        :param db:  Database name
        :type  db:  str

        .. versionadded:: 5.0.7

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_

        **Note:** The Triplot tool uses the following INI parameters

        ================  ===============================================
        TRIPLOT.TTM       name of the triplot template, "none" for none
        ----------------  -----------------------------------------------
        TRIPLOT.TTM_NAME  name of last template section, "" for none.
        ----------------  -----------------------------------------------
        TRIPLOT.X         name of channel to display in X
        ----------------  -----------------------------------------------
        TRIPLOT.Y         name of channel to display in Y
        ----------------  -----------------------------------------------
        TRIPLOT.Z         name of channel to display in Z
        ----------------  -----------------------------------------------
        TRIPLOT.MASK      name of channel to use for mask
        ================  ===============================================

        The database should be a currently open database.
        """
        gxapi_cy.WrapCHIMERA._launch_triplot(GXContext._get_tls_geo(), db.encode())
        



    @classmethod
    def mask_chan_lst(cls, db, lst):
        """
        Load a `GXLST <geosoft.gxapi.GXLST>` with mask channels.
        
        :param db:   hDB - Database Object
        :param lst:  `GXLST <geosoft.gxapi.GXLST>` object to populate
        :type  db:   GXDB
        :type  lst:  GXLST

        .. versionadded:: 5.0.7

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_

        **Note:** Loads a `GXLST <geosoft.gxapi.GXLST>` with all channels with CLASS "MASK", as well
        as all channels containing the string "MASK", as long
        as the CLASS for these channels is not set to something
        other than "" or "MASK".

        This function has been duplicated by `GXDB.mask_chan_lst <geosoft.gxapi.GXDB.mask_chan_lst>`, which
        is safe to use in applications which do not have `GXCHIMERA <geosoft.gxapi.GXCHIMERA>` loaded.
        """
        gxapi_cy.WrapCHIMERA._mask_chan_lst(GXContext._get_tls_geo(), db, lst)
        



    @classmethod
    def ordered_channel_lst(cls, db, lst):
        """
        Fill a list with the channels in the preferred order.
        
        :param db:   hDB - Database Object
        :param lst:  `GXLST <geosoft.gxapi.GXLST>` object to populate [recommended 2*`STR_DB_SYMBOL <geosoft.gxapi.STR_DB_SYMBOL>`]
        :type  db:   GXDB
        :type  lst:  GXLST

        .. versionadded:: 5.1.8

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_

        **Note:** Loads a `GXLST <geosoft.gxapi.GXLST>` with all channels in the preferred order:

        First:  Sample, E, N, assay channels,
        Middle: Data from survey (other channels),
        Last:   Duplicate, Standard, Chemmask (and other masks), weight, lab, batch

        If the input `GXLST <geosoft.gxapi.GXLST>` object has values, it is used as the channel `GXLST <geosoft.gxapi.GXLST>`,
        otherwise, get all the database channels. (This allows you to pass in
        the currently displayed channels and only reload those).
        """
        gxapi_cy.WrapCHIMERA._ordered_channel_lst(GXContext._get_tls_geo(), db, lst)
        



    @classmethod
    def pie_plot(cls, mview, data_group, offset_group, xvv, yvv, dvv, cvv, col, offset, offset_size, radius):
        """
        Plot a Pie plot of up to 8 channels.
        
        :param mview:         View object to plot to
        :param data_group:    Data group name
        :param offset_group:  Offset group name
        :param xvv:           X locations
        :param yvv:           Y locations
        :param dvv:           Data handles, stored as INT values
        :param cvv:           Colors
        :param col:           Color for edges
        :param offset:        Offset symbols (0: No, 1: Yes)
        :param offset_size:   Offset symbol size
        :param radius:        Pie plot radius in data units.
        :type  mview:         GXMVIEW
        :type  data_group:    str
        :type  offset_group:  str
        :type  xvv:           GXVV
        :type  yvv:           GXVV
        :type  dvv:           GXVV
        :type  cvv:           GXVV
        :type  col:           int
        :type  offset:        int
        :type  offset_size:   float
        :type  radius:        float

        .. versionadded:: 5.0.7

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_

        **Note:** The number of channels is taken from the Data handles `GXVV <geosoft.gxapi.GXVV>`.
        The values in each data `GXVV <geosoft.gxapi.GXVV>` are summed and the pie arc is
        is given by the percent contribution of each constituent.
        See the note on offset symbols in `rose_plot <geosoft.gxapi.GXCHIMERA.rose_plot>`
        """
        gxapi_cy.WrapCHIMERA._pie_plot(GXContext._get_tls_geo(), mview, data_group.encode(), offset_group.encode(), xvv, yvv, dvv, cvv, col, offset, offset_size, radius)
        



    @classmethod
    def pie_plot2(cls, mview, data_group, offset_group, xvv, yvv, dvv, cvv, col, offset, offset_size, radius, start_angle):
        """
        Same as `pie_plot <geosoft.gxapi.GXCHIMERA.pie_plot>`, with a starting angle.
        
        :param mview:         View object to plot to
        :param data_group:    Data group name
        :param offset_group:  Offset group name
        :param xvv:           X locations
        :param yvv:           Y locations
        :param dvv:           Data handles, stored as INT values
        :param cvv:           Colors
        :param col:           Color for edges
        :param offset:        Offset symbols (0: No, 1: Yes)
        :param offset_size:   Offset symbol size
        :param radius:        Pie plot radius in data units.
        :param start_angle:   Starting angle in degrees CCW from horizontal (`rDUMMY <geosoft.gxapi.rDUMMY>` gives 0.0)
        :type  mview:         GXMVIEW
        :type  data_group:    str
        :type  offset_group:  str
        :type  xvv:           GXVV
        :type  yvv:           GXVV
        :type  dvv:           GXVV
        :type  cvv:           GXVV
        :type  col:           int
        :type  offset:        int
        :type  offset_size:   float
        :type  radius:        float
        :type  start_angle:   float

        .. versionadded:: 5.1.5

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_

        **Note:** The starting angle is the location of the edge of the first pie
        slice, counted in degrees counter-clockwise from horizontal
        (3 o'clock). Zero degrees gives the same plot as `pie_plot <geosoft.gxapi.GXCHIMERA.pie_plot>`.
        """
        gxapi_cy.WrapCHIMERA._pie_plot2(GXContext._get_tls_geo(), mview, data_group.encode(), offset_group.encode(), xvv, yvv, dvv, cvv, col, offset, offset_size, radius, start_angle)
        



    @classmethod
    def plot_string_classified_symbols_legend_from_class_file(cls, mview, title, x, y_min, y_max, class_file, index_vv):
        """
        Plot legend for the string classified symbols
        
        :param mview:       Map view object
        :param title:       Title
        :param x:           Left side X location
        :param y_min:       Bottom Y bound
        :param y_max:       Top Y bound
        :param class_file:  Class file name (`GXTPAT <geosoft.gxapi.GXTPAT>`)
        :param index_vv:    Class indices (INT `GXVV <geosoft.gxapi.GXVV>`)
        :type  mview:       GXMVIEW
        :type  title:       str
        :type  x:           float
        :type  y_min:       float
        :type  y_max:       float
        :type  class_file:  str
        :type  index_vv:    GXVV

        .. versionadded:: 8.0.1

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_

        **Note:** Plot in a legend the classes in the class file found in the input class indices.
        """
        gxapi_cy.WrapCHIMERA._plot_string_classified_symbols_legend_from_class_file(GXContext._get_tls_geo(), mview, title.encode(), x, y_min, y_max, class_file.encode(), index_vv)
        



    @classmethod
    def atomic_weight(cls, element):
        """
        Return the atomic weight of a particular element.
        
        :param element:  Element name (case insensitive)
        :type  element:  str

        :returns:        The atomic weight of the given element.
        :rtype:          float

        .. versionadded:: 6.4.2

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_

        **Note:** If the input string is not an element symbol (elements in the range
        1-92, "H" to "U"), then returns a dummy (`GS_R8DM <geosoft.gxapi.GS_R8DM>`).
        """
        ret_val = gxapi_cy.WrapCHIMERA._atomic_weight(GXContext._get_tls_geo(), element.encode())
        return ret_val



    @classmethod
    def rose_plot(cls, mview, data_group, offset_group, xvv, yvv, dvv, cvv, col, offset, offset_size):
        """
        Plot a Rose plot of up to 8 channels.
        
        :param mview:         View object to plot to
        :param data_group:    Data group name
        :param offset_group:  Offset group name
        :param xvv:           X locations
        :param yvv:           Y locations
        :param dvv:           Data handles, stored as INT values
        :param cvv:           Colors
        :param col:           Color for edges
        :param offset:        Offset symbols (0: No, 1: Yes)
        :param offset_size:   Offset symbol size
        :type  mview:         GXMVIEW
        :type  data_group:    str
        :type  offset_group:  str
        :type  xvv:           GXVV
        :type  yvv:           GXVV
        :type  dvv:           GXVV
        :type  cvv:           GXVV
        :type  col:           int
        :type  offset:        int
        :type  offset_size:   float

        .. versionadded:: 5.0.7

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_

        **Note:** The number of channels is taken from the Data handles `GXVV <geosoft.gxapi.GXVV>`.
        The values in each data `GXVV <geosoft.gxapi.GXVV>` give the radius, in view units,
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
        gxapi_cy.WrapCHIMERA._rose_plot(GXContext._get_tls_geo(), mview, data_group.encode(), offset_group.encode(), xvv, yvv, dvv, cvv, col, offset, offset_size)
        



    @classmethod
    def rose_plot2(cls, mview, data_group, offset_group, xvv, yvv, dvv, cvv, col, offset, offset_size, start_angle):
        """
        Same as `rose_plot <geosoft.gxapi.GXCHIMERA.rose_plot>`, with a starting angle.
        
        :param mview:         View object to plot to
        :param data_group:    Data group name
        :param offset_group:  Offset group name
        :param xvv:           X locations
        :param yvv:           Y locations
        :param dvv:           Data handles, stored as INT values
        :param cvv:           Colors
        :param col:           Color for edges
        :param offset:        Offset symbols (0: No, 1: Yes)
        :param offset_size:   Offset symbol size
        :param start_angle:   Starting angle in degrees CCW from horizontal (`rDUMMY <geosoft.gxapi.rDUMMY>` gives 0.0)
        :type  mview:         GXMVIEW
        :type  data_group:    str
        :type  offset_group:  str
        :type  xvv:           GXVV
        :type  yvv:           GXVV
        :type  dvv:           GXVV
        :type  cvv:           GXVV
        :type  col:           int
        :type  offset:        int
        :type  offset_size:   float
        :type  start_angle:   float

        .. versionadded:: 5.1.5

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_

        **Note:** The starting angle is the location of the edge of the first pie
        slice, counted in degrees counter-clockwise from horizontal
        (3 o'clock). Zero degrees gives the same plot as `rose_plot <geosoft.gxapi.GXCHIMERA.rose_plot>`.
        """
        gxapi_cy.WrapCHIMERA._rose_plot2(GXContext._get_tls_geo(), mview, data_group.encode(), offset_group.encode(), xvv, yvv, dvv, cvv, col, offset, offset_size, start_angle)
        



    @classmethod
    def scatter2(cls, mview, title, x1, y1, width, height, horz_vv, vert_vv, sym_font, sym_num_vv, sym_siz_vv, sym_col_vv, annot_style, h_chan, v_chan, h_units, v_units, h_min, h_max, v_min, v_max, hr_min, hr_max, vr_min, vr_max, use_hr_min, use_hr_max, use_vr_min, use_vr_max, h_scaling, v_scaling):
        """
        Plot the scatter plot on a map using symbol number, size and color VVs.
        
        :param mview:        View
        :param title:        Title
        :param x1:           X location (bottom left corner of box)
        :param y1:           Y location
        :param width:        Box width
        :param height:       Box height
        :param horz_vv:      Horizontal channel
        :param vert_vv:      Vertical channel
        :param sym_font:     Decorated font name, "" for default symbol font (normally symbols.gfn)
        :param sym_num_vv:   Symbol numbers
        :param sym_siz_vv:   Symbol sizes
        :param sym_col_vv:   Colors  if symbol number or Color == 0, do not plot
        :param annot_style:  Annotation style 0 - outside, 1 - inside
        :param h_chan:       Horizontal channel name
        :param v_chan:       Vertical channel name
        :param h_units:      Horizontal channel units
        :param v_units:      Vertical channel units
        :param h_min:        Min. Horizontal value, `rDUMMY <geosoft.gxapi.rDUMMY>` for default
        :param h_max:        Max. Horizontal value
        :param v_min:        Min. Vertical value
        :param v_max:        Max. Vertical value
        :param hr_min:       Min. Horizontal range value
        :param hr_max:       Max. Horizontal range value
        :param vr_min:       Min. Vertical range value
        :param vr_max:       Max. Vertical range value
        :param use_hr_min:   Use Min Horz. Range selection?
        :param use_hr_max:   Use Max Horz. Range selection?
        :param use_vr_min:   Use Min Vert. Range selection?
        :param use_vr_max:   Use Max Vert. Range selection?
        :param h_scaling:    Horizontal axis scaling: 0 - linear, 1 - log
        :param v_scaling:    Vertical axis scaling: 0 - linear, 1 - log
        :type  mview:        GXMVIEW
        :type  title:        str
        :type  x1:           float
        :type  y1:           float
        :type  width:        float
        :type  height:       float
        :type  horz_vv:      GXVV
        :type  vert_vv:      GXVV
        :type  sym_font:     str
        :type  sym_num_vv:   GXVV
        :type  sym_siz_vv:   GXVV
        :type  sym_col_vv:   GXVV
        :type  annot_style:  int
        :type  h_chan:       str
        :type  v_chan:       str
        :type  h_units:      str
        :type  v_units:      str
        :type  h_min:        float
        :type  h_max:        float
        :type  v_min:        float
        :type  v_max:        float
        :type  hr_min:       float
        :type  hr_max:       float
        :type  vr_min:       float
        :type  vr_max:       float
        :type  use_hr_min:   int
        :type  use_hr_max:   int
        :type  use_vr_min:   int
        :type  use_vr_max:   int
        :type  h_scaling:    int
        :type  v_scaling:    int

        .. versionadded:: 5.0.7

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_

        **Note:** The view scaling is not altered with any projection. The base view
        is best as the input.
        """
        gxapi_cy.WrapCHIMERA._scatter2(GXContext._get_tls_geo(), mview, title.encode(), x1, y1, width, height, horz_vv, vert_vv, sym_font.encode(), sym_num_vv, sym_siz_vv, sym_col_vv, annot_style, h_chan.encode(), v_chan.encode(), h_units.encode(), v_units.encode(), h_min, h_max, v_min, v_max, hr_min, hr_max, vr_min, vr_max, use_hr_min, use_hr_max, use_vr_min, use_vr_max, h_scaling, v_scaling)
        



    @classmethod
    def fixed_symbol_scatter_plot(cls, mview, title, x1, y1, width, height, x_vv, y_vv, m_vv, mask_col, symbol_font, symbol_number, symbol_size, symbol_angle, symbol_color, symbol_fill, db, line_vv, fid_vv, annotn, x_chan, y_chan, x_units, y_units, x_min, x_max, y_min, y_max, x_lin, y_lin, overlay):
        """
        Plot a scatter plot using a single fixed symbol.
        Optional data masking with masking Color.
        Optional database linking.
        
        :param mview:          View
        :param title:          Title
        :param x1:             X location (bottom left corner of box)
        :param y1:             Y location
        :param width:          Box width
        :param height:         Box height
        :param x_vv:           Horizontal channel data
        :param y_vv:           Vertical channel data
        :param m_vv:           Mask channel data (can be NULL)
        :param mask_col:       Mask Color; overrides symbol Color where mask data is not dummy. Pass an empty string to `GXMVIEW.color <geosoft.gxapi.GXMVIEW.color>` for no plot.
        :param symbol_font:    Decorated font name, "" for default symbol font (normally symbols.gfn)
        :param symbol_number:  Symbol number (>=0)
        :param symbol_size:    Symbol size ( >=0)
        :param symbol_angle:   Symbol angle (-360 to 360)
        :param symbol_color:   Symbol Color
        :param symbol_fill:    Symbol fill Color
        :param db:             Database (source of data)
        :param line_vv:        Line handles for data
        :param fid_vv:         Fid values for data
        :param annotn:         Annotation style 0 - outside, 1 - inside
        :param x_chan:         Horizontal channel name
        :param y_chan:         Vertical channel name
        :param x_units:        Horizontal channel units
        :param y_units:        Vertical channel units
        :param x_min:          Min. Horizontal value, `rDUMMY <geosoft.gxapi.rDUMMY>` for default
        :param x_max:          Max. Horizontal value
        :param y_min:          Min. Vertical value
        :param y_max:          Max. Vertical value
        :param x_lin:          Horizontal axis scaling: 0 - linear, 1 - log
        :param y_lin:          Vertical axis scaling
        :param overlay:        Plot overlay ("" for none)
        :type  mview:          GXMVIEW
        :type  title:          str
        :type  x1:             float
        :type  y1:             float
        :type  width:          float
        :type  height:         float
        :type  x_vv:           GXVV
        :type  y_vv:           GXVV
        :type  m_vv:           GXVV
        :type  mask_col:       int
        :type  symbol_font:    str
        :type  symbol_number:  int
        :type  symbol_size:    float
        :type  symbol_angle:   float
        :type  symbol_color:   int
        :type  symbol_fill:    int
        :type  db:             GXDB
        :type  line_vv:        GXVV
        :type  fid_vv:         GXVV
        :type  annotn:         int
        :type  x_chan:         str
        :type  y_chan:         str
        :type  x_units:        str
        :type  y_units:        str
        :type  x_min:          float
        :type  x_max:          float
        :type  y_min:          float
        :type  y_max:          float
        :type  x_lin:          int
        :type  y_lin:          int
        :type  overlay:        str

        .. versionadded:: 8.0.1

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_

        **Note:** Plot a scatter plot using a single fixed symbol.
        """
        gxapi_cy.WrapCHIMERA._fixed_symbol_scatter_plot(GXContext._get_tls_geo(), mview, title.encode(), x1, y1, width, height, x_vv, y_vv, m_vv, mask_col, symbol_font.encode(), symbol_number, symbol_size, symbol_angle, symbol_color, symbol_fill, db, line_vv, fid_vv, annotn, x_chan.encode(), y_chan.encode(), x_units.encode(), y_units.encode(), x_min, x_max, y_min, y_max, x_lin, y_lin, overlay.encode())
        



    @classmethod
    def zone_coloured_scatter_plot(cls, mview, title, x1, y1, width, height, x_vv, y_vv, m_vv, mask_col, zone_data_vv, zone_file, symbol_font, symbol_number, symbol_size, symbol_angle, symbol_color, symbol_fill, fix_edge_color, db, line_vv, fid_vv, annotn, x_chan, y_chan, x_units, y_units, x_min, x_max, y_min, y_max, x_lin, y_lin, overlay):
        """
        Plot a scatter plot using colors based on a zone file.
        Optional data masking with masking color.
        Optional database linking.
        
        :param mview:           View
        :param title:           Title
        :param x1:              X location (bottom left corner of box)
        :param y1:              Y location
        :param width:           Box width
        :param height:          Box height
        :param x_vv:            Horizontal channel data
        :param y_vv:            Vertical channel data
        :param m_vv:            Mask channel data (can be NULL)
        :param mask_col:        Mask color; overrides symbol color where mask data is not dummy. Pass an empty string to `GXMVIEW.color <geosoft.gxapi.GXMVIEW.color>` for no plot.
        :param zone_data_vv:    Zone channel data
        :param zone_file:       Zone file name
        :param symbol_font:     Decorated font name, "" for default symbol font (normally symbols.gfn)
        :param symbol_number:   Symbol number (>=0)
        :param symbol_size:     Symbol size ( >=0)
        :param symbol_angle:    Symbol angle (-360 to 360)
        :param symbol_color:    Symbol color
        :param symbol_fill:     Symbol fill color
        :param fix_edge_color:  Fix symbol edge color?
        :param db:              Database (source of data)
        :param line_vv:         Line handles for data
        :param fid_vv:          Fid values for data
        :param annotn:          Annotation style 0 - outside, 1 - inside
        :param x_chan:          Horizontal channel name
        :param y_chan:          Vertical channel name
        :param x_units:         Horizontal channel units
        :param y_units:         Vertical channel units
        :param x_min:           Min. Horizontal value, `rDUMMY <geosoft.gxapi.rDUMMY>` for default
        :param x_max:           Max. Horizontal value
        :param y_min:           Min. Vertical value
        :param y_max:           Max. Vertical value
        :param x_lin:           Horizontal axis scaling: 0 - linear, 1 - log
        :param y_lin:           Vertical axis scaling
        :param overlay:         Plot overlay ("" for none)
        :type  mview:           GXMVIEW
        :type  title:           str
        :type  x1:              float
        :type  y1:              float
        :type  width:           float
        :type  height:          float
        :type  x_vv:            GXVV
        :type  y_vv:            GXVV
        :type  m_vv:            GXVV
        :type  mask_col:        int
        :type  zone_data_vv:    GXVV
        :type  zone_file:       str
        :type  symbol_font:     str
        :type  symbol_number:   int
        :type  symbol_size:     float
        :type  symbol_angle:    float
        :type  symbol_color:    int
        :type  symbol_fill:     int
        :type  fix_edge_color:  int
        :type  db:              GXDB
        :type  line_vv:         GXVV
        :type  fid_vv:          GXVV
        :type  annotn:          int
        :type  x_chan:          str
        :type  y_chan:          str
        :type  x_units:         str
        :type  y_units:         str
        :type  x_min:           float
        :type  x_max:           float
        :type  y_min:           float
        :type  y_max:           float
        :type  x_lin:           int
        :type  y_lin:           int
        :type  overlay:         str

        .. versionadded:: 8.0.1

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_

        **Note:** Plot a scatter plot using colors based on a zone file.
        """
        gxapi_cy.WrapCHIMERA._zone_coloured_scatter_plot(GXContext._get_tls_geo(), mview, title.encode(), x1, y1, width, height, x_vv, y_vv, m_vv, mask_col, zone_data_vv, zone_file.encode(), symbol_font.encode(), symbol_number, symbol_size, symbol_angle, symbol_color, symbol_fill, fix_edge_color, db, line_vv, fid_vv, annotn, x_chan.encode(), y_chan.encode(), x_units.encode(), y_units.encode(), x_min, x_max, y_min, y_max, x_lin, y_lin, overlay.encode())
        



    @classmethod
    def string_classified_scatter_plot(cls, mview, title, x1, y1, width, height, x_vv, y_vv, m_vv, mask_col, class_vv, class_file, symbol_size_override, db, line_vv, fid_vv, annotn, x_chan, y_chan, x_units, y_units, x_min, x_max, y_min, y_max, x_lin, y_lin, overlay):
        """
        Plot a scatter plot using symbols based on a symbol class file.
        Optional data masking with masking color.
        Optional database linking.
        
        :param mview:                 View
        :param title:                 Title
        :param x1:                    X location (bottom left corner of box)
        :param y1:                    Y location
        :param width:                 Box width
        :param height:                Box height
        :param x_vv:                  Horizontal channel data
        :param y_vv:                  Vertical channel data
        :param m_vv:                  Mask channel data
        :param mask_col:              Mask color; overrides symbol color. Pass an empty string to `GXMVIEW.color <geosoft.gxapi.GXMVIEW.color>` for no plot.
        :param class_vv:              Class channel data
        :param class_file:            Class file (`GXTPAT <geosoft.gxapi.GXTPAT>`) name.
        :param symbol_size_override:  Symbol size override. Set to 0.0 to use class file symbol sizes.
        :param db:                    Database (source of data)
        :param line_vv:               Line handles for data
        :param fid_vv:                Fid values for data
        :param annotn:                Annotation style 0 - outside, 1 - inside
        :param x_chan:                Horizontal channel name
        :param y_chan:                Vertical channel name
        :param x_units:               Horizontal channel units
        :param y_units:               Vertical channel units
        :param x_min:                 Min. Horizontal value, `rDUMMY <geosoft.gxapi.rDUMMY>` for default
        :param x_max:                 Max. Horizontal value
        :param y_min:                 Min. Vertical value
        :param y_max:                 Max. Vertical value
        :param x_lin:                 Horizontal axis scaling: 0 - linear, 1 - log
        :param y_lin:                 Vertical axis scaling
        :param overlay:               Plot overlay ("" for none)
        :type  mview:                 GXMVIEW
        :type  title:                 str
        :type  x1:                    float
        :type  y1:                    float
        :type  width:                 float
        :type  height:                float
        :type  x_vv:                  GXVV
        :type  y_vv:                  GXVV
        :type  m_vv:                  GXVV
        :type  mask_col:              int
        :type  class_vv:              GXVV
        :type  class_file:            str
        :type  symbol_size_override:  float
        :type  db:                    GXDB
        :type  line_vv:               GXVV
        :type  fid_vv:                GXVV
        :type  annotn:                int
        :type  x_chan:                str
        :type  y_chan:                str
        :type  x_units:               str
        :type  y_units:               str
        :type  x_min:                 float
        :type  x_max:                 float
        :type  y_min:                 float
        :type  y_max:                 float
        :type  x_lin:                 int
        :type  y_lin:                 int
        :type  overlay:               str

        .. versionadded:: 8.0.1

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_

        **Note:** Plot a scatter plot using symbols based on a symbol class file.
        """
        gxapi_cy.WrapCHIMERA._string_classified_scatter_plot(GXContext._get_tls_geo(), mview, title.encode(), x1, y1, width, height, x_vv, y_vv, m_vv, mask_col, class_vv, class_file.encode(), symbol_size_override, db, line_vv, fid_vv, annotn, x_chan.encode(), y_chan.encode(), x_units.encode(), y_units.encode(), x_min, x_max, y_min, y_max, x_lin, y_lin, overlay.encode())
        



    @classmethod
    def set_lithogeochem_data(cls, db, lst, vv_d, vv_line, vv_n, vv_used, vv_index, vv_fids, vv_fidi, vv_dummy):
        """
        Set data back into a database.
        
        :param db:        [i] database handle
        :param lst:       [i] channels of data to set
        :param vv_d:      [i] (INT) input data - one `GXVV <geosoft.gxapi.GXVV>` handle per channel
        :param vv_line:   [i] line symbols selected
        :param vv_n:      [i] number of original data items in each line
        :param vv_used:   [i] number of non-dummy rows
        :param vv_index:  [i] indices into original data
        :param vv_fids:   [i] Fid Starts (REAL)
        :param vv_fidi:   [i] Fid Increments (REAL)
        :param vv_dummy:  [i] init channel values to dummies first (0:No, 1:Yes)?
        :type  db:        GXDB
        :type  lst:       GXLST
        :type  vv_d:      GXVV
        :type  vv_line:   GXVV
        :type  vv_n:      GXVV
        :type  vv_used:   GXVV
        :type  vv_index:  GXVV
        :type  vv_fids:   GXVV
        :type  vv_fidi:   GXVV
        :type  vv_dummy:  GXVV

        .. versionadded:: 6.2

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_

        **Note:** This function would normally be called after
        AAGetLithogeochemData_CHIMERA to write processed values
        back into a database, in the correct lines,
        and in the correct fiducial locations wrt the
        other data. The book-keeping VVs would all be
        set up in AAGetLithogeochemData_CHIMERA.

        Values NOT in the data (missing indices) will
        be initialized to dummy if the channel is new,
        or if the value in the last `GXVV <geosoft.gxapi.GXVV>` below is set to 1.

        New channel types will be set using the data `GXVV <geosoft.gxapi.GXVV>` type.
        Any metadata (CLASS, display formats) should be set separately.
        """
        gxapi_cy.WrapCHIMERA._set_lithogeochem_data(GXContext._get_tls_geo(), db, lst, vv_d, vv_line, vv_n, vv_used, vv_index, vv_fids, vv_fidi, vv_dummy)
        



    @classmethod
    def stacked_bar_plot(cls, mview, data_group, offset_group, xvv, yvv, dvv, cvv, col, offset, offset_size, width):
        """
        Plot a Bar plot of up to 8 channels, bars stacked on each other.
        
        :param mview:         View object to plot to
        :param data_group:    Data group name
        :param offset_group:  Offset group name
        :param xvv:           X locations
        :param yvv:           Y locations
        :param dvv:           Data handles, stored as INT values
        :param cvv:           Colors
        :param col:           Color for edges
        :param offset:        Offset symbols (0: No, 1: Yes)
        :param offset_size:   Offset symbol size
        :param width:         Single bar width in data units.
        :type  mview:         GXMVIEW
        :type  data_group:    str
        :type  offset_group:  str
        :type  xvv:           GXVV
        :type  yvv:           GXVV
        :type  dvv:           GXVV
        :type  cvv:           GXVV
        :type  col:           int
        :type  offset:        int
        :type  offset_size:   float
        :type  width:         float

        .. versionadded:: 5.1.8

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_

        **Note:** The number of channels is taken from the Data handles `GXVV <geosoft.gxapi.GXVV>`.
        Plots a bar plot with the center of the "X" axis at the symbol location.
        See the note on offset symbols in `rose_plot <geosoft.gxapi.GXCHIMERA.rose_plot>`
        """
        gxapi_cy.WrapCHIMERA._stacked_bar_plot(GXContext._get_tls_geo(), mview, data_group.encode(), offset_group.encode(), xvv, yvv, dvv, cvv, col, offset, offset_size, width)
        



    @classmethod
    def standard(cls, mview, vv, old, tol, min, max, title, unit, x0, y0, xs, ys):
        """
        Plot ASSAY Standard result in a graph window.
        
        :param mview:  View
        :param vv:     Standard data
        :param old:    Number of old samples in the `GXVV <geosoft.gxapi.GXVV>`
        :param tol:    Tolerance as a function of std dev
        :param min:    Minimum acceptable value
        :param max:    Maximum acceptable value
        :param title:  Title
        :param unit:   Unit
        :param x0:     X location (bottom left corner of graph)
        :param y0:     Y location
        :param xs:     Graph width
        :param ys:     Graph height
        :type  mview:  GXMVIEW
        :type  vv:     GXVV
        :type  old:    int
        :type  tol:    float
        :type  min:    float
        :type  max:    float
        :type  title:  str
        :type  unit:   str
        :type  x0:     float
        :type  y0:     float
        :type  xs:     float
        :type  ys:     float

        .. versionadded:: 5.0.7

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_

        **Note:** If the tolerance is `rDUMMY <geosoft.gxapi.rDUMMY>`, then the minimum and maximum
        values are used, and must be specified.
        """
        gxapi_cy.WrapCHIMERA._standard(GXContext._get_tls_geo(), mview, vv, old, tol, min, max, title.encode(), unit.encode(), x0, y0, xs, ys)
        



    @classmethod
    def standard_view(cls, map, view, group, ipj, vvy, old, tol, min, max, title, unit, xs, vvx, vv_line, vv_fid, db, min_y, max_y):
        """
        Plot ASSAY Standard result in a graph window.
        
        :param map:      Map
        :param view:     New view name
        :param group:    New group name
        :param vvy:      Standard data (`GXVV <geosoft.gxapi.GXVV>` Y)
        :param old:      Number of old samples in the `GXVV <geosoft.gxapi.GXVV>`
        :param tol:      Tolerance as a function of std dev
        :param min:      Minimum acceptable value
        :param max:      Maximum acceptable value
        :param title:    Title
        :param unit:     Unit
        :param xs:       Size X
        :param vvx:      `GXVV <geosoft.gxapi.GXVV>` X
        :param vv_line:  `GXVV <geosoft.gxapi.GXVV>` Line
        :param vv_fid:   `GXVV <geosoft.gxapi.GXVV>` Fid
        :param db:       Database
        :param min_y:    Returned MinY
        :param max_y:    Returned MaxY
        :type  map:      GXMAP
        :type  view:     str
        :type  group:    str
        :type  ipj:      GXIPJ
        :type  vvy:      GXVV
        :type  old:      int
        :type  tol:      float
        :type  min:      float
        :type  max:      float
        :type  title:    str
        :type  unit:     str
        :type  xs:       float
        :type  vvx:      GXVV
        :type  vv_line:  GXVV
        :type  vv_fid:   GXVV
        :type  db:       GXDB
        :type  min_y:    float_ref
        :type  max_y:    float_ref

        .. versionadded:: 8.3

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_

        **Note:** Same as `standard <geosoft.gxapi.GXCHIMERA.standard>` but plot in a new view.
        """
        min_y.value, max_y.value = gxapi_cy.WrapCHIMERA._standard_view(GXContext._get_tls_geo(), map, view.encode(), group.encode(), ipj, vvy, old, tol, min, max, title.encode(), unit.encode(), xs, vvx, vv_line, vv_fid, db, min_y.value, max_y.value)
        



    @classmethod
    def tri_plot2(cls, mview, title, x1, y1, width, height, x_vv, y_vv, z_vv, m_vv, sym_font, sym_num_vv, sym_siz_vv, sym_col_vv, x_chan, y_chan, z_chan, xr_min, xr_max, yr_min, yr_max, zr_min, zr_max, use_xr_min, use_xr_max, use_yr_min, use_yr_max, use_zr_min, use_zr_max, grid, tic, grid_inc):
        """
        Plot the TriPlot on a map using symbol number, size and color VVs.
        
        :param mview:       View
        :param title:       Title
        :param x1:          X location (bottom left corner of box)
        :param y1:          Y location
        :param width:       Box width
        :param height:      Box height
        :param x_vv:        X channel
        :param y_vv:        Y channel
        :param z_vv:        Z channel
        :param m_vv:        Mask channel
        :param sym_font:    Decorated font name, "" for default symbol font (normally symbols.gfn)
        :param sym_num_vv:  Symbol numbers
        :param sym_siz_vv:  Symbol sizes
        :param sym_col_vv:  Colors  if symbol number or color == 0, do not plot
        :param x_chan:      X channel name
        :param y_chan:      Y channel name
        :param z_chan:      Z channel name
        :param xr_min:      Min. X range value
        :param xr_max:      Max. X range value
        :param yr_min:      Min. Y range value
        :param yr_max:      Max. Y range value
        :param zr_min:      Min. Z range value
        :param zr_max:      Max. Z range value
        :param use_xr_min:  Use Min X Range selection?
        :param use_xr_max:  Use Max X Range selection?
        :param use_yr_min:  Use Min Y Range selection?
        :param use_yr_max:  Use Max Y Range selection?
        :param use_zr_min:  Use Min Z Range selection?
        :param use_zr_max:  Use Max Z Range selection?
        :param grid:        Plot Grid lines? (0: Just outside edge tics, 1: Grid lines).
        :param tic:         Tic Increment (in percent)
        :param grid_inc:    Grid increment (in percent)
        :type  mview:       GXMVIEW
        :type  title:       str
        :type  x1:          float
        :type  y1:          float
        :type  width:       float
        :type  height:      float
        :type  x_vv:        GXVV
        :type  y_vv:        GXVV
        :type  z_vv:        GXVV
        :type  m_vv:        GXVV
        :type  sym_font:    str
        :type  sym_num_vv:  GXVV
        :type  sym_siz_vv:  GXVV
        :type  sym_col_vv:  GXVV
        :type  x_chan:      str
        :type  y_chan:      str
        :type  z_chan:      str
        :type  xr_min:      float
        :type  xr_max:      float
        :type  yr_min:      float
        :type  yr_max:      float
        :type  zr_min:      float
        :type  zr_max:      float
        :type  use_xr_min:  int
        :type  use_xr_max:  int
        :type  use_yr_min:  int
        :type  use_yr_max:  int
        :type  use_zr_min:  int
        :type  use_zr_max:  int
        :type  grid:        int
        :type  tic:         float
        :type  grid_inc:    float

        .. versionadded:: 5.1.6

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_

        **Note:** The mask channel `GXVV <geosoft.gxapi.GXVV>` is used for plotting precedence; those points with
        mask = dummy are plotted first, then overwritten with the non-masked
        values, so you don't get "good" points being covered up by masked values.
        The view scaling is not altered with any projection. The base view
        is best as the input.
        """
        gxapi_cy.WrapCHIMERA._tri_plot2(GXContext._get_tls_geo(), mview, title.encode(), x1, y1, width, height, x_vv, y_vv, z_vv, m_vv, sym_font.encode(), sym_num_vv, sym_siz_vv, sym_col_vv, x_chan.encode(), y_chan.encode(), z_chan.encode(), xr_min, xr_max, yr_min, yr_max, zr_min, zr_max, use_xr_min, use_xr_max, use_yr_min, use_yr_max, use_zr_min, use_zr_max, grid, tic, grid_inc)
        



    @classmethod
    def fixed_symbol_tri_plot(cls, mview, title, x1, y1, side, x_vv, y_vv, z_vv, m_vv, mask_col, symbol_font, symbol_number, symbol_size, symbol_angle, symbol_color, symbol_fill, db, line_vv, fid_vv, x_chan, y_chan, z_chan, grid, tic, grid_inc, overlay):
        """
        Plot a tri-plot using a single fixed symbol.
        Optional data masking with masking color.
        Optional database linking.
        
        :param mview:          View
        :param title:          Title
        :param x1:             X location (bottom left corner of box)
        :param y1:             Y location
        :param side:           Triangle side length
        :param x_vv:           X channel data
        :param y_vv:           Y channel data
        :param z_vv:           Z channel data
        :param m_vv:           Mask channel data
        :param mask_col:       Mask color; overrides symbol color where mask data is not dummy. Pass an empty string to `GXMVIEW.color <geosoft.gxapi.GXMVIEW.color>` for no plot.
        :param symbol_font:    Decorated font name, "" for default symbol font (normally symbols.gfn)
        :param symbol_number:  Symbol number (>=0)
        :param symbol_size:    Symbol size ( >=0)
        :param symbol_angle:   Symbol angle (-360 to 360)
        :param symbol_color:   Symbol color
        :param symbol_fill:    Symbol fill color
        :param db:             Database (source of data)
        :param line_vv:        Line handles for data
        :param fid_vv:         Fid values for data
        :param x_chan:         X channel name
        :param y_chan:         Y channel name
        :param z_chan:         Z channel name
        :param grid:           Plot Grid lines? (0: Just outside edge tics, 1: Grid lines).
        :param tic:            Tic Increment (in percent)
        :param grid_inc:       Grid increment (in percent)
        :param overlay:        Plot overlay ("" for none)
        :type  mview:          GXMVIEW
        :type  title:          str
        :type  x1:             float
        :type  y1:             float
        :type  side:           float
        :type  x_vv:           GXVV
        :type  y_vv:           GXVV
        :type  z_vv:           GXVV
        :type  m_vv:           GXVV
        :type  mask_col:       int
        :type  symbol_font:    str
        :type  symbol_number:  int
        :type  symbol_size:    float
        :type  symbol_angle:   float
        :type  symbol_color:   int
        :type  symbol_fill:    int
        :type  db:             GXDB
        :type  line_vv:        GXVV
        :type  fid_vv:         GXVV
        :type  x_chan:         str
        :type  y_chan:         str
        :type  z_chan:         str
        :type  grid:           int
        :type  tic:            float
        :type  grid_inc:       float
        :type  overlay:        str

        .. versionadded:: 8.0.1

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_

        **Note:** Plot a tri plot using a single fixed symbol.
        """
        gxapi_cy.WrapCHIMERA._fixed_symbol_tri_plot(GXContext._get_tls_geo(), mview, title.encode(), x1, y1, side, x_vv, y_vv, z_vv, m_vv, mask_col, symbol_font.encode(), symbol_number, symbol_size, symbol_angle, symbol_color, symbol_fill, db, line_vv, fid_vv, x_chan.encode(), y_chan.encode(), z_chan.encode(), grid, tic, grid_inc, overlay.encode())
        



    @classmethod
    def zone_coloured_tri_plot(cls, mview, title, x1, y1, side, x_vv, y_vv, z_vv, m_vv, mask_col, zone_data_vv, zone_file, symbol_font, symbol_number, symbol_size, symbol_angle, symbol_color, symbol_fill, fix_edge_color, db, line_vv, fid_vv, x_chan, y_chan, z_chan, grid, tic, grid_inc, overlay):
        """
        Plot a tri-plot using colors based on a zone file.
        Optional data masking with masking color.
        Optional database linking.
        
        :param mview:           View
        :param title:           Title
        :param x1:              X location (bottom left corner of box)
        :param y1:              Y location
        :param side:            Triangle side length
        :param x_vv:            X channel data
        :param y_vv:            Y channel data
        :param z_vv:            Z channel data
        :param m_vv:            Mask channel data
        :param mask_col:        Mask color; overrides symbol color where mask data is not dummy. Pass an empty string to `GXMVIEW.color <geosoft.gxapi.GXMVIEW.color>` for no plot.
        :param zone_data_vv:    Zone channel data
        :param zone_file:       Zone file name
        :param symbol_font:     Decorated font name, "" for default symbol font (normally symbols.gfn)
        :param symbol_number:   Symbol number (>=0)
        :param symbol_size:     Symbol size ( >=0)
        :param symbol_angle:    Symbol angle (-360 to 360)
        :param symbol_color:    Symbol color
        :param symbol_fill:     Symbol fill color
        :param fix_edge_color:  Fix symbol edge color?
        :param db:              Database (source of data)
        :param line_vv:         Line handles for data
        :param fid_vv:          Fid values for data
        :param x_chan:          X channel name
        :param y_chan:          Y channel name
        :param z_chan:          Z channel name
        :param grid:            Plot Grid lines? (0: Just outside edge tics, 1: Grid lines).
        :param tic:             Tic Increment (in percent)
        :param grid_inc:        Grid increment (in percent)
        :param overlay:         Plot overlay ("" for none)
        :type  mview:           GXMVIEW
        :type  title:           str
        :type  x1:              float
        :type  y1:              float
        :type  side:            float
        :type  x_vv:            GXVV
        :type  y_vv:            GXVV
        :type  z_vv:            GXVV
        :type  m_vv:            GXVV
        :type  mask_col:        int
        :type  zone_data_vv:    GXVV
        :type  zone_file:       str
        :type  symbol_font:     str
        :type  symbol_number:   int
        :type  symbol_size:     float
        :type  symbol_angle:    float
        :type  symbol_color:    int
        :type  symbol_fill:     int
        :type  fix_edge_color:  int
        :type  db:              GXDB
        :type  line_vv:         GXVV
        :type  fid_vv:          GXVV
        :type  x_chan:          str
        :type  y_chan:          str
        :type  z_chan:          str
        :type  grid:            int
        :type  tic:             float
        :type  grid_inc:        float
        :type  overlay:         str

        .. versionadded:: 8.0.1

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_

        **Note:** Plot a tri plot using colors based on a zone file.
        """
        gxapi_cy.WrapCHIMERA._zone_coloured_tri_plot(GXContext._get_tls_geo(), mview, title.encode(), x1, y1, side, x_vv, y_vv, z_vv, m_vv, mask_col, zone_data_vv, zone_file.encode(), symbol_font.encode(), symbol_number, symbol_size, symbol_angle, symbol_color, symbol_fill, fix_edge_color, db, line_vv, fid_vv, x_chan.encode(), y_chan.encode(), z_chan.encode(), grid, tic, grid_inc, overlay.encode())
        



    @classmethod
    def string_classified_tri_plot(cls, mview, title, x1, y1, side, x_vv, y_vv, z_vv, m_vv, mask_col, class_vv, class_file, symbol_size_override, db, line_vv, fid_vv, x_chan, y_chan, z_chan, grid, tic, grid_inc, overlay):
        """
        Plot a tri-plot using symbols based on a symbol class file.
        Optional data masking with masking color.
        Optional database linking.
        
        :param mview:                 View
        :param title:                 Title
        :param x1:                    X location (bottom left corner of box)
        :param y1:                    Y location
        :param side:                  Triangle side length
        :param x_vv:                  X channel data
        :param y_vv:                  Y channel data
        :param z_vv:                  Z channel data
        :param m_vv:                  Mask channel data
        :param mask_col:              Mask color; overrides symbol color. Pass an empty string to `GXMVIEW.color <geosoft.gxapi.GXMVIEW.color>` for no plot.
        :param class_vv:              Class channel data
        :param class_file:            Class file (`GXTPAT <geosoft.gxapi.GXTPAT>`) name.
        :param symbol_size_override:  Symbol size override. Set to 0.0 to use class file symbol sizes.
        :param db:                    Database (source of data)
        :param line_vv:               Line handles for data
        :param fid_vv:                Fid values for data
        :param x_chan:                X channel name
        :param y_chan:                Y channel name
        :param z_chan:                Z channel name
        :param grid:                  Plot Grid lines? (0: Just outside edge tics, 1: Grid lines).
        :param tic:                   Tic Increment (in percent)
        :param grid_inc:              Grid increment (in percent)
        :param overlay:               Plot overlay ("" for none)
        :type  mview:                 GXMVIEW
        :type  title:                 str
        :type  x1:                    float
        :type  y1:                    float
        :type  side:                  float
        :type  x_vv:                  GXVV
        :type  y_vv:                  GXVV
        :type  z_vv:                  GXVV
        :type  m_vv:                  GXVV
        :type  mask_col:              int
        :type  class_vv:              GXVV
        :type  class_file:            str
        :type  symbol_size_override:  float
        :type  db:                    GXDB
        :type  line_vv:               GXVV
        :type  fid_vv:                GXVV
        :type  x_chan:                str
        :type  y_chan:                str
        :type  z_chan:                str
        :type  grid:                  int
        :type  tic:                   float
        :type  grid_inc:              float
        :type  overlay:               str

        .. versionadded:: 8.0.1

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_

        **Note:** Plot a tri-plot using symbols based on a symbol class file.
        """
        gxapi_cy.WrapCHIMERA._string_classified_tri_plot(GXContext._get_tls_geo(), mview, title.encode(), x1, y1, side, x_vv, y_vv, z_vv, m_vv, mask_col, class_vv, class_file.encode(), symbol_size_override, db, line_vv, fid_vv, x_chan.encode(), y_chan.encode(), z_chan.encode(), grid, tic, grid_inc, overlay.encode())
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer