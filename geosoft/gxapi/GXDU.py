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
class GXDU:
    """
    GXDU class.

    `GXDU <geosoft.gxapi.GXDU>` functions provide a variety of common utilities that can be applied
    efficiently to the contents of a database. Most `GXDU <geosoft.gxapi.GXDU>` library functions take
    as their first argument a `GXDB <geosoft.gxapi.GXDB>` object, and apply standard processes to data
    stored in an OASIS database, including import and export functions.

    **Note:**

    The following defines are used by GX functions but are not required
    for any methods:
    
    `DU_LINES_`
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._wrapper = None

    def __del__(self):
        self._wrapper = None

    def __init__(self, wrapper=None):
        self._wrapper = wrapper if wrapper else gxapi_cy.WrapDU(GXContext._get_tls_geo(), 0)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of `GXDU`
        
        :returns: A null `GXDU`
        """
        return cls()

    def is_null(self):
        """
        Check if the instance of `GXDU` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of `GXDU`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Miscellaneous


    @classmethod
    def table_look1(cls, db, line, i_ch, o_ch, ref_field, l_field, mode, close, tb):
        """
        Create a new channel using a single reference table

        **Note:**

        Fails if table does not contain requested fields.
        The nominal data sample spacing for the CLOSE options is
        calculated by finding the fiducial increment the
        - primary index channel for Lookup1C_DU;
        - secondary index channel for Lookup2C_DU, LookupIValC_DU
        and LookupRValC_DU
        """
        gxapi_cy.WrapDU.table_look1(GXContext._get_tls_geo(), db._wrapper, line, i_ch, o_ch, ref_field.encode(), l_field.encode(), mode, close, tb._wrapper)
        



    @classmethod
    def table_look2(cls, db, line, r1_ch, r2_ch, o_ch, r1_field, r2_field, l_field, mode, close, tb):
        """
        Create a new channel using a double reference  table.

        **Note:**

        Fails if table does not contain requested fields.
        The nominal data sample spacing for the CLOSE options is
        calculated by finding the fiducial increment the
        - primary index channel for Lookup1C_DU;
        - secondary index channel for Lookup2C_DU, LookupIValC_DU
        and LookupRValC_DU
        """
        gxapi_cy.WrapDU.table_look2(GXContext._get_tls_geo(), db._wrapper, line, r1_ch, r2_ch, o_ch, r1_field.encode(), r2_field.encode(), l_field.encode(), mode, close, tb._wrapper)
        



    @classmethod
    def table_look_i2(cls, db, line, val, i_ch, o_ch, r1, r2, field, mode, dist, tb):
        """
        Create a new channel using constant integer primary
        reference and a secondary reference table.

        **Note:**

        Fails if table does not contain requested fields.
        The nominal data sample spacing for the CLOSE options is
        calculated by finding the fiducial increment the
        - primary index channel for Lookup1C_DU;
        - secondary index channel for Lookup2C_DU, LookupIValC_DU
        and LookupRValC_DU
        """
        gxapi_cy.WrapDU.table_look_i2(GXContext._get_tls_geo(), db._wrapper, line, val, i_ch, o_ch, r1.encode(), r2.encode(), field.encode(), mode, dist, tb._wrapper)
        



    @classmethod
    def table_look_r2(cls, db, line, val, i_ch, o_ch, r1, r2, field, mode, dist, tb):
        """
        Create a new channel using a constant real primary
        reference and a secondary reference table.

        **Note:**

        Fails if table does not contain requested fields.
        The nominal data sample spacing for the CLOSE options is
        calculated by finding the fiducial increment the
        - primary index channel for Lookup1C_DU;
        - secondary index channel for Lookup2C_DU, LookupIValC_DU
        and LookupRValC_DU
        """
        gxapi_cy.WrapDU.table_look_r2(GXContext._get_tls_geo(), db._wrapper, line, val, i_ch, o_ch, r1.encode(), r2.encode(), field.encode(), mode, dist, tb._wrapper)
        



    @classmethod
    def ado_table_names(cls, connect, vv):
        """
        Scans a ADO-compliant database and returns the table names in a `GXVV <geosoft.gxapi.GXVV>`

        **Note:**

        The `GXVV <geosoft.gxapi.GXVV>` must be created to hold strings of length
        `STR_DB_SYMBOL <geosoft.gxapi.STR_DB_SYMBOL>`; i.e. use
        Creat_VV(-`STR_DB_SYMBOL <geosoft.gxapi.STR_DB_SYMBOL>`, 0), or it will assert.
        """
        gxapi_cy.WrapDU.ado_table_names(GXContext._get_tls_geo(), connect.encode(), vv._wrapper)
        



    @classmethod
    def an_sig(cls, db, line, i_ch, o_ch):
        """
        Calculate the Analytic Signal of a channel.
        """
        gxapi_cy.WrapDU.an_sig(GXContext._get_tls_geo(), db._wrapper, line, i_ch, o_ch)
        



    @classmethod
    def append(cls, d_bi, d_bo, ignore):
        """
        Append a source database onto a destination database.

        **Note:**

        If the source database and destination database have channels
        with the same name, then data is appended onto the end
        of the channel in lines which have the same number.
        
        If a channel in the destination database is not also in the source
        database, it is ignored.
        """
        gxapi_cy.WrapDU.append(GXContext._get_tls_geo(), d_bi._wrapper, d_bo._wrapper, ignore)
        



    @classmethod
    def avg_azimuth(cls, db, precision, azimuth):
        """
        Returns average azimuth of selected lines.

        **Note:**

        Direction in degrees azimuth (clockwise relative
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
        azimuth.value = gxapi_cy.WrapDU.avg_azimuth(GXContext._get_tls_geo(), db._wrapper, precision, azimuth.value)
        



    @classmethod
    def base_data(cls, db, line, in_ch, time_ch, out_ch, tb):
        """
        This method corrects an entire database line using a
        time-based correction table. It is given 2 input channel
        tokens and 1 output channel token as well as the table
        object to use.
        """
        gxapi_cy.WrapDU.base_data(GXContext._get_tls_geo(), db._wrapper, line, in_ch, time_ch, out_ch, tb._wrapper)
        



    @classmethod
    def base_data_ex(cls, db, line, in_ch, time_ch, out_ch, tb, flag):
        """
        This method corrects an entire database line using a
        time-based correction table. It is given 2 input channel
        tokens and 1 output channel token as well as the table
        object to use (table sort flag=1 for sort, =0 for no sort).
        """
        gxapi_cy.WrapDU.base_data_ex(GXContext._get_tls_geo(), db._wrapper, line, in_ch, time_ch, out_ch, tb._wrapper, flag)
        



    @classmethod
    def bound_line(cls, db, line, x_chan, y_chan, pply):
        """
        Set map boundary clip limits.
        """
        gxapi_cy.WrapDU.bound_line(GXContext._get_tls_geo(), db._wrapper, line, x_chan, y_chan, pply._wrapper)
        



    @classmethod
    def bp_filt(cls, db, line, i_ch, o_ch, sw, lw, filt_len):
        """
        This method applies a band-pass filter to the specified
        line/channel and places the output in the output channel.

        **Note:**

        If the short and long wavelengths are <= 0, the input channel
        is simply copied to the output channel without filtering.
        """
        gxapi_cy.WrapDU.bp_filt(GXContext._get_tls_geo(), db._wrapper, line, i_ch, o_ch, sw, lw, filt_len)
        



    @classmethod
    def break_line(cls, db, line, chan):
        """
        Break up a line based on line numbers in a channel.
        """
        gxapi_cy.WrapDU.break_line(GXContext._get_tls_geo(), db._wrapper, line, chan)
        



    @classmethod
    def break_line2(cls, db, line, chan, reset_fi_ds):
        """
        Break up a line based on line numbers in a channel.

        **Note:**

        The same as BreakLine, but with an option to reset each line's starting fiducial to zero.
        """
        gxapi_cy.WrapDU.break_line2(GXContext._get_tls_geo(), db._wrapper, line, chan, reset_fi_ds)
        



    @classmethod
    def break_line_to_groups(cls, db, line, chan, cl):
        """
        Break up a line into group-lines based on a channel.

        **Note:**

        The original line will be deleted.
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
        gxapi_cy.WrapDU.break_line_to_groups(GXContext._get_tls_geo(), db._wrapper, line, chan, cl.encode())
        



    @classmethod
    def break_line_to_groups2(cls, db, line, chan, cl, reset_fi_ds):
        """
        Break up a line into group-lines based on a channel.

        **Note:**

        The same as BreakLineToGroups, but with an option to reset each line's starting fiducial to zero.
        """
        gxapi_cy.WrapDU.break_line_to_groups2(GXContext._get_tls_geo(), db._wrapper, line, chan, cl.encode(), reset_fi_ds)
        



    @classmethod
    def b_spline(cls, db, line, i_ch, o_ch, sd, rou, tau):
        """
        B-spline Interpolate a Channel.

        .. seealso::

            `trend <geosoft.gxapi.GXDU.trend>`
        """
        gxapi_cy.WrapDU.b_spline(GXContext._get_tls_geo(), db._wrapper, line, i_ch, o_ch, sd, rou, tau)
        



    @classmethod
    def closest_point(cls, db, x, y, xp, yp, line, fid):
        """
        Return closest data point to input location.

        **Note:**

        Selected lines are scanned for the (X, Y) location
        which is closest to the input location.
        The line and fiducial of the point are returned.
        
        Will register an error if no valid (X, Y) locations
        are found.
        """
        xp.value, yp.value, line.value, fid.value = gxapi_cy.WrapDU.closest_point(GXContext._get_tls_geo(), db._wrapper, x, y, xp.value, yp.value, line.value, fid.value)
        



    @classmethod
    def copy_line(cls, db, i_line, o_line):
        """
        Copy a line.

        **Note:**

        Existing channels in the output line will be replaced
        by copied channels.
        """
        gxapi_cy.WrapDU.copy_line(GXContext._get_tls_geo(), db._wrapper, i_line, o_line)
        



    @classmethod
    def copy_line_across(cls, idb, i_line, odb, o_line):
        """
        Copy a line from one database to another.

        **Note:**

        Existing channels in the output line will be replaced
        by copied channels.

        .. seealso::

            `copy_line_chan_across <geosoft.gxapi.GXDU.copy_line_chan_across>` function
        """
        gxapi_cy.WrapDU.copy_line_across(GXContext._get_tls_geo(), idb._wrapper, i_line, odb._wrapper, o_line)
        



    @classmethod
    def copy_line_chan_across(cls, idb, i_line, vv_chan, odb, o_line):
        """
        Copy a list of channels in a line from one database to another.

        **Note:**

        Existing channels in the output line will be replaced
        by copied channels.

        .. seealso::

            `copy_line_across <geosoft.gxapi.GXDU.copy_line_across>` function
        """
        gxapi_cy.WrapDU.copy_line_chan_across(GXContext._get_tls_geo(), idb._wrapper, i_line, vv_chan._wrapper, odb._wrapper, o_line)
        



    @classmethod
    def copy_line_masked(cls, db, i_line, mask, prune, o_line):
        """
        Copy a line, prune items based on a mask channel

        **Note:**

        The input line's channel data is ReFidded to the mask
        channel, and then pruned from the output line data,
        based on the value of the VVU_PRUNE_XXX variable.
        For `VVU_PRUNE_DUMMY <geosoft.gxapi.VVU_PRUNE_DUMMY>`, only those items where the mask channel
        value is not a dummy are retained, while the complement
        is retained for VV_PRUNE_VALID.
        """
        gxapi_cy.WrapDU.copy_line_masked(GXContext._get_tls_geo(), db._wrapper, i_line, mask, prune, o_line)
        



    @classmethod
    def dao_table_names(cls, file, type, vv):
        """
        Scans a DAO-compliant database and returns the table names in a `GXVV <geosoft.gxapi.GXVV>`

        **Note:**

        The `GXVV <geosoft.gxapi.GXVV>` must be created to hold strings of length
        `STR_DB_SYMBOL <geosoft.gxapi.STR_DB_SYMBOL>`; i.e. use
        Creat_VV(-`STR_DB_SYMBOL <geosoft.gxapi.STR_DB_SYMBOL>`, 0), or it will assert.
        """
        gxapi_cy.WrapDU.dao_table_names(GXContext._get_tls_geo(), file.encode(), type.encode(), vv._wrapper)
        



    @classmethod
    def decimate(cls, db, line, i_ch, o_ch, n):
        """
        Copy and decimate a channel
        """
        gxapi_cy.WrapDU.decimate(GXContext._get_tls_geo(), db._wrapper, line, i_ch, o_ch, n)
        



    @classmethod
    def diff(cls, db, line, i_ch, o_ch, n):
        """
        Calculate differences within a channel.

        **Note:**

        Differences with dummies result in dummies.
        An even number of differences locates data accurately.
        An odd number of differences locates result 1/2 element lower
        in the `GXVV <geosoft.gxapi.GXVV>`.
        """
        gxapi_cy.WrapDU.diff(GXContext._get_tls_geo(), db._wrapper, line, i_ch, o_ch, n)
        



    @classmethod
    def distance(cls, db, line, x_ch, y_ch, o_ch):
        """
        Create a distance channel from X and Y.
        """
        gxapi_cy.WrapDU.distance(GXContext._get_tls_geo(), db._wrapper, line, x_ch, y_ch, o_ch)
        



    @classmethod
    def distance_3d(cls, db, line, x_ch, y_ch, z_ch, type, o_ch):
        """
        Create a distance channel from XY or XYZ with direction options.
        """
        gxapi_cy.WrapDU.distance_3d(GXContext._get_tls_geo(), db._wrapper, line, x_ch, y_ch, z_ch, type, o_ch)
        



    @classmethod
    def distline(cls, db, line, x_ch, y_ch, dist):
        """
        Calculate cummulative distance for a line.
        """
        dist.value = gxapi_cy.WrapDU.distline(GXContext._get_tls_geo(), db._wrapper, line, x_ch, y_ch, dist.value)
        



    @classmethod
    def dup_chan_locks(cls, d_bi, d_bo):
        """
        Duplicate all channels protect-info from input `GXDB <geosoft.gxapi.GXDB>`.
        """
        gxapi_cy.WrapDU.dup_chan_locks(GXContext._get_tls_geo(), d_bi._wrapper, d_bo._wrapper)
        



    @classmethod
    def dup_chans(cls, d_bi, d_bo):
        """
        Duplicate all channels from input `GXDB <geosoft.gxapi.GXDB>`.
        """
        gxapi_cy.WrapDU.dup_chans(GXContext._get_tls_geo(), d_bi._wrapper, d_bo._wrapper)
        



    @classmethod
    def edit_duplicates(cls, db, line, x_ch, y_ch, option, single, fid_num):
        """
        Edit duplicate readings at individual location

        **Note:**

        All the channels must be of the same fid incr/start and length.
        Protected channels are modified automatically.
        """
        gxapi_cy.WrapDU.edit_duplicates(GXContext._get_tls_geo(), db._wrapper, line, x_ch, y_ch, option, single, fid_num)
        



    @classmethod
    def export1(cls, db, format, cur_line, chan_vv, chan, data, dummies, header):
        """
        Export to a specific format.

        **Note:**

        For databases with both groups and lines:
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
        gxapi_cy.WrapDU.export1(GXContext._get_tls_geo(), db._wrapper, format, cur_line.encode(), chan_vv._wrapper, chan, data.encode(), dummies, header)
        



    @classmethod
    def export2(cls, db, format, cur_line, chan_vv, chan, data, dummies, header, line_names):
        """
        Like `export1 <geosoft.gxapi.GXDU.export1>`, but include line names as data.

        **Note:**

        See `export1 <geosoft.gxapi.GXDU.export1>`.
        The line names are printed as the first column of data exported.
        """
        gxapi_cy.WrapDU.export2(GXContext._get_tls_geo(), db._wrapper, format, cur_line.encode(), chan_vv._wrapper, chan, data.encode(), dummies, header, line_names)
        



    @classmethod
    def export_amira(cls, db, wa, one_cols_ch, array_ch, time_ch, errors_ch, datatype, units, config, instrument, frequency):
        """
        Export to database an AMIRA data file.

        **Note:**

        Other defined FIELDS stored in the database (see `import_amira <geosoft.gxapi.GXDU.import_amira>` function)
        will be automatically included in the export
        """
        gxapi_cy.WrapDU.export_amira(GXContext._get_tls_geo(), db._wrapper, wa._wrapper, one_cols_ch.encode(), array_ch.encode(), time_ch.encode(), errors_ch.encode(), datatype.encode(), units.encode(), config.encode(), instrument.encode(), frequency.encode())
        



    @classmethod
    def export_aseg(cls, db, cur_line, chan_vv, chan, defn, data):
        """
        Export to ASEG-GDF format file(s).

        **Note:**

        At least one of the header file
        or data file names must be set. (Unset names will get the
        same file name, but with the extensions .dfn (header) or
        .dat (data).
        For databases with both groups and lines:
        If both lines and groups are selected, save only the lines.
        If no lines are selected, (only groups), save the current line
        if it is (1) a group and (2) selected, else save the first selected
        group. ---
        """
        gxapi_cy.WrapDU.export_aseg(GXContext._get_tls_geo(), db._wrapper, cur_line.encode(), chan_vv._wrapper, chan, defn.encode(), data.encode())
        



    @classmethod
    def export_aseg_proj(cls, db, cur_line, chan_vv, chan, defn, data, proj, ipj):
        """
        Export to ASEG-GDF format file(s) (supports projections).

        **Note:**

        At least one of the header file
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
        gxapi_cy.WrapDU.export_aseg_proj(GXContext._get_tls_geo(), db._wrapper, cur_line.encode(), chan_vv._wrapper, chan, defn.encode(), data.encode(), proj.encode(), ipj._wrapper)
        



    @classmethod
    def export_chan_crc(cls, db, symb, crc, file):
        """
        Export a channel as XML and compute a CRC value.

        **Note:**

        The output file is an XML describing the channel. The
        CRC is of the channel data ONLY. To compute a CRC of the
        full channel (include metadata) do a CRC of the generated
        file.
        """
        crc.value = gxapi_cy.WrapDU.export_chan_crc(GXContext._get_tls_geo(), db._wrapper, symb, crc.value, file.encode())
        



    @classmethod
    def export_csv(cls, db, cur_line, chan_vv, chan, data, dummies, header):
        """
        Export to a CSV file.

        **Note:**

        For databases with both groups and lines:
        If both lines and groups are selected, save only the lines.
        If no lines are selected, (only groups), save the current line
        if it is (1) a group and (2) selected, else save the first selected
        group. ---
        Option to filter out data where one of the channels has a dummy in it.
        Option to allow a header with the channel names.
        """
        gxapi_cy.WrapDU.export_csv(GXContext._get_tls_geo(), db._wrapper, cur_line.encode(), chan_vv._wrapper, chan, data.encode(), dummies, header)
        



    @classmethod
    def export_database_crc(cls, db, crc, file):
        """
        Export a channel as XML and compute a CRC value.

        **Note:**

        The output file is an XML describing the channel. The
        CRC is of the channel data ONLY. To compute a CRC of the
        full channel (include metadata) do a CRC of the generated
        file.
        """
        crc.value = gxapi_cy.WrapDU.export_database_crc(GXContext._get_tls_geo(), db._wrapper, crc.value, file.encode())
        



    @classmethod
    def export_gbn(cls, db, vv, data):
        """
        Export to a GBN data file.

        **Note:**

        The iDispChanList_DBE or `GXDB.symb_list <geosoft.gxapi.GXDB.symb_list>` methods can be
        used to obtain a list of channels.
        """
        gxapi_cy.WrapDU.export_gbn(GXContext._get_tls_geo(), db._wrapper, vv._wrapper, data.encode())
        



    @classmethod
    def export_mdb(cls, db, cur_line, chan_vv, chan, single, data):
        """
        Export to a Microsoft Access Database (MDB) file.

        **Note:**

        Similar to `export_gbn <geosoft.gxapi.GXDU.export_gbn>`, with the addition that
        Groups go to individual tables, and lines go to
        a single table, or individual tables, based on the
        value of `DU_LINEOUT_`
        """
        gxapi_cy.WrapDU.export_mdb(GXContext._get_tls_geo(), db._wrapper, cur_line.encode(), chan_vv._wrapper, chan, single, data.encode())
        



    @classmethod
    def export_geodatabase(cls, db, feature_class_name, cur_line, chan_vv, chan, output, single, data):
        """
        Export to a ESRI Geodatabase file.

        **Note:**

        Similar to `export_gbn <geosoft.gxapi.GXDU.export_gbn>`, with the addition that
        Groups go to individual tables, and lines go to
        a single table, or individual tables, based on the
        value of `DU_LINEOUT_`
        """
        gxapi_cy.WrapDU.export_geodatabase(GXContext._get_tls_geo(), db._wrapper, feature_class_name.encode(), cur_line.encode(), chan_vv._wrapper, chan, output, single, data.encode())
        



    @classmethod
    def get_existing_feature_classes_in_geodatabase(cls, db, geodatabase, lst, vv):
        """
        Searches the geodatabases for an existing Feature class.

        **Note:**

        Searches the geodatabases for an existing Feature class
        """
        ret_val = gxapi_cy.WrapDU.get_existing_feature_classes_in_geodatabase(GXContext._get_tls_geo(), db._wrapper, geodatabase.encode(), lst._wrapper, vv._wrapper)
        return ret_val



    @classmethod
    def export_shp(cls, db, cur_line, chan_vv, chan, single, data, lst):
        """
        Export to a shape file or files.

        **Note:**

        Similar to `export_mdb <geosoft.gxapi.GXDU.export_mdb>`, with the addition that groups go to indiviual files
        with group name suffixes, and lines go to a single file, or multiple files
        with line name suffixes, based on the value of `DU_LINEOUT_`.
        """
        gxapi_cy.WrapDU.export_shp(GXContext._get_tls_geo(), db._wrapper, cur_line.encode(), chan_vv._wrapper, chan, single, data.encode(), lst._wrapper)
        



    @classmethod
    def export_xyz(cls, db, data, template):
        """
        Export XYZdata from a database to an XYZ file.

        **Note:**

        1. The export template can be in the local directory or the GEOSOFT
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
        gxapi_cy.WrapDU.export_xyz(GXContext._get_tls_geo(), db._wrapper, data.encode(), template.encode())
        



    @classmethod
    def export_xyz2(cls, db, wa, ra):
        """
        Export XYZdata from a database to an XYZ file, using file handles.

        .. seealso::

            `export_xyz <geosoft.gxapi.GXDU.export_xyz>`
        """
        gxapi_cy.WrapDU.export_xyz2(GXContext._get_tls_geo(), db._wrapper, wa._wrapper, ra._wrapper)
        



    @classmethod
    def fft(cls, db, line, s_ch, r_ch, i_ch):
        """
        Apply an `GXFFT <geosoft.gxapi.GXFFT>` to space data.
        """
        gxapi_cy.WrapDU.fft(GXContext._get_tls_geo(), db._wrapper, line, s_ch, r_ch, i_ch)
        



    @classmethod
    def filter(cls, db, line, i_ch, o_ch, flt):
        """
        Apply a convolution filter to a channel.
        """
        gxapi_cy.WrapDU.filter(GXContext._get_tls_geo(), db._wrapper, line, i_ch, o_ch, flt)
        



    @classmethod
    def gen_lev(cls, db, in_file, out_file, max_dz, m0):
        """
        Generate a Level table from an Intersection Table.
        """
        gxapi_cy.WrapDU.gen_lev(GXContext._get_tls_geo(), db._wrapper, in_file.encode(), out_file.encode(), max_dz, m0)
        



    @classmethod
    def gen_lev_db(cls, db, out_file, max_dz, m0):
        """
        Generate a Level table from an Intersection Database

        **Note:**

        Requires channels with the following names:
        
        ine, TFid, TZ, TDZ
        Line, LFid, LZ, LDZ
        Mask
        """
        gxapi_cy.WrapDU.gen_lev_db(GXContext._get_tls_geo(), db._wrapper, out_file.encode(), max_dz, m0)
        



    @classmethod
    def gen_xyz_temp(cls, xyz, temp):
        """
        Generate default XYZ template for a XYZ file.
        """
        gxapi_cy.WrapDU.gen_xyz_temp(GXContext._get_tls_geo(), xyz.encode(), temp.encode())
        



    @classmethod
    def get_xyz_num_fields(cls, xyz, num_fields):
        """
        Get the number of fields in the XYZ file.
        """
        num_fields.value = gxapi_cy.WrapDU.get_xyz_num_fields(GXContext._get_tls_geo(), xyz.encode(), num_fields.value)
        



    @classmethod
    def get_chan_data_lst(cls, db, chan, mask, lst):
        """
        Populate a `GXLST <geosoft.gxapi.GXLST>` with unique items in a channel.

        **Note:**

        Items from all selected lines are collected,
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
        gxapi_cy.WrapDU.get_chan_data_lst(GXContext._get_tls_geo(), db._wrapper, chan, mask, lst._wrapper)
        



    @classmethod
    def get_chan_data_vv(cls, db, chan, mask, vv):
        """
        Populate a `GXVV <geosoft.gxapi.GXVV>` with unique items in a channel.

        **Note:**

        Items from all selected lines are collected,
        sorted, and duplicates removed.
        The data is collected in the channel's data type,
        so normal `GXVV.sort <geosoft.gxapi.GXVV.sort>` rules apply.
        If the output `GXVV <geosoft.gxapi.GXVV>` and channel type are not the
        same, then the data is converted using the
        Copy_VV function, so see that for conversion rules.
        If a mask channel is selected, then only those items
        where the mask channel is not a dummy are collected.
        """
        gxapi_cy.WrapDU.get_chan_data_vv(GXContext._get_tls_geo(), db._wrapper, chan, mask, vv._wrapper)
        



    @classmethod
    def gradient(cls, dbi, dbo, ix_ch, iy_ch, iz_ch, ig_ch, ox_ch, oy_ch, oz_ch, angle, width):
        """
        This method takes 4 channels from input database and
        duplicats each line twice to output database)
        (input and Output can be the same channel).
        """
        gxapi_cy.WrapDU.gradient(GXContext._get_tls_geo(), dbi._wrapper, dbo._wrapper, ix_ch, iy_ch, iz_ch, ig_ch, ox_ch, oy_ch, oz_ch, angle, width)
        



    @classmethod
    def grav_drift(cls, db, line, date, time, read, base, clos):
        """
        Calculate base loop closure and correct for drift.
        """
        gxapi_cy.WrapDU.grav_drift(GXContext._get_tls_geo(), db._wrapper, line, date, time, read, base, clos)
        



    @classmethod
    def grav_tide(cls, db, line, lat, lon, date, time, gmt, tide):
        """
        Calculate earth tide gravity correction.
        """
        gxapi_cy.WrapDU.grav_tide(GXContext._get_tls_geo(), db._wrapper, line, lat, lon, date, time, gmt, tide)
        



    @classmethod
    def grid_load(cls, db, img, xdec, ydec, trim_dum, create_index):
        """
        Load grid data to a database.
        """
        gxapi_cy.WrapDU.grid_load(GXContext._get_tls_geo(), db._wrapper, img._wrapper, xdec, ydec, trim_dum, create_index)
        



    @classmethod
    def grid_load_xyz(cls, db, img, ch_x, ch_y, ch_z, ch_data, xdec, ydec, trim_dum, index_ch):
        """
        Load grid data to a database using specified channels
        """
        gxapi_cy.WrapDU.grid_load_xyz(GXContext._get_tls_geo(), db._wrapper, img._wrapper, ch_x, ch_y, ch_z, ch_data, xdec, ydec, trim_dum, index_ch)
        



    @classmethod
    def head(cls, db, line, i_ch, o_ch, tb, dir):
        """
        Applies a heading correction.

        **Note:**

        Updates channel with Direction in degrees azimuth (counter-clockwise
        relative the +Y direction).
        `GS_R8DM <geosoft.gxapi.GS_R8DM>` if the line has no data, or if there is a
        problem.
        """
        gxapi_cy.WrapDU.head(GXContext._get_tls_geo(), db._wrapper, line, i_ch, o_ch, tb._wrapper, dir)
        



    @classmethod
    def import_bin3(cls, db, data, template, line, flight, date, wa):
        """
        Same as `import_bin2 <geosoft.gxapi.GXDU.import_bin2>`, but returns the name of the imported line.

        **Note:**

        See `import_bin2 <geosoft.gxapi.GXDU.import_bin2>`. Because the name of the created line is
        not necessarily the value passed in (and the value passed in
        can be blank), this version returns the name of the line
        to which the data is actually imported.

        .. seealso::

            `import_bin2 <geosoft.gxapi.GXDU.import_bin2>`
        """
        line.value = gxapi_cy.WrapDU.import_bin3(GXContext._get_tls_geo(), db._wrapper, data.encode(), template.encode(), line.value.encode(), flight, date, wa._wrapper)
        



    @classmethod
    def imp_cb_ply(cls, db, pj, file, x_chan, y_chan):
        """
        Import concession boundary polygon file into a database

        **Note:**

        The polygon file is provided by Ana Christina in Brazil.
        """
        gxapi_cy.WrapDU.imp_cb_ply(GXContext._get_tls_geo(), db._wrapper, pj._wrapper, file.encode(), x_chan, y_chan)
        



    @classmethod
    def import_ado(cls, db, connect, table, template, line):
        """
        Import an external database table into a group using ADO.

        **Note:**

        1. The import template can be in the local directory or the GEOSOFT
        directory.
        
        2. Only the import template must be specified. The database connection string,
        the database table and Oasis line name are normally taken from the template
        file itself, but if these values are provided, they will override those found in the template.
        
        3. If the line already exists, the data will overwrite the existing data.
        """
        gxapi_cy.WrapDU.import_ado(GXContext._get_tls_geo(), db._wrapper, connect.encode(), table.encode(), template.encode(), line.encode())
        



    @classmethod
    def import_all_ado(cls, db, connect, storage):
        """
        Import an entire external database using ADO.

        **Note:**

        1. For group storage, the table names are imported "as is". For line storage,
        if the table names are valid Geosoft line names, they are used as is.
        Otherwise, line names will be created with type LINE_NORMAL, starting at
        L0 and incrementing by 10 (L10, L20 etc.)
        
        2. If the line exists, the data will overwrite the existing data.
        
        3. All tables and fields will be imported.
        
        4. If connection string is of type "FILENAME=..." the connection will attempt to resolve
        it as a file database. (see also ODBCFileConnect_GUI)
        """
        gxapi_cy.WrapDU.import_all_ado(GXContext._get_tls_geo(), db._wrapper, connect.encode(), storage)
        



    @classmethod
    def import_all_dao(cls, db, data, type, storage):
        """
        Import an entire external database using DAO.

        **Note:**

        1. The file is assumed to be a DAO compliant database.
        
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
        gxapi_cy.WrapDU.import_all_dao(GXContext._get_tls_geo(), db._wrapper, data.encode(), type.encode(), storage)
        



    @classmethod
    def import_amira(cls, db, ra, wa):
        """
        Import an AMIRA data file.

        **Note:**

        All the constant declarations are stored within the database
        under \\TEM\\CONSTANTS. The format is as follows:
        
            1. Lines stored in the file beginning with "/" are comments
            2. Each constant occupies a line in the file. It uses the format: CONSTANT=VALUE
        """
        gxapi_cy.WrapDU.import_amira(GXContext._get_tls_geo(), db._wrapper, ra._wrapper, wa._wrapper)
        



    @classmethod
    def import_aseg(cls, db, template, file, data, flc, chans):
        """
        Import an ASEG-GDF data file.
        """
        gxapi_cy.WrapDU.import_aseg(GXContext._get_tls_geo(), db._wrapper, template.encode(), file.encode(), data.encode(), flc.encode(), chans)
        



    @classmethod
    def import_aseg_proj(cls, db, template, file, data, flc, chans, proj, x_ch, y_ch):
        """
        Import an ASEG-GDF data file (supports projections).

        **Note:**

        This version supports projections
        """
        gxapi_cy.WrapDU.import_aseg_proj(GXContext._get_tls_geo(), db._wrapper, template.encode(), file.encode(), data.encode(), flc.encode(), chans, proj.encode(), x_ch.encode(), y_ch.encode())
        



    @classmethod
    def import_bin(cls, db, data, template, line, flight, date):
        """
        Import blocked binary or archive ASCII data

        **Note:**

        1. Binary import templates have extension .I2 by convention.  See
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
        gxapi_cy.WrapDU.import_bin(GXContext._get_tls_geo(), db._wrapper, data.encode(), template.encode(), line.encode(), flight, date)
        



    @classmethod
    def import_bin2(cls, db, data, template, line, flight, date, wa):
        """
        Import blocked binary or archive ASCII data with data error display

        **Note:**

        1. Binary import templates have extension .I2 by convention.  See
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
        gxapi_cy.WrapDU.import_bin2(GXContext._get_tls_geo(), db._wrapper, data.encode(), template.encode(), line.encode(), flight, date, wa._wrapper)
        



    @classmethod
    def import_bin4(cls, db, mode, data, template, line, flight, date, wa):
        """
        Same as `import_bin2 <geosoft.gxapi.GXDU.import_bin2>` but with an import mode

        **Note:**

        Same as `import_bin2 <geosoft.gxapi.GXDU.import_bin2>` but with an import mode

        .. seealso::

            `import_bin2 <geosoft.gxapi.GXDU.import_bin2>`
        """
        gxapi_cy.WrapDU.import_bin4(GXContext._get_tls_geo(), db._wrapper, mode, data.encode(), template.encode(), line.encode(), flight, date, wa._wrapper)
        



    @classmethod
    def import_daarc500_serial(cls, db, line, file, channel, type):
        """
        Import Serial data from the RMS Instruments DAARC500.

        **Note:**

        Imports data stored in a serial channel recorded
        by the RMS Instruments DAARC500 instrument, and outputs the data to
        a line in the database. The channels created depend on the input data type
        """
        gxapi_cy.WrapDU.import_daarc500_serial(GXContext._get_tls_geo(), db._wrapper, line, file.encode(), channel, type)
        



    @classmethod
    def import_daarc500_serial_gps(cls, db, line, file, channel):
        """
        Import Serial GPS data from the RMS Instruments DAARC500.

        **Note:**

        Imports GPS data stored in a serial channel recorded
        by the RMS Instruments DAARC500 instrument, and outputs the data to
        a line in the database. Makes the following channels:
        
        Fid, UTC_Time, Latitude, Longitude, Altitude, GPS_Quality,
        NumSat (Number of satellites), GPS_HDOP (Horizontal Dilution of Position),
        Undulation, GPS_DiffAge (Age of differential channel).
        """
        gxapi_cy.WrapDU.import_daarc500_serial_gps(GXContext._get_tls_geo(), db._wrapper, line, file.encode(), channel)
        



    @classmethod
    def import_dao(cls, db, data, type, table, template, line):
        """
        Import an external database table into a group using DAO.

        **Note:**

        1. The import template can be in the local directory or the GEOSOFT
        directory.  The import data file must include the path if it is not
        in the local directory.
        
        2. Only the import template must be specified. The database file name,
        file type, the database table and Oasis line name are normally
        taken from the template file itself, but if these values are provided,
        they will override those found in the template.
        
        3. If the line already exists, the data will overwrite the existing data.
        """
        gxapi_cy.WrapDU.import_dao(GXContext._get_tls_geo(), db._wrapper, data.encode(), type.encode(), table.encode(), template.encode(), line.encode())
        



    @classmethod
    def import_esri(cls, db, connect, template, line):
        """
        Import an ArcGIS Geodatabase table or feature class into a GDB group

        **Note:**

        1. The import template can be in the local directory or the GEOSOFT
        directory.
        
        2. Only the import template must be specified. The Geodatabase connection string
        and Oasis line name are normally taken from the template file itself,
        but if these values are provided, they will override those found in the template.
        
        3. If the line already exists, the data will overwrite the existing data.
        """
        gxapi_cy.WrapDU.import_esri(GXContext._get_tls_geo(), db._wrapper, connect.encode(), template.encode(), line.encode())
        



    @classmethod
    def import_gbn(cls, db, file):
        """
        Import GBN data file.
        """
        gxapi_cy.WrapDU.import_gbn(GXContext._get_tls_geo(), db._wrapper, file.encode())
        



    @classmethod
    def import_oddf(cls, db, file):
        """
        Import ODDF data file.
        """
        gxapi_cy.WrapDU.import_oddf(GXContext._get_tls_geo(), db._wrapper, file.encode())
        



    @classmethod
    def import_pico(cls, db, template, data, chans):
        """
        Import a Picodas data file.
        """
        gxapi_cy.WrapDU.import_pico(GXContext._get_tls_geo(), db._wrapper, template.encode(), data.encode(), chans)
        



    @classmethod
    def import_ubc_mod_msh(cls, db, mesh, mods, dir, dummy):
        """
        Import UBC Mod and Msh files.

        **Note:**

        Each slice in X,Y or Z is imported to its own line in the database
        beginning with L0.
        """
        gxapi_cy.WrapDU.import_ubc_mod_msh(GXContext._get_tls_geo(), db._wrapper, mesh.encode(), mods.encode(), dir, dummy)
        



    @classmethod
    def import_usgs_post(cls, db, file):
        """
        Import USGS Post data file.
        """
        gxapi_cy.WrapDU.import_usgs_post(GXContext._get_tls_geo(), db._wrapper, file.encode())
        



    @classmethod
    def import_xyz(cls, db, mode, data, template):
        """
        Import XYZ data into the database.

        **Note:**

        1. The import template can be in the local directory or the GEOSOFT
        directory.  The import data file must include the path if it is not
        in the local directory.
        
        2. Both the import template and data file must exist.
        """
        gxapi_cy.WrapDU.import_xyz(GXContext._get_tls_geo(), db._wrapper, mode, data.encode(), template.encode())
        



    @classmethod
    def import_xyz2(cls, db, mode, data, template, wa):
        """
        Import XYZ data into the database.

        **Note:**

        1. The import template can be in the local directory or the GEOSOFT
        directory.  The import data file must include the path if it is not
        in the local directory.
        
        2. Both the import template and data file must exist.
        """
        gxapi_cy.WrapDU.import_xyz2(GXContext._get_tls_geo(), db._wrapper, mode, data.encode(), template.encode(), wa._wrapper)
        



    @classmethod
    def import_io_gas(cls, db, data_csv, template):
        """
        Import data columns from an ioGAS data file.

        **Note:**

        1. All columns in the speficied ioGAS data file will be imported.
        2. If a line already exists, the data will overwrite the existing data.
        """
        gxapi_cy.WrapDU.import_io_gas(GXContext._get_tls_geo(), db._wrapper, data_csv.encode(), template.encode())
        



    @classmethod
    def index_order(cls, db, line, in_ch, ch):
        """
        Change the order of a channel using an index channel.
        """
        gxapi_cy.WrapDU.index_order(GXContext._get_tls_geo(), db._wrapper, line, in_ch, ch)
        



    @classmethod
    def interp(cls, db, line, i_ch, o_ch, inside, outside):
        """
        Replace all dummies by interpolating from valid data.
        """
        gxapi_cy.WrapDU.interp(GXContext._get_tls_geo(), db._wrapper, line, i_ch, o_ch, inside, outside)
        



    @classmethod
    def interp_gap(cls, db, line, i_ch, o_ch, inside, outside, gap, extend):
        """
        Replace all dummies by interpolating from valid data.
        """
        gxapi_cy.WrapDU.interp_gap(GXContext._get_tls_geo(), db._wrapper, line, i_ch, o_ch, inside, outside, gap, extend)
        



    @classmethod
    def intersect(cls, db, x_chan, y_chan, z_chan, tol, file):
        """
        Create Tie Line & Normal Line intersect table.
        """
        gxapi_cy.WrapDU.intersect(GXContext._get_tls_geo(), db._wrapper, x_chan, y_chan, z_chan, tol, file.encode())
        



    @classmethod
    def intersect_all(cls, db, x_chan, y_chan, z_chan, tol, file):
        """
        Create line intersect table from all lines.
        """
        gxapi_cy.WrapDU.intersect_all(GXContext._get_tls_geo(), db._wrapper, x_chan, y_chan, z_chan, tol, file.encode())
        



    @classmethod
    def intersect_gd_bto_tbl(cls, db, tbl):
        """
        Create a new intersection table from an intersection database.

        **Note:**

        If the TBL exists, it is overwritten.
        """
        gxapi_cy.WrapDU.intersect_gd_bto_tbl(GXContext._get_tls_geo(), db.encode(), tbl.encode())
        



    @classmethod
    def intersect_old(cls, db, x_chan, y_chan, z_chan, in_file, out_file):
        """
        Use existing intersection table and re-calculate miss-ties.

        **Note:**

        Reads intersection information from an existing intersect
        table and looks up the values at the intersections for the
        input Z channel. This makes it unnecessary to re-calculate
        the intersections every time if you want to determine
        miss-ties using different Z channels, or the same Z channel
        after processing levelling corrections. Existing intersections
        whose locations do not exist in the database are ignored.
        """
        gxapi_cy.WrapDU.intersect_old(GXContext._get_tls_geo(), db._wrapper, x_chan, y_chan, z_chan, in_file.encode(), out_file.encode())
        



    @classmethod
    def intersect_tb_lto_gdb(cls, tbl, db):
        """
        Create a new intersection database from an intersection table.

        **Note:**

        If the GDB exists, it is deleted, so it should not
        be loaded.
        The database is split by Tie lines (or whatever lines are found in column 3
        of the TBL file.
        """
        gxapi_cy.WrapDU.intersect_tb_lto_gdb(GXContext._get_tls_geo(), tbl.encode(), db.encode())
        



    @classmethod
    def lab_template(cls, data, template, type, delimit, name_off, unit_off, data_off, sample_type, data_type):
        """
        Makes a default template from a lab assay file.

        **Note:**

        The template can be used to import the file using
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
        gxapi_cy.WrapDU.lab_template(GXContext._get_tls_geo(), data.encode(), template.encode(), type, delimit.encode(), name_off, unit_off, data_off, sample_type, data_type)
        



    @classmethod
    def load_gravity(cls, db, reg, line, data):
        """
        Load a gravity survey file

        **Note:**

        See GRAVITY.`GXDAT <geosoft.gxapi.GXDAT>` for a description of the file format.
        
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
        gxapi_cy.WrapDU.load_gravity(GXContext._get_tls_geo(), db._wrapper, reg._wrapper, line, data.encode())
        



    @classmethod
    def load_ltb(cls, db, line, ltb, mode):
        """
        Load `GXLTB <geosoft.gxapi.GXLTB>` into a database line.

        **Note:**

        A new channel will be created for all `GXLTB <geosoft.gxapi.GXLTB>` fields
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
        gxapi_cy.WrapDU.load_ltb(GXContext._get_tls_geo(), db._wrapper, line, ltb._wrapper, mode)
        



    @classmethod
    def make_fid(cls, db, line, i_ch, o_ch):
        """
        Make a fiducial channel based on an existing channel.
        """
        gxapi_cy.WrapDU.make_fid(GXContext._get_tls_geo(), db._wrapper, line, i_ch, o_ch)
        



    @classmethod
    def mask(cls, db, line, i_ch, m_ch):
        """
        Mask dummies in one channel against another.
        """
        gxapi_cy.WrapDU.mask(GXContext._get_tls_geo(), db._wrapper, line, i_ch, m_ch)
        



    @classmethod
    def math(cls, db, line, exp):
        """
        Apply an expression to the database

        **Note:**

        The MATH_DU method will READWRITE lock channels on the left
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
        gxapi_cy.WrapDU.math(GXContext._get_tls_geo(), db._wrapper, line, exp._wrapper)
        



    @classmethod
    def merge_line(cls, db, i_line, m_line, o_line, mode):
        """
        Merge a line a the fiducial and copies any data past
        that fiducial into the new line.
        """
        gxapi_cy.WrapDU.merge_line(GXContext._get_tls_geo(), db._wrapper, i_line, m_line, o_line, mode)
        



    @classmethod
    def mod_fid_range(cls, db, ln, fid_start, incr, start_index, num, opt):
        """
        Insert/Append/Delete a range of fids.

        **Note:**

        Channels that do not have the same fid start or fid
        increment are not processed.
        
        Protected channels are modified automatically.
        """
        gxapi_cy.WrapDU.mod_fid_range(GXContext._get_tls_geo(), db._wrapper, ln, fid_start, incr, start_index, num, opt)
        



    @classmethod
    def move(cls, db, line, i_ch, c_ch, o_ch, mode):
        """
        Move/correct a channel to a control channel.

        **Note:**

        The input channel is moved to the absolute location
        of the control channel.
        """
        gxapi_cy.WrapDU.move(GXContext._get_tls_geo(), db._wrapper, line, i_ch, c_ch, o_ch, mode)
        



    @classmethod
    def nl_filt(cls, db, line, i_ch, o_ch, width, tol):
        """
        This method applies a non-linear filter to the specified
        line/channel and places the output in the output channel.
        """
        gxapi_cy.WrapDU.nl_filt(GXContext._get_tls_geo(), db._wrapper, line, i_ch, o_ch, width, tol)
        



    @classmethod
    def normal(cls, db, ch, ignore):
        """
        Set fid of all channels to match a specified channel.

        .. seealso::

            `re_fid_all_ch <geosoft.gxapi.GXDU.re_fid_all_ch>`
        """
        gxapi_cy.WrapDU.normal(GXContext._get_tls_geo(), db._wrapper, ch, ignore)
        



    @classmethod
    def poly_fill(cls, db, line, x_chan, y_chan, r_chan, pply, dummy):
        """
        Fill using a polygon with a value of 1.
        """
        gxapi_cy.WrapDU.poly_fill(GXContext._get_tls_geo(), db._wrapper, line, x_chan, y_chan, r_chan, pply._wrapper, dummy)
        



    @classmethod
    def poly_mask(cls, db, line, x_chan, y_chan, r_chan, pply, dummy):
        """
        Mask against a polygon.
        """
        gxapi_cy.WrapDU.poly_mask(GXContext._get_tls_geo(), db._wrapper, line, x_chan, y_chan, r_chan, pply._wrapper, dummy)
        



    @classmethod
    def project_data(cls, db, line, ix_ch, iy_ch, ox_ch, oy_ch, pj):
        """
        Project X,Y channels

        **Note:**

        Output channels can be the same as input channels
        """
        gxapi_cy.WrapDU.project_data(GXContext._get_tls_geo(), db._wrapper, line, ix_ch, iy_ch, ox_ch, oy_ch, pj._wrapper)
        



    @classmethod
    def project_xyz(cls, db, line, ix_ch, iy_ch, iz_ch, ox_ch, oy_ch, oz_ch, pj):
        """
        Project X,Y,Z channels from one system to another.

        **Note:**

        Output channels can be the same as input channels
        """
        gxapi_cy.WrapDU.project_xyz(GXContext._get_tls_geo(), db._wrapper, line, ix_ch, iy_ch, iz_ch, ox_ch, oy_ch, oz_ch, pj._wrapper)
        



    @classmethod
    def proj_points(cls, db, line, ix_ch, iy_ch, iz_ch, ox_ch, oy_ch, oz_ch, i_name_chan, i_datum_chan, i_method_chan, i_unit_chan, il_datum_chan, o_name_chan, o_datum_chan, o_method_chan, o_unit_chan, ol_datum_chan, error_chan, force_local_datum):
        """
        Project X,Y(Z) channels with different projections

        **Note:**

        Output channels can be the same as input channels
        """
        gxapi_cy.WrapDU.proj_points(GXContext._get_tls_geo(), db._wrapper, line, ix_ch, iy_ch, iz_ch, ox_ch, oy_ch, oz_ch, i_name_chan, i_datum_chan, i_method_chan, i_unit_chan, il_datum_chan, o_name_chan, o_datum_chan, o_method_chan, o_unit_chan, ol_datum_chan, error_chan, force_local_datum)
        



    @classmethod
    def qc_init_separation(cls, db, sep, dir):
        """
        Creates the nearest line channels for line separation QC.

        **Note:**

        This must be called before QCSeparation_DU. It uses a pager to
        establish the relative positions of the selected lines, then,
        for every point determines the closest point in another line to
        the left and to the right (as determined by looking in the
        direction of the line.) These distances are stored to two new
        channels in the database, "Closest_Left" and "Closest_Right"
        """
        gxapi_cy.WrapDU.qc_init_separation(GXContext._get_tls_geo(), db._wrapper, sep, dir)
        



    @classmethod
    def qc_survey_plan(cls, db, wa, pply, sl_spa, sl_azi, slx, sly, sl_sta, sl_inc, tl_spa, tl_azi, tlx, tly, tl_sta, tl_inc, type, sample_spacing, extend_outside):
        """
        Create a database containing proposed survey plan in a `GXPLY <geosoft.gxapi.GXPLY>`

        **Note:**

        The LINE on which has the reference (X,Y) will have the starting Line number
        The lines on the right hand side of the reference line (while looking
        into azimuth of ref. line) have increasing line numbers. The lines
        on the left hand side have the decreasing line numbers from the starting
        number. Returns an error code or 0 (if successful)
        """
        ret_val = gxapi_cy.WrapDU.qc_survey_plan(GXContext._get_tls_geo(), db._wrapper, wa._wrapper, pply._wrapper, sl_spa, sl_azi, slx, sly, sl_sta, sl_inc, tl_spa, tl_azi, tlx, tly, tl_sta, tl_inc, type, sample_spacing, extend_outside)
        return ret_val



    @classmethod
    def direction(cls, db, line, x_ch, y_ch):
        """
        Returns the direction of a line.

        **Note:**

        The direction is calculated from the first and last
        non-dummy locations in the X and Y reference channels.
        """
        ret_val = gxapi_cy.WrapDU.direction(GXContext._get_tls_geo(), db._wrapper, line, x_ch, y_ch)
        return ret_val



    @classmethod
    def re_fid(cls, db, line, in_ch, ref_ch, out_ch, mode, start, incr, gap):
        """
        Re-fid a channel based on a reference channel

        **Note:**

        The original channel can be an array channel, in which case
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
        gxapi_cy.WrapDU.re_fid(GXContext._get_tls_geo(), db._wrapper, line, in_ch, ref_ch, out_ch, mode, start, incr, gap)
        



    @classmethod
    def re_fid_all_ch(cls, db, line, ref_ch):
        """
        Simple re-fid of all channels based on a reference channel

        **Note:**

        Channels can be array channels, in which case
        the columns are individually re-fidded.

        .. seealso::

            `normal <geosoft.gxapi.GXDU.normal>`
        """
        gxapi_cy.WrapDU.re_fid_all_ch(GXContext._get_tls_geo(), db._wrapper, line, ref_ch)
        



    @classmethod
    def re_fid_ch(cls, db, line, ref_ch, ch):
        """
        Simple re-fid of a channel based on a reference channel

        **Note:**

        The original channel can be an array channel, in which case
        the columns are individually re-fidded.
        
        `re_fid_ch <geosoft.gxapi.GXDU.re_fid_ch>` resamples the "Channel to refid" to the "Reference Channel" Fid
        range and increment.
        """
        gxapi_cy.WrapDU.re_fid_ch(GXContext._get_tls_geo(), db._wrapper, line, ref_ch, ch)
        



    @classmethod
    def rotate(cls, db, line, in_x_ch, in_y_ch, out_x_ch, out_y_ch, x0, y0, deg):
        """
        Rotate coordinates.
        """
        gxapi_cy.WrapDU.rotate(GXContext._get_tls_geo(), db._wrapper, line, in_x_ch, in_y_ch, out_x_ch, out_y_ch, x0, y0, deg)
        



    @classmethod
    def sample_gd(cls, db, line, ix_ch, iy_ch, o_ch, img):
        """
        Sample a `GXGD <geosoft.gxapi.GXGD>` at a specified X and Y.

        **Note:**

        Values in result channel
        """
        gxapi_cy.WrapDU.sample_gd(GXContext._get_tls_geo(), db._wrapper, line, ix_ch, iy_ch, o_ch, img._wrapper)
        



    @classmethod
    def sample_img(cls, db, line, ix_ch, iy_ch, o_ch, img):
        """
        Sample a `GXIMG <geosoft.gxapi.GXIMG>` at a specified X and Y.

        **Note:**

        Values in result channel
        """
        gxapi_cy.WrapDU.sample_img(GXContext._get_tls_geo(), db._wrapper, line, ix_ch, iy_ch, o_ch, img._wrapper)
        



    @classmethod
    def sample_img_line_lst(cls, db, lst, ix_ch, iy_ch, o_ch, img):
        """
        Sample an `GXIMG <geosoft.gxapi.GXIMG>` at a specified X and Y, for a `GXLST <geosoft.gxapi.GXLST>` of lines.

        **Note:**

        Values in result channel
        """
        gxapi_cy.WrapDU.sample_img_line_lst(GXContext._get_tls_geo(), db._wrapper, lst._wrapper, ix_ch, iy_ch, o_ch, img._wrapper)
        



    @classmethod
    def scan_ado(cls, connect, table, template):
        """
        Scans an external ADO database and generates a default template.

        **Note:**

        All the channels are listed
        """
        gxapi_cy.WrapDU.scan_ado(GXContext._get_tls_geo(), connect.encode(), table.encode(), template.encode())
        



    @classmethod
    def scan_aseg(cls, file, data, flc, template):
        """
        This method scans an ASEG-GDF file and generates a default
        template listing all the channels and all the ALIAS lines.
        """
        gxapi_cy.WrapDU.scan_aseg(GXContext._get_tls_geo(), file.encode(), data.encode(), flc.encode(), template.encode())
        



    @classmethod
    def scan_dao(cls, file, type, table, template):
        """
        Scans an external DAO database and generates a default template.

        **Note:**

        All the channels are listed
        """
        gxapi_cy.WrapDU.scan_dao(GXContext._get_tls_geo(), file.encode(), type.encode(), table.encode(), template.encode())
        



    @classmethod
    def scan_pico(cls, data, template):
        """
        This method scans a picodas file and generates a default
        template listing all the channels and all the ALIAS lines.
        """
        gxapi_cy.WrapDU.scan_pico(GXContext._get_tls_geo(), data.encode(), template.encode())
        



    @classmethod
    def sort(cls, db, line, ch, sort):
        """
        Sort the contents of a channel.
        """
        gxapi_cy.WrapDU.sort(GXContext._get_tls_geo(), db._wrapper, line, ch, sort)
        



    @classmethod
    def sort_index(cls, db, line, ch, in_ch, sort):
        """
        Create an ordered index of the contents of a channel.
        """
        gxapi_cy.WrapDU.sort_index(GXContext._get_tls_geo(), db._wrapper, line, ch, in_ch, sort)
        



    @classmethod
    def sort_index2(cls, db, line, ch1, sort1, ch2, sort2, in_ch):
        """
        Create an ordered index from two channels
        """
        gxapi_cy.WrapDU.sort_index2(GXContext._get_tls_geo(), db._wrapper, line, ch1, sort1, ch2, sort2, in_ch)
        



    @classmethod
    def split_line(cls, db, i_line, o_line, fid):
        """
        Splits a line a the fiducial and copies any data past
        that fiducial into the new line.
        """
        gxapi_cy.WrapDU.split_line(GXContext._get_tls_geo(), db._wrapper, i_line, o_line, fid)
        



    @classmethod
    def split_line2(cls, db, i_line, o_line, fid, reset_fi_ds):
        """
        Splits a line a the fiducial and copies any data past
        that fiducial into the new line.

        **Note:**

        The same as SplitLine, but with an option to reset each line's starting fiducial to zero.
        """
        gxapi_cy.WrapDU.split_line2(GXContext._get_tls_geo(), db._wrapper, i_line, o_line, fid, reset_fi_ds)
        



    @classmethod
    def split_line_xy(cls, db, line, x_ch, y_ch, dirctn, tolrnc, down_tol, method, first_line, line_inc):
        """
        Break up a line based on tolerance of lateral and horizontal distance, with
        options for the output line names.

        **Note:**

        The original line will be deleted.
        """
        first_line.value = gxapi_cy.WrapDU.split_line_xy(GXContext._get_tls_geo(), db._wrapper, line, x_ch, y_ch, dirctn, tolrnc, down_tol, method, first_line.value, line_inc)
        



    @classmethod
    def split_line_xy2(cls, db, line, x_ch, y_ch, dirctn, tolrnc, down_tol, method, first_line, line_inc, reset_fi_ds):
        """
        Break up a line based on tolerance of lateral and horizontal distance, with
        options for the output line names.

        **Note:**

        The same as SplitLineXY, but with an option to reset each line's starting fiducial to zero.
        """
        first_line.value = gxapi_cy.WrapDU.split_line_xy2(GXContext._get_tls_geo(), db._wrapper, line, x_ch, y_ch, dirctn, tolrnc, down_tol, method, first_line.value, line_inc, reset_fi_ds)
        



    @classmethod
    def split_line_xy3(cls, db, line, x_ch, y_ch, dirctn, tolrnc, down_tol, method, first_line, line_inc, retain_line_type, reset_fi_ds):
        """
        Break up a line based on tolerance of lateral and horizontal distance, with
        options for the output line names.

        **Note:**

        The same as SplitLineXY2, but with the option to maintain line types when outputting sequentially numbered lines.
        """
        first_line.value = gxapi_cy.WrapDU.split_line_xy3(GXContext._get_tls_geo(), db._wrapper, line, x_ch, y_ch, dirctn, tolrnc, down_tol, method, first_line.value, line_inc, retain_line_type, reset_fi_ds)
        



    @classmethod
    def split_line_by_direction(cls, db, line, x_ch, y_ch, angular_change, over_a_distance_of, minimum_line_length, break_on_separation_distance, save_discards, method, first_line, line_inc, reset_fi_ds):
        """
        The line is split when the heading (calculated from the current X and Y channels) changes by more than a specified amount over
        a specified distance. Additional options to discard too-short lines

        **Note:**

        Split a line based on changes in heading.
        """
        first_line.value = gxapi_cy.WrapDU.split_line_by_direction(GXContext._get_tls_geo(), db._wrapper, line, x_ch, y_ch, angular_change, over_a_distance_of, minimum_line_length, break_on_separation_distance, save_discards, method, first_line.value, line_inc, reset_fi_ds)
        



    @classmethod
    def split_line_by_direction2(cls, db, line, x_ch, y_ch, angular_change, over_a_distance_of, minimum_line_length, break_on_separation_distance, save_discards, method, first_line, line_inc, retain_line_type, reset_fi_ds):
        """
        The same as SplitLineByDirection, but with the option to maintain line types when outputting sequentially numbered lines.

        **Note:**

        Split a line based on changes in heading.
        """
        first_line.value = gxapi_cy.WrapDU.split_line_by_direction2(GXContext._get_tls_geo(), db._wrapper, line, x_ch, y_ch, angular_change, over_a_distance_of, minimum_line_length, break_on_separation_distance, save_discards, method, first_line.value, line_inc, retain_line_type, reset_fi_ds)
        



    @classmethod
    def stat(cls, db, line, i_ch, st):
        """
        Add a data channel to a statistics object.

        **Note:**

        If the input channel is a `GXVA <geosoft.gxapi.GXVA>` (array) channel, then the columns set using
        `GXDB.set_va_windows <geosoft.gxapi.GXDB.set_va_windows>` are used in the statistics; all columns are used by default.

        .. seealso::

            `GXST <geosoft.gxapi.GXST>`
        """
        gxapi_cy.WrapDU.stat(GXContext._get_tls_geo(), db._wrapper, line, i_ch, st._wrapper)
        



    @classmethod
    def table_line_fid(cls, db, chan, ref, tb, field):
        """
        Place a Line/Fid information into a Channel.
        """
        gxapi_cy.WrapDU.table_line_fid(GXContext._get_tls_geo(), db._wrapper, chan, ref, tb._wrapper, field)
        



    @classmethod
    def table_selected_lines_fid(cls, db, chan, ref, tb, field):
        """
        Place a Line/Fid information into a Channel for the selected lines in the database.
        """
        gxapi_cy.WrapDU.table_selected_lines_fid(GXContext._get_tls_geo(), db._wrapper, chan, ref, tb._wrapper, field)
        



    @classmethod
    def time_constant(cls, db, line, resp_chan, time_chan, tau_chan, intercept_chan, fit_chan, log_opt):
        """
        Calculate TEM time constant (Tau)

        **Note:**

        When DU_TIME_LOG option is used, Time channel will be converted
        with logarithmic before calculating time constant.
        Logarthmic conversion is always applied to the response channel.
        """
        gxapi_cy.WrapDU.time_constant(GXContext._get_tls_geo(), db._wrapper, line, resp_chan, time_chan, tau_chan, intercept_chan, fit_chan, log_opt)
        



    @classmethod
    def trend(cls, db, line, i_ch, o_ch, order):
        """
        Calculates an n'th order trend of a data channel.

        .. seealso::

            `b_spline <geosoft.gxapi.GXDU.b_spline>`
        """
        gxapi_cy.WrapDU.trend(GXContext._get_tls_geo(), db._wrapper, line, i_ch, o_ch, order)
        



    @classmethod
    def update_intersect_db(cls, db, x_chan, z_chan, int_db):
        """
        Update the Z and DZ values in an intersection database, using the current database.

        **Note:**

        Updates the TZ, TDZ, LZ and LDZ channels at the intersections,
        using the current flight database.
        """
        gxapi_cy.WrapDU.update_intersect_db(GXContext._get_tls_geo(), db._wrapper, x_chan, z_chan, int_db._wrapper)
        



    @classmethod
    def voxel_section(cls, db, line, x_ch, y_ch, vox, grid, cell_x, cell_y, interp):
        """
        Slice a voxel to a grid under a database line.

        **Note:**

        Takes the first and XY locations in a line (using the
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
        gxapi_cy.WrapDU.voxel_section(GXContext._get_tls_geo(), db._wrapper, line, x_ch, y_ch, vox._wrapper, grid.encode(), cell_x, cell_y, interp)
        



    @classmethod
    def write_wa(cls, db, line, lst, wa):
        """
        Write data to an ASCII file.

        **Note:**

        Channels to be written should be placed in a `GXLST <geosoft.gxapi.GXLST>` object.
        
        Channels are written in the order of the list.  Only the
        channel names in the list are used.
        
        Data is formated as in the channel definition and
        channels are separated by a single space character.
        """
        gxapi_cy.WrapDU.write_wa(GXContext._get_tls_geo(), db._wrapper, line, lst._wrapper, wa._wrapper)
        



    @classmethod
    def xyz_line(cls, db, line, x_ch, y_ch, dirctn, tolrnc):
        """
        Break up a line based on tolerance of lateral distance.

        **Note:**

        The original line will be deleted.
        """
        gxapi_cy.WrapDU.xyz_line(GXContext._get_tls_geo(), db._wrapper, line, x_ch, y_ch, dirctn, tolrnc)
        



    @classmethod
    def xyz_line2(cls, db, line, x_ch, y_ch, dirctn, tolrnc, down_tol):
        """
        Break up a line based on tolerance of lateral and horizontal distance.

        **Note:**

        The original line will be deleted.
        """
        gxapi_cy.WrapDU.xyz_line2(GXContext._get_tls_geo(), db._wrapper, line, x_ch, y_ch, dirctn, tolrnc, down_tol)
        



    @classmethod
    def xyz_line3(cls, db, line, x_ch, y_ch, dirctn, tolrnc, down_tol, reset_fi_ds):
        """
        Break up a line based on tolerance of lateral and horizontal distance.

        **Note:**

        The same as XyzLine2, but with an option to reset each line's starting fiducial to zero.
        """
        gxapi_cy.WrapDU.xyz_line3(GXContext._get_tls_geo(), db._wrapper, line, x_ch, y_ch, dirctn, tolrnc, down_tol, reset_fi_ds)
        



    @classmethod
    def z_mask(cls, db, line, chan, z_chan, zmin, zmax):
        """
        Mask dummies in one channel against another(Z) with the range Zmin/Zmax.
        """
        gxapi_cy.WrapDU.z_mask(GXContext._get_tls_geo(), db._wrapper, line, chan, z_chan, zmin, zmax)
        



    @classmethod
    def range_xy(cls, db, x_min, y_min, x_max, y_max):
        """
        Find the range of X, and Y in the selected lines.

        **Note:**

        Returns the range in X and Y of the current X and Y channels.
        Returned values are dummy if no valid items are found.
        """
        x_min.value, y_min.value, x_max.value, y_max.value = gxapi_cy.WrapDU.range_xy(GXContext._get_tls_geo(), db._wrapper, x_min.value, y_min.value, x_max.value, y_max.value)
        



    @classmethod
    def range_xyz(cls, db, x_ch, y_ch, z_ch, x_min, y_min, z_min, x_max, y_max, z_max, n_tot):
        """
        Find the range of X, Y and Z in selected lines.

        **Note:**

        The X, Y and Z channels should be normal (not array) channels.
        Only locations where all values are non-dummy are included in the calculation.
        If no non-dummy values are found, Dummy values are returned.
        """
        x_min.value, y_min.value, z_min.value, x_max.value, y_max.value, z_max.value, n_tot.value = gxapi_cy.WrapDU.range_xyz(GXContext._get_tls_geo(), db._wrapper, x_ch, y_ch, z_ch, x_min.value, y_min.value, z_min.value, x_max.value, y_max.value, z_max.value, n_tot.value)
        



    @classmethod
    def range_xyz_data(cls, db, x_ch, y_ch, z_ch, d_ch, x_min, y_min, z_min, d_min, x_max, y_max, z_max, d_max, n_tot):
        """
        Find the range of X, Y, Z and Data values in selected lines.

        **Note:**

        The Z and Data channels may be array channels, but both must have
        the same number of columns.
        Only values where all channels are non-dummy (or, for `GXVA <geosoft.gxapi.GXVA>` channels,
        where the Z or Data value are defined) are included in the calculation.
        If no non-dummy values are found, Dummy values are returned.
        This function is optimized for cases where Z and Data are array channels
        with many columns (e.g. 32 or more columns).
        """
        x_min.value, y_min.value, z_min.value, d_min.value, x_max.value, y_max.value, z_max.value, d_max.value, n_tot.value = gxapi_cy.WrapDU.range_xyz_data(GXContext._get_tls_geo(), db._wrapper, x_ch, y_ch, z_ch, d_ch, x_min.value, y_min.value, z_min.value, d_min.value, x_max.value, y_max.value, z_max.value, d_max.value, n_tot.value)
        



    @classmethod
    def create_drillhole_parameter_weight_constraint_database(cls, db, ch, reg, database):
        """
        Used for weighting inversion models.

        **Note:**

        Control parameters are passed in the `GXREG <geosoft.gxapi.GXREG>` (to allow for future expansion without
        the need to modify the wrappers).
        The input drillhole database must contain current X, Y and Z channels.
        Drillhole data should be equally spaced (or nearly so) down the hole.
        Weights are calculated on a circle perpendicular to the hole at each point.
        
        RADIUS - Maximum radius from drillhole to create weighting points (Default = 100).
        INCRMENENT - Grid cell size in weighting circle (Default = 10).
        MINIMUM - the minimum weighting value to apply, at the radius (Default = 0.0001).
        POWER - Exponential power to use in the weighting function (negative of this is used) (Default = 2).
        """
        gxapi_cy.WrapDU.create_drillhole_parameter_weight_constraint_database(GXContext._get_tls_geo(), db._wrapper, ch, reg._wrapper, database.encode())
        



    @classmethod
    def calculate_draped_survey_altitude(cls, db, line, x_ch, y_ch, img, z_ch, ascent, descent, drape_height, n_hanning, hanning_width, min_curvature):
        """
        Calculate a draped flight path, enforcing maximum descent and ascent rates.

        **Note:**

        Calculate a draped flight path, enforcing maximum descent and ascent rates. Additional Inputs are the sample distance along the line
        and a topography grid.
        """
        gxapi_cy.WrapDU.calculate_draped_survey_altitude(GXContext._get_tls_geo(), db._wrapper, line, x_ch, y_ch, img._wrapper, z_ch, ascent, descent, drape_height, n_hanning, hanning_width, min_curvature)
        



    @classmethod
    def calculate_draped_survey_altitude2(cls, db, line, x_ch, y_ch, img, dem_ch, z_ch, ascent, descent, drape_height, min_drape_height, n_hanning, hanning_width, min_curvature):
        """
        Calculate a draped flight path, enforcing maximum descent and ascent rates.

        **Note:**

        Calculate a draped flight path, enforcing maximum descent and ascent rates.
        Set both a nominal and minimum drape height.
        Additional Inputs are the sample distance along the line
        and a topography grid.
        """
        gxapi_cy.WrapDU.calculate_draped_survey_altitude2(GXContext._get_tls_geo(), db._wrapper, line, x_ch, y_ch, img._wrapper, dem_ch, z_ch, ascent, descent, drape_height, min_drape_height, n_hanning, hanning_width, min_curvature)
        



    @classmethod
    def direct_grid_data_to_voxel(cls, db, x_channel, y_channel, z_channel, data_channel, output_voxel_filename, origin_x, origin_y, origin_z, cell_count_x, cell_count_y, cell_count_z, cell_size_x, cell_size_y, cell_size_z, method):
        """
        Create a voxel using direct gridding.

        **Note:**

        The Z and Data channels may be array channels. If they are, the array sizes must match.
        """
        gxapi_cy.WrapDU.direct_grid_data_to_voxel(GXContext._get_tls_geo(), db._wrapper, x_channel, y_channel, z_channel, data_channel, output_voxel_filename.encode(), origin_x, origin_y, origin_z, cell_count_x, cell_count_y, cell_count_z, cell_size_x, cell_size_y, cell_size_z, method)
        



    @classmethod
    def direct_grid_item_counts_to_voxel(cls, db, x_channel, y_channel, z_channel, data_channel, output_voxel_filename, origin_x, origin_y, origin_z, cell_count_x, cell_count_y, cell_count_z, cell_size_x, cell_size_y, cell_size_z, pb_replace_zeroes_with_dummy):
        """
        Create a voxel using direct gridding containing the number of data points in each cell.

        **Note:**

        The Z and Data channels may be array channels. If they are, the array sizes must match.
        """
        gxapi_cy.WrapDU.direct_grid_item_counts_to_voxel(GXContext._get_tls_geo(), db._wrapper, x_channel, y_channel, z_channel, data_channel, output_voxel_filename.encode(), origin_x, origin_y, origin_z, cell_count_x, cell_count_y, cell_count_z, cell_size_x, cell_size_y, cell_size_z, pb_replace_zeroes_with_dummy)
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer