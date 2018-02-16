"""
Utility functions to support Geosoft Python scripts and modules.

.. note::

    Regression tests provide usage examples:
    `Tests <https://github.com/GeosoftInc/gxpy/blob/master/geosoft/gxpy/tests/test_utility.py>`_

"""

import math
import decimal
import os
import numpy as np
import uuid as uid
import json
import datetime
import time
import subprocess
import binascii
from time import gmtime, strftime
from ._jdcal.jdcal import is_leap, gcal2jd, jd2gcal
from distutils.version import StrictVersion
from collections import OrderedDict
import xmltodict
import urllib.request

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


# check valid group/parameter string
def _validate_parameter(s):
    if '.' in s:
        return False
    return True


class UtilityException(Exception):
    """
    Exceptions from :mod:`geosoft.gxpy.utility`.

    .. versionadded:: 9.1
    """
    pass


def check_version(v, raise_on_fail=True):
    """
    Check the minimum API version.

    :param v:               minimum version string required (ie "9.1" or "9.2.4")
    :param raise_on_fail:   if True, raises an error if the version check fails, returns False otherwise
    :returns:               True if version is OK, False otherwise(unless raise_on_fail is False)

    .. note::  
        A valid version consists of two or three dot-separated numeric components, with an optional development
        version tag on the end.  The development version tag consists of the letter 'b' (for beta) followed by
        a number.  If the numeric components of two version numbers are equal, then a development version will
        always be deemed earlier (lesser) than one without.

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

    try:
        if StrictVersion(__version__) >= StrictVersion(str(v)):
            return True
        else:
            if raise_on_fail:
                raise UtilityException(_t("GX Requires API {}, only {} installed.").format(v, __version__))
            return False
    except ValueError:
        raise UtilityException(_t('Invalid version string "{}", expecting something like "{}".'.format(v, __version__)))


def dict_from_lst(lst, ordered=False):
    """
    Return a dictionary from a Geosoft `geosoft.gxapi.GXLST` instance.
    
    :param lst:     `geosoft.gxapi.GXLST` instance
    :param ordered: True to return an OrderedDict
    :returns:       python dictionary from a Geosoft GXLST

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


def xml_from_dict(d, pretty=False):
    """
    Return a unicode XML string of a dictionary.
    
    :param d: dictionary
    :param pretty: True to indent with line-feeds for pretty-printing

    If the dictionary does not have a single node root, the root XML will be '__gx_xml__'.
    
    Based on: https://github.com/martinblech/xmltodict
    
    .. seealso:: :func:`dict_from_xml`
     
    .. versionadded:: 9.2
    """

    if not d:
        raise UtilityException(_t('Cannot create XML from an empty dictionary.'))
    if len(d) > 1:
        d = {'__gx_xml__': d}

    xml = xmltodict.unparse(d, pretty=pretty)
    return xml


def dict_from_xml(xml):
    """
    Return a dictionary of an xml string.
    
    :param xml: xml string              
    :returns:   dictionary of the XML content.
    
    If the XML root is '__gx_xml__', the root is stripped.
    
    Based on: https://github.com/martinblech/xmltodict
    
    Tag attributes will become keys with '@' as the first character, and the key value will be the attribute setting.
    
    For example, XML string:
    
    .. code::
    
        <?xml version="1.0" encoding="UTF-8"?>
        <gmd:MD_Metadata xsi:schemaLocation="http://www.isotc211.org/2005/gmd ../schemas/iso19139fra/gmd/gmd.xsd">
            <geosoft xmlns="http://www.geosoft.com/schema/geo">
                <dataset version="1" beta="abc">
                    <title>test_grid_1</title>
                    <file_format>Geosoft Grid</file_format>
                </dataset>
            </geosoft>
        </gmd:MD_Metadata>
        
    returns dictionary:
    
    .. code::
    
        {'gmd:MD_Metadata': {
            '@xsi:schemaLocation': "http://www.isotc211.org/2005/gmd ../schemas/iso19139fra/gmd/gmd.xsd",
            'geosoft': {
                '@xmlns': "http://www.geosoft.com/schema/geo",
                'dataset': {
                    '@beta': "abc",
                    '@version': "1",
                    'title': "test_grid_1",
                    'file_format': "Geosoft Grid"
                    }
                }
            }
        }
        
    .. seealso:: :func:`xml_from_dict` 
        
    .. versionadded:: 9.2
    """

    d = xmltodict.parse(xml)

    # strip the generic dictionary root
    if '__gx_xml__' in d:
        d = d['__gx_xml__']

    return d


def merge_dict(d, d2):
    """
    Update a dictionary by adding key-values from second dictionary.  Unlike Python's 
    update(), this adds new keys to nested dictionaries rather than replace everything
    in a nested dictionary.
    
    :param d:   dictionary to update
    :param d2:  new items to add or replace
    :return:    merged dictionary
    
    .. versionadded:: 9.2
    """

    def update(old, new):
        for k, v in new.items():
            if k not in old:
                old[k] = v
            else:
                if isinstance(v, dict):
                    update(old[k], v)
                else:
                    old[k] = v

    update(d, d2)
    return d


def geosoft_metadata(geosoft_file_name):
    """
    Get the metadata dictionary for a geosoft data file.
    
    :param geosoft_file_name:   geosoft supported file name
    :returns:                   dictionary of the metadata
    
    If the metadata for the file does not exist  {'metadata': {}} is returned.
    
    .. versionadded:: 9.2
    """
    metadata = None
    if geosoft_file_name:
        if not geosoft_file_name.lower().endswith('.xml'):
            geosoft_file_name = geosoft_file_name + '.xml'
        if os.path.isfile(geosoft_file_name):
            with open(geosoft_file_name) as f:
                metadata = dict_from_xml(f.read())
    if metadata:
        return metadata
    return {'metadata': {}}


def time_stamp():
    """current date-time as a string."""
    return strftime("%Y-%m-%d %H:%M:%S", gmtime())


def yearFromJulianDay2(jd1, jd2):
    """
    Julian year
    
    :param jd1: part 1 Julian date (https://pypi.python.org/pypi/jdcal)
    :param jd2: part 2 Julian date
    :returns: decimal Gregorian year (Western calendar year)

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
    :returns: float of decoded string

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
    :returns:   decoded number, gxapi.rDUMMY if unable to decode the string

    See rdecode_err(string) for more details.

    .. versionadded:: 9.1
    """

    try:
        return rdecode_err(s)
    except ValueError:
        return gxapi.rDUMMY


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
    :returns:   GX type for a numpy dtype

    .. versionadded:: 9.1
    """

    global _np2gx_type
    if not bool(_np2gx_type):
        _np2gx_type = {
            str(np.dtype(np.float)): gxapi.GS_DOUBLE,
            str(np.dtype(np.int)): gxapi.GS_LONG64,
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
        return _np2gx_type[str(dtype)]
    except KeyError:
        if dtype.type is np.str_:
            return -int(dtype.str[2:])


def dtype_gx(gtype):
    """
    :returns:   numpy dtype from a GX type

    .. versionadded:: 9.1
    """

    global _gx2np_type
    if not bool(_gx2np_type):
        _gx2np_type = {
            gxapi.GS_TYPE_DEFAULT: None,
            gxapi.GS_DOUBLE: np.dtype(np.float64),
            gxapi.GS_FLOAT: np.dtype(np.float32),
            gxapi.GS_LONG64: np.dtype(np.int64),
            gxapi.GS_LONG: np.dtype(np.int32),
            gxapi.GS_BYTE: np.dtype(np.byte),
            gxapi.GS_SHORT: np.dtype(np.int16),
            gxapi.GS_UBYTE: np.dtype(np.uint8),
            gxapi.GS_USHORT: np.dtype(np.uint16),
            gxapi.GS_ULONG: np.dtype(np.uint32),
            gxapi.GS_ULONG64: np.dtype(np.uint64),
            gxapi.GS_FLOAT2D: np.dtype(np.float32),
            gxapi.GS_DOUBLE2D: np.dtype(np.float64),
            gxapi.GS_FLOAT3D: np.dtype(np.float32),
            gxapi.GS_DOUBLE3D: np.dtype(np.float64)}
    try:
        return _gx2np_type[gtype]
    except KeyError:
        if gtype < 0:
            return np.dtype('U{}'.format(-gtype))


def dtype_gx_dimension(gtype):
    """
    :returns:   numpy dtype and dimension of the type, 1, 2 or 3. The dimension indicates 1D, 2D or 3D data.

    .. versionadded:: 9.3.1
    """
    if (gtype == gxapi.GS_FLOAT2D) or (gtype == gxapi.GS_DOUBLE2D):
        return dtype_gx(gtype), 2
    elif (gtype == gxapi.GS_FLOAT3D) or (gtype == gxapi.GS_DOUBLE3D):
        return dtype_gx(gtype), 3
    return dtype_gx(gtype), 1


def gx_dtype_dimension(dtype, dimension=1):
    """
    :returns:   GX type for a numpy dtype, with dimensions 2 and 3

    .. versionadded:: 9.3.1
    """

    gtype = gx_dtype(dtype)
    if dimension == 1:
        return gtype
    if not((gtype == gxapi.GS_DOUBLE) or (gtype == gxapi.GS_FLOAT)):
        raise UtilityException(_t('Dimensioned data must be float32 or float64'))
    if dimension == 2:
        if gtype == gxapi.GS_DOUBLE:
            return gxapi.GS_DOUBLE2D
        return gxapi.GS_FLOAT2D
    if dimension != 3:
        raise UtilityException(_t('Dimension must be 1, 2 or 3'))
    if gtype == gxapi.GS_DOUBLE:
        return gxapi.GS_DOUBLE3D
    return gxapi.GS_FLOAT3D


def is_float(gxtype):
    """ Return True of gxtype can be stored in a 64-bit float"""
    if gxtype >= 0 and gxtype in {gxapi.GS_DOUBLE, gxapi.GS_FLOAT,
                                  gxapi.GS_DOUBLE2D, gxapi.GS_FLOAT2D,
                                  gxapi.GS_DOUBLE3D, gxapi.GS_FLOAT3D}:
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
    Return the dummy for this value, or this type.

    :returns:   GX dummy for this data
    :raises:    KeyError if the dtype is not supported

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
        dtype = np.dtype(dtype)
    except TypeError:
        dtype = np.dtype(type(dtype))

    try:
        return _dummy_map[dtype]

    except KeyError:
        s = str(dtype)
        if s[0] == 'U' or s[1] == 'U':
            return ''
        raise


def dummy_none(v):
    """ 
    Returns None if dummy, otherwise the value.

    .. versionadded:: 9.2
    """

    if v == gx_dummy(v):
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
    :returns:   numpy 1D array, True for any row that had a dummy in any data field

    .. versionadded:: 9.2
    """

    dummy = gx_dummy(npd.dtype)
    if npd.ndim == 1:
        return npd == dummy
    if len(npd.shape) != 2:
        raise UtilityException(_t('Must be a 2D array'))
    return np.apply_along_axis(lambda a: dummy in a, 1, npd)


def dummy_to_nan(data):
    """
    Replaces dummies in float data to numpy.nan.  All other data types are returned unchanged.

    If passed data is a numpy array, dummies are changed in-place.
    The numpy array is returned.
    
    :param data:    float value or a numpy array
    :returns:       data with dummies replaced by numpy.nan
    
    .. versionadded:: 9.2
    """

    if isinstance(data, np.ndarray):
        if not ((data.dtype == np.float64) or (data.dtype == np.float32)):
            return data
        else:
            gxdummy = gx_dummy(data.dtype)
            data[data == gxdummy] = np.nan
            return data
    else:
        if data == gxapi.rDUMMY:
            return np.nan
        else:
            return data


def reg_from_dict(rd, max_size=4096, json_encode=True):
    """
    `geosoft.gxapi.GXREG` instance from a dictionary
    
    :param rd:          dictionary
    :param max_size:    maximum "key=value" string size
    :param json_encode: if True, non-string values in the dictionary are converted to JSON strings and stored as
                        "_JSON:json-string". False will encode non-string values as ``str(value)``
    :returns:           `geosoft.gxapi.GXREG` instance

    .. versionadded:: 9.1
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
    dictionary from a `geosoft.gxapi.GXREG` instance
    
    :param reg:     `geosoft.gxapi.GXREG` instance
    :param ordered: True to return and OrderedDict
    :returns:       python dictionary from a Geosoft GXREG

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


def save_parameters(group='_', parms=None):
    """
    Save parameters to the Project Parameter Block.  Parameter group names and member names
    are converted to uppercase.

    :param group:   parameter block group name, default is '_'
    :param parms:   dict containing named parameter settings, must be specified

    .. versionadded:: 9.1
    """

    if not isinstance(parms, dict):
        raise UtilityException(_t('parms dictionary not defined.'))

    if not(_validate_parameter(group)):
        raise UtilityException(_t('Group name \'{}\' contains invalid character \'.\''.format(group)))

    for k, v in parms.items():
        if not (_validate_parameter(k)):
            raise UtilityException(_t('Parameter name \'{}\' contains invalid character \'.\''.format(k)))

        # remove escaped characters because set_str() puts them back in
        s = json.dumps(v).replace('\\\\', '\\')
        gxapi.GXSYS.set_string(group.upper(), k, s)


def get_parameters(group='_', parms=None, default=None):
    """
    Get parameters from the Project Parameter Block.

    :param group:   name in the parameter block group name
    :param parms:   if specified only these keys are searched and the value is replaced by the found parameter.
                    Parameter keys are not case sensitive, though if parms is not provided all returned keys will
                    be upper-case.
    :param default: default value for parameters not found, ignored if parms is provided as a dict, in which
                    case the current key:value settings will be unchanged.
    :returns:       dictionary containing group parameters

    .. versionchanged:: 9.2.1
        Now retains case on keys passed in to parms, which allows callers to maintain case.  Note that
        if not specifying parms, the returned keys will always be upper-case.
        Fixed bug handling file name construction on Windows.

    .. versionadded:: 9.1
    """

    sv = gxapi.str_ref()
    p = {}

    if not(_validate_parameter(group)):
        raise UtilityException(_t('Group name \'{}\' contains invalid character \'.\''.format(group)))
    group = group.upper()

    if parms is not None:
        if not isinstance(parms, dict):
            for k in parms:
                p[k] = default
            parms = p
        for k, default in parms.items():
            k_upper = k.upper()
            if gxapi.GXSYS.exist_string(group, k_upper):
                gxapi.GXSYS.gt_string(group, k_upper, sv)
                try:
                    p[k] = json.loads(sv.value.replace('\\', '\\\\'))
                except ValueError:
                    p[k] = sv.value
            else:
                p[k] = default

    else:
        h_reg = gxapi.GXREG.create(4096)
        gxapi.GXSYS.get_reg(h_reg, group)
        k = gxapi.str_ref()
        for i in range(h_reg.entries()):
            h_reg.get_one(i, k, sv)
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


def folder_temp(use_override=True):
    """
    Return the Geosoft temporary folder name.

    :param use_override: True to use the _temp_folder_overide if it is defined (used by tests)

    .. Note::
        If creating temporary files, better to use gx method :meth:`~gx.GXpy.temp_file`, which will
        create the temporary file in the GX-specific folder :mod:`~gx.GXpy.temp_folder`.

    .. versionadded:: 9.1
    """
    global _temp_folder_override
    if use_override and _temp_folder_override:
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
    :returns: normalized file name

    .. versionadded:: 9.2
    """
    return fn.replace('\\', '/')


def uuid():
    """
    :returns: a uuid as a string

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


def set_shared_dict(shared_dict=None):
    """
    Save a dictionary to be shared by an separate application.
    This is a companion file to run_external_python().

    :param shared_dict:  dictionary of parameters to save

    .. versionadded:: 9.1
    """

    # if no dictionary, pop the existing one if it is there
    if shared_dict is None:
        get_shared_dict()
    else:
        with open(_temp_dict_file_name(), 'w') as f:
            json.dump(shared_dict, f)


def get_shared_dict():
    """
    Get a dictionary shared by an external application.
    The shared dictionary is cleared (popped) so a subsequent call will return an empty dictionary.

    .. versionadded:: 9.1
    """

    try:
        with open(_temp_dict_file_name(), 'r') as f:
            shared_dict = json.load(f)
        os.remove(_temp_dict_file_name())
        return shared_dict

    except (IOError, OSError):
        return {}


def run_external_python(script, script_args='',
                        python_args='',
                        shared_dict=None,
                        console=True,
                        catcherr=True):
    """
    Run a python script as an external program, returning results as a dictionary.
    External program calls gxpy.utility.get_shared_dict() to get the caller's dictionary,
    and gxpy.utility.set_shared_dict(return_dictionary) to return a dictionary back to caller.

    :param script:      full path of the python script
    :param shared_dict: dictionary passed to the external script (get_shared_dict() to retrieve)
    :param script_args: command line arguments as a string
    :param python_args: command line arguments as a string
    :param console:     True (default) will create a separate console for the process.
    :param catcherr:    True (default) Catch and re-raise errors from the sub-process.
    :returns:           dictionary passed back from caller via set_shared_dict(dict)

    .. versionadded:: 9.1
    """

    if not os.path.isfile(script):
        raise UtilityException(_t('Cannot find script: {}'.format(script)))

    s = gxapi.str_ref()
    gxapi.GXSYS.get_env('PYTHON_HOME', s)
    py = os.path.join(s.value, 'python.exe')

    command = "\"{}\" {} \"{}\" {}".format(py, python_args, script, script_args)

    set_shared_dict(shared_dict)

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


def crc32(byte_buffer, crc=0):
    """
    Return 32-bit CRC of a byte buffer.

    :param byte_buffer: byte buffer (fulfills the Buffer Protocol)
    :param crc:         seed crc, can be passed along to accumulate the crc

    .. versionadded:: 9.2
    """
    crc = binascii.crc32(byte_buffer, crc)
    return crc


def crc32_file(filename, crc=0):
    """
    Return 32-bit CRC of a file.

    :param filename:    file name
    :param crc:         seed crc, default 0

    .. versionadded:: 9.2
    """

    def readbuff(ff, bsize=16384):
        while True:
            buff = ff.read(bsize)
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
    
    :param dt:  datetime
    :returns:   decimal Gregorian year to an accuracy of 1 millisecond

    .. versionadded:: 9.2
    """

    naive_dt = dt.replace(tzinfo=None)
    y_start = datetime.datetime(naive_dt.year, 1, 1)
    y_end = y_start.replace(year=naive_dt.year + 1)
    return dt.year + (naive_dt - y_start) / (y_end - y_start)


def datetime_from_year(year):
    """
    Return the Python datetime from a decimal Gregorian year.
    
    :param year:    decimal year on the Gregorian calendar.
    :returns:       datetime (resolved to 1 millisecond)

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
    :param n:       number of significant digits
    :param mode:    0 round, 1 ceiling, -1 floor
    :returns:       string to n significant figures
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


def url_retrieve(url, filename=None, overwrite=False, reporthook=None):
    """
    Retrieve a URL resource as a file.

    :param url:         name of the URL resource
    :param filename:    name of file in which to place the resource, default is the resource base name.
    :param overwrite:   True to overwrite an existing file.  Default is False, in which case if the file
                        exists the filename is returned.
    :param reporthook:  a hook function that will be called once on establishment of the network connection
                        and once after each block read thereafter. The hook will be passed three arguments;
                        a count of blocks transferred so far, a block size in bytes, and the total size of the file.
    :return:            filename of the file that is created.

    .. seealso:: https://docs.python.org/3.6/library/urllib.request.html#urllib.request.urlretrieve

    .. versionadded:: 9.3
    """

    if filename is None:
        filename = os.path.basename(url).replace('%20', ' ')

    if not overwrite:
        if os.path.isfile(filename):
            return filename

    file, message = urllib.request.urlretrieve(url.replace(' ', '%20'), filename=filename, reporthook=reporthook)
    return file


def delete_file(file_name):
    """
    Delete a file, does nothing if file does not exist.

    :param file_name:   file to delete

    .. versionadded:: 9.3.1
    """
    try:
        os.remove(file_name)
    except FileNotFoundError:
        pass


def unique_name(name, invalid=None, separator='()', maxversion=1000):
    """
    Build a unique name or file name.
    
    :param name:        seed name, returns this if callback(name) is False the name in unique
    :param invalid:     callback function invalid(name), returns True if name is invalid. If a call-back
                        is not provided a simple os.path.isfile(name) is used.
    :param separator:   single or two-character separator. The unique name is constructed by appending
                        an increasing number to the seed name until a valid name is found. By default
                        the number is enclosed in parentheses (e.g. some_name(4).txt). If a single separator
                        character is defined the number is separted from the name by the single character
                        (e.g. for separator='_', might return some_name_4.txt).
    :param maxversion:  maximum number to try, default is 1000. This protects against infinite loop
                        should there be a bug in your callback.
    :return:            unique name

    .. versionadded:: 9.3.1
    """

    def parts():
        path, file = os.path.split(name)
        base, ex = os.path.splitext(file)
        isep = base.rfind(separator[0])
        if isep == -1:
            n = 0
        else:
            current_base = base
            if len(separator) > 1:
                if base[-1] == separator[1]:
                    base = base[:-1]
            try:
                n = int(base[isep + 1:])
                base = base[:isep]
            except ValueError:
                n = 0
                base = current_base
        return path + base, n, ex

    if invalid is None:
        invalid = os.path.isfile

    while invalid(name):
        path_name, number, ext = parts()
        number += 1
        if number >= maxversion:
            raise UtilityException(_t("Cannot determine a unique name in {} tries.").format(maxversion))
        name = path_name + separator[0] + str(number)
        if len(separator) > 1:
            name = name + separator[1]
        name = name + ext

    return name


def is_file_locked(file_name, age=None):
    """
    Returns True if the file exists and is currently locked by another process or is younger than age.

    :param file_name:   file to test
    :param age:         minimum age in seconds, default ignores age

    .. versionadded:: 9.3.1
    """
    if os.path.exists(file_name):
        if age and file_age(file_name) < age:
            return True
        try:
            f = open(file_name, 'a')
            f.close()
            return False
        except IOError:
            return True
    return False


def file_age(file_name):
    """
    Returns the age of a file in seconds from now. -1 if the file does not exist.

    :param file_name: file name

    .. versionadded:: 9.3.1
    """
    if not os.path.exists(file_name):
        return -1
    return time.time() - os.path.getmtime(file_name)


def is_path_locked(path, age=None):
    """
    Returns True if any files in this folder or sub-folders are locked or younger than age.

    :param path:    name of the folder
    :param age:     age in seconds from now

    .. versionadded:: 9.3.1
    """

    if os.path.exists(path):
        if not os.path.isdir(path):
            return is_file_locked(path, age=age)
        for item in os.listdir(path):
            item = os.path.join(path, item)
            if os.path.isdir(item):
                if is_path_locked(item):
                    return True
            else:
                if is_file_locked(item):
                    return True
                if age and file_age(item) < age:
                    return True
    return False


def delete_folder(folder_name, age=None, raise_on_error=False):
    """
    Delete a folder if all files and sub-folders are accessible and deletable.

    :param folder_name:     name of the folder
    :param age:             age in seconds relative to the current date/time
    :param raise_on_error:  True to raise an error if unsuccessful, otherwise just returns False
    :return:                True if successful

    .. versionadded:: 9.3.1
    """

    if is_path_locked(folder_name, age=age):
        if raise_on_error:
            raise UtilityException(_t("Folder `{}` is locked.").format(folder_name))
        return False

    try:
        for item in os.listdir(folder_name):
            if os.path.isdir(item):
                delete_folder(item, age=age)

        for item in os.listdir(folder_name):
            if age and file_age(item) > age:
                os.remove(item)

        os.removedirs(folder_name)

    except IOError:
        if raise_on_error:
            raise

    return True


def jupyter_markdown_toc(j_file, numbered=True, start_level=1, max_depth=1, prefix=' '):
    """
    Create a markdoown table-of-content string from a jupyter notebook based on markdown "#".

    :param j_file:      jupyter notebook name. Default file extension is '.ipynb'
    :param numbered:    True (default) to number the main headings, False for all bulletys
    :param start_level: toc base level, default is 1, which starts TOC at "##"
    :param max_depth:   maximum levels relative to the start level, default is first level only.
    :param prefix:      previx for each TOC line, default is ' ' so TOC will appear indented.
    :return:        toc string.

    Include this in a jupyter notebook to create a TOC that can then be cut/pasted into the
    introductory markdown:

    .. code::

        import geosoft.gxpy.utility as gxu
        print (gxu.jupyter_markdown_toc('my_notebook_name'))

    .. versionadded:: 9.3.1
    """
    base, ext = os.path.splitext(j_file)
    if not ext:
        j_file = j_file + '.ipynb'
    data = json.loads(open(j_file).read())
    toc = ''
    i = 1
    for k in data['cells']:
        if k['cell_type'] == 'markdown':
            for sl in k['source']:
                sl = sl.strip()
                if sl and sl[0] == '#':
                    sl = sl[start_level:]
                    if sl[0] == '#':
                        indent, label = sl.split(' ', 1)
                        if len(indent) <= max_depth:
                            if label[-1] == '\n':
                                label = label[:-1]
                            if numbered and len(indent) == 1:
                                lead = str(i) + '. ['
                                i += 1
                            else:
                                lead = str(' ' * len(indent)) + '- ['
                            toc = toc + prefix + lead + label + '](#' + label.replace(' ', '-') + ')\n'
    return toc


def vector_normalize(v):
    """
    Normalise (Euclidean) the last axis of a numpy array

    :param v: numpy vector array, any dimension
    :return:  array normalized, 0 vectors will be np.nan

    .. versionadded:: 9.3.1
    """
    if v.ndim < 2:
        return np.array((1.,))
    vs = v.shape
    v = v.reshape((-1, v.shape[-1]))
    mag = np.linalg.norm(v, axis=1)
    mag[mag == 0.] = np.nan
    return (v.T * np.reciprocal(mag)).T.reshape(vs)
