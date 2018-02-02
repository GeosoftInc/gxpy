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
class GXDU(gxapi_cy.WrapDU):
    """
    GXDU class.

    `GXDU <geosoft.gxapi.GXDU>` functions provide a variety of common utilities that can be applied
    efficiently to the contents of a database. Most `GXDU <geosoft.gxapi.GXDU>` library functions take
    as their first argument a `GXDB <geosoft.gxapi.GXDB>` object, and apply standard processes to data
    stored in an OASIS database, including import and export functions.

    **Note:**

    The following defines are used by GX functions but are not required
    for any methods:
    
    :ref:`DU_LINES`
    """

    def __init__(self, handle=0):
        super().__init__(GXContext._get_tls_geo(), handle)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of `GXDU <geosoft.gxapi.GXDU>`
        
        :returns: A null `GXDU <geosoft.gxapi.GXDU>`
        :rtype:   GXDU
        """
        return GXDU()

    def is_null(self):
        """
        Check if this is a null (undefined) instance
        
        :returns: True if this is a null (undefined) instance, False otherwise.
        :rtype:   bool
        """
        return self._internal_handle() == 0



# Miscellaneous


    @classmethod
    def table_look1(cls, db, line, i_ch, o_ch, ref_field, l_field, mode, close, tb):
        """
        Create a new channel using a single reference table
        
        :param db:         Database
        :param line:       Line Handle
        :param i_ch:       Lookup reference channel [`DB_LOCK_READONLY <geosoft.gxapi.DB_LOCK_READONLY>`]
        :param o_ch:       Output Channel Token     [`DB_LOCK_READWRITE <geosoft.gxapi.DB_LOCK_READWRITE>`]
        :param ref_field:  Reference field name in table
        :param l_field:    Lookup output name in table
        :param mode:       :ref:`DU_LOOKUP`
        :param close:      CLOSE lookup distance. If 0.0, distance is calculated from lookup reference channel.
        :param tb:         `GXTB <geosoft.gxapi.GXTB>` table Object
        :type  db:         GXDB
        :type  line:       int
        :type  i_ch:       int
        :type  o_ch:       int
        :type  ref_field:  str
        :type  l_field:    str
        :type  mode:       int
        :type  close:      float
        :type  tb:         GXTB

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** Fails if table does not contain requested fields.
        The nominal data sample spacing for the CLOSE options is
        calculated by finding the fiducial increment the
        - primary index channel for Lookup1C_DU;
        - secondary index channel for Lookup2C_DU, LookupIValC_DU
        and LookupRValC_DU
        """
        gxapi_cy.WrapDU._table_look1(GXContext._get_tls_geo(), db, line, i_ch, o_ch, ref_field.encode(), l_field.encode(), mode, close, tb)
        



    @classmethod
    def table_look2(cls, db, line, r1_ch, r2_ch, o_ch, r1_field, r2_field, l_field, mode, close, tb):
        """
        Create a new channel using a double reference  table.
        
        :param db:        Database
        :param line:      Line Handle
        :param r1_ch:     Primary reference channel [`DB_LOCK_READONLY <geosoft.gxapi.DB_LOCK_READONLY>`]
        :param r2_ch:     Secondary reference channel [`DB_LOCK_READONLY <geosoft.gxapi.DB_LOCK_READONLY>`]
        :param o_ch:      Output channel [`DB_LOCK_READWRITE <geosoft.gxapi.DB_LOCK_READWRITE>`]
        :param r1_field:  Primary reference field name in table
        :param r2_field:  Secondary reference field name in table
        :param l_field:   Lookup result field name in table
        :param mode:      :ref:`DU_LOOKUP`
        :param close:     CLOSE lookup distance.  If 0.0, distance is calculated from secondary reference channel.
        :param tb:        Table Object
        :type  db:        GXDB
        :type  line:      int
        :type  r1_ch:     int
        :type  r2_ch:     int
        :type  o_ch:      int
        :type  r1_field:  str
        :type  r2_field:  str
        :type  l_field:   str
        :type  mode:      int
        :type  close:     float
        :type  tb:        GXTB

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** Fails if table does not contain requested fields.
        The nominal data sample spacing for the CLOSE options is
        calculated by finding the fiducial increment the
        - primary index channel for Lookup1C_DU;
        - secondary index channel for Lookup2C_DU, LookupIValC_DU
        and LookupRValC_DU
        """
        gxapi_cy.WrapDU._table_look2(GXContext._get_tls_geo(), db, line, r1_ch, r2_ch, o_ch, r1_field.encode(), r2_field.encode(), l_field.encode(), mode, close, tb)
        



    @classmethod
    def table_look_i2(cls, db, line, val, i_ch, o_ch, r1, r2, field, mode, dist, tb):
        """
        Create a new channel using constant integer primary
        reference and a secondary reference table.
        
        :param db:     Database
        :param line:   Line Handle
        :param val:    Lookup primary reference value
        :param i_ch:   Lookup secondary reference channel [`DB_LOCK_READONLY <geosoft.gxapi.DB_LOCK_READONLY>`]
        :param o_ch:   Output Channel Token [`DB_LOCK_READWRITE <geosoft.gxapi.DB_LOCK_READWRITE>`]
        :param r1:     Primary reference field name in table
        :param r2:     Secondary reference field name in table
        :param field:  Lookup result field name in table
        :param mode:   :ref:`DU_LOOKUP`
        :param dist:   CLOSE lookup distance.  If 0.0, distance calculated from secondary reference channel.
        :param tb:     Table Object
        :type  db:     GXDB
        :type  line:   int
        :type  val:    int
        :type  i_ch:   int
        :type  o_ch:   int
        :type  r1:     str
        :type  r2:     str
        :type  field:  str
        :type  mode:   int
        :type  dist:   float
        :type  tb:     GXTB

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** Fails if table does not contain requested fields.
        The nominal data sample spacing for the CLOSE options is
        calculated by finding the fiducial increment the
        - primary index channel for Lookup1C_DU;
        - secondary index channel for Lookup2C_DU, LookupIValC_DU
        and LookupRValC_DU
        """
        gxapi_cy.WrapDU._table_look_i2(GXContext._get_tls_geo(), db, line, val, i_ch, o_ch, r1.encode(), r2.encode(), field.encode(), mode, dist, tb)
        



    @classmethod
    def table_look_r2(cls, db, line, val, i_ch, o_ch, r1, r2, field, mode, dist, tb):
        """
        Create a new channel using a constant real primary
        reference and a secondary reference table.
        
        :param db:     Database
        :param line:   Line Handle
        :param val:    Primary reference value
        :param i_ch:   Secondary reference value [`DB_LOCK_READONLY <geosoft.gxapi.DB_LOCK_READONLY>`]
        :param o_ch:   Output Channel Token [`DB_LOCK_READWRITE <geosoft.gxapi.DB_LOCK_READWRITE>`]
        :param r1:     Primary reference field name in table
        :param r2:     Secondary reference field name in table
        :param field:  Lookup result field name in table
        :param mode:   :ref:`DU_LOOKUP`
        :param dist:   CLOSE lookup distance.  If 0.0, distance calculated from secondary reference channel.
        :param tb:     Table Object
        :type  db:     GXDB
        :type  line:   int
        :type  val:    float
        :type  i_ch:   int
        :type  o_ch:   int
        :type  r1:     str
        :type  r2:     str
        :type  field:  str
        :type  mode:   int
        :type  dist:   float
        :type  tb:     GXTB

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** Fails if table does not contain requested fields.
        The nominal data sample spacing for the CLOSE options is
        calculated by finding the fiducial increment the
        - primary index channel for Lookup1C_DU;
        - secondary index channel for Lookup2C_DU, LookupIValC_DU
        and LookupRValC_DU
        """
        gxapi_cy.WrapDU._table_look_r2(GXContext._get_tls_geo(), db, line, val, i_ch, o_ch, r1.encode(), r2.encode(), field.encode(), mode, dist, tb)
        



    @classmethod
    def ado_table_names(cls, connect, vv):
        """
        Scans a ADO-compliant database and returns the table names in a `GXVV <geosoft.gxapi.GXVV>`
        
        :param connect:  Database connection string
        :param vv:       `GXVV <geosoft.gxapi.GXVV>` to return names in
        :type  connect:  str
        :type  vv:       GXVV

        .. versionadded:: 5.0.8

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** The `GXVV <geosoft.gxapi.GXVV>` must be created to hold strings of length
        `STR_DB_SYMBOL <geosoft.gxapi.STR_DB_SYMBOL>`; i.e. use
        Creat_VV(-`STR_DB_SYMBOL <geosoft.gxapi.STR_DB_SYMBOL>`, 0), or it will assert.
        """
        gxapi_cy.WrapDU._ado_table_names(GXContext._get_tls_geo(), connect.encode(), vv)
        



    @classmethod
    def an_sig(cls, db, line, i_ch, o_ch):
        """
        Calculate the Analytic Signal of a channel.
        
        :param db:    Database
        :param line:  Line handle
        :param i_ch:  Input channel [`DB_LOCK_READONLY <geosoft.gxapi.DB_LOCK_READONLY>`]
        :param o_ch:  Output Analytic Signal channel [`DB_LOCK_READWRITE <geosoft.gxapi.DB_LOCK_READWRITE>`]
        :type  db:    GXDB
        :type  line:  int
        :type  i_ch:  int
        :type  o_ch:  int

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        gxapi_cy.WrapDU._an_sig(GXContext._get_tls_geo(), db, line, i_ch, o_ch)
        



    @classmethod
    def append(cls, d_bi, d_bo, ignore):
        """
        Append a source database onto a destination database.
        
        :param d_bi:    Source Database
        :param d_bo:    Destination Database
        :param ignore:  Ignore write protection on channels? (TRUE or FALSE)
        :type  d_bi:    GXDB
        :type  d_bo:    GXDB
        :type  ignore:  int

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** If the source database and destination database have channels
        with the same name, then data is appended onto the end
        of the channel in lines which have the same number.
        
        If a channel in the destination database is not also in the source
        database, it is ignored.
        """
        gxapi_cy.WrapDU._append(GXContext._get_tls_geo(), d_bi, d_bo, ignore)
        



    @classmethod
    def avg_azimuth(cls, db, precision, azimuth):
        """
        Returns average azimuth of selected lines.
        
        :param db:         Database Object
        :param precision:  Precision in degrees (1 to 45)
        :param azimuth:    Azimuth value returned
        :type  db:         GXDB
        :type  precision:  float
        :type  azimuth:    float_ref

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** Direction in degrees azimuth (clockwise relative
        the +Y direction). The result is in the range
        -90 < azimuth <= 90. The method handles lines going
        in opposite directions (they do not average to 0!)
        The method takes a precision, which is used to generate
        a series of "test" angles.
        The dot product of the line directions is taken
        with each of the test angles, and the absolute values summed.
        The maximum value occurs at the angle which most closely
        approximates the trend direction of the lines.
        """
        azimuth.value = gxapi_cy.WrapDU._avg_azimuth(GXContext._get_tls_geo(), db, precision, azimuth.value)
        



    @classmethod
    def base_data(cls, db, line, in_ch, time_ch, out_ch, tb):
        """
        This method corrects an entire database line using a
        time-based correction table. It is given 2 input channel
        tokens and 1 output channel token as well as the table
        object to use.
        
        :param db:       Database
        :param line:     Line Handle to apply correction to
        :param in_ch:    Input Channel Token  [`DB_LOCK_READONLY <geosoft.gxapi.DB_LOCK_READONLY>`]
        :param time_ch:  Time Channel Token   [`DB_LOCK_READONLY <geosoft.gxapi.DB_LOCK_READONLY>`]
        :param out_ch:   Output Channel Token [`DB_LOCK_READWRITE <geosoft.gxapi.DB_LOCK_READWRITE>`]
        :param tb:       Table Object (a Date/Time/Correction Table)
        :type  db:       GXDB
        :type  line:     int
        :type  in_ch:    int
        :type  time_ch:  int
        :type  out_ch:   int
        :type  tb:       GXTB

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        gxapi_cy.WrapDU._base_data(GXContext._get_tls_geo(), db, line, in_ch, time_ch, out_ch, tb)
        



    @classmethod
    def base_data_ex(cls, db, line, in_ch, time_ch, out_ch, tb, flag):
        """
        This method corrects an entire database line using a
        time-based correction table. It is given 2 input channel
        tokens and 1 output channel token as well as the table
        object to use (table sort flag=1 for sort, =0 for no sort).
        
        :param db:       Database
        :param line:     Line Handle to apply correction to
        :param in_ch:    Input Channel Token  [`DB_LOCK_READONLY <geosoft.gxapi.DB_LOCK_READONLY>`]
        :param time_ch:  Time Channel Token   [`DB_LOCK_READONLY <geosoft.gxapi.DB_LOCK_READONLY>`]
        :param out_ch:   Output Channel Token [`DB_LOCK_READWRITE <geosoft.gxapi.DB_LOCK_READWRITE>`]
        :param tb:       Table Object (a Date/Time/Correction Table)
        :param flag:     Table sort flag: 0 - do not sort, 1 - do sort.
        :type  db:       GXDB
        :type  line:     int
        :type  in_ch:    int
        :type  time_ch:  int
        :type  out_ch:   int
        :type  tb:       GXTB
        :type  flag:     int

        .. versionadded:: 5.1.8

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        gxapi_cy.WrapDU._base_data_ex(GXContext._get_tls_geo(), db, line, in_ch, time_ch, out_ch, tb, flag)
        



    @classmethod
    def bound_line(cls, db, line, x_chan, y_chan, pply):
        """
        Set map boundary clip limits.
        
        :param db:      Database
        :param line:    Line Handle [`DB_LOCK_READWRITE <geosoft.gxapi.DB_LOCK_READWRITE>`]
        :param x_chan:  X Channel   [`DB_LOCK_READONLY <geosoft.gxapi.DB_LOCK_READONLY>`]
        :param y_chan:  Y Channel   [`DB_LOCK_READONLY <geosoft.gxapi.DB_LOCK_READONLY>`]
        :param pply:    Polygon Object to use
        :type  db:      GXDB
        :type  line:    int
        :type  x_chan:  int
        :type  y_chan:  int
        :type  pply:    GXPLY

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        gxapi_cy.WrapDU._bound_line(GXContext._get_tls_geo(), db, line, x_chan, y_chan, pply)
        



    @classmethod
    def bp_filt(cls, db, line, i_ch, o_ch, sw, lw, filt_len):
        """
        This method applies a band-pass filter to the specified
        line/channel and places the output in the output channel.
        
        :param db:        Database
        :param line:      Line handle
        :param i_ch:      Input channel to filter [`DB_LOCK_READONLY <geosoft.gxapi.DB_LOCK_READONLY>`]
        :param o_ch:      Output filtered channel [`DB_LOCK_READWRITE <geosoft.gxapi.DB_LOCK_READWRITE>`]
        :param sw:        Short wavelength cutoff, 0 for highpass
        :param lw:        Long wavelength cutoff, 0 for lowpass
        :param filt_len:  Filter Length, 0 for default length
        :type  db:        GXDB
        :type  line:      int
        :type  i_ch:      int
        :type  o_ch:      int
        :type  sw:        float
        :type  lw:        float
        :type  filt_len:  int

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** If the short and long wavelengths are <= 0, the input channel
        is simply copied to the output channel without filtering.
        """
        gxapi_cy.WrapDU._bp_filt(GXContext._get_tls_geo(), db, line, i_ch, o_ch, sw, lw, filt_len)
        



    @classmethod
    def break_line(cls, db, line, chan):
        """
        Break up a line based on line numbers in a channel.
        
        :param db:    Database
        :param line:  Line to be broken up [`DB_LOCK_READONLY <geosoft.gxapi.DB_LOCK_READONLY>`]
        :param chan:  Channel containing line numbers [`DB_LOCK_READONLY <geosoft.gxapi.DB_LOCK_READONLY>`]
        :type  db:    GXDB
        :type  line:  int
        :type  chan:  int

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        gxapi_cy.WrapDU._break_line(GXContext._get_tls_geo(), db, line, chan)
        



    @classmethod
    def break_line2(cls, db, line, chan, reset_fi_ds):
        """
        Break up a line based on line numbers in a channel.
        
        :param db:           Database
        :param line:         Line to be broken up [`DB_LOCK_READONLY <geosoft.gxapi.DB_LOCK_READONLY>`]
        :param chan:         Channel containing line numbers [`DB_LOCK_READONLY <geosoft.gxapi.DB_LOCK_READONLY>`]
        :param reset_fi_ds:  Reset starting fiducials to zero (0: No, 1: Yes)
        :type  db:           GXDB
        :type  line:         int
        :type  chan:         int
        :type  reset_fi_ds:  int

        .. versionadded:: 8.4

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** The same as BreakLine, but with an option to reset each line's starting fiducial to zero.
        """
        gxapi_cy.WrapDU._break_line2(GXContext._get_tls_geo(), db, line, chan, reset_fi_ds)
        



    @classmethod
    def break_line_to_groups(cls, db, line, chan, cl):
        """
        Break up a line into group-lines based on a channel.
        
        :param db:    Database
        :param line:  Line to be broken up [`DB_LOCK_READONLY <geosoft.gxapi.DB_LOCK_READONLY>`]
        :param chan:  Channel containing line numbers [`DB_LOCK_READONLY <geosoft.gxapi.DB_LOCK_READONLY>`]
        :param cl:    Class name for new group lines (can be "")
        :type  db:    GXDB
        :type  line:  int
        :type  chan:  int
        :type  cl:    str

        .. versionadded:: 5.1.8

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** The original line will be deleted.
        This is similar to `break_line <geosoft.gxapi.GXDU.break_line>`, but the output lines
        are "group" lines, without the line type letters at the
        start. (See db.gxh for information of Group Lines).
        All channels are associated with each group line, and the
        input class name is assigned to each group.
        Class names for
        groups ensure that (for instance) if you add a new channel to
        one group of a given class, it will get added to all other
        groups in the same class. If the class name is left empty, then
        this will NOT be true. (Groups without class names are treated
        as isolated entities for the purposes of channel loading).
        """
        gxapi_cy.WrapDU._break_line_to_groups(GXContext._get_tls_geo(), db, line, chan, cl.encode())
        



    @classmethod
    def break_line_to_groups2(cls, db, line, chan, cl, reset_fi_ds):
        """
        Break up a line into group-lines based on a channel.
        
        :param db:           Database
        :param line:         Line to be broken up [`DB_LOCK_READONLY <geosoft.gxapi.DB_LOCK_READONLY>`]
        :param chan:         Channel containing line numbers [`DB_LOCK_READONLY <geosoft.gxapi.DB_LOCK_READONLY>`]
        :param cl:           Class name for new group lines (can be "")
        :param reset_fi_ds:  Reset starting fiducials to zero (0: No, 1: Yes)
        :type  db:           GXDB
        :type  line:         int
        :type  chan:         int
        :type  cl:           str
        :type  reset_fi_ds:  int

        .. versionadded:: 8.4

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** The same as BreakLineToGroups, but with an option to reset each line's starting fiducial to zero.
        """
        gxapi_cy.WrapDU._break_line_to_groups2(GXContext._get_tls_geo(), db, line, chan, cl.encode(), reset_fi_ds)
        



    @classmethod
    def b_spline(cls, db, line, i_ch, o_ch, sd, rou, tau):
        """
        B-spline Interpolate a Channel.
        
        :param db:    Database
        :param line:  Line handle
        :param i_ch:  Channel to interpolate [`DB_LOCK_READONLY <geosoft.gxapi.DB_LOCK_READONLY>`]
        :param o_ch:  Output interpolated channel [`DB_LOCK_READWRITE <geosoft.gxapi.DB_LOCK_READWRITE>`]
        :param sd:    Data error (Std Dev > 0.0)
        :param rou:   Roughness (Rou > 0.0)
        :param tau:   Tension (0.<= Tension <=1.)
        :type  db:    GXDB
        :type  line:  int
        :type  i_ch:  int
        :type  o_ch:  int
        :type  sd:    float
        :type  rou:   float
        :type  tau:   float

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        .. seealso::

            `trend <geosoft.gxapi.GXDU.trend>`
        """
        gxapi_cy.WrapDU._b_spline(GXContext._get_tls_geo(), db, line, i_ch, o_ch, sd, rou, tau)
        



    @classmethod
    def closest_point(cls, db, x, y, xp, yp, line, fid):
        """
        Return closest data point to input location.
        
        :param x:     X location
        :param y:     Y location
        :param xp:    Located X location
        :param yp:    Located Y location
        :param line:  Line for located point
        :param fid:   Fiducial of located point
        :type  db:    GXDB
        :type  x:     float
        :type  y:     float
        :type  xp:    float_ref
        :type  yp:    float_ref
        :type  line:  int_ref
        :type  fid:   float_ref

        .. versionadded:: 6.2

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** Selected lines are scanned for the (X, Y) location
        which is closest to the input location.
        The line and fiducial of the point are returned.
        
        Will register an error if no valid (X, Y) locations
        are found.
        """
        xp.value, yp.value, line.value, fid.value = gxapi_cy.WrapDU._closest_point(GXContext._get_tls_geo(), db, x, y, xp.value, yp.value, line.value, fid.value)
        



    @classmethod
    def copy_line(cls, db, i_line, o_line):
        """
        Copy a line.
        
        :param db:      Database
        :param i_line:  Input Line  [`DB_LOCK_READONLY <geosoft.gxapi.DB_LOCK_READONLY>`]
        :param o_line:  Output Line [`DB_LOCK_READWRITE <geosoft.gxapi.DB_LOCK_READWRITE>`]
        :type  db:      GXDB
        :type  i_line:  int
        :type  o_line:  int

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** Existing channels in the output line will be replaced
        by copied channels.
        """
        gxapi_cy.WrapDU._copy_line(GXContext._get_tls_geo(), db, i_line, o_line)
        



    @classmethod
    def copy_line_across(cls, idb, i_line, odb, o_line):
        """
        Copy a line from one database to another.
        
        :param idb:     Input Database
        :param i_line:  Input Line  [`DB_LOCK_READONLY <geosoft.gxapi.DB_LOCK_READONLY>`]
        :param odb:     Output Database
        :param o_line:  Output Line [`DB_LOCK_READWRITE <geosoft.gxapi.DB_LOCK_READWRITE>`]
        :type  idb:     GXDB
        :type  i_line:  int
        :type  odb:     GXDB
        :type  o_line:  int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Existing channels in the output line will be replaced
        by copied channels.

        .. seealso::

            `copy_line_chan_across <geosoft.gxapi.GXDU.copy_line_chan_across>` function
        """
        gxapi_cy.WrapDU._copy_line_across(GXContext._get_tls_geo(), idb, i_line, odb, o_line)
        



    @classmethod
    def copy_line_chan_across(cls, idb, i_line, vv_chan, odb, o_line):
        """
        Copy a list of channels in a line from one database to another.
        
        :param idb:      Input Database
        :param i_line:   Input Line   [`DB_LOCK_READONLY <geosoft.gxapi.DB_LOCK_READONLY>`]
        :param vv_chan:  `GXVV <geosoft.gxapi.GXVV>` containing a list of channel symbols, must be of INT
        :param odb:      Output Database
        :param o_line:   Output Line  [`DB_LOCK_READWRITE <geosoft.gxapi.DB_LOCK_READWRITE>`]
        :type  idb:      GXDB
        :type  i_line:   int
        :type  vv_chan:  GXVV
        :type  odb:      GXDB
        :type  o_line:   int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Existing channels in the output line will be replaced
        by copied channels.

        .. seealso::

            `copy_line_across <geosoft.gxapi.GXDU.copy_line_across>` function
        """
        gxapi_cy.WrapDU._copy_line_chan_across(GXContext._get_tls_geo(), idb, i_line, vv_chan, odb, o_line)
        



    @classmethod
    def copy_line_masked(cls, db, i_line, mask, prune, o_line):
        """
        Copy a line, prune items based on a mask channel
        
        :param db:      Database Object
        :param i_line:  Input  Line Symbol [`DB_LOCK_READONLY <geosoft.gxapi.DB_LOCK_READONLY>`]
        :param mask:    Mask Channel Symbol [`DB_LOCK_READONLY <geosoft.gxapi.DB_LOCK_READONLY>`]
        :param prune:   :ref:`VVU_PRUNE`
        :param o_line:  Output Line Symbol [`DB_LOCK_READWRITE <geosoft.gxapi.DB_LOCK_READWRITE>`]
        :type  db:      GXDB
        :type  i_line:  int
        :type  mask:    int
        :type  prune:   int
        :type  o_line:  int

        .. versionadded:: 5.0.8

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** The input line's channel data is ReFidded to the mask
        channel, and then pruned from the output line data,
        based on the value of the VVU_PRUNE_XXX variable.
        For `VVU_PRUNE_DUMMY <geosoft.gxapi.VVU_PRUNE_DUMMY>`, only those items where the mask channel
        value is not a dummy are retained, while the complement
        is retained for VV_PRUNE_VALID.
        """
        gxapi_cy.WrapDU._copy_line_masked(GXContext._get_tls_geo(), db, i_line, mask, prune, o_line)
        



    @classmethod
    def dao_table_names(cls, file, type, vv):
        """
        Scans a DAO-compliant database and returns the table names in a `GXVV <geosoft.gxapi.GXVV>`
        
        :param file:  Database file name
        :param type:  Database Type
        :param vv:    `GXVV <geosoft.gxapi.GXVV>` to return names in
        :type  file:  str
        :type  type:  str
        :type  vv:    GXVV

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** The `GXVV <geosoft.gxapi.GXVV>` must be created to hold strings of length
        `STR_DB_SYMBOL <geosoft.gxapi.STR_DB_SYMBOL>`; i.e. use
        Creat_VV(-`STR_DB_SYMBOL <geosoft.gxapi.STR_DB_SYMBOL>`, 0), or it will assert.
        """
        gxapi_cy.WrapDU._dao_table_names(GXContext._get_tls_geo(), file.encode(), type.encode(), vv)
        



    @classmethod
    def decimate(cls, db, line, i_ch, o_ch, n):
        """
        Copy and decimate a channel
        
        :param db:    Database
        :param line:  Line handle
        :param i_ch:  Origin Channel [`DB_LOCK_READONLY <geosoft.gxapi.DB_LOCK_READONLY>`]
        :param o_ch:  Destination Channel [`DB_LOCK_READWRITE <geosoft.gxapi.DB_LOCK_READWRITE>`]
        :param n:     Decimation factor
        :type  db:    GXDB
        :type  line:  int
        :type  i_ch:  int
        :type  o_ch:  int
        :type  n:     int

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        gxapi_cy.WrapDU._decimate(GXContext._get_tls_geo(), db, line, i_ch, o_ch, n)
        



    @classmethod
    def diff(cls, db, line, i_ch, o_ch, n):
        """
        Calculate differences within a channel.
        
        :param db:    Database
        :param line:  Line handle
        :param i_ch:  Origin Channel [`DB_LOCK_READONLY <geosoft.gxapi.DB_LOCK_READONLY>`]
        :param o_ch:  Destination Channel [`DB_LOCK_READWRITE <geosoft.gxapi.DB_LOCK_READWRITE>`]
        :param n:     Number of differences
        :type  db:    GXDB
        :type  line:  int
        :type  i_ch:  int
        :type  o_ch:  int
        :type  n:     int

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** Differences with dummies result in dummies.
        An even number of differences locates data accurately.
        An odd number of differences locates result 1/2 element lower
        in the `GXVV <geosoft.gxapi.GXVV>`.
        """
        gxapi_cy.WrapDU._diff(GXContext._get_tls_geo(), db, line, i_ch, o_ch, n)
        



    @classmethod
    def distance(cls, db, line, x_ch, y_ch, o_ch):
        """
        Create a distance channel from X and Y.
        
        :param db:    Database
        :param line:  Line symbol
        :param x_ch:  X channel [`DB_LOCK_READONLY <geosoft.gxapi.DB_LOCK_READONLY>`]
        :param y_ch:  Y channel [`DB_LOCK_READONLY <geosoft.gxapi.DB_LOCK_READONLY>`]
        :param o_ch:  Output Distance channel [`DB_LOCK_READWRITE <geosoft.gxapi.DB_LOCK_READWRITE>`]
        :type  db:    GXDB
        :type  line:  int
        :type  x_ch:  int
        :type  y_ch:  int
        :type  o_ch:  int

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        gxapi_cy.WrapDU._distance(GXContext._get_tls_geo(), db, line, x_ch, y_ch, o_ch)
        



    @classmethod
    def distance_3d(cls, db, line, x_ch, y_ch, z_ch, type, o_ch):
        """
        Create a distance channel from XY or XYZ with direction options.
        
        :param db:    Database
        :param line:  Line symbol
        :param x_ch:  X channel [`DB_LOCK_READONLY <geosoft.gxapi.DB_LOCK_READONLY>`]
        :param y_ch:  Y channel [`DB_LOCK_READONLY <geosoft.gxapi.DB_LOCK_READONLY>`]
        :param z_ch:  Z channel [`DB_LOCK_READONLY <geosoft.gxapi.DB_LOCK_READONLY>`] (can be `NULLSYMB <geosoft.gxapi.NULLSYMB>`)
        :param type:  :ref:`DU_DISTANCE_CHANNEL_TYPE`
        :param o_ch:  Output Distance channel [`DB_LOCK_READWRITE <geosoft.gxapi.DB_LOCK_READWRITE>`]
        :type  db:    GXDB
        :type  line:  int
        :type  x_ch:  int
        :type  y_ch:  int
        :type  z_ch:  int
        :type  type:  int
        :type  o_ch:  int

        .. versionadded:: 8.1

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        gxapi_cy.WrapDU._distance_3d(GXContext._get_tls_geo(), db, line, x_ch, y_ch, z_ch, type, o_ch)
        



    @classmethod
    def distline(cls, db, line, x_ch, y_ch, dist):
        """
        Calculate cummulative distance for a line.
        
        :param db:    Database
        :param line:  Line symbol
        :param x_ch:  X channel [`DB_LOCK_READONLY <geosoft.gxapi.DB_LOCK_READONLY>`]
        :param y_ch:  Y channel [`DB_LOCK_READONLY <geosoft.gxapi.DB_LOCK_READONLY>`]
        :param dist:  Cummulative distance (retruned)
        :type  db:    GXDB
        :type  line:  int
        :type  x_ch:  int
        :type  y_ch:  int
        :type  dist:  float_ref

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        dist.value = gxapi_cy.WrapDU._distline(GXContext._get_tls_geo(), db, line, x_ch, y_ch, dist.value)
        



    @classmethod
    def dup_chan_locks(cls, d_bi, d_bo):
        """
        Duplicate all channels protect-info from input `GXDB <geosoft.gxapi.GXDB>`.
        
        :param d_bi:  Input Database handle
        :param d_bo:  Output Database handle.
        :type  d_bi:  GXDB
        :type  d_bo:  GXDB

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        gxapi_cy.WrapDU._dup_chan_locks(GXContext._get_tls_geo(), d_bi, d_bo)
        



    @classmethod
    def dup_chans(cls, d_bi, d_bo):
        """
        Duplicate all channels from input `GXDB <geosoft.gxapi.GXDB>`.
        
        :param d_bi:  Input Database handle
        :param d_bo:  Output Database handle.
        :type  d_bi:  GXDB
        :type  d_bo:  GXDB

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        gxapi_cy.WrapDU._dup_chans(GXContext._get_tls_geo(), d_bi, d_bo)
        



    @classmethod
    def edit_duplicates(cls, db, line, x_ch, y_ch, option, single, fid_num):
        """
        Edit duplicate readings at individual location
        
        :param db:       Database
        :param line:     Line
        :param x_ch:     Channel X, unlocked
        :param y_ch:     Channel Y, unlocked
        :param option:   :ref:`DB_DUP`
        :param single:   :ref:`DB_DUPEDIT`
        :param fid_num:  Fiducial number (required if `DB_DUPEDIT_SINGLE <geosoft.gxapi.DB_DUPEDIT_SINGLE>`)
        :type  db:       GXDB
        :type  line:     int
        :type  x_ch:     int
        :type  y_ch:     int
        :type  option:   int
        :type  single:   int
        :type  fid_num:  float

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** All the channels must be of the same fid incr/start and length.
        Protected channels are modified automatically.
        """
        gxapi_cy.WrapDU._edit_duplicates(GXContext._get_tls_geo(), db, line, x_ch, y_ch, option, single, fid_num)
        



    @classmethod
    def export1(cls, db, format, cur_line, chan_vv, chan, data, dummies, header):
        """
        Export to a specific format.
        
        :param db:        Database
        :param format:    :ref:`DU_EXPORT`
        :param cur_line:  Current line
        :param chan_vv:   List of channels - channel symbols stored as INT
        :param chan:      :ref:`DU_CHANNELS`
        :param data:      Data file name
        :param dummies:   Write out dummies?
        :param header:    Include a header with channel names?
        :type  db:        GXDB
        :type  format:    int
        :type  cur_line:  str
        :type  chan_vv:   GXVV
        :type  chan:      int
        :type  data:      str
        :type  dummies:   int
        :type  header:    int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** For databases with both groups and lines:
        If both lines and groups are selected, save only the lines.
        If no lines are selected, (only groups), save the current line
        if it is (1) a group and (2) selected, else save the first selected
        group. ---
        Option to filter out data where one of the channels has a dummy in it.
        Option to allow a header with the channel names.
        
        The `DU_CHANNELS_DISPLAYED <geosoft.gxapi.DU_CHANNELS_DISPLAYED>` option can be used to export any selection of
        channels, listed by the symbols (DB_SYMB) values, cast to int values and
        stored in a `GXVV <geosoft.gxapi.GXVV>`.
        """
        gxapi_cy.WrapDU._export1(GXContext._get_tls_geo(), db, format, cur_line.encode(), chan_vv, chan, data.encode(), dummies, header)
        



    @classmethod
    def export2(cls, db, format, cur_line, chan_vv, chan, data, dummies, header, line_names):
        """
        Like `export1 <geosoft.gxapi.GXDU.export1>`, but include line names as data.
        
        :param db:          Database
        :param format:      :ref:`DU_EXPORT`
        :param cur_line:    Current line
        :param chan_vv:     List of channels - channel symbols stored as INT
        :param chan:        :ref:`DU_CHANNELS`
        :param data:        Data file name
        :param dummies:     Write out dummies?
        :param header:      Include a header with channel names?
        :param line_names:  Include line names as data?
        :type  db:          GXDB
        :type  format:      int
        :type  cur_line:    str
        :type  chan_vv:     GXVV
        :type  chan:        int
        :type  data:        str
        :type  dummies:     int
        :type  header:      int
        :type  line_names:  int

        .. versionadded:: 5.1.6

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** See `export1 <geosoft.gxapi.GXDU.export1>`.
        The line names are printed as the first column of data exported.
        """
        gxapi_cy.WrapDU._export2(GXContext._get_tls_geo(), db, format, cur_line.encode(), chan_vv, chan, data.encode(), dummies, header, line_names)
        



    @classmethod
    def export_amira(cls, db, wa, one_cols_ch, array_ch, time_ch, errors_ch, datatype, units, config, instrument, frequency):
        """
        Export to database an AMIRA data file.
        
        :param db:           Database
        :param wa:           AMIRA data file handle
        :param one_cols_ch:  Single column channel names, supporting comma (,) separated names of multiple channels, maximum 32 channels
        :param array_ch:     `GXVA <geosoft.gxapi.GXVA>` channel name, required
        :param time_ch:      Optional Time   channel name (must be `GXVA <geosoft.gxapi.GXVA>` channel and same array size as above `GXVA <geosoft.gxapi.GXVA>` channel)
        :param errors_ch:    Optional Errors channel name (must be `GXVA <geosoft.gxapi.GXVA>` channel and same array size as above `GXVA <geosoft.gxapi.GXVA>` channel)
        :param datatype:     Mandatory fields: DATATYPE
        :param units:        UNITS
        :param config:       CONFIG
        :param instrument:   INSTRUMENT
        :param frequency:    FREQUENCY
        :type  db:           GXDB
        :type  wa:           GXWA
        :type  one_cols_ch:  str
        :type  array_ch:     str
        :type  time_ch:      str
        :type  errors_ch:    str
        :type  datatype:     str
        :type  units:        str
        :type  config:       str
        :type  instrument:   str
        :type  frequency:    str

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Other defined FIELDS stored in the database (see `import_amira <geosoft.gxapi.GXDU.import_amira>` function)
        will be automatically included in the export
        """
        gxapi_cy.WrapDU._export_amira(GXContext._get_tls_geo(), db, wa, one_cols_ch.encode(), array_ch.encode(), time_ch.encode(), errors_ch.encode(), datatype.encode(), units.encode(), config.encode(), instrument.encode(), frequency.encode())
        



    @classmethod
    def export_aseg(cls, db, cur_line, chan_vv, chan, defn, data):
        """
        Export to ASEG-GDF format file(s).
        
        :param db:        Database
        :param cur_line:  Current line
        :param chan_vv:   Displayed channels
        :param chan:      :ref:`DU_CHANNELS`
        :param defn:      Header file name
        :param data:      Data file name
        :type  db:        GXDB
        :type  cur_line:  str
        :type  chan_vv:   GXVV
        :type  chan:      int
        :type  defn:      str
        :type  data:      str

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** At least one of the header file
        or data file names must be set. (Unset names will get the
        same file name, but with the extensions .dfn (header) or
        .dat (data).
        For databases with both groups and lines:
        If both lines and groups are selected, save only the lines.
        If no lines are selected, (only groups), save the current line
        if it is (1) a group and (2) selected, else save the first selected
        group. ---
        """
        gxapi_cy.WrapDU._export_aseg(GXContext._get_tls_geo(), db, cur_line.encode(), chan_vv, chan, defn.encode(), data.encode())
        



    @classmethod
    def export_aseg_proj(cls, db, cur_line, chan_vv, chan, defn, data, proj, ipj):
        """
        Export to ASEG-GDF format file(s) (supports projections).
        
        :param db:        Database
        :param cur_line:  Current line
        :param chan_vv:   Displayed channels
        :param chan:      :ref:`DU_CHANNELS`
        :param defn:      Export header file name
        :param data:      Export data file name
        :param proj:      Export projection file name
        :param ipj:       Projection handle
        :type  db:        GXDB
        :type  cur_line:  str
        :type  chan_vv:   GXVV
        :type  chan:      int
        :type  defn:      str
        :type  data:      str
        :type  proj:      str
        :type  ipj:       GXIPJ

        .. versionadded:: 5.0.1

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** At least one of the header file
        or data file names must be set. (Unset names will get the
        same file name, but with the extensions .dfn (header) or
        .dat (data).
        For databases with both groups and lines:
        If both lines and groups are selected, save only the lines.
        If no lines are selected, (only groups), save the current line
        if it is (1) a group and (2) selected, else save the first selected
        group. ---
        
        This version supports projections
        """
        gxapi_cy.WrapDU._export_aseg_proj(GXContext._get_tls_geo(), db, cur_line.encode(), chan_vv, chan, defn.encode(), data.encode(), proj.encode(), ipj)
        



    @classmethod
    def export_chan_crc(cls, db, symb, crc, file):
        """
        Export a channel as XML and compute a CRC value.
        
        :param db:    Database
        :param symb:  Channel
        :param crc:   CRC Value returned
        :param file:  File name to generate with XML
        :type  db:    GXDB
        :type  symb:  int
        :type  crc:   int_ref
        :type  file:  str

        .. versionadded:: 6.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** The output file is an XML describing the channel. The
        CRC is of the channel data ONLY. To compute a CRC of the
        full channel (include metadata) do a CRC of the generated
        file.
        """
        crc.value = gxapi_cy.WrapDU._export_chan_crc(GXContext._get_tls_geo(), db, symb, crc.value, file.encode())
        



    @classmethod
    def export_csv(cls, db, cur_line, chan_vv, chan, data, dummies, header):
        """
        Export to a CSV file.
        
        :param db:        Database
        :param cur_line:  Current line
        :param chan_vv:   Displayed channels
        :param chan:      :ref:`DU_CHANNELS`
        :param data:      Data file name
        :param dummies:   Write out dummies?
        :param header:    Include a header with channel names?
        :type  db:        GXDB
        :type  cur_line:  str
        :type  chan_vv:   GXVV
        :type  chan:      int
        :type  data:      str
        :type  dummies:   int
        :type  header:    int

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** For databases with both groups and lines:
        If both lines and groups are selected, save only the lines.
        If no lines are selected, (only groups), save the current line
        if it is (1) a group and (2) selected, else save the first selected
        group. ---
        Option to filter out data where one of the channels has a dummy in it.
        Option to allow a header with the channel names.
        """
        gxapi_cy.WrapDU._export_csv(GXContext._get_tls_geo(), db, cur_line.encode(), chan_vv, chan, data.encode(), dummies, header)
        



    @classmethod
    def export_database_crc(cls, db, crc, file):
        """
        Export a channel as XML and compute a CRC value.
        
        :param db:    Database
        :param crc:   CRC Value returned
        :param file:  File name to generate with XML
        :type  db:    GXDB
        :type  crc:   int_ref
        :type  file:  str

        .. versionadded:: 6.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** The output file is an XML describing the channel. The
        CRC is of the channel data ONLY. To compute a CRC of the
        full channel (include metadata) do a CRC of the generated
        file.
        """
        crc.value = gxapi_cy.WrapDU._export_database_crc(GXContext._get_tls_geo(), db, crc.value, file.encode())
        



    @classmethod
    def export_gbn(cls, db, vv, data):
        """
        Export to a GBN data file.
        
        :param db:    Database
        :param vv:    List of channels to export
        :param data:  Export data file name
        :type  db:    GXDB
        :type  vv:    GXVV
        :type  data:  str

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** The iDispChanList_DBE or `GXDB.symb_list <geosoft.gxapi.GXDB.symb_list>` methods can be
        used to obtain a list of channels.
        """
        gxapi_cy.WrapDU._export_gbn(GXContext._get_tls_geo(), db, vv, data.encode())
        



    @classmethod
    def export_mdb(cls, db, cur_line, chan_vv, chan, single, data):
        """
        Export to a Microsoft Access Database (MDB) file.
        
        :param db:        Database
        :param cur_line:  Current line
        :param chan_vv:   Displayed channels
        :param chan:      :ref:`DU_CHANNELS`
        :param single:    :ref:`DU_LINEOUT`
        :param data:      Export data file name
        :type  db:        GXDB
        :type  cur_line:  str
        :type  chan_vv:   GXVV
        :type  chan:      int
        :type  single:    int
        :type  data:      str

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Similar to `export_gbn <geosoft.gxapi.GXDU.export_gbn>`, with the addition that
        Groups go to individual tables, and lines go to
        a single table, or individual tables, based on the
        value of :ref:`DU_LINEOUT`
        """
        gxapi_cy.WrapDU._export_mdb(GXContext._get_tls_geo(), db, cur_line.encode(), chan_vv, chan, single, data.encode())
        



    @classmethod
    def export_geodatabase(cls, db, feature_class_name, cur_line, chan_vv, chan, output, single, data):
        """
        Export to a ESRI Geodatabase file.
        
        :param db:                  Database
        :param feature_class_name:  Feature class name
        :param cur_line:            Current line
        :param chan_vv:             Displayed channels
        :param chan:                :ref:`DU_CHANNELS`
        :param output:              :ref:`DU_FEATURE_TYPE_OUTPUT`
        :param single:              :ref:`DU_LINEOUT`
        :param data:                Export data file name
        :type  db:                  GXDB
        :type  feature_class_name:  str
        :type  cur_line:            str
        :type  chan_vv:             GXVV
        :type  chan:                int
        :type  output:              int
        :type  single:              int
        :type  data:                str

        .. versionadded:: 8.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** Similar to `export_gbn <geosoft.gxapi.GXDU.export_gbn>`, with the addition that
        Groups go to individual tables, and lines go to
        a single table, or individual tables, based on the
        value of :ref:`DU_LINEOUT`
        """
        gxapi_cy.WrapDU._export_geodatabase(GXContext._get_tls_geo(), db, feature_class_name.encode(), cur_line.encode(), chan_vv, chan, output, single, data.encode())
        



    @classmethod
    def get_existing_feature_classes_in_geodatabase(cls, db, geodatabase, lst, vv):
        """
        Searches the geodatabases for an existing Feature class.
        
        :param db:           Database
        :param geodatabase:  File geodatabase
        :param lst:          Feature class names to verify
        :param vv:           Output list of existing feature class names
        :type  db:           GXDB
        :type  geodatabase:  str
        :type  lst:          GXLST
        :type  vv:           GXVV

        :returns:            0 - Feature class does not exist
                             1 - Feature class exists
        :rtype:              int

        .. versionadded:: 8.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** Searches the geodatabases for an existing Feature class
        """
        ret_val = gxapi_cy.WrapDU._get_existing_feature_classes_in_geodatabase(GXContext._get_tls_geo(), db, geodatabase.encode(), lst, vv)
        return ret_val



    @classmethod
    def export_shp(cls, db, cur_line, chan_vv, chan, single, data, lst):
        """
        Export to a shape file or files.
        
        :param db:        Database
        :param cur_line:  Current line
        :param chan_vv:   Displayed channels
        :param chan:      :ref:`DU_CHANNELS`
        :param single:    :ref:`DU_LINEOUT`
        :param data:      Export shape file name or base filename (shp assumed if no extension given)
        :param lst:       `GXLST <geosoft.gxapi.GXLST>` object will be filled with shape files created
        :type  db:        GXDB
        :type  cur_line:  str
        :type  chan_vv:   GXVV
        :type  chan:      int
        :type  single:    int
        :type  data:      str
        :type  lst:       GXLST

        .. versionadded:: 6.1

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Similar to `export_mdb <geosoft.gxapi.GXDU.export_mdb>`, with the addition that groups go to indiviual files
        with group name suffixes, and lines go to a single file, or multiple files
        with line name suffixes, based on the value of :ref:`DU_LINEOUT`.
        """
        gxapi_cy.WrapDU._export_shp(GXContext._get_tls_geo(), db, cur_line.encode(), chan_vv, chan, single, data.encode(), lst)
        



    @classmethod
    def export_xyz(cls, db, data, template):
        """
        Export XYZdata from a database to an XYZ file.
        
        :param db:        Database
        :param data:      Export data file name
        :param template:  Export template name
        :type  db:        GXDB
        :type  data:      str
        :type  template:  str

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** 1. The export template can be in the local directory or the GEOSOFT
        directory.  The import data file must include the path if it is not
        in the local directory.
        
        2. Both the import template and data file must exist.
        
        3. Sample Template file
        
        [EXPORT XYZ]
        EXPORT     CHAN {,FORMAT} {,WIDTH} {,DECIMAL}
        WRITEDUMMY YES
        CLIPMAP    YES
        MAXPOINTS  1000
        INCREMENT  .5
        
        4. This can be used to export a group, but the group must be the
        currently displayed line, and only that group will be exported.
        """
        gxapi_cy.WrapDU._export_xyz(GXContext._get_tls_geo(), db, data.encode(), template.encode())
        



    @classmethod
    def export_xyz2(cls, db, wa, ra):
        """
        Export XYZdata from a database to an XYZ file, using file handles.
        
        :param db:  Database
        :param wa:  Export data file `GXWA <geosoft.gxapi.GXWA>` handle
        :param ra:  Export template file `GXRA <geosoft.gxapi.GXRA>` handle
        :type  db:  GXDB
        :type  wa:  GXWA
        :type  ra:  GXRA

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        .. seealso::

            `export_xyz <geosoft.gxapi.GXDU.export_xyz>`
        """
        gxapi_cy.WrapDU._export_xyz2(GXContext._get_tls_geo(), db, wa, ra)
        



    @classmethod
    def fft(cls, db, line, s_ch, r_ch, i_ch):
        """
        Apply an `GXFFT <geosoft.gxapi.GXFFT>` to space data.
        
        :param db:    Database
        :param line:  Line handle
        :param s_ch:  Space Channel [`DB_LOCK_READONLY <geosoft.gxapi.DB_LOCK_READONLY>`]
        :param r_ch:  Real Channel  [`DB_LOCK_READWRITE <geosoft.gxapi.DB_LOCK_READWRITE>`]
        :param i_ch:  Imaginary Channel [`DB_LOCK_READWRITE <geosoft.gxapi.DB_LOCK_READWRITE>`]
        :type  db:    GXDB
        :type  line:  int
        :type  s_ch:  int
        :type  r_ch:  int
        :type  i_ch:  int

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        gxapi_cy.WrapDU._fft(GXContext._get_tls_geo(), db, line, s_ch, r_ch, i_ch)
        



    @classmethod
    def filter(cls, db, line, i_ch, o_ch, flt):
        """
        Apply a convolution filter to a channel.
        
        :param db:    Database
        :param line:  Line handle
        :param i_ch:  Input channel [`DB_LOCK_READONLY <geosoft.gxapi.DB_LOCK_READONLY>`]
        :param o_ch:  Output filtered channel [`DB_LOCK_READWRITE <geosoft.gxapi.DB_LOCK_READWRITE>`]
        :param flt:   Filter handle (`GXFLT <geosoft.gxapi.GXFLT>`)
        :type  db:    GXDB
        :type  line:  int
        :type  i_ch:  int
        :type  o_ch:  int
        :type  flt:   int

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        gxapi_cy.WrapDU._filter(GXContext._get_tls_geo(), db, line, i_ch, o_ch, flt)
        



    @classmethod
    def gen_lev(cls, db, in_file, out_file, max_dz, m0):
        """
        Generate a Level table from an Intersection Table.
        
        :param db:        Database
        :param in_file:   Input Table file Name
        :param out_file:  Output Table file Name
        :param max_dz:    Max. gradient
        :param m0:        :ref:`DU_LEVEL`
        :type  db:        GXDB
        :type  in_file:   str
        :type  out_file:  str
        :type  max_dz:    float
        :type  m0:        int

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        gxapi_cy.WrapDU._gen_lev(GXContext._get_tls_geo(), db, in_file.encode(), out_file.encode(), max_dz, m0)
        



    @classmethod
    def gen_lev_db(cls, db, out_file, max_dz, m0):
        """
        Generate a Level table from an Intersection Database
        
        :param db:        Input intersection database object
        :param out_file:  Output Table File Name
        :param max_dz:    Max. gradient
        :param m0:        :ref:`DU_LEVEL`
        :type  db:        GXDB
        :type  out_file:  str
        :type  max_dz:    float
        :type  m0:        int

        .. versionadded:: 7.1

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** Requires channels with the following names:
        
        ine, TFid, TZ, TDZ
        Line, LFid, LZ, LDZ
        Mask
        """
        gxapi_cy.WrapDU._gen_lev_db(GXContext._get_tls_geo(), db, out_file.encode(), max_dz, m0)
        



    @classmethod
    def gen_xyz_temp(cls, xyz, temp):
        """
        Generate default XYZ template for a XYZ file.
        
        :param xyz:   Xyz file name
        :param temp:  Template file name to create
        :type  xyz:   str
        :type  temp:  str

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        gxapi_cy.WrapDU._gen_xyz_temp(GXContext._get_tls_geo(), xyz.encode(), temp.encode())
        



    @classmethod
    def get_xyz_num_fields(cls, xyz, num_fields):
        """
        Get the number of fields in the XYZ file.
        
        :param xyz:         Xyz file name
        :param num_fields:  Returned number of fields
        :type  xyz:         str
        :type  num_fields:  int_ref

        .. versionadded:: 9.1

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        num_fields.value = gxapi_cy.WrapDU._get_xyz_num_fields(GXContext._get_tls_geo(), xyz.encode(), num_fields.value)
        



    @classmethod
    def get_chan_data_lst(cls, db, chan, mask, lst):
        """
        Populate a `GXLST <geosoft.gxapi.GXLST>` with unique items in a channel.
        
        :param db:    Database
        :param chan:  Data Channel
        :param mask:  Mask Channel  (can be `NULLSYMB <geosoft.gxapi.NULLSYMB>`)
        :param lst:   `GXLST <geosoft.gxapi.GXLST>` object to populate
        :type  db:    GXDB
        :type  chan:  int
        :type  mask:  int
        :type  lst:   GXLST

        .. versionadded:: 6.1

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** Items from all selected lines are collected,
        sorted, and duplicates removed. The output
        `GXLST <geosoft.gxapi.GXLST>` name and value are set to the item values.
        Non-string channels are converted internally to
        string values using Copy_VV,
        so results may differ from what
        you may expect given the current channel's display
        width and number of decimals.
        If a mask channel is selected, then only those items
        where the mask channel is not a dummy are collected.
        """
        gxapi_cy.WrapDU._get_chan_data_lst(GXContext._get_tls_geo(), db, chan, mask, lst)
        



    @classmethod
    def get_chan_data_vv(cls, db, chan, mask, vv):
        """
        Populate a `GXVV <geosoft.gxapi.GXVV>` with unique items in a channel.
        
        :param db:    Database
        :param chan:  Channel
        :param mask:  Mask Channel  (can be `NULLSYMB <geosoft.gxapi.NULLSYMB>`)
        :param vv:    `GXVV <geosoft.gxapi.GXVV>` object to populate
        :type  db:    GXDB
        :type  chan:  int
        :type  mask:  int
        :type  vv:    GXVV

        .. versionadded:: 6.1

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** Items from all selected lines are collected,
        sorted, and duplicates removed.
        The data is collected in the channel's data type,
        so normal `GXVV.sort <geosoft.gxapi.GXVV.sort>` rules apply.
        If the output `GXVV <geosoft.gxapi.GXVV>` and channel type are not the
        same, then the data is converted using the
        Copy_VV function, so see that for conversion rules.
        If a mask channel is selected, then only those items
        where the mask channel is not a dummy are collected.
        """
        gxapi_cy.WrapDU._get_chan_data_vv(GXContext._get_tls_geo(), db, chan, mask, vv)
        



    @classmethod
    def gradient(cls, dbi, dbo, ix_ch, iy_ch, iz_ch, ig_ch, ox_ch, oy_ch, oz_ch, angle, width):
        """
        This method takes 4 channels from input database and
        duplicats each line twice to output database)
        (input and Output can be the same channel).
        
        :param dbi:    Database InPut
        :param dbo:    DAtabase Output
        :param ix_ch:  X Input Channel  [`DB_LOCK_READONLY <geosoft.gxapi.DB_LOCK_READONLY>`]
        :param iy_ch:  Y Input Channel  [`DB_LOCK_READONLY <geosoft.gxapi.DB_LOCK_READONLY>`]
        :param iz_ch:  Z Input Channel  [`DB_LOCK_READONLY <geosoft.gxapi.DB_LOCK_READONLY>`]
        :param ig_ch:  G Input Channel  [`DB_LOCK_READONLY <geosoft.gxapi.DB_LOCK_READONLY>`]
        :param ox_ch:  X Output Channel [`DB_LOCK_READWRITE <geosoft.gxapi.DB_LOCK_READWRITE>`]
        :param oy_ch:  Y Output Channel [`DB_LOCK_READWRITE <geosoft.gxapi.DB_LOCK_READWRITE>`]
        :param oz_ch:  Z Output Channel [`DB_LOCK_READWRITE <geosoft.gxapi.DB_LOCK_READWRITE>`]
        :param angle:  Angle
        :param width:  Width
        :type  dbi:    GXDB
        :type  dbo:    GXDB
        :type  ix_ch:  int
        :type  iy_ch:  int
        :type  iz_ch:  int
        :type  ig_ch:  int
        :type  ox_ch:  int
        :type  oy_ch:  int
        :type  oz_ch:  int
        :type  angle:  float
        :type  width:  float

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        gxapi_cy.WrapDU._gradient(GXContext._get_tls_geo(), dbi, dbo, ix_ch, iy_ch, iz_ch, ig_ch, ox_ch, oy_ch, oz_ch, angle, width)
        



    @classmethod
    def grav_drift(cls, db, line, date, time, read, base, clos):
        """
        Calculate base loop closure and correct for drift.
        
        :param db:    Database
        :param line:  Line                    [`DB_LOCK_READONLY <geosoft.gxapi.DB_LOCK_READONLY>`]
        :param date:  Date                    [`DB_LOCK_READONLY <geosoft.gxapi.DB_LOCK_READONLY>`]
        :param time:  Local time (on date)    [`DB_LOCK_READONLY <geosoft.gxapi.DB_LOCK_READONLY>`]
        :param read:  Reading                 [`DB_LOCK_READONLY <geosoft.gxapi.DB_LOCK_READONLY>`]
        :param base:  Base                    [`DB_LOCK_READWRITE <geosoft.gxapi.DB_LOCK_READWRITE>`]
        :param clos:  Closure error           [`DB_LOCK_READWRITE <geosoft.gxapi.DB_LOCK_READWRITE>`]
        :type  db:    GXDB
        :type  line:  int
        :type  date:  int
        :type  time:  int
        :type  read:  int
        :type  base:  int
        :type  clos:  int

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        gxapi_cy.WrapDU._grav_drift(GXContext._get_tls_geo(), db, line, date, time, read, base, clos)
        



    @classmethod
    def grav_tide(cls, db, line, lat, lon, date, time, gmt, tide):
        """
        Calculate earth tide gravity correction.
        
        :param db:    Database
        :param line:  Line
        :param lat:   Lat  [`DB_LOCK_READONLY <geosoft.gxapi.DB_LOCK_READONLY>`]
        :param lon:   Long [`DB_LOCK_READONLY <geosoft.gxapi.DB_LOCK_READONLY>`]
        :param date:  Date [`DB_LOCK_READONLY <geosoft.gxapi.DB_LOCK_READONLY>`]
        :param time:  Local time (on date) [`DB_LOCK_READONLY <geosoft.gxapi.DB_LOCK_READONLY>`]
        :param gmt:   GMT difference (added to time to give GMT)
        :param tide:  Calculated tide [`DB_LOCK_READWRITE <geosoft.gxapi.DB_LOCK_READWRITE>`]
        :type  db:    GXDB
        :type  line:  int
        :type  lat:   int
        :type  lon:   int
        :type  date:  int
        :type  time:  int
        :type  gmt:   float
        :type  tide:  int

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        gxapi_cy.WrapDU._grav_tide(GXContext._get_tls_geo(), db, line, lat, lon, date, time, gmt, tide)
        



    @classmethod
    def grid_load(cls, db, img, xdec, ydec, trim_dum, create_index):
        """
        Load grid data to a database.
        
        :param db:            Database
        :param img:           Grid img
        :param xdec:          X decimation factor
        :param ydec:          Y decimation factor
        :param trim_dum:      0 trim leading/trailing dummies (default), 1 trim all dummies, 2 leave all dummies
        :param create_index:  Flag for creating index channel: 0 no (default), 1 yes.
        :type  db:            GXDB
        :type  img:           GXIMG
        :type  xdec:          int
        :type  ydec:          int
        :type  trim_dum:      int
        :type  create_index:  int

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        gxapi_cy.WrapDU._grid_load(GXContext._get_tls_geo(), db, img, xdec, ydec, trim_dum, create_index)
        



    @classmethod
    def grid_load_xyz(cls, db, img, ch_x, ch_y, ch_z, ch_data, xdec, ydec, trim_dum, index_ch):
        """
        Load grid data to a database using specified channels
        
        :param db:        Database
        :param img:       Grid img
        :param ch_x:      X Channel
        :param ch_y:      Y Channel
        :param ch_z:      Z Channel
        :param ch_data:   Data Channel
        :param xdec:      X decimation factor
        :param ydec:      Y decimation factor
        :param trim_dum:  0 trim leading/trailing dummies (default), 1 trim all dummies, 2 leave all dummies
        :param index_ch:  Flag for creating index channel: 0 no (default), 1 yes.
        :type  db:        GXDB
        :type  img:       GXIMG
        :type  ch_x:      int
        :type  ch_y:      int
        :type  ch_z:      int
        :type  ch_data:   int
        :type  xdec:      int
        :type  ydec:      int
        :type  trim_dum:  int
        :type  index_ch:  int

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        gxapi_cy.WrapDU._grid_load_xyz(GXContext._get_tls_geo(), db, img, ch_x, ch_y, ch_z, ch_data, xdec, ydec, trim_dum, index_ch)
        



    @classmethod
    def head(cls, db, line, i_ch, o_ch, tb, dir):
        """
        Applies a heading correction.
        
        :param db:    Database object
        :param line:  Line Symbol
        :param i_ch:  Channel to correct [`DB_LOCK_READONLY <geosoft.gxapi.DB_LOCK_READONLY>`]
        :param o_ch:  Corrected channel  [`DB_LOCK_READWRITE <geosoft.gxapi.DB_LOCK_READWRITE>`]
        :param tb:    Heading table
        :param dir:   Line direction
        :type  db:    GXDB
        :type  line:  int
        :type  i_ch:  int
        :type  o_ch:  int
        :type  tb:    GXTB
        :type  dir:   float

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** Updates channel with Direction in degrees azimuth (counter-clockwise
        relative the +Y direction).
        `GS_R8DM <geosoft.gxapi.GS_R8DM>` if the line has no data, or if there is a
        problem.
        """
        gxapi_cy.WrapDU._head(GXContext._get_tls_geo(), db, line, i_ch, o_ch, tb, dir)
        



    @classmethod
    def import_bin3(cls, db, data, template, line, flight, date, wa):
        """
        Same as `import_bin2 <geosoft.gxapi.GXDU.import_bin2>`, but returns the name of the imported line.
        
        :param db:        Database
        :param data:      Import data file name
        :param template:  Import template name
        :param line:      Optional Line name (on return, the actual line)
        :param flight:    Optional Flight number
        :param date:      Optional date
        :type  db:        GXDB
        :type  data:      str
        :type  template:  str
        :type  line:      str_ref
        :type  flight:    int
        :type  date:      float
        :type  wa:        GXWA

        .. versionadded:: 6.1

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** See `import_bin2 <geosoft.gxapi.GXDU.import_bin2>`. Because the name of the created line is
        not necessarily the value passed in (and the value passed in
        can be blank), this version returns the name of the line
        to which the data is actually imported.

        .. seealso::

            `import_bin2 <geosoft.gxapi.GXDU.import_bin2>`
        """
        line.value = gxapi_cy.WrapDU._import_bin3(GXContext._get_tls_geo(), db, data.encode(), template.encode(), line.value.encode(), flight, date, wa)
        



    @classmethod
    def imp_cb_ply(cls, db, pj, file, x_chan, y_chan):
        """
        Import concession boundary polygon file into a database
        
        :param db:      Database
        :param pj:      Projection Files Object
        :param file:    Import data file name
        :param x_chan:  X channel handle
        :param y_chan:  Y channel handle
        :type  db:      GXDB
        :type  pj:      GXPJ
        :type  file:    str
        :type  x_chan:  int
        :type  y_chan:  int

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** The polygon file is provided by Ana Christina in Brazil.
        """
        gxapi_cy.WrapDU._imp_cb_ply(GXContext._get_tls_geo(), db, pj, file.encode(), x_chan, y_chan)
        



    @classmethod
    def import_ado(cls, db, connect, table, template, line):
        """
        Import an external database table into a group using ADO.
        
        :param db:        Database
        :param connect:   Import database connection string       (overrides template value)
        :param table:     Imported table in database file (overrides template value)
        :param template:  Import template name
        :param line:      Oasis montaj line name to create (overrides template value)
        :type  db:        GXDB
        :type  connect:   str
        :type  table:     str
        :type  template:  str
        :type  line:      str

        .. versionadded:: 5.0.8

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** 1. The import template can be in the local directory or the GEOSOFT
        directory.
        
        2. Only the import template must be specified. The database connection string,
        the database table and Oasis line name are normally taken from the template
        file itself, but if these values are provided, they will override those found in the template.
        
        3. If the line already exists, the data will overwrite the existing data.
        """
        gxapi_cy.WrapDU._import_ado(GXContext._get_tls_geo(), db, connect.encode(), table.encode(), template.encode(), line.encode())
        



    @classmethod
    def import_all_ado(cls, db, connect, storage):
        """
        Import an entire external database using ADO.
        
        :param db:       Database
        :param connect:  Import database connection string
        :param storage:  :ref:`DU_STORAGE`
        :type  db:       GXDB
        :type  connect:  str
        :type  storage:  int

        .. versionadded:: 5.0.8

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** 1. For group storage, the table names are imported "as is". For line storage,
        if the table names are valid Geosoft line names, they are used as is.
        Otherwise, line names will be created with type LINE_NORMAL, starting at
        L0 and incrementing by 10 (L10, L20 etc.)
        
        2. If the line exists, the data will overwrite the existing data.
        
        3. All tables and fields will be imported.
        
        4. If connection string is of type "FILENAME=..." the connection will attempt to resolve
        it as a file database. (see also ODBCFileConnect_GUI)
        """
        gxapi_cy.WrapDU._import_all_ado(GXContext._get_tls_geo(), db, connect.encode(), storage)
        



    @classmethod
    def import_all_dao(cls, db, data, type, storage):
        """
        Import an entire external database using DAO.
        
        :param db:       Database
        :param data:     Import data file name
        :param type:     Database type
        :param storage:  :ref:`DU_STORAGE`
        :type  db:       GXDB
        :type  data:     str
        :type  type:     str
        :type  storage:  int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** 1. The file is assumed to be a DAO compliant database.
        
        2. The import data file must include the path if it is not
        in the local directory.
        
        3. For group storage, the table names are imported "as is". For line storage,
        if the table names are valid Geosoft line names, they are used as is.
        Otherwise, line names will be created with type LINE_NORMAL, starting at
        L0 and incrementing by 10 (L10, L20 etc.)
        
        4. If the line exists, the data will overwrite the existing data.
        
        5. All tables and fields will be imported.
        
        6. The following are valid type strings for DAO:
        
        MSJET       : Microsoft Access
        ODBC        : ODBC source
        dBASE III
        dBASE IV
        dBASE 5
        FoxPro 2.0
        FoxPro 2.5
        FoxPro 2.6
        Paradox 3.x
        Paradox 4.x
        Paradox 5.x
        """
        gxapi_cy.WrapDU._import_all_dao(GXContext._get_tls_geo(), db, data.encode(), type.encode(), storage)
        



    @classmethod
    def import_amira(cls, db, ra, wa):
        """
        Import an AMIRA data file.
        
        :param db:  Database
        :param ra:  AMIRA data file handle
        :param wa:  Log file handle
        :type  db:  GXDB
        :type  ra:  GXRA
        :type  wa:  GXWA

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** All the constant declarations are stored within the database
        under \\TEM\\CONSTANTS. The format is as follows:
        
            1. Lines stored in the file beginning with "/" are comments
            2. Each constant occupies a line in the file. It uses the format: CONSTANT=VALUE
        """
        gxapi_cy.WrapDU._import_amira(GXContext._get_tls_geo(), db, ra, wa)
        



    @classmethod
    def import_aseg(cls, db, template, file, data, flc, chans):
        """
        Import an ASEG-GDF data file.
        
        :param db:        Database
        :param template:  Template file name
        :param file:      Header file name
        :param data:      Data file name
        :param flc:       Flight Line Channel name
        :param chans:     Number of channels to import at one time
        :type  db:        GXDB
        :type  template:  str
        :type  file:      str
        :type  data:      str
        :type  flc:       str
        :type  chans:     int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        gxapi_cy.WrapDU._import_aseg(GXContext._get_tls_geo(), db, template.encode(), file.encode(), data.encode(), flc.encode(), chans)
        



    @classmethod
    def import_aseg_proj(cls, db, template, file, data, flc, chans, proj, x_ch, y_ch):
        """
        Import an ASEG-GDF data file (supports projections).
        
        :param db:        Database
        :param template:  Template file name
        :param file:      Header file name
        :param data:      Data file name
        :param flc:       Flight Line Channel name
        :param chans:     Number of channels to import at one time
        :param proj:      Projection file name
        :param x_ch:      Channel pair to associate projection
        :param y_ch:      Channel pair to associate projection
        :type  db:        GXDB
        :type  template:  str
        :type  file:      str
        :type  data:      str
        :type  flc:       str
        :type  chans:     int
        :type  proj:      str
        :type  x_ch:      str
        :type  y_ch:      str

        .. versionadded:: 5.0.1

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** This version supports projections
        """
        gxapi_cy.WrapDU._import_aseg_proj(GXContext._get_tls_geo(), db, template.encode(), file.encode(), data.encode(), flc.encode(), chans, proj.encode(), x_ch.encode(), y_ch.encode())
        



    @classmethod
    def import_bin(cls, db, data, template, line, flight, date):
        """
        Import blocked binary or archive ASCII data
        
        :param db:        Database
        :param data:      Import data file name
        :param template:  Import template name
        :param line:      Optional Line name (see note 3.)
        :param flight:    Optional Flight number
        :param date:      Optional date
        :type  db:        GXDB
        :type  data:      str
        :type  template:  str
        :type  line:      str
        :type  flight:    int
        :type  date:      float

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** 1. Binary import templates have extension .I2 by convention.  See
        BINARY.I2 for a description of the template format.
        Archive import templates have extension .I3 by convention. See
        ARCHIVE.I3 for a description of the template format.
        
        2. Both the import template and data file must exist.
        
        3. If a line already exists in the database, a new version is created
        unless a line name is passed in.  In this case, the specified name
        is used and the imported channels on the previous line will be
        destroyed.

        .. seealso::

            `lab_template <geosoft.gxapi.GXDU.lab_template>`
        """
        gxapi_cy.WrapDU._import_bin(GXContext._get_tls_geo(), db, data.encode(), template.encode(), line.encode(), flight, date)
        



    @classmethod
    def import_bin2(cls, db, data, template, line, flight, date, wa):
        """
        Import blocked binary or archive ASCII data with data error display
        
        :param db:        Database
        :param data:      Import data file name
        :param template:  Import template name
        :param line:      Optional Line name (see note 3.)
        :param flight:    Optional Flight number
        :param date:      Optional date
        :type  db:        GXDB
        :type  data:      str
        :type  template:  str
        :type  line:      str
        :type  flight:    int
        :type  date:      float
        :type  wa:        GXWA

        .. versionadded:: 5.1.6

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** 1. Binary import templates have extension .I2 by convention.  See
        BINARY.I2 for a description of the template format.
        Archive import templates have extension .I3 by convention. See
        ARCHIVE.I3 for a description of the template format.
        
        2. Both the import template and data file must exist.
        
        3. If a line already exists in the database, a new version is created
        unless a line name is passed in.  In this case, the specified name
        is used and the imported channels on the previous line will be
        destroyed.

        .. seealso::

            `lab_template <geosoft.gxapi.GXDU.lab_template>`
        """
        gxapi_cy.WrapDU._import_bin2(GXContext._get_tls_geo(), db, data.encode(), template.encode(), line.encode(), flight, date, wa)
        



    @classmethod
    def import_bin4(cls, db, mode, data, template, line, flight, date, wa):
        """
        Same as `import_bin2 <geosoft.gxapi.GXDU.import_bin2>` but with an import mode
        
        :param db:        Database
        :param mode:      :ref:`DU_IMPORT`
        :param data:      Import data file name
        :param template:  Import template name
        :param line:      Optional Line name (see note 3.)
        :param flight:    Optional Flight number
        :param date:      Optional date
        :type  db:        GXDB
        :type  mode:      int
        :type  data:      str
        :type  template:  str
        :type  line:      str
        :type  flight:    int
        :type  date:      float
        :type  wa:        GXWA

        .. versionadded:: 9.1

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Same as `import_bin2 <geosoft.gxapi.GXDU.import_bin2>` but with an import mode

        .. seealso::

            `import_bin2 <geosoft.gxapi.GXDU.import_bin2>`
        """
        gxapi_cy.WrapDU._import_bin4(GXContext._get_tls_geo(), db, mode, data.encode(), template.encode(), line.encode(), flight, date, wa)
        



    @classmethod
    def import_daarc500_serial(cls, db, line, file, channel, type):
        """
        Import Serial data from the RMS Instruments DAARC500.
        
        :param db:       Database object
        :param line:     Output line (`DB_LOCK_READWRITE <geosoft.gxapi.DB_LOCK_READWRITE>`)
        :param file:     Name of file to import
        :param channel:  Channel to import, 1-8
        :param type:     :ref:`GU_DAARC500_DATATYPE`
        :type  db:       GXDB
        :type  line:     int
        :type  file:     str
        :type  channel:  int
        :type  type:     int

        .. versionadded:: 7.2

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Imports data stored in a serial channel recorded
        by the RMS Instruments DAARC500 instrument, and outputs the data to
        a line in the database. The channels created depend on the input data type
        """
        gxapi_cy.WrapDU._import_daarc500_serial(GXContext._get_tls_geo(), db, line, file.encode(), channel, type)
        



    @classmethod
    def import_daarc500_serial_gps(cls, db, line, file, channel):
        """
        Import Serial GPS data from the RMS Instruments DAARC500.
        
        :param db:       Database object
        :param line:     Output line (`DB_LOCK_READWRITE <geosoft.gxapi.DB_LOCK_READWRITE>`)
        :param file:     Name of file to import
        :param channel:  Channel to import, 1-8
        :type  db:       GXDB
        :type  line:     int
        :type  file:     str
        :type  channel:  int

        .. versionadded:: 7.2

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Imports GPS data stored in a serial channel recorded
        by the RMS Instruments DAARC500 instrument, and outputs the data to
        a line in the database. Makes the following channels:
        
        Fid, UTC_Time, Latitude, Longitude, Altitude, GPS_Quality,
        NumSat (Number of satellites), GPS_HDOP (Horizontal Dilution of Position),
        Undulation, GPS_DiffAge (Age of differential channel).
        """
        gxapi_cy.WrapDU._import_daarc500_serial_gps(GXContext._get_tls_geo(), db, line, file.encode(), channel)
        



    @classmethod
    def import_dao(cls, db, data, type, table, template, line):
        """
        Import an external database table into a group using DAO.
        
        :param db:        Database
        :param data:      Import database file name   (overrides template value)
        :param type:      Import data file type       (overrides template value)
        :param table:     Imported table in database file (overrides template value)
        :param template:  Import template name
        :param line:      Oasis Montaj line name to create (overrides template value)
        :type  db:        GXDB
        :type  data:      str
        :type  type:      str
        :type  table:     str
        :type  template:  str
        :type  line:      str

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** 1. The import template can be in the local directory or the GEOSOFT
        directory.  The import data file must include the path if it is not
        in the local directory.
        
        2. Only the import template must be specified. The database file name,
        file type, the database table and Oasis line name are normally
        taken from the template file itself, but if these values are provided,
        they will override those found in the template.
        
        3. If the line already exists, the data will overwrite the existing data.
        """
        gxapi_cy.WrapDU._import_dao(GXContext._get_tls_geo(), db, data.encode(), type.encode(), table.encode(), template.encode(), line.encode())
        



    @classmethod
    def import_esri(cls, db, connect, template, line):
        """
        Import an ArcGIS Geodatabase table or feature class into a GDB group
        
        :param db:        Database
        :param connect:   Import database connection string (e.g. "d:\\Personal\\test.mdb|Table" or "d:\\File\\test.gdb|FeatureClass, overrides template value)
        :param template:  Import template name
        :param line:      Oasis montaj line name to create (overrides template value)
        :type  db:        GXDB
        :type  connect:   str
        :type  template:  str
        :type  line:      str

        .. versionadded:: 7.1

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** 1. The import template can be in the local directory or the GEOSOFT
        directory.
        
        2. Only the import template must be specified. The Geodatabase connection string
        and Oasis line name are normally taken from the template file itself,
        but if these values are provided, they will override those found in the template.
        
        3. If the line already exists, the data will overwrite the existing data.
        """
        gxapi_cy.WrapDU._import_esri(GXContext._get_tls_geo(), db, connect.encode(), template.encode(), line.encode())
        



    @classmethod
    def import_gbn(cls, db, file):
        """
        Import GBN data file.
        
        :param db:    Database
        :param file:  File name of the GBN file to import
        :type  db:    GXDB
        :type  file:  str

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        gxapi_cy.WrapDU._import_gbn(GXContext._get_tls_geo(), db, file.encode())
        



    @classmethod
    def import_oddf(cls, db, file):
        """
        Import ODDF data file.
        
        :param db:    Database
        :param file:  File name of the ODDF file to import
        :type  db:    GXDB
        :type  file:  str

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        gxapi_cy.WrapDU._import_oddf(GXContext._get_tls_geo(), db, file.encode())
        



    @classmethod
    def import_pico(cls, db, template, data, chans):
        """
        Import a Picodas data file.
        
        :param db:        Database
        :param template:  Template file name
        :param data:      Data file name
        :param chans:     Number of channels to import at one time
        :type  db:        GXDB
        :type  template:  str
        :type  data:      str
        :type  chans:     int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        gxapi_cy.WrapDU._import_pico(GXContext._get_tls_geo(), db, template.encode(), data.encode(), chans)
        



    @classmethod
    def import_ubc_mod_msh(cls, db, mesh, mods, dir, dummy):
        """
        Import UBC Mod and Msh files.
        
        :param db:     Database Object
        :param mesh:   Mesh file
        :param mods:   1-5 Mod files, delimited with "|"
        :param dir:    Import slice direction (0-2 for X,Y and Z)
        :param dummy:  Value to interpret as dummy
        :type  db:     GXDB
        :type  mesh:   str
        :type  mods:   str
        :type  dir:    int
        :type  dummy:  float

        .. versionadded:: 6.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Each slice in X,Y or Z is imported to its own line in the database
        beginning with L0.
        """
        gxapi_cy.WrapDU._import_ubc_mod_msh(GXContext._get_tls_geo(), db, mesh.encode(), mods.encode(), dir, dummy)
        



    @classmethod
    def import_usgs_post(cls, db, file):
        """
        Import USGS Post data file.
        
        :param db:    Database
        :param file:  File name of the USGS post file to import
        :type  db:    GXDB
        :type  file:  str

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        gxapi_cy.WrapDU._import_usgs_post(GXContext._get_tls_geo(), db, file.encode())
        



    @classmethod
    def import_xyz(cls, db, mode, data, template):
        """
        Import XYZ data into the database.
        
        :param db:        Database
        :param mode:      :ref:`DU_IMPORT`
        :param data:      Import data file name
        :param template:  Import template name
        :type  db:        GXDB
        :type  mode:      int
        :type  data:      str
        :type  template:  str

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** 1. The import template can be in the local directory or the GEOSOFT
        directory.  The import data file must include the path if it is not
        in the local directory.
        
        2. Both the import template and data file must exist.
        """
        gxapi_cy.WrapDU._import_xyz(GXContext._get_tls_geo(), db, mode, data.encode(), template.encode())
        



    @classmethod
    def import_xyz2(cls, db, mode, data, template, wa):
        """
        Import XYZ data into the database.
        
        :param db:        Database
        :param mode:      :ref:`DU_IMPORT`
        :param data:      Import data file name
        :param template:  Import template name
        :type  db:        GXDB
        :type  mode:      int
        :type  data:      str
        :type  template:  str
        :type  wa:        GXWA

        .. versionadded:: 5.1.6

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** 1. The import template can be in the local directory or the GEOSOFT
        directory.  The import data file must include the path if it is not
        in the local directory.
        
        2. Both the import template and data file must exist.
        """
        gxapi_cy.WrapDU._import_xyz2(GXContext._get_tls_geo(), db, mode, data.encode(), template.encode(), wa)
        



    @classmethod
    def import_io_gas(cls, db, data_csv, template):
        """
        Import data columns from an ioGAS data file.
        
        :param db:        Database
        :param data_csv:  Input data.csv file name
        :param template:  Input template file name
        :type  db:        GXDB
        :type  data_csv:  str
        :type  template:  str

        .. versionadded:: 8.5

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** 1. All columns in the speficied ioGAS data file will be imported.
        2. If a line already exists, the data will overwrite the existing data.
        """
        gxapi_cy.WrapDU._import_io_gas(GXContext._get_tls_geo(), db, data_csv.encode(), template.encode())
        



    @classmethod
    def index_order(cls, db, line, in_ch, ch):
        """
        Change the order of a channel using an index channel.
        
        :param db:     Database
        :param line:   Line symbol
        :param in_ch:  Ordered index channel (should be int) [`DB_LOCK_READONLY <geosoft.gxapi.DB_LOCK_READONLY>`]
        :param ch:     Channel to reorder [`DB_LOCK_READWRITE <geosoft.gxapi.DB_LOCK_READWRITE>`]
        :type  db:     GXDB
        :type  line:   int
        :type  in_ch:  int
        :type  ch:     int

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        gxapi_cy.WrapDU._index_order(GXContext._get_tls_geo(), db, line, in_ch, ch)
        



    @classmethod
    def interp(cls, db, line, i_ch, o_ch, inside, outside):
        """
        Replace all dummies by interpolating from valid data.
        
        :param db:       Database
        :param line:     Line handle
        :param i_ch:     Channel to interpolate [`DB_LOCK_READONLY <geosoft.gxapi.DB_LOCK_READONLY>`]
        :param o_ch:     Output interpolated channel [`DB_LOCK_READWRITE <geosoft.gxapi.DB_LOCK_READWRITE>`]
        :param inside:   :ref:`DU_INTERP`
        :param outside:  :ref:`DU_INTERP_EDGE`
        :type  db:       GXDB
        :type  line:     int
        :type  i_ch:     int
        :type  o_ch:     int
        :type  inside:   int
        :type  outside:  int

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        gxapi_cy.WrapDU._interp(GXContext._get_tls_geo(), db, line, i_ch, o_ch, inside, outside)
        



    @classmethod
    def interp_gap(cls, db, line, i_ch, o_ch, inside, outside, gap, extend):
        """
        Replace all dummies by interpolating from valid data.
        
        :param db:       Database
        :param line:     Line handle
        :param i_ch:     Channel to interpolate [`DB_LOCK_READONLY <geosoft.gxapi.DB_LOCK_READONLY>`]
        :param o_ch:     Output interpolated channel [`DB_LOCK_READWRITE <geosoft.gxapi.DB_LOCK_READWRITE>`]
        :param inside:   :ref:`DU_INTERP`
        :param outside:  :ref:`DU_INTERP_EDGE`
        :param gap:      Maximum gap to interpolate (fiducials)
        :param extend:   Maximum items to extend at ends.
        :type  db:       GXDB
        :type  line:     int
        :type  i_ch:     int
        :type  o_ch:     int
        :type  inside:   int
        :type  outside:  int
        :type  gap:      int
        :type  extend:   int

        .. versionadded:: 8.4

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        gxapi_cy.WrapDU._interp_gap(GXContext._get_tls_geo(), db, line, i_ch, o_ch, inside, outside, gap, extend)
        



    @classmethod
    def intersect(cls, db, x_chan, y_chan, z_chan, tol, file):
        """
        Create Tie Line & Normal Line intersect table.
        
        :param db:      Database
        :param x_chan:  X Channel [`DB_LOCK_READONLY <geosoft.gxapi.DB_LOCK_READONLY>`]
        :param y_chan:  Y Channel [`DB_LOCK_READONLY <geosoft.gxapi.DB_LOCK_READONLY>`]
        :param z_chan:  Z Channel [`DB_LOCK_READONLY <geosoft.gxapi.DB_LOCK_READONLY>`]
        :param tol:     Intersection tolerance
        :param file:    Output Table file Name
        :type  db:      GXDB
        :type  x_chan:  int
        :type  y_chan:  int
        :type  z_chan:  int
        :type  tol:     float
        :type  file:    str

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        gxapi_cy.WrapDU._intersect(GXContext._get_tls_geo(), db, x_chan, y_chan, z_chan, tol, file.encode())
        



    @classmethod
    def intersect_all(cls, db, x_chan, y_chan, z_chan, tol, file):
        """
        Create line intersect table from all lines.
        
        :param db:      Database
        :param x_chan:  X Channel [`DB_LOCK_READONLY <geosoft.gxapi.DB_LOCK_READONLY>`]
        :param y_chan:  Y Channel [`DB_LOCK_READONLY <geosoft.gxapi.DB_LOCK_READONLY>`]
        :param z_chan:  Z Channel [`DB_LOCK_READONLY <geosoft.gxapi.DB_LOCK_READONLY>`]
        :param tol:     Intersection tolerance
        :param file:    Output Table file Name
        :type  db:      GXDB
        :type  x_chan:  int
        :type  y_chan:  int
        :type  z_chan:  int
        :type  tol:     float
        :type  file:    str

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        gxapi_cy.WrapDU._intersect_all(GXContext._get_tls_geo(), db, x_chan, y_chan, z_chan, tol, file.encode())
        



    @classmethod
    def intersect_gd_bto_tbl(cls, db, tbl):
        """
        Create a new intersection table from an intersection database.
        
        :param db:   Input Intersection Database name
        :param tbl:  Output intersection TBL
        :type  db:   str
        :type  tbl:  str

        .. versionadded:: 7.1

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** If the TBL exists, it is overwritten.
        """
        gxapi_cy.WrapDU._intersect_gd_bto_tbl(GXContext._get_tls_geo(), db.encode(), tbl.encode())
        



    @classmethod
    def intersect_old(cls, db, x_chan, y_chan, z_chan, in_file, out_file):
        """
        Use existing intersection table and re-calculate miss-ties.
        
        :param db:        Database
        :param x_chan:    X Channel [`DB_LOCK_READONLY <geosoft.gxapi.DB_LOCK_READONLY>`]
        :param y_chan:    Y Channel [`DB_LOCK_READONLY <geosoft.gxapi.DB_LOCK_READONLY>`]
        :param z_chan:    Z Channel [`DB_LOCK_READONLY <geosoft.gxapi.DB_LOCK_READONLY>`]
        :param in_file:   Input Table file name
        :param out_file:  Output Table file Name
        :type  db:        GXDB
        :type  x_chan:    int
        :type  y_chan:    int
        :type  z_chan:    int
        :type  in_file:   str
        :type  out_file:  str

        .. versionadded:: 5.1.4

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** Reads intersection information from an existing intersect
        table and looks up the values at the intersections for the
        input Z channel. This makes it unnecessary to re-calculate
        the intersections every time if you want to determine
        miss-ties using different Z channels, or the same Z channel
        after processing levelling corrections. Existing intersections
        whose locations do not exist in the database are ignored.
        """
        gxapi_cy.WrapDU._intersect_old(GXContext._get_tls_geo(), db, x_chan, y_chan, z_chan, in_file.encode(), out_file.encode())
        



    @classmethod
    def intersect_tb_lto_gdb(cls, tbl, db):
        """
        Create a new intersection database from an intersection table.
        
        :param tbl:  Input intersection TBL
        :param db:   Output Intersection Database name
        :type  tbl:  str
        :type  db:   str

        .. versionadded:: 7.1

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** If the GDB exists, it is deleted, so it should not
        be loaded.
        The database is split by Tie lines (or whatever lines are found in column 3
        of the TBL file.
        """
        gxapi_cy.WrapDU._intersect_tb_lto_gdb(GXContext._get_tls_geo(), tbl.encode(), db.encode())
        



    @classmethod
    def lab_template(cls, data, template, type, delimit, name_off, unit_off, data_off, sample_type, data_type):
        """
        Makes a default template from a lab assay file.
        
        :param data:         Data file name
        :param template:     New template name
        :param type:         :ref:`DU_LAB_TYPE`
        :param delimit:      Delimiter string
        :param name_off:     Offset to column labels line (0 for first line)
        :param unit_off:     Offset to unit labels line, -1 if none
        :param data_off:     Offset to first line that contains data
        :param sample_type:  Sample channel element type, recommend -10 for 10-character ASCII, or `GS_LONG <geosoft.gxapi.GS_LONG>` for numbers.
        :param data_type:    Default channel element type, recommend `GS_FLOAT <geosoft.gxapi.GS_FLOAT>`
        :type  data:         str
        :type  template:     str
        :type  type:         int
        :type  delimit:      str
        :type  name_off:     int
        :type  unit_off:     int
        :type  data_off:     int
        :type  sample_type:  int
        :type  data_type:    int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** The template can be used to import the file using
        sImportBIN_DU.
        
        The first column is assumed to be the sample number.
        
        If the unit label line is the same as the column label
        line, column labels are assummed to be followed by
        unit labels using the format "Au-ppm", "Au ppm" or
        "Au(ppm)".
        
        The number of channels is determined from the number of
        columns in the data channel.  If there are more column
        labels or unit labels, the last labels are assumed to
        be correct.  If there are fewer line labels, default
        labels "Col_n", where n is the column number, will be
        created and no unit labels will be defined.

        .. seealso::

            `import_bin <geosoft.gxapi.GXDU.import_bin>`
        """
        gxapi_cy.WrapDU._lab_template(GXContext._get_tls_geo(), data.encode(), template.encode(), type, delimit.encode(), name_off, unit_off, data_off, sample_type, data_type)
        



    @classmethod
    def load_gravity(cls, db, reg, line, data):
        """
        Load a gravity survey file
        
        :param db:    Database
        :param reg:   `GXREG <geosoft.gxapi.GXREG>` to hold constant data
        :param line:  Line in which to load data
        :param data:  Gravity data file
        :type  db:    GXDB
        :type  reg:   GXREG
        :type  line:  int
        :type  data:  str

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** See GRAVITY.`GXDAT <geosoft.gxapi.GXDAT>` for a description of the file format.
        
        Existing data in the line will be replaced.
        
        The following `GXREG <geosoft.gxapi.GXREG>` parameters will be set if they appear
        in the data file:
        default
        OPERATOR             ""
        DATE                 none
        INSTRUMENT           ""
        INSTRUMENT_SCALE     "1.0"
        BASE_GRAVITY         "0.0"
        FORMULA              "1967"
        GMT_DIFF             "0.0"
        DISTANCE_UNITS       "m"
        DENSITY_EARTH        "2.67"
        DENSITY_WATER        "1.0"
        DENSITY_ICE          "0.95"
        MAP_PROJECTION       ""
        
        If the corresponding constant is not specified and the
        `GXREG <geosoft.gxapi.GXREG>` already has the constant defined, it is not changed.
        If the constant is not defined and it is not already in
        the `GXREG <geosoft.gxapi.GXREG>`, the indicated default will be set.
        """
        gxapi_cy.WrapDU._load_gravity(GXContext._get_tls_geo(), db, reg, line, data.encode())
        



    @classmethod
    def load_gravity_cg6(cls, db, data):
        """
        Load a CG-6 gravity survey file.
        
        :param db:    Database
        :param data:  Gravity data file
        :type  db:    GXDB
        :type  data:  str

        .. versionadded:: 9.3.1

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** Has its own format - space-delimited columns of data
        """
        gxapi_cy.WrapDU._load_gravity_cg6(GXContext._get_tls_geo(), db, data.encode())
        



    @classmethod
    def load_ltb(cls, db, line, ltb, mode):
        """
        Load `GXLTB <geosoft.gxapi.GXLTB>` into a database line.
        
        :param db:    Database
        :param line:  Line
        :param ltb:   Table
        :param mode:  :ref:`DU_LOADLTB`
        :type  db:    GXDB
        :type  line:  int
        :type  ltb:   GXLTB
        :type  mode:  int

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** A new channel will be created for all `GXLTB <geosoft.gxapi.GXLTB>` fields
        that do not already exist.
        The `GXLTB <geosoft.gxapi.GXLTB>` field type will be double if all entries can be
        converted to double, otherwise it will be a string type
        set to the larger of 16 characters or the longest string
        in the field.
        
        For _APPEND, the `GXLTB <geosoft.gxapi.GXLTB>` data is simply added the end of each
        channel.  `re_fid_all_ch <geosoft.gxapi.GXDU.re_fid_all_ch>` can be used to re-fid data to
        match a specifc channel and there-by case all channels to be
        the same length before appending data.
        """
        gxapi_cy.WrapDU._load_ltb(GXContext._get_tls_geo(), db, line, ltb, mode)
        



    @classmethod
    def make_fid(cls, db, line, i_ch, o_ch):
        """
        Make a fiducial channel based on an existing channel.
        
        :param db:    Database object
        :param line:  Line Symbol
        :param i_ch:  Base channel [`DB_LOCK_READONLY <geosoft.gxapi.DB_LOCK_READONLY>`]
        :param o_ch:  New fiducial channel [`DB_LOCK_READWRITE <geosoft.gxapi.DB_LOCK_READWRITE>`]
        :type  db:    GXDB
        :type  line:  int
        :type  i_ch:  int
        :type  o_ch:  int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        gxapi_cy.WrapDU._make_fid(GXContext._get_tls_geo(), db, line, i_ch, o_ch)
        



    @classmethod
    def mask(cls, db, line, i_ch, m_ch):
        """
        Mask dummies in one channel against another.
        
        :param db:    Database
        :param line:  Line handle
        :param i_ch:  Channel to mask [`DB_LOCK_READWRITE <geosoft.gxapi.DB_LOCK_READWRITE>`]
        :param m_ch:  Mask channel [`DB_LOCK_READONLY <geosoft.gxapi.DB_LOCK_READONLY>`]
        :type  db:    GXDB
        :type  line:  int
        :type  i_ch:  int
        :type  m_ch:  int

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        gxapi_cy.WrapDU._mask(GXContext._get_tls_geo(), db, line, i_ch, m_ch)
        



    @classmethod
    def math(cls, db, line, exp):
        """
        Apply an expression to the database
        
        :param db:    Database
        :param line:  Line handle
        :param exp:   Math expression object (`GXEXP <geosoft.gxapi.GXEXP>`)
        :type  db:    GXDB
        :type  line:  int
        :type  exp:   GXEXP

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** The MATH_DU method will READWRITE lock channels on the left
        side of expressions and READONLY lock channels on the right
        side of expressions.  Channels are unlocked before returning.
        Therefore, channels on the left side of an expression cannot
        be locked READONLY because the `math <geosoft.gxapi.GXDU.math>` attempt to lock the
        channel READWRITE will fail.  Similarly, channels on the right
        side of an expression cannot be locked READWRITE because
        `math <geosoft.gxapi.GXDU.math>`'s attempt to lock the channels READONLY will fail.
        
        If this is confusing, just make sure no channels used in the
        expression are locked before calling `math <geosoft.gxapi.GXDU.math>`.

        .. seealso::

            `GXEXP <geosoft.gxapi.GXEXP>`
        """
        gxapi_cy.WrapDU._math(GXContext._get_tls_geo(), db, line, exp)
        



    @classmethod
    def merge_line(cls, db, i_line, m_line, o_line, mode):
        """
        Merge a line a the fiducial and copies any data past
        that fiducial into the new line.
        
        :param db:      Database
        :param i_line:  Input Line1 [`DB_LOCK_READONLY <geosoft.gxapi.DB_LOCK_READONLY>`]
        :param m_line:  Input Line2 [`DB_LOCK_READONLY <geosoft.gxapi.DB_LOCK_READONLY>`]
        :param o_line:  Output Line [`DB_LOCK_READWRITE <geosoft.gxapi.DB_LOCK_READWRITE>`]
        :param mode:    :ref:`DU_MERGE`
        :type  db:      GXDB
        :type  i_line:  int
        :type  m_line:  int
        :type  o_line:  int
        :type  mode:    int

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        gxapi_cy.WrapDU._merge_line(GXContext._get_tls_geo(), db, i_line, m_line, o_line, mode)
        



    @classmethod
    def mod_fid_range(cls, db, ln, fid_start, incr, start_index, num, opt):
        """
        Insert/Append/Delete a range of fids.
        
        :param db:           Database
        :param ln:           Line
        :param fid_start:    Base fid start
        :param incr:         Base fid increment
        :param start_index:  Start index (can be negative)
        :param num:          Number of fids
        :param opt:          :ref:`DU_MODFID`
        :type  db:           GXDB
        :type  ln:           int
        :type  fid_start:    float
        :type  incr:         float
        :type  start_index:  int
        :type  num:          int
        :type  opt:          int

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** Channels that do not have the same fid start or fid
        increment are not processed.
        
        Protected channels are modified automatically.
        """
        gxapi_cy.WrapDU._mod_fid_range(GXContext._get_tls_geo(), db, ln, fid_start, incr, start_index, num, opt)
        



    @classmethod
    def move(cls, db, line, i_ch, c_ch, o_ch, mode):
        """
        Move/correct a channel to a control channel.
        
        :param db:    Database
        :param line:  Line Handle to Apply this to
        :param i_ch:  Input channel   [`DB_LOCK_READONLY <geosoft.gxapi.DB_LOCK_READONLY>`]
        :param c_ch:  Control channel [`DB_LOCK_READONLY <geosoft.gxapi.DB_LOCK_READONLY>`]
        :param o_ch:  Result channel  [`DB_LOCK_READWRITE <geosoft.gxapi.DB_LOCK_READWRITE>`]
        :param mode:  :ref:`DU_MOVE`
        :type  db:    GXDB
        :type  line:  int
        :type  i_ch:  int
        :type  c_ch:  int
        :type  o_ch:  int
        :type  mode:  int

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** The input channel is moved to the absolute location
        of the control channel.
        """
        gxapi_cy.WrapDU._move(GXContext._get_tls_geo(), db, line, i_ch, c_ch, o_ch, mode)
        



    @classmethod
    def nl_filt(cls, db, line, i_ch, o_ch, width, tol):
        """
        This method applies a non-linear filter to the specified
        line/channel and places the output in the output channel.
        
        :param db:     Database
        :param line:   Line handle
        :param i_ch:   Channel to filter [`DB_LOCK_READONLY <geosoft.gxapi.DB_LOCK_READONLY>`]
        :param o_ch:   Output filtered channel [`DB_LOCK_READWRITE <geosoft.gxapi.DB_LOCK_READWRITE>`]
        :param width:  Filter Width
        :param tol:    Filter Tolerance, 0 for 10% of Std. Dev.
        :type  db:     GXDB
        :type  line:   int
        :type  i_ch:   int
        :type  o_ch:   int
        :type  width:  int
        :type  tol:    float

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        gxapi_cy.WrapDU._nl_filt(GXContext._get_tls_geo(), db, line, i_ch, o_ch, width, tol)
        



    @classmethod
    def normal(cls, db, ch, ignore):
        """
        Set fid of all channels to match a specified channel.
        
        :param db:      Database handle
        :param ch:      Base Channel for normalization.  [`DB_LOCK_READONLY <geosoft.gxapi.DB_LOCK_READONLY>`]
        :param ignore:  Ignore write protection on channels?
        :type  db:      GXDB
        :type  ch:      int
        :type  ignore:  bool

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        .. seealso::

            `re_fid_all_ch <geosoft.gxapi.GXDU.re_fid_all_ch>`
        """
        gxapi_cy.WrapDU._normal(GXContext._get_tls_geo(), db, ch, ignore)
        



    @classmethod
    def poly_fill(cls, db, line, x_chan, y_chan, r_chan, pply, dummy):
        """
        Fill using a polygon with a value of 1.
        
        :param db:      Database
        :param line:    Line Handle
        :param x_chan:  X Channel [`DB_LOCK_READONLY <geosoft.gxapi.DB_LOCK_READONLY>`]
        :param y_chan:  Y Channel [`DB_LOCK_READONLY <geosoft.gxapi.DB_LOCK_READONLY>`]
        :param r_chan:  Channel to fill [`DB_LOCK_READWRITE <geosoft.gxapi.DB_LOCK_READWRITE>`]
        :param pply:    Polygon Object to use
        :param dummy:   :ref:`DU_FILL`
        :type  db:      GXDB
        :type  line:    int
        :type  x_chan:  int
        :type  y_chan:  int
        :type  r_chan:  int
        :type  pply:    GXPLY
        :type  dummy:   int

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        gxapi_cy.WrapDU._poly_fill(GXContext._get_tls_geo(), db, line, x_chan, y_chan, r_chan, pply, dummy)
        



    @classmethod
    def poly_mask(cls, db, line, x_chan, y_chan, r_chan, pply, dummy):
        """
        Mask against a polygon.
        
        :param db:      Database
        :param line:    Line Handle
        :param x_chan:  X Channel [`DB_LOCK_READONLY <geosoft.gxapi.DB_LOCK_READONLY>`]
        :param y_chan:  Y Channel [`DB_LOCK_READONLY <geosoft.gxapi.DB_LOCK_READONLY>`]
        :param r_chan:  Channel to mask [`DB_LOCK_READWRITE <geosoft.gxapi.DB_LOCK_READWRITE>`]
        :param pply:    Polygon Object to use
        :param dummy:   :ref:`DU_MASK`
        :type  db:      GXDB
        :type  line:    int
        :type  x_chan:  int
        :type  y_chan:  int
        :type  r_chan:  int
        :type  pply:    GXPLY
        :type  dummy:   int

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        gxapi_cy.WrapDU._poly_mask(GXContext._get_tls_geo(), db, line, x_chan, y_chan, r_chan, pply, dummy)
        



    @classmethod
    def project_data(cls, db, line, ix_ch, iy_ch, ox_ch, oy_ch, pj):
        """
        Project X,Y channels
        
        :param db:     Database
        :param line:   Line Handle to project
        :param ix_ch:  X Input Channel  [`DB_LOCK_READONLY <geosoft.gxapi.DB_LOCK_READONLY>`]
        :param iy_ch:  Y Input Channel  [`DB_LOCK_READONLY <geosoft.gxapi.DB_LOCK_READONLY>`]
        :param ox_ch:  X Output Channel [`DB_LOCK_READWRITE <geosoft.gxapi.DB_LOCK_READWRITE>`]
        :param oy_ch:  Y Output Channel [`DB_LOCK_READWRITE <geosoft.gxapi.DB_LOCK_READWRITE>`]
        :param pj:     Projection object to Apply
        :type  db:     GXDB
        :type  line:   int
        :type  ix_ch:  int
        :type  iy_ch:  int
        :type  ox_ch:  int
        :type  oy_ch:  int
        :type  pj:     GXPJ

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** Output channels can be the same as input channels
        """
        gxapi_cy.WrapDU._project_data(GXContext._get_tls_geo(), db, line, ix_ch, iy_ch, ox_ch, oy_ch, pj)
        



    @classmethod
    def project_xyz(cls, db, line, ix_ch, iy_ch, iz_ch, ox_ch, oy_ch, oz_ch, pj):
        """
        Project X,Y,Z channels from one system to another.
        
        :param db:     Database
        :param line:   Line Handle to project
        :param ix_ch:  X Input Channel  [`DB_LOCK_READONLY <geosoft.gxapi.DB_LOCK_READONLY>`]
        :param iy_ch:  Y Input Channel  [`DB_LOCK_READONLY <geosoft.gxapi.DB_LOCK_READONLY>`]
        :param iz_ch:  Z Input Channel  [`DB_LOCK_READONLY <geosoft.gxapi.DB_LOCK_READONLY>`]
        :param ox_ch:  X Output Channel [`DB_LOCK_READWRITE <geosoft.gxapi.DB_LOCK_READWRITE>`]
        :param oy_ch:  Y Output Channel [`DB_LOCK_READWRITE <geosoft.gxapi.DB_LOCK_READWRITE>`]
        :param oz_ch:  Z Output Channel [`DB_LOCK_READWRITE <geosoft.gxapi.DB_LOCK_READWRITE>`]
        :param pj:     Projection object to Apply
        :type  db:     GXDB
        :type  line:   int
        :type  ix_ch:  int
        :type  iy_ch:  int
        :type  iz_ch:  int
        :type  ox_ch:  int
        :type  oy_ch:  int
        :type  oz_ch:  int
        :type  pj:     GXPJ

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** Output channels can be the same as input channels
        """
        gxapi_cy.WrapDU._project_xyz(GXContext._get_tls_geo(), db, line, ix_ch, iy_ch, iz_ch, ox_ch, oy_ch, oz_ch, pj)
        



    @classmethod
    def proj_points(cls, db, line, ix_ch, iy_ch, iz_ch, ox_ch, oy_ch, oz_ch, i_name_chan, i_datum_chan, i_method_chan, i_unit_chan, il_datum_chan, o_name_chan, o_datum_chan, o_method_chan, o_unit_chan, ol_datum_chan, error_chan, force_local_datum):
        """
        Project X,Y(Z) channels with different projections
        
        :param db:                 Database
        :param line:               Line Handle to project
        :param ix_ch:              X Input Channel  [`DB_LOCK_READONLY <geosoft.gxapi.DB_LOCK_READONLY>`]
        :param iy_ch:              Y Input Channel  [`DB_LOCK_READONLY <geosoft.gxapi.DB_LOCK_READONLY>`]
        :param iz_ch:              Z Input Channel  [`DB_LOCK_READONLY <geosoft.gxapi.DB_LOCK_READONLY>`] (can be DB_NULL_SYMB)
        :param ox_ch:              X Output Channel [`DB_LOCK_READWRITE <geosoft.gxapi.DB_LOCK_READWRITE>`]
        :param oy_ch:              Y Output Channel [`DB_LOCK_READWRITE <geosoft.gxapi.DB_LOCK_READWRITE>`]
        :param oz_ch:              Z Output Channel [`DB_LOCK_READWRITE <geosoft.gxapi.DB_LOCK_READWRITE>`] (can be DB_NULL_SYMB)
        :param i_name_chan:        Input Name Channel   [`DB_LOCK_READONLY <geosoft.gxapi.DB_LOCK_READONLY>`]
        :param i_datum_chan:       Input Datum Channel  [`DB_LOCK_READONLY <geosoft.gxapi.DB_LOCK_READONLY>`]
        :param i_method_chan:      Input Method Channel [`DB_LOCK_READONLY <geosoft.gxapi.DB_LOCK_READONLY>`]
        :param i_unit_chan:        Input Unit Channel   [`DB_LOCK_READONLY <geosoft.gxapi.DB_LOCK_READONLY>`]
        :param il_datum_chan:      Input Local Datum Channel [`DB_LOCK_READONLY <geosoft.gxapi.DB_LOCK_READONLY>`]
        :param o_name_chan:        Output Name Channel  [`DB_LOCK_READONLY <geosoft.gxapi.DB_LOCK_READONLY>`]
        :param o_datum_chan:       Output Datum Channel [`DB_LOCK_READONLY <geosoft.gxapi.DB_LOCK_READONLY>`]
        :param o_method_chan:      Output Method Channel [`DB_LOCK_READONLY <geosoft.gxapi.DB_LOCK_READONLY>`]
        :param o_unit_chan:        Output Unit Channel  [`DB_LOCK_READONLY <geosoft.gxapi.DB_LOCK_READONLY>`]
        :param ol_datum_chan:      Output Local Datum Channel [`DB_LOCK_READONLY <geosoft.gxapi.DB_LOCK_READONLY>`]
        :param error_chan:         Error Channel [`DB_LOCK_READWRITE <geosoft.gxapi.DB_LOCK_READWRITE>`]
        :param force_local_datum:  Force Local Datum Shifts?
        :type  db:                 GXDB
        :type  line:               int
        :type  ix_ch:              int
        :type  iy_ch:              int
        :type  iz_ch:              int
        :type  ox_ch:              int
        :type  oy_ch:              int
        :type  oz_ch:              int
        :type  i_name_chan:        int
        :type  i_datum_chan:       int
        :type  i_method_chan:      int
        :type  i_unit_chan:        int
        :type  il_datum_chan:      int
        :type  o_name_chan:        int
        :type  o_datum_chan:       int
        :type  o_method_chan:      int
        :type  o_unit_chan:        int
        :type  ol_datum_chan:      int
        :type  error_chan:         int
        :type  force_local_datum:  int

        .. versionadded:: 6.3

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** Output channels can be the same as input channels
        """
        gxapi_cy.WrapDU._proj_points(GXContext._get_tls_geo(), db, line, ix_ch, iy_ch, iz_ch, ox_ch, oy_ch, oz_ch, i_name_chan, i_datum_chan, i_method_chan, i_unit_chan, il_datum_chan, o_name_chan, o_datum_chan, o_method_chan, o_unit_chan, ol_datum_chan, error_chan, force_local_datum)
        



    @classmethod
    def qc_init_separation(cls, db, sep, dir):
        """
        Creates the nearest line channels for line separation QC.
        
        :param db:   Database
        :param sep:  Nominal Line separation
        :param dir:  Nominal Line direction
        :type  db:   GXDB
        :type  sep:  float
        :type  dir:  float

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** This must be called before QCSeparation_DU. It uses a pager to
        establish the relative positions of the selected lines, then,
        for every point determines the closest point in another line to
        the left and to the right (as determined by looking in the
        direction of the line.) These distances are stored to two new
        channels in the database, "Closest_Left" and "Closest_Right"
        """
        gxapi_cy.WrapDU._qc_init_separation(GXContext._get_tls_geo(), db, sep, dir)
        



    @classmethod
    def qc_survey_plan(cls, db, wa, pply, sl_spa, sl_azi, slx, sly, sl_sta, sl_inc, tl_spa, tl_azi, tlx, tly, tl_sta, tl_inc, type, sample_spacing, extend_outside):
        """
        Create a database containing proposed survey plan in a `GXPLY <geosoft.gxapi.GXPLY>`
        
        :param db:              Database to save proposed survey plan
        :param wa:              `GXWA <geosoft.gxapi.GXWA>` to save survey plan summary
        :param pply:            Boundary `GXPLY <geosoft.gxapi.GXPLY>`
        :param sl_spa:          Survey line spacing
        :param sl_azi:          Survey line azimuth
        :param slx:             Survey line reference X coordinate
        :param sly:             Survey line reference Y coordinate
        :param sl_sta:          Survey line starting number of LINES
        :param sl_inc:          Line number increment for survey line
        :param tl_spa:          Tie line spacing
        :param tl_azi:          Tie line azimuth
        :param tlx:             Tie line reference X coordinate
        :param tly:             Tie line reference Y coordinate
        :param tl_sta:          Tie line starting number of LINES
        :param tl_inc:          Line number increment for Tie line
        :param type:            :ref:`QC_PLAN_TYPE`
        :param sample_spacing:  Sample spacing (spacing between points in lines)
        :param extend_outside:  Spacing to extend lines outside polygon
        :type  db:              GXDB
        :type  wa:              GXWA
        :type  pply:            GXPLY
        :type  sl_spa:          float
        :type  sl_azi:          float
        :type  slx:             float
        :type  sly:             float
        :type  sl_sta:          int
        :type  sl_inc:          int
        :type  tl_spa:          float
        :type  tl_azi:          float
        :type  tlx:             float
        :type  tly:             float
        :type  tl_sta:          int
        :type  tl_inc:          int
        :type  type:            int
        :type  sample_spacing:  float
        :type  extend_outside:  float
        :rtype:                 int

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** The LINE on which has the reference (X,Y) will have the starting Line number
        The lines on the right hand side of the reference line (while looking
        into azimuth of ref. line) have increasing line numbers. The lines
        on the left hand side have the decreasing line numbers from the starting
        number. Returns an error code or 0 (if successful)
        """
        ret_val = gxapi_cy.WrapDU._qc_survey_plan(GXContext._get_tls_geo(), db, wa, pply, sl_spa, sl_azi, slx, sly, sl_sta, sl_inc, tl_spa, tl_azi, tlx, tly, tl_sta, tl_inc, type, sample_spacing, extend_outside)
        return ret_val



    @classmethod
    def direction(cls, db, line, x_ch, y_ch):
        """
        Returns the direction of a line.
        
        :param db:    Database Object
        :param line:  Line Symbol
        :param x_ch:  X reference channel [`DB_LOCK_READONLY <geosoft.gxapi.DB_LOCK_READONLY>`]
        :param y_ch:  Y reference channel [`DB_LOCK_READONLY <geosoft.gxapi.DB_LOCK_READONLY>`]
        :type  db:    GXDB
        :type  line:  int
        :type  x_ch:  int
        :type  y_ch:  int

        :returns:     direction in degrees azimuth (clockwise relative
                      the +Y direction).
                      `GS_R8DM <geosoft.gxapi.GS_R8DM>` if the line has no data, or if there is a
                      problem.  Problems will register errors.
        :rtype:       float

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** The direction is calculated from the first and last
        non-dummy locations in the X and Y reference channels.
        """
        ret_val = gxapi_cy.WrapDU._direction(GXContext._get_tls_geo(), db, line, x_ch, y_ch)
        return ret_val



    @classmethod
    def re_fid(cls, db, line, in_ch, ref_ch, out_ch, mode, start, incr, gap):
        """
        Re-fid a channel based on a reference channel
        
        :param db:      Database Object
        :param line:    Line Symbol
        :param in_ch:   Original Channel [`DB_LOCK_READONLY <geosoft.gxapi.DB_LOCK_READONLY>`]  "Y" values
        :param ref_ch:  Reference Channel [`DB_LOCK_READONLY <geosoft.gxapi.DB_LOCK_READONLY>`] "X" locations
        :param out_ch:  Output Channel [`DB_LOCK_READWRITE <geosoft.gxapi.DB_LOCK_READWRITE>`]
        :param mode:    :ref:`DU_REFID`
        :param start:   Start Fid, if `GS_R8DM <geosoft.gxapi.GS_R8DM>`, use ref channel minimum
        :param incr:    Fid increment, if `GS_R8DM <geosoft.gxapi.GS_R8DM>` use nominal spacing of the reference channel.
        :param gap:     Maximum gap to interpolate across
        :type  db:      GXDB
        :type  line:    int
        :type  in_ch:   int
        :type  ref_ch:  int
        :type  out_ch:  int
        :type  mode:    int
        :type  start:   float
        :type  incr:    float
        :type  gap:     float

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** The original channel can be an array channel, in which case
        the columns (up to the number of columns available in the output)
        are individually interpolated. If the number of
        columns in the output channel is more than the input channel,
        the remaining columns are dummied.
        
        This function is fundamentally different in behaviour from `re_fid_ch <geosoft.gxapi.GXDU.re_fid_ch>`.
        The values in the Reference channel in `re_fid <geosoft.gxapi.GXDU.re_fid>` are the "X" locations
        corresponding to the "Y" locations in the "Original Channel". Output
        Channel values are calculated at the new "X" locations specified by
        the Start Fid and the Fid Increment.
        """
        gxapi_cy.WrapDU._re_fid(GXContext._get_tls_geo(), db, line, in_ch, ref_ch, out_ch, mode, start, incr, gap)
        



    @classmethod
    def re_fid_all_ch(cls, db, line, ref_ch):
        """
        Simple re-fid of all channels based on a reference channel
        
        :param db:      Database Object
        :param line:    Line Symbol
        :param ref_ch:  Reference Channel [`DB_LOCK_READONLY <geosoft.gxapi.DB_LOCK_READONLY>`]
        :type  db:      GXDB
        :type  line:    int
        :type  ref_ch:  int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Channels can be array channels, in which case
        the columns are individually re-fidded.

        .. seealso::

            `normal <geosoft.gxapi.GXDU.normal>`
        """
        gxapi_cy.WrapDU._re_fid_all_ch(GXContext._get_tls_geo(), db, line, ref_ch)
        



    @classmethod
    def re_fid_ch(cls, db, line, ref_ch, ch):
        """
        Simple re-fid of a channel based on a reference channel
        
        :param db:      Database Object
        :param line:    Line Symbol
        :param ref_ch:  Reference Channel [`DB_LOCK_READONLY <geosoft.gxapi.DB_LOCK_READONLY>`]
        :param ch:      Channel to refid  [`DB_LOCK_READWRITE <geosoft.gxapi.DB_LOCK_READWRITE>`]
        :type  db:      GXDB
        :type  line:    int
        :type  ref_ch:  int
        :type  ch:      int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** The original channel can be an array channel, in which case
        the columns are individually re-fidded.
        
        `re_fid_ch <geosoft.gxapi.GXDU.re_fid_ch>` resamples the "Channel to refid" to the "Reference Channel" Fid
        range and increment.
        """
        gxapi_cy.WrapDU._re_fid_ch(GXContext._get_tls_geo(), db, line, ref_ch, ch)
        



    @classmethod
    def rotate(cls, db, line, in_x_ch, in_y_ch, out_x_ch, out_y_ch, x0, y0, deg):
        """
        Rotate coordinates.
        
        :param db:        Database
        :param line:      Line symbol
        :param in_x_ch:   Input X channel [`DB_LOCK_READONLY <geosoft.gxapi.DB_LOCK_READONLY>`]
        :param in_y_ch:   Input Y channel [`DB_LOCK_READONLY <geosoft.gxapi.DB_LOCK_READONLY>`]
        :param out_x_ch:  Output X channel [`DB_LOCK_READWRITE <geosoft.gxapi.DB_LOCK_READWRITE>`]
        :param out_y_ch:  Output Y channel [`DB_LOCK_READWRITE <geosoft.gxapi.DB_LOCK_READWRITE>`]
        :param x0:        X point about which to rotate
        :param y0:        Y of point about which to rotate
        :param deg:       Angle in degrees CCW
        :type  db:        GXDB
        :type  line:      int
        :type  in_x_ch:   int
        :type  in_y_ch:   int
        :type  out_x_ch:  int
        :type  out_y_ch:  int
        :type  x0:        float
        :type  y0:        float
        :type  deg:       float

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        gxapi_cy.WrapDU._rotate(GXContext._get_tls_geo(), db, line, in_x_ch, in_y_ch, out_x_ch, out_y_ch, x0, y0, deg)
        



    @classmethod
    def sample_gd(cls, db, line, ix_ch, iy_ch, o_ch, img):
        """
        Sample a `GXGD <geosoft.gxapi.GXGD>` at a specified X and Y.
        
        :param db:     Database
        :param line:   Line Handle to sample
        :param ix_ch:  X Input Channel [`DB_LOCK_READONLY <geosoft.gxapi.DB_LOCK_READONLY>`]
        :param iy_ch:  Y Input Channel [`DB_LOCK_READONLY <geosoft.gxapi.DB_LOCK_READONLY>`]
        :param o_ch:   Z Output Channel sampled from `GXGD <geosoft.gxapi.GXGD>` [`DB_LOCK_READWRITE <geosoft.gxapi.DB_LOCK_READWRITE>`]
        :param img:    Grid handle
        :type  db:     GXDB
        :type  line:   int
        :type  ix_ch:  int
        :type  iy_ch:  int
        :type  o_ch:   int
        :type  img:    GXGD

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** Values in result channel
        """
        gxapi_cy.WrapDU._sample_gd(GXContext._get_tls_geo(), db, line, ix_ch, iy_ch, o_ch, img)
        



    @classmethod
    def sample_img(cls, db, line, ix_ch, iy_ch, o_ch, img):
        """
        Sample a `GXIMG <geosoft.gxapi.GXIMG>` at a specified X and Y.
        
        :param db:     Database
        :param line:   Line Handle to sample
        :param ix_ch:  X Input Channel [`DB_LOCK_READONLY <geosoft.gxapi.DB_LOCK_READONLY>`]
        :param iy_ch:  Y Input Channel [`DB_LOCK_READONLY <geosoft.gxapi.DB_LOCK_READONLY>`]
        :param o_ch:   Z Output Channel sampled from `GXIMG <geosoft.gxapi.GXIMG>` [`DB_LOCK_READWRITE <geosoft.gxapi.DB_LOCK_READWRITE>`]
        :param img:    `GXIMG <geosoft.gxapi.GXIMG>` handle
        :type  db:     GXDB
        :type  line:   int
        :type  ix_ch:  int
        :type  iy_ch:  int
        :type  o_ch:   int
        :type  img:    GXIMG

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** Values in result channel
        """
        gxapi_cy.WrapDU._sample_img(GXContext._get_tls_geo(), db, line, ix_ch, iy_ch, o_ch, img)
        



    @classmethod
    def sample_img_line_lst(cls, db, lst, ix_ch, iy_ch, o_ch, img):
        """
        Sample an `GXIMG <geosoft.gxapi.GXIMG>` at a specified X and Y, for a `GXLST <geosoft.gxapi.GXLST>` of lines.
        
        :param db:     Database
        :param lst:    `GXLST <geosoft.gxapi.GXLST>` of (Line Name, Line Handle) values to sample
        :param ix_ch:  X Input Channel [`DB_LOCK_READONLY <geosoft.gxapi.DB_LOCK_READONLY>`]
        :param iy_ch:  Y Input Channel [`DB_LOCK_READONLY <geosoft.gxapi.DB_LOCK_READONLY>`]
        :param o_ch:   Z Output Channel sampled from `GXIMG <geosoft.gxapi.GXIMG>` [`DB_LOCK_READWRITE <geosoft.gxapi.DB_LOCK_READWRITE>`]
        :param img:    `GXIMG <geosoft.gxapi.GXIMG>` handle
        :type  db:     GXDB
        :type  lst:    GXLST
        :type  ix_ch:  int
        :type  iy_ch:  int
        :type  o_ch:   int
        :type  img:    GXIMG

        .. versionadded:: 8.3

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** Values in result channel
        """
        gxapi_cy.WrapDU._sample_img_line_lst(GXContext._get_tls_geo(), db, lst, ix_ch, iy_ch, o_ch, img)
        



    @classmethod
    def scan_ado(cls, connect, table, template):
        """
        Scans an external ADO database and generates a default template.
        
        :param connect:   Database connection string
        :param table:     Database Table Name
        :param template:  Template file name to Create
        :type  connect:   str
        :type  table:     str
        :type  template:  str

        .. versionadded:: 5.0.8

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** All the channels are listed
        """
        gxapi_cy.WrapDU._scan_ado(GXContext._get_tls_geo(), connect.encode(), table.encode(), template.encode())
        



    @classmethod
    def scan_aseg(cls, file, data, flc, template):
        """
        This method scans an ASEG-GDF file and generates a default
        template listing all the channels and all the ALIAS lines.
        
        :param file:      Header file name
        :param data:      Data file name
        :param flc:       Flight Line Channel name
        :param template:  Template file name to Create
        :type  file:      str
        :type  data:      str
        :type  flc:       str
        :type  template:  str

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        gxapi_cy.WrapDU._scan_aseg(GXContext._get_tls_geo(), file.encode(), data.encode(), flc.encode(), template.encode())
        



    @classmethod
    def scan_dao(cls, file, type, table, template):
        """
        Scans an external DAO database and generates a default template.
        
        :param file:      Database file name
        :param type:      Database Type
        :param table:     Database Table Name
        :param template:  Template file name to Create
        :type  file:      str
        :type  type:      str
        :type  table:     str
        :type  template:  str

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** All the channels are listed
        """
        gxapi_cy.WrapDU._scan_dao(GXContext._get_tls_geo(), file.encode(), type.encode(), table.encode(), template.encode())
        



    @classmethod
    def scan_pico(cls, data, template):
        """
        This method scans a picodas file and generates a default
        template listing all the channels and all the ALIAS lines.
        
        :param data:      Data file Name
        :param template:  Template file name to Create
        :type  data:      str
        :type  template:  str

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        gxapi_cy.WrapDU._scan_pico(GXContext._get_tls_geo(), data.encode(), template.encode())
        



    @classmethod
    def sort(cls, db, line, ch, sort):
        """
        Sort the contents of a channel.
        
        :param db:    Database
        :param line:  Line symbol
        :param ch:    Channel to sort [`DB_LOCK_READONLY <geosoft.gxapi.DB_LOCK_READONLY>`]
        :param sort:  :ref:`DU_SORT`
        :type  db:    GXDB
        :type  line:  int
        :type  ch:    int
        :type  sort:  int

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        gxapi_cy.WrapDU._sort(GXContext._get_tls_geo(), db, line, ch, sort)
        



    @classmethod
    def sort_index(cls, db, line, ch, in_ch, sort):
        """
        Create an ordered index of the contents of a channel.
        
        :param db:     Database
        :param line:   Line symbol
        :param ch:     Channel to sort [`DB_LOCK_READONLY <geosoft.gxapi.DB_LOCK_READONLY>`]
        :param in_ch:  Output index channel (should be int) [`DB_LOCK_READWRITE <geosoft.gxapi.DB_LOCK_READWRITE>`]
        :param sort:   :ref:`DU_SORT`
        :type  db:     GXDB
        :type  line:   int
        :type  ch:     int
        :type  in_ch:  int
        :type  sort:   int

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        gxapi_cy.WrapDU._sort_index(GXContext._get_tls_geo(), db, line, ch, in_ch, sort)
        



    @classmethod
    def sort_index2(cls, db, line, ch1, sort1, ch2, sort2, in_ch):
        """
        Create an ordered index from two channels
        
        :param db:     Database
        :param line:   Line symbol
        :param ch1:    Sort by this channel [`DB_LOCK_READONLY <geosoft.gxapi.DB_LOCK_READONLY>`]
        :param sort1:  :ref:`DU_SORT`
        :param ch2:    Then by this channel [`DB_LOCK_READONLY <geosoft.gxapi.DB_LOCK_READONLY>`]
        :param sort2:  :ref:`DU_SORT`
        :param in_ch:  Output index channel (should be int) [`DB_LOCK_READWRITE <geosoft.gxapi.DB_LOCK_READWRITE>`]
        :type  db:     GXDB
        :type  line:   int
        :type  ch1:    int
        :type  sort1:  int
        :type  ch2:    int
        :type  sort2:  int
        :type  in_ch:  int

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        gxapi_cy.WrapDU._sort_index2(GXContext._get_tls_geo(), db, line, ch1, sort1, ch2, sort2, in_ch)
        



    @classmethod
    def split_line(cls, db, i_line, o_line, fid):
        """
        Splits a line a the fiducial and copies any data past
        that fiducial into the new line.
        
        :param db:      Database
        :param i_line:  Input Line, will be reduced at fid  [`DB_LOCK_READWRITE <geosoft.gxapi.DB_LOCK_READWRITE>`]
        :param o_line:  Output Line, will take data above fid [`DB_LOCK_READWRITE <geosoft.gxapi.DB_LOCK_READWRITE>`]
        :param fid:     Fid number of split
        :type  db:      GXDB
        :type  i_line:  int
        :type  o_line:  int
        :type  fid:     float

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        gxapi_cy.WrapDU._split_line(GXContext._get_tls_geo(), db, i_line, o_line, fid)
        



    @classmethod
    def split_line2(cls, db, i_line, o_line, fid, reset_fi_ds):
        """
        Splits a line a the fiducial and copies any data past
        that fiducial into the new line.
        
        :param db:           Database
        :param i_line:       Input Line, will be reduced at fid  [`DB_LOCK_READWRITE <geosoft.gxapi.DB_LOCK_READWRITE>`]
        :param o_line:       Output Line, will take data above fid [`DB_LOCK_READWRITE <geosoft.gxapi.DB_LOCK_READWRITE>`]
        :param fid:          Fid number of split
        :param reset_fi_ds:  Reset starting fiducials to zero (0: No, 1: Yes)
        :type  db:           GXDB
        :type  i_line:       int
        :type  o_line:       int
        :type  fid:          float
        :type  reset_fi_ds:  int

        .. versionadded:: 8.4

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** The same as SplitLine, but with an option to reset each line's starting fiducial to zero.
        """
        gxapi_cy.WrapDU._split_line2(GXContext._get_tls_geo(), db, i_line, o_line, fid, reset_fi_ds)
        



    @classmethod
    def split_line_xy(cls, db, line, x_ch, y_ch, dirctn, tolrnc, down_tol, method, first_line, line_inc):
        """
        Break up a line based on tolerance of lateral and horizontal distance, with
        options for the output line names.
        
        :param db:          Database
        :param line:        Line to be broken up [`DB_LOCK_READONLY <geosoft.gxapi.DB_LOCK_READONLY>`]
        :param x_ch:        Channel X [`DB_LOCK_READWRITE <geosoft.gxapi.DB_LOCK_READWRITE>`]
        :param y_ch:        Channel Y [`DB_LOCK_READWRITE <geosoft.gxapi.DB_LOCK_READWRITE>`]
        :param dirctn:      Line direction, 0-any, 1-X, 2-Y.
        :param tolrnc:      Lateral tolerance, DUMMY for the default (10% of the separation between the first two points.
        :param down_tol:    Downline Tolerance, DUMMY for none
        :param method:      :ref:`DU_SPLITLINE`
        :param first_line:  First line in the sequence, for `DU_SPLITLINE_SEQUENTIAL <geosoft.gxapi.DU_SPLITLINE_SEQUENTIAL>`. On return, the next line in the sequence.
        :param line_inc:    Increment in the line number sequence, for `DU_SPLITLINE_SEQUENTIAL <geosoft.gxapi.DU_SPLITLINE_SEQUENTIAL>`
        :type  db:          GXDB
        :type  line:        int
        :type  x_ch:        int
        :type  y_ch:        int
        :type  dirctn:      int
        :type  tolrnc:      float
        :type  down_tol:    float
        :type  method:      int
        :type  first_line:  int_ref
        :type  line_inc:    int

        .. versionadded:: 8.3

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** The original line will be deleted.
        """
        first_line.value = gxapi_cy.WrapDU._split_line_xy(GXContext._get_tls_geo(), db, line, x_ch, y_ch, dirctn, tolrnc, down_tol, method, first_line.value, line_inc)
        



    @classmethod
    def split_line_xy2(cls, db, line, x_ch, y_ch, dirctn, tolrnc, down_tol, method, first_line, line_inc, reset_fi_ds):
        """
        Break up a line based on tolerance of lateral and horizontal distance, with
        options for the output line names.
        
        :param db:           Database
        :param line:         Line to be broken up [`DB_LOCK_READONLY <geosoft.gxapi.DB_LOCK_READONLY>`]
        :param x_ch:         Channel X [`DB_LOCK_READWRITE <geosoft.gxapi.DB_LOCK_READWRITE>`]
        :param y_ch:         Channel Y [`DB_LOCK_READWRITE <geosoft.gxapi.DB_LOCK_READWRITE>`]
        :param dirctn:       Line direction, 0-any, 1-X, 2-Y.
        :param tolrnc:       Lateral tolerance, DUMMY for the default (10% of the separation between the first two points.
        :param down_tol:     Downline Tolerance, DUMMY for none
        :param method:       :ref:`DU_SPLITLINE`
        :param first_line:   First line in the sequence, for `DU_SPLITLINE_SEQUENTIAL <geosoft.gxapi.DU_SPLITLINE_SEQUENTIAL>`. On return, the next line in the sequence.
        :param line_inc:     Increment in the line number sequence, for `DU_SPLITLINE_SEQUENTIAL <geosoft.gxapi.DU_SPLITLINE_SEQUENTIAL>`
        :param reset_fi_ds:  Reset starting fiducials to zero (0: No, 1: Yes)
        :type  db:           GXDB
        :type  line:         int
        :type  x_ch:         int
        :type  y_ch:         int
        :type  dirctn:       int
        :type  tolrnc:       float
        :type  down_tol:     float
        :type  method:       int
        :type  first_line:   int_ref
        :type  line_inc:     int
        :type  reset_fi_ds:  int

        .. versionadded:: 8.4

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** The same as SplitLineXY, but with an option to reset each line's starting fiducial to zero.
        """
        first_line.value = gxapi_cy.WrapDU._split_line_xy2(GXContext._get_tls_geo(), db, line, x_ch, y_ch, dirctn, tolrnc, down_tol, method, first_line.value, line_inc, reset_fi_ds)
        



    @classmethod
    def split_line_xy3(cls, db, line, x_ch, y_ch, dirctn, tolrnc, down_tol, method, first_line, line_inc, retain_line_type, reset_fi_ds):
        """
        Break up a line based on tolerance of lateral and horizontal distance, with
        options for the output line names.
        
        :param db:                Database
        :param line:              Line to be broken up [`DB_LOCK_READONLY <geosoft.gxapi.DB_LOCK_READONLY>`]
        :param x_ch:              Channel X [`DB_LOCK_READWRITE <geosoft.gxapi.DB_LOCK_READWRITE>`]
        :param y_ch:              Channel Y [`DB_LOCK_READWRITE <geosoft.gxapi.DB_LOCK_READWRITE>`]
        :param dirctn:            Line direction, 0-any, 1-X, 2-Y.
        :param tolrnc:            Lateral tolerance, DUMMY for the default (10% of the separation between the first two points.
        :param down_tol:          Downline Tolerance, DUMMY for none
        :param method:            :ref:`DU_SPLITLINE`
        :param first_line:        First line in the sequence, for `DU_SPLITLINE_SEQUENTIAL <geosoft.gxapi.DU_SPLITLINE_SEQUENTIAL>`. On return, the next line in the sequence.
        :param line_inc:          Increment in the line number sequence, for `DU_SPLITLINE_SEQUENTIAL <geosoft.gxapi.DU_SPLITLINE_SEQUENTIAL>`
        :param retain_line_type:  Maintain line types for `DU_SPLITLINE_SEQUENTIAL <geosoft.gxapi.DU_SPLITLINE_SEQUENTIAL>`  (0: No, 1: Yes)
        :param reset_fi_ds:       Reset starting fiducials to zero (0: No, 1: Yes)
        :type  db:                GXDB
        :type  line:              int
        :type  x_ch:              int
        :type  y_ch:              int
        :type  dirctn:            int
        :type  tolrnc:            float
        :type  down_tol:          float
        :type  method:            int
        :type  first_line:        int_ref
        :type  line_inc:          int
        :type  retain_line_type:  int
        :type  reset_fi_ds:       int

        .. versionadded:: 9.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** The same as SplitLineXY2, but with the option to maintain line types when outputting sequentially numbered lines.
        """
        first_line.value = gxapi_cy.WrapDU._split_line_xy3(GXContext._get_tls_geo(), db, line, x_ch, y_ch, dirctn, tolrnc, down_tol, method, first_line.value, line_inc, retain_line_type, reset_fi_ds)
        



    @classmethod
    def split_line_by_direction(cls, db, line, x_ch, y_ch, angular_change, over_a_distance_of, minimum_line_length, break_on_separation_distance, save_discards, method, first_line, line_inc, reset_fi_ds):
        """
        The line is split when the heading (calculated from the current X and Y channels) changes by more than a specified amount over
        a specified distance. Additional options to discard too-short lines
        
        :param db:                            Database
        :param line:                          Line to be broken up [`DB_LOCK_READONLY <geosoft.gxapi.DB_LOCK_READONLY>`]
        :param x_ch:                          X Channel [`DB_LOCK_READWRITE <geosoft.gxapi.DB_LOCK_READWRITE>`].
        :param y_ch:                          Y Channel [`DB_LOCK_READWRITE <geosoft.gxapi.DB_LOCK_READWRITE>`].
        :param angular_change:                Maximum angular change allowed (degrees)...
        :param over_a_distance_of:            ...over a distance of
        :param minimum_line_length:           Delete lines shorter than (can be `rDUMMY <geosoft.gxapi.rDUMMY>`)
        :param break_on_separation_distance:  Break on data XY separation greater than (can be `rDUMMY <geosoft.gxapi.rDUMMY>`)
        :param save_discards:                 Whether to save too-short segments as special lines or to discard them
        :param method:                        :ref:`DU_SPLITLINE` ONLY DU_SPLITLINEXY_SEQUENTIAL and DU_SPLITLINEXY_VERSIONS
        :param first_line:                    First line in the sequence, for `DU_SPLITLINE_SEQUENTIAL <geosoft.gxapi.DU_SPLITLINE_SEQUENTIAL>`. On return, the next line in the sequence.
        :param line_inc:                      Increment in the line number sequence, for `DU_SPLITLINE_SEQUENTIAL <geosoft.gxapi.DU_SPLITLINE_SEQUENTIAL>`
        :param reset_fi_ds:                   Reset starting fiducials to zero (0: No, 1: Yes)
        :type  db:                            GXDB
        :type  line:                          int
        :type  x_ch:                          int
        :type  y_ch:                          int
        :type  angular_change:                float
        :type  over_a_distance_of:            float
        :type  minimum_line_length:           float
        :type  break_on_separation_distance:  float
        :type  save_discards:                 int
        :type  method:                        int
        :type  first_line:                    int_ref
        :type  line_inc:                      int
        :type  reset_fi_ds:                   int

        .. versionadded:: 8.5

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** Split a line based on changes in heading.
        """
        first_line.value = gxapi_cy.WrapDU._split_line_by_direction(GXContext._get_tls_geo(), db, line, x_ch, y_ch, angular_change, over_a_distance_of, minimum_line_length, break_on_separation_distance, save_discards, method, first_line.value, line_inc, reset_fi_ds)
        



    @classmethod
    def split_line_by_direction2(cls, db, line, x_ch, y_ch, angular_change, over_a_distance_of, minimum_line_length, break_on_separation_distance, save_discards, method, first_line, line_inc, retain_line_type, reset_fi_ds):
        """
        The same as SplitLineByDirection, but with the option to maintain line types when outputting sequentially numbered lines.
        
        :param db:                            Database
        :param line:                          Line to be broken up [`DB_LOCK_READONLY <geosoft.gxapi.DB_LOCK_READONLY>`]
        :param x_ch:                          X Channel [`DB_LOCK_READWRITE <geosoft.gxapi.DB_LOCK_READWRITE>`].
        :param y_ch:                          Y Channel [`DB_LOCK_READWRITE <geosoft.gxapi.DB_LOCK_READWRITE>`].
        :param angular_change:                Maximum angular change allowed (degrees)...
        :param over_a_distance_of:            ...over a distance of
        :param minimum_line_length:           Delete lines shorter than (can be `rDUMMY <geosoft.gxapi.rDUMMY>`)
        :param break_on_separation_distance:  Break on data XY separation greater than (can be `rDUMMY <geosoft.gxapi.rDUMMY>`)
        :param save_discards:                 Whether to save too-short segments as special lines or to discard them
        :param method:                        :ref:`DU_SPLITLINE` ONLY DU_SPLITLINEXY_SEQUENTIAL and DU_SPLITLINEXY_VERSIONS
        :param first_line:                    First line in the sequence, for `DU_SPLITLINE_SEQUENTIAL <geosoft.gxapi.DU_SPLITLINE_SEQUENTIAL>`. On return, the next line in the sequence.
        :param line_inc:                      Increment in the line number sequence, for `DU_SPLITLINE_SEQUENTIAL <geosoft.gxapi.DU_SPLITLINE_SEQUENTIAL>`
        :param retain_line_type:              Maintain line types for `DU_SPLITLINE_SEQUENTIAL <geosoft.gxapi.DU_SPLITLINE_SEQUENTIAL>`  (0: No, 1: Yes)
        :param reset_fi_ds:                   Reset starting fiducials to zero (0: No, 1: Yes)
        :type  db:                            GXDB
        :type  line:                          int
        :type  x_ch:                          int
        :type  y_ch:                          int
        :type  angular_change:                float
        :type  over_a_distance_of:            float
        :type  minimum_line_length:           float
        :type  break_on_separation_distance:  float
        :type  save_discards:                 int
        :type  method:                        int
        :type  first_line:                    int_ref
        :type  line_inc:                      int
        :type  retain_line_type:              int
        :type  reset_fi_ds:                   int

        .. versionadded:: 9.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** Split a line based on changes in heading.
        """
        first_line.value = gxapi_cy.WrapDU._split_line_by_direction2(GXContext._get_tls_geo(), db, line, x_ch, y_ch, angular_change, over_a_distance_of, minimum_line_length, break_on_separation_distance, save_discards, method, first_line.value, line_inc, retain_line_type, reset_fi_ds)
        



    @classmethod
    def stat(cls, db, line, i_ch, st):
        """
        Add a data channel to a statistics object.
        
        :param db:    Database
        :param line:  Line handle
        :param i_ch:  Channel handle [`DB_LOCK_READONLY <geosoft.gxapi.DB_LOCK_READONLY>`]
        :param st:    Statistics handle
        :type  db:    GXDB
        :type  line:  int
        :type  i_ch:  int
        :type  st:    GXST

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** If the input channel is a `GXVA <geosoft.gxapi.GXVA>` (array) channel, then the columns set using
        `GXDB.set_va_windows <geosoft.gxapi.GXDB.set_va_windows>` are used in the statistics; all columns are used by default.

        .. seealso::

            `GXST <geosoft.gxapi.GXST>`
        """
        gxapi_cy.WrapDU._stat(GXContext._get_tls_geo(), db, line, i_ch, st)
        



    @classmethod
    def table_line_fid(cls, db, chan, ref, tb, field):
        """
        Place a Line/Fid information into a Channel.
        
        :param db:     Database
        :param chan:   Output channel [`DB_LOCK_READWRITE <geosoft.gxapi.DB_LOCK_READWRITE>`]
        :param ref:    Reference channel [`DB_LOCK_READONLY <geosoft.gxapi.DB_LOCK_READONLY>`]
        :param tb:     Table to Use
        :param field:  Table field wanted
        :type  db:     GXDB
        :type  chan:   int
        :type  ref:    int
        :type  tb:     GXTB
        :type  field:  int

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        gxapi_cy.WrapDU._table_line_fid(GXContext._get_tls_geo(), db, chan, ref, tb, field)
        



    @classmethod
    def table_selected_lines_fid(cls, db, chan, ref, tb, field):
        """
        Place a Line/Fid information into a Channel for the selected lines in the database.
        
        :param db:     Database
        :param chan:   Output channel [`DB_LOCK_READWRITE <geosoft.gxapi.DB_LOCK_READWRITE>`]
        :param ref:    Reference channel [`DB_LOCK_READONLY <geosoft.gxapi.DB_LOCK_READONLY>`]
        :param tb:     Table to Use
        :param field:  Table field wanted
        :type  db:     GXDB
        :type  chan:   int
        :type  ref:    int
        :type  tb:     GXTB
        :type  field:  int

        .. versionadded:: 9.1

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        gxapi_cy.WrapDU._table_selected_lines_fid(GXContext._get_tls_geo(), db, chan, ref, tb, field)
        



    @classmethod
    def time_constant(cls, db, line, resp_chan, time_chan, tau_chan, intercept_chan, fit_chan, log_opt):
        """
        Calculate TEM time constant (Tau)
        
        :param db:              Database, required
        :param line:            Line Handle, required
        :param resp_chan:       Response channel, required [`DB_LOCK_READONLY <geosoft.gxapi.DB_LOCK_READONLY>`]
        :param time_chan:       Time channel, required [`DB_LOCK_READONLY <geosoft.gxapi.DB_LOCK_READONLY>`]
        :param tau_chan:        Output Time constant (Tau) channel, required [`DB_LOCK_READWRITE <geosoft.gxapi.DB_LOCK_READWRITE>`]
        :param intercept_chan:  Output Intercept channel, no output if `NULLSYMB <geosoft.gxapi.NULLSYMB>` [`DB_LOCK_READWRITE <geosoft.gxapi.DB_LOCK_READWRITE>`]
        :param fit_chan:        Output predicted response channel, no output if `NULLSYMB <geosoft.gxapi.NULLSYMB>` [`DB_LOCK_READWRITE <geosoft.gxapi.DB_LOCK_READWRITE>`] Result is based on least square fit from Tau and Intercept
        :param log_opt:         Log option applied to time channel: 0 - linear, 1 - log10
        :type  db:              GXDB
        :type  line:            int
        :type  resp_chan:       int
        :type  time_chan:       int
        :type  tau_chan:        int
        :type  intercept_chan:  int
        :type  fit_chan:        int
        :type  log_opt:         int

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** When DU_TIME_LOG option is used, Time channel will be converted
        with logarithmic before calculating time constant.
        Logarthmic conversion is always applied to the response channel.
        """
        gxapi_cy.WrapDU._time_constant(GXContext._get_tls_geo(), db, line, resp_chan, time_chan, tau_chan, intercept_chan, fit_chan, log_opt)
        



    @classmethod
    def trend(cls, db, line, i_ch, o_ch, order):
        """
        Calculates an n'th order trend of a data channel.
        
        :param db:     Database
        :param line:   Line Handle to Apply this to
        :param i_ch:   Input channel  [`DB_LOCK_READONLY <geosoft.gxapi.DB_LOCK_READONLY>`]
        :param o_ch:   Result channel [`DB_LOCK_READWRITE <geosoft.gxapi.DB_LOCK_READWRITE>`]
        :param order:  Trend Order, 0 to 9
        :type  db:     GXDB
        :type  line:   int
        :type  i_ch:   int
        :type  o_ch:   int
        :type  order:  int

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        .. seealso::

            `b_spline <geosoft.gxapi.GXDU.b_spline>`
        """
        gxapi_cy.WrapDU._trend(GXContext._get_tls_geo(), db, line, i_ch, o_ch, order)
        



    @classmethod
    def update_intersect_db(cls, db, x_chan, z_chan, int_db):
        """
        Update the Z and DZ values in an intersection database, using the current database.
        
        :param db:      Flight Database Object
        :param x_chan:  X Channel [`DB_LOCK_READONLY <geosoft.gxapi.DB_LOCK_READONLY>`] (for location info)
        :param z_chan:  Z Channel [`DB_LOCK_READONLY <geosoft.gxapi.DB_LOCK_READONLY>`]
        :param int_db:  Intersection database to update
        :type  db:      GXDB
        :type  x_chan:  int
        :type  z_chan:  int
        :type  int_db:  GXDB

        .. versionadded:: 7.1

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** Updates the TZ, TDZ, LZ and LDZ channels at the intersections,
        using the current flight database.
        """
        gxapi_cy.WrapDU._update_intersect_db(GXContext._get_tls_geo(), db, x_chan, z_chan, int_db)
        



    @classmethod
    def voxel_section(cls, db, line, x_ch, y_ch, vox, grid, cell_x, cell_y, interp):
        """
        Slice a voxel to a grid under a database line.
        
        :param db:      Database Object
        :param line:    Input  Line Symbol [READWRITE]
        :param x_ch:    X Channel (DB_NO_SYMB if LineDir==0)
        :param y_ch:    Y Channel (DB_NO_SYMB if LineDir==0)
        :param vox:     Voxel to slice
        :param grid:    Output grid name
        :param cell_x:  X cell size (horizontal)
        :param cell_y:  Y cell size (vertical)
        :param interp:  Interp: 1 - linear, 0 - nearest
        :type  db:      GXDB
        :type  line:    int
        :type  x_ch:    int
        :type  y_ch:    int
        :type  vox:     GXVOX
        :type  grid:    str
        :type  cell_x:  float
        :type  cell_y:  float
        :type  interp:  int

        .. versionadded:: 6.4

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** Takes the first and XY locations in a line (using the
        current X and Y channels) and defines a section grid
        as a slice through a voxel file.
        The grid cell sizes can be left as `GS_R8DM <geosoft.gxapi.GS_R8DM>`, in which
        case an attempt will be made to match the voxel cell
        size, based on the line azimuth, voxel rotation, etc.
        
        If the slice does NOT intersect the voxel, or if
        there are fewer than 2 valid locations in the line,
        then no grid file is created, but there is no error.
        (This is to simplify creating multiple grids from
        at once, where not all may intersect).
        """
        gxapi_cy.WrapDU._voxel_section(GXContext._get_tls_geo(), db, line, x_ch, y_ch, vox, grid.encode(), cell_x, cell_y, interp)
        



    @classmethod
    def write_wa(cls, db, line, lst, wa):
        """
        Write data to an ASCII file.
        
        :param db:    Database
        :param line:  Line symbol
        :param lst:   List of channel names to write
        :param wa:    `GXWA <geosoft.gxapi.GXWA>` to write to
        :type  db:    GXDB
        :type  line:  int
        :type  lst:   GXLST
        :type  wa:    GXWA

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Channels to be written should be placed in a `GXLST <geosoft.gxapi.GXLST>` object.
        
        Channels are written in the order of the list.  Only the
        channel names in the list are used.
        
        Data is formated as in the channel definition and
        channels are separated by a single space character.
        """
        gxapi_cy.WrapDU._write_wa(GXContext._get_tls_geo(), db, line, lst, wa)
        



    @classmethod
    def xyz_line(cls, db, line, x_ch, y_ch, dirctn, tolrnc):
        """
        Break up a line based on tolerance of lateral distance.
        
        :param db:      Database
        :param line:    Line to be broken up
        :param x_ch:    Channel X
        :param y_ch:    Channel Y
        :param dirctn:  Line direction, 0-any, 1-X, 2-Y.
        :param tolrnc:  Tolerance, DUMMY for the default (10% of the separation between the first two points.
        :type  db:      GXDB
        :type  line:    int
        :type  x_ch:    int
        :type  y_ch:    int
        :type  dirctn:  int
        :type  tolrnc:  float

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** The original line will be deleted.
        """
        gxapi_cy.WrapDU._xyz_line(GXContext._get_tls_geo(), db, line, x_ch, y_ch, dirctn, tolrnc)
        



    @classmethod
    def xyz_line2(cls, db, line, x_ch, y_ch, dirctn, tolrnc, down_tol):
        """
        Break up a line based on tolerance of lateral and horizontal distance.
        
        :param db:        Database
        :param line:      Line to be broken up [`DB_LOCK_READONLY <geosoft.gxapi.DB_LOCK_READONLY>`]
        :param x_ch:      Channel X [`DB_LOCK_READWRITE <geosoft.gxapi.DB_LOCK_READWRITE>`]
        :param y_ch:      Channel Y [`DB_LOCK_READWRITE <geosoft.gxapi.DB_LOCK_READWRITE>`]
        :param dirctn:    Line direction, 0-any, 1-X, 2-Y.
        :param tolrnc:    Tolerance, DUMMY for the default (10% of the separation between the first two points.
        :param down_tol:  Downline Tolerance, DUMMY for none
        :type  db:        GXDB
        :type  line:      int
        :type  x_ch:      int
        :type  y_ch:      int
        :type  dirctn:    int
        :type  tolrnc:    float
        :type  down_tol:  float

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** The original line will be deleted.
        """
        gxapi_cy.WrapDU._xyz_line2(GXContext._get_tls_geo(), db, line, x_ch, y_ch, dirctn, tolrnc, down_tol)
        



    @classmethod
    def xyz_line3(cls, db, line, x_ch, y_ch, dirctn, tolrnc, down_tol, reset_fi_ds):
        """
        Break up a line based on tolerance of lateral and horizontal distance.
        
        :param db:           Database
        :param line:         Line to be broken up [`DB_LOCK_READONLY <geosoft.gxapi.DB_LOCK_READONLY>`]
        :param x_ch:         Channel X [`DB_LOCK_READWRITE <geosoft.gxapi.DB_LOCK_READWRITE>`]
        :param y_ch:         Channel Y [`DB_LOCK_READWRITE <geosoft.gxapi.DB_LOCK_READWRITE>`]
        :param dirctn:       Line direction, 0-any, 1-X, 2-Y.
        :param tolrnc:       Tolerance, DUMMY for the default (10% of the separation between the first two points.
        :param down_tol:     Downline Tolerance, DUMMY for none
        :param reset_fi_ds:  Reset starting fiducials to zero (0: No, 1: Yes)
        :type  db:           GXDB
        :type  line:         int
        :type  x_ch:         int
        :type  y_ch:         int
        :type  dirctn:       int
        :type  tolrnc:       float
        :type  down_tol:     float
        :type  reset_fi_ds:  int

        .. versionadded:: 8.4

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** The same as XyzLine2, but with an option to reset each line's starting fiducial to zero.
        """
        gxapi_cy.WrapDU._xyz_line3(GXContext._get_tls_geo(), db, line, x_ch, y_ch, dirctn, tolrnc, down_tol, reset_fi_ds)
        



    @classmethod
    def z_mask(cls, db, line, chan, z_chan, zmin, zmax):
        """
        Mask dummies in one channel against another(Z) with the range Zmin/Zmax.
        
        :param db:      Database
        :param line:    Line Handle
        :param chan:    Channel to mask [`DB_LOCK_READWRITE <geosoft.gxapi.DB_LOCK_READWRITE>`]
        :param z_chan:  Mask Channel [`DB_LOCK_READONLY <geosoft.gxapi.DB_LOCK_READONLY>`]
        :param zmin:    Min value of mask range
        :param zmax:    Max value of mask range
        :type  db:      GXDB
        :type  line:    int
        :type  chan:    int
        :type  z_chan:  int
        :type  zmin:    float
        :type  zmax:    float

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        gxapi_cy.WrapDU._z_mask(GXContext._get_tls_geo(), db, line, chan, z_chan, zmin, zmax)
        



    @classmethod
    def range_xy(cls, db, x_min, y_min, x_max, y_max):
        """
        Find the range of X, and Y in the selected lines.
        
        :param db:     Database
        :param x_min:  Minimum X (returned)
        :param y_min:  Minimum Y (returned)
        :param x_max:  Maximum X (returned)
        :param y_max:  Maximum Y (returned)
        :type  db:     GXDB
        :type  x_min:  float_ref
        :type  y_min:  float_ref
        :type  x_max:  float_ref
        :type  y_max:  float_ref

        .. versionadded:: 8.5

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** Returns the range in X and Y of the current X and Y channels.
        Returned values are dummy if no valid items are found.
        """
        x_min.value, y_min.value, x_max.value, y_max.value = gxapi_cy.WrapDU._range_xy(GXContext._get_tls_geo(), db, x_min.value, y_min.value, x_max.value, y_max.value)
        



    @classmethod
    def range_xyz(cls, db, x_ch, y_ch, z_ch, x_min, y_min, z_min, x_max, y_max, z_max, n_tot):
        """
        Find the range of X, Y and Z in selected lines.
        
        :param db:     Database
        :param x_ch:   X Channel [`DB_LOCK_READONLY <geosoft.gxapi.DB_LOCK_READONLY>`]
        :param y_ch:   Y Channel [`DB_LOCK_READONLY <geosoft.gxapi.DB_LOCK_READONLY>`]
        :param z_ch:   Z Channel [`DB_LOCK_READONLY <geosoft.gxapi.DB_LOCK_READONLY>`]
        :param x_min:  Minimum X (returned)
        :param y_min:  Minimum Y (returned)
        :param z_min:  Minimum Z (returned)
        :param x_max:  Maximum X (returned)
        :param y_max:  Maximum Y (returned)
        :param z_max:  Maximum Z (returned)
        :param n_tot:  Number of data values (returned)
        :type  db:     GXDB
        :type  x_ch:   int
        :type  y_ch:   int
        :type  z_ch:   int
        :type  x_min:  float_ref
        :type  y_min:  float_ref
        :type  z_min:  float_ref
        :type  x_max:  float_ref
        :type  y_max:  float_ref
        :type  z_max:  float_ref
        :type  n_tot:  int_ref

        .. versionadded:: 8.5

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** The X, Y and Z channels should be normal (not array) channels.
        Only locations where all values are non-dummy are included in the calculation.
        If no non-dummy values are found, Dummy values are returned.
        """
        x_min.value, y_min.value, z_min.value, x_max.value, y_max.value, z_max.value, n_tot.value = gxapi_cy.WrapDU._range_xyz(GXContext._get_tls_geo(), db, x_ch, y_ch, z_ch, x_min.value, y_min.value, z_min.value, x_max.value, y_max.value, z_max.value, n_tot.value)
        



    @classmethod
    def range_xyz_data(cls, db, x_ch, y_ch, z_ch, d_ch, x_min, y_min, z_min, d_min, x_max, y_max, z_max, d_max, n_tot):
        """
        Find the range of X, Y, Z and Data values in selected lines.
        
        :param db:     Database
        :param x_ch:   X Channel [`DB_LOCK_READONLY <geosoft.gxapi.DB_LOCK_READONLY>`]
        :param y_ch:   Y Channel [`DB_LOCK_READONLY <geosoft.gxapi.DB_LOCK_READONLY>`]
        :param z_ch:   Z Channel [`DB_LOCK_READONLY <geosoft.gxapi.DB_LOCK_READONLY>`]
        :param d_ch:   Data Channel [`DB_LOCK_READONLY <geosoft.gxapi.DB_LOCK_READONLY>`]
        :param x_min:  Minimum X (returned)
        :param y_min:  Minimum Y (returned)
        :param z_min:  Minimum Z (returned)
        :param d_min:  Minimum Data value (returned)
        :param x_max:  Maximum X (returned)
        :param y_max:  Maximum Y (returned)
        :param z_max:  Maximum Z (returned)
        :param d_max:  Maximum Data value (returned)
        :param n_tot:  Number of data values (returned)
        :type  db:     GXDB
        :type  x_ch:   int
        :type  y_ch:   int
        :type  z_ch:   int
        :type  d_ch:   int
        :type  x_min:  float_ref
        :type  y_min:  float_ref
        :type  z_min:  float_ref
        :type  d_min:  float_ref
        :type  x_max:  float_ref
        :type  y_max:  float_ref
        :type  z_max:  float_ref
        :type  d_max:  float_ref
        :type  n_tot:  int_ref

        .. versionadded:: 8.1

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** The Z and Data channels may be array channels, but both must have
        the same number of columns.
        Only values where all channels are non-dummy (or, for `GXVA <geosoft.gxapi.GXVA>` channels,
        where the Z or Data value are defined) are included in the calculation.
        If no non-dummy values are found, Dummy values are returned.
        This function is optimized for cases where Z and Data are array channels
        with many columns (e.g. 32 or more columns).
        """
        x_min.value, y_min.value, z_min.value, d_min.value, x_max.value, y_max.value, z_max.value, d_max.value, n_tot.value = gxapi_cy.WrapDU._range_xyz_data(GXContext._get_tls_geo(), db, x_ch, y_ch, z_ch, d_ch, x_min.value, y_min.value, z_min.value, d_min.value, x_max.value, y_max.value, z_max.value, d_max.value, n_tot.value)
        



    @classmethod
    def create_drillhole_parameter_weight_constraint_database(cls, db, ch, reg, database):
        """
        Used for weighting inversion models.
        
        :param db:        Database (selected lines used)
        :param ch:        Property channel handle [`DB_LOCK_READONLY <geosoft.gxapi.DB_LOCK_READONLY>`]
        :param reg:       Parameters (see notes)
        :param database:  Output database
        :type  db:        GXDB
        :type  ch:        int
        :type  reg:       GXREG
        :type  database:  str

        .. versionadded:: 8.2

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** Control parameters are passed in the `GXREG <geosoft.gxapi.GXREG>` (to allow for future expansion without
        the need to modify the wrappers).
        The input drillhole database must contain current X, Y and Z channels.
        Drillhole data should be equally spaced (or nearly so) down the hole.
        Weights are calculated on a circle perpendicular to the hole at each point.
        
        RADIUS - Maximum radius from drillhole to create weighting points (Default = 100).
        INCRMENENT - Grid cell size in weighting circle (Default = 10).
        MINIMUM - the minimum weighting value to apply, at the radius (Default = 0.0001).
        POWER - Exponential power to use in the weighting function (negative of this is used) (Default = 2).
        """
        gxapi_cy.WrapDU._create_drillhole_parameter_weight_constraint_database(GXContext._get_tls_geo(), db, ch, reg, database.encode())
        



    @classmethod
    def calculate_draped_survey_altitude(cls, db, line, x_ch, y_ch, img, z_ch, ascent, descent, drape_height, n_hanning, hanning_width, min_curvature):
        """
        Calculate a draped flight path, enforcing maximum descent and ascent rates.
        
        :param db:             Database
        :param line:           Line [`DB_LOCK_READONLY <geosoft.gxapi.DB_LOCK_READONLY>`]
        :param x_ch:           X Channel [`DB_LOCK_READONLY <geosoft.gxapi.DB_LOCK_READONLY>`]
        :param y_ch:           Y Channel [`DB_LOCK_READONLY <geosoft.gxapi.DB_LOCK_READONLY>`]
        :param img:            Topography grid
        :param z_ch:           Output draped altitude channel [`DB_LOCK_READWRITE <geosoft.gxapi.DB_LOCK_READWRITE>`]
        :param ascent:         Maximum rate of ascent (%)
        :param descent:        Maximum rate of descent (%)
        :param drape_height:   Minimum terrain clearance (drape height)
        :param n_hanning:      Number of times to apply Hanning Filter
        :param hanning_width:  Width of Hanning Filter
        :param min_curvature:  Minimum radius of curvature down slopes and at valley bottoms (`rDUMMY <geosoft.gxapi.rDUMMY>` to disable)
        :type  db:             GXDB
        :type  line:           int
        :type  x_ch:           int
        :type  y_ch:           int
        :type  img:            GXIMG
        :type  z_ch:           int
        :type  ascent:         float
        :type  descent:        float
        :type  drape_height:   float
        :type  n_hanning:      int
        :type  hanning_width:  float
        :type  min_curvature:  float

        .. versionadded:: 8.3

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** Calculate a draped flight path, enforcing maximum descent and ascent rates. Additional Inputs are the sample distance along the line
        and a topography grid.
        """
        gxapi_cy.WrapDU._calculate_draped_survey_altitude(GXContext._get_tls_geo(), db, line, x_ch, y_ch, img, z_ch, ascent, descent, drape_height, n_hanning, hanning_width, min_curvature)
        



    @classmethod
    def calculate_draped_survey_altitude2(cls, db, line, x_ch, y_ch, img, dem_ch, z_ch, ascent, descent, drape_height, min_drape_height, n_hanning, hanning_width, min_curvature):
        """
        Calculate a draped flight path, enforcing maximum descent and ascent rates.
        
        :param db:                Database
        :param line:              Line [`DB_LOCK_READONLY <geosoft.gxapi.DB_LOCK_READONLY>`]
        :param x_ch:              X Channel [`DB_LOCK_READONLY <geosoft.gxapi.DB_LOCK_READONLY>`]
        :param y_ch:              Y Channel [`DB_LOCK_READONLY <geosoft.gxapi.DB_LOCK_READONLY>`]
        :param img:               Topography grid
        :param dem_ch:            Output DEM channel [`DB_LOCK_READWRITE <geosoft.gxapi.DB_LOCK_READWRITE>`] (can be `NULLSYMB <geosoft.gxapi.NULLSYMB>` if not required)
        :param z_ch:              Output draped altitude channel [`DB_LOCK_READWRITE <geosoft.gxapi.DB_LOCK_READWRITE>`]
        :param ascent:            Maximum rate of ascent (%)
        :param descent:           Maximum rate of descent (%)
        :param drape_height:      Nominal terrain clearance (drape height)
        :param min_drape_height:  Minimum terrain clearance (hard minimum drape height)
        :param n_hanning:         Number of times to apply Hanning Filter
        :param hanning_width:     Width of Hanning Filter
        :param min_curvature:     Minimum radius of curvature down slopes and at valley bottoms (`rDUMMY <geosoft.gxapi.rDUMMY>` to disable)
        :type  db:                GXDB
        :type  line:              int
        :type  x_ch:              int
        :type  y_ch:              int
        :type  img:               GXIMG
        :type  dem_ch:            int
        :type  z_ch:              int
        :type  ascent:            float
        :type  descent:           float
        :type  drape_height:      float
        :type  min_drape_height:  float
        :type  n_hanning:         int
        :type  hanning_width:     float
        :type  min_curvature:     float

        .. versionadded:: 8.4

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** Calculate a draped flight path, enforcing maximum descent and ascent rates.
        Set both a nominal and minimum drape height.
        Additional Inputs are the sample distance along the line
        and a topography grid.
        """
        gxapi_cy.WrapDU._calculate_draped_survey_altitude2(GXContext._get_tls_geo(), db, line, x_ch, y_ch, img, dem_ch, z_ch, ascent, descent, drape_height, min_drape_height, n_hanning, hanning_width, min_curvature)
        



    @classmethod
    def direct_grid_data_to_voxel(cls, db, x_channel, y_channel, z_channel, data_channel, output_voxel_filename, origin_x, origin_y, origin_z, cell_count_x, cell_count_y, cell_count_z, cell_size_x, cell_size_y, cell_size_z, method):
        """
        Create a voxel using direct gridding.
        
        :param db:                     Database
        :param x_channel:              X channel [`DB_LOCK_READONLY <geosoft.gxapi.DB_LOCK_READONLY>`]
        :param y_channel:              Y channel [`DB_LOCK_READONLY <geosoft.gxapi.DB_LOCK_READONLY>`]
        :param z_channel:              Z channel [`DB_LOCK_READONLY <geosoft.gxapi.DB_LOCK_READONLY>`]
        :param data_channel:           Data channel [`DB_LOCK_READONLY <geosoft.gxapi.DB_LOCK_READONLY>`]
        :param output_voxel_filename:  Output voxel filename
        :param origin_x:               Voxel origin X
        :param origin_y:               Voxel origin Y
        :param origin_z:               Voxel origin Z
        :param cell_count_x:           Voxel cell count X
        :param cell_count_y:           Voxel cell count Y
        :param cell_count_z:           Voxel cell count Z
        :param cell_size_x:            Voxel cell size X
        :param cell_size_y:            Voxel cell size Y
        :param cell_size_z:            Voxel cell size Z
        :param method:                 :ref:`DU_DIRECTGRID_METHOD`
        :type  db:                     GXDB
        :type  x_channel:              int
        :type  y_channel:              int
        :type  z_channel:              int
        :type  data_channel:           int
        :type  output_voxel_filename:  str
        :type  origin_x:               float
        :type  origin_y:               float
        :type  origin_z:               float
        :type  cell_count_x:           int
        :type  cell_count_y:           int
        :type  cell_count_z:           int
        :type  cell_size_x:            float
        :type  cell_size_y:            float
        :type  cell_size_z:            float
        :type  method:                 int

        .. versionadded:: 8.4

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** The Z and Data channels may be array channels. If they are, the array sizes must match.
        """
        gxapi_cy.WrapDU._direct_grid_data_to_voxel(GXContext._get_tls_geo(), db, x_channel, y_channel, z_channel, data_channel, output_voxel_filename.encode(), origin_x, origin_y, origin_z, cell_count_x, cell_count_y, cell_count_z, cell_size_x, cell_size_y, cell_size_z, method)
        



    @classmethod
    def direct_grid_item_counts_to_voxel(cls, db, x_channel, y_channel, z_channel, data_channel, output_voxel_filename, origin_x, origin_y, origin_z, cell_count_x, cell_count_y, cell_count_z, cell_size_x, cell_size_y, cell_size_z, pb_replace_zeroes_with_dummy):
        """
        Create a voxel using direct gridding containing the number of data points in each cell.
        
        :param db:                            Database
        :param x_channel:                     X channel [`DB_LOCK_READONLY <geosoft.gxapi.DB_LOCK_READONLY>`]
        :param y_channel:                     Y channel [`DB_LOCK_READONLY <geosoft.gxapi.DB_LOCK_READONLY>`]
        :param z_channel:                     Z channel [`DB_LOCK_READONLY <geosoft.gxapi.DB_LOCK_READONLY>`]
        :param data_channel:                  Data channel [`DB_LOCK_READONLY <geosoft.gxapi.DB_LOCK_READONLY>`]
        :param output_voxel_filename:         Output voxel filename
        :param origin_x:                      Voxel origin X
        :param origin_y:                      Voxel origin Y
        :param origin_z:                      Voxel origin Z
        :param cell_count_x:                  Voxel cell count X
        :param cell_count_y:                  Voxel cell count Y
        :param cell_count_z:                  Voxel cell count Z
        :param cell_size_x:                   Voxel cell size X
        :param cell_size_y:                   Voxel cell size Y
        :param cell_size_z:                   Voxel cell size Z
        :param pb_replace_zeroes_with_dummy:  Replace zero values in output with DUMMY?
        :type  db:                            GXDB
        :type  x_channel:                     int
        :type  y_channel:                     int
        :type  z_channel:                     int
        :type  data_channel:                  int
        :type  output_voxel_filename:         str
        :type  origin_x:                      float
        :type  origin_y:                      float
        :type  origin_z:                      float
        :type  cell_count_x:                  int
        :type  cell_count_y:                  int
        :type  cell_count_z:                  int
        :type  cell_size_x:                   float
        :type  cell_size_y:                   float
        :type  cell_size_z:                   float
        :type  pb_replace_zeroes_with_dummy:  bool

        .. versionadded:: 8.4

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** The Z and Data channels may be array channels. If they are, the array sizes must match.
        """
        gxapi_cy.WrapDU._direct_grid_item_counts_to_voxel(GXContext._get_tls_geo(), db, x_channel, y_channel, z_channel, data_channel, output_voxel_filename.encode(), origin_x, origin_y, origin_z, cell_count_x, cell_count_y, cell_count_z, cell_size_x, cell_size_y, cell_size_z, pb_replace_zeroes_with_dummy)
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer