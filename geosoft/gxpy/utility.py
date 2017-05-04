"""
Utility functions to support Geosoft Python scripts and modules.

.. note::

    Regression tests provide usage examples: `Tests <https://github.com/GeosoftInc/gxpy/blob/master/geosoft/gxpy/tests/test_utility.py>`_

"""

import math
import decimal
import os
import uuid as uid
import json
import datetime
import subprocess
import binascii
from time import gmtime, strftime
from ._jdcal.jdcal import is_leap, gcal2jd, jd2gcal
from distutils.version import StrictVersion
import numpy as np
from collections import OrderedDict

import geosoft
import geosoft.gxapi as gxapi

__version__ = geosoft.__version__


def _t(s):
    return geosoft.gxpy.system.translate(s)


# cached lookup tables
_dummy_map = {}
_gx2np_type = {}
_np2gx_type = {}

# Assign to valid path to override the Geosoft temporary file folder
_temp_folder_override = None

# Assign callable to override unique ID generation
_uuid_callable = None

class UtilityException(Exception):
    """
    Exceptions from this module.

    .. versionadded:: 9.1
    """
    pass


def check_version(v, raise_on_fail=True):
    """
    Check the minimum API version.

    :param v:               minimum version string required (ie "9.1" or "9.2.4")
    :param raise_on_fail:   if True, raises an error if the version check fails, returns False otherwise
    :return:                True if version is OK, False otherwise(unless raise_on_fail is False)

    .. note::  
        A valid version consists of two or three dot-separated numeric components, with an optional development version tag
        on the end.  The development version tag consists of the letter 'b' (for beta) followed by a number.  If the numeric components 
        of two version numbers are equal, then a development version will always be deemed earlier (lesser) than one without.

        The following are valid version numbers (shown in order of used for meeting minimum requirements):

            * 9.1 or 9.1.0  (they are equivalent)
            * 9.1.1b0 (development version)
            * 9.1.1
            * 9.2

        The following are examples of invalid version numbers:

            * 1
            * 2.7.2.2
            * 1.3.a4
            * 1.3pl1
            * 1.3c4

        The rationale for this version numbering system is explained
        in the `distutils <https://docs.python.org/3/distutils/>`_ documentation.

    .. versionadded:: 9.1

    """

    if StrictVersion(__version__) >= StrictVersion(str(v)):
        return True
    if raise_on_fail:
        raise UtilityException(_t("GX API version {} or higher is required.").format(v))
    return False


def dict_from_lst(lst, ordered=False):
    """
    :param lst:     gxapi.GXLST instance
    :param ordered: True to return an OrderedDict
    :return:        python dictionary from a Geosoft GXLST

    .. versionadded:: 9.1

    """
    key = gxapi.str_ref()
    val = gxapi.str_ref()
    if ordered:
        dct = OrderedDict()
    else:
        dct = {}
    for item in range(lst.size()):
        lst.gt_item(0, item, key)
        lst.gt_item(1, item, val)
        dct[key.value] = val.value
    return dct


def time_stamp():
    return strftime("%Y-%m-%d %H:%M:%S", gmtime())


def yearFromJulianDay2(jd1, jd2):
    """
    :param jd1: part 1 Julian date (https://pypi.python.org/pypi/jdcal)
    :param jd2: part 2 Julian date
    :return: decimal Gregorian year (Western calendar year)

    .. versionadded:: 9.1
    """
    y, m, d, f = jd2gcal(jd1, jd2)
    jdt_1, jdt_2 = gcal2jd(y, 1, 1)
    day_diff = (jd1 - jdt_1) + (jd2 - jdt_2)
    return y + (day_diff / (366 if is_leap(y) else 365))


def rdecode_err(s):
    """
    Geosoft string conversion to a number, raising ValueError on failure

    :param s: string to be decoded
    :return: float of decoded string

    If unable to decode string:
        | rdecode_err()   raises ValueError
        | rdecode()       returns gxapi.rDUMMY

    Any string that begins with "*" character is interpreted as a dummy.

    If unable to directly convert simple string, decoder will clean-up the string by
    removing leading/trailing white space and converting 'o' or 'O' to numeral '0'.

    If decoder still fails, it will attempt to decode time and geographic formatted
    strings to return decimal hours or decimal degrees respectively:

    :date:
        | yyyy-mm-dd
        | yyyy/mm/dd
        | date will be fractional Gregorian year

    :time:
        | hh:mm:ss.ssAM/am
        | hh:mm:ss.ssPM/pm
        | PM/pm adds 12 hours (for example 2:30pm returns 14.5)

    :geographic:
        | [+/-]deg mm ss.ss[N/S/E/W/n/s/e/w]
        | [+/-]deg.mm.ss.ss[N/S/E/W/n/s/e/w]
        | S/s and W/w return negative of decoded value
        |
        | Example:
        | "-90 15 18.0" = "90 15 18.0W" = "90.15.18w", returns -90.255
        | "14" = "14N" = "14.00.00" = "14 00 00", returns 14.0

    Note that mm and ss.ss can go over 60.0 and will be decoded as minutes or seconds
    as presented. For example, "20 90 0.00" will return 21.5.

    .. versionadded:: 9.1
    """

    # nothing there, or a dummy
    if (not s) or (s[0] == '*'):
        return gxapi.rDUMMY

    # try floating point
    try:
        return float(s)

    except ValueError:

        # date
        if (len(s) >= 8) and (s[4:5] in '/-'):
            s = s[0:10]
            try:
                smonth = s[5:7]
                if smonth[-1] in '/-':
                    smonth = smonth[0]
                    sday = s[7:]
                else:
                    sday = s[8:10]
                j1, j2 = gcal2jd(s[:4], smonth, sday)
                return yearFromJulianDay2(j1, j2)
            except:
                raise ValueError

        # tabs are spaces, trim leading white space
        ss = s.replace("\t", " ")
        ss = ss.lstrip()
        ss = ss.rstrip()

        # replace mistyped "o", "O"
        ss = ss.replace("o", "0")
        ss = ss.replace("O", "0")

        # nothing there, or a dummy
        if (not ss) or (ss[0] == '*'):
            return gxapi.rDUMMY

        try:

            return float(ss)

        except ValueError:

            # look for time or geographic format - two spaces become dots
            sg = ss.replace(' ', '.', 2)
            sg = sg.replace(':', '.', 2)
            if ' ' in sg:  # ok, this string is messed up
                raise ValueError
            sg = sg.upper()
            twelve = 0.0
            negsuf = negpre = 1.0
            suf = sg[len(sg) - 1]
            if (suf == 'S') or (suf == 'W'):
                negsuf = -1.0
            if sg[0] == '-':
                negpre = -1.0
                sg = sg[1:]
            else:
                if 'PM' in sg:
                    twelve = 12.0
            sg = sg.rstrip("NSEWAMP")
            dms = sg.split('.', 2)
            degrees = float(dms[0])
            if len(dms) > 1:
                minutes = float(dms[1])
            else:
                minutes = 0.0
            if len(dms) > 2:
                seconds = float(dms[2])
            else:
                seconds = 0.0
            return (degrees + (minutes + seconds / 60.0) / 60.0) * negpre * negsuf + twelve


def rdecode(s):
    """
    Geosoft string (number, date, time, geographic) conversion to a number, always works.

    :param s:   string to decode
    :return:    decoded number, gxapi.rDUMMY if unable to decode the string

    See rdecode_err(string) for more details.

    .. versionadded:: 9.1
    """

    try:
        return (rdecode_err(s))
    except ValueError:
        return (gxapi.rDUMMY)


def decode(s, f):
    """
    Decode a string (s) to a numpy format defined by string (f).

    :param s:   string to decode
    :param f:   format string:

        === ================================================
        b	Boolean
        i	(signed) integer
        u	unsigned integer
        f	floating-point
        S   string, interpreted as 'U' unicode
        a	string, interpreted as 'U' unicode
        U	unicode, requires length suffix, ie 'U1', 'U14'
        === ================================================

    :times:
        Times in the form hh:mm:ss.sss return a decimal hour.

    :dates:
        Dates in form yyyy-mm-dd, yyyy-m-d, yy/mm/dd or yyyy/m/d will be decoded naturally
        and return a decimal Gregorian year. Other date formats will raise a ValueErr.

    :Errors:
        ========== ======================================
        TypeError  if unable to recognize type
        ValueError if there is a problem with the string.
        ========== ======================================

    .. versionadded:: 9.1
    """

    # always use Unicode for strings
    if f[0] in "Sa":
        f = 'U' + f[1:]

    # handle strings
    if f[:1] == 'U':
        if len(f) < 2:
            raise TypeError
        type(f)  # to insure valid type
        return s[0:int(f[1:])]

    # not currently supporting complex
    if f[0] == 'c':
        raise TypeError

    type(f)  # raises error if unknown type

    r = rdecode_err(s)
    if f[0] == 'f':
        return r

    # boolean
    if f[0] == 'b':
        if r == gxapi.rDUMMY:
            return False
        else:
            return not (int(round(r)) == 0)

    # everything else is returned as an int
    if r == gxapi.rDUMMY:
        return gxapi.GS_S4DM
    return int(round(r))


def display_message(title, message):
    """
    Display a message to the user.

    :param title:   message title
    :param message: message

    .. versionadded:: 9.1
    """

    try:
        gxapi.GXSYS.display_message(title, message)
    except geosoft.gxapi.GXAPIError:
        print('Title: {}\nMessage: {}'.format(title, message))


def gx_dtype(dtype):
    """
    :return:    GX type for a numpy dtype

    .. versionadded:: 9.1
    """

    global _np2gx_type
    if not bool(_np2gx_type):
        _np2gx_type = {
            str(np.dtype(np.float)): gxapi.GS_DOUBLE,
            str(np.dtype(np.int)): gxapi.GS_LONG,
            str(np.dtype(np.byte)): gxapi.GS_BYTE,
            str(np.dtype(np.float64)): gxapi.GS_DOUBLE,
            str(np.dtype(np.float32)): gxapi.GS_FLOAT,
            str(np.dtype(np.int64)): gxapi.GS_LONG64,
            str(np.dtype(np.int32)): gxapi.GS_LONG,
            str(np.dtype(np.int16)): gxapi.GS_SHORT,
            str(np.dtype(np.int8)): gxapi.GS_BYTE,
            str(np.dtype(np.uint8)): gxapi.GS_UBYTE,
            str(np.dtype(np.uint16)): gxapi.GS_USHORT,
            str(np.dtype(np.uint32)): gxapi.GS_ULONG,
            str(np.dtype(np.uint64)): gxapi.GS_ULONG64}

    if dtype is None:
        return gxapi.GS_TYPE_DEFAULT
    dtype = np.dtype(dtype)
    try:
        return (_np2gx_type[str(dtype)])
    except KeyError:
        if dtype.type is np.str_:
            return -(int(dtype.str[2:]))


def dtype_gx(gtype):
    """
    :return:    numpy dtype from a GX type

    .. versionadded:: 9.1
    """

    global _gx2np_type
    if not bool(_gx2np_type):
        _gx2np_type = {
            gxapi.GS_TYPE_DEFAULT: None,
            gxapi.GS_DOUBLE: np.dtype(np.float),
            gxapi.GS_FLOAT: np.dtype(np.float32),
            gxapi.GS_LONG64: np.dtype(np.int64),
            gxapi.GS_LONG: np.dtype(np.int32),
            gxapi.GS_BYTE: np.dtype(np.byte),
            gxapi.GS_SHORT: np.dtype(np.int16),
            gxapi.GS_UBYTE: np.dtype(np.uint8),
            gxapi.GS_USHORT: np.dtype(np.uint16),
            gxapi.GS_ULONG: np.dtype(np.uint32),
            gxapi.GS_ULONG64: np.dtype(np.uint64)}
    try:
        return _gx2np_type[gtype]
    except KeyError:
        if gtype < 0:
            return np.dtype('U{}'.format(-gtype))


def is_float(gxtype):
    """ Return True of gxtype can be stored in a 64-bit float"""
    if gxtype >= 0 and gxtype in {gxapi.GS_DOUBLE, gxapi.GS_FLOAT}:
        return True
    else:
        return False


def is_int(gxtype):
    """ Return True of gxtype can be stored in a 64-bit integer"""
    if gxtype >= 0 and not is_float(gxtype):
        return True
    else:
        return False


def is_string(gxtype):
    """ Return length of a gxtype string, 0 (False) if not a string."""
    if gxtype < 0:
        return -gxtype
    else:
        return False


def gxDummy(dtype):
    """
    .. deprecated:: 9.2 use gx_dummy()
    """
    return gx_dummy(dtype)


def gx_dummy(dtype):
    """
    :return:    GX dummy for this dtype

    .. versionadded:: 9.2
    """
    global _dummy_map
    if not bool(_dummy_map):
        _dummy_map = {
            np.dtype(np.float): gxapi.rDUMMY,
            np.dtype(np.float64): gxapi.rDUMMY,
            np.dtype(np.float32): gxapi.rDUMMY,
            np.dtype(np.int): gxapi.iDUMMY,
            np.dtype(np.int64): gxapi.iDUMMY,
            np.dtype(np.int8): gxapi.GS_S1DM,
            np.dtype(np.int16): gxapi.GS_S2DM,
            np.dtype(np.int32): gxapi.GS_S4DM,
            np.dtype(np.int64): gxapi.GS_S8DM,
            np.dtype(np.str_): ''}
    try:
        return (_dummy_map[np.dtype(dtype)])
    except KeyError:
        s = str(dtype)
        if s[0] == 'U' or s[1] == 'U':
            return ''


def dummy_none(v):
    """ 
    Returns None if dummy, otherwise the value.

    .. versionadded:: 9.2
    """

    dummy = gx_dummy(np.dtype(type(v)))
    if v == dummy:
        return None
    else:
        return v


def dummyMask(npd):
    """
    .. deprecated:: 9.2 use dummy_mask()
    """
    return dummy_mask(npd)


def dummy_mask(npd):
    """
    Return a 1-D dummy mask that is True for all rows  in a 2D numpy array that
    have a Geosoft dummy value.

    :param npd: numpy data array
    :return:    numpy 1D array, True for any row that had a dummy in any data field

    .. versionadded:: 9.2
    """

    dummy = gx_dummy(npd.dtype)
    if npd.ndim == 1:
        return npd == dummy
    if len(npd.shape) != 2:
        raise UtilityException(_t('Must be a 2D array'))
    return np.apply_along_axis(lambda a: dummy in a, 1, npd)


def is_nan(v):
    """
    Returns True is v is a numpy.nan 
    
    .. versionadded:: 9.2
    """
    return not (v == v)


def dummy_to_nan(data):
    """
    Replaces dummies in float data to numpy.nan.  All other data types are returned unchanged.
    
    .. versionadded:: 9.2
    """

    if not isinstance(data, np.ndarray):
        data = np.array(data)
    if not ((data.dtype == np.float64) or (data.dtype == np.float32)):
        return data
    else:
        gxdummy = gx_dummy(data.dtype)
        data[data == gxdummy] = np.nan
        return data


def save_parameters(group='_', parms=None):
    """
    Save parameters to the Project Parameter Block.  Parameter group names and member names
    are converted to upper-case.

    :param group:   parameter block group name
    :param parms:   dict containing named parameter settings

    .. versionadded:: 9.1
    """
    if parms is not None:
        for k, v in parms.items():
            # remove escaped characters because set_str() puts them back in
            s = json.dumps(v).replace('\\\\', '\\')
            gxapi.GXSYS.set_string(group, k, s)


def reg_from_dict(rd, max_size=4096, json_encode=True):
    """
    :param rd:          dictionary
    :param max_size:    maximum "key=value" string size
    :param json:        True to encode non-string values as sas json strings (prefix '_JSON:')
                        False will encode non-string values as ``str(value)``
    :return:            gxapi.GXREG instance

    Non-string values in the dictionary are converted to JSON strings and stored as
    "_JSON:json-string}"
    """
    reg = gxapi.GXREG.create(max_size)
    for key, value in rd.items():
        if type(value) is not str:
            if json_encode:
                value = "_JSON:{}".format(json.dumps(value))
            else:
                value = str(value)
        if len(key) + len(value) >= max_size:
            raise UtilityException(_t("\'key=value\' longer than maximum ({}):\n{}={}")
                                   .format(max_size, key, value))
        reg.set(key, value)
    return reg


def dict_from_reg(reg, ordered=False):
    """
    :param reg:     gxapi.GXREG instance
    :param ordered: True to return and OrderedDict
    :return:        python dictionary from a Geosoft GXREG

    .. versionadded:: 9.1

    """
    key = gxapi.str_ref()
    val = gxapi.str_ref()
    if ordered:
        dct = OrderedDict()
    else:
        dct = {}
    for i in range(reg.entries()):
        reg.get_one(i, key, val)
        if val.value[:6] == "_JSON:":
            dct[key.value] = json.loads(val.value[6:])
        else:
            dct[key.value] = val.value
    return dct


def get_parameters(group='_', parms=None, default=None):
    """
    Get parameters from the Project Parameter Block.  Note that parameter names
    will always be upper-case.

    :param group:   name in the parameter block group name
    :param parms:   if specified only these items are found and returned, otherwise all are found and returned
    :param parms:   default parameter setting returned for parameters not found, otherwise dict will
                    not have the parameter.
    :return:        dictionary containing group parameters

    .. versionadded:: 9.1
    """

    sv = gxapi.str_ref()
    p = {}

    if parms is not None:
        for k in parms:
            if gxapi.GXSYS.exist_string(group, k):
                gxapi.GXSYS.gt_string(group, k, sv)
                try:
                    p[k.upper()] = json.loads(sv.value)
                except ValueError:
                    p[k.upper()] = sv.value

            elif default is not None:
                p[k.upper()] = default

    else:
        hREG = gxapi.GXREG.create(4096)
        gxapi.GXSYS.get_reg(hREG, group)
        k = gxapi.str_ref()
        for i in range(hREG.entries()):
            hREG.get_one(i, k, sv)
            key = k.value.split('.')[1]
            try:
                p[key] = json.loads(sv.value)
            except ValueError:
                p[key] = sv.value

    return p


def folder_workspace():
    """
    Return the Geosoft project folder name.

    .. versionadded:: 9.1
    """
    path = gxapi.str_ref()
    gxapi.GXSYS.get_path(gxapi.SYS_PATH_LOCAL, path)
    return path.value.replace('\\', os.sep)


def folder_user():
    """
    Return the Geosoft user configurations folder name.

    .. versionadded:: 9.1
    """
    path = gxapi.str_ref()
    gxapi.GXSYS.get_path(gxapi.SYS_PATH_GEOSOFT_USER, path)
    return path.value.replace('\\', os.sep)


def folder_temp():
    """
    Return the Geosoft temporary folder name.

    .. Note::
        If creating temporary files, better to use gx method :meth:`~gx.GXpy.temp_file`, which will
        create the temporary file in the GX-specific folder :mod:`~gx.GXpy.temp_folder`.

    .. versionadded:: 9.1
    """
    global _temp_folder_override
    if _temp_folder_override:
        return _temp_folder_override

    path = gxapi.str_ref()
    gxapi.GXSYS.get_path(gxapi.SYS_PATH_GEOTEMP, path)
    path = path.value.replace('\\', os.sep)
    return os.path.normpath(path)


def normalize_file_name(fn):
    """
    Normalize a file name string by replacing '\' with '/'.  This is useful for writing
    file names to control files.

    :param fn: file name
    :return: normalized file name

    .. versionadded:: 9.2
    """
    return fn.replace('\\', '/')


def uuid():
    """
    :return: a uuid as a string

    .. versionadded:: 9.2
    """
    global _uuid_callable
    if _uuid_callable:
        return _uuid_callable()
    else:
        return str(str(uid.uuid1()))

def _temp_dict_file_name():
    """Name of the expected python dictionary as a json file from run_external_python().

    .. versionadded:: 9.1
    """
    return '__shared_dictionary__'


def set_shared_dict(dict=None):
    """
    Save a dictionary to be shared by an separate application.
    This is a companion file to run_external_python().

    :param dict:  dictionary of parameters to save

    .. versionadded:: 9.1
    """

    # if no dictionary, pop the existing one if it is there
    if dict is None:
        get_shared_dict()
    else:
        with open(_temp_dict_file_name(), 'w') as f:
            json.dump(dict, f)


def get_shared_dict():
    """
    Get a dictionary shared by an external application.
    The shared dictionary is cleared (popped) so a subsequent call will return an empty dictionary.

    .. versionadded:: 9.1
    """

    try:
        with open(_temp_dict_file_name(), 'r') as f:
            dict = json.load(f)
        os.remove(_temp_dict_file_name())
        return dict

    except (IOError, OSError):
        return {}


def run_external_python(script, script_args='',
                        python_args='',
                        dict=None,
                        console=True,
                        catcherr=True):
    """
    Run a python script as an external program, returning results as a dictionary.
    External program calls gxpy.utility.get_shared_dict() to get the caller's dictionary,
    and gxpy.utility.set_shared_dict(return_dictionary) to return a dictionary back to caller.

    :param script:      full path of the python script
    :param dict:        dictionary passed to the external script (get_shared_dict() to retrieve)
    :param script_args: command line arguments as a string
    :param python_args: command line arguments as a string
    :param console:     True (default) will create a separate console for the process.
    :param catcherr:    True (default) Catch and re-raise errors from the sub-process.
    :return:            dictionary passed back from caller via set_shared_dict(dict)

    .. versionadded:: 9.1
    """

    if not os.path.isfile(script):
        raise UtilityException('Cannot find script: {}'.format(script))

    s = gxapi.str_ref()
    gxapi.GXSYS.get_env('PYTHON_HOME', s)
    py = os.path.join(s.value, 'python.exe')

    command = "\"{}\" {} \"{}\" {}".format(py, python_args, script, script_args)

    set_shared_dict(dict)

    kwargs = {}
    if console:
        kwargs['creationflags'] = subprocess.CREATE_NEW_CONSOLE

    if hasattr(subprocess, 'run'):
        if catcherr:
            kwargs['stderr'] = subprocess.PIPE
        cp = subprocess.run(command, **kwargs)
        if catcherr and cp.returncode != 0:
            raise UtilityException(_t('\n\nExternal python error:\n\n{}').format(cp.stderr.decode("utf-8")))

    else:  # use call, python 3.4...
        err = subprocess.call(command, **kwargs)
        if catcherr and err != 0:
            raise UtilityException(_t('\n\nExternal python error({}) running: {}').format(err, command))

    return get_shared_dict()


def crc32(bytes, crc=0):
    """
    Return 32-bit CRC of a byte buffer.

    :param bytes:   byte buffer (fulfills the Buffer Protocol)
    :param crc:     seed crc, can be passed along to accumulate the crc

    .. versionadded:: 9.2
    """
    crc = binascii.crc32(bytes, crc)
    return crc


def crc32_file(filename, crc=0):
    """
    Return 32-bit CRC of a file.

    :param filename:    file name
    :param crc:         seed crc, default 0

    .. versionadded:: 9.2
    """

    def readbuff(f, bsize=16384):
        while True:
            buff = f.read(bsize)
            if not buff:
                break
            yield buff

    with open(filename, 'rb') as f:
        for b in readbuff(f):
            crc = crc32(b, crc)

    return crc


def crc32_str(s, crc=0):
    """
    Return 32-bit CRC of a string.

    :param s:    string
    :param crc:  seed crc, default 0

    .. versionadded:: 9.2
    """
    crc = crc32(s.encode(), crc)
    return crc


def year_from_datetime(dt):
    """
    Return a decimal Gregorian calendar year from a Python datetime.
    :param dt: datetime
    :return: decimal Gregorian year to an accuracy of 1 millisecond

    .. versionadded:: 9.2
    """

    naive_dt = dt.replace(tzinfo=None)
    y_start = datetime.datetime(naive_dt.year, 1, 1)
    y_end = y_start.replace(year=naive_dt.year + 1)
    return dt.year + (naive_dt - y_start) / (y_end - y_start)


def datetime_from_year(year):
    """
    Return the Python datetime from a decimal Gregorian year.
    :param year: decimal year on the Gregorian calendar.
    :return: datetime (resolved to 1 millisecond)

    .. versionadded:: 9.2
    """
    yr = int(year)
    remainder = year - yr
    y_start = datetime.datetime(yr, 1, 1)
    y_end = y_start.replace(yr + 1)
    milliseconds = round(remainder * (y_end - y_start).total_seconds() * 1000.0)
    return y_start + datetime.timedelta(seconds=milliseconds / 1000.0)


def str_significant(value, n, mode=0):
    """
    Return a formatted string to n significant figures.
    :param value:   value to format
    :param mode:    0 round, 1 ceiling, -1 floor
    :return:        string to n significant figures
    """

    if value == 0.0:
        return '0'

    value = decimal.Decimal(str(value))
    if value < 0.0:
        mult = decimal.Decimal(-1)
        value = value * -1
    else:
        mult = decimal.Decimal(1)

    vstr = '{:33.16f}'.format(value).strip(' 0')

    power = vstr.index('.')
    vstr = vstr[:power] + vstr[power + 1:]
    for i, c in enumerate(vstr):
        if c != '0':
            power -= i
            break
    vstr = vstr.strip('0')

    significant = len(vstr)
    if significant <= n:
        s = str(value * decimal.Decimal(mult))
        if s.endswith('.0'):
            return s[:-2]
        else:
            return s

    v = float(vstr[:n] + '.' + vstr[n:])
    if mode == 0:
        vstr = str(round(v))
    elif mode == 1:
        vstr = str(math.ceil(v))
    else:
        vstr = str(math.floor(v))

    return str(decimal.Decimal(vstr) * mult * (10 ** decimal.Decimal(power - n)))
