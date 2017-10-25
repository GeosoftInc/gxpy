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

    The :class:`geosoft.gxapi.GXDB` class is used to create, open and work with databases and database symbols.
    Database symbols are objects inside databases, such as lines, channels and blobs

    **Note:**

    The following defines are not used by any methods but are
    used by GX's:
    
    :attr:`geosoft.gxapi.DB_ACTIVITY_BLOB`
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
        A null (undefined) instance of :class:`geosoft.gxapi.GXDB`
        
        :returns: A null :class:`geosoft.gxapi.GXDB`
        """
        return cls()

    def is_null(self):
        """
        Check if the instance of :class:`geosoft.gxapi.GXDB` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of :class:`geosoft.gxapi.GXDB`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Channel



    def create_dup(self, p2):
        """
        This method makes a brand new database identical to the input
        Database in-size.
        The database is opened in ReadWrite Mode.
        """
        self._wrapper.create_dup(p2.encode())
        




    def create_dup_comp(self, p2, p3):
        """
        This method makes a brand new database identical to the input
        Database in-size except it changes the compression.
        The database is opened in ReadWrite Mode.
        """
        self._wrapper.create_dup_comp(p2.encode(), p3)
        




    def dup_symb_across(self, p2, p3):
        """
        Create a new Symbol by duplicating an existing symbol.
        exactly the same type but in output database. The symbol must
        not already exist in the output database.
        """
        ret_val = self._wrapper.dup_symb_across(p2._wrapper, p3)
        return ret_val




    def easy_maker_symb(self, p2, p3, p4):
        """
        Adds a Maker to the database symbol based on current GX
        """
        self._wrapper.easy_maker_symb(p2, p3.encode(), p4.encode())
        




    def get_chan_str(self, p2, p3, p4, p5):
        """
        Get individual elements in a channel.

        **Note:**

        These methods are slow and should only be used when
        performance is not an issue.
        """
        p5.value = self._wrapper.get_chan_str(p2, p3, p4, p5.value.encode())
        




    def get_chan_vv(self, p2, p3, p4):
        """
        Place the contents of a channel in a :class:`geosoft.gxapi.GXVV`.

        **Note:**

        If a :class:`geosoft.gxapi.GXVA` channel is specified, then element [0] of this
        :class:`geosoft.gxapi.GXVA` channel is used to populated the :class:`geosoft.gxapi.GXVV`.
        """
        self._wrapper.get_chan_vv(p2, p3, p4._wrapper)
        




    def get_chan_vv_expanded(self, p2, p3, p4):
        """
        Read a channel into a :class:`geosoft.gxapi.GXVV`. If the channel is a :class:`geosoft.gxapi.GXVA` channel it is
        treaded as a :class:`geosoft.gxapi.GXVV` channel with multiple values per fid and the FID expation
        is set to the array size.

        **Note:**

        This method is to be used in conjunction with the ReFidVV_VV method
        that will honor the FID Expansion setting.
        """
        self._wrapper.get_chan_vv_expanded(p2, p3, p4._wrapper)
        




    def get_ipj(self, p2, p3):
        """
        Get georeference information in an :class:`geosoft.gxapi.GXIPJ`.

        **Note:**

        If the channel does not have an :class:`geosoft.gxapi.GXIPJ`, the :class:`geosoft.gxapi.GXIPJ` that is
        returned will have an unknown projection.
        """
        self._wrapper.get_ipj(p2, p3._wrapper)
        




    def get_itr(self, p2, p3):
        """
        Get :class:`geosoft.gxapi.GXITR` for a channel.

        **Note:**

        If a channel does not have an :class:`geosoft.gxapi.GXITR`, GetITR_DB will not change
        the passed :class:`geosoft.gxapi.GXITR`.
        Channel must be locked for READONLY or READWRITE.
        """
        self._wrapper.get_itr(p2, p3._wrapper)
        




    def get_reg_symb(self, p2, p3):
        """
        Get a :class:`geosoft.gxapi.GXREG` object from a symbol
        """
        self._wrapper.get_reg_symb(p2, p3._wrapper)
        




    def get_reg_symb_setting(self, p2, p3, p4):
        """
        Get a :class:`geosoft.gxapi.GXREG` string setting from a symbol reg

        **Note:**

        The symbol :class:`geosoft.gxapi.GXREG` is used to store a variety of attribute
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
        
        This is a convenient but low-performance way to get/set :class:`geosoft.gxapi.GXREG`
        settings.  If performance is an issue, and more than one
        setting is to be Get and or Set, use the :class:`geosoft.gxapi.GXREG` directly.
        """
        p4.value = self._wrapper.get_reg_symb_setting(p2, p3.encode(), p4.value.encode())
        




    def get_va_chan_vv(self, p2, p3, p4, p5, p6):
        """
        Place the contents of a specific part of a channel in a :class:`geosoft.gxapi.GXVV`.

        **Note:**

        If a :class:`geosoft.gxapi.GXVA` channel is specified, then element [0] of this
        :class:`geosoft.gxapi.GXVA` channel is used to populated the :class:`geosoft.gxapi.GXVV`.
        """
        self._wrapper.get_va_chan_vv(p2, p3, p4._wrapper, p5, p6)
        




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




    def format_chan(self, p2, p3, p4):
        """
        Format a real value based on a channel format.

        **Note:**

        If the passed string is too short, the result will be
        "**".
        """
        p4.value = self._wrapper.format_chan(p2, p3, p4.value.encode())
        




    def get_chan_array_size(self, p2):
        """
        This method Gets a channel's array size for a
        given channel handle.
        """
        ret_val = self._wrapper.get_chan_array_size(p2)
        return ret_val




    def get_chan_class(self, p2, p3):
        """
        This method gets a channel's label

        **Note:**

        The channel label is stored in the "CLASS" parameter
        of the channel reg. If no class is defined, then an
        empty string is returned.
        The channel must be locked :attr:`geosoft.gxapi.DB_LOCK_READONLY` or :attr:`geosoft.gxapi.DB_LOCK_READWRITE`
        """
        p3.value = self._wrapper.get_chan_class(p2, p3.value.encode())
        




    def get_chan_decimal(self, p2):
        """
        This method gets a channel's number of digits displayed
        to the right of the decimal point.

        **Note:**

        The channel must be locked :attr:`geosoft.gxapi.DB_LOCK_READONLY` or :attr:`geosoft.gxapi.DB_LOCK_READWRITE`
        """
        ret_val = self._wrapper.get_chan_decimal(p2)
        return ret_val




    def get_chan_format(self, p2):
        """
        This method Gets a channel's display format for a
        given channel handle.

        **Note:**

        The returned format is one of the `DB_CHAN_FORMAT`.
        The channel must be locked :attr:`geosoft.gxapi.DB_LOCK_READONLY` or :attr:`geosoft.gxapi.DB_LOCK_READWRITE`
        """
        ret_val = self._wrapper.get_chan_format(p2)
        return ret_val




    def get_chan_int(self, p2, p3, p4):
        """
        Get individual elements in a channel.

        **Note:**

        These methods are slow and should only be used when
        performance is not an issue.
        """
        ret_val = self._wrapper.get_chan_int(p2, p3, p4)
        return ret_val




    def get_chan_label(self, p2, p3):
        """
        This method gets a channel's label

        **Note:**

        The channel label is stored in the "LABEL" parameter
        of the channel reg.  If the setting is empty, the
        channel name is returned.
        The channel must be locked :attr:`geosoft.gxapi.DB_LOCK_READONLY` or :attr:`geosoft.gxapi.DB_LOCK_READWRITE`
        """
        p3.value = self._wrapper.get_chan_label(p2, p3.value.encode())
        




    def get_chan_name(self, p2, p3):
        """
        This method Gets a channel's name for a
        given channel handle.

        **Note:**

        The channel must be locked :attr:`geosoft.gxapi.DB_LOCK_READONLY` or :attr:`geosoft.gxapi.DB_LOCK_READWRITE`
        """
        p3.value = self._wrapper.get_chan_name(p2, p3.value.encode())
        




    def get_chan_protect(self, p2):
        """
        This method gets a channel's read-only protection status.

        **Note:**

        The channel must be locked :attr:`geosoft.gxapi.DB_LOCK_READONLY` or :attr:`geosoft.gxapi.DB_LOCK_READWRITE`
        """
        ret_val = self._wrapper.get_chan_protect(p2)
        return ret_val




    def get_chan_type(self, p2):
        """
        This method Gets a channel's type for a
        given channel handle.

        **Note:**

        The type returned is one of the `DB_CATEGORY_CHAN`.
        Use the GS_SIMPLE_TYPE() macro to convert to INT,REAL
        or string types.
        The channel must be locked :attr:`geosoft.gxapi.DB_LOCK_READONLY` or :attr:`geosoft.gxapi.DB_LOCK_READWRITE`
        """
        ret_val = self._wrapper.get_chan_type(p2)
        return ret_val




    def get_chan_unit(self, p2, p3):
        """
        This method Gets a channel's unit

        **Note:**

        The unit label is stored in the "UNITS" parameter
        of the channel reg.
        The channel must be locked :attr:`geosoft.gxapi.DB_LOCK_READONLY` or :attr:`geosoft.gxapi.DB_LOCK_READWRITE`
        """
        p3.value = self._wrapper.get_chan_unit(p2, p3.value.encode())
        




    def get_chan_width(self, p2):
        """
        This method gets a channel's display width for a
        given channel handle.

        **Note:**

        The channel must be locked :attr:`geosoft.gxapi.DB_LOCK_READONLY` or :attr:`geosoft.gxapi.DB_LOCK_READWRITE`
        """
        ret_val = self._wrapper.get_chan_width(p2)
        return ret_val




    def get_name(self, p2, p3):
        """
        Gets a name from the database.
        """
        p3.value = self._wrapper.get_name(p2, p3.value.encode())
        




    def get_reg_symb_setting_int(self, p2, p3):
        """
        Get an integer-valued :class:`geosoft.gxapi.GXREG` setting from a symbol reg

        **Note:**

        Same as GetRegSymbSetting_DB, but converts
        the setting automatically to an integer value.
        
        This is a convenient but low-performance way to get/set :class:`geosoft.gxapi.GXREG`
        settings.  If performance is an issue, and more than one
        setting is to be Get and or Set, use the :class:`geosoft.gxapi.GXREG` directly.
        """
        ret_val = self._wrapper.get_reg_symb_setting_int(p2, p3.encode())
        return ret_val




    def get_symb_name(self, p2, p3):
        """
        This method gets a symbol's name

        **Note:**

        See GetChanName_DB for more information
        The channel must be locked :attr:`geosoft.gxapi.DB_LOCK_READONLY` or :attr:`geosoft.gxapi.DB_LOCK_READWRITE`
        """
        p3.value = self._wrapper.get_symb_name(p2, p3.value.encode())
        




    def have_itr(self, p2):
        """
        Returns TRUE if channel has an :class:`geosoft.gxapi.GXITR`.

        **Note:**

        If a channel has an :class:`geosoft.gxapi.GXITR`, the :class:`geosoft.gxapi.GXITR` colors are used to
        display channel values in the spreadsheet.
        
        If a channel does not have an :class:`geosoft.gxapi.GXITR`, GetITR_DB will not change
        the passed :class:`geosoft.gxapi.GXITR`.
        """
        ret_val = self._wrapper.have_itr(p2)
        return ret_val




    def coord_pair(self, p2, p3):
        """
        Get the matching coordinate pair of a channel.

        **Note:**

        If the channel does not have a matching coordinate
        pair, or of the channel does not exist, the returned
        string will be empty.
        """
        ret_val, p3.value = self._wrapper.coord_pair(p2.encode(), p3.value.encode())
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




    def maker_symb(self, p2, p3, p4, p5):
        """
        Adds a Maker to the database symbol
        """
        self._wrapper.maker_symb(p2, p3.encode(), p4.encode(), p5.encode())
        




    def put_chan_vv(self, p2, p3, p4):
        """
        Place the contents of a :class:`geosoft.gxapi.GXVV` in a channel.

        **Note:**

        If a :class:`geosoft.gxapi.GXVA` channel is specified, then element [0] of this
        :class:`geosoft.gxapi.GXVA` channel will be populated with the :class:`geosoft.gxapi.GXVV`.
        
        There is a limit of 2000 elements for non-licensed users.
        """
        self._wrapper.put_chan_vv(p2, p3, p4._wrapper)
        




    def put_va_chan_vv(self, p2, p3, p4, p5, p6):
        """
        Place the contents of a :class:`geosoft.gxapi.GXVV` at a specific part of a channel.

        **Note:**

        If a :class:`geosoft.gxapi.GXVA` channel is specified, then element [0] of this
        :class:`geosoft.gxapi.GXVA` channel will be populated with the :class:`geosoft.gxapi.GXVV`.
        """
        self._wrapper.put_va_chan_vv(p2, p3, p4._wrapper, p5, p6)
        




    def read_blob_bf(self, p2, p3):
        """
        Read a blob from a database into a file.
        """
        self._wrapper.read_blob_bf(p2, p3._wrapper)
        




    def get_chan_double(self, p2, p3, p4):
        """
        Get individual elements in a channel.

        **Note:**

        These methods are slow and should only be used when
        performance is not an issue.
        """
        ret_val = self._wrapper.get_chan_double(p2, p3, p4)
        return ret_val




    def get_reg_symb_setting_double(self, p2, p3):
        """
        Get a real-valued :class:`geosoft.gxapi.GXREG` setting from a symbol reg

        **Note:**

        Same as GetRegSymbSetting_DB, but converts
        the setting automatically to a real value.
        
        This is a convenient but low-performance way to get/set :class:`geosoft.gxapi.GXREG`
        settings.  If performance is an issue, and more than one
        setting is to be Get and or Set, use the :class:`geosoft.gxapi.GXREG` directly.
        """
        ret_val = self._wrapper.get_reg_symb_setting_double(p2, p3.encode())
        return ret_val




    def set_all_chan_protect(self, p2):
        """
        This method sets all the channels' read-only protection status.

        **Note:**

        Value to set must be either :attr:`geosoft.gxapi.DB_CHAN_PROTECTED` or
        :attr:`geosoft.gxapi.DB_CHAN_UNPROTECTED`
        This method does its own channel locking/unlocking.
        Channels already lock :attr:`geosoft.gxapi.DB_LOCK_READONLY` are ignored.
        """
        self._wrapper.set_all_chan_protect(p2)
        




    def set_chan_class(self, p2, p3):
        """
        Set a channel class

        **Note:**

        The channel class is stored in the "CLASS" parameter
        of the channel reg.
        The channel must be locked :attr:`geosoft.gxapi.DB_LOCK_READWRITE`
        """
        self._wrapper.set_chan_class(p2, p3.encode())
        




    def set_chan_decimal(self, p2, p3):
        """
        This method sets a channel's number of digits displayed
        to the right of the decimal point.

        **Note:**

        The number of display digits must be from 0 to 50.
        The channel must be locked :attr:`geosoft.gxapi.DB_LOCK_READWRITE`
        """
        self._wrapper.set_chan_decimal(p2, p3)
        




    def set_chan_format(self, p2, p3):
        """
        This method sets a channel's display format.

        **Note:**

        The channel must be locked :attr:`geosoft.gxapi.DB_LOCK_READWRITE`
        """
        self._wrapper.set_chan_format(p2, p3)
        




    def set_chan_int(self, p2, p3, p4, p5):
        """
        Set individual elements in a channel.

        **Note:**

        These methods are slow and should only be used when
        performance is not an issue.
        """
        self._wrapper.set_chan_int(p2, p3, p4, p5)
        




    def set_chan_label(self, p2, p3):
        """
        Set a channel label

        **Note:**

        The channel label is stored in the "LABEL" parameter
        of the channel reg.
        The channel must be locked :attr:`geosoft.gxapi.DB_LOCK_READWRITE`
        """
        self._wrapper.set_chan_label(p2, p3.encode())
        




    def set_chan_name(self, p2, p3):
        """
        This method sets a channel's name.

        **Note:**

        The channel must be locked :attr:`geosoft.gxapi.DB_LOCK_READWRITE`
        """
        self._wrapper.set_chan_name(p2, p3.encode())
        




    def set_chan_protect(self, p2, p3):
        """
        This method sets a channel's read-only protection
        status.

        **Note:**

        Value to set must be either :attr:`geosoft.gxapi.DB_CHAN_PROTECTED` or
        :attr:`geosoft.gxapi.DB_CHAN_UNPROTECTED`
        The channel must be locked :attr:`geosoft.gxapi.DB_LOCK_READWRITE`
        """
        self._wrapper.set_chan_protect(p2, p3)
        




    def set_chan_double(self, p2, p3, p4, p5):
        """
        Set individual elements in a channel.

        **Note:**

        These methods are slow and should only be used when
        performance is not an issue.
        """
        self._wrapper.set_chan_double(p2, p3, p4, p5)
        




    def set_chan_str(self, p2, p3, p4, p5):
        """
        Set individual elements in a channel.

        **Note:**

        These methods are slow and should only be used when
        performance is not an issue.
        """
        self._wrapper.set_chan_str(p2, p3, p4, p5.encode())
        




    def set_chan_unit(self, p2, p3):
        """
        This method sets a channel's unit for a
        given channel handle.

        **Note:**

        The channel must be locked :attr:`geosoft.gxapi.DB_LOCK_READWRITE`
        """
        self._wrapper.set_chan_unit(p2, p3.encode())
        




    def set_chan_width(self, p2, p3):
        """
        This method sets a channel's display width

        **Note:**

        The number of display digits must be from 0 to 50.
        The channel must be locked :attr:`geosoft.gxapi.DB_LOCK_READWRITE`
        """
        self._wrapper.set_chan_width(p2, p3)
        




    def set_ipj(self, p2, p3, p4):
        """
        Set a :class:`geosoft.gxapi.GXREG` object into a symbol
        """
        self._wrapper.set_ipj(p2, p3, p4._wrapper)
        




    def set_itr(self, p2, p3):
        """
        Set :class:`geosoft.gxapi.GXITR` for a channel.

        **Note:**

        Use :attr:`geosoft.gxapi.ITR_NULL` to clear the channel :class:`geosoft.gxapi.GXITR`.
        Channel must be locked for READONLY or READWRITE.
        """
        self._wrapper.set_itr(p2, p3._wrapper)
        




    def set_reg_symb(self, p2, p3):
        """
        Set a :class:`geosoft.gxapi.GXREG` object into a symbol
        """
        self._wrapper.set_reg_symb(p2, p3._wrapper)
        




    def set_reg_symb_setting(self, p2, p3, p4):
        """
        Set a :class:`geosoft.gxapi.GXREG` string setting in a symbol reg

        **Note:**

        The symbol :class:`geosoft.gxapi.GXREG` is used to store a variety of attribute
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
        
        This is a convenient but low-performance way to get/set :class:`geosoft.gxapi.GXREG`
        settings.  If performance is an issue, and more than one
        setting is to be Get and or Set, use the :class:`geosoft.gxapi.GXREG` directly.
        """
        self._wrapper.set_reg_symb_setting(p2, p3.encode(), p4.encode())
        




    def write_blob_bf(self, p2, p3):
        """
        Write a blob from a file into a database.
        """
        self._wrapper.write_blob_bf(p2, p3._wrapper)
        




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
    def create(cls, p1, p2, p3, p4, p5, p6, p7, p8):
        """
        This method makes a brand new database of the specified size.
        The database is opened in ReadWrite Mode.
        """
        gxapi_cy.WrapDB.create(GXContext._get_tls_geo(), p1.encode(), p2, p3, p4, p5, p6, p7.encode(), p8.encode())
        



    @classmethod
    def create_comp(cls, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10):
        """
        This method makes a brand new database of the specified size.
        The database is opened in ReadWrite Mode. Also allows you to
        set paging size and the Compression Level.
        """
        gxapi_cy.WrapDB.create_comp(GXContext._get_tls_geo(), p1.encode(), p2, p3, p4, p5, p6, p7.encode(), p8.encode(), p9, p10)
        



    @classmethod
    def create_ex(cls, p1, p2, p3, p4, p5, p6, p7, p8, p9):
        """
        This method makes a brand new database of the specified size.
        The database is opened in ReadWrite Mode. Also allows you to
        set paging size.
        """
        gxapi_cy.WrapDB.create_ex(GXContext._get_tls_geo(), p1.encode(), p2, p3, p4, p5, p6, p7.encode(), p8.encode(), p9)
        




    def del_line0(self):
        """
        Delete Empty Line 0.

        **Note:**

        A new database is created with a single, empty line L0, but many processes
        create databases then create their own lines, so the empty line L0 may remain
        after the process finishes. This function will delete a line L0
        a) If it exists and is empty
        b) It is not the only line in the database.
        """
        self._wrapper.del_line0()
        






    def discard(self):
        """
        This method discards all changes made to the database since
        the last commit or opening.
        """
        self._wrapper.discard()
        



    @classmethod
    def grow(cls, p1, p2, p3, p4, p5, p6):
        """
        Enlarges the database.
        """
        gxapi_cy.WrapDB.grow(GXContext._get_tls_geo(), p1.encode(), p2, p3, p4, p5, p6)
        



    @classmethod
    def can_open(cls, p1, p2, p3):
        """
        This method checks whether it is possible to open a database.

        **Note:**

        This method is useful to determine if another session already locked a database.
        By using this method before an Open_DB a GX may handle errors like this more gracefully.
        """
        ret_val = gxapi_cy.WrapDB.can_open(GXContext._get_tls_geo(), p1.encode(), p2.encode(), p3.encode())
        return ret_val



    @classmethod
    def can_open_read_only(cls, p1, p2, p3):
        """
        This method checks whether it is possible to open a database in read-only mode.

        **Note:**

        This method is useful to determine if another session already locked a database.
        By using this method before an OpenReadOnly_DB a GX may handle errors like this more gracefully.
        """
        ret_val = gxapi_cy.WrapDB.can_open_read_only(GXContext._get_tls_geo(), p1.encode(), p2.encode(), p3.encode())
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




    def is_line_empty(self, p2):
        """
        See if a specific line in the database is empty.
        """
        ret_val = self._wrapper.is_line_empty(p2)
        return ret_val



    @classmethod
    def open(cls, p1, p2, p3):
        """
        This method opens a database.
        """
        ret_val = gxapi_cy.WrapDB.open(GXContext._get_tls_geo(), p1.encode(), p2.encode(), p3.encode())
        return GXDB(ret_val)



    @classmethod
    def open_read_only(cls, p1, p2, p3):
        """
        This method opens a database.

        **Note:**

        This method is useful to open multiple reader instances on the same database. This call will fail
        if a :class:`geosoft.gxapi.GXDB` has already been opened with Open_DB or locked in the application with Lock_EDB.
        """
        ret_val = gxapi_cy.WrapDB.open_read_only(GXContext._get_tls_geo(), p1.encode(), p2.encode(), p3.encode())
        return GXDB(ret_val)



    @classmethod
    def repair(cls, p1):
        """
        Cleans the database by removing invalid blocks
        """
        gxapi_cy.WrapDB.repair(GXContext._get_tls_geo(), p1.encode())
        




    def sync(self):
        """
        Syncronize the Metadata from this database to the XML
        """
        self._wrapper.sync()
        




# Data



    def copy_data(self, p2, p3, p4):
        """
        This method copies the data from one channel to another on
        on the specified line. The data is converted if such
        conversion in neccessary.

        **Note:**

        All the data in the destination channel is destroyed along
        with the fiducial start and increment.
        """
        self._wrapper.copy_data(p2, p3, p4)
        




    def get_col_va(self, p2):
        """
        Returns the # of columns in a :class:`geosoft.gxapi.GXVA` channel.

        **Note:**

        If the channel is :class:`geosoft.gxapi.GXVV`, this function returns 1.
        """
        ret_val = self._wrapper.get_col_va(p2)
        return ret_val




    def get_channel_length(self, p2, p3):
        """
        Returns the # of elements in a channel.

        **Note:**

        Returns the actual number of data items (rows) in a channel. For :class:`geosoft.gxapi.GXVA` channels no correction is
        necessary for the number of columns (which was true of the obsoleted function iGetLength_DB).
        """
        ret_val = self._wrapper.get_channel_length(p2, p3)
        return ret_val




    def get_fid_incr(self, p2, p3):
        """
        This method returns the fiducial increment value of a
        specified Channel.
        """
        ret_val = self._wrapper.get_fid_incr(p2, p3)
        return ret_val




    def get_fid_start(self, p2, p3):
        """
        This method returns the fiducial start value of a
        specified Channel.
        """
        ret_val = self._wrapper.get_fid_start(p2, p3)
        return ret_val




    def set_fid(self, p2, p3, p4, p5):
        """
        This method allows the user to set the fiducial start and
        increment of a channel. The Increment should never be 0.
        """
        self._wrapper.set_fid(p2, p3, p4, p5)
        




    def window_va_ch(self, p2, p3, p4, p5, p6):
        """
        Copy a window of data in a channel into a new channel

        **Note:**

        This function normally used for :class:`geosoft.gxapi.GXVA` channels. A copy of the
        original channel will be made if start and end column
        numbers to copy are dummies.
        All the columns including start and end columns will be copied
        """
        self._wrapper.window_va_ch(p2, p3, p4, p5, p6)
        




    def window_va_ch2(self, p2, p3, p4, p5):
        """
        Copy a windowed version of data in a channel into a new channel

        **Note:**

        Similar to WindowVACh_DB, but the input and output channels must
        contain the same number of columns. The input :class:`geosoft.gxapi.GXVV` tells which columns
        to copy over; 0 values indicate that the output column is to be
        dummied, and non-zero values indicate the column is to be copied.
        The :class:`geosoft.gxapi.GXVV` length must be the same as the number of columns.
        """
        self._wrapper.window_va_ch2(p2, p3, p4, p5._wrapper)
        




# Line



    def set_line_selection(self, p2, p3):
        """
        Set the selection status for a line.
        """
        self._wrapper.set_line_selection(p2, p3)
        




    def get_line_selection(self, p2):
        """
        Get the selection status for a line.
        """
        ret_val = self._wrapper.get_line_selection(p2)
        return ret_val




    def first_sel_line(self):
        """
        This method will return a handle to the first selected
        line in the database.
        """
        ret_val = self._wrapper.first_sel_line()
        return ret_val




    def get_line_map_fid(self, p2, p3, p4):
        """
        This method gets a line map clip fiducial.

        **Note:**

        The channel must be locked :attr:`geosoft.gxapi.DB_LOCK_READONLY` or :attr:`geosoft.gxapi.DB_LOCK_READWRITE`
        """
        p3.value, p4.value = self._wrapper.get_line_map_fid(p2, p3.value, p4.value)
        




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
    def is_chan_name(cls, p1):
        """
        Is this a valid channel name?

        **Note:**

        Channel names must only contain alpha-numeric characters or the
        underscore character "_", and the first letter must be a letter
        or an underscore.
        """
        ret_val = gxapi_cy.WrapDB.is_chan_name(GXContext._get_tls_geo(), p1.encode())
        return ret_val




    def is_chan_valid(self, p2):
        """
        This method checks to see if the channel handle is a
        valid channel.
        """
        ret_val = self._wrapper.is_chan_valid(p2)
        return ret_val



    @classmethod
    def is_line_name(cls, p1):
        """
        Is this a valid line name.
        """
        ret_val = gxapi_cy.WrapDB.is_line_name(GXContext._get_tls_geo(), p1.encode())
        return ret_val




    def is_line_valid(self, p2):
        """
        This method checks to see if the line handle returned by
        the Line methods is a valid line.
        """
        ret_val = self._wrapper.is_line_valid(p2)
        return ret_val




    def line_category(self, p2):
        """
        This method returns the category (group, line) of a line.

        **Note:**

        The channel must be locked :attr:`geosoft.gxapi.DB_LOCK_READONLY` or :attr:`geosoft.gxapi.DB_LOCK_READWRITE`
        """
        ret_val = self._wrapper.line_category(p2)
        return ret_val




    def line_flight(self, p2):
        """
        This method returns the flight number of a line.

        **Note:**

        The channel must be locked :attr:`geosoft.gxapi.DB_LOCK_READONLY` or :attr:`geosoft.gxapi.DB_LOCK_READWRITE`
        """
        ret_val = self._wrapper.line_flight(p2)
        return ret_val




    def line_label(self, p2, p3, p5):
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
        p3.value = self._wrapper.line_label(p2, p3.value.encode(), p5)
        




    def line_number(self, p2):
        """
        This method returns the number of a line.

        **Note:**

        The channel must be locked :attr:`geosoft.gxapi.DB_LOCK_READONLY` or :attr:`geosoft.gxapi.DB_LOCK_READWRITE`
        """
        ret_val = self._wrapper.line_number(p2)
        return ret_val




    def line_number2(self, p2, p3):
        """
        Returns the string form of the line number (can be alphanumeric)

        **Note:**

        The channel must be locked :attr:`geosoft.gxapi.DB_LOCK_READONLY` or :attr:`geosoft.gxapi.DB_LOCK_READWRITE`
        """
        p3.value = self._wrapper.line_number2(p2, p3.value.encode())
        




    def line_type(self, p2):
        """
        This method returns the type of a line.

        **Note:**

        The channel must be locked :attr:`geosoft.gxapi.DB_LOCK_READONLY` or :attr:`geosoft.gxapi.DB_LOCK_READWRITE`
        """
        ret_val = self._wrapper.line_type(p2)
        return ret_val




    def line_version(self, p2):
        """
        This method returns the version number of a line.

        **Note:**

        The channel must be locked :attr:`geosoft.gxapi.DB_LOCK_READONLY` or :attr:`geosoft.gxapi.DB_LOCK_READWRITE`
        """
        ret_val = self._wrapper.line_version(p2)
        return ret_val



    @classmethod
    def set_line_name(cls, p1, p2, p3, p4):
        """
        This method sets up a line name given the line's number,
        type, and version.

        **Note:**

        This MUST be called to generate a line name when calls
        are made to iExistSymb_DB, CreateSymb_DB or DeleteSymb_DB
        for an operation on a line.
        See also SetLineName2_DB.
        """
        p4.value = gxapi_cy.WrapDB.set_line_name(GXContext._get_tls_geo(), p1, p2, p3, p4.value.encode())
        



    @classmethod
    def set_line_name2(cls, p1, p2, p3, p4):
        """
        Like SetLineName_DB, but can use alphanumeric for line number

        **Note:**

        This MUST be called to generate a line name when calls
        are made to iExistSymb_DB, CreateSymb_DB or DeleteSymb_DB
        for an operation on a line.
        The line number can be any combination of letters and numbers,
        i.e. XU324, 98765, A, 23NGV etc.
        """
        p4.value = gxapi_cy.WrapDB.set_line_name2(GXContext._get_tls_geo(), p1.encode(), p2, p3, p4.value.encode())
        




    def load_select(self, p2):
        """
        Load selections to from a file.
        """
        self._wrapper.load_select(p2.encode())
        




    def next_sel_line(self, p2):
        """
        This method will advance to the next selected line based
        on the currently selected line handle.
        """
        ret_val = self._wrapper.next_sel_line(p2)
        return ret_val




    def line_bearing(self, p2):
        """
        This method returns the bearing of a line.

        **Note:**

        The channel must be locked :attr:`geosoft.gxapi.DB_LOCK_READONLY` or :attr:`geosoft.gxapi.DB_LOCK_READWRITE`
        
        This function simply returns a value set using the SetLineBearing_DB
        function. It returns :attr:`geosoft.gxapi.rDUMMY` for line categories other than
        :attr:`geosoft.gxapi.DB_CATEGORY_LINE_FLIGHT`.
        
        To calculate the line azimuth based on the first and
        last non-dummy locations, use the rDirection_DU function.
        """
        ret_val = self._wrapper.line_bearing(p2)
        return ret_val




    def line_date(self, p2):
        """
        This method returns the date of a line.

        **Note:**

        The channel must be locked :attr:`geosoft.gxapi.DB_LOCK_READONLY` or :attr:`geosoft.gxapi.DB_LOCK_READWRITE`
        """
        ret_val = self._wrapper.line_date(p2)
        return ret_val




    def save_select(self, p2):
        """
        Saves current selections to a file.
        """
        self._wrapper.save_select(p2.encode())
        




    def select(self, p2, p3):
        """
        Select/deselect lines based on selection string

        **Note:**

        Selections/deselections are cumulative. If lines had already
        been selected, then any further selection/deselection will
        affect that set of selections.
        
        E.g. "L99:800" is the string to select all normal lines from
        99 to 800. If Select_DB is called again to select "L1000",
        then lines 99 to 800 and 1000 would all be selected.
        
        Use a "T" prefix for Tie lines.
        Use an "F" prefix to specify lines of a specific flight.
        E.g. "F10" would select all lines of flight 10.
        Use an empty string ("") to select/deselect ALL lines.
        """
        self._wrapper.select(p2.encode(), p3)
        




    def set_line_bearing(self, p2, p3):
        """
        Sets a line's bearing.

        **Note:**

        The channel must be locked :attr:`geosoft.gxapi.DB_LOCK_READWRITE`
        
        This function simply sets a value in the line's metadata
        that is retrieved using the rLineBearing_DB
        function. It terminates for line categories other than
        :attr:`geosoft.gxapi.DB_CATEGORY_LINE_FLIGHT`.
        """
        self._wrapper.set_line_bearing(p2, p3)
        




    def set_line_date(self, p2, p3):
        """
        This method sets a line's date.

        **Note:**

        The channel must be locked :attr:`geosoft.gxapi.DB_LOCK_READWRITE`
        """
        self._wrapper.set_line_date(p2, p3)
        




    def set_line_flight(self, p2, p3):
        """
        This method sets a line's flight.

        **Note:**

        The channel must be locked :attr:`geosoft.gxapi.DB_LOCK_READWRITE`
        """
        self._wrapper.set_line_flight(p2, p3)
        




    def set_line_map_fid(self, p2, p3, p4):
        """
        This method changes a line map clip fiducial.

        **Note:**

        for full range, set Start Fid to :attr:`geosoft.gxapi.rMIN` and End Fid to :attr:`geosoft.gxapi.rMAX`.
        for no data, set Start and End Fids to :attr:`geosoft.gxapi.rDUMMY`.
        """
        self._wrapper.set_line_map_fid(p2, p3, p4)
        




    def set_line_num(self, p2, p3):
        """
        This method sets a line's number.

        **Note:**

        The channel must be locked :attr:`geosoft.gxapi.DB_LOCK_READWRITE`
        """
        self._wrapper.set_line_num(p2, p3)
        




    def set_line_type(self, p2, p3):
        """
        This method sets a line's type.

        **Note:**

        The channel must be locked :attr:`geosoft.gxapi.DB_LOCK_READWRITE`
        """
        self._wrapper.set_line_type(p2, p3)
        




    def set_line_ver(self, p2, p3):
        """
        This method sets a line's version.

        **Note:**

        The channel must be locked :attr:`geosoft.gxapi.DB_LOCK_READWRITE`
        """
        self._wrapper.set_line_ver(p2, p3)
        




    def set_select(self, p2):
        """
        Sets the Line Selections.

        **Note:**

        This method also destroys the DB_SELECT object.
        """
        self._wrapper.set_select(p2)
        




# META



    def get_meta(self, p2):
        """
        Get the metadata of a database.
        """
        self._wrapper.get_meta(p2._wrapper)
        




    def set_meta(self, p2):
        """
        Set the metadata of a database.
        """
        self._wrapper.set_meta(p2._wrapper)
        




# Symbols



    def array_lst(self, p2):
        """
        Load a :class:`geosoft.gxapi.GXLST` object with array (:class:`geosoft.gxapi.GXVA`) channel symbols.
        """
        self._wrapper.array_lst(p2._wrapper)
        




    def array_size_lst(self, p2, p3):
        """
        Load a :class:`geosoft.gxapi.GXLST` object with array (:class:`geosoft.gxapi.GXVA`) channel symbols with a particular number of columns.
        """
        self._wrapper.array_size_lst(p2, p3._wrapper)
        




    def chan_lst(self, p2):
        """
        Load a :class:`geosoft.gxapi.GXLST` with database channels.

        **Note:**

        Populates a :class:`geosoft.gxapi.GXLST` with channel symbols.
        The name is put into the "Name" part of the :class:`geosoft.gxapi.GXLST` (0),
        and the handle, an integer value written as a string, is
        placed in the value part of the :class:`geosoft.gxapi.GXLST` (1).
        Array channels are included, as well as virtual channels (array channel single columns loaded in the database like \\"Chan[1]\\".
        
        The :class:`geosoft.gxapi.GXLST` is cleared first, and the items are sorted by name.
        """
        self._wrapper.chan_lst(p2._wrapper)
        




    def normal_chan_lst(self, p2):
        """
        Load a :class:`geosoft.gxapi.GXLST` with non-array database channels.

        **Note:**

        Like ChanLST_DB, but does not include array channels or virtual channels.
        """
        self._wrapper.normal_chan_lst(p2._wrapper)
        




    def class_chan_lst(self, p2, p3):
        """
        Load a :class:`geosoft.gxapi.GXLST` with channels in a particular class.

        **Note:**

        The Name of the symbol is placed in the
        item name and the item value is set to the symbol handle.
        Only channels with the given class name are included,
        e.g. use "ASSAY" for assay channels in :class:`geosoft.gxapi.GXCHIMERA`.
        
        The :class:`geosoft.gxapi.GXLST` is cleared first, and the items are sorted by name.
        """
        self._wrapper.class_chan_lst(p2._wrapper, p3.encode())
        




    def class_group_lst(self, p2, p3):
        """
        Load a :class:`geosoft.gxapi.GXLST` with group lines in a particular class.

        **Note:**

        The Name of the symbol is placed in the
        item name and the item value is set to the symbol handle.
        Only group lines with the given class name are included,
        e.g. use "TARGETS" for UX-Detect Target groups.
        
        The :class:`geosoft.gxapi.GXLST` is cleared first, and the items are sorted by name.
        """
        self._wrapper.class_group_lst(p2._wrapper, p3.encode())
        




    def create_symb(self, p2, p3, p4, p5):
        """
        Create a new Symbol.

        **Note:**

        If symbol already exits, and it is the same type
        simply returns a handle to the existing symbol.
        
        This method simple calls CreateSymbEx_DB with the
        extra info set to 1.
        
        STRING-type channels: To create a string-type channel,
        enter a negative number for the channel category below.
        For instance, "-32" will create a string channel with
        32 characters per item.
        
        BLOBS: Blobs (Binary Large Objects) can be used for storing
        miscellaneous data which does not fit well into any of the
        other various storage objects, such as a :class:`geosoft.gxapi.GXREG`. Generally,
        one or more objects is serialized to a :class:`geosoft.gxapi.GXBF` object, which
        is then written to the blob using the sWriteBlobBF_DB()
        function. Retrieval is done in the reverse order, using
        sWriteBlobBF_DB() first, then extracting the objects from the
        :class:`geosoft.gxapi.GXBF` object.
        To avoid namespace problems, Geosoft reserves the following
        name prefixes:
        
        OE.   (Core functions)
        GS.   (Applications)
        CS.   (Custom Solutions applications)
        
        Programmers should avoid using the above prefixes as the starting
        letters of their blob names to avoid any possible conflicts.
        """
        ret_val = self._wrapper.create_symb(p2.encode(), p3, p4, p5)
        return ret_val




    def create_symb_ex(self, p2, p3, p4, p5, p6):
        """
        Create a new Symbol.

        **Note:**

        If symbol already exits it is returned.
        
        STRING-type channels: To create a string-type channel,
        enter a negative number for the channel category below.
        For instance, "-32" will create a string channel with
        32 characters per item.
        
        Symbol name for :attr:`geosoft.gxapi.DB_CATEGORY_LINE_FLIGHT` must conform to
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
        
        The ability to create a :class:`geosoft.gxapi.GXVA` channel is not available in the
        free interface and requires a Montaj license.
        """
        ret_val = self._wrapper.create_symb_ex(p2.encode(), p3, p4, p5, p6)
        return ret_val




    def csv_chan_lst(self, p2, p3):
        """
        Load a :class:`geosoft.gxapi.GXLST` with channels in a comma-separated list.

        **Note:**

        The Name of the symbol is placed in the
        item name and the item value is set to the symbol handle.
        Only channels in the list which are present in the database
        are included.
        
        The :class:`geosoft.gxapi.GXLST` is cleared first.
        """
        self._wrapper.csv_chan_lst(p2._wrapper, p3.encode())
        




    def delete_symb(self, p2):
        """
        This method destroys a symbol in the database and all
        the data associated with it. The symbol's lock is
        automatically removed.
        """
        self._wrapper.delete_symb(p2)
        




    def dup_line_symb(self, p2, p3):
        """
        Duplicate a line symbol from a group or line symbol.
        The new name must not already exist in the database.
        """
        ret_val = self._wrapper.dup_line_symb(p2, p3.encode())
        return ret_val




    def dup_symb(self, p2, p3):
        """
        New Symbol by duplicating an existing symbol, LOCKED

        **Note:**

        The symbol will be locked READWRITE.
        The new name must not already exist in the database.
        """
        ret_val = self._wrapper.dup_symb(p2, p3.encode())
        return ret_val




    def dup_symb_no_lock(self, p2, p3):
        """
        New Symbol by duplicating an existing symbol, NO LOCK.

        **Note:**

        The symbol will be NOT be locked.
        The new name must not already exist in the database.
        """
        ret_val = self._wrapper.dup_symb_no_lock(p2, p3.encode())
        return ret_val




    def find_chan(self, p2):
        """
        Get handle to the specified channel.

        **Note:**

        To work with a specific column from a :class:`geosoft.gxapi.GXVA` channel,
        specify the :class:`geosoft.gxapi.GXVA` element number in square brackets as part
        of the :class:`geosoft.gxapi.GXVA` channel name (e.g. "EM[3]" will treat the fourth
        column of the :class:`geosoft.gxapi.GXVA` channel as a :class:`geosoft.gxapi.GXVV`).
        
        See notes for FindSymb_DB.
        Introduced in v5.1.3.
        The new FindChan_DB searches using the exact channel name.
        """
        ret_val = self._wrapper.find_chan(p2.encode())
        return ret_val




    def find_symb(self, p2, p3):
        """
        Get handle to the specified symbol.

        **Note:**

        To work with a specific column from a :class:`geosoft.gxapi.GXVA` channel,
        specify the :class:`geosoft.gxapi.GXVA` element number in square brackets as part
        of the :class:`geosoft.gxapi.GXVA` channel name (e.g. "EM[3]" will treat the fourth
        column of the :class:`geosoft.gxapi.GXVA` channel as a :class:`geosoft.gxapi.GXVV`).
        
        For backward compatibility with GXs not employing the
        GetXYZChanSymb_DB function, the following behaviour has
        been introduced as of v5.1.3:  (also true for "Y").
        
        FindSymb_DB(hDB, "X", :attr:`geosoft.gxapi.DB_SYMB_CHAN`) is now equivalent to:
        
        GetXYZChanSymb_DB(hDB, :attr:`geosoft.gxapi.DB_CHAN_X`);
        
        In other words, the current X or Y is searched for, not
        necessarily the literal "X" or "Y". This ensures that newer
        databases, which might have "Easting" and "Northing"
        (or other similar names) instead of "X" and "Y" will still
        work with older GXs expecting "X" and "Y".
        
        The new FindChan_DB searches using the exact channel name.
        """
        ret_val = self._wrapper.find_symb(p2.encode(), p3)
        return ret_val




    def get_chan_order_lst(self, p2):
        """
        This method gets the channel display order for a
        database. The list will be stored in an :class:`geosoft.gxapi.GXLST` object.
        In order to modify this displayed channels list,
        call SetChanOrderLST_DB after.
        """
        self._wrapper.get_chan_order_lst(p2._wrapper)
        




    def get_xyz_chan_symb(self, p2):
        """
        Searches for current X, Y or Z channel symbol
        """
        ret_val = self._wrapper.get_xyz_chan_symb(p2)
        return ret_val




    def class_chan_list(self, p2, p3):
        """
        Place a list of channels for a given class in a :class:`geosoft.gxapi.GXVV`.

        **Note:**

        This method generates a list of symbols in the database
        and places their handles into a :class:`geosoft.gxapi.GXVV`. The list is not
        sorted.
        Only channels with the given class name are included,
        e.g. use "ASSAY" for assay channels used in :class:`geosoft.gxapi.GXCHIMERA`.
        """
        ret_val = self._wrapper.class_chan_list(p2._wrapper, p3.encode())
        return ret_val




    def exist_chan(self, p2):
        """
        See if the specified channel exists in the database.

        **Note:**

        See notes for iExistSymb_DB.
        Introduced in v5.1.3.
        iExistChan_DB searches using the exact channel name.
        """
        ret_val = self._wrapper.exist_chan(p2.encode())
        return ret_val




    def exist_symb(self, p2, p3):
        """
        This method checks to see if the specified symbol exists
        in the database.

        **Note:**

        For backward compatibility with GXs not employing the
        GetXYZChan_DB function, the following behaviour has
        been introduced as of v5.1.3:  (also true for "Y").
        
        iExistSymb_DB(hDB, "X", :attr:`geosoft.gxapi.DB_SYMB_CHAN`) is now equivalent to:
        
        GetXYZChan_DB(hDB, :attr:`geosoft.gxapi.DB_CHAN_X`, sXCh);
        iExistSymb_DB(hDB, sXCh, :attr:`geosoft.gxapi.DB_SYMB_CHAN`);
        
        In other words, the current X or Y is searched for, not
        necessarily the literal "X" or "Y". This ensures that newer
        databases, which might have "Easting" and "Northing"
        (or other similar names) instead of "X" and "Y" will still
        work with older GXs expecting "X" and "Y".
        
        The new iExistChan_DB searches using the exact channel name.
        """
        ret_val = self._wrapper.exist_symb(p2.encode(), p3)
        return ret_val




    def valid_symb(self, p2, p3):
        """
        This method checks to see if the specified symbol is a valid symbol in the database.
        """
        ret_val = self._wrapper.valid_symb(p2, p3)
        return ret_val




    def get_symb_lock(self, p2):
        """
        Determines if a symbol is locked
        """
        ret_val = self._wrapper.get_symb_lock(p2)
        return ret_val




    def get_xyz_chan(self, p2, p3):
        """
        Gets current X, Y or Z channel name

        **Note:**

        searches for the "current" X, Y or Z channel.
        If none is defined, then returns "X", "Y" or "Z".
        """
        p3.value = self._wrapper.get_xyz_chan(p2, p3.value.encode())
        




    def symb_list(self, p2, p3):
        """
        Place a list of symbols in a :class:`geosoft.gxapi.GXVV`.
        """
        ret_val = self._wrapper.symb_list(p2._wrapper, p3)
        return ret_val




    def line_lst(self, p2):
        """
        Load a :class:`geosoft.gxapi.GXLST` with database lines.

        **Note:**

        Populates a :class:`geosoft.gxapi.GXLST` with channel symbols.
        The name is put into the "Name" part of the :class:`geosoft.gxapi.GXLST` (0),
        and the handle, an integer value written as a string, is
        placed in the value part of the :class:`geosoft.gxapi.GXLST` (1).
        The :class:`geosoft.gxapi.GXLST` is cleared first, and the items are sorted in logical line order.
        """
        self._wrapper.line_lst(p2._wrapper)
        




    def lock_symb(self, p2, p3, p4):
        """
        Locks a symbol for READONLY or READWRITE.
        """
        self._wrapper.lock_symb(p2, p3, p4)
        




    def mask_chan_lst(self, p2):
        """
        Load a :class:`geosoft.gxapi.GXLST` with mask channels.

        **Note:**

        Loads a :class:`geosoft.gxapi.GXLST` with all channels with CLASS "MASK", as well
        as all channels containing the string "MASK", as long
        as the CLASS for these channels is not set to something
        other than "" or "MASK".
        
        This function is a duplicate of the MaskChanLST_CHIMERA
        function, and can be used if :class:`geosoft.gxapi.GXCHIMERA` is not installed.
        
        The :class:`geosoft.gxapi.GXLST` is cleared first, and the items are sorted by name.
        "None" is added at the end, with a handle value of "-1".
        """
        self._wrapper.mask_chan_lst(p2._wrapper)
        




    def selected_line_lst(self, p2):
        """
        Load a :class:`geosoft.gxapi.GXLST` with the selected lines.

        **Note:**

        This method populates a :class:`geosoft.gxapi.GXLST` object with all of the symbols
        of the selected lines in the database.
        The name is put into the "Name" part of the :class:`geosoft.gxapi.GXLST` (0),
        and the handle, an integer value written as a string, is
        placed in the value part of the :class:`geosoft.gxapi.GXLST` (1).
        
        Symbols are automatically sorted in logical line order.
        """
        self._wrapper.selected_line_lst(p2._wrapper)
        




    def set_chan_order_lst(self, p2):
        """
        This method sets the channel display order for a
        database. The list to modify will be stored in an :class:`geosoft.gxapi.GXLST`
        object. Call GetChanOrderLST_DB to populate the :class:`geosoft.gxapi.GXLST`.
        """
        self._wrapper.set_chan_order_lst(p2._wrapper)
        




    def set_xyz_chan(self, p2, p3):
        """
        Sets current X, Y or Z channel name

        **Note:**

        If the value specified is "", the internally stored value
        is cleared, and GetXYZChan_DB will return "X", "Y" or "Z"
        
        This can be used, for instance, to make "Easting" and "Northing"
        the current X and Y channels, and have GXs using the
        GetXYZChanSymb_DB function to load "X" and "Y" work as desired.
        """
        self._wrapper.set_xyz_chan(p2, p3.encode())
        




    def string_chan_lst(self, p2):
        """
        Load a :class:`geosoft.gxapi.GXLST` with string-type channels.

        **Note:**

        The Name of the symbol is placed in the
        item name and the item value is set to the symbol handle.
        Only channels with the string-type data (sChanType_DB < 0)
        are included.
        
        The :class:`geosoft.gxapi.GXLST` is cleared first, and the items are sorted by name.
        """
        self._wrapper.string_chan_lst(p2._wrapper)
        




    def symb_lst(self, p2, p3):
        """
        Populate a :class:`geosoft.gxapi.GXLST` with database symbols.

        **Note:**

        Populates a :class:`geosoft.gxapi.GXLST` with channel, line, blob or user symbols.
        The name is put into the "Name" part of the :class:`geosoft.gxapi.GXLST` (0),
        and the handle, an integer value written as a string, is
        placed in the value part of the :class:`geosoft.gxapi.GXLST` (1).
        
        Line symbols are automatically sorted in logical line order.
        
        NOTE: The :class:`geosoft.gxapi.GXLST` is NOT cleared before being filled. If you
        want to clear the :class:`geosoft.gxapi.GXLST` and get sorted values, use the
        ChanLST_DB and LineLST_DB functions.
        """
        self._wrapper.symb_lst(p2._wrapper, p3)
        




    def un_lock_all_symb(self):
        """
        UnLocks all symbols.
        """
        self._wrapper.un_lock_all_symb()
        




    def un_lock_symb(self, p2):
        """
        UnLocks a symbol.
        """
        self._wrapper.un_lock_symb(p2)
        




# VA Channels



    def add_associated_load(self, p2, p3):
        """
        Add this channel to the auto-load feature of the group.

        **Note:**

        If the channel is not yet associated, it is first associated.
        If the channel is already in the associated-load list, this
        does nothing.
        
        As of v6.0, the load-status of channels is no longer stored
        in the database, but in the project, so this function is
        equivalent to calling Associate_DB.
        """
        self._wrapper.add_associated_load(p2, p3)
        




    def add_comment(self, p2, p3, p4):
        """
        Add a comment with a string to the activity log of the database.

        **Note:**

        The comment is written in the form:
        
        Comment: String2
        
        and is followed by a carriage return.
        The activity log is created automatically if it does not exist.
        """
        self._wrapper.add_comment(p2.encode(), p3.encode(), p4)
        




    def add_int_comment(self, p2, p3, p4):
        """
        Add a comment with an integer to the activity log of the database.

        **Note:**

        The comment is written in the form:
        
        Comment: Value
        
        and is followed by a carriage return.
        The activity log is created automatically if it does not exist.
        
        See Notes in AddComment_DB.
        """
        self._wrapper.add_int_comment(p2.encode(), p3, p4)
        




    def add_double_comment(self, p2, p3, p4):
        """
        Add a comment with a float value to the activity log of the database.

        **Note:**

        The comment is written in the form:
        
        Comment: Value
        
        and if followed by a carriage return.
        The activity log is created automatically if it does not exist.
        
        See Notes in AddComment_DB.
        """
        self._wrapper.add_double_comment(p2.encode(), p3, p4)
        




    def add_time_comment(self, p2, p3):
        """
        Add a comment with the date and time to the activity log of the database.

        **Note:**

        The comment is written in the form:
        
        Comment: 2001/12/31 23:59:59
        
        and is followed by a carriage return.
        The activity log is created automatically if it does not exist.
        
        See Notes in AddComment_DB.
        """
        self._wrapper.add_time_comment(p2.encode(), p3)
        




    def associate(self, p2, p3):
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
        self._wrapper.associate(p2, p3)
        




    def associate_all(self, p2):
        """
        Associate all channels with a group.

        **Note:**

        As of v6.3, if a group line has no class defined, then ALL
        channels are already assumed to be associated with it, and this
        function does nothing.
        """
        self._wrapper.associate_all(p2)
        




    def associate_class(self, p2, p3):
        """
        Associate a channel with all groups of a specific class.

        **Note:**

        As of v6.3, if a group line has no class defined, then ALL
        channels are automatically assumed to be associated with it.
        """
        self._wrapper.associate_class(p2, p3.encode())
        



    @classmethod
    def gen_valid_chan_symb(cls, p1, p2):
        """
        Generate a valid channel name from a name candidate
        """
        p2.value = gxapi_cy.WrapDB.gen_valid_chan_symb(GXContext._get_tls_geo(), p1.encode(), p2.value.encode())
        



    @classmethod
    def gen_valid_line_symb(cls, p1, p2):
        """
        Generate a valid line symb name string from given string.

        **Note:**

        The returned name is either the same size as the input
        or shorter. Escapes, leading and trailing spaces are removed, then
        all illegal characters are replaced with an underscore.
        """
        p2.value = gxapi_cy.WrapDB.gen_valid_line_symb(GXContext._get_tls_geo(), p1.encode(), p2.value.encode())
        




    def get_chan_va(self, p2, p3, p4):
        """
        Place the contents of a channel in a :class:`geosoft.gxapi.GXVA`.
        """
        self._wrapper.get_chan_va(p2, p3, p4._wrapper)
        




    def get_va_scaling(self, p2, p3, p4):
        """
        Get base and range for :class:`geosoft.gxapi.GXVA` channel cell display.

        **Note:**

        See SetVAScaling_DB.
        """
        p3.value, p4.value = self._wrapper.get_va_scaling(p2, p3.value, p4.value)
        




    def get_va_windows(self, p2, p3, p4):
        """
        Get the range of windows displayed for a :class:`geosoft.gxapi.GXVA` channel.

        **Note:**

        See SetVAWindows_DB.
        """
        p3.value, p4.value = self._wrapper.get_va_windows(p2, p3.value, p4.value)
        




    def set_va_base_coordinate_info(self, p2, p3, p4, p5, p6, p7):
        """
        Set the array channel base coordinate type, offset and values.

        **Note:**

        See GetVABaseCoordinateInfo_DB.
        """
        self._wrapper.set_va_base_coordinate_info(p2, p3, p4, p5._wrapper, p6.encode(), p7)
        




    def get_va_base_coordinate_info(self, p2, p3, p4, p5, p6):
        """
        Set the array channel base coordinate type, offset and values.

        **Note:**

        See SetVABaseCoordinateInfo_DB.
        """
        p3.value, p4.value, p6.value = self._wrapper.get_va_base_coordinate_info(p2, p3.value, p4.value, p5._wrapper, p6.value.encode())
        




    def get_group_class(self, p2, p3):
        """
        Set the Class name for a group line.

        **Note:**

        This method fails if the line is not a group line.
        Group classes are used to identify group lines used for
        special purposes, e.g.: "COLLAR" for the Wholeplot collar table,
        or "TARGETS" for the UX-Detect Targets list.
        """
        p3.value = self._wrapper.get_group_class(p2, p3.value.encode())
        




    def get_info(self, p2):
        """
        Get information about the database.
        """
        ret_val = self._wrapper.get_info(p2)
        return ret_val




    def get_va_prof_color_file(self, p2, p3):
        """
        Get colors for a :class:`geosoft.gxapi.GXVA` channel when displayed in the profile window.

        **Note:**

        See SetVAProfColorFile_DB.
        """
        p3.value = self._wrapper.get_va_prof_color_file(p2, p3.value.encode())
        




    def get_va_prof_sect_option(self, p2, p3):
        """
        Get the display options of :class:`geosoft.gxapi.GXVA` channels
        """
        p3.value = self._wrapper.get_va_prof_sect_option(p2, p3.value.encode())
        




    def get_va_sect_color_file(self, p2, p3):
        """
        Get colors for a :class:`geosoft.gxapi.GXVA` channel when displayed section in the profile window.

        **Note:**

        Fails in the channel is not an array channel
        """
        p3.value = self._wrapper.get_va_sect_color_file(p2, p3.value.encode())
        




    def is_associated(self, p2, p3):
        """
        Check to see if a channel is associated with group.
        """
        ret_val = self._wrapper.is_associated(p2, p3)
        return ret_val




    def is_wholeplot(self):
        """
        Is this a Wholeplot database?

        **Note:**

        Currently checks to see if the DH_COLLAR line exists.
        """
        ret_val = self._wrapper.is_wholeplot()
        return ret_val




    def put_chan_va(self, p2, p3, p4):
        """
        Place the contents of a :class:`geosoft.gxapi.GXVA` in a channel.
        """
        self._wrapper.put_chan_va(p2, p3, p4._wrapper)
        




    def set_group_class(self, p2, p3):
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
        """
        self._wrapper.set_group_class(p2, p3.encode())
        




    def set_va_prof_color_file(self, p2, p3):
        """
        Set colors for a :class:`geosoft.gxapi.GXVA` channel when displayed in the profile window.

        **Note:**

        Fails in the channel is not an array channel, if the
        file does not exist, or if it is not a valid color zone file.
        
        The individual columns in the array channel are displayed using the input
        zone file colors. A linear :class:`geosoft.gxapi.GXITR` from 0 to 1 is created on the color zones
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
        self._wrapper.set_va_prof_color_file(p2, p3.encode())
        




    def set_va_prof_sect_option(self, p2, p3):
        """
        Set the display options of :class:`geosoft.gxapi.GXVA` channels
        """
        self._wrapper.set_va_prof_sect_option(p2, p3.encode())
        




    def set_va_scaling(self, p2, p3, p4):
        """
        Set base and range for :class:`geosoft.gxapi.GXVA` channel cell display.

        **Note:**

        By default, :class:`geosoft.gxapi.GXVA` profiles autoscale to fit in the database cell.
        This lets the user set a single base and range for all cells.
        If either input is a dummy, both are set as dummies, and autoscaling
        is used.
        """
        self._wrapper.set_va_scaling(p2, p3, p4)
        




    def set_va_sect_color_file(self, p2, p3):
        """
        Set colors for a :class:`geosoft.gxapi.GXVA` channel when displayed section in the profile window.

        **Note:**

        Fails in the channel is not an array channel, if the
        file does not exist, or if it is not a valid color zone file.
        """
        self._wrapper.set_va_sect_color_file(p2, p3.encode())
        




    def set_va_windows(self, p2, p3, p4):
        """
        Set the range of windows to display for a :class:`geosoft.gxapi.GXVA` channel.

        **Note:**

        Use to display a subset of the :class:`geosoft.gxapi.GXVA` channel windows in the GDB.
        Windows index from 0.
        """
        self._wrapper.set_va_windows(p2, p3, p4)
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer