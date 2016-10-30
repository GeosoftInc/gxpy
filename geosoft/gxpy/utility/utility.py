'''

   Utility functions to support Geosoft Python scripts and modules.

'''

import sys, os
import json
from time import gmtime, strftime
from jdcal import is_leap, gcal2jd, jd2gcal
import numpy as np
import geosoft
import geosoft.gxapi as gxapi

__version__ = geosoft.__version__

class UtilityException(Exception):
    pass

# translation hook
def _(string):
    return string

###############
# static

def dictFromLst(lst):
    '''
    :return:    python dictionary from a Geosoft GXLST
    '''
    key = gxapi.str_ref()
    val = gxapi.str_ref()
    dct = {}
    for item in range(lst.size()):
        lst.gt_item(0,item,key)
        lst.gt_item(1,item,val)
        dct[key.value] = val.value
    del key
    del val
    return dct

def timeStamp():
    return strftime("%Y-%m-%d %H:%M:%S", gmtime())

def yearFromJulianDay2(jd1,jd2):
    '''
    :param jd1: part 1 Julian date (https://pypi.python.org/pypi/jdcal)
    :param jd2: part 2 Julian date
    :return: decimal Gregorian year (Western calendar year)
    '''
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
    """

    #nothing there, or a dummy
    if (not s) or (s[0] == '*'):
        return gxapi.rDUMMY

    #try floating point
    try:
        return(float(s))

    except ValueError:

        #date
        if (len(s) >= 8) and (s[4:5] in '/-'):
            s = s[0:10]
            try:
                smonth = s[5:7]
                if smonth[-1] in '/-':
                    smonth = smonth[0]
                    sday = s[7:]
                else:
                    sday = s[8:10]
                j1,j2 = gcal2jd(s[:4],smonth,sday)
                return yearFromJulianDay2(j1,j2)
            except:
                raise ValueError

        #tabs are spaces, trim leading white space
        ss = s.replace("\t"," ")
        ss = ss.lstrip()
        ss = ss.rstrip()

        #replace mistyped "o", "O"
        ss = ss.replace("o","0")
        ss = ss.replace("O","0")

        #nothing there, or a dummy
        if (not ss) or (ss[0] == '*'):
            return gxapi.rDUMMY

        try:

            return(float(ss))

        except ValueError:

            #look for time or geographic format - two spaces become dots
            sg = ss.replace(' ','.',2)
            sg = sg.replace(':','.',2)
            if (' ' in sg): #ok, this string is messed up
                raise ValueError
            sg = sg.upper();
            twelve = 0.0
            negsuf = negpre = 1.0
            suf = sg[len(sg)-1]
            if ((suf == 'S') or (suf == 'W')):
                negsuf = -1.0
            if sg[0] == '-':
                negpre = -1.0
                sg = sg[1:]
            else:
                if ('PM' in sg):
                    twelve = 12.0
            sg = sg.rstrip("NSEWAMP")
            dms = sg.split('.',2)
            degrees = float(dms[0])
            if (len(dms)>1):
                minutes = float(dms[1])
            else:
                minutes=0.0
            if (len(dms)>2):
                seconds = float(dms[2])
            else:
                seconds=0.0
            return (degrees + (minutes + seconds/60.0)/60.0) * negpre * negsuf + twelve

def rdecode(s):
    """
    Geosoft string (number, date, time, geographic) conversion to a number, always works.

    :param s:   string to decode
    :return:    decoded number, gxapi.rDUMMY if unable to decode the string

    See rdecode_err(string) for more details.
    """

    try:
        return(rdecode_err(s))
    except ValueError:
        return(gxapi.rDUMMY)


def decode(s,f):
    '''
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

    '''

    #always use Unicode for strings
    if f[0] in "Sa":
        f = 'U'+f[1:]

    #handle strings
    if f[:1] == 'U':
        if len(f) < 2:
            raise TypeError
        type(f) #to insure valid type
        return s[0:int(f[1:])]

    #not currently supporting complex
    if f[0] == 'c':
        raise TypeError

    type(f) #raises error if unknown type

    r = rdecode_err(s)
    if f[0] == 'f':
        return r

    #boolean
    if f[0] == 'b':
        if r == gxapi.rDUMMY:
            return False
        else:
            return not (int(round(r)) == 0)

    #everything else is returned as an int
    if r == gxapi.rDUMMY:
        return gxapi.GS_S4DM
    return int(round(r))

def gxType(dtype):
    '''
    :return:    GX type for a numpy dtype
    '''
    if dtype is None:
        return gxapi.GS_TYPE_DEFAULT
    dtype = np.dtype(dtype)
    if dtype == np.float:   return gxapi.GS_DOUBLE
    if dtype == np.int:     return gxapi.GS_LONG
    if dtype.type is np.str_:
       return -(int(dtype.str[2:]))
    if dtype == np.byte:    return gxapi.GS_BYTE
    if dtype == np.float64: return gxapi.GS_DOUBLE
    if dtype == np.float32: return gxapi.GS_FLOAT
    if dtype == np.int64:   return gxapi.GS_LONG64
    if dtype == np.int32:   return gxapi.GS_LONG
    if dtype == np.int16:   return gxapi.GS_SHORT
    if dtype == np.int8:    return gxapi.GS_BYTE
    if dtype == np.uint8:   return gxapi.GS_UBYTE
    if dtype == np.uint16:  return gxapi.GS_USHORT
    if dtype == np.uint32:  return gxapi.GS_ULONG
    if dtype == np.uint64:  return gxapi.GS_ULONG64

    raise UtilityException(_("Unsupported numpy type {}").format(dtype))

def dtypeGX(gtype):
    '''
    :return:    numpy dtype from a GX type
    '''
    if gtype == gxapi.GS_TYPE_DEFAULT: return None
    if gtype == gxapi.GS_DOUBLE:   return np.dtype(np.float)
    if gtype == gxapi.GS_FLOAT:    return np.dtype(np.float32)
    if gtype == gxapi.GS_LONG64:   return np.dtype(np.int64)
    if gtype == gxapi.GS_LONG:     return np.dtype(np.int32)
    if gtype < 0:
        return np.dtype('<U{}'.format(-gtype))
    if gtype == gxapi.GS_BYTE:     return np.dtype(np.byte)
    if gtype == gxapi.GS_SHORT:    return np.dtype(np.int16)
    if gtype == gxapi.GS_UBYTE:    return np.dtype(np.uint8)
    if gtype == gxapi.GS_USHORT:   return np.dtype(np.uint16)
    if gtype == gxapi.GS_ULONG:    return np.dtype(np.uint32)
    if gtype == gxapi.GS_ULONG64:  return np.dtype(np.uint64)
    raise UtilityException(_("Unsupported GX type {}").format(gtype))

def gxDummy(dtype):
    '''
    :return:    GX dummy for this dtype
    '''
    dtype = np.dtype(dtype)
    if dtype == np.float: return gxapi.rDUMMY
    if dtype == np.float64: return gxapi.rDUMMY
    if dtype == np.float32: return gxapi.rDUMMY
    if dtype == np.int: return gxapi.iDUMMY
    if dtype == np.int64: return gxapi.iDUMMY
    if dtype == np.int8: return gxapi.GS_S1DM
    if dtype == np.int16: return gxapi.GS_S2DM
    if dtype == np.int32: return gxapi.GS_S4DM
    if dtype == np.int64: return gxapi.GS_S8DM
    if dtype.type is np.str_: return '*'
    raise UtilityException(_("Unsupported dummy for numpy type {}").format(dtype))

def dummyMask(npd):
    '''
    Return a 1-D dummy mask that is True for all rows  in a 2D numpy array that
    have a Geosoft dummy value.

    :param npd: numpy data array
    :return:    numpy 1D array, True for any row that had a dummy in any data field

    '''

    if len(npd.shape) != 2:
        raise UtilityException(_('Must be a 2D array'))
    dummy = gxDummy(npd.dtype)
    return np.apply_along_axis(lambda a: dummy in a, 1, npd)

def save_parameters(group='_', parms={}):
    '''
    Save parameters to the Project Parameter Block.

    :param group:   parameter block group name
    :param parms:   dict containing named parameter settings
    '''

    for k,v in parms.items():
        gxapi.GXSYS.set_string(group, k, str(v))

def get_parameters(group='_', parms=None):
    '''
    Get parameters from the Project Parameter Block.

    :param group:   name in the parameter block group name
    :param parms:   if specified only these items are found and returned, otherwise all are found and returned
    :return:        dictionary containing group parameters
    '''

    sv = gxapi.str_ref()
    p = {}

    if parms is not None:
        for k in parms:
            if gxapi.GXSYS.exist_string(group, k):
                gxapi.GXSYS.gt_string(group, k, sv)
                p[k] = sv.value

    else:
        hREG = gxapi.GXREG.create(4096)
        gxapi.GXSYS.get_reg(hREG, group)
        k = gxapi.str_ref()
        for i in range(hREG.entries()):
            hREG.get_one(i, k, sv)
            p[k.value.split('.')[1]] = sv.value

    return p


def project_path():
    ''' return the Geosoft project folder path'''
    path = gxapi.str_ref()
    gxapi.GXSYS.get_path(gxapi.SYS_PATH_LOCAL, path)
    return path.value.replace('\\', '/')

def user_path():
    ''' return the Geosoft user configurations folder path'''
    path = gxapi.str_ref()
    gxapi.GXSYS.get_path(gxapi.SYS_PATH_GEOSOFT_USER, path)
    return path.value.replace('\\', '/')

def temp_path():
    ''' return the Geosoft temporary folder path'''
    path = gxapi.str_ref()
    gxapi.GXSYS.get_path(gxapi.SYS_PATH_GEOTEMP, path)
    return path.value.replace('\\', '/')

def safeApiException(fn, args, EClass=Exception):
    '''
    This is a helper method that turns a gxapi.GXError and gxapi.GXAPIError exceptions into exception of class EClass so
    you can catch and deal with it. The GXError message is provided in the EClass, traceback of original
    exception is preserved.
    

    :param fn:      gxapi finction to call
    :param args:    arguments as a tuple
    :param EClass:  exception class returned, default is Exception
    :returns:       function return
    '''

    try:
        return fn(*args)
    except (gxapi.GXError, gxapi.GXAPIError):
        exc_class, exc, tb = sys.exc_info()
        raise EClass(str(exc)).with_traceback(tb)

def _results_file():
    ''' name of the expected python results json file from run_external_python()'''
    return os.path.join(temp_path(), '__external_python_results__')

def run_return(parameters):
    ''' 
    Parameters to be passed back to run_external_pyhton caller.
    
    :param parameters:  dictionary of parameters to pass back to caller.
    '''
    with open(_results_file(), 'w') as f:
        json.dump(parameters, f)

def run_external_python(script, script_args='', python_args='', hold=gxapi.SYS_RUN_HOLD_ONERROR):
    '''
    Run a python script as an external program, returning results as a dictionary.
    External program can call gxpy.utility.run_return(dict) to pass a dictionary back to caller.
    
    :param script:      path of the python script
    :param script_args: command line arguments as a string
    :param python_args: command line arguments as a string
    :param hold:        gxapi.SYS_RUN_HOLD_ option, default is gxapi.SYS_RUN_HOLD_ONERROR
    :return:            dictionary registered gxpy.utility.run_return(dict)
    '''

    s = gxapi.str_ref()
    gxapi.GXSYS.get_env('PYTHON_HOME', s)
    py = os.path.join(s.value, 'python.exe')

    command = "{} {} {}".format(python_args, script, script_args)

    try:
        if gxapi.GXSYS.run(py, command, gxapi.SYS_RUN_TYPE_EXE+hold) == -1:
            raise UtilityException(_('Failed running:\n{} {}').format(py, command))
    except:
        raise

    # look for default script result dictionary
    results = _results_file()
    if os.path.isfile(results):
        with open(results) as f:
            data = json.load(f)
        os.remove(results)
        return data
    return {}