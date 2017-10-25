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

    `GXDU` functions provide a variety of common utilities that can be applied
    efficiently to the contents of a database. Most `GXDU` library functions take
    as their first argument a `GXDB` object, and apply standard processes to data
    stored in an OASIS database, including import and export functions.

    **Note:**

    The following defines are used by GX functions but are not required
    for any methods:
    
    `DU_LINES`
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
    def table_look1(cls, p1, p2, p3, p4, p5, p6, p7, p8, p9):
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
        gxapi_cy.WrapDU.table_look1(GXContext._get_tls_geo(), p1._wrapper, p2, p3, p4, p5.encode(), p6.encode(), p7, p8, p9._wrapper)
        



    @classmethod
    def table_look2(cls, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11):
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
        gxapi_cy.WrapDU.table_look2(GXContext._get_tls_geo(), p1._wrapper, p2, p3, p4, p5, p6.encode(), p7.encode(), p8.encode(), p9, p10, p11._wrapper)
        



    @classmethod
    def table_look_i2(cls, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11):
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
        gxapi_cy.WrapDU.table_look_i2(GXContext._get_tls_geo(), p1._wrapper, p2, p3, p4, p5, p6.encode(), p7.encode(), p8.encode(), p9, p10, p11._wrapper)
        



    @classmethod
    def table_look_r2(cls, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11):
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
        gxapi_cy.WrapDU.table_look_r2(GXContext._get_tls_geo(), p1._wrapper, p2, p3, p4, p5, p6.encode(), p7.encode(), p8.encode(), p9, p10, p11._wrapper)
        



    @classmethod
    def ado_table_names(cls, p1, p2):
        """
        Scans a ADO-compliant database and returns the table names in a `GXVV`

        **Note:**

        The `GXVV` must be created to hold strings of length
        `STR_DB_SYMBOL`; i.e. use
        Creat_VV(-`STR_DB_SYMBOL`, 0), or it will assert.
        """
        gxapi_cy.WrapDU.ado_table_names(GXContext._get_tls_geo(), p1.encode(), p2._wrapper)
        



    @classmethod
    def an_sig(cls, p1, p2, p3, p4):
        """
        Calculate the Analytic Signal of a channel.
        """
        gxapi_cy.WrapDU.an_sig(GXContext._get_tls_geo(), p1._wrapper, p2, p3, p4)
        



    @classmethod
    def append(cls, p1, p2, p3):
        """
        Append a source database onto a destination database.

        **Note:**

        If the source database and destination database have channels
        with the same name, then data is appended onto the end
        of the channel in lines which have the same number.
        
        If a channel in the destination database is not also in the source
        database, it is ignored.
        """
        gxapi_cy.WrapDU.append(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3)
        



    @classmethod
    def avg_azimuth(cls, p1, p2, p3):
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
        p3.value = gxapi_cy.WrapDU.avg_azimuth(GXContext._get_tls_geo(), p1._wrapper, p2, p3.value)
        



    @classmethod
    def base_data(cls, p1, p2, p3, p4, p5, p6):
        """
        This method corrects an entire database line using a
        time-based correction table. It is given 2 input channel
        tokens and 1 output channel token as well as the table
        object to use.
        """
        gxapi_cy.WrapDU.base_data(GXContext._get_tls_geo(), p1._wrapper, p2, p3, p4, p5, p6._wrapper)
        



    @classmethod
    def base_data_ex(cls, p1, p2, p3, p4, p5, p6, p7):
        """
        This method corrects an entire database line using a
        time-based correction table. It is given 2 input channel
        tokens and 1 output channel token as well as the table
        object to use (table sort flag=1 for sort, =0 for no sort).
        """
        gxapi_cy.WrapDU.base_data_ex(GXContext._get_tls_geo(), p1._wrapper, p2, p3, p4, p5, p6._wrapper, p7)
        



    @classmethod
    def bound_line(cls, p1, p2, p3, p4, p5):
        """
        Set map boundary clip limits.
        """
        gxapi_cy.WrapDU.bound_line(GXContext._get_tls_geo(), p1._wrapper, p2, p3, p4, p5._wrapper)
        



    @classmethod
    def bp_filt(cls, p1, p2, p3, p4, p5, p6, p7):
        """
        This method applies a band-pass filter to the specified
        line/channel and places the output in the output channel.

        **Note:**

        If the short and long wavelengths are <= 0, the input channel
        is simply copied to the output channel without filtering.
        """
        gxapi_cy.WrapDU.bp_filt(GXContext._get_tls_geo(), p1._wrapper, p2, p3, p4, p5, p6, p7)
        



    @classmethod
    def break_line(cls, p1, p2, p3):
        """
        Break up a line based on line numbers in a channel.
        """
        gxapi_cy.WrapDU.break_line(GXContext._get_tls_geo(), p1._wrapper, p2, p3)
        



    @classmethod
    def break_line2(cls, p1, p2, p3, p4):
        """
        Break up a line based on line numbers in a channel.

        **Note:**

        The same as BreakLine, but with an option to reset each line's starting fiducial to zero.
        """
        gxapi_cy.WrapDU.break_line2(GXContext._get_tls_geo(), p1._wrapper, p2, p3, p4)
        



    @classmethod
    def break_line_to_groups(cls, p1, p2, p3, p4):
        """
        Break up a line into group-lines based on a channel.

        **Note:**

        The original line will be deleted.
        This is similar to `break_line`, but the output lines
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
        gxapi_cy.WrapDU.break_line_to_groups(GXContext._get_tls_geo(), p1._wrapper, p2, p3, p4.encode())
        



    @classmethod
    def break_line_to_groups2(cls, p1, p2, p3, p4, p5):
        """
        Break up a line into group-lines based on a channel.

        **Note:**

        The same as BreakLineToGroups, but with an option to reset each line's starting fiducial to zero.
        """
        gxapi_cy.WrapDU.break_line_to_groups2(GXContext._get_tls_geo(), p1._wrapper, p2, p3, p4.encode(), p5)
        



    @classmethod
    def b_spline(cls, p1, p2, p3, p4, p5, p6, p7):
        """
        B-spline Interpolate a Channel.

        .. seealso::

            `trend`
        """
        gxapi_cy.WrapDU.b_spline(GXContext._get_tls_geo(), p1._wrapper, p2, p3, p4, p5, p6, p7)
        



    @classmethod
    def closest_point(cls, p1, p2, p3, p4, p5, p6, p7):
        """
        Return closest data point to input location.

        **Note:**

        Selected lines are scanned for the (X, Y) location
        which is closest to the input location.
        The line and fiducial of the point are returned.
        
        Will register an error if no valid (X, Y) locations
        are found.
        """
        p4.value, p5.value, p6.value, p7.value = gxapi_cy.WrapDU.closest_point(GXContext._get_tls_geo(), p1._wrapper, p2, p3, p4.value, p5.value, p6.value, p7.value)
        



    @classmethod
    def copy_line(cls, p1, p2, p3):
        """
        Copy a line.

        **Note:**

        Existing channels in the output line will be replaced
        by copied channels.
        """
        gxapi_cy.WrapDU.copy_line(GXContext._get_tls_geo(), p1._wrapper, p2, p3)
        



    @classmethod
    def copy_line_across(cls, p1, p2, p3, p4):
        """
        Copy a line from one database to another.

        **Note:**

        Existing channels in the output line will be replaced
        by copied channels.

        .. seealso::

            `copy_line_chan_across` function
        """
        gxapi_cy.WrapDU.copy_line_across(GXContext._get_tls_geo(), p1._wrapper, p2, p3._wrapper, p4)
        



    @classmethod
    def copy_line_chan_across(cls, p1, p2, p3, p4, p5):
        """
        Copy a list of channels in a line from one database to another.

        **Note:**

        Existing channels in the output line will be replaced
        by copied channels.

        .. seealso::

            `copy_line_across` function
        """
        gxapi_cy.WrapDU.copy_line_chan_across(GXContext._get_tls_geo(), p1._wrapper, p2, p3._wrapper, p4._wrapper, p5)
        



    @classmethod
    def copy_line_masked(cls, p1, p2, p3, p4, p5):
        """
        Copy a line, prune items based on a mask channel

        **Note:**

        The input line's channel data is ReFidded to the mask
        channel, and then pruned from the output line data,
        based on the value of the VVU_PRUNE_XXX variable.
        For `VVU_PRUNE_DUMMY`, only those items where the mask channel
        value is not a dummy are retained, while the complement
        is retained for VV_PRUNE_VALID.
        """
        gxapi_cy.WrapDU.copy_line_masked(GXContext._get_tls_geo(), p1._wrapper, p2, p3, p4, p5)
        



    @classmethod
    def dao_table_names(cls, p1, p2, p3):
        """
        Scans a DAO-compliant database and returns the table names in a `GXVV`

        **Note:**

        The `GXVV` must be created to hold strings of length
        `STR_DB_SYMBOL`; i.e. use
        Creat_VV(-`STR_DB_SYMBOL`, 0), or it will assert.
        """
        gxapi_cy.WrapDU.dao_table_names(GXContext._get_tls_geo(), p1.encode(), p2.encode(), p3._wrapper)
        



    @classmethod
    def decimate(cls, p1, p2, p3, p4, p5):
        """
        Copy and decimate a channel
        """
        gxapi_cy.WrapDU.decimate(GXContext._get_tls_geo(), p1._wrapper, p2, p3, p4, p5)
        



    @classmethod
    def diff(cls, p1, p2, p3, p4, p5):
        """
        Calculate differences within a channel.

        **Note:**

        Differences with dummies result in dummies.
        An even number of differences locates data accurately.
        An odd number of differences locates result 1/2 element lower
        in the `GXVV`.
        """
        gxapi_cy.WrapDU.diff(GXContext._get_tls_geo(), p1._wrapper, p2, p3, p4, p5)
        



    @classmethod
    def distance(cls, p1, p2, p3, p4, p5):
        """
        Create a distance channel from X and Y.
        """
        gxapi_cy.WrapDU.distance(GXContext._get_tls_geo(), p1._wrapper, p2, p3, p4, p5)
        



    @classmethod
    def distance_3d(cls, p1, p2, p3, p4, p5, p6, p7):
        """
        Create a distance channel from XY or XYZ with direction options.
        """
        gxapi_cy.WrapDU.distance_3d(GXContext._get_tls_geo(), p1._wrapper, p2, p3, p4, p5, p6, p7)
        



    @classmethod
    def distline(cls, p1, p2, p3, p4, p5):
        """
        Calculate cummulative distance for a line.
        """
        p5.value = gxapi_cy.WrapDU.distline(GXContext._get_tls_geo(), p1._wrapper, p2, p3, p4, p5.value)
        



    @classmethod
    def dup_chan_locks(cls, p1, p2):
        """
        Duplicate all channels protect-info from input `GXDB`.
        """
        gxapi_cy.WrapDU.dup_chan_locks(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper)
        



    @classmethod
    def dup_chans(cls, p1, p2):
        """
        Duplicate all channels from input `GXDB`.
        """
        gxapi_cy.WrapDU.dup_chans(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper)
        



    @classmethod
    def edit_duplicates(cls, p1, p2, p3, p4, p5, p6, p7):
        """
        Edit duplicate readings at individual location

        **Note:**

        All the channels must be of the same fid incr/start and length.
        Protected channels are modified automatically.
        """
        gxapi_cy.WrapDU.edit_duplicates(GXContext._get_tls_geo(), p1._wrapper, p2, p3, p4, p5, p6, p7)
        



    @classmethod
    def export1(cls, p1, p2, p3, p4, p5, p6, p7, p8):
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
        
        The `DU_CHANNELS_DISPLAYED` option can be used to export any selection of
        channels, listed by the symbols (DB_SYMB) values, cast to int values and
        stored in a `GXVV`.
        """
        gxapi_cy.WrapDU.export1(GXContext._get_tls_geo(), p1._wrapper, p2, p3.encode(), p4._wrapper, p5, p6.encode(), p7, p8)
        



    @classmethod
    def export2(cls, p1, p2, p3, p4, p5, p6, p7, p8, p9):
        """
        Like `export1`, but include line names as data.

        **Note:**

        See `export1`.
        The line names are printed as the first column of data exported.
        """
        gxapi_cy.WrapDU.export2(GXContext._get_tls_geo(), p1._wrapper, p2, p3.encode(), p4._wrapper, p5, p6.encode(), p7, p8, p9)
        



    @classmethod
    def export_amira(cls, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11):
        """
        Export to database an AMIRA data file.

        **Note:**

        Other defined FIELDS stored in the database (see `import_amira` function)
        will be automatically included in the export
        """
        gxapi_cy.WrapDU.export_amira(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3.encode(), p4.encode(), p5.encode(), p6.encode(), p7.encode(), p8.encode(), p9.encode(), p10.encode(), p11.encode())
        



    @classmethod
    def export_aseg(cls, p1, p2, p3, p4, p5, p6):
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
        gxapi_cy.WrapDU.export_aseg(GXContext._get_tls_geo(), p1._wrapper, p2.encode(), p3._wrapper, p4, p5.encode(), p6.encode())
        



    @classmethod
    def export_aseg_proj(cls, p1, p2, p3, p4, p5, p6, p7, p8):
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
        gxapi_cy.WrapDU.export_aseg_proj(GXContext._get_tls_geo(), p1._wrapper, p2.encode(), p3._wrapper, p4, p5.encode(), p6.encode(), p7.encode(), p8._wrapper)
        



    @classmethod
    def export_chan_crc(cls, p1, p2, p3, p4):
        """
        Export a channel as XML and compute a CRC value.

        **Note:**

        The output file is an XML describing the channel. The
        CRC is of the channel data ONLY. To compute a CRC of the
        full channel (include metadata) do a CRC of the generated
        file.
        """
        p3.value = gxapi_cy.WrapDU.export_chan_crc(GXContext._get_tls_geo(), p1._wrapper, p2, p3.value, p4.encode())
        



    @classmethod
    def export_csv(cls, p1, p2, p3, p4, p5, p6, p7):
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
        gxapi_cy.WrapDU.export_csv(GXContext._get_tls_geo(), p1._wrapper, p2.encode(), p3._wrapper, p4, p5.encode(), p6, p7)
        



    @classmethod
    def export_database_crc(cls, p1, p2, p3):
        """
        Export a channel as XML and compute a CRC value.

        **Note:**

        The output file is an XML describing the channel. The
        CRC is of the channel data ONLY. To compute a CRC of the
        full channel (include metadata) do a CRC of the generated
        file.
        """
        p2.value = gxapi_cy.WrapDU.export_database_crc(GXContext._get_tls_geo(), p1._wrapper, p2.value, p3.encode())
        



    @classmethod
    def export_gbn(cls, p1, p2, p3):
        """
        Export to a GBN data file.

        **Note:**

        The iDispChanList_DBE or `GXDB.symb_list` methods can be
        used to obtain a list of channels.
        """
        gxapi_cy.WrapDU.export_gbn(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3.encode())
        



    @classmethod
    def export_mdb(cls, p1, p2, p3, p4, p5, p6):
        """
        Export to a Microsoft Access Database (MDB) file.

        **Note:**

        Similar to `export_gbn`, with the addition that
        Groups go to individual tables, and lines go to
        a single table, or individual tables, based on the
        value of `DU_LINEOUT`
        """
        gxapi_cy.WrapDU.export_mdb(GXContext._get_tls_geo(), p1._wrapper, p2.encode(), p3._wrapper, p4, p5, p6.encode())
        



    @classmethod
    def export_geodatabase(cls, p1, p2, p3, p4, p5, p6, p7, p8):
        """
        Export to a ESRI Geodatabase file.

        **Note:**

        Similar to `export_gbn`, with the addition that
        Groups go to individual tables, and lines go to
        a single table, or individual tables, based on the
        value of `DU_LINEOUT`
        """
        gxapi_cy.WrapDU.export_geodatabase(GXContext._get_tls_geo(), p1._wrapper, p2.encode(), p3.encode(), p4._wrapper, p5, p6, p7, p8.encode())
        



    @classmethod
    def get_existing_feature_classes_in_geodatabase(cls, p1, p2, p3, p4):
        """
        Searches the geodatabases for an existing Feature class.

        **Note:**

        Searches the geodatabases for an existing Feature class
        """
        ret_val = gxapi_cy.WrapDU.get_existing_feature_classes_in_geodatabase(GXContext._get_tls_geo(), p1._wrapper, p2.encode(), p3._wrapper, p4._wrapper)
        return ret_val



    @classmethod
    def export_shp(cls, p1, p2, p3, p4, p5, p6, p7):
        """
        Export to a shape file or files.

        **Note:**

        Similar to `export_mdb`, with the addition that groups go to indiviual files
        with group name suffixes, and lines go to a single file, or multiple files
        with line name suffixes, based on the value of `DU_LINEOUT`.
        """
        gxapi_cy.WrapDU.export_shp(GXContext._get_tls_geo(), p1._wrapper, p2.encode(), p3._wrapper, p4, p5, p6.encode(), p7._wrapper)
        



    @classmethod
    def export_xyz(cls, p1, p2, p3):
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
        gxapi_cy.WrapDU.export_xyz(GXContext._get_tls_geo(), p1._wrapper, p2.encode(), p3.encode())
        



    @classmethod
    def export_xyz2(cls, p1, p2, p3):
        """
        Export XYZdata from a database to an XYZ file, using file handles.

        .. seealso::

            `export_xyz`
        """
        gxapi_cy.WrapDU.export_xyz2(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3._wrapper)
        



    @classmethod
    def fft(cls, p1, p2, p3, p4, p5):
        """
        Apply an `GXFFT` to space data.
        """
        gxapi_cy.WrapDU.fft(GXContext._get_tls_geo(), p1._wrapper, p2, p3, p4, p5)
        



    @classmethod
    def filter(cls, p1, p2, p3, p4, p5):
        """
        Apply a convolution filter to a channel.
        """
        gxapi_cy.WrapDU.filter(GXContext._get_tls_geo(), p1._wrapper, p2, p3, p4, p5)
        



    @classmethod
    def gen_lev(cls, p1, p2, p3, p4, p5):
        """
        Generate a Level table from an Intersection Table.
        """
        gxapi_cy.WrapDU.gen_lev(GXContext._get_tls_geo(), p1._wrapper, p2.encode(), p3.encode(), p4, p5)
        



    @classmethod
    def gen_lev_db(cls, p1, p2, p3, p4):
        """
        Generate a Level table from an Intersection Database

        **Note:**

        Requires channels with the following names:
        
        ine, TFid, TZ, TDZ
        Line, LFid, LZ, LDZ
        Mask
        """
        gxapi_cy.WrapDU.gen_lev_db(GXContext._get_tls_geo(), p1._wrapper, p2.encode(), p3, p4)
        



    @classmethod
    def gen_xyz_temp(cls, p1, p2):
        """
        Generate default XYZ template for a XYZ file.
        """
        gxapi_cy.WrapDU.gen_xyz_temp(GXContext._get_tls_geo(), p1.encode(), p2.encode())
        



    @classmethod
    def get_xyz_num_fields(cls, p1, p2):
        """
        Get the number of fields in the XYZ file.
        """
        p2.value = gxapi_cy.WrapDU.get_xyz_num_fields(GXContext._get_tls_geo(), p1.encode(), p2.value)
        



    @classmethod
    def get_chan_data_lst(cls, p1, p2, p3, p4):
        """
        Populate a `GXLST` with unique items in a channel.

        **Note:**

        Items from all selected lines are collected,
        sorted, and duplicates removed. The output
        `GXLST` name and value are set to the item values.
        Non-string channels are converted internally to
        string values using Copy_VV,
        so results may differ from what
        you may expect given the current channel's display
        width and number of decimals.
        If a mask channel is selected, then only those items
        where the mask channel is not a dummy are collected.
        """
        gxapi_cy.WrapDU.get_chan_data_lst(GXContext._get_tls_geo(), p1._wrapper, p2, p3, p4._wrapper)
        



    @classmethod
    def get_chan_data_vv(cls, p1, p2, p3, p4):
        """
        Populate a `GXVV` with unique items in a channel.

        **Note:**

        Items from all selected lines are collected,
        sorted, and duplicates removed.
        The data is collected in the channel's data type,
        so normal `GXVV.sort` rules apply.
        If the output `GXVV` and channel type are not the
        same, then the data is converted using the
        Copy_VV function, so see that for conversion rules.
        If a mask channel is selected, then only those items
        where the mask channel is not a dummy are collected.
        """
        gxapi_cy.WrapDU.get_chan_data_vv(GXContext._get_tls_geo(), p1._wrapper, p2, p3, p4._wrapper)
        



    @classmethod
    def gradient(cls, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11):
        """
        This method takes 4 channels from input database and
        duplicats each line twice to output database)
        (input and Output can be the same channel).
        """
        gxapi_cy.WrapDU.gradient(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3, p4, p5, p6, p7, p8, p9, p10, p11)
        



    @classmethod
    def grav_drift(cls, p1, p2, p3, p4, p5, p6, p7):
        """
        Calculate base loop closure and correct for drift.
        """
        gxapi_cy.WrapDU.grav_drift(GXContext._get_tls_geo(), p1._wrapper, p2, p3, p4, p5, p6, p7)
        



    @classmethod
    def grav_tide(cls, p1, p2, p3, p4, p5, p6, p7, p8):
        """
        Calculate earth tide gravity correction.
        """
        gxapi_cy.WrapDU.grav_tide(GXContext._get_tls_geo(), p1._wrapper, p2, p3, p4, p5, p6, p7, p8)
        



    @classmethod
    def grid_load(cls, p1, p2, p3, p4, p5, p6):
        """
        Load grid data to a database.
        """
        gxapi_cy.WrapDU.grid_load(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3, p4, p5, p6)
        



    @classmethod
    def grid_load_xyz(cls, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10):
        """
        Load grid data to a database using specified channels
        """
        gxapi_cy.WrapDU.grid_load_xyz(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3, p4, p5, p6, p7, p8, p9, p10)
        



    @classmethod
    def head(cls, p1, p2, p3, p4, p5, p6):
        """
        Applies a heading correction.

        **Note:**

        Updates channel with Direction in degrees azimuth (counter-clockwise
        relative the +Y direction).
        `GS_R8DM` if the line has no data, or if there is a
        problem.
        """
        gxapi_cy.WrapDU.head(GXContext._get_tls_geo(), p1._wrapper, p2, p3, p4, p5._wrapper, p6)
        



    @classmethod
    def import_bin3(cls, p1, p2, p3, p4, p6, p7, p8):
        """
        Same as `import_bin2`, but returns the name of the imported line.

        **Note:**

        See `import_bin2`. Because the name of the created line is
        not necessarily the value passed in (and the value passed in
        can be blank), this version returns the name of the line
        to which the data is actually imported.

        .. seealso::

            `import_bin2`
        """
        p4.value = gxapi_cy.WrapDU.import_bin3(GXContext._get_tls_geo(), p1._wrapper, p2.encode(), p3.encode(), p4.value.encode(), p6, p7, p8._wrapper)
        



    @classmethod
    def imp_cb_ply(cls, p1, p2, p3, p4, p5):
        """
        Import concession boundary polygon file into a database

        **Note:**

        The polygon file is provided by Ana Christina in Brasil.
        """
        gxapi_cy.WrapDU.imp_cb_ply(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3.encode(), p4, p5)
        



    @classmethod
    def import_ado(cls, p1, p2, p3, p4, p5):
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
        gxapi_cy.WrapDU.import_ado(GXContext._get_tls_geo(), p1._wrapper, p2.encode(), p3.encode(), p4.encode(), p5.encode())
        



    @classmethod
    def import_all_ado(cls, p1, p2, p3):
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
        gxapi_cy.WrapDU.import_all_ado(GXContext._get_tls_geo(), p1._wrapper, p2.encode(), p3)
        



    @classmethod
    def import_all_dao(cls, p1, p2, p3, p4):
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
        gxapi_cy.WrapDU.import_all_dao(GXContext._get_tls_geo(), p1._wrapper, p2.encode(), p3.encode(), p4)
        



    @classmethod
    def import_amira(cls, p1, p2, p3):
        """
        Import an AMIRA data file.

        **Note:**

        All the constant declarations are stored within the database
        under \\TEM\\CONSTANTS. The format is as follows:
        
            1. Lines stored in the file beginning with "/" are comments
            2. Each constant occupies a line in the file. It uses the format: CONSTANT=VALUE
        """
        gxapi_cy.WrapDU.import_amira(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3._wrapper)
        



    @classmethod
    def import_aseg(cls, p1, p2, p3, p4, p5, p6):
        """
        Import an ASEG-GDF data file.
        """
        gxapi_cy.WrapDU.import_aseg(GXContext._get_tls_geo(), p1._wrapper, p2.encode(), p3.encode(), p4.encode(), p5.encode(), p6)
        



    @classmethod
    def import_aseg_proj(cls, p1, p2, p3, p4, p5, p6, p7, p8, p9):
        """
        Import an ASEG-GDF data file (supports projections).

        **Note:**

        This version supports projections
        """
        gxapi_cy.WrapDU.import_aseg_proj(GXContext._get_tls_geo(), p1._wrapper, p2.encode(), p3.encode(), p4.encode(), p5.encode(), p6, p7.encode(), p8.encode(), p9.encode())
        



    @classmethod
    def import_bin(cls, p1, p2, p3, p4, p5, p6):
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

            `lab_template`
        """
        gxapi_cy.WrapDU.import_bin(GXContext._get_tls_geo(), p1._wrapper, p2.encode(), p3.encode(), p4.encode(), p5, p6)
        



    @classmethod
    def import_bin2(cls, p1, p2, p3, p4, p5, p6, p7):
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

            `lab_template`
        """
        gxapi_cy.WrapDU.import_bin2(GXContext._get_tls_geo(), p1._wrapper, p2.encode(), p3.encode(), p4.encode(), p5, p6, p7._wrapper)
        



    @classmethod
    def import_bin4(cls, p1, p2, p3, p4, p5, p6, p7, p8):
        """
        Same as `import_bin2` but with an import mode

        **Note:**

        Same as `import_bin2` but with an import mode

        .. seealso::

            `import_bin2`
        """
        gxapi_cy.WrapDU.import_bin4(GXContext._get_tls_geo(), p1._wrapper, p2, p3.encode(), p4.encode(), p5.encode(), p6, p7, p8._wrapper)
        



    @classmethod
    def import_daarc500_serial(cls, p1, p2, p3, p4, p5):
        """
        Import Serial data from the RMS Instruments DAARC500.

        **Note:**

        Imports data stored in a serial channel recorded
        by the RMS Instruments DAARC500 instrument, and outputs the data to
        a line in the database. The channels created depend on the input data type
        """
        gxapi_cy.WrapDU.import_daarc500_serial(GXContext._get_tls_geo(), p1._wrapper, p2, p3.encode(), p4, p5)
        



    @classmethod
    def import_daarc500_serial_gps(cls, p1, p2, p3, p4):
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
        gxapi_cy.WrapDU.import_daarc500_serial_gps(GXContext._get_tls_geo(), p1._wrapper, p2, p3.encode(), p4)
        



    @classmethod
    def import_dao(cls, p1, p2, p3, p4, p5, p6):
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
        gxapi_cy.WrapDU.import_dao(GXContext._get_tls_geo(), p1._wrapper, p2.encode(), p3.encode(), p4.encode(), p5.encode(), p6.encode())
        



    @classmethod
    def import_esri(cls, p1, p2, p3, p4):
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
        gxapi_cy.WrapDU.import_esri(GXContext._get_tls_geo(), p1._wrapper, p2.encode(), p3.encode(), p4.encode())
        



    @classmethod
    def import_gbn(cls, p1, p2):
        """
        Import GBN data file.
        """
        gxapi_cy.WrapDU.import_gbn(GXContext._get_tls_geo(), p1._wrapper, p2.encode())
        



    @classmethod
    def import_oddf(cls, p1, p2):
        """
        Import ODDF data file.
        """
        gxapi_cy.WrapDU.import_oddf(GXContext._get_tls_geo(), p1._wrapper, p2.encode())
        



    @classmethod
    def import_pico(cls, p1, p2, p3, p4):
        """
        Import a Picodas data file.
        """
        gxapi_cy.WrapDU.import_pico(GXContext._get_tls_geo(), p1._wrapper, p2.encode(), p3.encode(), p4)
        



    @classmethod
    def import_ubc_mod_msh(cls, p1, p2, p3, p4, p5):
        """
        Import UBC Mod and Msh files.

        **Note:**

        Each slice in X,Y or Z is imported to its own line in the database
        beginning with L0.
        """
        gxapi_cy.WrapDU.import_ubc_mod_msh(GXContext._get_tls_geo(), p1._wrapper, p2.encode(), p3.encode(), p4, p5)
        



    @classmethod
    def import_usgs_post(cls, p1, p2):
        """
        Import USGS Post data file.
        """
        gxapi_cy.WrapDU.import_usgs_post(GXContext._get_tls_geo(), p1._wrapper, p2.encode())
        



    @classmethod
    def import_xyz(cls, p1, p2, p3, p4):
        """
        Import XYZ data into the database.

        **Note:**

        1. The import template can be in the local directory or the GEOSOFT
        directory.  The import data file must include the path if it is not
        in the local directory.
        
        2. Both the import template and data file must exist.
        """
        gxapi_cy.WrapDU.import_xyz(GXContext._get_tls_geo(), p1._wrapper, p2, p3.encode(), p4.encode())
        



    @classmethod
    def import_xyz2(cls, p1, p2, p3, p4, p5):
        """
        Import XYZ data into the database.

        **Note:**

        1. The import template can be in the local directory or the GEOSOFT
        directory.  The import data file must include the path if it is not
        in the local directory.
        
        2. Both the import template and data file must exist.
        """
        gxapi_cy.WrapDU.import_xyz2(GXContext._get_tls_geo(), p1._wrapper, p2, p3.encode(), p4.encode(), p5._wrapper)
        



    @classmethod
    def import_io_gas(cls, p1, p2, p3):
        """
        Import data columns from an ioGAS data file.

        **Note:**

        1. All columns in the speficied ioGAS data file will be imported.
        2. If a line already exists, the data will overwrite the existing data.
        """
        gxapi_cy.WrapDU.import_io_gas(GXContext._get_tls_geo(), p1._wrapper, p2.encode(), p3.encode())
        



    @classmethod
    def index_order(cls, p1, p2, p3, p4):
        """
        Change the order of a channel using an index channel.
        """
        gxapi_cy.WrapDU.index_order(GXContext._get_tls_geo(), p1._wrapper, p2, p3, p4)
        



    @classmethod
    def interp(cls, p1, p2, p3, p4, p5, p6):
        """
        Replace all dummies by interpolating from valid data.
        """
        gxapi_cy.WrapDU.interp(GXContext._get_tls_geo(), p1._wrapper, p2, p3, p4, p5, p6)
        



    @classmethod
    def interp_gap(cls, p1, p2, p3, p4, p5, p6, p7, p8):
        """
        Replace all dummies by interpolating from valid data.
        """
        gxapi_cy.WrapDU.interp_gap(GXContext._get_tls_geo(), p1._wrapper, p2, p3, p4, p5, p6, p7, p8)
        



    @classmethod
    def intersect(cls, p1, p2, p3, p4, p5, p6):
        """
        Create Tie Line & Normal Line intersect table.
        """
        gxapi_cy.WrapDU.intersect(GXContext._get_tls_geo(), p1._wrapper, p2, p3, p4, p5, p6.encode())
        



    @classmethod
    def intersect_all(cls, p1, p2, p3, p4, p5, p6):
        """
        Create line intersect table from all lines.
        """
        gxapi_cy.WrapDU.intersect_all(GXContext._get_tls_geo(), p1._wrapper, p2, p3, p4, p5, p6.encode())
        



    @classmethod
    def intersect_gd_bto_tbl(cls, p1, p2):
        """
        Create a new intersection table from an intersection database.

        **Note:**

        If the TBL exists, it is overwritten.
        """
        gxapi_cy.WrapDU.intersect_gd_bto_tbl(GXContext._get_tls_geo(), p1.encode(), p2.encode())
        



    @classmethod
    def intersect_old(cls, p1, p2, p3, p4, p5, p6):
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
        gxapi_cy.WrapDU.intersect_old(GXContext._get_tls_geo(), p1._wrapper, p2, p3, p4, p5.encode(), p6.encode())
        



    @classmethod
    def intersect_tb_lto_gdb(cls, p1, p2):
        """
        Create a new intersection database from an intersection table.

        **Note:**

        If the GDB exists, it is deleted, so it should not
        be loaded.
        The database is split by Tie lines (or whatever lines are found in column 3
        of the TBL file.
        """
        gxapi_cy.WrapDU.intersect_tb_lto_gdb(GXContext._get_tls_geo(), p1.encode(), p2.encode())
        



    @classmethod
    def lab_template(cls, p1, p2, p3, p4, p5, p6, p7, p8, p9):
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

            `import_bin`
        """
        gxapi_cy.WrapDU.lab_template(GXContext._get_tls_geo(), p1.encode(), p2.encode(), p3, p4.encode(), p5, p6, p7, p8, p9)
        



    @classmethod
    def load_gravity(cls, p1, p2, p3, p4):
        """
        Load a gravity survey file

        **Note:**

        See GRAVITY.`GXDAT` for a description of the file format.
        
        Existing data in the line will be replaced.
        
        The following `GXREG` parameters will be set if they appear
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
        `GXREG` already has the constant defined, it is not changed.
        If the constant is not defined and it is not already in
        the `GXREG`, the indicated default will be set.
        """
        gxapi_cy.WrapDU.load_gravity(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3, p4.encode())
        



    @classmethod
    def load_ltb(cls, p1, p2, p3, p4):
        """
        Load `GXLTB` into a database line.

        **Note:**

        A new channel will be created for all `GXLTB` fields
        that do not already exist.
        The `GXLTB` field type will be double if all entries can be
        converted to double, otherwise it will be a string type
        set to the larger of 16 characters or the longest string
        in the field.
        
        For _APPEND, the `GXLTB` data is simply added the end of each
        channel.  `re_fid_all_ch` can be used to re-fid data to
        match a specifc channel and there-by case all channels to be
        the same length before appending data.
        """
        gxapi_cy.WrapDU.load_ltb(GXContext._get_tls_geo(), p1._wrapper, p2, p3._wrapper, p4)
        



    @classmethod
    def make_fid(cls, p1, p2, p3, p4):
        """
        Make a fiducial channel based on an existing channel.
        """
        gxapi_cy.WrapDU.make_fid(GXContext._get_tls_geo(), p1._wrapper, p2, p3, p4)
        



    @classmethod
    def mask(cls, p1, p2, p3, p4):
        """
        Mask dummies in one channel against another.
        """
        gxapi_cy.WrapDU.mask(GXContext._get_tls_geo(), p1._wrapper, p2, p3, p4)
        



    @classmethod
    def math(cls, p1, p2, p3):
        """
        Apply an expression to the database

        **Note:**

        The MATH_DU method will READWRITE lock channels on the left
        side of expressions and READONLY lock channels on the right
        side of expressions.  Channels are unlocked before returning.
        Therefore, channels on the left side of an expression cannot
        be locked READONLY because the `math` attempt to lock the
        channel READWRITE will fail.  Similarly, channels on the right
        side of an expression cannot be locked READWRITE because
        `math`'s attempt to lock the channels READONLY will fail.
        
        If this is confusing, just make sure no channels used in the
        expression are locked before calling `math`.

        .. seealso::

            `GXEXP`
        """
        gxapi_cy.WrapDU.math(GXContext._get_tls_geo(), p1._wrapper, p2, p3._wrapper)
        



    @classmethod
    def merge_line(cls, p1, p2, p3, p4, p5):
        """
        Merge a line a the fiducial and copies any data past
        that fiducial into the new line.
        """
        gxapi_cy.WrapDU.merge_line(GXContext._get_tls_geo(), p1._wrapper, p2, p3, p4, p5)
        



    @classmethod
    def mod_fid_range(cls, p1, p2, p3, p4, p5, p6, p7):
        """
        Insert/Append/Delete a range of fids.

        **Note:**

        Channels that do not have the same fid start or fid
        increment are not processed.
        
        Protected channels are modified automatically.
        """
        gxapi_cy.WrapDU.mod_fid_range(GXContext._get_tls_geo(), p1._wrapper, p2, p3, p4, p5, p6, p7)
        



    @classmethod
    def move(cls, p1, p2, p3, p4, p5, p6):
        """
        Move/correct a channel to a control channel.

        **Note:**

        The input channel is moved to the absolute location
        of the control channel.
        """
        gxapi_cy.WrapDU.move(GXContext._get_tls_geo(), p1._wrapper, p2, p3, p4, p5, p6)
        



    @classmethod
    def nl_filt(cls, p1, p2, p3, p4, p5, p6):
        """
        This method applies a non-linear filter to the specified
        line/channel and places the output in the output channel.
        """
        gxapi_cy.WrapDU.nl_filt(GXContext._get_tls_geo(), p1._wrapper, p2, p3, p4, p5, p6)
        



    @classmethod
    def normal(cls, p1, p2, p3):
        """
        Set fid of all channels to match a specified channel.

        .. seealso::

            `re_fid_all_ch`
        """
        gxapi_cy.WrapDU.normal(GXContext._get_tls_geo(), p1._wrapper, p2, p3)
        



    @classmethod
    def poly_fill(cls, p1, p2, p3, p4, p5, p6, p7):
        """
        Fill using a polygon with a value of 1.
        """
        gxapi_cy.WrapDU.poly_fill(GXContext._get_tls_geo(), p1._wrapper, p2, p3, p4, p5, p6._wrapper, p7)
        



    @classmethod
    def poly_mask(cls, p1, p2, p3, p4, p5, p6, p7):
        """
        Mask against a polygon.
        """
        gxapi_cy.WrapDU.poly_mask(GXContext._get_tls_geo(), p1._wrapper, p2, p3, p4, p5, p6._wrapper, p7)
        



    @classmethod
    def project_data(cls, p1, p2, p3, p4, p5, p6, p7):
        """
        Project X,Y channels

        **Note:**

        Output channels can be the same as input channels
        """
        gxapi_cy.WrapDU.project_data(GXContext._get_tls_geo(), p1._wrapper, p2, p3, p4, p5, p6, p7._wrapper)
        



    @classmethod
    def project_xyz(cls, p1, p2, p3, p4, p5, p6, p7, p8, p9):
        """
        Project X,Y,Z channels from one system to another.

        **Note:**

        Output channels can be the same as input channels
        """
        gxapi_cy.WrapDU.project_xyz(GXContext._get_tls_geo(), p1._wrapper, p2, p3, p4, p5, p6, p7, p8, p9._wrapper)
        



    @classmethod
    def proj_points(cls, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16, p17, p18, p19, p20):
        """
        Project X,Y(Z) channels with different projections

        **Note:**

        Output channels can be the same as input channels
        """
        gxapi_cy.WrapDU.proj_points(GXContext._get_tls_geo(), p1._wrapper, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16, p17, p18, p19, p20)
        



    @classmethod
    def qc_init_separation(cls, p1, p2, p3):
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
        gxapi_cy.WrapDU.qc_init_separation(GXContext._get_tls_geo(), p1._wrapper, p2, p3)
        



    @classmethod
    def qc_survey_plan(cls, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16, p17, p18):
        """
        Create a database containing proposed survey plan in a `GXPLY`

        **Note:**

        The LINE on which has the reference (X,Y) will have the starting Line number
        The lines on the right hand side of the reference line (while looking
        into azimuth of ref. line) have increasing line numbers. The lines
        on the left hand side have the decreasing line numbers from the starting
        number. Returns an error code or 0 (if successful)
        """
        ret_val = gxapi_cy.WrapDU.qc_survey_plan(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3._wrapper, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16, p17, p18)
        return ret_val



    @classmethod
    def direction(cls, p1, p2, p3, p4):
        """
        Returns the direction of a line.

        **Note:**

        The direction is calculated from the first and last
        non-dummy locations in the X and Y reference channels.
        """
        ret_val = gxapi_cy.WrapDU.direction(GXContext._get_tls_geo(), p1._wrapper, p2, p3, p4)
        return ret_val



    @classmethod
    def re_fid(cls, p1, p2, p3, p4, p5, p6, p7, p8, p9):
        """
        Re-fid a channel based on a reference channel

        **Note:**

        The original channel can be an array channel, in which case
        the columns (up to the number of columns available in the output)
        are individually interpolated. If the number of
        columns in the output channel is more than the input channel,
        the remaining columns are dummied.
        
        This function is fundamentally different in behaviour from `re_fid_ch`.
        The values in the Reference channel in `re_fid` are the "X" locations
        corresponding to the "Y" locations in the "Original Channel". Output
        Channel values are calculated at the new "X" locations specified by
        the Start Fid and the Fid Increment.
        """
        gxapi_cy.WrapDU.re_fid(GXContext._get_tls_geo(), p1._wrapper, p2, p3, p4, p5, p6, p7, p8, p9)
        



    @classmethod
    def re_fid_all_ch(cls, p1, p2, p3):
        """
        Simple re-fid of all channels based on a reference channel

        **Note:**

        Channels can be array channels, in which case
        the columns are individually re-fidded.

        .. seealso::

            `normal`
        """
        gxapi_cy.WrapDU.re_fid_all_ch(GXContext._get_tls_geo(), p1._wrapper, p2, p3)
        



    @classmethod
    def re_fid_ch(cls, p1, p2, p3, p4):
        """
        Simple re-fid of a channel based on a reference channel

        **Note:**

        The original channel can be an array channel, in which case
        the columns are individually re-fidded.
        
        `re_fid_ch` resamples the "Channel to refid" to the "Reference Channel" Fid
        range and increment.
        """
        gxapi_cy.WrapDU.re_fid_ch(GXContext._get_tls_geo(), p1._wrapper, p2, p3, p4)
        



    @classmethod
    def rotate(cls, p1, p2, p3, p4, p5, p6, p7, p8, p9):
        """
        Rotate coordinates.
        """
        gxapi_cy.WrapDU.rotate(GXContext._get_tls_geo(), p1._wrapper, p2, p3, p4, p5, p6, p7, p8, p9)
        



    @classmethod
    def sample_gd(cls, p1, p2, p3, p4, p5, p6):
        """
        Sample a `GXGD` at a specified X and Y.

        **Note:**

        Values in result channel
        """
        gxapi_cy.WrapDU.sample_gd(GXContext._get_tls_geo(), p1._wrapper, p2, p3, p4, p5, p6._wrapper)
        



    @classmethod
    def sample_img(cls, p1, p2, p3, p4, p5, p6):
        """
        Sample a `GXIMG` at a specified X and Y.

        **Note:**

        Values in result channel
        """
        gxapi_cy.WrapDU.sample_img(GXContext._get_tls_geo(), p1._wrapper, p2, p3, p4, p5, p6._wrapper)
        



    @classmethod
    def sample_img_line_lst(cls, p1, p2, p3, p4, p5, p6):
        """
        Sample an `GXIMG` at a specified X and Y, for a `GXLST` of lines.

        **Note:**

        Values in result channel
        """
        gxapi_cy.WrapDU.sample_img_line_lst(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3, p4, p5, p6._wrapper)
        



    @classmethod
    def scan_ado(cls, p1, p2, p3):
        """
        Scans an external ADO database and generates a default template.

        **Note:**

        All the channels are listed
        """
        gxapi_cy.WrapDU.scan_ado(GXContext._get_tls_geo(), p1.encode(), p2.encode(), p3.encode())
        



    @classmethod
    def scan_aseg(cls, p1, p2, p3, p4):
        """
        This method scans an ASEG-GDF file and generates a default
        template listing all the channels and all the ALIAS lines.
        """
        gxapi_cy.WrapDU.scan_aseg(GXContext._get_tls_geo(), p1.encode(), p2.encode(), p3.encode(), p4.encode())
        



    @classmethod
    def scan_dao(cls, p1, p2, p3, p4):
        """
        Scans an external DAO database and generates a default template.

        **Note:**

        All the channels are listed
        """
        gxapi_cy.WrapDU.scan_dao(GXContext._get_tls_geo(), p1.encode(), p2.encode(), p3.encode(), p4.encode())
        



    @classmethod
    def scan_pico(cls, p1, p2):
        """
        This method scans a picodas file and generates a default
        template listing all the channels and all the ALIAS lines.
        """
        gxapi_cy.WrapDU.scan_pico(GXContext._get_tls_geo(), p1.encode(), p2.encode())
        



    @classmethod
    def sort(cls, p1, p2, p3, p4):
        """
        Sort the contents of a channel.
        """
        gxapi_cy.WrapDU.sort(GXContext._get_tls_geo(), p1._wrapper, p2, p3, p4)
        



    @classmethod
    def sort_index(cls, p1, p2, p3, p4, p5):
        """
        Create an ordered index of the contents of a channel.
        """
        gxapi_cy.WrapDU.sort_index(GXContext._get_tls_geo(), p1._wrapper, p2, p3, p4, p5)
        



    @classmethod
    def sort_index2(cls, p1, p2, p3, p4, p5, p6, p7):
        """
        Create an ordered index from two channels
        """
        gxapi_cy.WrapDU.sort_index2(GXContext._get_tls_geo(), p1._wrapper, p2, p3, p4, p5, p6, p7)
        



    @classmethod
    def split_line(cls, p1, p2, p3, p4):
        """
        Splits a line a the fiducial and copies any data past
        that fiducial into the new line.
        """
        gxapi_cy.WrapDU.split_line(GXContext._get_tls_geo(), p1._wrapper, p2, p3, p4)
        



    @classmethod
    def split_line2(cls, p1, p2, p3, p4, p5):
        """
        Splits a line a the fiducial and copies any data past
        that fiducial into the new line.

        **Note:**

        The same as SplitLine, but with an option to reset each line's starting fiducial to zero.
        """
        gxapi_cy.WrapDU.split_line2(GXContext._get_tls_geo(), p1._wrapper, p2, p3, p4, p5)
        



    @classmethod
    def split_line_xy(cls, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10):
        """
        Break up a line based on tolerance of lateral and horizontal distance, with
        options for the output line names.

        **Note:**

        The original line will be deleted.
        """
        p9.value = gxapi_cy.WrapDU.split_line_xy(GXContext._get_tls_geo(), p1._wrapper, p2, p3, p4, p5, p6, p7, p8, p9.value, p10)
        



    @classmethod
    def split_line_xy2(cls, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11):
        """
        Break up a line based on tolerance of lateral and horizontal distance, with
        options for the output line names.

        **Note:**

        The same as SplitLineXY, but with an option to reset each line's starting fiducial to zero.
        """
        p9.value = gxapi_cy.WrapDU.split_line_xy2(GXContext._get_tls_geo(), p1._wrapper, p2, p3, p4, p5, p6, p7, p8, p9.value, p10, p11)
        



    @classmethod
    def split_line_xy3(cls, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12):
        """
        Break up a line based on tolerance of lateral and horizontal distance, with
        options for the output line names.

        **Note:**

        The same as SplitLineXY2, but with the option to maintain line types when outputting sequentially numbered lines.
        """
        p9.value = gxapi_cy.WrapDU.split_line_xy3(GXContext._get_tls_geo(), p1._wrapper, p2, p3, p4, p5, p6, p7, p8, p9.value, p10, p11, p12)
        



    @classmethod
    def split_line_by_direction(cls, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13):
        """
        The line is split when the heading (calculated from the current X and Y channels) changes by more than a specified amount over
        a specified distance. Additional options to discard too-short lines

        **Note:**

        Split a line based on changes in heading.
        """
        p11.value = gxapi_cy.WrapDU.split_line_by_direction(GXContext._get_tls_geo(), p1._wrapper, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11.value, p12, p13)
        



    @classmethod
    def split_line_by_direction2(cls, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14):
        """
        The same as SplitLineByDirection, but with the option to maintain line types when outputting sequentially numbered lines.

        **Note:**

        Split a line based on changes in heading.
        """
        p11.value = gxapi_cy.WrapDU.split_line_by_direction2(GXContext._get_tls_geo(), p1._wrapper, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11.value, p12, p13, p14)
        



    @classmethod
    def stat(cls, p1, p2, p3, p4):
        """
        Add a data channel to a statistics object.

        **Note:**

        If the input channel is a `GXVA` (array) channel, then the columns set using
        `GXDB.set_va_windows`() are used in the statistics; all columns are used by default.

        .. seealso::

            `GXST`
        """
        gxapi_cy.WrapDU.stat(GXContext._get_tls_geo(), p1._wrapper, p2, p3, p4._wrapper)
        



    @classmethod
    def table_line_fid(cls, p1, p2, p3, p4, p5):
        """
        Place a Line/Fid information into a Channel.
        """
        gxapi_cy.WrapDU.table_line_fid(GXContext._get_tls_geo(), p1._wrapper, p2, p3, p4._wrapper, p5)
        



    @classmethod
    def table_selected_lines_fid(cls, p1, p2, p3, p4, p5):
        """
        Place a Line/Fid information into a Channel for the selected lines in the database.
        """
        gxapi_cy.WrapDU.table_selected_lines_fid(GXContext._get_tls_geo(), p1._wrapper, p2, p3, p4._wrapper, p5)
        



    @classmethod
    def time_constant(cls, p1, p2, p3, p4, p5, p6, p7, p8):
        """
        Calculate TEM time constant (Tau)

        **Note:**

        When DU_TIME_LOG option is used, Time channel will be converted
        with logarithmic before calculating time constant.
        Logarthmic conversion is always applied to the response channel.
        """
        gxapi_cy.WrapDU.time_constant(GXContext._get_tls_geo(), p1._wrapper, p2, p3, p4, p5, p6, p7, p8)
        



    @classmethod
    def trend(cls, p1, p2, p3, p4, p5):
        """
        Calculates an n'th order trend of a data channel.

        .. seealso::

            `b_spline`
        """
        gxapi_cy.WrapDU.trend(GXContext._get_tls_geo(), p1._wrapper, p2, p3, p4, p5)
        



    @classmethod
    def update_intersect_db(cls, p1, p2, p3, p4):
        """
        Update the Z and DZ values in an intersection database, using the current database.

        **Note:**

        Updates the TZ, TDZ, LZ and LDZ channels at the intersections,
        using the current flight database.
        """
        gxapi_cy.WrapDU.update_intersect_db(GXContext._get_tls_geo(), p1._wrapper, p2, p3, p4._wrapper)
        



    @classmethod
    def voxel_section(cls, p1, p2, p3, p4, p5, p6, p7, p8, p9):
        """
        Slice a voxel to a grid under a database line.

        **Note:**

        Takes the first and XY locations in a line (using the
        current X and Y channels) and defines a section grid
        as a slice through a voxel file.
        The grid cell sizes can be left as `GS_R8DM`, in which
        case an attempt will be made to match the voxel cell
        size, based on the line azimuth, voxel rotation, etc.
        
        If the slice does NOT intersect the voxel, or if
        there are fewer than 2 valid locations in the line,
        then no grid file is created, but there is no error.
        (This is to simplify creating multiple grids from
        at once, where not all may intersect).
        """
        gxapi_cy.WrapDU.voxel_section(GXContext._get_tls_geo(), p1._wrapper, p2, p3, p4, p5._wrapper, p6.encode(), p7, p8, p9)
        



    @classmethod
    def write_wa(cls, p1, p2, p3, p4):
        """
        Write data to an ASCII file.

        **Note:**

        Channels to be written should be placed in a `GXLST` object.
        
        Channels are written in the order of the list.  Only the
        channel names in the list are used.
        
        Data is formated as in the channel definition and
        channels are separated by a single space character.
        """
        gxapi_cy.WrapDU.write_wa(GXContext._get_tls_geo(), p1._wrapper, p2, p3._wrapper, p4._wrapper)
        



    @classmethod
    def xyz_line(cls, p1, p2, p3, p4, p5, p6):
        """
        Break up a line based on tolerance of lateral distance.

        **Note:**

        The original line will be deleted.
        """
        gxapi_cy.WrapDU.xyz_line(GXContext._get_tls_geo(), p1._wrapper, p2, p3, p4, p5, p6)
        



    @classmethod
    def xyz_line2(cls, p1, p2, p3, p4, p5, p6, p7):
        """
        Break up a line based on tolerance of lateral and horizontal distance.

        **Note:**

        The original line will be deleted.
        """
        gxapi_cy.WrapDU.xyz_line2(GXContext._get_tls_geo(), p1._wrapper, p2, p3, p4, p5, p6, p7)
        



    @classmethod
    def xyz_line3(cls, p1, p2, p3, p4, p5, p6, p7, p8):
        """
        Break up a line based on tolerance of lateral and horizontal distance.

        **Note:**

        The same as XyzLine2, but with an option to reset each line's starting fiducial to zero.
        """
        gxapi_cy.WrapDU.xyz_line3(GXContext._get_tls_geo(), p1._wrapper, p2, p3, p4, p5, p6, p7, p8)
        



    @classmethod
    def z_mask(cls, p1, p2, p3, p4, p5, p6):
        """
        Mask dummies in one channel against another(Z) with the range Zmin/Zmax.
        """
        gxapi_cy.WrapDU.z_mask(GXContext._get_tls_geo(), p1._wrapper, p2, p3, p4, p5, p6)
        



    @classmethod
    def range_xy(cls, p1, p2, p3, p4, p5):
        """
        Find the range of X, and Y in the selected lines.

        **Note:**

        Returns the range in X and Y of the current X and Y channels.
        Returned values are dummy if no valid items are found.
        """
        p2.value, p3.value, p4.value, p5.value = gxapi_cy.WrapDU.range_xy(GXContext._get_tls_geo(), p1._wrapper, p2.value, p3.value, p4.value, p5.value)
        



    @classmethod
    def range_xyz(cls, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11):
        """
        Find the range of X, Y and Z in selected lines.

        **Note:**

        The X, Y and Z channels should be normal (not array) channels.
        Only locations where all values are non-dummy are included in the calculation.
        If no non-dummy values are found, Dummy values are returned.
        """
        p5.value, p6.value, p7.value, p8.value, p9.value, p10.value, p11.value = gxapi_cy.WrapDU.range_xyz(GXContext._get_tls_geo(), p1._wrapper, p2, p3, p4, p5.value, p6.value, p7.value, p8.value, p9.value, p10.value, p11.value)
        



    @classmethod
    def range_xyz_data(cls, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14):
        """
        Find the range of X, Y, Z and Data values in selected lines.

        **Note:**

        The Z and Data channels may be array channels, but both must have
        the same number of columns.
        Only values where all channels are non-dummy (or, for `GXVA` channels,
        where the Z or Data value are defined) are included in the calculation.
        If no non-dummy values are found, Dummy values are returned.
        This function is optimized for cases where Z and Data are array channels
        with many columns (e.g. 32 or more columns).
        """
        p6.value, p7.value, p8.value, p9.value, p10.value, p11.value, p12.value, p13.value, p14.value = gxapi_cy.WrapDU.range_xyz_data(GXContext._get_tls_geo(), p1._wrapper, p2, p3, p4, p5, p6.value, p7.value, p8.value, p9.value, p10.value, p11.value, p12.value, p13.value, p14.value)
        



    @classmethod
    def create_drillhole_parameter_weight_constraint_database(cls, p1, p2, p3, p4):
        """
        Used for weighting inversion models.

        **Note:**

        Control parameters are passed in the `GXREG` (to allow for future expansion without
        the need to modify the wrappers).
        The input drillhole database must contain current X, Y and Z channels.
        Drillhole data should be equally spaced (or nearly so) down the hole.
        Weights are calculated on a circle perpendicular to the hole at each point.
        
        RADIUS - Maximum radius from drillhole to create weighting points (Default = 100).
        INCRMENENT - Grid cell size in weighting circle (Default = 10).
        MINIMUM - the minimum weighting value to apply, at the radius (Default = 0.0001).
        POWER - Exponential power to use in the weighting function (negative of this is used) (Default = 2).
        """
        gxapi_cy.WrapDU.create_drillhole_parameter_weight_constraint_database(GXContext._get_tls_geo(), p1._wrapper, p2, p3._wrapper, p4.encode())
        



    @classmethod
    def calculate_draped_survey_altitude(cls, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12):
        """
        Calculate a draped flight path, enforcing maximum descent and ascent rates.

        **Note:**

        Calculate a draped flight path, enforcing maximum descent and ascent rates. Additional Inputs are the sample distance along the line
        and a topography grid.
        """
        gxapi_cy.WrapDU.calculate_draped_survey_altitude(GXContext._get_tls_geo(), p1._wrapper, p2, p3, p4, p5._wrapper, p6, p7, p8, p9, p10, p11, p12)
        



    @classmethod
    def calculate_draped_survey_altitude2(cls, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14):
        """
        Calculate a draped flight path, enforcing maximum descent and ascent rates.

        **Note:**

        Calculate a draped flight path, enforcing maximum descent and ascent rates.
        Set both a nominal and minimum drape height.
        Additional Inputs are the sample distance along the line
        and a topography grid.
        """
        gxapi_cy.WrapDU.calculate_draped_survey_altitude2(GXContext._get_tls_geo(), p1._wrapper, p2, p3, p4, p5._wrapper, p6, p7, p8, p9, p10, p11, p12, p13, p14)
        



    @classmethod
    def direct_grid_data_to_voxel(cls, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16):
        """
        Create a voxel using direct gridding.

        **Note:**

        The Z and Data channels may be array channels. If they are, the array sizes must match.
        """
        gxapi_cy.WrapDU.direct_grid_data_to_voxel(GXContext._get_tls_geo(), p1._wrapper, p2, p3, p4, p5, p6.encode(), p7, p8, p9, p10, p11, p12, p13, p14, p15, p16)
        



    @classmethod
    def direct_grid_item_counts_to_voxel(cls, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16):
        """
        Create a voxel using direct gridding containing the number of data points in each cell.

        **Note:**

        The Z and Data channels may be array channels. If they are, the array sizes must match.
        """
        gxapi_cy.WrapDU.direct_grid_item_counts_to_voxel(GXContext._get_tls_geo(), p1._wrapper, p2, p3, p4, p5, p6.encode(), p7, p8, p9, p10, p11, p12, p13, p14, p15, p16)
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer