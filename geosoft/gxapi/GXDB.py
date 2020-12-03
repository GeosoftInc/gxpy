### extends 'class_empty.py'
### block ClassImports
# NOTICE: Do not edit anything here, it is generated code
from . import gxapi_cy
from geosoft.gxapi import GXContext, float_ref, int_ref, str_ref
from .GXLST import GXLST


### endblock ClassImports

### block Header
# NOTICE: The code generator will not replace the code in this block
### endblock Header

### block ClassImplementation
# NOTICE: Do not edit anything here, it is generated code
class GXDB(gxapi_cy.WrapDB):
    """
    GXDB class.

    The `GXDB <geosoft.gxapi.GXDB>` class is used to create, open and work with databases and database symbols.
    Database symbols are objects inside databases, such as lines, channels and blobs

    **Note:**

    The following defines are not used by any methods but are
    used by GX's:

    `DB_ACTIVITY_BLOB <geosoft.gxapi.DB_ACTIVITY_BLOB>`
    """

    def __init__(self, handle=0):
        super(GXDB, self).__init__(GXContext._get_tls_geo(), handle)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of `GXDB <geosoft.gxapi.GXDB>`
        
        :returns: A null `GXDB <geosoft.gxapi.GXDB>`
        :rtype:   GXDB
        """
        return GXDB()

    def is_null(self):
        """
        Check if this is a null (undefined) instance
        
        :returns: True if this is a null (undefined) instance, False otherwise.
        :rtype:   bool
        """
        return self._internal_handle() == 0



# Channel



    def create_dup(self, file):
        """
        This method makes a brand new database identical to the input
        Database in-size.
        The database is opened in ReadWrite Mode.
        
        :param file:  Name of the Database File to Create
        :type  file:  str

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._create_dup(file.encode())
        




    def create_dup_comp(self, file, level):
        """
        This method makes a brand new database identical to the input
        Database in-size except it changes the compression.
        The database is opened in ReadWrite Mode.
        
        :param file:   Name of the Database File to Create
        :param level:  :ref:`DB_COMP`
        :type  file:   str
        :type  level:  int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._create_dup_comp(file.encode(), level)
        




    def dup_symb_across(self, dbo, symb):
        """
        Create a new Symbol by duplicating an existing symbol.
        exactly the same type but in output database. The symbol must
        not already exist in the output database.
        
        :param dbo:   Database output
        :param symb:  Symbol Handle to duplicate
        :type  dbo:   GXDB
        :type  symb:  int

        :returns:     New Symbol Handle
        :rtype:       int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = self._dup_symb_across(dbo, symb)
        return ret_val




    def easy_maker_symb(self, symb, name, groups):
        """
        Adds a Maker to the database symbol based on current GX
        
        :param symb:    Symbol to create maker for
        :param name:    Maker name, used in menu prompt
        :param groups:  INI groups (terminate each with a ";")
        :type  symb:    int
        :type  name:    str
        :type  groups:  str

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._easy_maker_symb(symb, name.encode(), groups.encode())
        




    def get_chan_str(self, line, chan, ind, str_val):
        """
        Get individual elements in a channel.
        
        :param line:     Line
        :param chan:     Channel
        :param ind:      Index
        :param str_val:  String
        :type  line:     int
        :type  chan:     int
        :type  ind:      int
        :type  str_val:  str_ref

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** These methods are slow and should only be used when
        performance is not an issue.
        """
        str_val.value = self._get_chan_str(line, chan, ind, str_val.value.encode())
        




    def get_chan_vv(self, line, chan, vv):
        """
        Place the contents of a channel in a `GXVV <geosoft.gxapi.GXVV>`.
        
        :param line:  Line
        :param chan:  Channel
        :param vv:    `GXVV <geosoft.gxapi.GXVV>` in which to place the data
        :type  line:  int
        :type  chan:  int
        :type  vv:    GXVV

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** If a `GXVA <geosoft.gxapi.GXVA>` channel is specified, then element [0] of this
        `GXVA <geosoft.gxapi.GXVA>` channel is used to populated the `GXVV <geosoft.gxapi.GXVV>`.

        .. seealso::

            `GXVV <geosoft.gxapi.GXVV>` class.
        """
        self._get_chan_vv(line, chan, vv)
        




    def get_chan_vv_expanded(self, line, chan, vv):
        """
        Read a channel into a `GXVV <geosoft.gxapi.GXVV>`. If the channel is a `GXVA <geosoft.gxapi.GXVA>` channel it is
        treaded as a `GXVV <geosoft.gxapi.GXVV>` channel with multiple values per fid and the FID expation
        is set to the array size.
        
        :param line:  Line
        :param chan:  Channel
        :param vv:    `GXVV <geosoft.gxapi.GXVV>` in which to place the data
        :type  line:  int
        :type  chan:  int
        :type  vv:    GXVV

        .. versionadded:: 6.4

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** This method is to be used in conjunction with the `GXVV.re_fid_vv <geosoft.gxapi.GXVV.re_fid_vv>` method
        that will honor the FID Expansion setting.

        .. seealso::

            `GXVV <geosoft.gxapi.GXVV>` class.
        """
        self._get_chan_vv_expanded(line, chan, vv)
        




    def get_ipj(self, ch, ipj):
        """
        Get georeference information in an `GXIPJ <geosoft.gxapi.GXIPJ>`.
        
        :param ch:   Symbol
        :param ipj:  `GXIPJ <geosoft.gxapi.GXIPJ>` to fill in
        :type  ch:   int
        :type  ipj:  GXIPJ

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** If the channel does not have an `GXIPJ <geosoft.gxapi.GXIPJ>`, the `GXIPJ <geosoft.gxapi.GXIPJ>` that is
        returned will have an unknown projection.
        """
        self._get_ipj(ch, ipj)
        




    def get_itr(self, ch, itr):
        """
        Get `GXITR <geosoft.gxapi.GXITR>` for a channel.
        
        :param ch:   Channel
        :param itr:  `GXITR <geosoft.gxapi.GXITR>` to fill in
        :type  ch:   int
        :type  itr:  GXITR

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** If a channel does not have an `GXITR <geosoft.gxapi.GXITR>`, `get_itr <geosoft.gxapi.GXDB.get_itr>` will not change
        the passed `GXITR <geosoft.gxapi.GXITR>`.
        Channel must be locked for READONLY or READWRITE.
        """
        self._get_itr(ch, itr)
        




    def get_reg_symb(self, symb, reg):
        """
        Get a `GXREG <geosoft.gxapi.GXREG>` object from a symbol
        
        :param symb:  Symbol, `NULLSYMB <geosoft.gxapi.NULLSYMB>` for the database `GXREG <geosoft.gxapi.GXREG>`
        :param reg:   `GXREG <geosoft.gxapi.GXREG>` to copy data into
        :type  symb:  int
        :type  reg:   GXREG

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._get_reg_symb(symb, reg)
        




    def get_reg_symb_setting(self, symb, name, setting):
        """
        Get a `GXREG <geosoft.gxapi.GXREG>` string setting from a symbol reg
        
        :param symb:     Symbol, `NULLSYMB <geosoft.gxapi.NULLSYMB>` for the database `GXREG <geosoft.gxapi.GXREG>`
        :param name:     `GXREG <geosoft.gxapi.GXREG>` entry name
        :param setting:  Returned setting
        :type  symb:     int
        :type  name:     str
        :type  setting:  str_ref

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** The symbol `GXREG <geosoft.gxapi.GXREG>` is used to store a variety of attribute
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
        setting.value = self._get_reg_symb_setting(symb, name.encode(), setting.value.encode())
        




    def get_va_chan_vv(self, line, chan, vv, offset, items):
        """
        Place the contents of a specific part of a channel in a `GXVV <geosoft.gxapi.GXVV>`.
        
        :param line:    Line
        :param chan:    Channel
        :param vv:      `GXVV <geosoft.gxapi.GXVV>` in which to place the data
        :param offset:  Offset
        :param items:   Number to Write
        :type  line:    int
        :type  chan:    int
        :type  vv:      GXVV
        :type  offset:  int
        :type  items:   int

        .. versionadded:: 5.1.1

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** If a `GXVA <geosoft.gxapi.GXVA>` channel is specified, then element [0] of this
        `GXVA <geosoft.gxapi.GXVA>` channel is used to populated the `GXVV <geosoft.gxapi.GXVV>`.

        .. seealso::

            `GXVV <geosoft.gxapi.GXVV>` class.
        """
        self._get_va_chan_vv(line, chan, vv, offset, items)
        




    def blobs_max(self):
        """
        Gets Maximum Number of Blobs in the Database
        

        :returns:    Maximum Number of Blobs in the Database
        :rtype:      int

        .. versionadded:: 5.1.1

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = self._blobs_max()
        return ret_val




    def chans_max(self):
        """
        Gets Maximum Number of Channels in the Database
        

        :returns:    Maximum Number of Channels in the Database
        :rtype:      int

        .. versionadded:: 5.1.1

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = self._chans_max()
        return ret_val




    def format_chan(self, chan, val, str_val):
        """
        Format a real value based on a channel format.
        
        :param chan:     Channel handle
        :param val:      Value to format
        :param str_val:  String
        :type  chan:     int
        :type  val:      float
        :type  str_val:  str_ref

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** If the passed string is too short, the result will be
        "**".
        """
        str_val.value = self._format_chan(chan, val, str_val.value.encode())
        




    def get_chan_array_size(self, chan):
        """
        This method Gets a channel's array size for a
        given channel handle.
        
        :param chan:  Channel handle
        :type  chan:  int

        :returns:     Channel type
        :rtype:       int

        .. versionadded:: 6.0.1

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = self._get_chan_array_size(chan)
        return ret_val




    def get_chan_class(self, chan, cl):
        """
        This method gets a channel's label
        
        :param chan:  Channel handle
        :param cl:    Returned class into
        :type  chan:  int
        :type  cl:    str_ref

        .. versionadded:: 5.1.8

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** The channel label is stored in the "CLASS" parameter
        of the channel reg. If no class is defined, then an
        empty string is returned.
        The channel must be locked `DB_LOCK_READONLY <geosoft.gxapi.DB_LOCK_READONLY>` or `DB_LOCK_READWRITE <geosoft.gxapi.DB_LOCK_READWRITE>`
        """
        cl.value = self._get_chan_class(chan, cl.value.encode())
        




    def get_chan_decimal(self, chan):
        """
        This method gets a channel's number of digits displayed
        to the right of the decimal point.
        
        :param chan:  Channel handle
        :type  chan:  int

        :returns:     Number of digits displayed to right of decimal
        :rtype:       int

        .. versionadded:: 6.0.1

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** The channel must be locked `DB_LOCK_READONLY <geosoft.gxapi.DB_LOCK_READONLY>` or `DB_LOCK_READWRITE <geosoft.gxapi.DB_LOCK_READWRITE>`
        """
        ret_val = self._get_chan_decimal(chan)
        return ret_val




    def get_chan_format(self, chan):
        """
        This method Gets a channel's display format for a
        given channel handle.
        
        :param chan:  Channel handle
        :type  chan:  int

        :returns:     Channel display format
        :rtype:       int

        .. versionadded:: 6.0.1

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** The returned format is one of the :ref:`DB_CHAN_FORMAT`.
        The channel must be locked `DB_LOCK_READONLY <geosoft.gxapi.DB_LOCK_READONLY>` or `DB_LOCK_READWRITE <geosoft.gxapi.DB_LOCK_READWRITE>`
        """
        ret_val = self._get_chan_format(chan)
        return ret_val




    def get_chan_int(self, line, chan, ind):
        """
        Get individual elements in a channel.
        
        :param line:  Line
        :param chan:  Channel
        :param ind:   Index
        :type  line:  int
        :type  chan:  int
        :type  ind:   int

        :returns:     Value, or dummy if out of range.
                      For settings, terminates if error.
        :rtype:       int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** These methods are slow and should only be used when
        performance is not an issue.
        """
        ret_val = self._get_chan_int(line, chan, ind)
        return ret_val




    def get_chan_label(self, chan, label):
        """
        This method gets a channel's label
        
        :param chan:   Channel handle
        :param label:  Returned label into
        :type  chan:   int
        :type  label:  str_ref

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** The channel label is stored in the "LABEL" parameter
        of the channel reg.  If the setting is empty, the
        channel name is returned.
        The channel must be locked `DB_LOCK_READONLY <geosoft.gxapi.DB_LOCK_READONLY>` or `DB_LOCK_READWRITE <geosoft.gxapi.DB_LOCK_READWRITE>`
        """
        label.value = self._get_chan_label(chan, label.value.encode())
        




    def get_chan_name(self, chan, name):
        """
        This method Gets a channel's name for a
        given channel handle.
        
        :param chan:  Channel handle
        :param name:  String to place name into
        :type  chan:  int
        :type  name:  str_ref

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** The channel must be locked `DB_LOCK_READONLY <geosoft.gxapi.DB_LOCK_READONLY>` or `DB_LOCK_READWRITE <geosoft.gxapi.DB_LOCK_READWRITE>`
        """
        name.value = self._get_chan_name(chan, name.value.encode())
        




    def get_chan_protect(self, chan):
        """
        This method gets a channel's read-only protection status.
        
        :param chan:  Channel handle
        :type  chan:  int

        :returns:     :ref:`DB_CHAN_PROTECTION`
        :rtype:       int

        .. versionadded:: 6.0.1

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** The channel must be locked `DB_LOCK_READONLY <geosoft.gxapi.DB_LOCK_READONLY>` or `DB_LOCK_READWRITE <geosoft.gxapi.DB_LOCK_READWRITE>`
        """
        ret_val = self._get_chan_protect(chan)
        return ret_val




    def get_chan_type(self, chan):
        """
        This method Gets a channel's type for a
        given channel handle.
        
        :param chan:  Channel handle
        :type  chan:  int

        :returns:     Channel type
        :rtype:       int

        .. versionadded:: 6.0.1

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** The type returned is one of the :ref:`DB_CATEGORY_CHAN`.
        Use the GS_SIMPLE_TYPE() macro to convert to INT,REAL
        or string types.
        The channel must be locked `DB_LOCK_READONLY <geosoft.gxapi.DB_LOCK_READONLY>` or `DB_LOCK_READWRITE <geosoft.gxapi.DB_LOCK_READWRITE>`
        """
        ret_val = self._get_chan_type(chan)
        return ret_val




    def get_chan_unit(self, chan, unit):
        """
        This method Gets a channel's unit
        
        :param chan:  Channel handle
        :param unit:  String to place unit into
        :type  chan:  int
        :type  unit:  str_ref

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** The unit label is stored in the "UNITS" parameter
        of the channel reg.
        The channel must be locked `DB_LOCK_READONLY <geosoft.gxapi.DB_LOCK_READONLY>` or `DB_LOCK_READWRITE <geosoft.gxapi.DB_LOCK_READWRITE>`
        """
        unit.value = self._get_chan_unit(chan, unit.value.encode())
        




    def get_chan_width(self, chan):
        """
        This method gets a channel's display width for a
        given channel handle.
        
        :param chan:  Channel handle
        :type  chan:  int

        :returns:     Channel display width
        :rtype:       int

        .. versionadded:: 6.0.1

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** The channel must be locked `DB_LOCK_READONLY <geosoft.gxapi.DB_LOCK_READONLY>` or `DB_LOCK_READWRITE <geosoft.gxapi.DB_LOCK_READWRITE>`
        """
        ret_val = self._get_chan_width(chan)
        return ret_val




    def get_name(self, name, psz_name):
        """
        Gets a name from the database.
        
        :param name:      :ref:`DB_NAME`
        :param psz_name:  Name returned
        :type  name:      int
        :type  psz_name:  str_ref

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        psz_name.value = self._get_name(name, psz_name.value.encode())
        




    def get_reg_symb_setting_int(self, symb, name):
        """
        Get an integer-valued `GXREG <geosoft.gxapi.GXREG>` setting from a symbol reg
        
        :param symb:  Symbol, `NULLSYMB <geosoft.gxapi.NULLSYMB>` for the database `GXREG <geosoft.gxapi.GXREG>`
        :param name:  `GXREG <geosoft.gxapi.GXREG>` entry name
        :type  symb:  int
        :type  name:  str

        :returns:     The setting, or `iDUMMY <geosoft.gxapi.iDUMMY>` if not found or not convertable.
        :rtype:       int

        .. versionadded:: 6.2

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Same as `get_reg_symb_setting <geosoft.gxapi.GXDB.get_reg_symb_setting>`, but converts
        the setting automatically to an integer value.

        This is a convenient but low-performance way to get/set `GXREG <geosoft.gxapi.GXREG>`
        settings.  If performance is an issue, and more than one
        setting is to be Get and or Set, use the `GXREG <geosoft.gxapi.GXREG>` directly.
        """
        ret_val = self._get_reg_symb_setting_int(symb, name.encode())
        return ret_val




    def get_symb_name(self, symb, name):
        """
        This method gets a symbol's name
        
        :param symb:  Symbol handle
        :param name:  String to place name into
        :type  symb:  int
        :type  name:  str_ref

        .. versionadded:: 6.1

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** See GetChanName_DB for more information
        The channel must be locked `DB_LOCK_READONLY <geosoft.gxapi.DB_LOCK_READONLY>` or `DB_LOCK_READWRITE <geosoft.gxapi.DB_LOCK_READWRITE>`
        """
        name.value = self._get_symb_name(symb, name.value.encode())
        




    def have_itr(self, ch):
        """
        Returns TRUE if channel has an `GXITR <geosoft.gxapi.GXITR>`.
        
        :param ch:  Channel
        :type  ch:  int
        :rtype:      int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** If a channel has an `GXITR <geosoft.gxapi.GXITR>`, the `GXITR <geosoft.gxapi.GXITR>` colors are used to
        display channel values in the spreadsheet.

        If a channel does not have an `GXITR <geosoft.gxapi.GXITR>`, `get_itr <geosoft.gxapi.GXDB.get_itr>` will not change
        the passed `GXITR <geosoft.gxapi.GXITR>`.
        """
        ret_val = self._have_itr(ch)
        return ret_val




    def coord_pair(self, chan, pair):
        """
        Get the matching coordinate pair of a channel.
        
        :param chan:  Channel name
        :param pair:  String in which to place paired channel name
        :type  chan:  str
        :type  pair:  str_ref

        :returns:     :ref:`DB_COORDPAIR`
        :rtype:       int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** If the channel does not have a matching coordinate
        pair, or of the channel does not exist, the returned
        string will be empty.
        """
        ret_val, pair.value = self._coord_pair(chan.encode(), pair.value.encode())
        return ret_val




    def lines_max(self):
        """
        Gets Maximum number of lines in the database
        

        :returns:    Maximum number of lines in the database
        :rtype:      int

        .. versionadded:: 5.1.1

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = self._lines_max()
        return ret_val




    def users_max(self):
        """
        Gets Maximum number of Users
        

        :returns:    Maximum number of Users
        :rtype:      int

        .. versionadded:: 5.1.1

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = self._users_max()
        return ret_val




    def maker_symb(self, symb, prog, name, groups):
        """
        Adds a Maker to the database symbol
        
        :param symb:    Symbol to create maker for
        :param prog:    Name of program
        :param name:    Maker name, used in menu prompt
        :param groups:  INI groups (terminate each with a ";")
        :type  symb:    int
        :type  prog:    str
        :type  name:    str
        :type  groups:  str

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._maker_symb(symb, prog.encode(), name.encode(), groups.encode())
        




    def put_chan_vv(self, line, chan, vv):
        """
        Place the contents of a `GXVV <geosoft.gxapi.GXVV>` in a channel.
        
        :param line:  Line
        :param chan:  Channel
        :param vv:    `GXVV <geosoft.gxapi.GXVV>` from which to get the data
        :type  line:  int
        :type  chan:  int
        :type  vv:    GXVV

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** If a `GXVA <geosoft.gxapi.GXVA>` channel is specified, then element [0] of this
        `GXVA <geosoft.gxapi.GXVA>` channel will be populated with the `GXVV <geosoft.gxapi.GXVV>`.

        There is a limit of 2000 elements for non-licensed users.

        .. seealso::

            `GXVV <geosoft.gxapi.GXVV>` class.
        """
        self._put_chan_vv(line, chan, vv)
        




    def put_va_chan_vv(self, line, chan, vv, offset, items):
        """
        Place the contents of a `GXVV <geosoft.gxapi.GXVV>` at a specific part of a channel.
        
        :param line:    Line
        :param chan:    Channel
        :param vv:      `GXVV <geosoft.gxapi.GXVV>` from which to get the data
        :param offset:  Offset
        :param items:   Number to Write
        :type  line:    int
        :type  chan:    int
        :type  vv:      GXVV
        :type  offset:  int
        :type  items:   int

        .. versionadded:: 5.1.1

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** If a `GXVA <geosoft.gxapi.GXVA>` channel is specified, then element [0] of this
        `GXVA <geosoft.gxapi.GXVA>` channel will be populated with the `GXVV <geosoft.gxapi.GXVV>`.

        .. seealso::

            `GXVV <geosoft.gxapi.GXVV>` class.
        """
        self._put_va_chan_vv(line, chan, vv, offset, items)
        




    def read_blob_bf(self, symb, bf):
        """
        Read a blob from a database into a file.
        
        :param symb:  Blob (`DB_SYMB_BLOB <geosoft.gxapi.DB_SYMB_BLOB>`) to read into `GXBF <geosoft.gxapi.GXBF>` from database
        :param bf:    File to read blob from
        :type  symb:  int
        :type  bf:    GXBF

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._read_blob_bf(symb, bf)
        




    def get_chan_double(self, line, chan, ind):
        """
        Get individual elements in a channel.
        
        :param line:  Line
        :param chan:  Channel
        :param ind:   Index
        :type  line:  int
        :type  chan:  int
        :type  ind:   int

        :returns:     Value, or dummy if out of range.
                      For settings, terminates if error.
        :rtype:       float

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** These methods are slow and should only be used when
        performance is not an issue.
        """
        ret_val = self._get_chan_double(line, chan, ind)
        return ret_val




    def get_reg_symb_setting_double(self, symb, name):
        """
        Get a real-valued `GXREG <geosoft.gxapi.GXREG>` setting from a symbol reg
        
        :param symb:  Symbol, `NULLSYMB <geosoft.gxapi.NULLSYMB>` for the database `GXREG <geosoft.gxapi.GXREG>`
        :param name:  `GXREG <geosoft.gxapi.GXREG>` entry name
        :type  symb:  int
        :type  name:  str

        :returns:     The setting, or `rDUMMY <geosoft.gxapi.rDUMMY>` if not found or not convertable.
        :rtype:       float

        .. versionadded:: 6.2

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Same as `get_reg_symb_setting <geosoft.gxapi.GXDB.get_reg_symb_setting>`, but converts
        the setting automatically to a real value.

        This is a convenient but low-performance way to get/set `GXREG <geosoft.gxapi.GXREG>`
        settings.  If performance is an issue, and more than one
        setting is to be Get and or Set, use the `GXREG <geosoft.gxapi.GXREG>` directly.
        """
        ret_val = self._get_reg_symb_setting_double(symb, name.encode())
        return ret_val




    def set_all_chan_protect(self, prot):
        """
        This method sets all the channels' read-only protection status.
        
        :param prot:  :ref:`DB_CHAN_PROTECTION`
        :type  prot:  int

        .. versionadded:: 7.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Value to set must be either `DB_CHAN_PROTECTED <geosoft.gxapi.DB_CHAN_PROTECTED>` or
        `DB_CHAN_UNPROTECTED <geosoft.gxapi.DB_CHAN_UNPROTECTED>`
        This method does its own channel locking/unlocking.
        Channels already lock `DB_LOCK_READONLY <geosoft.gxapi.DB_LOCK_READONLY>` are ignored.
        """
        self._set_all_chan_protect(prot)
        




    def set_chan_class(self, chan, cl):
        """
        Set a channel class
        
        :param chan:  Channel handle
        :param cl:    Class
        :type  chan:  int
        :type  cl:    str

        .. versionadded:: 5.1.8

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** The channel class is stored in the "CLASS" parameter
        of the channel reg.
        The channel must be locked `DB_LOCK_READWRITE <geosoft.gxapi.DB_LOCK_READWRITE>`
        """
        self._set_chan_class(chan, cl.encode())
        




    def set_chan_decimal(self, chan, dec):
        """
        This method sets a channel's number of digits displayed
        to the right of the decimal point.
        
        :param chan:  Channel handle
        :param dec:   Number of digits to display right of the decimal
        :type  chan:  int
        :type  dec:   int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** The number of display digits must be from 0 to 50.
        The channel must be locked `DB_LOCK_READWRITE <geosoft.gxapi.DB_LOCK_READWRITE>`
        """
        self._set_chan_decimal(chan, dec)
        




    def set_chan_format(self, chan, format):
        """
        This method sets a channel's display format.
        
        :param chan:    Channel handle
        :param format:  :ref:`DB_CHAN_FORMAT`
        :type  chan:    int
        :type  format:  int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** The channel must be locked `DB_LOCK_READWRITE <geosoft.gxapi.DB_LOCK_READWRITE>`
        """
        self._set_chan_format(chan, format)
        




    def set_chan_int(self, line, chan, ind, val):
        """
        Set individual elements in a channel.
        
        :param line:  Line
        :param chan:  Channel
        :param ind:   Index
        :param val:   Value
        :type  line:  int
        :type  chan:  int
        :type  ind:   int
        :type  val:   int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** These methods are slow and should only be used when
        performance is not an issue.
        """
        self._set_chan_int(line, chan, ind, val)
        




    def set_chan_label(self, chan, label):
        """
        Set a channel label
        
        :param chan:   Channel handle
        :param label:  Label
        :type  chan:   int
        :type  label:  str

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** The channel label is stored in the "LABEL" parameter
        of the channel reg.
        The channel must be locked `DB_LOCK_READWRITE <geosoft.gxapi.DB_LOCK_READWRITE>`
        """
        self._set_chan_label(chan, label.encode())
        




    def set_chan_name(self, chan, name):
        """
        This method sets a channel's name.
        
        :param chan:  Channel handle
        :param name:  String to set channel name to
        :type  chan:  int
        :type  name:  str

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** The channel must be locked `DB_LOCK_READWRITE <geosoft.gxapi.DB_LOCK_READWRITE>`
        """
        self._set_chan_name(chan, name.encode())
        




    def set_chan_protect(self, chan, prot):
        """
        This method sets a channel's read-only protection
        status.
        
        :param chan:  Channel handle
        :param prot:  :ref:`DB_CHAN_PROTECTION`
        :type  chan:  int
        :type  prot:  int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Value to set must be either `DB_CHAN_PROTECTED <geosoft.gxapi.DB_CHAN_PROTECTED>` or
        `DB_CHAN_UNPROTECTED <geosoft.gxapi.DB_CHAN_UNPROTECTED>`
        The channel must be locked `DB_LOCK_READWRITE <geosoft.gxapi.DB_LOCK_READWRITE>`
        """
        self._set_chan_protect(chan, prot)
        




    def set_chan_double(self, line, chan, ind, val):
        """
        Set individual elements in a channel.
        
        :param line:  Line
        :param chan:  Channel
        :param ind:   Index
        :param val:   Value
        :type  line:  int
        :type  chan:  int
        :type  ind:   int
        :type  val:   float

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** These methods are slow and should only be used when
        performance is not an issue.
        """
        self._set_chan_double(line, chan, ind, val)
        




    def set_chan_str(self, line, chan, ind, str_val):
        """
        Set individual elements in a channel.
        
        :param line:     Line
        :param chan:     Channel
        :param ind:      Index
        :param str_val:  String
        :type  line:     int
        :type  chan:     int
        :type  ind:      int
        :type  str_val:  str

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** These methods are slow and should only be used when
        performance is not an issue.
        """
        self._set_chan_str(line, chan, ind, str_val.encode())
        




    def set_chan_unit(self, chan, unit):
        """
        This method sets a channel's unit for a
        given channel handle.
        
        :param chan:  Channel handle
        :param unit:  String to put channel unit
        :type  chan:  int
        :type  unit:  str

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** The channel must be locked `DB_LOCK_READWRITE <geosoft.gxapi.DB_LOCK_READWRITE>`
        """
        self._set_chan_unit(chan, unit.encode())
        




    def set_chan_width(self, chan, width):
        """
        This method sets a channel's display width
        
        :param chan:   Channel handle
        :param width:  Display width
        :type  chan:   int
        :type  width:  int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** The number of display digits must be from 0 to 50.
        The channel must be locked `DB_LOCK_READWRITE <geosoft.gxapi.DB_LOCK_READWRITE>`
        """
        self._set_chan_width(chan, width)
        




    def set_ipj(self, ch1, ch2, ipj):
        """
        Set a `GXREG <geosoft.gxapi.GXREG>` object into a symbol
        
        :param ch1:  X channel
        :param ch2:  Y channel
        :type  ch1:  int
        :type  ch2:  int
        :type  ipj:  GXIPJ

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._set_ipj(ch1, ch2, ipj)
        




    def set_itr(self, ch, itr):
        """
        Set `GXITR <geosoft.gxapi.GXITR>` for a channel.
        
        :param ch:   Channel
        :param itr:  `GXITR <geosoft.gxapi.GXITR>` to fill in
        :type  ch:   int
        :type  itr:  GXITR

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Use `ITR_NULL <geosoft.gxapi.ITR_NULL>` to clear the channel `GXITR <geosoft.gxapi.GXITR>`.
        Channel must be locked for READONLY or READWRITE.
        """
        self._set_itr(ch, itr)
        




    def set_reg_symb(self, symb, reg):
        """
        Set a `GXREG <geosoft.gxapi.GXREG>` object into a symbol
        
        :param symb:  Symbol, `NULLSYMB <geosoft.gxapi.NULLSYMB>` for the database `GXREG <geosoft.gxapi.GXREG>`
        :param reg:   `GXREG <geosoft.gxapi.GXREG>` to set into Blob
        :type  symb:  int
        :type  reg:   GXREG

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._set_reg_symb(symb, reg)
        




    def set_reg_symb_setting(self, symb, name, setting):
        """
        Set a `GXREG <geosoft.gxapi.GXREG>` string setting in a symbol reg
        
        :param symb:     Symbol, `NULLSYMB <geosoft.gxapi.NULLSYMB>` for the database `GXREG <geosoft.gxapi.GXREG>`
        :param name:     `GXREG <geosoft.gxapi.GXREG>` entry name
        :param setting:  Setting
        :type  symb:     int
        :type  name:     str
        :type  setting:  str

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** The symbol `GXREG <geosoft.gxapi.GXREG>` is used to store a variety of attribute
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
        self._set_reg_symb_setting(symb, name.encode(), setting.encode())
        




    def write_blob_bf(self, symb, bf):
        """
        Write a blob from a file into a database.
        
        :param symb:  Blob (`DB_SYMB_BLOB <geosoft.gxapi.DB_SYMB_BLOB>`) to write into database from file
        :param bf:    File to write blob into
        :type  symb:  int
        :type  bf:    GXBF

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._write_blob_bf(symb, bf)
        




# Control



    def commit(self):
        """
        This method forces all changes to the database to be saved.
        

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._commit()
        




    def compact(self):
        """
        Removes any extra space from the database. This will
        reduce the database to its smallest size.
        

        .. versionadded:: 5.1.1

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._compact()
        



    @classmethod
    def create(cls, file, lines, chans, blobs, users, cache, super, password):
        """
        This method makes a brand new database of the specified size.
        The database is opened in ReadWrite Mode.
        
        :param file:      Name of the Database File to Create
        :param lines:     Max Lines in the Database    (200)
        :param chans:     Max Channels in the Database (50)
        :param blobs:     Max Blobs in the Database    (Channels+Lines+20)
        :param users:     Max Users in the Database    (10)
        :param cache:     Number of Erase Caches       (100)
        :param super:     Name of the Super User       "SUPER"
        :param password:  Password of the Super User   ""
        :type  file:      str
        :type  lines:     int
        :type  chans:     int
        :type  blobs:     int
        :type  users:     int
        :type  cache:     int
        :type  super:     str
        :type  password:  str

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        gxapi_cy.WrapDB._create(GXContext._get_tls_geo(), file.encode(), lines, chans, blobs, users, cache, super.encode(), password.encode())
        



    @classmethod
    def create_comp(cls, file, lines, chans, blobs, users, cache, super, password, page, level):
        """
        This method makes a brand new database of the specified size.
        The database is opened in ReadWrite Mode. Also allows you to
        set paging size and the Compression Level.
        
        :param file:      Name of the Database File to Create
        :param lines:     Max Lines in the Database    (200)
        :param chans:     Max Channels in the Database (50)
        :param blobs:     Max Blobs in the Database    (Channels+Lines+20)
        :param users:     Max Users in the Database    (10)
        :param cache:     Number of Erase Caches       (100)
        :param super:     Name of the Super User       "SUPER"
        :param password:  Password of the Super User   ""
        :param page:      Page Size Must be (64,128,256,512,1024,2048,4096) normally 1024
        :param level:     :ref:`DB_COMP`
        :type  file:      str
        :type  lines:     int
        :type  chans:     int
        :type  blobs:     int
        :type  users:     int
        :type  cache:     int
        :type  super:     str
        :type  password:  str
        :type  page:      int
        :type  level:     int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        gxapi_cy.WrapDB._create_comp(GXContext._get_tls_geo(), file.encode(), lines, chans, blobs, users, cache, super.encode(), password.encode(), page, level)
        



    @classmethod
    def create_ex(cls, file, lines, chans, blobs, users, cache, super, password, page):
        """
        This method makes a brand new database of the specified size.
        The database is opened in ReadWrite Mode. Also allows you to
        set paging size.
        
        :param file:      Name of the Database File to Create
        :param lines:     Max Lines in the Database    (200)
        :param chans:     Max Channels in the Database (50)
        :param blobs:     Max Blobs in the Database    (Channels+Lines+20)
        :param users:     Max Users in the Database    (10)
        :param cache:     Number of Erase Caches       (100)
        :param super:     Name of the Super User       "SUPER"
        :param password:  Password of the Super User   ""
        :param page:      Page Size Must be (64,128,256,512,1024,2048,4096) normally 1024
        :type  file:      str
        :type  lines:     int
        :type  chans:     int
        :type  blobs:     int
        :type  users:     int
        :type  cache:     int
        :type  super:     str
        :type  password:  str
        :type  page:      int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        gxapi_cy.WrapDB._create_ex(GXContext._get_tls_geo(), file.encode(), lines, chans, blobs, users, cache, super.encode(), password.encode(), page)
        




    def del_line0(self):
        """
        Delete Empty Line 0.
        

        .. versionadded:: 7.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** A new database is created with a single, empty line L0, but many processes
        create databases then create their own lines, so the empty line L0 may remain
        after the process finishes. This function will delete a line L0
        a) If it exists and is empty
        b) It is not the only line in the database.

        .. seealso::

            `GXEDB.del_line0 <geosoft.gxapi.GXEDB.del_line0>` - deletes an empty line 0 from the currently edited database.
        """
        self._del_line0()
        






    def discard(self):
        """
        This method discards all changes made to the database since
        the last commit or opening.
        

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._discard()
        



    @classmethod
    def grow(cls, file, lines, chans, blobs, users, cache):
        """
        Enlarges the database.
        
        :param file:   Name of the Database File to Create
        :param lines:  Max Lines in the Database    (200)
        :param chans:  Max Channels in the Database (50)
        :param blobs:  Max Blobs in the Database    (Channels+Lines+20)
        :param users:  Max Users in the Database    (10)
        :param cache:  Number of Erase Caches       (100)
        :type  file:   str
        :type  lines:  int
        :type  chans:  int
        :type  blobs:  int
        :type  users:  int
        :type  cache:  int

        .. versionadded:: 5.1.1

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        gxapi_cy.WrapDB._grow(GXContext._get_tls_geo(), file.encode(), lines, chans, blobs, users, cache)
        



    @classmethod
    def can_open(cls, file, user, password):
        """
        This method checks whether it is possible to open a database.
        
        :param file:      Name of the Database File to Open
        :param user:      Name of the user ("SUPER" normally)
        :param password:  Password of the user ("" normally)
        :type  file:      str
        :type  user:      str
        :type  password:  str
        :rtype:           bool

        .. versionadded:: 6.1

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** This method is useful to determine if another session already locked a database.
        By using this method before an `open <geosoft.gxapi.GXDB.open>` a GX may handle errors like this more gracefully.

        .. seealso::

            `open <geosoft.gxapi.GXDB.open>`, `open_read_only <geosoft.gxapi.GXDB.open_read_only>`, `can_open_read_only <geosoft.gxapi.GXDB.can_open_read_only>`
        """
        ret_val = gxapi_cy.WrapDB._can_open(GXContext._get_tls_geo(), file.encode(), user.encode(), password.encode())
        return ret_val



    @classmethod
    def can_open_read_only(cls, file, user, password):
        """
        This method checks whether it is possible to open a database in read-only mode.
        
        :param file:      Name of the Database File to Open
        :param user:      Name of the user ("SUPER" normally)
        :param password:  Password of the user ("" normally)
        :type  file:      str
        :type  user:      str
        :type  password:  str
        :rtype:           bool

        .. versionadded:: 6.4.2

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** This method is useful to determine if another session already locked a database.
        By using this method before an `open_read_only <geosoft.gxapi.GXDB.open_read_only>` a GX may handle errors like this more gracefully.

        .. seealso::

            `open <geosoft.gxapi.GXDB.open>`, `open_read_only <geosoft.gxapi.GXDB.open_read_only>`, `can_open <geosoft.gxapi.GXDB.can_open>`
        """
        ret_val = gxapi_cy.WrapDB._can_open_read_only(GXContext._get_tls_geo(), file.encode(), user.encode(), password.encode())
        return ret_val




    def check(self):
        """
        Does an integrity check of the data in the database to
        ensure it is valid.
        

        :returns:    0 - Ok
                    1 - Invalid Blocks in the Database
        :rtype:      int

        .. versionadded:: 6.0.1

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = self._check()
        return ret_val




    def is_empty(self):
        """
        See if a database contains only empty lines.
        

        :returns:    1 if the database contains only empty lines.
        :rtype:      int

        .. versionadded:: 6.1

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** This function does not check for other information or blobs,
        it merely looks at all lines in the database to see if they
        are empty. If all are empty, it returns 1.
        """
        ret_val = self._is_empty()
        return ret_val




    def is_line_empty(self, symb):
        """
        See if a specific line in the database is empty.
        
        :param symb:  Line symbol
        :type  symb:  int

        :returns:     1 if the database contains only empty lines.
        :rtype:       int

        .. versionadded:: 6.1

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = self._is_line_empty(symb)
        return ret_val



    @classmethod
    def open(cls, file, user, password):
        """
        This method opens a database.
        
        :param file:      Name of the Database File to Open
        :param user:      Name of the user ("SUPER" normally)
        :param password:  Password of the user ("" normally)
        :type  file:      str
        :type  user:      str
        :type  password:  str

        :returns:         `GXDB <geosoft.gxapi.GXDB>` Object
        :rtype:           GXDB

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        .. seealso::

            `open_read_only <geosoft.gxapi.GXDB.open_read_only>`, `can_open <geosoft.gxapi.GXDB.can_open>`, `can_open_read_only <geosoft.gxapi.GXDB.can_open_read_only>`
        """
        ret_val = gxapi_cy.WrapDB._open(GXContext._get_tls_geo(), file.encode(), user.encode(), password.encode())
        return GXDB(ret_val)



    @classmethod
    def open_read_only(cls, file, user, password):
        """
        This method opens a database.
        
        :param file:      Name of the Database File to Open
        :param user:      Name of the user ("SUPER" normally)
        :param password:  Password of the user ("" normally)
        :type  file:      str
        :type  user:      str
        :type  password:  str

        :returns:         `GXDB <geosoft.gxapi.GXDB>` Object
        :rtype:           GXDB

        .. versionadded:: 6.4.2

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** This method is useful to open multiple reader instances on the same database. This call will fail
        if a `GXDB <geosoft.gxapi.GXDB>` has already been opened with `open <geosoft.gxapi.GXDB.open>` or locked in the application with `GXEDB.lock <geosoft.gxapi.GXEDB.lock>`.

        .. seealso::

            `open <geosoft.gxapi.GXDB.open>`, `can_open <geosoft.gxapi.GXDB.can_open>`, `can_open_read_only <geosoft.gxapi.GXDB.can_open_read_only>`
        """
        ret_val = gxapi_cy.WrapDB._open_read_only(GXContext._get_tls_geo(), file.encode(), user.encode(), password.encode())
        return GXDB(ret_val)



    @classmethod
    def repair(cls, file):
        """
        Cleans the database by removing invalid blocks
        
        :param file:  Name of the Database File to Create
        :type  file:  str

        .. versionadded:: 5.1.1

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        gxapi_cy.WrapDB._repair(GXContext._get_tls_geo(), file.encode())
        




    def sync(self):
        """
        Syncronize the Metadata from this database to the XML
        

        .. versionadded:: 7.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._sync()
        




# Data



    def copy_data(self, line, i_chan, o_chan):
        """
        This method copies the data from one channel to another on
        on the specified line. The data is converted if such
        conversion in neccessary.
        
        :param line:    Line
        :param i_chan:  Channel to Copy Data From
        :param o_chan:  Channel to Copy Data To
        :type  line:    int
        :type  i_chan:  int
        :type  o_chan:  int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** All the data in the destination channel is destroyed along
        with the fiducial start and increment.
        """
        self._copy_data(line, i_chan, o_chan)
        




    def get_col_va(self, chan):
        """
        Returns the # of columns in a `GXVA <geosoft.gxapi.GXVA>` channel.
        
        :param chan:  Channel (read locked)
        :type  chan:  int

        :returns:     # of columns
                      0 if error
        :rtype:       int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** If the channel is `GXVV <geosoft.gxapi.GXVV>`, this function returns 1.
        """
        ret_val = self._get_col_va(chan)
        return ret_val




    def get_channel_length(self, line, chan):
        """
        Returns the # of elements in a channel.
        
        :param line:  Line    (read or write locked)
        :param chan:  Channel (read or write locked)
        :type  line:  int
        :type  chan:  int

        :returns:     # of elements
        :rtype:       int

        .. versionadded:: 8.1

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Returns the actual number of data items (rows) in a channel. For `GXVA <geosoft.gxapi.GXVA>` channels no correction is
        necessary for the number of columns.
        """
        ret_val = self._get_channel_length(line, chan)
        return ret_val




    def get_fid_incr(self, line, chan):
        """
        This method returns the fiducial increment value of a
        specified Channel.
        
        :param line:  Line (read or write locked)
        :param chan:  Channel (read locked)
        :type  line:  int
        :type  chan:  int

        :returns:     Fiducial Start.
        :rtype:       float

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = self._get_fid_incr(line, chan)
        return ret_val




    def get_fid_start(self, line, chan):
        """
        This method returns the fiducial start value of a
        specified Channel.
        
        :param line:  Line (read or write locked)
        :param chan:  Channel (read locked)
        :type  line:  int
        :type  chan:  int

        :returns:     Fiducial Start.
        :rtype:       float

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = self._get_fid_start(line, chan)
        return ret_val




    def set_fid(self, line, chan, start, incr):
        """
        This method allows the user to set the fiducial start and
        increment of a channel. The Increment should never be 0.
        
        :param line:   Line (read or write locked)
        :param chan:   Channel to set fiducial (write locked)
        :param start:  Start Fiducial Value
        :param incr:   Increment Fiducial Value
        :type  line:   int
        :type  chan:   int
        :type  start:  float
        :type  incr:   float

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._set_fid(line, chan, start, incr)
        




    def window_va_ch(self, line, i_ch, o_ch, col_s, col_e):
        """
        Copy a window of data in a channel into a new channel
        
        :param line:   Line symbol
        :param i_ch:   Original channel
        :param o_ch:   Output channel
        :param col_s:  Start column number to copy, 0 is first column
        :param col_e:  End column number to copy
        :type  line:   int
        :type  i_ch:   int
        :type  o_ch:   int
        :type  col_s:  int
        :type  col_e:  int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** This function normally used for `GXVA <geosoft.gxapi.GXVA>` channels. A copy of the
        original channel will be made if start and end column
        numbers to copy are dummies.
        All the columns including start and end columns will be copied
        """
        self._window_va_ch(line, i_ch, o_ch, col_s, col_e)
        




    def window_va_ch2(self, line, i_ch, o_ch, gvv):
        """
        Copy a windowed version of data in a channel into a new channel
        
        :param line:  Line symbol
        :param i_ch:  Original channel
        :param o_ch:  Output channel
        :param gvv:   `GXVV <geosoft.gxapi.GXVV>` containing 0/1 values for each channel.
        :type  line:  int
        :type  i_ch:  int
        :type  o_ch:  int
        :type  gvv:   GXVV

        .. versionadded:: 5.0.1

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Similar to `window_va_ch <geosoft.gxapi.GXDB.window_va_ch>`, but the input and output channels must
        contain the same number of columns. The input `GXVV <geosoft.gxapi.GXVV>` tells which columns
        to copy over; 0 values indicate that the output column is to be
        dummied, and non-zero values indicate the column is to be copied.
        The `GXVV <geosoft.gxapi.GXVV>` length must be the same as the number of columns.
        """
        self._window_va_ch2(line, i_ch, o_ch, gvv)
        




# Line



    def set_line_selection(self, line, mode):
        """
        Set the selection status for a line.
        
        :param line:  Handle of line to select/deselect
        :param mode:  :ref:`DB_LINE_SELECT`
        :type  line:  int
        :type  mode:  int

        .. versionadded:: 9.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._set_line_selection(line, mode)
        




    def get_line_selection(self, line):
        """
        Get the selection status for a line.
        
        :param line:  Line handle
        :type  line:  int

        :returns:     One of :ref:`DB_LINE_SELECT`
        :rtype:       int

        .. versionadded:: 9.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = self._get_line_selection(line)
        return ret_val




    def first_sel_line(self):
        """
        This method will return a handle to the first selected
        line in the database.
        

        :returns:    Line Handle (use iIsLineValid method to see if valid)
        :rtype:      int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = self._first_sel_line()
        return ret_val




    def get_line_map_fid(self, line, start, end):
        """
        This method gets a line map clip fiducial.
        
        :param line:   Line handle to look at
        :param start:  Start Fid
        :param end:    End Fid
        :type  line:   int
        :type  start:  float_ref
        :type  end:    float_ref

        .. versionadded:: 5.1.1

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** The channel must be locked `DB_LOCK_READONLY <geosoft.gxapi.DB_LOCK_READONLY>` or `DB_LOCK_READWRITE <geosoft.gxapi.DB_LOCK_READWRITE>`
        """
        start.value, end.value = self._get_line_map_fid(line, start.value, end.value)
        




    def get_select(self):
        """
        Gets the Line Selections.
        

        :returns:    Selections Object.
        :rtype:      int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = self._get_select()
        return ret_val




    def count_sel_lines(self):
        """
        This method counts the number of selected lines in
        the database.
        

        :returns:    x - Number of selected lines in the database
        :rtype:      int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = self._count_sel_lines()
        return ret_val



    @classmethod
    def is_chan_name(cls, chan):
        """
        Is this a valid channel name?
        
        :param chan:  Name to test
        :type  chan:  str

        :returns:     1 if it is a valid channel name
                      0 if it is not a valid channel name
        :rtype:       int

        .. versionadded:: 7.2

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Channel names must only contain alpha-numeric characters or the
        underscore character "_", and the first letter must be a letter
        or an underscore.
        """
        ret_val = gxapi_cy.WrapDB._is_chan_name(GXContext._get_tls_geo(), chan.encode())
        return ret_val




    def is_chan_valid(self, chan):
        """
        This method checks to see if the channel handle is a
        valid channel.
        
        :param chan:  Channel handle to check
        :type  chan:  int

        :returns:     0 - Not a valid channel
                      1 - Valid
        :rtype:       int

        .. versionadded:: 5.1.1

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = self._is_chan_valid(chan)
        return ret_val



    @classmethod
    def is_line_name(cls, line):
        """
        Is this a valid line name.
        
        :param line:  Name to test
        :type  line:  str

        :returns:     1 if it is a valid line name
                      0 if it is not a valid line name
        :rtype:       int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = gxapi_cy.WrapDB._is_line_name(GXContext._get_tls_geo(), line.encode())
        return ret_val




    def is_line_valid(self, line):
        """
        This method checks to see if the line handle returned by
        the Line methods is a valid line.
        
        :param line:  Line handle to check
        :type  line:  int

        :returns:     0 - Not a valid line
                      1 - Valid
        :rtype:       int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = self._is_line_valid(line)
        return ret_val




    def line_category(self, line):
        """
        This method returns the category (group, line) of a line.
        
        :param line:  Line handle to look at
        :type  line:  int

        :returns:     :ref:`DB_CATEGORY_LINE` or `iDUMMY <geosoft.gxapi.iDUMMY>`.
        :rtype:       int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** The channel must be locked `DB_LOCK_READONLY <geosoft.gxapi.DB_LOCK_READONLY>` or `DB_LOCK_READWRITE <geosoft.gxapi.DB_LOCK_READWRITE>`
        """
        ret_val = self._line_category(line)
        return ret_val




    def line_flight(self, line):
        """
        This method returns the flight number of a line.
        
        :param line:  Line handle to look at
        :type  line:  int

        :returns:     Line Flight Number.
        :rtype:       int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** The channel must be locked `DB_LOCK_READONLY <geosoft.gxapi.DB_LOCK_READONLY>` or `DB_LOCK_READWRITE <geosoft.gxapi.DB_LOCK_READWRITE>`
        """
        ret_val = self._line_flight(line)
        return ret_val




    def line_label(self, line, label, format):
        """
        Create a line label
        
        :param line:    Line symbol
        :param label:   String in which to place label
        :param format:  :ref:`DB_LINE_LABEL_FORMAT`
        :type  line:    int
        :type  label:   str_ref
        :type  format:  int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Label formats.

        example full format is
        "L1023.4 13"   type "L"
        number "1023"
        version "4"
        flight "13"

        formats can be added to get combined format

        Use LINK format to create a database link label.
        """
        label.value = self._line_label(line, label.value.encode(), format)
        




    def line_number(self, line):
        """
        This method returns the number of a line.
        
        :param line:  Line handle to look at
        :type  line:  int

        :returns:     Line Number.
        :rtype:       int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** The line must be locked `DB_LOCK_READONLY <geosoft.gxapi.DB_LOCK_READONLY>` or `DB_LOCK_READWRITE <geosoft.gxapi.DB_LOCK_READWRITE>`
        """
        ret_val = self._line_number(line)
        return ret_val




    def line_number2(self, line, line_number):
        """
        Returns the string form of the line number (can be alphanumeric)
        
        :param line:         Line handle to look at
        :param line_number:  Line number
        :type  line:         int
        :type  line_number:  str_ref

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** The line must be locked `DB_LOCK_READONLY <geosoft.gxapi.DB_LOCK_READONLY>` or `DB_LOCK_READWRITE <geosoft.gxapi.DB_LOCK_READWRITE>`
        """
        line_number.value = self._line_number2(line, line_number.value.encode())
        




    def line_type(self, line):
        """
        This method returns the type of a line.
        
        :param line:  Line handle to look at
        :type  line:  int

        :returns:     :ref:`DB_LINE_TYPE`
        :rtype:       int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** The line must be locked `DB_LOCK_READONLY <geosoft.gxapi.DB_LOCK_READONLY>` or `DB_LOCK_READWRITE <geosoft.gxapi.DB_LOCK_READWRITE>`
        """
        ret_val = self._line_type(line)
        return ret_val




    def line_version(self, line):
        """
        This method returns the version number of a line.
        
        :param line:  Line handle to look at
        :type  line:  int

        :returns:     Line Number.
        :rtype:       int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** The line must be locked `DB_LOCK_READONLY <geosoft.gxapi.DB_LOCK_READONLY>` or `DB_LOCK_READWRITE <geosoft.gxapi.DB_LOCK_READWRITE>`
        """
        ret_val = self._line_version(line)
        return ret_val



    @classmethod
    def set_line_name(cls, num, type, ver, name):
        """
        This method sets up a line name given the line's number,
        type, and version.
        
        :param num:   Line number
        :param type:  Line type
        :param ver:   Line version
        :param name:  String to set line name to
        :type  num:   int
        :type  type:  int
        :type  ver:   int
        :type  name:  str_ref

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** This MUST be called to generate a line name when calls
        are made to `exist_symb <geosoft.gxapi.GXDB.exist_symb>`, `create_symb <geosoft.gxapi.GXDB.create_symb>` or `delete_symb <geosoft.gxapi.GXDB.delete_symb>`
        for an operation on a line.
        See also SetLineName2_DB.
        """
        name.value = gxapi_cy.WrapDB._set_line_name(GXContext._get_tls_geo(), num, type, ver, name.value.encode())
        



    @classmethod
    def set_line_name2(cls, al_num, type, ver, name):
        """
        Like SetLineName_DB, but can use alphanumeric for line number
        
        :param al_num:  Line number (alphanumeric)
        :param type:    Line type
        :param ver:     Line version
        :param name:    String to set line name to
        :type  al_num:  str
        :type  type:    int
        :type  ver:     int
        :type  name:    str_ref

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** This MUST be called to generate a line name when calls
        are made to `exist_symb <geosoft.gxapi.GXDB.exist_symb>`, `create_symb <geosoft.gxapi.GXDB.create_symb>` or `delete_symb <geosoft.gxapi.GXDB.delete_symb>`
        for an operation on a line.
        The line number can be any combination of letters and numbers,
        i.e. XU324, 98765, A, 23NGV etc.
        """
        name.value = gxapi_cy.WrapDB._set_line_name2(GXContext._get_tls_geo(), al_num.encode(), type, ver, name.value.encode())
        




    def rename_line(self, line, al_num, type, ver):
        """
        Change the name for a line.
        
        :param line:    Line handle of line to modify (READWRITE
        :param al_num:  Line number (alphanumeric)
        :param type:    Line type
        :param ver:     Line version
        :type  line:    int
        :type  al_num:  str
        :type  type:    int
        :type  ver:     int

        .. versionadded:: 9.9

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** The line must be locked :const:`DB_LOCK_READWRITE'
        Sets/resets the name of an existing line directly from line type, number, and version.
        The line number can be any combination of letters and numbers,
        i.e. XU324, 98765, A, 23NGV etc.
        Returns an error if the renamed line already exists.
        """
        self._rename_line(line, al_num.encode(), type, ver)
        




    def load_select(self, file):
        """
        Load selections to from a file.
        
        :param file:  File Name
        :type  file:  str

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._load_select(file.encode())
        




    def next_sel_line(self, prev):
        """
        This method will advance to the next selected line based
        on the currently selected line handle.
        
        :param prev:  Previous Line
        :type  prev:  int

        :returns:     Line Handle (use iIsLineValid method to see if valid).
        :rtype:       int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = self._next_sel_line(prev)
        return ret_val




    def line_bearing(self, line):
        """
        This method returns the bearing of a line.
        
        :param line:  Line handle to look at
        :type  line:  int

        :returns:     Bearing value, `rDUMMY <geosoft.gxapi.rDUMMY>` if not set.
        :rtype:       float

        .. versionadded:: 5.1.1

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** The channel must be locked `DB_LOCK_READONLY <geosoft.gxapi.DB_LOCK_READONLY>` or `DB_LOCK_READWRITE <geosoft.gxapi.DB_LOCK_READWRITE>`

        This function simply returns a value set using the `set_line_bearing <geosoft.gxapi.GXDB.set_line_bearing>`
        function. It returns `rDUMMY <geosoft.gxapi.rDUMMY>` for line categories other than
        `DB_CATEGORY_LINE_FLIGHT <geosoft.gxapi.DB_CATEGORY_LINE_FLIGHT>`.

        To calculate the line azimuth based on the first and
        last non-dummy locations, use the `GXDU.direction <geosoft.gxapi.GXDU.direction>` function.

        .. seealso::

            `set_line_bearing <geosoft.gxapi.GXDB.set_line_bearing>`, `GXDU.direction <geosoft.gxapi.GXDU.direction>`
        """
        ret_val = self._line_bearing(line)
        return ret_val




    def line_date(self, line):
        """
        This method returns the date of a line.
        
        :param line:  Line handle to look at
        :type  line:  int

        :returns:     Date value.
        :rtype:       float

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** The channel must be locked `DB_LOCK_READONLY <geosoft.gxapi.DB_LOCK_READONLY>` or `DB_LOCK_READWRITE <geosoft.gxapi.DB_LOCK_READWRITE>`
        """
        ret_val = self._line_date(line)
        return ret_val




    def save_select(self, file):
        """
        Saves current selections to a file.
        
        :param file:  File Name
        :type  file:  str

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._save_select(file.encode())
        




    def select(self, select, mode):
        """
        Select/deselect lines based on selection string
        
        :param select:  Selection
        :param mode:    :ref:`DB_LINE_SELECT`
        :type  select:  str
        :type  mode:    int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Selections/deselections are cumulative. If lines had already
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
        self._select(select.encode(), mode)
        




    def set_line_bearing(self, line, bearing):
        """
        Sets a line's bearing.
        
        :param line:     Line handle
        :param bearing:  Value to set bearing to
        :type  line:     int
        :type  bearing:  float

        .. versionadded:: 5.1.1

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** The channel must be locked `DB_LOCK_READWRITE <geosoft.gxapi.DB_LOCK_READWRITE>`

        This function simply sets a value in the line's metadata
        that is retrieved using the `line_bearing <geosoft.gxapi.GXDB.line_bearing>`
        function. It terminates for line categories other than
        `DB_CATEGORY_LINE_FLIGHT <geosoft.gxapi.DB_CATEGORY_LINE_FLIGHT>`.

        .. seealso::

            `line_bearing <geosoft.gxapi.GXDB.line_bearing>`, `GXDU.direction <geosoft.gxapi.GXDU.direction>`
        """
        self._set_line_bearing(line, bearing)
        




    def set_line_date(self, line, date):
        """
        This method sets a line's date.
        
        :param line:  Line handle
        :param date:  Value to set date to
        :type  line:  int
        :type  date:  float

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** The channel must be locked `DB_LOCK_READWRITE <geosoft.gxapi.DB_LOCK_READWRITE>`
        """
        self._set_line_date(line, date)
        




    def set_line_flight(self, line, fl):
        """
        This method sets a line's flight.
        
        :param line:  Line handle
        :param fl:    Value to set line flight to
        :type  line:  int
        :type  fl:    int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** The channel must be locked `DB_LOCK_READWRITE <geosoft.gxapi.DB_LOCK_READWRITE>`
        """
        self._set_line_flight(line, fl)
        




    def set_line_map_fid(self, line, start, end):
        """
        This method changes a line map clip fiducial.
        
        :param line:   Line handle to look at
        :param start:  Start Fid
        :param end:    End Fid
        :type  line:   int
        :type  start:  float
        :type  end:    float

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** for full range, set Start Fid to `rMIN <geosoft.gxapi.rMIN>` and End Fid to `rMAX <geosoft.gxapi.rMAX>`.
        for no data, set Start and End Fids to `rDUMMY <geosoft.gxapi.rDUMMY>`.
        """
        self._set_line_map_fid(line, start, end)
        




    def set_line_num(self, line, num):
        """
        This method sets a line's number.
        
        :param line:  Line handle
        :param num:   Value to set line number to
        :type  line:  int
        :type  num:   int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** The channel must be locked `DB_LOCK_READWRITE <geosoft.gxapi.DB_LOCK_READWRITE>`
        """
        self._set_line_num(line, num)
        




    def set_line_type(self, line, type):
        """
        This method sets a line's type.
        
        :param line:  Line handle
        :param type:  :ref:`DB_LINE_TYPE`
        :type  line:  int
        :type  type:  int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** The channel must be locked `DB_LOCK_READWRITE <geosoft.gxapi.DB_LOCK_READWRITE>`
        """
        self._set_line_type(line, type)
        




    def set_line_ver(self, line, ver):
        """
        This method sets a line's version.
        
        :param line:  Line handle
        :param ver:   Value to set line version to
        :type  line:  int
        :type  ver:   int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** The channel must be locked `DB_LOCK_READWRITE <geosoft.gxapi.DB_LOCK_READWRITE>`
        """
        self._set_line_ver(line, ver)
        




    def set_select(self, sel):
        """
        Sets the Line Selections.
        
        :param sel:  Selections
        :type  sel:  int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** This method also destroys the DB_SELECT object.
        """
        self._set_select(sel)
        




# META



    def get_meta(self, meta):
        """
        Get the metadata of a database.
        
        :param meta:  Meta object to fill with database's meta
        :type  meta:  GXMETA

        .. versionadded:: 5.1.5

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._get_meta(meta)
        




    def set_meta(self, meta):
        """
        Set the metadata of a database.
        
        :param meta:  Meta object to add to database's meta
        :type  meta:  GXMETA

        .. versionadded:: 5.1.5

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._set_meta(meta)
        




# Symbols


    @classmethod
    def create_symb_lst(cls):
        """
        Create  a `GXLST <geosoft.gxapi.GXLST>` object large enough to contain channel names and symbols numbers.
        
        :rtype:      GXLST

        .. versionadded:: 9.8

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = gxapi_cy.WrapDB._create_symb_lst(GXContext._get_tls_geo())
        return GXLST(ret_val)




    def array_lst(self, lst):
        """
        Load a `GXLST <geosoft.gxapi.GXLST>` object with array (`GXVA <geosoft.gxapi.GXVA>`) channel symbols.
        
        :param lst:  List to Populate (construct with CreateSymbLST_DB)
        :type  lst:  GXLST

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._array_lst(lst)
        




    def array_size_lst(self, columns, lst):
        """
        Load a `GXLST <geosoft.gxapi.GXLST>` object with array (`GXVA <geosoft.gxapi.GXVA>`) channel symbols with a particular number of columns.
        
        :param columns:  Number of columns in array ( > 1 )
        :param lst:      List to Populate (construct with CreateSymbLST_DB)
        :type  columns:  int
        :type  lst:      GXLST

        .. versionadded:: 8.2

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._array_size_lst(columns, lst)
        




    def chan_lst(self, lst):
        """
        Load a `GXLST <geosoft.gxapi.GXLST>` with database channels.
        
        :param lst:  List to Populate (construct with CreateSymbLST_DB)
        :type  lst:  GXLST

        .. versionadded:: 6.3

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Populates a `GXLST <geosoft.gxapi.GXLST>` with channel symbols.
        The name is put into the "Name" part of the `GXLST <geosoft.gxapi.GXLST>` (0),
        and the handle, an integer value written as a string, is
        placed in the value part of the `GXLST <geosoft.gxapi.GXLST>` (1).
        Array channels are included, as well as virtual channels (array channel single columns loaded in the database like \\"Chan[1]\\".

        The `GXLST <geosoft.gxapi.GXLST>` is cleared first, and the items are sorted by name.
        """
        self._chan_lst(lst)
        




    def normal_chan_lst(self, lst):
        """
        Load a `GXLST <geosoft.gxapi.GXLST>` with non-array database channels.
        
        :param lst:  List to Populate (construct with CreateSymbLST_DB)
        :type  lst:  GXLST

        .. versionadded:: 8.2

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Like `chan_lst <geosoft.gxapi.GXDB.chan_lst>`, but does not include array channels or virtual channels.
        """
        self._normal_chan_lst(lst)
        




    def non_string_and_non_array_chan_lst(self, lst):
        """
        Load a `GXLST <geosoft.gxapi.GXLST>` with non-string and non-array database channels.
        
        :param lst:  List to Populate (construct with CreateSymbLST_DB)
        :type  lst:  GXLST

        .. versionadded:: 9.9

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Like `chan_lst <geosoft.gxapi.GXDB.chan_lst>`, but does not include array channels, virtual channels or string channels.
        """
        self._non_string_and_non_array_chan_lst(lst)
        




    def class_chan_lst(self, lst, cl):
        """
        Load a `GXLST <geosoft.gxapi.GXLST>` with channels in a particular class.
        
        :param lst:  `GXLST <geosoft.gxapi.GXLST>` object to populate (construct with CreateSymbLST_DB)
        :param cl:   CLASS name for the channel ("" for all)
        :type  lst:  GXLST
        :type  cl:   str

        .. versionadded:: 5.0.3

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** The Name of the symbol is placed in the
        item name and the item value is set to the symbol handle.
        Only channels with the given class name are included,
        e.g. use "ASSAY" for assay channels in `GXCHIMERA <geosoft.gxapi.GXCHIMERA>`.

        The `GXLST <geosoft.gxapi.GXLST>` is cleared first, and the items are sorted by name.
        """
        self._class_chan_lst(lst, cl.encode())
        




    def class_group_lst(self, lst, cl):
        """
        Load a `GXLST <geosoft.gxapi.GXLST>` with group lines in a particular class.
        
        :param lst:  `GXLST <geosoft.gxapi.GXLST>` object to populate (construct with CreateSymbLST_DB)
        :param cl:   CLASS name for the group ("" for all)
        :type  lst:  GXLST
        :type  cl:   str

        .. versionadded:: 5.0.8

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** The Name of the symbol is placed in the
        item name and the item value is set to the symbol handle.
        Only group lines with the given class name are included,
        e.g. use "TARGETS" for UX-Detect Target groups.

        The `GXLST <geosoft.gxapi.GXLST>` is cleared first, and the items are sorted by name.
        """
        self._class_group_lst(lst, cl.encode())
        




    def create_symb(self, name, symb, owner, category):
        """
        Create a new Symbol.
        
        :param name:      Symbol Name
        :param symb:      :ref:`DB_SYMB_TYPE`
        :param owner:     :ref:`DB_OWN`
        :param category:  :ref:`DB_CATEGORY_USER`, :ref:`DB_CATEGORY_LINE`, :ref:`DB_CATEGORY_CHAN`, :ref:`DB_CATEGORY_BLOB`
        :type  name:      str
        :type  symb:      int
        :type  owner:     int
        :type  category:  int

        :returns:         DB_SYMB Object
        :rtype:           int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** If symbol already exits, and it is the same type
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
        ret_val = self._create_symb(name.encode(), symb, owner, category)
        return ret_val




    def create_symb_ex(self, name, symb, owner, category, extra):
        """
        Create a new Symbol.
        
        :param name:      Symbol Name
        :param symb:      :ref:`DB_SYMB_TYPE`
        :param owner:     :ref:`DB_OWN`
        :param category:  :ref:`DB_CATEGORY_USER`, :ref:`DB_CATEGORY_LINE`, :ref:`DB_CATEGORY_CHAN`, :ref:`DB_CATEGORY_BLOB`
        :param extra:     Extra info, which depends on :ref:`DB_SYMB_TYPE` `DB_SYMB_CHAN <geosoft.gxapi.DB_SYMB_CHAN>` - element width for a `GXVA <geosoft.gxapi.GXVA>` channel ignores for all other :ref:`DB_SYMB_TYPE` types
        :type  name:      str
        :type  symb:      int
        :type  owner:     int
        :type  category:  int
        :type  extra:     int

        :returns:         DB_SYMB handle.
        :rtype:           int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** If symbol already exits it is returned.

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
        ret_val = self._create_symb_ex(name.encode(), symb, owner, category, extra)
        return ret_val




    def csv_chan_lst(self, lst, channels):
        """
        Load a `GXLST <geosoft.gxapi.GXLST>` with channels in a comma-separated list.
        
        :param lst:       `GXLST <geosoft.gxapi.GXLST>` object to populate (construct with CreateSymbLST_DB)
        :param channels:  Comma-separated list of channels
        :type  lst:       GXLST
        :type  channels:  str

        .. versionadded:: 6.2

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** The Name of the symbol is placed in the
        item name and the item value is set to the symbol handle.
        Only channels in the list which are present in the database
        are included.

        The `GXLST <geosoft.gxapi.GXLST>` is cleared first.
        """
        self._csv_chan_lst(lst, channels.encode())
        




    def delete_symb(self, symb):
        """
        This method destroys a symbol in the database and all
        the data associated with it. The symbol's lock is
        automatically removed.
        
        :param symb:  Symbol to Delete (must be READWRITE locked)
        :type  symb:  int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._delete_symb(symb)
        




    def dup_line_symb(self, symb, new_name):
        """
        Duplicate a line symbol from a group or line symbol.
        The new name must not already exist in the database.
        
        :param symb:      Symbol Handle to duplicate
        :param new_name:  Name of the New Symbol
        :type  symb:      int
        :type  new_name:  str

        :returns:         New Symbol Handle
        :rtype:           int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = self._dup_line_symb(symb, new_name.encode())
        return ret_val




    def dup_symb(self, symb, new_name):
        """
        New Symbol by duplicating an existing symbol, LOCKED
        
        :param symb:      Symbol Handle to duplicate
        :param new_name:  Name of the New Symbol
        :type  symb:      int
        :type  new_name:  str

        :returns:         New Symbol Handle
        :rtype:           int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** The symbol will be locked READWRITE.
        The new name must not already exist in the database.

        .. seealso::

            `dup_symb_no_lock <geosoft.gxapi.GXDB.dup_symb_no_lock>`
        """
        ret_val = self._dup_symb(symb, new_name.encode())
        return ret_val




    def dup_symb_no_lock(self, symb, new_name):
        """
        New Symbol by duplicating an existing symbol, NO LOCK.
        
        :param symb:      Symbol Handle to duplicate
        :param new_name:  Name of the New Symbol
        :type  symb:      int
        :type  new_name:  str

        :returns:         New Symbol Handle
        :rtype:           int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** The symbol will be NOT be locked.
        The new name must not already exist in the database.

        .. seealso::

            `dup_symb <geosoft.gxapi.GXDB.dup_symb>`
        """
        ret_val = self._dup_symb_no_lock(symb, new_name.encode())
        return ret_val




    def find_chan(self, chan):
        """
        Get handle to the specified channel.
        
        :param chan:  Name of channel
        :type  chan:  str

        :returns:     Channel Handle, `NULLSYMB <geosoft.gxapi.NULLSYMB>` if not defined
        :rtype:       int

        .. versionadded:: 5.1.3

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** To work with a specific column from a `GXVA <geosoft.gxapi.GXVA>` channel,
        specify the `GXVA <geosoft.gxapi.GXVA>` element number in square brackets as part
        of the `GXVA <geosoft.gxapi.GXVA>` channel name (e.g. "EM[3]" will treat the fourth
        column of the `GXVA <geosoft.gxapi.GXVA>` channel as a `GXVV <geosoft.gxapi.GXVV>`).

        See notes for `find_symb <geosoft.gxapi.GXDB.find_symb>`.
        Introduced in v5.1.3.
        The new `find_chan <geosoft.gxapi.GXDB.find_chan>` searches using the exact channel name.
        """
        ret_val = self._find_chan(chan.encode())
        return ret_val




    def find_symb(self, symb, type):
        """
        Get handle to the specified symbol.
        
        :param symb:  Name of symbol
        :param type:  :ref:`DB_SYMB_TYPE`
        :type  symb:  str
        :type  type:  int

        :returns:     Symbol Handle, `NULLSYMB <geosoft.gxapi.NULLSYMB>` if not defined
        :rtype:       int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** To work with a specific column from a `GXVA <geosoft.gxapi.GXVA>` channel,
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
        ret_val = self._find_symb(symb.encode(), type)
        return ret_val




    def get_chan_order_lst(self, lst):
        """
        This method gets the channel display order for a
        database. The list will be stored in an `GXLST <geosoft.gxapi.GXLST>` object.
        In order to modify this displayed channels list,
        call `set_chan_order_lst <geosoft.gxapi.GXDB.set_chan_order_lst>` after.
        
        :param lst:  `GXLST <geosoft.gxapi.GXLST>` object to populate (construct with CreateSymbLST_DB)
        :type  lst:  GXLST

        .. versionadded:: 5.0.8

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._get_chan_order_lst(lst)
        




    def get_xyz_chan_symb(self, chan):
        """
        Searches for current X, Y or Z channel symbol
        
        :param chan:  :ref:`DB_CHAN_SYMBOL`
        :type  chan:  int

        :returns:     x - Symbol Handle
                      `NULLSYMB <geosoft.gxapi.NULLSYMB>` - Symbol not found

                      searches for the "current" X, Y or Z channel.
                      If none is defined, then looks for "X", "Y" or "Z" channel
                      If the channel is defined, but not present, returns `NULLSYMB <geosoft.gxapi.NULLSYMB>`.
        :rtype:       int

        .. versionadded:: 5.1.3

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = self._get_xyz_chan_symb(chan)
        return ret_val




    def class_chan_list(self, vv, cl):
        """
        Place a list of channels for a given class in a `GXVV <geosoft.gxapi.GXVV>`.
        
        :param vv:  `GXVV <geosoft.gxapi.GXVV>` to populate, must be type INT.
        :param cl:  Class name to match ("" for all)
        :type  vv:  GXVV
        :type  cl:  str

        :returns:    Number of symbols.
        :rtype:      int

        .. versionadded:: 5.0.5

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** This method generates a list of symbols in the database
        and places their handles into a `GXVV <geosoft.gxapi.GXVV>`. The list is not
        sorted.
        Only channels with the given class name are included,
        e.g. use "ASSAY" for assay channels used in `GXCHIMERA <geosoft.gxapi.GXCHIMERA>`.
        """
        ret_val = self._class_chan_list(vv, cl.encode())
        return ret_val




    def exist_chan(self, chan):
        """
        See if the specified channel exists in the database.
        
        :param chan:  Name of Channel
        :type  chan:  str

        :returns:     0 - Symbol does not exist in the database
                      1 - Symbol Exists
        :rtype:       int

        .. versionadded:: 5.1.3

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** See notes for `exist_symb <geosoft.gxapi.GXDB.exist_symb>`.
        Introduced in v5.1.3.
        `exist_chan <geosoft.gxapi.GXDB.exist_chan>` searches using the exact channel name.
        """
        ret_val = self._exist_chan(chan.encode())
        return ret_val




    def exist_symb(self, symb, type):
        """
        This method checks to see if the specified symbol exists
        in the database.
        
        :param symb:  Name of Symbol
        :param type:  :ref:`DB_SYMB_TYPE`
        :type  symb:  str
        :type  type:  int

        :returns:     0 - Symbol does not exist in the database
                      1 - Symbol Exists
        :rtype:       int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** For backward compatibility with GXs not employing the
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
        ret_val = self._exist_symb(symb.encode(), type)
        return ret_val




    def valid_symb(self, symb, type):
        """
        This method checks to see if the specified symbol is a valid symbol in the database.
        
        :param symb:  Symbol to check
        :param type:  :ref:`DB_SYMB_TYPE`
        :type  symb:  int
        :type  type:  int

        :returns:     0 - Invalid symbol 
                      1 - Symbol is valid
        :rtype:       int

        .. versionadded:: 9.1

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = self._valid_symb(symb, type)
        return ret_val




    def get_symb_lock(self, symb):
        """
        Determines if a symbol is locked
        
        :param symb:  Symbol to Lock
        :type  symb:  int

        :returns:     :ref:`DB_LOCK`
        :rtype:       int

        .. versionadded:: 6.3

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = self._get_symb_lock(symb)
        return ret_val




    def get_xyz_chan(self, chan_symb, chan):
        """
        Gets current X, Y or Z channel name
        
        :param chan_symb:  :ref:`DB_CHAN_SYMBOL`
        :param chan:       Returned name
        :type  chan_symb:  int
        :type  chan:       str_ref

        .. versionadded:: 5.1.3

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** searches for the "current" X, Y or Z channel.
        If none is defined, then returns "X", "Y" or "Z".
        """
        chan.value = self._get_xyz_chan(chan_symb, chan.value.encode())
        




    def symb_list(self, vv, symb):
        """
        Place a list of symbols in a `GXVV <geosoft.gxapi.GXVV>`.
        
        :param vv:    `GXVV <geosoft.gxapi.GXVV>` to populate, must be type INT.
        :param symb:  :ref:`DB_SYMB_TYPE`
        :type  vv:    GXVV
        :type  symb:  int

        :returns:     Number of symbols.
        :rtype:       int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = self._symb_list(vv, symb)
        return ret_val




    def line_lst(self, lst):
        """
        Load a `GXLST <geosoft.gxapi.GXLST>` with database lines.
        
        :param lst:  List to Populate (construct with CreateSymbLST_DB)
        :type  lst:  GXLST

        .. versionadded:: 6.3

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Populates a `GXLST <geosoft.gxapi.GXLST>` with channel symbols.
        The name is put into the "Name" part of the `GXLST <geosoft.gxapi.GXLST>` (0),
        and the handle, an integer value written as a string, is
        placed in the value part of the `GXLST <geosoft.gxapi.GXLST>` (1).
        The `GXLST <geosoft.gxapi.GXLST>` is cleared first, and the items are sorted in logical line order.
        """
        self._line_lst(lst)
        




    def lock_symb(self, symb, lock, wait):
        """
        Locks a symbol for READONLY or READWRITE.
        
        :param symb:  Symbol to Lock
        :param lock:  :ref:`DB_LOCK`
        :param wait:  :ref:`DB_WAIT`
        :type  symb:  int
        :type  lock:  int
        :type  wait:  int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._lock_symb(symb, lock, wait)
        




    def mask_chan_lst(self, lst):
        """
        Load a `GXLST <geosoft.gxapi.GXLST>` with mask channels.
        
        :param lst:  `GXLST <geosoft.gxapi.GXLST>` object to populate
        :type  lst:  GXLST

        .. versionadded:: 5.1.5

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Loads a `GXLST <geosoft.gxapi.GXLST>` with all channels with CLASS "MASK", as well
        as all channels containing the string "MASK", as long
        as the CLASS for these channels is not set to something
        other than "" or "MASK".

        This function is a duplicate of the `GXCHIMERA.mask_chan_lst <geosoft.gxapi.GXCHIMERA.mask_chan_lst>`
        function, and can be used if `GXCHIMERA <geosoft.gxapi.GXCHIMERA>` is not installed.

        The `GXLST <geosoft.gxapi.GXLST>` is cleared first, and the items are sorted by name.
        "None" is added at the end, with a handle value of "-1".
        """
        self._mask_chan_lst(lst)
        




    def selected_line_lst(self, lst):
        """
        Load a `GXLST <geosoft.gxapi.GXLST>` with the selected lines.
        
        :param lst:  List to Populate (construct with CreateSymbLST_DB)
        :type  lst:  GXLST

        .. versionadded:: 5.1.2

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** This method populates a `GXLST <geosoft.gxapi.GXLST>` object with all of the symbols
        of the selected lines in the database.
        The name is put into the "Name" part of the `GXLST <geosoft.gxapi.GXLST>` (0),
        and the handle, an integer value written as a string, is
        placed in the value part of the `GXLST <geosoft.gxapi.GXLST>` (1).

        Symbols are automatically sorted in logical line order.
        """
        self._selected_line_lst(lst)
        




    def set_chan_order_lst(self, lst):
        """
        This method sets the channel display order for a
        database. The list to modify will be stored in an `GXLST <geosoft.gxapi.GXLST>`
        object. Call `get_chan_order_lst <geosoft.gxapi.GXDB.get_chan_order_lst>` to populate the `GXLST <geosoft.gxapi.GXLST>`.
        
        :param lst:  `GXLST <geosoft.gxapi.GXLST>` object to modify
        :type  lst:  GXLST

        .. versionadded:: 5.0.8

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._set_chan_order_lst(lst)
        




    def set_xyz_chan(self, chan_symb, chan):
        """
        Sets current X, Y or Z channel name
        
        :param chan_symb:  :ref:`DB_CHAN_SYMBOL`
        :param chan:       Channel name
        :type  chan_symb:  int
        :type  chan:       str

        .. versionadded:: 5.1.3

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** If the value specified is "", the internally stored value
        is cleared, and GetXYZChan_DB will return "X", "Y" or "Z"

        This can be used, for instance, to make "Easting" and "Northing"
        the current X and Y channels, and have GXs using the
        `get_xyz_chan_symb <geosoft.gxapi.GXDB.get_xyz_chan_symb>` function to load "X" and "Y" work as desired.
        """
        self._set_xyz_chan(chan_symb, chan.encode())
        




    def string_chan_lst(self, lst):
        """
        Load a `GXLST <geosoft.gxapi.GXLST>` with string-type channels.
        
        :param lst:  `GXLST <geosoft.gxapi.GXLST>` object to populate
        :type  lst:  GXLST

        .. versionadded:: 6.2

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** The Name of the symbol is placed in the
        item name and the item value is set to the symbol handle.
        Only channels with the string-type data (sChanType_DB < 0)
        are included.

        The `GXLST <geosoft.gxapi.GXLST>` is cleared first, and the items are sorted by name.
        """
        self._string_chan_lst(lst)
        




    def symb_lst(self, lst, type):
        """
        Populate a `GXLST <geosoft.gxapi.GXLST>` with database symbols.
        
        :param lst:   List to Populate (construct with CreateSymbLST_DB)
        :param type:  :ref:`DB_SYMB_TYPE`
        :type  lst:   GXLST
        :type  type:  int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Populates a `GXLST <geosoft.gxapi.GXLST>` with channel, line, blob or user symbols.
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
        self._symb_lst(lst, type)
        




    def un_lock_all_symb(self):
        """
        UnLocks all symbols.
        

        .. versionadded:: 5.1.1

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._un_lock_all_symb()
        




    def un_lock_symb(self, symb):
        """
        UnLocks a symbol.
        
        :param symb:  Symbol to Lock
        :type  symb:  int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._un_lock_symb(symb)
        




# VA Channels



    def add_associated_load(self, group, chan):
        """
        Add this channel to the auto-load feature of the group.
        
        :param group:  Line
        :param chan:   Channel
        :type  group:  int
        :type  chan:   int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** If the channel is not yet associated, it is first associated.
        If the channel is already in the associated-load list, this
        does nothing.

        As of v6.0, the load-status of channels is no longer stored
        in the database, but in the project, so this function is
        equivalent to calling `associate <geosoft.gxapi.GXDB.associate>`.
        """
        self._add_associated_load(group, chan)
        




    def add_comment(self, comment, str_val, indent):
        """
        Add a comment with a string to the activity log of the database.
        
        :param comment:  Comment
        :param str_val:  String
        :param indent:   Indent comment one tab? (TRUE or FALSE)
        :type  comment:  str
        :type  str_val:  str
        :type  indent:   int

        .. versionadded:: 5.0.8

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** The comment is written in the form:

        Comment: String2

        and is followed by a carriage return.
        The activity log is created automatically if it does not exist.
        """
        self._add_comment(comment.encode(), str_val.encode(), indent)
        




    def add_int_comment(self, comment, val, indent):
        """
        Add a comment with an integer to the activity log of the database.
        
        :param comment:  Comment
        :param val:      Value
        :param indent:   Indent comment one tab?
        :type  comment:  str
        :type  val:      int
        :type  indent:   bool

        .. versionadded:: 5.0.8

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** The comment is written in the form:

        Comment: Value

        and is followed by a carriage return.
        The activity log is created automatically if it does not exist.

        See Notes in `add_comment <geosoft.gxapi.GXDB.add_comment>`.
        """
        self._add_int_comment(comment.encode(), val, indent)
        




    def add_double_comment(self, comment, val, indent):
        """
        Add a comment with a float value to the activity log of the database.
        
        :param comment:  Comment
        :param val:      Value
        :param indent:   Indent comment one tab?
        :type  comment:  str
        :type  val:      float
        :type  indent:   bool

        .. versionadded:: 5.0.8

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** The comment is written in the form:

        Comment: Value

        and if followed by a carriage return.
        The activity log is created automatically if it does not exist.

        See Notes in `add_comment <geosoft.gxapi.GXDB.add_comment>`.
        """
        self._add_double_comment(comment.encode(), val, indent)
        




    def add_time_comment(self, comment, indent):
        """
        Add a comment with the date and time to the activity log of the database.
        
        :param comment:  Comment
        :param indent:   Indent comment one tab?
        :type  comment:  str
        :type  indent:   bool

        .. versionadded:: 5.0.8

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** The comment is written in the form:

        Comment: 2001/12/31 23:59:59

        and is followed by a carriage return.
        The activity log is created automatically if it does not exist.

        See Notes in `add_comment <geosoft.gxapi.GXDB.add_comment>`.
        """
        self._add_time_comment(comment.encode(), indent)
        




    def associate(self, group, chan):
        """
        Associate a channel with a group.
        
        :param group:  Group line
        :param chan:   Channel
        :type  group:  int
        :type  chan:   int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** If it is already associated, or if the group has no
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
        self._associate(group, chan)
        




    def associate_all(self, group):
        """
        Associate all channels with a group.
        
        :param group:  Group line
        :type  group:  int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** As of v6.3, if a group line has no class defined, then ALL
        channels are already assumed to be associated with it, and this
        function does nothing.
        """
        self._associate_all(group)
        




    def associate_class(self, chan, cl):
        """
        Associate a channel with all groups of a specific class.
        
        :param chan:  Channel
        :param cl:    Class name of groups to associate the channel with. (Must be defined).
        :type  chan:  int
        :type  cl:    str

        .. versionadded:: 5.1.1

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** As of v6.3, if a group line has no class defined, then ALL
        channels are automatically assumed to be associated with it.
        """
        self._associate_class(chan, cl.encode())
        



    @classmethod
    def gen_valid_chan_symb(cls, str_in, str_out):
        """
        Generate a valid channel name from a name candidate
        
        :param str_in:   Input string
        :param str_out:  Outout string
        :type  str_in:   str
        :type  str_out:  str_ref

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        str_out.value = gxapi_cy.WrapDB._gen_valid_chan_symb(GXContext._get_tls_geo(), str_in.encode(), str_out.value.encode())
        



    @classmethod
    def gen_valid_line_symb(cls, str_in, str_out):
        """
        Generate a valid line symb name string from given string.
        
        :param str_in:   Input string
        :param str_out:  Outout string
        :type  str_in:   str
        :type  str_out:  str_ref

        .. versionadded:: 6.4

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** The returned name is either the same size as the input
        or shorter. Escapes, leading and trailing spaces are removed, then
        all illegal characters are replaced with an underscore.
        """
        str_out.value = gxapi_cy.WrapDB._gen_valid_line_symb(GXContext._get_tls_geo(), str_in.encode(), str_out.value.encode())
        




    def get_chan_va(self, line, chan, va):
        """
        Place the contents of a channel in a `GXVA <geosoft.gxapi.GXVA>`.
        
        :param line:  Line
        :param chan:  Channel
        :param va:    `GXVA <geosoft.gxapi.GXVA>` in which to place the data
        :type  line:  int
        :type  chan:  int
        :type  va:    GXVA

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        .. seealso::

            `GXVA <geosoft.gxapi.GXVA>` class.
        """
        self._get_chan_va(line, chan, va)
        




    def get_va_scaling(self, ch, base, range):
        """
        Get base and range for `GXVA <geosoft.gxapi.GXVA>` channel cell display.
        
        :param ch:     Channel (Locked `DB_LOCK_READWRITE <geosoft.gxapi.DB_LOCK_READWRITE>`)
        :param base:   Base value (rDummy for none)
        :param range:  Range value (rDummy for none)
        :type  ch:     int
        :type  base:   float_ref
        :type  range:  float_ref

        .. versionadded:: 5.1.5

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** See `set_va_scaling <geosoft.gxapi.GXDB.set_va_scaling>`.
        """
        base.value, range.value = self._get_va_scaling(ch, base.value, range.value)
        




    def get_va_windows(self, ch, min_w, max_w):
        """
        Get the range of windows displayed for a `GXVA <geosoft.gxapi.GXVA>` channel.
        
        :param ch:     Channel (Locked `DB_LOCK_READWRITE <geosoft.gxapi.DB_LOCK_READWRITE>`)
        :param min_w:  First window (0 to N-2, iDummy for default)
        :param max_w:  Last window (1 to N-1, iDummy for default)
        :type  ch:     int
        :type  min_w:  int_ref
        :type  max_w:  int_ref

        .. versionadded:: 5.1.5

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** See `set_va_windows <geosoft.gxapi.GXDB.set_va_windows>`.
        """
        min_w.value, max_w.value = self._get_va_windows(ch, min_w.value, max_w.value)
        




    def set_va_base_coordinate_info(self, ch, domain, base, vv, units, allow_changes):
        """
        Set the array channel base coordinate type, offset and values.
        
        :param ch:             Channel (Locked `DB_LOCK_READWRITE <geosoft.gxapi.DB_LOCK_READWRITE>`)
        :param domain:         :ref:`DB_ARRAY_BASETYPE`
        :param base:           Optional offset or base frequency
        :param vv:             Values (one per array channel column) (REAL)
        :param units:          Units
        :param allow_changes:  Allow changes to existing values?
        :type  ch:             int
        :type  domain:         int
        :type  base:           float
        :type  vv:             GXVV
        :type  units:          str
        :type  allow_changes:  bool

        .. versionadded:: 8.2

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** See `get_va_base_coordinate_info <geosoft.gxapi.GXDB.get_va_base_coordinate_info>`.
        """
        self._set_va_base_coordinate_info(ch, domain, base, vv, units.encode(), allow_changes)
        




    def get_va_base_coordinate_info(self, ch, domain, base, vv, units):
        """
        Set the array channel base coordinate type, offset and values.
        
        :param ch:      Channel (Locked `DB_LOCK_READONLY <geosoft.gxapi.DB_LOCK_READONLY>`)
        :param domain:  :ref:`DB_ARRAY_BASETYPE`
        :param base:    Optional offset or base frequency
        :param vv:      Values (one per array channel column) (REAL)
        :param units:   Units
        :type  ch:      int
        :type  domain:  int_ref
        :type  base:    float_ref
        :type  vv:      GXVV
        :type  units:   str_ref

        .. versionadded:: 8.2

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** See `set_va_base_coordinate_info <geosoft.gxapi.GXDB.set_va_base_coordinate_info>`.
        """
        domain.value, base.value, units.value = self._get_va_base_coordinate_info(ch, domain.value, base.value, vv, units.value.encode())
        




    def get_group_class(self, symb, cl):
        """
        Set the Class name for a group line.
        
        :param symb:  Group line - `DB_LOCK_READWRITE <geosoft.gxapi.DB_LOCK_READWRITE>` or `DB_LOCK_READONLY <geosoft.gxapi.DB_LOCK_READONLY>`
        :param cl:    Returned class name - max size = `DB_GROUP_CLASS_SIZE <geosoft.gxapi.DB_GROUP_CLASS_SIZE>` - 1
        :type  symb:  int
        :type  cl:    str_ref

        .. versionadded:: 5.0.8

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** This method fails if the line is not a group line.
        Group classes are used to identify group lines used for
        special purposes, e.g.: "COLLAR" for the Wholeplot collar table,
        or "TARGETS" for the UX-Detect Targets list.

        .. seealso::

            `line_category <geosoft.gxapi.GXDB.line_category>` - to see if a line is a group line.
        """
        cl.value = self._get_group_class(symb, cl.value.encode())
        




    def get_info(self, item):
        """
        Get information about the database.
        
        :param item:  :ref:`DB_INFO`
        :type  item:  int

        :returns:     x - Return Value
        :rtype:       int

        .. versionadded:: 7.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = self._get_info(item)
        return ret_val




    def get_va_prof_color_file(self, ch, file):
        """
        Get colors for a `GXVA <geosoft.gxapi.GXVA>` channel when displayed in the profile window.
        
        :param ch:    Channel (Locked `DB_LOCK_READWRITE <geosoft.gxapi.DB_LOCK_READWRITE>`)
        :param file:  Zone file name, "" to clear.
        :type  ch:    int
        :type  file:  str_ref

        .. versionadded:: 5.1.5

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** See `set_va_prof_color_file <geosoft.gxapi.GXDB.set_va_prof_color_file>`.
        """
        file.value = self._get_va_prof_color_file(ch, file.value.encode())
        




    def get_va_prof_sect_option(self, ch, option):
        """
        Get the display options of `GXVA <geosoft.gxapi.GXVA>` channels
        
        :param ch:      Channel (Locked `DB_LOCK_READWRITE <geosoft.gxapi.DB_LOCK_READWRITE>`)
        :param option:  Option  "Profile", "Section" or "Section and Profile"
        :type  ch:      int
        :type  option:  str_ref

        .. versionadded:: 5.1.6

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        option.value = self._get_va_prof_sect_option(ch, option.value.encode())
        




    def get_va_sect_color_file(self, ch, file):
        """
        Get colors for a `GXVA <geosoft.gxapi.GXVA>` channel when displayed section in the profile window.
        
        :param ch:    Channel (Locked `DB_LOCK_READWRITE <geosoft.gxapi.DB_LOCK_READWRITE>`)
        :param file:  Zone file name
        :type  ch:    int
        :type  file:  str_ref

        .. versionadded:: 5.1.6

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Fails in the channel is not an array channel
        """
        file.value = self._get_va_sect_color_file(ch, file.value.encode())
        




    def is_associated(self, group, chan):
        """
        Check to see if a channel is associated with group.
        
        :param group:  Line
        :param chan:   Channel
        :type  group:  int
        :type  chan:   int

        :returns:      0 if not a group line, or if the channel is not associated.

                       As of v6.3, if a group line has no class defined, then ALL
                       channels are automatically assumed to be associated with it.
        :rtype:        int

        .. versionadded:: 5.1.3

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = self._is_associated(group, chan)
        return ret_val




    def is_wholeplot(self):
        """
        Is this a Wholeplot database?
        

        :returns:    1 if it is a Wholeplot database
                    0 if it is not.
        :rtype:      int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Currently checks to see if the DH_COLLAR line exists.
        """
        ret_val = self._is_wholeplot()
        return ret_val




    def put_chan_va(self, line, chan, va):
        """
        Place the contents of a `GXVA <geosoft.gxapi.GXVA>` in a channel.
        
        :param line:  Line
        :param chan:  Channel
        :param va:    `GXVA <geosoft.gxapi.GXVA>` from which to get the data
        :type  line:  int
        :type  chan:  int
        :type  va:    GXVA

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        .. seealso::

            `GXVA <geosoft.gxapi.GXVA>` class.
        """
        self._put_chan_va(line, chan, va)
        




    def set_group_class(self, symb, cl):
        """
        Set the Class name for a group line.
        
        :param symb:  Group line - `DB_LOCK_READWRITE <geosoft.gxapi.DB_LOCK_READWRITE>`
        :param cl:    `DB_GROUP_CLASS_SIZE <geosoft.gxapi.DB_GROUP_CLASS_SIZE>`
        :type  symb:  int
        :type  cl:    str

        .. versionadded:: 5.0.8

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** This method fails if the line is not a group line.
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
        self._set_group_class(symb, cl.encode())
        




    def set_va_prof_color_file(self, ch, file):
        """
        Set colors for a `GXVA <geosoft.gxapi.GXVA>` channel when displayed in the profile window.
        
        :param ch:    Channel (Locked `DB_LOCK_READWRITE <geosoft.gxapi.DB_LOCK_READWRITE>`)
        :param file:  Zone file name, "" to clear.
        :type  ch:    int
        :type  file:  str

        .. versionadded:: 5.1.5

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Fails in the channel is not an array channel, if the
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
        self._set_va_prof_color_file(ch, file.encode())
        




    def set_va_prof_sect_option(self, ch, option):
        """
        Set the display options of `GXVA <geosoft.gxapi.GXVA>` channels
        
        :param ch:      Channel (Locked `DB_LOCK_READWRITE <geosoft.gxapi.DB_LOCK_READWRITE>`)
        :param option:  Option  "Profile", "Section" or "Section and Profile"
        :type  ch:      int
        :type  option:  str

        .. versionadded:: 5.1.6

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._set_va_prof_sect_option(ch, option.encode())
        




    def set_va_scaling(self, ch, base, range):
        """
        Set base and range for `GXVA <geosoft.gxapi.GXVA>` channel cell display.
        
        :param ch:     Channel (Locked `DB_LOCK_READWRITE <geosoft.gxapi.DB_LOCK_READWRITE>`)
        :param base:   Base value (rDummy for none)
        :param range:  Range value (rDummy for none)
        :type  ch:     int
        :type  base:   float
        :type  range:  float

        .. versionadded:: 5.1.5

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** By default, `GXVA <geosoft.gxapi.GXVA>` profiles autoscale to fit in the database cell.
        This lets the user set a single base and range for all cells.
        If either input is a dummy, both are set as dummies, and autoscaling
        is used.
        """
        self._set_va_scaling(ch, base, range)
        




    def set_va_sect_color_file(self, ch, file):
        """
        Set colors for a `GXVA <geosoft.gxapi.GXVA>` channel when displayed section in the profile window.
        
        :param ch:    Channel (Locked `DB_LOCK_READWRITE <geosoft.gxapi.DB_LOCK_READWRITE>`)
        :param file:  Zone file name
        :type  ch:    int
        :type  file:  str

        .. versionadded:: 5.1.6

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Fails in the channel is not an array channel, if the
        file does not exist, or if it is not a valid color zone file.
        """
        self._set_va_sect_color_file(ch, file.encode())
        




    def set_va_windows(self, ch, min_w, max_w):
        """
        Set the range of windows to display for a `GXVA <geosoft.gxapi.GXVA>` channel.
        
        :param ch:     Channel (Locked `DB_LOCK_READWRITE <geosoft.gxapi.DB_LOCK_READWRITE>`)
        :param min_w:  First window (0 to N-1, iDummy for default)
        :param max_w:  Last window (0 to N-1, iDummy for default)
        :type  ch:     int
        :type  min_w:  int
        :type  max_w:  int

        .. versionadded:: 5.1.5

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Use to display a subset of the `GXVA <geosoft.gxapi.GXVA>` channel windows in the GDB.
        Windows index from 0.
        """
        self._set_va_windows(ch, min_w, max_w)
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer