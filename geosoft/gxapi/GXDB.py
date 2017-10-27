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
class GXDB:
    """
    GXDB class.

    The `GXDB <geosoft.gxapi.GXDB>` class is used to create, open and work with databases and database symbols.
    Database symbols are objects inside databases, such as lines, channels and blobs

    **Note:**

    The following defines are not used by any methods but are
    used by GX's:
    
    `DB_ACTIVITY_BLOB <geosoft.gxapi.DB_ACTIVITY_BLOB>`
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._wrapper = None

    def __del__(self):
        self._wrapper = None

    def __init__(self, wrapper=None):
        self._wrapper = wrapper if wrapper else gxapi_cy.WrapDB(GXContext._get_tls_geo(), 0)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of `GXDB`
        
        :returns: A null `GXDB`
        """
        return cls()

    def is_null(self):
        """
        Check if the instance of `GXDB` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of `GXDB`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Channel



    def create_dup(self, file):
        """
        This method makes a brand new database identical to the input
        Database in-size.
        The database is opened in ReadWrite Mode.
        """
        self._wrapper.create_dup(file.encode())
        




    def create_dup_comp(self, file, level):
        """
        This method makes a brand new database identical to the input
        Database in-size except it changes the compression.
        The database is opened in ReadWrite Mode.
        """
        self._wrapper.create_dup_comp(file.encode(), level)
        




    def dup_symb_across(self, dbo, symb):
        """
        Create a new Symbol by duplicating an existing symbol.
        exactly the same type but in output database. The symbol must
        not already exist in the output database.
        """
        ret_val = self._wrapper.dup_symb_across(dbo._wrapper, symb)
        return ret_val




    def easy_maker_symb(self, symb, name, groups):
        """
        Adds a Maker to the database symbol based on current GX
        """
        self._wrapper.easy_maker_symb(symb, name.encode(), groups.encode())
        




    def get_chan_str(self, line, chan, ind, str_val):
        """
        Get individual elements in a channel.

        **Note:**

        These methods are slow and should only be used when
        performance is not an issue.
        """
        str_val.value = self._wrapper.get_chan_str(line, chan, ind, str_val.value.encode())
        




    def get_chan_vv(self, line, chan, vv):
        """
        Place the contents of a channel in a `GXVV <geosoft.gxapi.GXVV>`.

        **Note:**

        If a `GXVA <geosoft.gxapi.GXVA>` channel is specified, then element [0] of this
        `GXVA <geosoft.gxapi.GXVA>` channel is used to populated the `GXVV <geosoft.gxapi.GXVV>`.

        .. seealso::

            `GXVV <geosoft.gxapi.GXVV>` class.
        """
        self._wrapper.get_chan_vv(line, chan, vv._wrapper)
        




    def get_chan_vv_expanded(self, line, chan, vv):
        """
        Read a channel into a `GXVV <geosoft.gxapi.GXVV>`. If the channel is a `GXVA <geosoft.gxapi.GXVA>` channel it is
        treaded as a `GXVV <geosoft.gxapi.GXVV>` channel with multiple values per fid and the FID expation
        is set to the array size.

        **Note:**

        This method is to be used in conjunction with the `GXVV.re_fid_vv <geosoft.gxapi.GXVV.re_fid_vv>` method
        that will honor the FID Expansion setting.

        .. seealso::

            `GXVV <geosoft.gxapi.GXVV>` class.
        """
        self._wrapper.get_chan_vv_expanded(line, chan, vv._wrapper)
        




    def get_ipj(self, ch, ipj):
        """
        Get georeference information in an `GXIPJ <geosoft.gxapi.GXIPJ>`.

        **Note:**

        If the channel does not have an `GXIPJ <geosoft.gxapi.GXIPJ>`, the `GXIPJ <geosoft.gxapi.GXIPJ>` that is
        returned will have an unknown projection.
        """
        self._wrapper.get_ipj(ch, ipj._wrapper)
        




    def get_itr(self, ch, itr):
        """
        Get `GXITR <geosoft.gxapi.GXITR>` for a channel.

        **Note:**

        If a channel does not have an `GXITR <geosoft.gxapi.GXITR>`, `get_itr <geosoft.gxapi.GXDB.get_itr>` will not change
        the passed `GXITR <geosoft.gxapi.GXITR>`.
        Channel must be locked for READONLY or READWRITE.
        """
        self._wrapper.get_itr(ch, itr._wrapper)
        




    def get_reg_symb(self, symb, reg):
        """
        Get a `GXREG <geosoft.gxapi.GXREG>` object from a symbol
        """
        self._wrapper.get_reg_symb(symb, reg._wrapper)
        




    def get_reg_symb_setting(self, symb, name, setting):
        """
        Get a `GXREG <geosoft.gxapi.GXREG>` string setting from a symbol reg

        **Note:**

        The symbol `GXREG <geosoft.gxapi.GXREG>` is used to store a variety of attribute
        about the symbol.  Following a conventionally used entries:
        
        UNITS                   - channel units
        CLASS                   - symbol class name (i.e. "Assay")
        _PJ_ipj                 - projection blob name
        _PJ_x                   - projection coordinate pair
        _PJ_y
        _PJ_name                - projection GXF-style info
        _PJ_ellipsoid
        _PJ_projection
        _PJ_units
        _PJ_datum_transform
        
        This is a convenient but low-performance way to get/set `GXREG <geosoft.gxapi.GXREG>`
        settings.  If performance is an issue, and more than one
        setting is to be Get and or Set, use the `GXREG <geosoft.gxapi.GXREG>` directly.
        """
        setting.value = self._wrapper.get_reg_symb_setting(symb, name.encode(), setting.value.encode())
        




    def get_va_chan_vv(self, line, chan, vv, offset, items):
        """
        Place the contents of a specific part of a channel in a `GXVV <geosoft.gxapi.GXVV>`.

        **Note:**

        If a `GXVA <geosoft.gxapi.GXVA>` channel is specified, then element [0] of this
        `GXVA <geosoft.gxapi.GXVA>` channel is used to populated the `GXVV <geosoft.gxapi.GXVV>`.

        .. seealso::

            `GXVV <geosoft.gxapi.GXVV>` class.
        """
        self._wrapper.get_va_chan_vv(line, chan, vv._wrapper, offset, items)
        




    def blobs_max(self):
        """
        Gets Maximum Number of Blobs in the Database
        """
        ret_val = self._wrapper.blobs_max()
        return ret_val




    def chans_max(self):
        """
        Gets Maximum Number of Channels in the Database
        """
        ret_val = self._wrapper.chans_max()
        return ret_val




    def format_chan(self, chan, val, str_val):
        """
        Format a real value based on a channel format.

        **Note:**

        If the passed string is too short, the result will be
        "**".
        """
        str_val.value = self._wrapper.format_chan(chan, val, str_val.value.encode())
        




    def get_chan_array_size(self, chan):
        """
        This method Gets a channel's array size for a
        given channel handle.
        """
        ret_val = self._wrapper.get_chan_array_size(chan)
        return ret_val




    def get_chan_class(self, chan, cl):
        """
        This method gets a channel's label

        **Note:**

        The channel label is stored in the "CLASS" parameter
        of the channel reg. If no class is defined, then an
        empty string is returned.
        The channel must be locked `DB_LOCK_READONLY <geosoft.gxapi.DB_LOCK_READONLY>` or `DB_LOCK_READWRITE <geosoft.gxapi.DB_LOCK_READWRITE>`
        """
        cl.value = self._wrapper.get_chan_class(chan, cl.value.encode())
        




    def get_chan_decimal(self, chan):
        """
        This method gets a channel's number of digits displayed
        to the right of the decimal point.

        **Note:**

        The channel must be locked `DB_LOCK_READONLY <geosoft.gxapi.DB_LOCK_READONLY>` or `DB_LOCK_READWRITE <geosoft.gxapi.DB_LOCK_READWRITE>`
        """
        ret_val = self._wrapper.get_chan_decimal(chan)
        return ret_val




    def get_chan_format(self, chan):
        """
        This method Gets a channel's display format for a
        given channel handle.

        **Note:**

        The returned format is one of the `DB_CHAN_FORMAT_`.
        The channel must be locked `DB_LOCK_READONLY <geosoft.gxapi.DB_LOCK_READONLY>` or `DB_LOCK_READWRITE <geosoft.gxapi.DB_LOCK_READWRITE>`
        """
        ret_val = self._wrapper.get_chan_format(chan)
        return ret_val




    def get_chan_int(self, line, chan, ind):
        """
        Get individual elements in a channel.

        **Note:**

        These methods are slow and should only be used when
        performance is not an issue.
        """
        ret_val = self._wrapper.get_chan_int(line, chan, ind)
        return ret_val




    def get_chan_label(self, chan, label):
        """
        This method gets a channel's label

        **Note:**

        The channel label is stored in the "LABEL" parameter
        of the channel reg.  If the setting is empty, the
        channel name is returned.
        The channel must be locked `DB_LOCK_READONLY <geosoft.gxapi.DB_LOCK_READONLY>` or `DB_LOCK_READWRITE <geosoft.gxapi.DB_LOCK_READWRITE>`
        """
        label.value = self._wrapper.get_chan_label(chan, label.value.encode())
        




    def get_chan_name(self, chan, name):
        """
        This method Gets a channel's name for a
        given channel handle.

        **Note:**

        The channel must be locked `DB_LOCK_READONLY <geosoft.gxapi.DB_LOCK_READONLY>` or `DB_LOCK_READWRITE <geosoft.gxapi.DB_LOCK_READWRITE>`
        """
        name.value = self._wrapper.get_chan_name(chan, name.value.encode())
        




    def get_chan_protect(self, chan):
        """
        This method gets a channel's read-only protection status.

        **Note:**

        The channel must be locked `DB_LOCK_READONLY <geosoft.gxapi.DB_LOCK_READONLY>` or `DB_LOCK_READWRITE <geosoft.gxapi.DB_LOCK_READWRITE>`
        """
        ret_val = self._wrapper.get_chan_protect(chan)
        return ret_val




    def get_chan_type(self, chan):
        """
        This method Gets a channel's type for a
        given channel handle.

        **Note:**

        The type returned is one of the `DB_CATEGORY_CHAN_`.
        Use the GS_SIMPLE_TYPE() macro to convert to INT,REAL
        or string types.
        The channel must be locked `DB_LOCK_READONLY <geosoft.gxapi.DB_LOCK_READONLY>` or `DB_LOCK_READWRITE <geosoft.gxapi.DB_LOCK_READWRITE>`
        """
        ret_val = self._wrapper.get_chan_type(chan)
        return ret_val




    def get_chan_unit(self, chan, unit):
        """
        This method Gets a channel's unit

        **Note:**

        The unit label is stored in the "UNITS" parameter
        of the channel reg.
        The channel must be locked `DB_LOCK_READONLY <geosoft.gxapi.DB_LOCK_READONLY>` or `DB_LOCK_READWRITE <geosoft.gxapi.DB_LOCK_READWRITE>`
        """
        unit.value = self._wrapper.get_chan_unit(chan, unit.value.encode())
        




    def get_chan_width(self, chan):
        """
        This method gets a channel's display width for a
        given channel handle.

        **Note:**

        The channel must be locked `DB_LOCK_READONLY <geosoft.gxapi.DB_LOCK_READONLY>` or `DB_LOCK_READWRITE <geosoft.gxapi.DB_LOCK_READWRITE>`
        """
        ret_val = self._wrapper.get_chan_width(chan)
        return ret_val




    def get_name(self, name, psz_name):
        """
        Gets a name from the database.
        """
        psz_name.value = self._wrapper.get_name(name, psz_name.value.encode())
        




    def get_reg_symb_setting_int(self, symb, name):
        """
        Get an integer-valued `GXREG <geosoft.gxapi.GXREG>` setting from a symbol reg

        **Note:**

        Same as `get_reg_symb_setting <geosoft.gxapi.GXDB.get_reg_symb_setting>`, but converts
        the setting automatically to an integer value.
        
        This is a convenient but low-performance way to get/set `GXREG <geosoft.gxapi.GXREG>`
        settings.  If performance is an issue, and more than one
        setting is to be Get and or Set, use the `GXREG <geosoft.gxapi.GXREG>` directly.
        """
        ret_val = self._wrapper.get_reg_symb_setting_int(symb, name.encode())
        return ret_val




    def get_symb_name(self, symb, name):
        """
        This method gets a symbol's name

        **Note:**

        See GetChanName_DB for more information
        The channel must be locked `DB_LOCK_READONLY <geosoft.gxapi.DB_LOCK_READONLY>` or `DB_LOCK_READWRITE <geosoft.gxapi.DB_LOCK_READWRITE>`
        """
        name.value = self._wrapper.get_symb_name(symb, name.value.encode())
        




    def have_itr(self, ch):
        """
        Returns TRUE if channel has an `GXITR <geosoft.gxapi.GXITR>`.

        **Note:**

        If a channel has an `GXITR <geosoft.gxapi.GXITR>`, the `GXITR <geosoft.gxapi.GXITR>` colors are used to
        display channel values in the spreadsheet.
        
        If a channel does not have an `GXITR <geosoft.gxapi.GXITR>`, `get_itr <geosoft.gxapi.GXDB.get_itr>` will not change
        the passed `GXITR <geosoft.gxapi.GXITR>`.
        """
        ret_val = self._wrapper.have_itr(ch)
        return ret_val




    def coord_pair(self, chan, pair):
        """
        Get the matching coordinate pair of a channel.

        **Note:**

        If the channel does not have a matching coordinate
        pair, or of the channel does not exist, the returned
        string will be empty.
        """
        ret_val, pair.value = self._wrapper.coord_pair(chan.encode(), pair.value.encode())
        return ret_val




    def lines_max(self):
        """
        Gets Maximum number of lines in the database
        """
        ret_val = self._wrapper.lines_max()
        return ret_val




    def users_max(self):
        """
        Gets Maximum number of Users
        """
        ret_val = self._wrapper.users_max()
        return ret_val




    def maker_symb(self, symb, prog, name, groups):
        """
        Adds a Maker to the database symbol
        """
        self._wrapper.maker_symb(symb, prog.encode(), name.encode(), groups.encode())
        




    def put_chan_vv(self, line, chan, vv):
        """
        Place the contents of a `GXVV <geosoft.gxapi.GXVV>` in a channel.

        **Note:**

        If a `GXVA <geosoft.gxapi.GXVA>` channel is specified, then element [0] of this
        `GXVA <geosoft.gxapi.GXVA>` channel will be populated with the `GXVV <geosoft.gxapi.GXVV>`.
        
        There is a limit of 2000 elements for non-licensed users.

        .. seealso::

            `GXVV <geosoft.gxapi.GXVV>` class.
        """
        self._wrapper.put_chan_vv(line, chan, vv._wrapper)
        




    def put_va_chan_vv(self, line, chan, vv, offset, items):
        """
        Place the contents of a `GXVV <geosoft.gxapi.GXVV>` at a specific part of a channel.

        **Note:**

        If a `GXVA <geosoft.gxapi.GXVA>` channel is specified, then element [0] of this
        `GXVA <geosoft.gxapi.GXVA>` channel will be populated with the `GXVV <geosoft.gxapi.GXVV>`.

        .. seealso::

            `GXVV <geosoft.gxapi.GXVV>` class.
        """
        self._wrapper.put_va_chan_vv(line, chan, vv._wrapper, offset, items)
        




    def read_blob_bf(self, symb, bf):
        """
        Read a blob from a database into a file.
        """
        self._wrapper.read_blob_bf(symb, bf._wrapper)
        




    def get_chan_double(self, line, chan, ind):
        """
        Get individual elements in a channel.

        **Note:**

        These methods are slow and should only be used when
        performance is not an issue.
        """
        ret_val = self._wrapper.get_chan_double(line, chan, ind)
        return ret_val




    def get_reg_symb_setting_double(self, symb, name):
        """
        Get a real-valued `GXREG <geosoft.gxapi.GXREG>` setting from a symbol reg

        **Note:**

        Same as `get_reg_symb_setting <geosoft.gxapi.GXDB.get_reg_symb_setting>`, but converts
        the setting automatically to a real value.
        
        This is a convenient but low-performance way to get/set `GXREG <geosoft.gxapi.GXREG>`
        settings.  If performance is an issue, and more than one
        setting is to be Get and or Set, use the `GXREG <geosoft.gxapi.GXREG>` directly.
        """
        ret_val = self._wrapper.get_reg_symb_setting_double(symb, name.encode())
        return ret_val




    def set_all_chan_protect(self, prot):
        """
        This method sets all the channels' read-only protection status.

        **Note:**

        Value to set must be either `DB_CHAN_PROTECTED <geosoft.gxapi.DB_CHAN_PROTECTED>` or
        `DB_CHAN_UNPROTECTED <geosoft.gxapi.DB_CHAN_UNPROTECTED>`
        This method does its own channel locking/unlocking.
        Channels already lock `DB_LOCK_READONLY <geosoft.gxapi.DB_LOCK_READONLY>` are ignored.
        """
        self._wrapper.set_all_chan_protect(prot)
        




    def set_chan_class(self, chan, cl):
        """
        Set a channel class

        **Note:**

        The channel class is stored in the "CLASS" parameter
        of the channel reg.
        The channel must be locked `DB_LOCK_READWRITE <geosoft.gxapi.DB_LOCK_READWRITE>`
        """
        self._wrapper.set_chan_class(chan, cl.encode())
        




    def set_chan_decimal(self, chan, dec):
        """
        This method sets a channel's number of digits displayed
        to the right of the decimal point.

        **Note:**

        The number of display digits must be from 0 to 50.
        The channel must be locked `DB_LOCK_READWRITE <geosoft.gxapi.DB_LOCK_READWRITE>`
        """
        self._wrapper.set_chan_decimal(chan, dec)
        




    def set_chan_format(self, chan, format):
        """
        This method sets a channel's display format.

        **Note:**

        The channel must be locked `DB_LOCK_READWRITE <geosoft.gxapi.DB_LOCK_READWRITE>`
        """
        self._wrapper.set_chan_format(chan, format)
        




    def set_chan_int(self, line, chan, ind, val):
        """
        Set individual elements in a channel.

        **Note:**

        These methods are slow and should only be used when
        performance is not an issue.
        """
        self._wrapper.set_chan_int(line, chan, ind, val)
        




    def set_chan_label(self, chan, label):
        """
        Set a channel label

        **Note:**

        The channel label is stored in the "LABEL" parameter
        of the channel reg.
        The channel must be locked `DB_LOCK_READWRITE <geosoft.gxapi.DB_LOCK_READWRITE>`
        """
        self._wrapper.set_chan_label(chan, label.encode())
        




    def set_chan_name(self, chan, name):
        """
        This method sets a channel's name.

        **Note:**

        The channel must be locked `DB_LOCK_READWRITE <geosoft.gxapi.DB_LOCK_READWRITE>`
        """
        self._wrapper.set_chan_name(chan, name.encode())
        




    def set_chan_protect(self, chan, prot):
        """
        This method sets a channel's read-only protection
        status.

        **Note:**

        Value to set must be either `DB_CHAN_PROTECTED <geosoft.gxapi.DB_CHAN_PROTECTED>` or
        `DB_CHAN_UNPROTECTED <geosoft.gxapi.DB_CHAN_UNPROTECTED>`
        The channel must be locked `DB_LOCK_READWRITE <geosoft.gxapi.DB_LOCK_READWRITE>`
        """
        self._wrapper.set_chan_protect(chan, prot)
        




    def set_chan_double(self, line, chan, ind, val):
        """
        Set individual elements in a channel.

        **Note:**

        These methods are slow and should only be used when
        performance is not an issue.
        """
        self._wrapper.set_chan_double(line, chan, ind, val)
        




    def set_chan_str(self, line, chan, ind, str_val):
        """
        Set individual elements in a channel.

        **Note:**

        These methods are slow and should only be used when
        performance is not an issue.
        """
        self._wrapper.set_chan_str(line, chan, ind, str_val.encode())
        




    def set_chan_unit(self, chan, unit):
        """
        This method sets a channel's unit for a
        given channel handle.

        **Note:**

        The channel must be locked `DB_LOCK_READWRITE <geosoft.gxapi.DB_LOCK_READWRITE>`
        """
        self._wrapper.set_chan_unit(chan, unit.encode())
        




    def set_chan_width(self, chan, width):
        """
        This method sets a channel's display width

        **Note:**

        The number of display digits must be from 0 to 50.
        The channel must be locked `DB_LOCK_READWRITE <geosoft.gxapi.DB_LOCK_READWRITE>`
        """
        self._wrapper.set_chan_width(chan, width)
        




    def set_ipj(self, ch1, ch2, ipj):
        """
        Set a `GXREG <geosoft.gxapi.GXREG>` object into a symbol
        """
        self._wrapper.set_ipj(ch1, ch2, ipj._wrapper)
        




    def set_itr(self, ch, itr):
        """
        Set `GXITR <geosoft.gxapi.GXITR>` for a channel.

        **Note:**

        Use `ITR_NULL <geosoft.gxapi.ITR_NULL>` to clear the channel `GXITR <geosoft.gxapi.GXITR>`.
        Channel must be locked for READONLY or READWRITE.
        """
        self._wrapper.set_itr(ch, itr._wrapper)
        




    def set_reg_symb(self, symb, reg):
        """
        Set a `GXREG <geosoft.gxapi.GXREG>` object into a symbol
        """
        self._wrapper.set_reg_symb(symb, reg._wrapper)
        




    def set_reg_symb_setting(self, symb, name, setting):
        """
        Set a `GXREG <geosoft.gxapi.GXREG>` string setting in a symbol reg

        **Note:**

        The symbol `GXREG <geosoft.gxapi.GXREG>` is used to store a variety of attribute
        about the symbol.  Following a conventionally used entries:
        
        UNITS                   - channel units
        CLASS                   - symbol class name (i.e. "Assay")
        _PJ_ipj                 - projection blob name
        _PJ_x                   - projection coordinate pair
        _PJ_y
        _PJ_name                - projection GXF-style info
        _PJ_ellipsoid
        _PJ_projection
        _PJ_units
        _PJ_datum_transform
        
        This is a convenient but low-performance way to get/set `GXREG <geosoft.gxapi.GXREG>`
        settings.  If performance is an issue, and more than one
        setting is to be Get and or Set, use the `GXREG <geosoft.gxapi.GXREG>` directly.
        """
        self._wrapper.set_reg_symb_setting(symb, name.encode(), setting.encode())
        




    def write_blob_bf(self, symb, bf):
        """
        Write a blob from a file into a database.
        """
        self._wrapper.write_blob_bf(symb, bf._wrapper)
        




# Control



    def commit(self):
        """
        This method forces all changes to the database to be saved.
        """
        self._wrapper.commit()
        




    def compact(self):
        """
        Removes any extra space from the database. This will
        reduce the database to its smallest size.
        """
        self._wrapper.compact()
        



    @classmethod
    def create(cls, file, lines, chans, blobs, users, cache, super, password):
        """
        This method makes a brand new database of the specified size.
        The database is opened in ReadWrite Mode.
        """
        gxapi_cy.WrapDB.create(GXContext._get_tls_geo(), file.encode(), lines, chans, blobs, users, cache, super.encode(), password.encode())
        



    @classmethod
    def create_comp(cls, file, lines, chans, blobs, users, cache, super, password, page, level):
        """
        This method makes a brand new database of the specified size.
        The database is opened in ReadWrite Mode. Also allows you to
        set paging size and the Compression Level.
        """
        gxapi_cy.WrapDB.create_comp(GXContext._get_tls_geo(), file.encode(), lines, chans, blobs, users, cache, super.encode(), password.encode(), page, level)
        



    @classmethod
    def create_ex(cls, file, lines, chans, blobs, users, cache, super, password, page):
        """
        This method makes a brand new database of the specified size.
        The database is opened in ReadWrite Mode. Also allows you to
        set paging size.
        """
        gxapi_cy.WrapDB.create_ex(GXContext._get_tls_geo(), file.encode(), lines, chans, blobs, users, cache, super.encode(), password.encode(), page)
        




    def del_line0(self):
        """
        Delete Empty Line 0.

        **Note:**

        A new database is created with a single, empty line L0, but many processes
        create databases then create their own lines, so the empty line L0 may remain
        after the process finishes. This function will delete a line L0
        a) If it exists and is empty
        b) It is not the only line in the database.

        .. seealso::

            `GXEDB.del_line0 <geosoft.gxapi.GXEDB.del_line0>` - deletes an empty line 0 from the currently edited database.
        """
        self._wrapper.del_line0()
        






    def discard(self):
        """
        This method discards all changes made to the database since
        the last commit or opening.
        """
        self._wrapper.discard()
        



    @classmethod
    def grow(cls, file, lines, chans, blobs, users, cache):
        """
        Enlarges the database.
        """
        gxapi_cy.WrapDB.grow(GXContext._get_tls_geo(), file.encode(), lines, chans, blobs, users, cache)
        



    @classmethod
    def can_open(cls, file, user, password):
        """
        This method checks whether it is possible to open a database.

        **Note:**

        This method is useful to determine if another session already locked a database.
        By using this method before an `open <geosoft.gxapi.GXDB.open>` a GX may handle errors like this more gracefully.

        .. seealso::

            `open <geosoft.gxapi.GXDB.open>`, `open_read_only <geosoft.gxapi.GXDB.open_read_only>`, `can_open_read_only <geosoft.gxapi.GXDB.can_open_read_only>`
        """
        ret_val = gxapi_cy.WrapDB.can_open(GXContext._get_tls_geo(), file.encode(), user.encode(), password.encode())
        return ret_val



    @classmethod
    def can_open_read_only(cls, file, user, password):
        """
        This method checks whether it is possible to open a database in read-only mode.

        **Note:**

        This method is useful to determine if another session already locked a database.
        By using this method before an `open_read_only <geosoft.gxapi.GXDB.open_read_only>` a GX may handle errors like this more gracefully.

        .. seealso::

            `open <geosoft.gxapi.GXDB.open>`, `open_read_only <geosoft.gxapi.GXDB.open_read_only>`, `can_open <geosoft.gxapi.GXDB.can_open>`
        """
        ret_val = gxapi_cy.WrapDB.can_open_read_only(GXContext._get_tls_geo(), file.encode(), user.encode(), password.encode())
        return ret_val




    def check(self):
        """
        Does an integrity check of the data in the database to
        ensure it is valid.
        """
        ret_val = self._wrapper.check()
        return ret_val




    def is_empty(self):
        """
        See if a database contains only empty lines.

        **Note:**

        This function does not check for other information or blobs,
        it merely looks at all lines in the database to see if they
        are empty. If all are empty, it returns 1.
        """
        ret_val = self._wrapper.is_empty()
        return ret_val




    def is_line_empty(self, symb):
        """
        See if a specific line in the database is empty.
        """
        ret_val = self._wrapper.is_line_empty(symb)
        return ret_val



    @classmethod
    def open(cls, file, user, password):
        """
        This method opens a database.

        .. seealso::

            `open_read_only <geosoft.gxapi.GXDB.open_read_only>`, `can_open <geosoft.gxapi.GXDB.can_open>`, `can_open_read_only <geosoft.gxapi.GXDB.can_open_read_only>`
        """
        ret_val = gxapi_cy.WrapDB.open(GXContext._get_tls_geo(), file.encode(), user.encode(), password.encode())
        return GXDB(ret_val)



    @classmethod
    def open_read_only(cls, file, user, password):
        """
        This method opens a database.

        **Note:**

        This method is useful to open multiple reader instances on the same database. This call will fail
        if a `GXDB <geosoft.gxapi.GXDB>` has already been opened with `open <geosoft.gxapi.GXDB.open>` or locked in the application with `GXEDB.lock <geosoft.gxapi.GXEDB.lock>`.

        .. seealso::

            `open <geosoft.gxapi.GXDB.open>`, `can_open <geosoft.gxapi.GXDB.can_open>`, `can_open_read_only <geosoft.gxapi.GXDB.can_open_read_only>`
        """
        ret_val = gxapi_cy.WrapDB.open_read_only(GXContext._get_tls_geo(), file.encode(), user.encode(), password.encode())
        return GXDB(ret_val)



    @classmethod
    def repair(cls, file):
        """
        Cleans the database by removing invalid blocks
        """
        gxapi_cy.WrapDB.repair(GXContext._get_tls_geo(), file.encode())
        




    def sync(self):
        """
        Syncronize the Metadata from this database to the XML
        """
        self._wrapper.sync()
        




# Data



    def copy_data(self, line, i_chan, o_chan):
        """
        This method copies the data from one channel to another on
        on the specified line. The data is converted if such
        conversion in neccessary.

        **Note:**

        All the data in the destination channel is destroyed along
        with the fiducial start and increment.
        """
        self._wrapper.copy_data(line, i_chan, o_chan)
        




    def get_col_va(self, chan):
        """
        Returns the # of columns in a `GXVA <geosoft.gxapi.GXVA>` channel.

        **Note:**

        If the channel is `GXVV <geosoft.gxapi.GXVV>`, this function returns 1.
        """
        ret_val = self._wrapper.get_col_va(chan)
        return ret_val




    def get_channel_length(self, line, chan):
        """
        Returns the # of elements in a channel.

        **Note:**

        Returns the actual number of data items (rows) in a channel. For `GXVA <geosoft.gxapi.GXVA>` channels no correction is
        necessary for the number of columns.
        """
        ret_val = self._wrapper.get_channel_length(line, chan)
        return ret_val




    def get_fid_incr(self, line, chan):
        """
        This method returns the fiducial increment value of a
        specified Channel.
        """
        ret_val = self._wrapper.get_fid_incr(line, chan)
        return ret_val




    def get_fid_start(self, line, chan):
        """
        This method returns the fiducial start value of a
        specified Channel.
        """
        ret_val = self._wrapper.get_fid_start(line, chan)
        return ret_val




    def set_fid(self, line, chan, start, incr):
        """
        This method allows the user to set the fiducial start and
        increment of a channel. The Increment should never be 0.
        """
        self._wrapper.set_fid(line, chan, start, incr)
        




    def window_va_ch(self, line, i_ch, o_ch, col_s, col_e):
        """
        Copy a window of data in a channel into a new channel

        **Note:**

        This function normally used for `GXVA <geosoft.gxapi.GXVA>` channels. A copy of the
        original channel will be made if start and end column
        numbers to copy are dummies.
        All the columns including start and end columns will be copied
        """
        self._wrapper.window_va_ch(line, i_ch, o_ch, col_s, col_e)
        




    def window_va_ch2(self, line, i_ch, o_ch, gvv):
        """
        Copy a windowed version of data in a channel into a new channel

        **Note:**

        Similar to `window_va_ch <geosoft.gxapi.GXDB.window_va_ch>`, but the input and output channels must
        contain the same number of columns. The input `GXVV <geosoft.gxapi.GXVV>` tells which columns
        to copy over; 0 values indicate that the output column is to be
        dummied, and non-zero values indicate the column is to be copied.
        The `GXVV <geosoft.gxapi.GXVV>` length must be the same as the number of columns.
        """
        self._wrapper.window_va_ch2(line, i_ch, o_ch, gvv._wrapper)
        




# Line



    def set_line_selection(self, line, mode):
        """
        Set the selection status for a line.
        """
        self._wrapper.set_line_selection(line, mode)
        




    def get_line_selection(self, line):
        """
        Get the selection status for a line.
        """
        ret_val = self._wrapper.get_line_selection(line)
        return ret_val




    def first_sel_line(self):
        """
        This method will return a handle to the first selected
        line in the database.
        """
        ret_val = self._wrapper.first_sel_line()
        return ret_val




    def get_line_map_fid(self, line, start, end):
        """
        This method gets a line map clip fiducial.

        **Note:**

        The channel must be locked `DB_LOCK_READONLY <geosoft.gxapi.DB_LOCK_READONLY>` or `DB_LOCK_READWRITE <geosoft.gxapi.DB_LOCK_READWRITE>`
        """
        start.value, end.value = self._wrapper.get_line_map_fid(line, start.value, end.value)
        




    def get_select(self):
        """
        Gets the Line Selections.
        """
        ret_val = self._wrapper.get_select()
        return ret_val




    def count_sel_lines(self):
        """
        This method counts the number of selected lines in
        the database.
        """
        ret_val = self._wrapper.count_sel_lines()
        return ret_val



    @classmethod
    def is_chan_name(cls, chan):
        """
        Is this a valid channel name?

        **Note:**

        Channel names must only contain alpha-numeric characters or the
        underscore character "_", and the first letter must be a letter
        or an underscore.
        """
        ret_val = gxapi_cy.WrapDB.is_chan_name(GXContext._get_tls_geo(), chan.encode())
        return ret_val




    def is_chan_valid(self, chan):
        """
        This method checks to see if the channel handle is a
        valid channel.
        """
        ret_val = self._wrapper.is_chan_valid(chan)
        return ret_val



    @classmethod
    def is_line_name(cls, line):
        """
        Is this a valid line name.
        """
        ret_val = gxapi_cy.WrapDB.is_line_name(GXContext._get_tls_geo(), line.encode())
        return ret_val




    def is_line_valid(self, line):
        """
        This method checks to see if the line handle returned by
        the Line methods is a valid line.
        """
        ret_val = self._wrapper.is_line_valid(line)
        return ret_val




    def line_category(self, line):
        """
        This method returns the category (group, line) of a line.

        **Note:**

        The channel must be locked `DB_LOCK_READONLY <geosoft.gxapi.DB_LOCK_READONLY>` or `DB_LOCK_READWRITE <geosoft.gxapi.DB_LOCK_READWRITE>`
        """
        ret_val = self._wrapper.line_category(line)
        return ret_val




    def line_flight(self, line):
        """
        This method returns the flight number of a line.

        **Note:**

        The channel must be locked `DB_LOCK_READONLY <geosoft.gxapi.DB_LOCK_READONLY>` or `DB_LOCK_READWRITE <geosoft.gxapi.DB_LOCK_READWRITE>`
        """
        ret_val = self._wrapper.line_flight(line)
        return ret_val




    def line_label(self, line, label, format):
        """
        Create a line label

        **Note:**

        Label formats.
        
        example full format is
        "L1023.4 13"   type "L"
        number "1023"
        version "4"
        flight "13"
        
        formats can be added to get combined format
        
        Use LINK format to create a database link label.
        """
        label.value = self._wrapper.line_label(line, label.value.encode(), format)
        




    def line_number(self, line):
        """
        This method returns the number of a line.

        **Note:**

        The channel must be locked `DB_LOCK_READONLY <geosoft.gxapi.DB_LOCK_READONLY>` or `DB_LOCK_READWRITE <geosoft.gxapi.DB_LOCK_READWRITE>`
        """
        ret_val = self._wrapper.line_number(line)
        return ret_val




    def line_number2(self, line, line_number):
        """
        Returns the string form of the line number (can be alphanumeric)

        **Note:**

        The channel must be locked `DB_LOCK_READONLY <geosoft.gxapi.DB_LOCK_READONLY>` or `DB_LOCK_READWRITE <geosoft.gxapi.DB_LOCK_READWRITE>`
        """
        line_number.value = self._wrapper.line_number2(line, line_number.value.encode())
        




    def line_type(self, line):
        """
        This method returns the type of a line.

        **Note:**

        The channel must be locked `DB_LOCK_READONLY <geosoft.gxapi.DB_LOCK_READONLY>` or `DB_LOCK_READWRITE <geosoft.gxapi.DB_LOCK_READWRITE>`
        """
        ret_val = self._wrapper.line_type(line)
        return ret_val




    def line_version(self, line):
        """
        This method returns the version number of a line.

        **Note:**

        The channel must be locked `DB_LOCK_READONLY <geosoft.gxapi.DB_LOCK_READONLY>` or `DB_LOCK_READWRITE <geosoft.gxapi.DB_LOCK_READWRITE>`
        """
        ret_val = self._wrapper.line_version(line)
        return ret_val



    @classmethod
    def set_line_name(cls, num, type, ver, name):
        """
        This method sets up a line name given the line's number,
        type, and version.

        **Note:**

        This MUST be called to generate a line name when calls
        are made to `exist_symb <geosoft.gxapi.GXDB.exist_symb>`, `create_symb <geosoft.gxapi.GXDB.create_symb>` or `delete_symb <geosoft.gxapi.GXDB.delete_symb>`
        for an operation on a line.
        See also SetLineName2_DB.
        """
        name.value = gxapi_cy.WrapDB.set_line_name(GXContext._get_tls_geo(), num, type, ver, name.value.encode())
        



    @classmethod
    def set_line_name2(cls, al_num, type, ver, name):
        """
        Like SetLineName_DB, but can use alphanumeric for line number

        **Note:**

        This MUST be called to generate a line name when calls
        are made to `exist_symb <geosoft.gxapi.GXDB.exist_symb>`, `create_symb <geosoft.gxapi.GXDB.create_symb>` or `delete_symb <geosoft.gxapi.GXDB.delete_symb>`
        for an operation on a line.
        The line number can be any combination of letters and numbers,
        i.e. XU324, 98765, A, 23NGV etc.
        """
        name.value = gxapi_cy.WrapDB.set_line_name2(GXContext._get_tls_geo(), al_num.encode(), type, ver, name.value.encode())
        




    def load_select(self, file):
        """
        Load selections to from a file.
        """
        self._wrapper.load_select(file.encode())
        




    def next_sel_line(self, prev):
        """
        This method will advance to the next selected line based
        on the currently selected line handle.
        """
        ret_val = self._wrapper.next_sel_line(prev)
        return ret_val




    def line_bearing(self, line):
        """
        This method returns the bearing of a line.

        **Note:**

        The channel must be locked `DB_LOCK_READONLY <geosoft.gxapi.DB_LOCK_READONLY>` or `DB_LOCK_READWRITE <geosoft.gxapi.DB_LOCK_READWRITE>`
        
        This function simply returns a value set using the `set_line_bearing <geosoft.gxapi.GXDB.set_line_bearing>`
        function. It returns `rDUMMY <geosoft.gxapi.rDUMMY>` for line categories other than
        `DB_CATEGORY_LINE_FLIGHT <geosoft.gxapi.DB_CATEGORY_LINE_FLIGHT>`.
        
        To calculate the line azimuth based on the first and
        last non-dummy locations, use the `GXDU.direction <geosoft.gxapi.GXDU.direction>` function.

        .. seealso::

            `set_line_bearing <geosoft.gxapi.GXDB.set_line_bearing>`, `GXDU.direction <geosoft.gxapi.GXDU.direction>`
        """
        ret_val = self._wrapper.line_bearing(line)
        return ret_val




    def line_date(self, line):
        """
        This method returns the date of a line.

        **Note:**

        The channel must be locked `DB_LOCK_READONLY <geosoft.gxapi.DB_LOCK_READONLY>` or `DB_LOCK_READWRITE <geosoft.gxapi.DB_LOCK_READWRITE>`
        """
        ret_val = self._wrapper.line_date(line)
        return ret_val




    def save_select(self, file):
        """
        Saves current selections to a file.
        """
        self._wrapper.save_select(file.encode())
        




    def select(self, select, mode):
        """
        Select/deselect lines based on selection string

        **Note:**

        Selections/deselections are cumulative. If lines had already
        been selected, then any further selection/deselection will
        affect that set of selections.
        
        E.g. "L99:800" is the string to select all normal lines from
        99 to 800. If `select <geosoft.gxapi.GXDB.select>` is called again to select "L1000",
        then lines 99 to 800 and 1000 would all be selected.
        
        Use a "T" prefix for Tie lines.
        Use an "F" prefix to specify lines of a specific flight.
        E.g. "F10" would select all lines of flight 10.
        Use an empty string ("") to select/deselect ALL lines.
        """
        self._wrapper.select(select.encode(), mode)
        




    def set_line_bearing(self, line, bearing):
        """
        Sets a line's bearing.

        **Note:**

        The channel must be locked `DB_LOCK_READWRITE <geosoft.gxapi.DB_LOCK_READWRITE>`
        
        This function simply sets a value in the line's metadata
        that is retrieved using the `line_bearing <geosoft.gxapi.GXDB.line_bearing>`
        function. It terminates for line categories other than
        `DB_CATEGORY_LINE_FLIGHT <geosoft.gxapi.DB_CATEGORY_LINE_FLIGHT>`.

        .. seealso::

            `line_bearing <geosoft.gxapi.GXDB.line_bearing>`, `GXDU.direction <geosoft.gxapi.GXDU.direction>`
        """
        self._wrapper.set_line_bearing(line, bearing)
        




    def set_line_date(self, line, date):
        """
        This method sets a line's date.

        **Note:**

        The channel must be locked `DB_LOCK_READWRITE <geosoft.gxapi.DB_LOCK_READWRITE>`
        """
        self._wrapper.set_line_date(line, date)
        




    def set_line_flight(self, line, fl):
        """
        This method sets a line's flight.

        **Note:**

        The channel must be locked `DB_LOCK_READWRITE <geosoft.gxapi.DB_LOCK_READWRITE>`
        """
        self._wrapper.set_line_flight(line, fl)
        




    def set_line_map_fid(self, line, start, end):
        """
        This method changes a line map clip fiducial.

        **Note:**

        for full range, set Start Fid to `rMIN <geosoft.gxapi.rMIN>` and End Fid to `rMAX <geosoft.gxapi.rMAX>`.
        for no data, set Start and End Fids to `rDUMMY <geosoft.gxapi.rDUMMY>`.
        """
        self._wrapper.set_line_map_fid(line, start, end)
        




    def set_line_num(self, line, num):
        """
        This method sets a line's number.

        **Note:**

        The channel must be locked `DB_LOCK_READWRITE <geosoft.gxapi.DB_LOCK_READWRITE>`
        """
        self._wrapper.set_line_num(line, num)
        




    def set_line_type(self, line, type):
        """
        This method sets a line's type.

        **Note:**

        The channel must be locked `DB_LOCK_READWRITE <geosoft.gxapi.DB_LOCK_READWRITE>`
        """
        self._wrapper.set_line_type(line, type)
        




    def set_line_ver(self, line, ver):
        """
        This method sets a line's version.

        **Note:**

        The channel must be locked `DB_LOCK_READWRITE <geosoft.gxapi.DB_LOCK_READWRITE>`
        """
        self._wrapper.set_line_ver(line, ver)
        




    def set_select(self, sel):
        """
        Sets the Line Selections.

        **Note:**

        This method also destroys the DB_SELECT object.
        """
        self._wrapper.set_select(sel)
        




# META



    def get_meta(self, meta):
        """
        Get the metadata of a database.
        """
        self._wrapper.get_meta(meta._wrapper)
        




    def set_meta(self, meta):
        """
        Set the metadata of a database.
        """
        self._wrapper.set_meta(meta._wrapper)
        




# Symbols



    def array_lst(self, lst):
        """
        Load a `GXLST <geosoft.gxapi.GXLST>` object with array (`GXVA <geosoft.gxapi.GXVA>`) channel symbols.
        """
        self._wrapper.array_lst(lst._wrapper)
        




    def array_size_lst(self, columns, lst):
        """
        Load a `GXLST <geosoft.gxapi.GXLST>` object with array (`GXVA <geosoft.gxapi.GXVA>`) channel symbols with a particular number of columns.
        """
        self._wrapper.array_size_lst(columns, lst._wrapper)
        




    def chan_lst(self, lst):
        """
        Load a `GXLST <geosoft.gxapi.GXLST>` with database channels.

        **Note:**

        Populates a `GXLST <geosoft.gxapi.GXLST>` with channel symbols.
        The name is put into the "Name" part of the `GXLST <geosoft.gxapi.GXLST>` (0),
        and the handle, an integer value written as a string, is
        placed in the value part of the `GXLST <geosoft.gxapi.GXLST>` (1).
        Array channels are included, as well as virtual channels (array channel single columns loaded in the database like \\"Chan[1]\\".
        
        The `GXLST <geosoft.gxapi.GXLST>` is cleared first, and the items are sorted by name.
        """
        self._wrapper.chan_lst(lst._wrapper)
        




    def normal_chan_lst(self, lst):
        """
        Load a `GXLST <geosoft.gxapi.GXLST>` with non-array database channels.

        **Note:**

        Like `chan_lst <geosoft.gxapi.GXDB.chan_lst>`, but does not include array channels or virtual channels.
        """
        self._wrapper.normal_chan_lst(lst._wrapper)
        




    def class_chan_lst(self, lst, cl):
        """
        Load a `GXLST <geosoft.gxapi.GXLST>` with channels in a particular class.

        **Note:**

        The Name of the symbol is placed in the
        item name and the item value is set to the symbol handle.
        Only channels with the given class name are included,
        e.g. use "ASSAY" for assay channels in `GXCHIMERA <geosoft.gxapi.GXCHIMERA>`.
        
        The `GXLST <geosoft.gxapi.GXLST>` is cleared first, and the items are sorted by name.
        """
        self._wrapper.class_chan_lst(lst._wrapper, cl.encode())
        




    def class_group_lst(self, lst, cl):
        """
        Load a `GXLST <geosoft.gxapi.GXLST>` with group lines in a particular class.

        **Note:**

        The Name of the symbol is placed in the
        item name and the item value is set to the symbol handle.
        Only group lines with the given class name are included,
        e.g. use "TARGETS" for UX-Detect Target groups.
        
        The `GXLST <geosoft.gxapi.GXLST>` is cleared first, and the items are sorted by name.
        """
        self._wrapper.class_group_lst(lst._wrapper, cl.encode())
        




    def create_symb(self, name, symb, owner, category):
        """
        Create a new Symbol.

        **Note:**

        If symbol already exits, and it is the same type
        simply returns a handle to the existing symbol.
        
        This method simple calls `create_symb_ex <geosoft.gxapi.GXDB.create_symb_ex>` with the
        extra info set to 1.
        
        STRING-type channels: To create a string-type channel,
        enter a negative number for the channel category below.
        For instance, "-32" will create a string channel with
        32 characters per item.
        
        BLOBS: Blobs (Binary Large Objects) can be used for storing
        miscellaneous data which does not fit well into any of the
        other various storage objects, such as a `GXREG <geosoft.gxapi.GXREG>`. Generally,
        one or more objects is serialized to a `GXBF <geosoft.gxapi.GXBF>` object, which
        is then written to the blob using the sWriteBlobBF_DB()
        function. Retrieval is done in the reverse order, using
        sWriteBlobBF_DB() first, then extracting the objects from the
        `GXBF <geosoft.gxapi.GXBF>` object.
        To avoid namespace problems, Geosoft reserves the following
        name prefixes:
        
        OE.   (Core functions)
        GS.   (Applications)
        CS.   (Custom Solutions applications)
        
        Programmers should avoid using the above prefixes as the starting
        letters of their blob names to avoid any possible conflicts.
        """
        ret_val = self._wrapper.create_symb(name.encode(), symb, owner, category)
        return ret_val




    def create_symb_ex(self, name, symb, owner, category, extra):
        """
        Create a new Symbol.

        **Note:**

        If symbol already exits it is returned.
        
        STRING-type channels: To create a string-type channel,
        enter a negative number for the channel category below.
        For instance, "-32" will create a string channel with
        32 characters per item.
        
        Symbol name for `DB_CATEGORY_LINE_FLIGHT <geosoft.gxapi.DB_CATEGORY_LINE_FLIGHT>` must conform to
        the following line naming syntax:
        
        [type][number.version:flight]
        
        Type can be: L - normal line
        B - base line
        T - tie line
        R - trend line
        S - test line
        P - special line
        
        Examples: L100,
        T100.1:16
        
        Note the "Flight" is any whole number that may be useful
        to differentiate processing tasks.
        
        The ability to create a `GXVA <geosoft.gxapi.GXVA>` channel is not available in the
        free interface and requires a Montaj license.
        """
        ret_val = self._wrapper.create_symb_ex(name.encode(), symb, owner, category, extra)
        return ret_val




    def csv_chan_lst(self, lst, channels):
        """
        Load a `GXLST <geosoft.gxapi.GXLST>` with channels in a comma-separated list.

        **Note:**

        The Name of the symbol is placed in the
        item name and the item value is set to the symbol handle.
        Only channels in the list which are present in the database
        are included.
        
        The `GXLST <geosoft.gxapi.GXLST>` is cleared first.
        """
        self._wrapper.csv_chan_lst(lst._wrapper, channels.encode())
        




    def delete_symb(self, symb):
        """
        This method destroys a symbol in the database and all
        the data associated with it. The symbol's lock is
        automatically removed.
        """
        self._wrapper.delete_symb(symb)
        




    def dup_line_symb(self, symb, new):
        """
        Duplicate a line symbol from a group or line symbol.
        The new name must not already exist in the database.
        """
        ret_val = self._wrapper.dup_line_symb(symb, new.encode())
        return ret_val




    def dup_symb(self, symb, new):
        """
        New Symbol by duplicating an existing symbol, LOCKED

        **Note:**

        The symbol will be locked READWRITE.
        The new name must not already exist in the database.

        .. seealso::

            `dup_symb_no_lock <geosoft.gxapi.GXDB.dup_symb_no_lock>`
        """
        ret_val = self._wrapper.dup_symb(symb, new.encode())
        return ret_val




    def dup_symb_no_lock(self, symb, new):
        """
        New Symbol by duplicating an existing symbol, NO LOCK.

        **Note:**

        The symbol will be NOT be locked.
        The new name must not already exist in the database.

        .. seealso::

            `dup_symb <geosoft.gxapi.GXDB.dup_symb>`
        """
        ret_val = self._wrapper.dup_symb_no_lock(symb, new.encode())
        return ret_val




    def find_chan(self, chan):
        """
        Get handle to the specified channel.

        **Note:**

        To work with a specific column from a `GXVA <geosoft.gxapi.GXVA>` channel,
        specify the `GXVA <geosoft.gxapi.GXVA>` element number in square brackets as part
        of the `GXVA <geosoft.gxapi.GXVA>` channel name (e.g. "EM[3]" will treat the fourth
        column of the `GXVA <geosoft.gxapi.GXVA>` channel as a `GXVV <geosoft.gxapi.GXVV>`).
        
        See notes for `find_symb <geosoft.gxapi.GXDB.find_symb>`.
        Introduced in v5.1.3.
        The new `find_chan <geosoft.gxapi.GXDB.find_chan>` searches using the exact channel name.
        """
        ret_val = self._wrapper.find_chan(chan.encode())
        return ret_val




    def find_symb(self, symb, type):
        """
        Get handle to the specified symbol.

        **Note:**

        To work with a specific column from a `GXVA <geosoft.gxapi.GXVA>` channel,
        specify the `GXVA <geosoft.gxapi.GXVA>` element number in square brackets as part
        of the `GXVA <geosoft.gxapi.GXVA>` channel name (e.g. "EM[3]" will treat the fourth
        column of the `GXVA <geosoft.gxapi.GXVA>` channel as a `GXVV <geosoft.gxapi.GXVV>`).
        
        For backward compatibility with GXs not employing the
        `get_xyz_chan_symb <geosoft.gxapi.GXDB.get_xyz_chan_symb>` function, the following behaviour has
        been introduced as of v5.1.3:  (also true for "Y").
        
        `find_symb <geosoft.gxapi.GXDB.find_symb>`(hDB, "X", `DB_SYMB_CHAN <geosoft.gxapi.DB_SYMB_CHAN>`) is now equivalent to:
        
        `get_xyz_chan_symb <geosoft.gxapi.GXDB.get_xyz_chan_symb>`(hDB, `DB_CHAN_X <geosoft.gxapi.DB_CHAN_X>`);
        
        In other words, the current X or Y is searched for, not
        necessarily the literal "X" or "Y". This ensures that newer
        databases, which might have "Easting" and "Northing"
        (or other similar names) instead of "X" and "Y" will still
        work with older GXs expecting "X" and "Y".
        
        The new `find_chan <geosoft.gxapi.GXDB.find_chan>` searches using the exact channel name.
        """
        ret_val = self._wrapper.find_symb(symb.encode(), type)
        return ret_val




    def get_chan_order_lst(self, lst):
        """
        This method gets the channel display order for a
        database. The list will be stored in an `GXLST <geosoft.gxapi.GXLST>` object.
        In order to modify this displayed channels list,
        call `set_chan_order_lst <geosoft.gxapi.GXDB.set_chan_order_lst>` after.
        """
        self._wrapper.get_chan_order_lst(lst._wrapper)
        




    def get_xyz_chan_symb(self, chan):
        """
        Searches for current X, Y or Z channel symbol
        """
        ret_val = self._wrapper.get_xyz_chan_symb(chan)
        return ret_val




    def class_chan_list(self, vv, cl):
        """
        Place a list of channels for a given class in a `GXVV <geosoft.gxapi.GXVV>`.

        **Note:**

        This method generates a list of symbols in the database
        and places their handles into a `GXVV <geosoft.gxapi.GXVV>`. The list is not
        sorted.
        Only channels with the given class name are included,
        e.g. use "ASSAY" for assay channels used in `GXCHIMERA <geosoft.gxapi.GXCHIMERA>`.
        """
        ret_val = self._wrapper.class_chan_list(vv._wrapper, cl.encode())
        return ret_val




    def exist_chan(self, chan):
        """
        See if the specified channel exists in the database.

        **Note:**

        See notes for `exist_symb <geosoft.gxapi.GXDB.exist_symb>`.
        Introduced in v5.1.3.
        `exist_chan <geosoft.gxapi.GXDB.exist_chan>` searches using the exact channel name.
        """
        ret_val = self._wrapper.exist_chan(chan.encode())
        return ret_val




    def exist_symb(self, symb, type):
        """
        This method checks to see if the specified symbol exists
        in the database.

        **Note:**

        For backward compatibility with GXs not employing the
        GetXYZChan_DB function, the following behaviour has
        been introduced as of v5.1.3:  (also true for "Y").
        
        `exist_symb <geosoft.gxapi.GXDB.exist_symb>`(hDB, "X", `DB_SYMB_CHAN <geosoft.gxapi.DB_SYMB_CHAN>`) is now equivalent to:
        
        GetXYZChan_DB(hDB, `DB_CHAN_X <geosoft.gxapi.DB_CHAN_X>`, sXCh);
        `exist_symb <geosoft.gxapi.GXDB.exist_symb>`(hDB, sXCh, `DB_SYMB_CHAN <geosoft.gxapi.DB_SYMB_CHAN>`);
        
        In other words, the current X or Y is searched for, not
        necessarily the literal "X" or "Y". This ensures that newer
        databases, which might have "Easting" and "Northing"
        (or other similar names) instead of "X" and "Y" will still
        work with older GXs expecting "X" and "Y".
        
        The new `exist_chan <geosoft.gxapi.GXDB.exist_chan>` searches using the exact channel name.
        """
        ret_val = self._wrapper.exist_symb(symb.encode(), type)
        return ret_val




    def valid_symb(self, symb, type):
        """
        This method checks to see if the specified symbol is a valid symbol in the database.
        """
        ret_val = self._wrapper.valid_symb(symb, type)
        return ret_val




    def get_symb_lock(self, symb):
        """
        Determines if a symbol is locked
        """
        ret_val = self._wrapper.get_symb_lock(symb)
        return ret_val




    def get_xyz_chan(self, chan_symb, chan):
        """
        Gets current X, Y or Z channel name

        **Note:**

        searches for the "current" X, Y or Z channel.
        If none is defined, then returns "X", "Y" or "Z".
        """
        chan.value = self._wrapper.get_xyz_chan(chan_symb, chan.value.encode())
        




    def symb_list(self, vv, symb):
        """
        Place a list of symbols in a `GXVV <geosoft.gxapi.GXVV>`.
        """
        ret_val = self._wrapper.symb_list(vv._wrapper, symb)
        return ret_val




    def line_lst(self, lst):
        """
        Load a `GXLST <geosoft.gxapi.GXLST>` with database lines.

        **Note:**

        Populates a `GXLST <geosoft.gxapi.GXLST>` with channel symbols.
        The name is put into the "Name" part of the `GXLST <geosoft.gxapi.GXLST>` (0),
        and the handle, an integer value written as a string, is
        placed in the value part of the `GXLST <geosoft.gxapi.GXLST>` (1).
        The `GXLST <geosoft.gxapi.GXLST>` is cleared first, and the items are sorted in logical line order.
        """
        self._wrapper.line_lst(lst._wrapper)
        




    def lock_symb(self, symb, lock, wait):
        """
        Locks a symbol for READONLY or READWRITE.
        """
        self._wrapper.lock_symb(symb, lock, wait)
        




    def mask_chan_lst(self, lst):
        """
        Load a `GXLST <geosoft.gxapi.GXLST>` with mask channels.

        **Note:**

        Loads a `GXLST <geosoft.gxapi.GXLST>` with all channels with CLASS "MASK", as well
        as all channels containing the string "MASK", as long
        as the CLASS for these channels is not set to something
        other than "" or "MASK".
        
        This function is a duplicate of the `GXCHIMERA.mask_chan_lst <geosoft.gxapi.GXCHIMERA.mask_chan_lst>`
        function, and can be used if `GXCHIMERA <geosoft.gxapi.GXCHIMERA>` is not installed.
        
        The `GXLST <geosoft.gxapi.GXLST>` is cleared first, and the items are sorted by name.
        "None" is added at the end, with a handle value of "-1".
        """
        self._wrapper.mask_chan_lst(lst._wrapper)
        




    def selected_line_lst(self, lst):
        """
        Load a `GXLST <geosoft.gxapi.GXLST>` with the selected lines.

        **Note:**

        This method populates a `GXLST <geosoft.gxapi.GXLST>` object with all of the symbols
        of the selected lines in the database.
        The name is put into the "Name" part of the `GXLST <geosoft.gxapi.GXLST>` (0),
        and the handle, an integer value written as a string, is
        placed in the value part of the `GXLST <geosoft.gxapi.GXLST>` (1).
        
        Symbols are automatically sorted in logical line order.
        """
        self._wrapper.selected_line_lst(lst._wrapper)
        




    def set_chan_order_lst(self, lst):
        """
        This method sets the channel display order for a
        database. The list to modify will be stored in an `GXLST <geosoft.gxapi.GXLST>`
        object. Call `get_chan_order_lst <geosoft.gxapi.GXDB.get_chan_order_lst>` to populate the `GXLST <geosoft.gxapi.GXLST>`.
        """
        self._wrapper.set_chan_order_lst(lst._wrapper)
        




    def set_xyz_chan(self, chan_symb, chan):
        """
        Sets current X, Y or Z channel name

        **Note:**

        If the value specified is "", the internally stored value
        is cleared, and GetXYZChan_DB will return "X", "Y" or "Z"
        
        This can be used, for instance, to make "Easting" and "Northing"
        the current X and Y channels, and have GXs using the
        `get_xyz_chan_symb <geosoft.gxapi.GXDB.get_xyz_chan_symb>` function to load "X" and "Y" work as desired.
        """
        self._wrapper.set_xyz_chan(chan_symb, chan.encode())
        




    def string_chan_lst(self, lst):
        """
        Load a `GXLST <geosoft.gxapi.GXLST>` with string-type channels.

        **Note:**

        The Name of the symbol is placed in the
        item name and the item value is set to the symbol handle.
        Only channels with the string-type data (sChanType_DB < 0)
        are included.
        
        The `GXLST <geosoft.gxapi.GXLST>` is cleared first, and the items are sorted by name.
        """
        self._wrapper.string_chan_lst(lst._wrapper)
        




    def symb_lst(self, lst, type):
        """
        Populate a `GXLST <geosoft.gxapi.GXLST>` with database symbols.

        **Note:**

        Populates a `GXLST <geosoft.gxapi.GXLST>` with channel, line, blob or user symbols.
        The name is put into the "Name" part of the `GXLST <geosoft.gxapi.GXLST>` (0),
        and the handle, an integer value written as a string, is
        placed in the value part of the `GXLST <geosoft.gxapi.GXLST>` (1).
        
        Line symbols are automatically sorted in logical line order.
        
        NOTE: The `GXLST <geosoft.gxapi.GXLST>` is NOT cleared before being filled. If you
        want to clear the `GXLST <geosoft.gxapi.GXLST>` and get sorted values, use the
        `chan_lst <geosoft.gxapi.GXDB.chan_lst>` and `line_lst <geosoft.gxapi.GXDB.line_lst>` functions.

        .. seealso::

            `chan_lst <geosoft.gxapi.GXDB.chan_lst>`, `line_lst <geosoft.gxapi.GXDB.line_lst>`, `selected_line_lst <geosoft.gxapi.GXDB.selected_line_lst>`
        """
        self._wrapper.symb_lst(lst._wrapper, type)
        




    def un_lock_all_symb(self):
        """
        UnLocks all symbols.
        """
        self._wrapper.un_lock_all_symb()
        




    def un_lock_symb(self, symb):
        """
        UnLocks a symbol.
        """
        self._wrapper.un_lock_symb(symb)
        




# VA Channels



    def add_associated_load(self, group, chan):
        """
        Add this channel to the auto-load feature of the group.

        **Note:**

        If the channel is not yet associated, it is first associated.
        If the channel is already in the associated-load list, this
        does nothing.
        
        As of v6.0, the load-status of channels is no longer stored
        in the database, but in the project, so this function is
        equivalent to calling `associate <geosoft.gxapi.GXDB.associate>`.
        """
        self._wrapper.add_associated_load(group, chan)
        




    def add_comment(self, comment, str_val, indent):
        """
        Add a comment with a string to the activity log of the database.

        **Note:**

        The comment is written in the form:
        
        Comment: String2
        
        and is followed by a carriage return.
        The activity log is created automatically if it does not exist.
        """
        self._wrapper.add_comment(comment.encode(), str_val.encode(), indent)
        




    def add_int_comment(self, comment, val, indent):
        """
        Add a comment with an integer to the activity log of the database.

        **Note:**

        The comment is written in the form:
        
        Comment: Value
        
        and is followed by a carriage return.
        The activity log is created automatically if it does not exist.
        
        See Notes in `add_comment <geosoft.gxapi.GXDB.add_comment>`.
        """
        self._wrapper.add_int_comment(comment.encode(), val, indent)
        




    def add_double_comment(self, comment, val, indent):
        """
        Add a comment with a float value to the activity log of the database.

        **Note:**

        The comment is written in the form:
        
        Comment: Value
        
        and if followed by a carriage return.
        The activity log is created automatically if it does not exist.
        
        See Notes in `add_comment <geosoft.gxapi.GXDB.add_comment>`.
        """
        self._wrapper.add_double_comment(comment.encode(), val, indent)
        




    def add_time_comment(self, comment, indent):
        """
        Add a comment with the date and time to the activity log of the database.

        **Note:**

        The comment is written in the form:
        
        Comment: 2001/12/31 23:59:59
        
        and is followed by a carriage return.
        The activity log is created automatically if it does not exist.
        
        See Notes in `add_comment <geosoft.gxapi.GXDB.add_comment>`.
        """
        self._wrapper.add_time_comment(comment.encode(), indent)
        




    def associate(self, group, chan):
        """
        Associate a channel with a group.

        **Note:**

        If it is already associated, or if the group has no
        defined group class, does nothing.
        
        As of v6.3, if a group line has no class defined, then ALL
        channels are assumed to be associated with it. This means
        that you need to associate a new channel with a group only in
        those cases where the group class is defined.
        
        If this function is used on a group with a group class, then
        the channel is added to class's association list, and the
        channel will be recognized as being associated with all
        groups of that class.
        """
        self._wrapper.associate(group, chan)
        




    def associate_all(self, group):
        """
        Associate all channels with a group.

        **Note:**

        As of v6.3, if a group line has no class defined, then ALL
        channels are already assumed to be associated with it, and this
        function does nothing.
        """
        self._wrapper.associate_all(group)
        




    def associate_class(self, chan, cl):
        """
        Associate a channel with all groups of a specific class.

        **Note:**

        As of v6.3, if a group line has no class defined, then ALL
        channels are automatically assumed to be associated with it.
        """
        self._wrapper.associate_class(chan, cl.encode())
        



    @classmethod
    def gen_valid_chan_symb(cls, str_in, str_out):
        """
        Generate a valid channel name from a name candidate
        """
        str_out.value = gxapi_cy.WrapDB.gen_valid_chan_symb(GXContext._get_tls_geo(), str_in.encode(), str_out.value.encode())
        



    @classmethod
    def gen_valid_line_symb(cls, str_in, str_out):
        """
        Generate a valid line symb name string from given string.

        **Note:**

        The returned name is either the same size as the input
        or shorter. Escapes, leading and trailing spaces are removed, then
        all illegal characters are replaced with an underscore.
        """
        str_out.value = gxapi_cy.WrapDB.gen_valid_line_symb(GXContext._get_tls_geo(), str_in.encode(), str_out.value.encode())
        




    def get_chan_va(self, line, chan, va):
        """
        Place the contents of a channel in a `GXVA <geosoft.gxapi.GXVA>`.

        .. seealso::

            `GXVA <geosoft.gxapi.GXVA>` class.
        """
        self._wrapper.get_chan_va(line, chan, va._wrapper)
        




    def get_va_scaling(self, ch, base, range):
        """
        Get base and range for `GXVA <geosoft.gxapi.GXVA>` channel cell display.

        **Note:**

        See `set_va_scaling <geosoft.gxapi.GXDB.set_va_scaling>`.
        """
        base.value, range.value = self._wrapper.get_va_scaling(ch, base.value, range.value)
        




    def get_va_windows(self, ch, min_w, max_w):
        """
        Get the range of windows displayed for a `GXVA <geosoft.gxapi.GXVA>` channel.

        **Note:**

        See `set_va_windows <geosoft.gxapi.GXDB.set_va_windows>`.
        """
        min_w.value, max_w.value = self._wrapper.get_va_windows(ch, min_w.value, max_w.value)
        




    def set_va_base_coordinate_info(self, ch, domain, base, vv, units, allow_changes):
        """
        Set the array channel base coordinate type, offset and values.

        **Note:**

        See `get_va_base_coordinate_info <geosoft.gxapi.GXDB.get_va_base_coordinate_info>`.
        """
        self._wrapper.set_va_base_coordinate_info(ch, domain, base, vv._wrapper, units.encode(), allow_changes)
        




    def get_va_base_coordinate_info(self, ch, domain, base, vv, units):
        """
        Set the array channel base coordinate type, offset and values.

        **Note:**

        See `set_va_base_coordinate_info <geosoft.gxapi.GXDB.set_va_base_coordinate_info>`.
        """
        domain.value, base.value, units.value = self._wrapper.get_va_base_coordinate_info(ch, domain.value, base.value, vv._wrapper, units.value.encode())
        




    def get_group_class(self, symb, cl):
        """
        Set the Class name for a group line.

        **Note:**

        This method fails if the line is not a group line.
        Group classes are used to identify group lines used for
        special purposes, e.g.: "COLLAR" for the Wholeplot collar table,
        or "TARGETS" for the UX-Detect Targets list.

        .. seealso::

            `line_category <geosoft.gxapi.GXDB.line_category>` - to see if a line is a group line.
        """
        cl.value = self._wrapper.get_group_class(symb, cl.value.encode())
        




    def get_info(self, item):
        """
        Get information about the database.
        """
        ret_val = self._wrapper.get_info(item)
        return ret_val




    def get_va_prof_color_file(self, ch, file):
        """
        Get colors for a `GXVA <geosoft.gxapi.GXVA>` channel when displayed in the profile window.

        **Note:**

        See `set_va_prof_color_file <geosoft.gxapi.GXDB.set_va_prof_color_file>`.
        """
        file.value = self._wrapper.get_va_prof_color_file(ch, file.value.encode())
        




    def get_va_prof_sect_option(self, ch, option):
        """
        Get the display options of `GXVA <geosoft.gxapi.GXVA>` channels
        """
        option.value = self._wrapper.get_va_prof_sect_option(ch, option.value.encode())
        




    def get_va_sect_color_file(self, ch, file):
        """
        Get colors for a `GXVA <geosoft.gxapi.GXVA>` channel when displayed section in the profile window.

        **Note:**

        Fails in the channel is not an array channel
        """
        file.value = self._wrapper.get_va_sect_color_file(ch, file.value.encode())
        




    def is_associated(self, group, chan):
        """
        Check to see if a channel is associated with group.
        """
        ret_val = self._wrapper.is_associated(group, chan)
        return ret_val




    def is_wholeplot(self):
        """
        Is this a Wholeplot database?

        **Note:**

        Currently checks to see if the DH_COLLAR line exists.
        """
        ret_val = self._wrapper.is_wholeplot()
        return ret_val




    def put_chan_va(self, line, chan, va):
        """
        Place the contents of a `GXVA <geosoft.gxapi.GXVA>` in a channel.

        .. seealso::

            `GXVA <geosoft.gxapi.GXVA>` class.
        """
        self._wrapper.put_chan_va(line, chan, va._wrapper)
        




    def set_group_class(self, symb, cl):
        """
        Set the Class name for a group line.

        **Note:**

        This method fails if the line is not a group line.
        Group classes are used to identify group lines used for
        special purposes. All group lines with the same class share
        the same list of associated channels.
        
        As of v6.3, if a group line has no class defined, then ALL
        channels are assumed to be associated with it. This means
        that a group class should only be defined when you wish to
        associate a subset of the available channels to group line.

        .. seealso::

            `line_category <geosoft.gxapi.GXDB.line_category>` - to see if a line is a group line.
            `associate <geosoft.gxapi.GXDB.associate>` - Associate a channel with a group.
        """
        self._wrapper.set_group_class(symb, cl.encode())
        




    def set_va_prof_color_file(self, ch, file):
        """
        Set colors for a `GXVA <geosoft.gxapi.GXVA>` channel when displayed in the profile window.

        **Note:**

        Fails in the channel is not an array channel, if the
        file does not exist, or if it is not a valid color zone file.
        
        The individual columns in the array channel are displayed using the input
        zone file colors. A linear `GXITR <geosoft.gxapi.GXITR>` from 0 to 1 is created on the color zones
        to map to individual channel indices (expressed as a fraction as shown below).
        
        For instance, for a file with 8 colors the ranges are as follows:
        
        Color Range
        Color 1    0        > value >=  0.125
        Color 2    0.125    > value >=  0.25
        Color 3    0.25     > value >=  0.375
        Color 4    0.375    > value >=  0.5
        Color 5    0.5      > value >=  0.625
        Color 6    0.625    > value >=  0.75
        Color 7    0.75     > value >=  0.875
        Color 8    0.875    > value >=  1.0
        
        When an array channel is displayed, the index of each element (column) is mapped
        into the corresponding range above using the following formula:
        
        value = (column index) / (# of columns - 1)
        
        For an array with 8 columns, you get the following values:
        
        Column   Value    Color
        0        0        1
        1        0.14     2
        2        0.28     3
        3        0.43     4
        4        0.57     5
        5        0.71     6
        6        0.86     7
        7        1.0      8
        
        The color file search path is: Local directory, then oasismontaj\\tbl.
        """
        self._wrapper.set_va_prof_color_file(ch, file.encode())
        




    def set_va_prof_sect_option(self, ch, option):
        """
        Set the display options of `GXVA <geosoft.gxapi.GXVA>` channels
        """
        self._wrapper.set_va_prof_sect_option(ch, option.encode())
        




    def set_va_scaling(self, ch, base, range):
        """
        Set base and range for `GXVA <geosoft.gxapi.GXVA>` channel cell display.

        **Note:**

        By default, `GXVA <geosoft.gxapi.GXVA>` profiles autoscale to fit in the database cell.
        This lets the user set a single base and range for all cells.
        If either input is a dummy, both are set as dummies, and autoscaling
        is used.
        """
        self._wrapper.set_va_scaling(ch, base, range)
        




    def set_va_sect_color_file(self, ch, file):
        """
        Set colors for a `GXVA <geosoft.gxapi.GXVA>` channel when displayed section in the profile window.

        **Note:**

        Fails in the channel is not an array channel, if the
        file does not exist, or if it is not a valid color zone file.
        """
        self._wrapper.set_va_sect_color_file(ch, file.encode())
        




    def set_va_windows(self, ch, min_w, max_w):
        """
        Set the range of windows to display for a `GXVA <geosoft.gxapi.GXVA>` channel.

        **Note:**

        Use to display a subset of the `GXVA <geosoft.gxapi.GXVA>` channel windows in the GDB.
        Windows index from 0.
        """
        self._wrapper.set_va_windows(ch, min_w, max_w)
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer