
import os
import math
import numpy as np

import geosoft
import geosoft.gxapi as gxapi
from . import vv as gxvv
from . import va as gxva
from . import utility as gxu

__version__ = geosoft.__version__

# Constants

LINE_TYPE_NORMAL = gxapi.DB_LINE_TYPE_NORMAL
LINE_TYPE_BASE = gxapi.DB_LINE_TYPE_BASE
LINE_TYPE_TIE = gxapi.DB_LINE_TYPE_TIE
LINE_TYPE_TEST = gxapi.DB_LINE_TYPE_TEST
LINE_TYPE_TREND = gxapi.DB_LINE_TYPE_TREND
LINE_TYPE_SPECIAL = gxapi.DB_LINE_TYPE_SPECIAL
LINE_TYPE_RANDOM = gxapi.DB_LINE_TYPE_RANDOM

FORMAT_NORMAL = gxapi.DB_CHAN_FORMAT_NORMAL
FORMAT_EXP = gxapi.DB_CHAN_FORMAT_EXP
FORMAT_TIME = gxapi.DB_CHAN_FORMAT_TIME
FORMAT_DATE = gxapi.DB_CHAN_FORMAT_DATE
FORMAT_GEOGR = gxapi.DB_CHAN_FORMAT_GEOGR
FORMAT_SIGDIG = gxapi.DB_CHAN_FORMAT_SIGDIG
FORMAT_HEX = gxapi.DB_CHAN_FORMAT_HEX

CHAN_ALL = None     # matches all channel types
CHAN_NORMAL = 0     # non-array channels
CHAN_ARRAY = 1      # array channels
CHAN_DISPLAYED = 2  # displayed channels

SYMB_LINE_NORMAL = gxapi.DB_CATEGORY_LINE_NORMAL
SYMB_LINE_FLIGHT = gxapi.DB_CATEGORY_LINE_FLIGHT
SYMB_LINE_GROUP = gxapi.DB_CATEGORY_LINE_GROUP

SELECT_INCLUDE = gxapi.DB_LINE_SELECT_INCLUDE
SELECT_EXCLUDE = gxapi.DB_LINE_SELECT_EXCLUDE

COMP_NONE = gxapi.DB_COMP_NONE
COMP_SPEED = gxapi.DB_COMP_SPEED
COMP_SIZE = gxapi.DB_COMP_SIZE

READ_REMOVE_DUMMYROWS = 1
READ_REMOVE_DUMMYCOLUMNS = 2


class GDBException(Exception):
    '''
    Exceptions from this module.

    .. versionadded:: 9.1
    '''
    pass


def _(s):
    return s


def _va_width(data):
    if len(data.shape) == 1:
        width = 1
    elif len(data.shape) == 2:
        width = data.shape[1]
    else:
        raise GDBException(_("Only one or two-dimensional data allowed."))
    return width


class GXdb():
    '''
    Class to work with Geosoft databases. This class wraps many of the functions found in geosoft.gxapi.GXDB.

    Member ._db is the GXDB handle, which can be used to call gxapi methods.

    :constructor open: open  open an existing file, or if not specified open/lock the current database.

    :member fileName:  database file name

    **Some typical programming patterns**

    Python Oasis extension opens read through all data in the current database:

    .. code::

        import os,sys
        import numpy as np
        import gxpy.gx as gxp
        import gxpy.gdb as gxgdb

        # open the current database
        gdb = gxdb.GXdb.open(gxp)
        lines = gdb.lines()
        for line in lines:

            npd,ch,fid = gdb.read_line(line)
            # npd is a 2D numpy array to all data in this line.
            # ch is a list of the channels, one channel for each column in npd.
            # Array channels are expanded with channel names "name[0]", "name[1]" ...
            # fid is a tuple (start,increment) fiducial, which will be the minimum start and smallest increment.

            # ... do something with the data in npd ...

    External Python program to open and read through all data in a database:

    .. code::

        import os,sys
        import numpy as np
        import gxpy.gx as gxp
        import gxpy.gdb as gxgdb

        # initalize the gx environment - required for external programs.
        gxp = gxu.GXpy()

        # open a database
        gdb = gxdb.GXdb.open(gxp,'test.gdb')
        lines = gdb.lines()
        for line in lines:

            npd,ch,fid = gdb.read_line(line)
            # npd is a 2D numpy array to all data in this line.
            # ch is a list of the channels, one channel for each column in npd.
            # Array channels are expanded with channel names "name[0]", "name[1]" ...
            # fid is a tuple (start,increment) fiducial, which will be the minimum start and smallest increment.

            # ... do something with the data in npd ...

    The following creates a new channel that is the distance from the origin to the X,Y,Z location of every point.
    This code assumes that there are no dummies in the X, Y or Z channels (the next example shows how to
    deal with dummies).

    .. code::

        ...
        gdb = gxdb.GXdb.open(gxp,'test.gdb')
        lines = gdb.lines()
        for line in lines:

            npd,ch,fid = gdb.read_line(line, channels=['X','Y','Z'])

            squares = npd.square(npd)
            dist = np.sqrt(npd[0] + npd[1] + npd[2])

            gdb.write_channel(line, 'distance', dist, fid)

    Create a distance channel (as in previous example), with dummy handling:

    .. code::

        ...
        gdb = gxdb.GXdb.open(gxp,'test.gdb')
        lines = gdb.lines()
        for l in lines:

            ln, lsymb = gdb.line_name_symb(l)

            data, ch, fid = gdb.read_line(lsymb, channels=['X','Y','Z'])
            dummy = gxu.gx_dummy(data.dtype)

            # get a dummy mask, True for all rows with a dummy
            dummy_mask = gxu.dummy_mask(data)

            squares = npd.square(npd)
            dist = np.sqrt(npd[0] + npd[1] + npd[2])

            # insert dummies using the dummy mask, then write
            dist[dummy_mask] = dummy
            gdb.write_channel(lsymb, 'distance', dist)

    .. versionadded:: 9.1
    '''

    _edb = None
    _db = None
    _file_name = None

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self.__del__()

    def __repr__(self):
        return "{}({})".format(self.__class__, self.__dict__)

    def __str__(self):
        return os.path.basename(self._file_name)

    def __init__(self):
        self._lst = gxapi.GXLST.create(2000)
        self._sr = gxapi.str_ref()

    def __del__(self):
        if self._db is not None:
            if self._edb is not None:
                if self._edb.is_locked():
                    self._edb.un_lock()

    @classmethod
    def open(cls, name=None):
        '''
        Open an existing database.

        :param name:    name of the database, default is the current database
        :return:        GXdb instance

        .. versionadded:: 9.1
        '''

        gdb = cls()

        if name is None:
            gdb._edb = gxapi.GXEDB.current()
            gdb._db = gxapi.GXEDB.lock(gdb._edb)
        else:
            gdb._eDB = None
            gdb._db = gxapi.GXDB.open(name, 'SUPER', '')

        gxapi.GXDB.get_name(gdb._db, gxapi.DB_NAME_FILE, gdb._sr)
        gdb._file_name = os.path.normpath(gdb._sr.value)

        return gdb

    @classmethod
    def new(cls, name, maxLines=500, maxChannels=200, maxBlobs=0, pageSize=1024, comp=None):
        '''
        Create a new database.

        :param name:        database name
        :param maxLines:    maximum number of lines, default 500
        :param maxChannels: maximum number of channels, default 200
        :param maxBlobs:    maximum number of blobs, default lines*channels+20
        :param comp:        compression:
                            | COMP_NONE
                            | COMP_SPEED (default)
                            | COMP_SIZE

        .. versionadded:: 9.1
        '''
        maxLines = max(10, maxLines)
        maxChannels = max(25, maxChannels)
        minBlobs = maxChannels * maxLines + 20
        maxBlobs = max(minBlobs, maxBlobs)
        pageSize = min(max(pageSize, 64), 4096)
        if not comp:
            comp = COMP_SPEED

        gdb = cls()
        name = gdb._gdb_name(name)
        gxapi.GXDB.create_comp(name,
                               maxLines, maxChannels, maxBlobs, 10, 100,
                               'SUPER', '',
                               pageSize, comp)
        return(gdb.open(name))

    @staticmethod
    def _gdb_name(name):
        name = name.strip()
        nameExt = os.path.splitext(name)
        if nameExt[1].lower() == '.gdb':
            return name
        else:
            return os.path.normpath(name + ".gdb")

    def commit(self):
        '''
        Commit database changes.

        .. versionadded:: 9.1
        '''
        self._db.commit()

    def discard(self):
        '''
        Discard database changes.

        .. versionadded:: 9.1
        '''
        self._db.discard()

    # ============================================================================
    # internal helper functions

    def _exist_symb(self, symb, symb_type):
        '''
        Check if a symbol exists of the required type.
        :param symb: symbol name or number
        :param symb_type: one of DB_SYMB_TYPE
        :return: True if the symbol exists and is the expected symbol type, False otherwise

        .. versionadded:: 9.1
        '''
        if type(symb) is str:
            return self._db.exist_symb(symb, symb_type)
        else:
            return self._db.valid_symb(symb, symb_type)

    # ============================================================================
    # Information

    def file_name(self):
        '''
        :return: database file name

        .. versionadded:: 9.1
        '''
        return os.path.abspath(self._file_name)

    def line_name_symb(self, line, create=False):
        '''
        Return line name, symbol

        :param line:    line name, or symbol number
        :param create:  True to create a line if one does not exist
        :return:        line name, symbol, returns ('',-1) if invalid
        :raises:        GDBException if line not found or cannot be created

        .. versionadded:: 9.1
        '''

        if (self._exist_symb(line, gxapi.DB_SYMB_LINE)):
            if type(line) is str:
                symb = self._db.find_symb(line, gxapi.DB_SYMB_LINE)
                return line, symb
            else:
                self._db.get_symb_name(line, self._sr)
                return self._sr.value, line
        if create:
            return line, self.new_line(line)

        raise GDBException('Line \'{}\' not found'.format(line))

    def channel_name_symb(self, chan):
        '''
        Return channel name, symbol

        :param chan:    channel name, or symbol number
        :return:        line name, symbol, returns ('',-1) if invalid
        :raises:        GDBException if channel does not exist

        .. versionadded:: 9.1
        '''

        if (self._exist_symb(chan, gxapi.DB_SYMB_CHAN)):
            if type(chan) is str:
                symb = self._db.find_symb(chan, gxapi.DB_SYMB_CHAN)
                return chan, symb
            else:
                self._db.get_symb_name(chan, self._sr)
                return self._sr.value, chan

        raise GDBException('Channel \'{}\' not found'.format(chan))

    def channel_width(self, channel):
        '''
        Channel array width, 1 for normal channels, >1 for VA channels.

        :param channel: channel symbol or name
        :return:        array dimension, 1 for non-array channels

        .. versionadded:: 9.1
        '''
        return self._db.get_col_va(self.channel_name_symb(channel)[1])

    def list_channels(self, chan=None):
        '''
        Return a dict of channels in the database.

        :param chan: channel filter, default returns all channels

            =============== ============================
            CHAN_ALL        all channels, normal and VA
            CHAN_NORMAL     normal channels only
            CHAN_ARRAY      VA channels only
            =============== ============================

        :return: dictionary {channel_names: channel_symbols}

        .. versionadded:: 9.1
        '''

        def cleanChannelsDct():
            ''' returns list without any temporaty VA sliced channels '''
            self._db.chan_lst(self._lst)
            _dct = gxu.dict_from_lst(self._lst)
            dct = {}
            for k in _dct:
                if '[' in k:
                    continue
                dct[k] = _dct.get(k)
            return dct

        if chan == CHAN_ALL:
            dct = cleanChannelsDct()

        else:
            self._db.array_lst(self._lst)
            va = gxu.dict_from_lst(self._lst)
            if chan == CHAN_ARRAY:
                dct = va
            else:
                # filter VA channels out of the list
                all = cleanChannelsDct()
                va = list(va)
                dct = {}
                for k in all:
                    if not(k in va):
                        dct[k] = all.get(k)

        # convert symbol strings to ints
        for k in dct:
            dct[k] = int(dct.get(k))

        return dct

    def list_lines(self, select=True):
        '''
        List of lines in the database
        :param select=True:  True to return selected lines, false to return all lines
        :return: dictionary (line name: symbol)

        .. versionadded:: 9.1
        '''
        if select:
            self._db.selected_line_lst(self._lst)
        else:
            self._db.line_lst(self._lst)
        dct = gxu.dict_from_lst(self._lst)
        for k in dct:
            dct[k] = int(dct.get(k))
        return dct

    def line_details(self, line):
        '''
        Return dictionary of line details

        :param line: channel name or symbol
        :return: dictionary:

            =========== ==============================================================
            Key         Meaning
            =========== ==============================================================
            name        line name
            symbol      line symbol
            type        line type, one of gxapi.DB_LINE_TYPE
            category    one of SYMB_LINE
            date        date of the line
            number      numeric line number
            flight      flight number
            version     line version number
            groupclass  class name for grouped lines, '' if not a grouped line
            =========== ==============================================================

        .. versionadded:: 9.1
        '''

        def get_detail(fn):
            try:
                fn(ls, self._sr)
                return self._sr.value
            except geosoft.gxapi.GXAPIError:
                return ''

        ln, ls = self.line_name_symb(line)
        detail = {}
        self._lock_read(ls)
        try:
            detail['name'] = ln
            detail['symbol'] = ls
            detail['category'] = self._db.line_category(ls)
            detail['date'] = self._db.line_date(ls)
            detail['flight'] = self._db.line_flight(ls)
            detail['number'] = self._db.line_number(ls)
            detail['version'] = self._db.line_version(ls)
            detail['type'] = self._db.line_type(ls)
            detail['groupclass'] = get_detail(self._db.get_group_class)

        except:
            self._unlock(ls)
            raise

        return detail

    def channel_details(self, channel):
        '''
        Return dictionary of channel details

        :param channel: channel name or symbol
        :return:        dictionary:

            ======= ==============================================================
            Key     Meaning
            ======= ==============================================================
            name    channel name
            symbol  channel symbol
            class   class name
            format  format, one of gxapi.DB_CHAN_FORMAT constants
            width   display width in characters
            decimal decimal places to display
            unit    measurement unit
            label   channel label, which can be different from the channel name
            protect proptection: 0 can be modified; 1 protected from modification
            columns number data columns, 1 for normal channels, n for VA channels
            type    data type, one of gxapi.DB_CATEGORY_CHAN constants
            ======= ==============================================================

        .. versionadded:: 9.1
        '''

        def get_detail(fn):
            fn(cs, self._sr)
            return self._sr.value

        cn, cs = self.channel_name_symb(channel)
        detail = {}
        self._lock_read(cs)
        try:
            detail['name'] = cn
            detail['symbol'] = cs
            detail['class'] = get_detail(self._db.get_chan_class)
            detail['format'] = self._db.get_chan_format(cs)
            detail['width'] = self._db.get_chan_width(cs)
            detail['decimal'] = self._db.get_chan_decimal(cs)
            detail['unit'] = get_detail(self._db.get_chan_unit)
            detail['label'] = get_detail(self._db.get_chan_label)
            detail['protect'] = self._db.get_chan_protect(cs)
            detail['array'] = self.channel_width(cs)
            detail['type'] = self._db.get_chan_type(cs)
        except:
            self._unlock(cs)
            raise

        return detail

    def set_channel_details(self, channel, detail):
        '''
        Set/change channel details from dictionary

        :param channel: channel name or symbol
        :param detail:  dictionary, see chan_details

        .. versionadded:: 9.1
        '''

        def set_detail(what, fn):
            det = detail.get(what)
            if det is not None:
                fn(cs, det)

        cs = self.channel_name_symb(channel)[1]
        self._lock_write(cs)
        try:
            set_detail('class', self._db.set_chan_class)
            set_detail('format', self._db.set_chan_format)
            set_detail('width', self._db.set_chan_width)
            set_detail('decimal', self._db.set_chan_decimal)
            set_detail('unit', self._db.set_chan_unit)
            set_detail('label', self._db.set_chan_label)

            protect = detail.get('protect')
            if protect is not None:
                self._db.set_chan_protect(cs, protect)

        except:
            self._unlock(cs)
            raise

    def channel_dtype(self, channel):
        '''
        Returns channel numpy dtype

        :param channel: channel name or symbol
        :return:        numpy dtype

        .. versionadded:: 9.1
        '''
        return gxu.dtype_gx(self._db.get_chan_type(self.channel_name_symb(channel)[1]))

    def channel_fid(self, line, channel):
        '''
        Return the fiducial of a line, channel

        :param line:    line name or symbol
        :param channel: channel name or symbol
        :return:        (start,increment)
        '''
        ls = self.line_name_symb(line)[1]
        cs = self.channel_name_symb(channel)[1]
        self._lock_read(cs)
        try:
            fidStart = self._db.get_fid_start(ls, cs)
            fidIncr = self._db.get_fid_incr(ls, cs)
        except:
            self._unlock(cs)
            raise

        self._unlock(cs)
        return (fidStart, fidIncr)

    # ========================================================================================
    # management

    def new_channel(self, name, dtype=np.float64, array=1, details={'width': 12, 'decimal': 2}):
        '''
        Return a channel symbol, create if it does not exist.

        :param name:        channel name
        :param dtype:       numpy dtype (ie. np.int64)
        :param array:       array columns (default is 1)
        :param details:     dictionary containing channel details, see channel_details()

        :return:            channel symbol

        Examples:

        ..code::

            symb = gdb.newChan('X')
            symb = gdb.newChan('X', dtype=np.float64, details={'decimal':4})

        .. versionadded:: 9.1
        '''

        symb = self._db.find_symb(name, gxapi.DB_SYMB_CHAN)
        if symb == gxapi.NULLSYMB:
            symb = self._db.create_symb_ex(name,
                                           gxapi.DB_SYMB_CHAN,
                                           gxapi.DB_OWN_SHARED,
                                           gxu.gx_dtype(dtype),
                                           array)

        if details:
            self.set_channel_details(symb, details)

        return symb

    def new_line(self, line, linetype=None, group=''):
        '''
        Get a line symbol.  If line exists an error is raised.

        :param line:        line name
        :param linetype:    line type for creating a new line, ignored if group defines

            ================= =========================================
            SYMB_LINE_NORMAL  normal lines, name is a string
            SYMB_LINE_FLIGHT  flight lines, first letter is line type
            ================= =========================================

        :param group:       group name for a grouped class

        :return:            line symbol

        .. versionadded:: 9.1
        '''

        if not self._db.is_line_name(line):
            raise GDBException('Invalid line name \'{}\''.format(line))

        symb = self._db.find_symb(line, gxapi.DB_SYMB_LINE)
        if symb != gxapi.NULLSYMB:
            raise GDBException('Cannot create existing line \'{}\''.format(line))

        if len(group) > 0:
            linetype = SYMB_LINE_GROUP
        elif not linetype:
            linetype = SYMB_LINE_NORMAL

        symb = self._db.create_symb_ex(line,
                                       gxapi.DB_SYMB_LINE,
                                       gxapi.DB_OWN_SHARED,
                                       linetype,
                                       0)
        if len(group) > 0:
            self._lock_write(symb)
            try:
                self._db.set_group_class(symb, group)
            except geosoft.gxapi.GXAPIError:
                self._unlock(symb)
            except:
                self._unlock(symb)
                raise

        return symb

    def delete_channel(self, channels):
        '''
        Delete channel(s) by name or symbol.

        :param channels: channel name or symbol, or a list of channel names or symbols

        .. versionadded:: 9.1
        '''

        if type(channels) is str:
            channels = [channels]

        self._db.un_lock_all_symb()
        for s in channels:
            try:
                cn, cs = self.channel_name_symb(s)
                self._lock_write(cs)
                self._db.delete_symb(cs)
            except GDBException:
                continue

    def delete_line(self, s):
        '''
        Delete a line by name or symbol.

        :param s: line name or symbol

        .. versionadded:: 9.1
        '''
        if type(s) is str:
            s = self._db.find_symb(s, gxapi.DB_SYMB_LINE)
            if s == gxapi.NULLSYMB:
                return
        self._lock_write(s)
        self._db.delete_symb(s)

    def select_lines(self, selection='', select=True):
        '''
        Change selected state of a line, or group of lines
        :param selection:   string representing selection, comma-delimit multiple selections
        :param select=True: True to select, False to deselect

        "L99:800" will select all lines of type "L" in range 99 through 800.

        | Use a "T" prefix for Tie lines.
        | Use an "F" prefix to specify lines of a specific flight.
        |    For example, "F10" would select all lines of flight 10.
        | Use an empty string ("") to select/deselect ALL lines.

        .. versionadded:: 9.1
        '''

        for s in selection.split(','):
            if select:
                self._db.select(s, gxapi.DB_LINE_SELECT_INCLUDE)
            else:
                self._db.select(s, gxapi.DB_LINE_SELECT_EXCLUDE)

    # =====================================================================================
    # reading and writing

    def _lock_read(self, s):
        try:
            self._db.lock_symb(s, gxapi.DB_LOCK_READONLY, gxapi.DB_WAIT_INFINITY)
        except GDBException:
            raise GDBException('Cannot read lock symbol {}'.format(s))

    def _lock_write(self, s):
        try:
            self._db.lock_symb(s, gxapi.DB_LOCK_READWRITE, gxapi.DB_WAIT_INFINITY)
        except GDBException:
            raise GDBException('Cannot write lock symbol {}'.format(s))

    def _unlock(self, s):
        try:
            self._db.un_lock_symb(s)
        except GDBException:
            pass

    def vv_np(self, npdata, fid=(0.0, 1.0)):
        ''' return a VV copy of the numpy data.'''
        vv = gxapi.GXVV.create_ext(gxu.gx_dtype(npdata.dtype), 0)
        try:
            vv.set_data_np(0, npdata)
        except:
            vv.destroy()
            raise
        vv.set_fid_start(fid[0])
        vv.set_fid_incr(fid[1])
        return vv

    def _vaNp(self, npdata, fid=(0.0, 1.0)):
        ''' return a VA copy of data in a 2D numpy array.'''
        va = gxapi.GXVA.create_ext(gxu.gx_dtype(npdata.dtype), npdata.shape[0], npdata.shape[1])
        try:
            va.set_array_np(0, 0, npdata)
        except:
            va.destroy()
            raise
        va.set_fid_start(fid[0])
        va.set_fid_incr(fid[1])
        return va

    def _vv_ch(self, ls, cs, dtype=None):
        ''' return a VV of data from channel cs.'''

        if dtype is None:
            dtype = self.channel_dtype(cs)
        vv = gxvv.GXvv(dtype)
        self._lock_read(cs)
        try:
            self._db.get_chan_vv(ls, cs, vv._vv)
        except:
            self._unlock(cs)
            raise
        self._unlock(cs)
        return vv

    def _va_ch(self, ls, cs, dtype=None):
        ''' return a VA of data from channel cs.'''

        if dtype is None:
            dtype = self.channel_dtype(cs)
        w = self.channel_width(cs)
        va = gxva.GXva(w, dtype)
        self._lock_read(cs)
        try:
            self._db.get_chan_va(ls, cs, va._va)
        except:
            self._unlock(cs)
            raise
        self._unlock(cs)
        return va

    def _sorted_chan_list(self):

        ch = list(self.list_channels())
        ch.sort(key=str.lower)
        channels = []

        # put x,y,z at the front
        try:
            nX, sX = self.channel_name_symb(self._db.get_xyz_chan_symb(gxapi.DB_CHAN_X))
            channels.append(nX)
        except GDBException:
            nX = ''
        try:
            nY, sY = self.channel_name_symb(self._db.get_xyz_chan_symb(gxapi.DB_CHAN_Y))
            channels.append(nY)
        except GDBException:
            nY = ''
        try:
            nZ, sZ = self.channel_name_symb(self._db.get_xyz_chan_symb(gxapi.DB_CHAN_Z))
            channels.append(nZ)
        except GDBException:
            nZ = ''

        for c in ch:
            if (c == nX) or (c == nY) or (c == nZ):
                continue
            channels.append(c)

        return channels

    def _expand_chan_list(self, channels):
        """ expand VA channels and return lists of names, symbols and types"""

        chNames = []
        chSymbs = []
        cType = []
        for c in channels:
            cn, cs = self.channel_name_symb(c)
            w = self.channel_width(cs)
            if w == 1:
                chNames.append(cn)
                chSymbs.append(cs)
                cType.append(self._db.get_chan_type(cs))
            else:
                for i in range(w):
                    ccn, ccs = self.channel_name_symb("{}[{}]".format(cn, i))
                    chNames.append(ccn)
                    chSymbs.append(ccs)
                    cType.append(self._db.get_chan_type(cs))

        return chNames, chSymbs, cType

    def read_channel(self, line, channel, dtype=None):
        '''
        Read data from a single channel.

        :param line:    line name or symbol
        :param channel: channel name or symbol
        :param dtype:   type wanted, default same as the channel data

        :return:        numpy data, fid (start, increment)

        .. versionadded:: 9.1
        '''

        ln, ls = self.line_name_symb(line, create=True)
        cn, cs = self.channel_name_symb(channel)

        if self.channel_width(cs) == 1:
            vv = self._vv_ch(ls, cs, dtype)
            return vv.np(vv.dtype())[0], vv.fid()

        else:
            va = self._va_ch(ls, cs, dtype)
            return va.np(va.dtype())[0], va.fid()

    def read_line(self, line, channels=None, dtype=None, fid=None, dummy=None):
        '''
        Read a line of data into a numpy array.

        :param line:        line to read, string or symbol number
        :param channels:    list of channels, strings or symbol number.  If empty, read all channels
        :param dtype:       numpy data type for the array, default np.float64 for multi-channel data,
                            data type for single channel data. Use "<Unnn" for string type.
        :param fid:         required fiducial as tuple (start,incr), default smallest in data
        :param dummy:       dummy_handling for multi-channel read, default leaves dummies in place:

            ======================== ===================================================
            READ_REMOVE_DUMMYROWS    remove rows with dummies, fiducials lose meaning
            READ_REMOVE_DUMMYCOLUMNS remove columns with dummies
            ======================== ===================================================

        :return: 2D numpy array shape(records,channels), list of channel names, (fidStart,fidIncr)
        :raises: GDBException if first channel requested is empty

        VA channels are expanded by element with channel names name[0], name[1], etc.

        Examples:

        .. code::

            # npd - returned numpy array shape (n, number of channels)
            # ch  - list of returned channels names, array channels expanded to array[0], array[1], ...
            # fid - tuple (fidStart,fidIncrement), channels resampled as necessary

            npd,ch,fid = gdb.read_line('L100')                           # read all channels in line "L100"
            npd,ch,fid = gdb.read_line(681)                              # read all channels in line symbol 681
            npd,ch,fid = gdb.read_line('L100','X')                       # read channel 'X' from line 'L100'
            npd,ch,fid = gdb.read_line('L100',2135)                      # read channel symbol 2135 from 'L100"
            npd,ch,fid = gdb.read_line('L100',channels=['X','Y','Z'])    # read a list of channels to (n,3) array
            npd,ch,fid = gdb.read_line('L100','X',np.int32)              # read channel 'X' into integer array

        .. versionadded:: 9.1
        '''

        ln, ls = self.line_name_symb(line)

        # default all channels, sorted, X,Y,Z first
        if channels is None:
            channels = self._sorted_chan_list()

        else:
            if (type(channels) is str) or (type(channels) is int):
                channels = [channels]

        # just one channel
        if len(channels) == 1:
            npd, fid = self.read_channel(ls, channels[0], dtype)
            if self.channel_width(channels[0]) == 1:
                npd = npd.reshape(npd.shape[0], 1)  # make it a 2D array
            else:
                channels = self._expand_chan_list(channels)[0]
            return npd, channels, fid

        # multiple channels
        # make up channel list, expanding VA channels
        chNames, chSymb, cType = self._expand_chan_list(channels)

        if dtype is None:
            dtype = np.float64
        vvs = []
        for c in chNames:
            cs = self._db.find_symb(c, gxapi.DB_SYMB_CHAN)
            vv = self._vv_ch(ls, cs, dtype=dtype)
            vvs.append(vv)

        # determine fiducial range from data
        start = gxapi.GS_R8MX
        incr = gxapi.GS_R8MX
        fend = gxapi.GS_R8MN
        for vv in vvs:
            fd = vv.fid()
            if fd[0] != gxapi.rDUMMY:
                if fd[0] < start:
                    start = fd[0]
                if fd[1] < incr:
                    incr = fd[1]
                dend = start + incr * (vv.length() - 1)
                if dend > fend:
                    fend = dend
        if fid is None:
            fid = (start, incr)

        # there has to be some data
        nvd = math.ceil((fend - start) / incr) + 1
        if (fend == gxapi.GS_R8MN) or (nvd == 0):
            raise GDBException(_("Line {} is empty for channels {}").format(ln, chNames[0]))

        # refid everything
        nCh = len(chNames)
        for vv in vvs:
            vv.reFid(fid, nvd)
            vv.reFid(fid, nvd)

        # move data to numpy array
        npd = np.empty((nvd, nCh), dtype=dtype)
        dummy_value = gxu.gx_dummy(npd.dtype)
        for j in range(nCh):
            vv = vvs[j]
            if vv.length() > 0:
                npd[:, j] = vv.np(dtype=npd.dtype)[0]
            else:
                npd[:, j].fill(dummy_value)

        # dummy handling
        if dummy:
            dummy_value = gxu.gx_dummy(npd.dtype)
            if dummy == READ_REMOVE_DUMMYCOLUMNS:
                n_ok = 0

                # shift data and channel names to remove columns containing a dummy
                for i in range(nCh):
                    if dummy_value in npd[:, i]:
                        continue
                    if n_ok != i:
                        npd[:, n_ok] = npd[:, i]
                        chNames[n_ok] = chNames[i]
                    n_ok += 1
                if n_ok != nCh:
                    npd = npd[:, 0:n_ok]
                    chNames = chNames[0:n_ok]

            elif dummy == READ_REMOVE_DUMMYROWS:

                mask = np.apply_along_axis(lambda a: not (dummy_value in a), 1, npd)
                npd = npd[mask, :]
                fid = (0.0, 1.0)

            else:
                raise GDBException(_('Unrecognized dummy={}').format(dummy))

        return npd, chNames, fid

    def write_channel(self, line, channel, data, fid=(0.0, 1.0)):
        '''
        Write data to a single channel.

        :param line:    line name or symbol
        :param channel: channel name or symbol
        :param data:    numpy array (2D for VA channel)
        :param fid:     tuple (fid start, increment), default (0.0,1.0)

        .. versionadded:: 9.1
        '''

        def cleanup():
            self._unlock(cs)

        ln, ls = self.line_name_symb(line, create=True)

        try:
            cn, cs = self.channel_name_symb(channel)

        except GDBException:
            if type(channel) is str:
                cn = channel
                cs = self.new_channel(channel, data.dtype, array=_va_width(data))

        w = self.channel_width(cs)
        if w != _va_width(data):
            raise GDBException(
                _("Array data width {} does not fit into VA channel '{}' with width {}").
                format(_va_width(data), cn, w))

        # 1D channel
        if w == 1:

            # get a VV of the data
            vv = self.vv_np(data, fid)

            self._lock_write(cs)
            try:
                self._db.put_chan_vv(ls, cs, vv)
            except:
                cleanup()
                raise

        else:

            # get a VA of the data
            va = self._vaNp(data, fid)

            self._lock_write(cs)
            try:
                self._db.put_chan_va(ls, cs, va)
            except:
                cleanup()
                raise

        cleanup()

    def write_line(self, line, data, channels=None, fid=(0.0, 1.0)):
        '''
        Write data to a multiple channels in a line.  If no channel list is provided it assumes that the
        data is for all channels from the line, the compliment of readDataLine().

        :param line:        line to write to, name or symbol
        :param data:        numpy array shape (records,channels).  If single dimension, one channel
        :param channels:    channel name or symbol list, or a single name/symbol.  If a single name is specified
                            for multi-column data, a VA channel is assumed.
        :param fid:         option fid tupple (start, increment), default (0.0,1.0)

        .. versionadded:: 9.1
        '''

        if type(channels) is str:
            self.write_channel(line, channels, data, fid=fid)

        else:
            if channels is None:
                channels = self._sorted_chan_list()

            np_index = 0
            for chan in channels:
                try:
                    ch, cs = self.channel_name_symb(chan)
                    w = self.channel_width(cs)
                except GDBException:
                    w = 1
                    cs = chan
                self.write_channel(line, cs, data[:, np_index: np_index + w], fid=fid)
                np_index += w

            # error if there is any data left
            if np_index - data.shape[1] != 0:
                raise GDBException(_('More data than channels, but data up to channels was written out.'))

    def list_values(self, chan, max=1000, selected=True, dupl=50, progress=None, stop=None):
        '''
        Build a list of unique values in a channel.  Uniqueness depends on the current display format for
        the field.

        :param chan:            channel to scan
        :param max=1000:        maximum values allowed, once this maximum is reached scanning stops
        :param selected=True:   True to scan only selected lines
        :param dupl:            Stop growing list after this many lines fail to grow the list, 0 scans all lines
        :param progress:        progress reporting function
        :param stop:            stop check function
        :return:                list of values, represented as a string

        .. versionadded:: 9.1
        '''

        lines = list(self.list_lines(select=selected))
        cn, cs = self.channel_name_symb(chan)
        details = self.channel_details(cs)
        dtype = np.dtype('<U{}'.format(details.get('width')))
        lines.sort(key=str.lower)
        set = []
        n = 0
        nset = -1
        ndup = 0
        for l in lines:

            try:
                d, c, f = self.read_line(l, cs, dtype=dtype)
            except GDBException:
                continue

            if d.shape[0] == 0:
                continue

            d = np.unique(d)
            set = np.append(set, d)
            set = np.unique(set)

            if set.shape[0] > max:
                break
            if dupl > 0:
                if (set.shape[0] == nset):
                    ndup += 1
                    if ndup > dupl:
                        break
                else:
                    ndup = 0
            nset = set.shape[0]

            n += 1
            if progress:
                progress('Scaning unique values in "{}", {}'.format(cn, str(l)), (n * 100.0) / len(lines))
            if stop:
                if stop():
                    return set.tolist()

        if set.shape[0] > max:
            set = set[:max]

        return set.tolist()
