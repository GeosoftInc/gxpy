### extends 'init_empty.py'

### block Header
# NOTICE: The code generator will not replace the code in this block

import geosoft

class ref_value:
    def __init__(self, value=None):
        self._value = None

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value

class bool_ref(ref_value):
    def __init__(self, value=False):
        self._value = value

class int_ref(ref_value):
    def __init__(self, value=0):
        self._value = value
    
class float_ref(ref_value):
    def __init__(self, value=0.0):
        self._value = value

class str_ref(ref_value):
    def __init__(self, value=""):
        self._value = value


class GXCancel(SystemExit):
    """
    A subclass of `SystemExit <https://docs.python.org/3/library/exceptions.html#SystemExit>`_ which is raised when a 
    script should cleanly exit due to a cancellation condition. Generally not caught since it will have the same effect 
    as :exc:`SystemExit` for both standalone and Oasis montaj extension scripts. Raised from within API by 
    :func:`geosoft.gxapi.GXSYS.cancel()`

    .. versionadded:: 9.1
    """
    pass

class GXExit(SystemExit):
    """
    A subclass of `SystemExit <https://docs.python.org/3/library/exceptions.html#SystemExit>`_ which is raised when a 
    script should cleanly exit due to a completion condition. Generally not caught since it will have the same effect as 
    :exc:`SystemExit` for both standalone and Oasis montaj extension scripts. Raised from within API by 
    :func:`geosoft.gxapi.GXSYS.exit()`

    .. versionadded:: 9.1
    """
    pass

class GXAPIError(RuntimeError):
    """
    A subclass of `RuntimeError <https://docs.python.org/3/library/exceptions.html#RuntimeError>`_ which is raised whenever 
    the GX Python API encounters initialization issues or other API violations. It generally indicates a bug in Python code.

    .. versionadded:: 9.1
    """
    pass


class GXError(geosoft.GXRuntimeError):
    """
    A subclass of `RuntimeError <https://docs.python.org/3/library/exceptions.html#RuntimeError>`_ which is raised whenever 
    a GX Python API call encounters an error. Often the message string of these errors are informative to the user (e.g. File 
    'x' is locked in another application) but there could be cases where this is not the case. In most cases an attribute, 
    :attr:`number`, is also available on the exception object that matches the number in the :code:`geosoft.ger` file.
    These numbers instead of the string (which could change or even be translated) should be used to identify and handle
    very specific exceptions.

    .. versionadded:: 9.1
    """
    
    def __init__(self, message, module, error_number):
        super(geosoft.GXRuntimeError, self).__init__(message)
        self.module = module
        self.error_number = error_number


### endblock Header

### block Constants
# NOTICE: Do not edit anything here, it is generated code

import struct

#
# GX3DN Constants
# 

	

#
# GX3DV Constants
# 



#
# GEO3DV_OPEN constants
#
# Open Modes

#: Geo3dv mview read
GEO3DV_MVIEW_READ = 0
#: Geo3dv mview writeold
GEO3DV_MVIEW_WRITEOLD = 2	

#
# GXAGG Constants
# 



#
# AGG_LAYER_ZONE constants
#
# Aggregate Layer Zone defines

#: If a color table with no color transform is passed
#: it will be used with the default zoning
#: method of the data, which is usually
#: `AGG_LAYER_ZONE_EQUALAREA <geosoft.gxapi.AGG_LAYER_ZONE_EQUALAREA>`.
AGG_LAYER_ZONE_DEFAULT = 0
#: Linear Distribution
AGG_LAYER_ZONE_LINEAR = 1
#: Normal Distribution
AGG_LAYER_ZONE_NORMAL = 2
#: Equal Area Distribution
AGG_LAYER_ZONE_EQUALAREA = 3
#: If `AGG_LAYER_ZONE_SHADE <geosoft.gxapi.AGG_LAYER_ZONE_SHADE>` is specified, a shaded relief
#: layer is created from the specified grid.  A new grid
#: file will also be created to hold the shaded relief
#: image data.  This file will have the same name as the
#: original grid but with "_s" added to the root name.
#: It will always be located in the workspace directory
#: regardless of the location of the original source image.
#: If the file already exists, it will used as it is.
#: Shading is always at inclination = declination = 45 deg.
#: with default scaling.  If different shading is desired,
#: use the `layer_shade_img <geosoft.gxapi.GXAGG.layer_shade_img>` method.
AGG_LAYER_ZONE_SHADE = 4
#: Log Linear Distribution
AGG_LAYER_ZONE_LOGLINEAR = 5
#: The last `GXITR <geosoft.gxapi.GXITR>` used to display this
#: data will be used if it exists.  If it
#: does not exist, the behaviour is the same
#: as `AGG_LAYER_ZONE_DEFAULT <geosoft.gxapi.AGG_LAYER_ZONE_DEFAULT>`.
AGG_LAYER_ZONE_LAST = 6

#
# AGG_MODEL constants
#
# Aggregation color model defines

#: Hue Saturation Value
AGG_MODEL_HSV = 1
#: Red Green Blue
AGG_MODEL_RGB = 2
#: Cyan Magenta Yellow
AGG_MODEL_CMY = 3

#
# AGG_RENDER constants
#
# Aggregation rendering modes

#: Add all the colors together
AGG_RENDER_ADD = 0
#: Adds and divides by the number of non-dummy colors
AGG_RENDER_BLEND = 1
#: Adds and divides by the number of colors
AGG_RENDER_BLEND_ALL = 2
#: Multiplies current colors by the input's colors over 255 (input works as the percentage of color to preserve)
AGG_RENDER_FADE = 3	

#
# GXBF Constants
# 



#
# BF_BYTEORDER constants
#
# Byte order for read/write

#: Least significant byte first (Intel, Windows)
BF_BYTEORDER_LSB = 256
#: Most significant byte first (Mororola, Sun)
BF_BYTEORDER_MSB = 512

#
# BF_CLOSE constants
#
# Close Flags

#: Bf keep
BF_KEEP = 0
#: Bf delete
BF_DELETE = 1

#
# BF_ENCODE constants
#
# The way a string is encoded

#: String is stored as ANSI code page
BF_ENCODE_ANSI = 0
#: String is stored as :ref:`UTF8`
BF_ENCODE_UTF8 = 1

#
# BF_OPEN_MODE constants
#
# Open Status

#: Read only
BF_READ = 0
#: Erases existing file
BF_READWRITE_NEW = 1
#: File must pre-exist
BF_READWRITE_OLD = 2
#: Open and append onto pre-existing file (cannot be read from)
BF_READWRITE_APP = 4

#
# BF_SEEK constants
#
# Seek Location

#: Start
BF_SEEK_START = 0
#: Current
BF_SEEK_CURRENT = 1
#: Eof
BF_SEEK_EOF = 2	

#
# GXDAT Constants
# 



#
# DAT_FILE constants
#
# Type of grid

#: Grid
DAT_FILE_GRID = 1
#: Image
DAT_FILE_IMAGE = 2

#
# DAT_FILE_FORM constants
#
# Type of form

#: Open
DAT_FILE_FORM_OPEN = 0
#: Save
DAT_FILE_FORM_SAVE = 1

#
# DAT_XGD constants
#
# `GXDAT <geosoft.gxapi.GXDAT>` Open modes

#: Read
DAT_XGD_READ = 0
#: New
DAT_XGD_NEW = 1
#: Write
DAT_XGD_WRITE = 2	

#
# GXDATALINKD Constants
# 

	

#
# GXDATAMINE Constants
# 



#
# GIS_DMTYPE constants
#
# Datamine file types

#: String
GIS_DMTYPE_STRING = 2
#: Wireframe tr
GIS_DMTYPE_WIREFRAME_TR = 8
#: Dtm
GIS_DMTYPE_DTM = 16
#: Blockmodel
GIS_DMTYPE_BLOCKMODEL = 32
#: Wireframe pt
GIS_DMTYPE_WIREFRAME_PT = 64
#: Pointdata
GIS_DMTYPE_POINTDATA = 1024	

#
# GXDB Constants
# 



#
# DB_ACTIVITY_BLOB constants
#
# Activity Blob

#: Db activity blob
DB_ACTIVITY_BLOB = "OE.DB_ACTIVITY_LOG"

#
# DB_CATEGORY_BLOB constants
#
# Blob Categories

#: Normal
DB_CATEGORY_BLOB_NORMAL = 0

#
# DB_CATEGORY_CHAN constants
#
# Channel Categories
# For STRING type channels, use negative integers
# to specify channel width. For example, use -10
# to define a string channel with up to 10 characters.
# Use the GS_SIMPLE_TYPE() macro to convert to INT,REAL or string.

#: Byte
DB_CATEGORY_CHAN_BYTE = 0
#: Ushort
DB_CATEGORY_CHAN_USHORT = 1
#: Short
DB_CATEGORY_CHAN_SHORT = 2
#: Long
DB_CATEGORY_CHAN_LONG = 3
#: Float
DB_CATEGORY_CHAN_FLOAT = 4
#: Double
DB_CATEGORY_CHAN_DOUBLE = 5
#: Ubyte
DB_CATEGORY_CHAN_UBYTE = 6
#: Ulong
DB_CATEGORY_CHAN_ULONG = 7
#: Long64
DB_CATEGORY_CHAN_LONG64 = 8
#: Ulong64
DB_CATEGORY_CHAN_ULONG64 = 9

#
# DB_CATEGORY_LINE constants
#
# Line Categories

#: Flight
DB_CATEGORY_LINE_FLIGHT = 100
#: Group
DB_CATEGORY_LINE_GROUP = 200
#: Same as `DB_CATEGORY_LINE_FLIGHT <geosoft.gxapi.DB_CATEGORY_LINE_FLIGHT>`
DB_CATEGORY_LINE_NORMAL = 100

#
# DB_CATEGORY_USER constants
#
# User Categories

#: Normal
DB_CATEGORY_USER_NORMAL = 0

#
# DB_CHAN_FORMAT constants
#
# Channel formats

#: Normal
DB_CHAN_FORMAT_NORMAL = 0
#: Exp
DB_CHAN_FORMAT_EXP = 1
#: Time
DB_CHAN_FORMAT_TIME = 2
#: Date
DB_CHAN_FORMAT_DATE = 3
#: Geogr
DB_CHAN_FORMAT_GEOGR = 4
#: Sigdig
DB_CHAN_FORMAT_SIGDIG = 5
#: Hex
DB_CHAN_FORMAT_HEX = 6

#
# DB_CHAN_PROTECTION constants
#
# Channel Read-only Protection Status

#: Db chan unprotected
DB_CHAN_UNPROTECTED = 0
#: Db chan protected
DB_CHAN_PROTECTED = 1

#
# DB_CHAN_SYMBOL constants
#
# Channel symbol for special channels

#: Db chan x
DB_CHAN_X = 0
#: Db chan y
DB_CHAN_Y = 1
#: Db chan z
DB_CHAN_Z = 2

#
# DB_COMP constants
#
# Supported compression levels

#: None
DB_COMP_NONE = 0
#: Speed
DB_COMP_SPEED = 1
#: Size
DB_COMP_SIZE = 2

#
# DB_COORDPAIR constants
#
# Used to indicate the matching coordinate pair of a channel.

#: None
DB_COORDPAIR_NONE = 0
#: X
DB_COORDPAIR_X = 1
#: Y
DB_COORDPAIR_Y = 2

#
# DB_GROUP_CLASS_SIZE constants
#
# Class name max size

#: Db group class size
DB_GROUP_CLASS_SIZE = 16

#
# DB_INFO constants
#
# Integer Database Information

#: Maximum Number of Blobs in the Database
DB_INFO_BLOBS_MAX = 0
#: Maximum number of lines in the database
DB_INFO_LINES_MAX = 1
#: Maximum Number of Channels in the Database
DB_INFO_CHANS_MAX = 2
#: Maximum number of Users
DB_INFO_USERS_MAX = 3
#: Number of Blobs currently used
DB_INFO_BLOBS_USED = 4
#: Number of Lines currently used
DB_INFO_LINES_USED = 5
#: Number of Channels currently used
DB_INFO_CHANS_USED = 6
#: Number of Users in the database
DB_INFO_USERS_USED = 7
#: Size of the smallest database block in bytes
DB_INFO_PAGE_SIZE = 8
#: Number of Blocks in Entire Database
DB_INFO_DATA_SIZE = 9
#: Number of Lost Blocks in the Database
DB_INFO_LOST_SIZE = 10
#: Number of Free Blocks in the Database
DB_INFO_FREE_SIZE = 11
#: Compression Level in use
DB_INFO_COMP_LEVEL = 16
#: Number of pages given to blobs
DB_INFO_BLOB_SIZE = 19
#: Entire Size of File (in kbytes)
DB_INFO_FILE_SIZE = 17
#: Size of Index (in kbytes)
DB_INFO_INDEX_SIZE = 18
#: Naximum number of bytes in a block
DB_INFO_MAX_BLOCK_SIZE = 20
#: Will changes to this database be lost when this database is closed?
DB_INFO_CHANGESLOST = 21

#
# DB_LINE_LABEL_FORMAT constants
#
# Line Label Formats

#: Line
DB_LINE_LABEL_FORMAT_LINE = 1
#: Version
DB_LINE_LABEL_FORMAT_VERSION = 2
#: Type
DB_LINE_LABEL_FORMAT_TYPE = 4
#: Flight
DB_LINE_LABEL_FORMAT_FLIGHT = 8
#: Full
DB_LINE_LABEL_FORMAT_FULL = 15
#: Date
DB_LINE_LABEL_FORMAT_DATE = 16
#: Link
DB_LINE_LABEL_FORMAT_LINK = 7

#
# DB_LINE_SELECT constants
#
# Select modes

#: Include
DB_LINE_SELECT_INCLUDE = 0
#: Exclude
DB_LINE_SELECT_EXCLUDE = 1

#
# DB_LINE_TYPE constants
#
# Line types

#: Normal
DB_LINE_TYPE_NORMAL = 0
#: Base
DB_LINE_TYPE_BASE = 1
#: Tie
DB_LINE_TYPE_TIE = 2
#: Test
DB_LINE_TYPE_TEST = 3
#: Trend
DB_LINE_TYPE_TREND = 4
#: Special
DB_LINE_TYPE_SPECIAL = 5
#: Random
DB_LINE_TYPE_RANDOM = 6

#
# DB_LOCK constants
#
# Lock Modes

#: Used only by GetSymbLock_DB
DB_LOCK_NONE = -1
#: Readonly
DB_LOCK_READONLY = 0
#: Readwrite
DB_LOCK_READWRITE = 1

#
# DB_NAME constants
#
# Get Database file names

#: File
DB_NAME_FILE = 0

#
# DB_OWN constants
#
# Symbol Ownership

#: Shared
DB_OWN_SHARED = 0
#: User
DB_OWN_USER = 1

#
# DB_SYMB_TYPE constants
#
# Symbol types

#: Db symb blob
DB_SYMB_BLOB = 0
#: Db symb line
DB_SYMB_LINE = 1
#: Db symb chan
DB_SYMB_CHAN = 2
#: Db symb user
DB_SYMB_USER = 3

#
# DB_SYMB_NAME_SIZE constants
#
# Size of Symbol Names

#: Same `STR_DB_SYMBOL <geosoft.gxapi.STR_DB_SYMBOL>`
DB_SYMB_NAME_SIZE = 64

#
# DB_WAIT constants
#
# Wait Times

#: None
DB_WAIT_NONE = 0
#: Infinity
DB_WAIT_INFINITY = -1

#
# DB_ARRAY_BASETYPE constants
#
# Array channel base coordinate type

#: None
DB_ARRAY_BASETYPE_NONE = 0
#: Time windows
DB_ARRAY_BASETYPE_TIME_WINDOWS = 1
#: Times
DB_ARRAY_BASETYPE_TIMES = 2
#: Frequencies
DB_ARRAY_BASETYPE_FREQUENCIES = 3
#: Elevations
DB_ARRAY_BASETYPE_ELEVATIONS = 4
#: Depths
DB_ARRAY_BASETYPE_DEPTHS = 5
#: Velocities
DB_ARRAY_BASETYPE_VELOCITIES = 6
#: Discrete time windows
DB_ARRAY_BASETYPE_DISCRETE_TIME_WINDOWS = 7

#
# NULLSYMB constants
#
# Database Null

#: Nullsymb
NULLSYMB = -1	

#
# GXDBREAD Constants
# 

	

#
# GXDBWRITE Constants
# 

	

#
# GXDSEL Constants
# 



#
# DSEL_PICTURE_QUALITY constants
#
# Line Label Formats

#: Default
DSEL_PICTURE_QUALITY_DEFAULT = 0
#: Lossless
DSEL_PICTURE_QUALITY_LOSSLESS = 1
#: Semilossy
DSEL_PICTURE_QUALITY_SEMILOSSY = 2
#: Lossy
DSEL_PICTURE_QUALITY_LOSSY = 3
#: Native
DSEL_PICTURE_QUALITY_NATIVE = 4
#: Ecw
DSEL_PICTURE_QUALITY_ECW = 5
#: Jpg
DSEL_PICTURE_QUALITY_JPG = 6
#: Png
DSEL_PICTURE_QUALITY_PNG = 7
#: Bmp
DSEL_PICTURE_QUALITY_BMP = 8
#: Tif
DSEL_PICTURE_QUALITY_TIF = 9	

#
# GXE3DV Constants
# 

	

#
# GXEXT Constants
# 

	

#
# GXGEO Constants
# 

	

#
# GXGEOSOFT Constants
# 



#
# CRC_INIT_VALUE constants
#
# Initial value for starting a CRC

#: 0xFFFFFFFF
CRC_INIT_VALUE = 4294967295

#
# DATE_FORMAT constants
#
# Old Date formats

#: Standard Date (YYYY/MM/DD, YY/MM/DD, YYYYMMDD or YYMMDD, space or / delimited)
DATE_FORMAT_YYYYMMDD = 1
#: Date (DD/MM/YYYY or DD/MM/YY century 20 if YY>50, DISC compliant)
DATE_FORMAT_DDMMYYYY = 2
#: Date (MM/DD/YYYY or MM/DD/YY century 19)
DATE_FORMAT_MMDDYYYY = 3

#
# GEO_DUMMY constants
#
# Special numbers indicating NULLL

#: Integer Dummy (-2147483647)
iDUMMY = -2147483647
#: Floating Point Dummy (-1.0E32)
rDUMMY = -1.0E32

#
# GEO_FULL_LIMITS constants
#
# Data ranges of all Geosoft types

#: (signed char   )   127
GS_S1MX = 127
#: (signed char   )  -126
GS_S1MN = -126
#: (signed char   )  -127
GS_S1DM = -127
#: (unsigned char )   254U
GS_U1MX = 254
#: (unsigned char )   0U
GS_U1MN = 0
#: (unsigned char )   255U
GS_U1DM = 255
#: (short         )   32767
GS_S2MX = 32767
#: (short         )  -32766
GS_S2MN = -32766
#: (short         )  -32767
GS_S2DM = -32767
#: (unsigned short)   65534U
GS_U2MX = 65534
#: (unsigned short)   0U
GS_U2MN = 0
#: (unsigned short)   65535U
GS_U2DM = 65535
#: 2147483647L
GS_S4MX = 2147483647
#: -2147483646L
GS_S4MN = -2147483646
#: -2147483647L
GS_S4DM = -2147483647
#: (unsigned long )   0xFFFFFFFE
GS_U4MX = struct.unpack('>I', bytes.fromhex('FFFFFFFE'))[0]
#: (unsigned long )   0x00000000
GS_U4MN = struct.unpack('>I', bytes.fromhex('00000000'))[0]
#: (unsigned long )   0xFFFFFFFF
GS_U4DM = struct.unpack('>I', bytes.fromhex('FFFFFFFF'))[0]
#: (__GS_INT64    )   0x7FFFFFFFFFFFFFFF
GS_S8MX = struct.unpack('>q', bytes.fromhex('7FFFFFFFFFFFFFFF'))[0]
#: (__GS_INT64    )   0x8000000000000001
GS_S8MN = struct.unpack('>q', bytes.fromhex('8000000000000001'))[0]
#: (__GS_INT64    )   0x8000000000000000
GS_S8DM = struct.unpack('>q', bytes.fromhex('8000000000000000'))[0]
#: (__GS_UINT64   )   0xFFFFFFFFFFFFFFFE
GS_U8MX = struct.unpack('>Q', bytes.fromhex('FFFFFFFFFFFFFFFE'))[0]
#: (__GS_UINT64   )   0x0000000000000000
GS_U8MN = struct.unpack('>Q', bytes.fromhex('0000000000000000'))[0]
#: (__GS_UINT64   )   0xFFFFFFFFFFFFFFFF
GS_U8DM = struct.unpack('>Q', bytes.fromhex('FFFFFFFFFFFFFFFF'))[0]
#: (float         )   1.0E32   (In C these must be declared as external constants:)
GS_R4MX = 1.0E32
#: (float         )  -0.9E32     const float r4min=(float)-0.9E32,
GS_R4MN = -0.9E32
#: (float         )  -1.0E32                 r4max=(float)1.0E32,
#: r4dum=(float)-1.0E32;
GS_R4DM = -1.0E32
#: (double        )   1.0E32
GS_R8MX = 1.0E32
#: (double        )  -0.9E32
GS_R8MN = -0.9E+32
#: (double        )  -1.0E32
GS_R8DM = -1.0E+32
#: (float         )   1.0E-32
GS_R4EPSILON = 1.0E-32
#: (double        )   1.0E-32
GS_R8EPSILON = 1.0E-32

#
# GEO_LIMITS constants
#
# Data ranges of numbers

#: Smallest Integer (-2147483646)
iMIN = -2147483646
#: Largest Integer (2147483647)
iMAX = 2147483647
#: Smallest Floating Point (-0.9E32)
rMIN = -0.9E32
#: Largest Floating Point (1.0E32)
rMAX = 1.0E32

#
# GEO_STRING_SIZE constants
#
# Default string sized for different uses
# GX's must use these unless there is a
# very good reason not to. The path strings
# here are generally larger than what is possible
# in the OS, but it is defined as such for Unicode
# conversion reasons.

#: Default Size for almost everything (128 characters)
STR_DEFAULT = 128
#: Default Size for a short string (64 characters)
STR_DEFAULT_SHORT = 64
#: Default Size for a long string (1024 characters)
STR_DEFAULT_LONG = 1024
#: Default Size for an error string (2048 characters)
STR_ERROR = 2048
#: Default Size for a long string (16384 characters)
STR_VERY_LONG = 16384
#: Name of a View (2080)
STR_VIEW = 2080
#: Name of a Group (1040)
STR_GROUP = 1040
#: Combined View/Group Name (2080)
STR_VIEW_GROUP = 2080
#: Name of a file (1040)
STR_FILE = 1040
#: Name of multiple files (16384)
STR_MULTI_FILE = 16384
#: Name of database symbol (64)
STR_DB_SYMBOL = 64
#: Size of strings for GXF projection info (160).
STR_GXF = 160
#: Maximum path length (1040)
STR_MAX_PATH = 1040
#: Multi-file path (16384)
STR_MULTI_PATH = 16384
#: Same as `STR_FILE <geosoft.gxapi.STR_FILE>`
GS_MAX_PATH = 1040
#: Same as `STR_MULTI_FILE <geosoft.gxapi.STR_MULTI_FILE>`
GS_MULTI_PATH = 16384

#
# GEO_BOOL constants
#
# Boolean values

#: False
GS_FALSE = 0
#: True
GS_TRUE = 1

#
# GEO_VAR constants
#
# Variable types.
# Use -X for strings of X length

#: Integer (long)
GS_INT = 0
#: Floating Point (double)
GS_REAL = 1

#
# GS_FORMATS constants
#
# Special use data types. String are indicated by a
# negative maximum string length (including NULL).

#: Standard numbers (-134.534)
FORMAT_DECIMAL = 0
#: Decimals imply number of significant digits
FORMAT_SIG_DIG = 5
#: Exponential notation (-1.345e45)
FORMAT_EXP = 1
#: Standard Time (HH:MM:SS.SSSS)
FORMAT_TIME_COLON = 2
#: Time (HH.MMSSSSSSS)
FORMAT_TIME_HMS = 8
#: Time (HHMMSS)
FORMAT_TIME_HHMMSS = 9
#: Standard Date (YYYY/MM/DD, YY/MM/DD, YYYYMMDD or YYMMDD, space or / delimited)
FORMAT_DATE_YYYYMMDD = 3
#: Date (DD/MM/YYYY or DD/MM/YY century 20 if YY>50, DISC compliant)
FORMAT_DATE_DDMMYYYY = 6
#: Date (MM/DD/YYYY or MM/DD/YY century 19)
FORMAT_DATE_MMDDYYYY = 7
#: Standard Geographical (DEG.MM.SS.SSS)
FORMAT_GEOGRAPHIC = 4
#: GeoGraph (DEG:MM:SS.SSS)
FORMAT_GEOGRAPHIC_1 = 10
#: GeoGraph (DEG.MMSSSSS)
FORMAT_GEOGRAPHIC_2 = 11
#: GeoGraph (DEGMMmmmm or DEGMM.mmmm or DEG.MM.mmmm)  (mmmm: decimal minute)
FORMAT_GEOGRAPHIC_3 = 12

#
# GS_TYPES constants
#
# Special use data types. String are indicated by a
# negative maximum string length (including NULL).

#: Signed Byte
GS_BYTE = 0
#: Unsigned Short
GS_USHORT = 1
#: Signed Short
GS_SHORT = 2
#: Signed Long
GS_LONG = 3
#: 32-Bit floating point
GS_FLOAT = 4
#: 64-Bit floating point
GS_DOUBLE = 5
#: Unsigned byte
GS_UBYTE = 6
#: Unsigned Long
GS_ULONG = 7
#: 64-Bit signed long
GS_LONG64 = 8
#: 64-Bit unsigned long
GS_ULONG64 = 9
#: 3 x 32-Bit floating point
GS_FLOAT3D = 10
#: 3 x 64-Bit floating point
GS_DOUBLE3D = 11
#: 2 x 32-Bit floating point
GS_FLOAT2D = 12
#: 2 x 64-Bit floating point
GS_DOUBLE2D = 13
#: Maximum supported type (`GS_DOUBLE2D <geosoft.gxapi.GS_DOUBLE2D>`)
GS_MAXTYPE = 13
#: Default. Can be used only when a method specifically allows a default type.
GS_TYPE_DEFAULT = -32767

#
# SYS_CRYPT_KEY constants
#
# Special Encryption Keys

#: Using the current license key
SYS_CRYPT_LICENSE_KEY = "{***LICENSE_KEY***}"
#: Use the current computer ID
SYS_CRYPT_COMPUTER_ID = "{***COMPUTER_ID***}"
#: Use the non-changing computer ID
SYS_CRYPT_GLOBAL_ID = "{***GLOBAL_COMPUTER_ID***}"

#
# TIME_FORMAT constants
#
# Old Time formats

#: Standard Time (HH:MM:SS.SSSS)
TIME_FORMAT_COLON = 1
#: Time (HH.MMSSSSSSS)
TIME_FORMAT_HMS = 2	

#
# GXGEOSTRING Constants
# 



#
# GEOSTRING_OPEN constants
#
# Open Modes

#: Read
GEOSTRING_OPEN_READ = 0
#: Readwrite
GEOSTRING_OPEN_READWRITE = 1

#
# SECTION_ORIENTATION constants
#
# Section orientation types

#: Unknown
SECTION_ORIENTATION_UNKNOWN = 0
#: Plan
SECTION_ORIENTATION_PLAN = 1
#: Section
SECTION_ORIENTATION_SECTION = 2
#: Crooked
SECTION_ORIENTATION_CROOKED = 2
#: Gmsys
SECTION_ORIENTATION_GMSYS = 2	

#
# GXGIS Constants
# 



#
# GIS_MAP2D constants
#
# View type to create

#: Plan view
GIS_MAP2D_PLAN = 0
#: Section view, East-West
GIS_MAP2D_EWSECTION = 1
#: Section view, North-South
GIS_MAP2D_NSSECTION = 2

#
# GIS_TYPE constants
#
# Type of file

#: Mapinfo Files
GIS_TYPE_MAPINFO = 1
#: ArcView files
GIS_TYPE_ARCVIEW = 2
#: Microstation DGN files
GIS_TYPE_DGN = 3
#: Surpac `GXSTR <geosoft.gxapi.GXSTR>` and DTM files
GIS_TYPE_SURPAC = 4
#: Datamine DM files
GIS_TYPE_DATAMINE = 5
#: GEMCOM files
GIS_TYPE_GEMCOM = 6
#: MICROMINE files
GIS_TYPE_MICROMINE = 7
#: MINESIGHT files
GIS_TYPE_MINESIGHT = 8	

#
# GXGRID3D Constants
# 



#
# GRID3D_TYPE constants
#
# Type of Voxset

#: DOUBLE
GRID3D_DOUBLE = 0
#: VECTOR
GRID3D_VECTOR = 1
#: THEMATIC
GRID3D_THEMATIC = 2	

#
# GXHGD Constants
# 

	

#
# GXHXYZ Constants
# 

	

#
# GXIGRF Constants
# 

	

#
# GXIMG Constants
# 



#
# IMG_FILE constants
#
# Image open modes

#: Reading only
IMG_FILE_READONLY = 0
#: Reading and writting
IMG_FILE_READWRITE = 2
#: Allows you to open read-only grids to change the
#: projection or location information.  If you can write
#: to the original grid (dat), the changed projection
#: or location information will be passed on to the grid,
#: otherwise changes will only occur in the .gi file.
IMG_FILE_READORWRITE = 3

#
# IMG_QUERY constants
#
# Information to Query

#: Iwrite
IMG_QUERY_iWRITE = 0
#: Ipg
IMG_QUERY_iPG = 1
#: Iwritepg
IMG_QUERY_iWRITEPG = 2
#: The element type used to open the `GXIMG <geosoft.gxapi.GXIMG>`.
IMG_QUERY_iIMGTYPE = 3
#: DATTYPE is the native element type of the `GXDAT <geosoft.gxapi.GXDAT>`.
#: Types are:   0 - byte
#: 1 - unsigned 16-bit short
#: 2 - 16-bit short
#: 3 - 32-bit long
#: 4 - 32-bit float
#: 5 - 64-bit double
IMG_QUERY_iDATTYPE = 4
#: Render modes are:    0 - interpolate
#: 1 - pixelate
#: 2 - color
IMG_QUERY_iRENDER = 5
#: Ikx
IMG_QUERY_iKX = 6
#: Inx
IMG_QUERY_iNX = 7
#: Iny
IMG_QUERY_iNY = 8
#: Inv
IMG_QUERY_iNV = 9
#: Ine
IMG_QUERY_iNE = 10
#: Rxo
IMG_QUERY_rXO = 11
#: Ryo
IMG_QUERY_rYO = 12
#: Rdx
IMG_QUERY_rDX = 13
#: Rdy
IMG_QUERY_rDY = 14
#: Rrot
IMG_QUERY_rROT = 15
#: Rbase
IMG_QUERY_rBASE = 16
#: Rmult
IMG_QUERY_rMULT = 17
#: Rcompression ratio
IMG_QUERY_rCOMPRESSION_RATIO = 18

#
# IMG_RELOCATE constants
#
# Relocation Style

#: Will fit the image to fill the specified area
IMG_RELOCATE_FIT = 0
#: Will maintain aspect ratio
IMG_RELOCATE_ASPECT = 1	

#
# GXIMU Constants
# 



#
# IMU_BOOL_OLAP constants
#
# Overlapping area option

#: Overlap values are averaged
IMU_BOOL_OLAP_AVE = 0
#: Overlap values use grid 1 value
IMU_BOOL_OLAP_1 = 1
#: Overlap values use grid 2 value
IMU_BOOL_OLAP_2 = 2

#
# IMU_BOOL_OPT constants
#
# Boolean logic option

#: Valid areas are only where grids overlap
IMU_BOOL_OPT_AND = 0
#: Valid areas are where either grid is a valid value
IMU_BOOL_OPT_OR = 1
#: Overlap areas are dummied
IMU_BOOL_OPT_XOR = 2

#
# IMU_BOOL_SIZING constants
#
# Sizing option

#: Output grid is sized to overlapping region
IMU_BOOL_SIZING_MIN = 0
#: Output grid is sized to grid 1
IMU_BOOL_SIZING_0 = 1
#: Output grid is sized to grid 2
IMU_BOOL_SIZING_1 = 2
#: Output grid is sized to maximum combined area of both grids
IMU_BOOL_SIZING_MAX = 3

#
# IMU_DOUBLE_CRC_BITS constants
#
# Bits to use in double CRC's

#: Exact CRC
IMU_DOUBLE_CRC_BITS_EXACT = 0
#: Default inaccuracy in double (10 Bits)
IMU_DOUBLE_CRC_BITS_DEFAULT = 10
#: Maximum number of inaccuracy bits (51 Bits)
IMU_DOUBLE_CRC_BITS_MAX = 51

#
# IMU_EXPAND_SHAPE constants
#
# Shape of output grid

#: Rectangle
IMU_EXPAND_SHAPE_RECTANGLE = 0
#: Square
IMU_EXPAND_SHAPE_SQUARE = 1

#
# IMU_FILL_ROLLOPT constants
#
# Defines for Grid Filling Method Options

#: Linear
IMU_FILL_ROLLOPT_LINEAR = 1
#: Square
IMU_FILL_ROLLOPT_SQUARE = 2

#
# IMU_FILT_DUMMY constants
#
# Settings for placing dummy values in grid if any of filter
# values are dummy

#: No
IMU_FILT_DUMMY_NO = 0
#: Yes
IMU_FILT_DUMMY_YES = 1

#
# IMU_FILT_FILE constants
#
# Flags which indicate if a file is to be used to read the
# filter values

#: No
IMU_FILT_FILE_NO = 0
#: Yes
IMU_FILT_FILE_YES = 1

#
# IMU_FILT_HZDRV constants
#
# Flags which indicate which type of horizontal derivative
# is being applied (X direction, Y direction, none at all)

#: No
IMU_FILT_HZDRV_NO = 0
#: X
IMU_FILT_HZDRV_X = 1
#: Y
IMU_FILT_HZDRV_Y = 2

#
# IMU_FLOAT_CRC_BITS constants
#
# Bits to use in float CRC's

#: Exact CRC
IMU_FLOAT_CRC_BITS_EXACT = 0
#: Default inaccuracy in floats (7 Bits)
IMU_FLOAT_CRC_BITS_DEFAULT = 7
#: Maximum number of inaccuracy bits (22 Bits)
IMU_FLOAT_CRC_BITS_MAX = 22

#
# IMU_MASK constants
#
# Defined options for masking grids

#: Inside
IMU_MASK_INSIDE = 0
#: Outside
IMU_MASK_OUTSIDE = 1

#
# IMU_STAT_FORCED constants
#
# Defined options for forcing recalculating the grid values

#: No
IMU_STAT_FORCED_NO = 0
#: Yes
IMU_STAT_FORCED_YES = 1

#
# IMU_TRANS constants
#
# Transpose Options available for `grid_trns <geosoft.gxapi.GXIMU.grid_trns>`
# implies original grid lines:

#: Can be ANY orientation
IMU_TRANS_DEFAULT = 0
#: MUST be parallel to Y-Axis
IMU_TRANS_Y = 1
#: MUST be parallel to X-Axis
IMU_TRANS_X = -1

#
# IMU_TREND constants
#
# Points in grid to use

#: All
IMU_TREND_ALL = 0
#: Edge
IMU_TREND_EDGE = 1

#
# IMU_WIND_COORD constants
#
# Output grid coordinate units

#: Imu wind grid
IMU_WIND_GRID = 0
#: Imu wind ground
IMU_WIND_GROUND = 1

#
# IMU_WIND_DUMMIES constants
#
# Option for handling out-of-range Z values

#: Imu wind dummy
IMU_WIND_DUMMY = 0
#: Imu wind clip
IMU_WIND_CLIP = 1

#
# IMU_XYZ_INDEX constants
#
# Flags whether to use grid index numbers as
# station numbers.

#: No
IMU_XYZ_INDEX_NO = 0
#: Yes
IMU_XYZ_INDEX_YES = 1

#
# IMU_XYZ_LABEL constants
#
# XYZ Label Flags

#: No
IMU_XYZ_LABEL_NO = 1
#: Yes
IMU_XYZ_LABEL_YES = 0	

#
# GXIPJ Constants
# 



#
# IPJ_3D_FLAG constants
#
# 3D Flags

#: Standard
IPJ_3D_FLAG_NONE = 0
#: Invert angle rotation during matrix creation
IPJ_3D_FLAG_INVERTANGLES = 1
#: Invert the Z plane to make up down.
IPJ_3D_FLAG_INVERTZ = 2
#: Apply rotations in a specific order, determined by pdParm[7]
IPJ_3D_FLAG_ORDER_ROTATION = 4

#
# IPJ_3D_ROTATE constants
#
# 3D Rotation Mode

#: Default
IPJ_3D_ROTATE_DEFAULT = 0
#: Xyz
IPJ_3D_ROTATE_XYZ = 1
#: Xzy
IPJ_3D_ROTATE_XZY = 2
#: Yxz
IPJ_3D_ROTATE_YXZ = 3
#: Yzx
IPJ_3D_ROTATE_YZX = 4
#: Zxy
IPJ_3D_ROTATE_ZXY = 5
#: Zyx
IPJ_3D_ROTATE_ZYX = 6

#
# IPJ_CSP constants
#
# Projection Setting

#: Scale
IPJ_CSP_SCALE = 0
#: Falseeast
IPJ_CSP_FALSEEAST = 1
#: Falsenorth
IPJ_CSP_FALSENORTH = 2
#: Latorigin
IPJ_CSP_LATORIGIN = 3
#: Lonorigin
IPJ_CSP_LONORIGIN = 4
#: Parallel 1
IPJ_CSP_PARALLEL_1 = 5
#: Parallel 2
IPJ_CSP_PARALLEL_2 = 6
#: Azimuth
IPJ_CSP_AZIMUTH = 7
#: Angle
IPJ_CSP_ANGLE = 8
#: Pointlat 1
IPJ_CSP_POINTLAT_1 = 9
#: Pointlon 1
IPJ_CSP_POINTLON_1 = 10
#: Pointlat 2
IPJ_CSP_POINTLAT_2 = 11
#: Pointlon 2
IPJ_CSP_POINTLON_2 = 12

#
# IPJ_NAME constants
#
# Project Name

#: Projected coordinate system name
IPJ_NAME_PCS = 0
#: Projection name
IPJ_NAME_PROJECTION = 1
#: Projection method name
IPJ_NAME_METHOD = 2
#: Datum name
IPJ_NAME_DATUM = 3
#: Ellipsoid name
IPJ_NAME_ELLIPSOID = 4
#: Local datum name
IPJ_NAME_LDATUM = 5
#: Unit abbreviation
IPJ_NAME_UNIT_ABBR = 6
#: Full unit name
IPJ_NAME_UNIT_FULL = 7
#: Projection type description
IPJ_NAME_TYPE = 8
#: Datum transform table name
IPJ_NAME_LLDATUM = 9
#: Projection method parameters in GXF order
IPJ_NAME_METHOD_PARMS = 10
#: Projection method parameters labels
IPJ_NAME_METHOD_LABEL = 11
#: Datum parameters (major axis, flattening, prime meridian)
IPJ_NAME_DATUM_PARMS = 12
#: local datum parameters (dX,dY,dZ,rX,rY,rZ,scale)
#: See GXF revision 3 for parameter list order and
#: specifications.
IPJ_NAME_LDATUM_PARMS = 13
#: Geoid name if known
IPJ_NAME_GEOID = 14
#: Local datum description
IPJ_NAME_LDATUMDESCRIPTION = 15
#: Projection method parameters in GXF order (Native units for eastings/northings)
IPJ_NAME_METHOD_PARMS_NATIVE = 16
#: Orientation parameters
IPJ_NAME_ORIENTATION_PARMS = 17

#
# IPJ_ORIENT constants
#
# Projection Orientation

#: no special orientation - plan view. All views in maps
#: created before v5.1.3 will return this value.
IPJ_ORIENT_DEFAULT = 0
#: A plan view with a reference elevation and
#: optional rotation.
IPJ_ORIENT_PLAN = 1
#: Has an azimuth and swing.
#: The section view projects all plotted objects
#: HORIZONTALLY onto the viewing plan in order to
#: preserve elevations, even if the section has a swing.
IPJ_ORIENT_SECTION = 2
#: Same as `IPJ_ORIENT_SECTION <geosoft.gxapi.IPJ_ORIENT_SECTION>`, but the projection is perpendicular
#: to the section, not horizonatl, so elevatins are not preserved
#: on swung sections.
IPJ_ORIENT_SECTION_NORMAL = 5
#: This simple section has no azimuth or swing defined;
#: only the depth is of importance, and it is output as
#: the Y parameter, increasing downward. Used (for instance)
#: for strip logs in Wholeplot.
IPJ_ORIENT_DEPTH_SECTION = 3
#: A 3D rotation/scaling/translation orientation
IPJ_ORIENT_3D = 4
#: A 3D matrix orientation
IPJ_ORIENT_3D_MATRIX = 7
#: This is a vertical section that follows a
#: curving path, like a river or survey traverse.
#: The horizontal section location is the distance along
#: the path, while the vertical axis gives the elevation.
IPJ_ORIENT_SECTION_CROOKED = 6

#
# IPJ_PARM_LST constants
#
# Projection List

#: Coordinatesystem
IPJ_PARM_LST_COORDINATESYSTEM = 0
#: Datum
IPJ_PARM_LST_DATUM = 1
#: Projection
IPJ_PARM_LST_PROJECTION = 2
#: Units
IPJ_PARM_LST_UNITS = 3
#: Localdatumdescription
IPJ_PARM_LST_LOCALDATUMDESCRIPTION = 4
#: Localdatumname
IPJ_PARM_LST_LOCALDATUMNAME = 5
#: Unitsdescription
IPJ_PARM_LST_UNITSDESCRIPTION = 6

#
# IPJ_TYPE constants
#
# `GXIPJ <geosoft.gxapi.GXIPJ>` Types

#: Read from a PRJ file:
#: string 1 - Source file name
#: string 2 and 3 are not used.
IPJ_TYPE_PRJ = 0
#: Projected coordinate system:
#: string 1 - POSC PCS name
#: string 2 - POSC Datum transform name
#: string 3 - not used.
IPJ_TYPE_PCS = 1
#: Geographic coordinate system:
#: string 1 - POSC Datum name
#: string 2 - POSC Datum transform name
#: string 3 - not used.
IPJ_TYPE_GCS = 2
#: Custom projection
#: string 1 - POSC Datum name
#: string 2 - POSC Datum transform name
#: string 3 - POSC Transform, "" if geographic
IPJ_TYPE_ANY = 3
#: Not used for `read <geosoft.gxapi.GXIPJ.read>`.  This is used for
#: `source_type <geosoft.gxapi.GXIPJ.source_type>` to indicate no projection.
IPJ_TYPE_NONE = 4
#: Wrp
IPJ_TYPE_WRP = 5
#: tests the projection tables for internal consistency
#: and creates report files in the project directory.
#: string 1 - outout report file name
#: string 2 - ESRI coordinate strings file.  This contains one
#: ESRI coordinate string per line.  Lines that
#: start with '#' are skipped.
#: string 3 - not currently used
IPJ_TYPE_TEST = 6

#
# IPJ_UNIT constants
#
# Projection Unit Type

#: Abbreviation
IPJ_UNIT_ABBREVIATION = 0
#: Fullname
IPJ_UNIT_FULLNAME = 1

#
# IPJ_WARP constants
#
# Warp (Transformation) type

#: Matrix Warp
IPJ_WARP_MATRIX = -1
#: No warp
IPJ_WARP_NONE = 0
#: Translate only (needs 1 point)
IPJ_WARP_TRANS1 = 1
#: Translate, rotate, normal scale (needs 2 pts)
IPJ_WARP_TRANS2 = 2
#: Translate, rotate, scale X and Y (needs 3 pts or more, least-square fit)
IPJ_WARP_TRANS3 = 3
#: Quadrilateral warp (needs 4 points)
IPJ_WARP_QUAD = 4
#: Multipoint warp (needs at least 3 points)
IPJ_WARP_MULTIPOINT = 5
#: Convert from linear to log coords in X and/or Y
IPJ_WARP_LOG = 6
#: Multipoint warp in Y only (needs at least 3 points)
IPJ_WARP_MULTIPOINT_Y = 7	

#
# GXITR Constants
# 



#
# ITR_COLOR_MODEL constants
#
# `GXITR <geosoft.gxapi.GXITR>` Color Model defines

#: Hsv
ITR_COLOR_MODEL_HSV = 1
#: Rgb
ITR_COLOR_MODEL_RGB = 2
#: Cmy
ITR_COLOR_MODEL_CMY = 3

#
# ITR_POWER constants
#
# Power Zoning defines

#: Power of 10
ITR_POWER_10 = 0
#: Exponential
ITR_POWER_EXP = 1

#
# ITR_ZONE constants
#
# Zoning Methods

#: Default
ITR_ZONE_DEFAULT = 0
#: Linear
ITR_ZONE_LINEAR = 1
#: Normal
ITR_ZONE_NORMAL = 2
#: Equalarea
ITR_ZONE_EQUALAREA = 3
#: Shade
ITR_ZONE_SHADE = 4
#: Loglinear
ITR_ZONE_LOGLINEAR = 5

#
# ITR_ZONE_MODEL constants
#
# `GXITR <geosoft.gxapi.GXITR>` Zone Model defines

#: The `GXITR <geosoft.gxapi.GXITR>` has no numeric zones defined (e.g. from a TBL file)
ITR_ZONE_MODEL_NOZONE = -1
#: There is no specific zone model defined.
ITR_ZONE_MODEL_NONE = 0
#: The `GXITR <geosoft.gxapi.GXITR>` is set up with a linear transform.
ITR_ZONE_MODEL_LINEAR = 1
#: The `GXITR <geosoft.gxapi.GXITR>` is set up with a normal distribution transform.
ITR_ZONE_MODEL_NORMAL = 2
#: The `GXITR <geosoft.gxapi.GXITR>` is set up with an equal area transform.
ITR_ZONE_MODEL_EQUAL = 3
#: The `GXITR <geosoft.gxapi.GXITR>` is set up with a log-linear transform.
ITR_MODEL_LOGLIN = 4	

#
# GXLAYOUT Constants
# 



#
# LAYOUT_CONSTR constants
#
# Layout constraint specifiers

#: Adjust rectangle's left side
LAYOUT_CONSTR_LEFT = 0
#: Adjust rectangle's right side
LAYOUT_CONSTR_RIGHT = 1
#: Adjust rectangle's top side
LAYOUT_CONSTR_TOP = 2
#: Adjust rectangle's bottom side
LAYOUT_CONSTR_BOTTOM = 3
#: Adjust rectangle's width
LAYOUT_CONSTR_WIDTH = 4
#: Adjust rectangle's height
LAYOUT_CONSTR_HEIGHT = 5
#: Center rectangle with respect to width
LAYOUT_CONSTR_HCENTER = 6
#: Center rectangle with respect to height
LAYOUT_CONSTR_VCENTER = 7
#: Move rectangle, with respect to left
LAYOUT_CONSTR_MOVEL = 8
#: Move rectangle, with respect to right
LAYOUT_CONSTR_MOVER = 9
#: Move rectangle, with respect to top
LAYOUT_CONSTR_MOVET = 10
#: Move rectangle, with respect to bottom
LAYOUT_CONSTR_MOVEB = 11	

#
# GXLL2 Constants
# 

	

#
# GXLPT Constants
# 

	

#
# GXLST Constants
# 



#
# LST_ITEM constants
#
# `GXLST <geosoft.gxapi.GXLST>` data access

#: Access the "Name" part of the `GXLST <geosoft.gxapi.GXLST>` item.
LST_ITEM_NAME = 0
#: Access the "Value" part of the `GXLST <geosoft.gxapi.GXLST>` item.
LST_ITEM_VALUE = 1	

#
# GXLTB Constants
# 



#
# LTB_CASE constants
#
# Case handling of `GXLTB <geosoft.gxapi.GXLTB>` strings

#: Ignore case
LTB_CASE_INSENSITIVE = 0
#: Case is used
LTB_CASE_SENSITIVE = 1

#
# LTB_CONLST constants
#
# Matching types

#: Exact
LTB_CONLST_EXACT = 0
#: Any
LTB_CONLST_ANY = 1

#
# LTB_DELIM constants
#
# Types of `GXLTB <geosoft.gxapi.GXLTB>` Delimiters

#: Spaces
LTB_DELIM_SPACE = 0
#: Commas
LTB_DELIM_COMMA = 1
#: Spaces and Commas
LTB_DELIM_SPACECOMMA = 2

#
# LTB_TYPE constants
#
# Types of `GXLTB <geosoft.gxapi.GXLTB>` Headers

#: Has a header
LTB_TYPE_HEADER = 0
#: Has no header
LTB_TYPE_NOHEADER = 1	

#
# GXMAP Constants
# 



#
# DUPMAP constants
#
# Duplicate Modes

#: Blank
DUPMAP_BLANK = 0
#: Copy all current contents
DUPMAP_COPY = 1
#: Copy all current contents and save text for pre-6.2 versions.
DUPMAP_COPY_PRE62 = 2

#
# MAP_EXPORT_BITS constants
#
# Color Types

#: 32 Bit Color (8-bit alpha)
MAP_EXPORT_BITS_32 = 32
#: 24 Bit Color
MAP_EXPORT_BITS_24 = 24
#: 8 Bit Gray Scale
MAP_EXPORT_BITS_GREY8 = 9
#: 8 Bit Color
MAP_EXPORT_BITS_8 = 8
#: 4 Bit Gray Scale
MAP_EXPORT_BITS_GREY4 = 5
#: 4 Bit Color
MAP_EXPORT_BITS_4 = 4
#: 1 Bit Gray Scale
MAP_EXPORT_BITS_GREY1 = 1
#: Default Resolution
MAP_EXPORT_BITS_DEFAULT = 0

#
# MAP_EXPORT_FORMAT constants
#
# Export Formats
# Format   Description                  Type
# =======  ==========================   ====

#: "PLT"    Geosoft Plot (``*.plt``)         Plot
MAP_EXPORT_FORMAT_PLT = "PLT"
#: "`GXSHP <geosoft.gxapi.GXSHP>`"    ArcView Shapfile (``*.shp``)     Plot
MAP_EXPORT_FORMAT_SHP = "SHP"
#: "DXF12"  AutoCad12 (``*.dxf``)            Plot
MAP_EXPORT_FORMAT_DXF12 = "DXF12"
#: "DXF13"  AutoCad13 (``*.dxf``)            Plot
MAP_EXPORT_FORMAT_DXF13 = "DXF13"
#: "GTIFF"  GeoTIFF (``*.tif``),             Color Image
MAP_EXPORT_FORMAT_GTIFF = "GTIFF"
#: "MTIFF"  MapInfo TIFF (``*.tif``)         Color Image
MAP_EXPORT_FORMAT_MTIFF = "MTIFF"
#: "ATIFF"  ArcView TIFF (``*.tif``)         Color Image
MAP_EXPORT_FORMAT_ATIFF = "ATIFF"
#: "`GXGEO <geosoft.gxapi.GXGEO>`"    Geosoft COLOR grid (``*.grd``)   Color Image
MAP_EXPORT_FORMAT_GEO = "GEO"
#: "ERM"    ER Mapper RGB (``*.ers``)        Color Image
MAP_EXPORT_FORMAT_ERM = "ERM"
#: "KMZ"    Keyhole Markup (``*.kmz``)       Zipped XML/Image files
MAP_EXPORT_FORMAT_KMZ = "KMZ"

#
# MAP_EXPORT_METHOD constants
#
# Dithering Methods

#: Standard Dither
MAP_EXPORT_METHOD_STANDARD = 0
#: Error Diffusion Dither
MAP_EXPORT_METHOD_DIFFUSE = 1
#: No Dither
MAP_EXPORT_METHOD_NONE = 2

#
# MAP_EXPORT_RASTER_FORMAT constants
#
# Export Raster Formats
# .
# Format  Description                      Type           B/W  B/W  COL  B/W  COL  COL
# ======= ==========================       ===========    ===  ===  ===  ===  ===  ===

#: "EMF"   Enhanced Metafile (``*.emf``)        Plot
MAP_EXPORT_RASTER_FORMAT_EMF = "EMF"
#: "BMP"   Bitmap (``*.bmp``)                   Color Image     X    X    X    X    X    X
MAP_EXPORT_RASTER_FORMAT_BMP = "BMP"
#: "JPEGL" JPEG Low Quality (``*.jpg``)         Color Image                              X
MAP_EXPORT_RASTER_FORMAT_JPEGL = "JPEGL"
#: "JPEG" JPEG (``*.jpg``)                     Color Image                              X
MAP_EXPORT_RASTER_FORMAT_JPEG = "JPEG"
#: "JPEGH" JPEG High Quality (``*.jpg``)        Color Image                              X
MAP_EXPORT_RASTER_FORMAT_JPEGH = "JPEGH"
#: "GIF"   GIF (``*.gif``)                      Color Image     X    X    X    X    X
MAP_EXPORT_RASTER_FORMAT_GIF = "GIF"
#: "PCX"   PCX (``*.pcx``)                      Color Image     X    X    X    X    X    X
MAP_EXPORT_RASTER_FORMAT_PCX = "PCX"
#: "PNG"   PNG (``*.png``)                      Color Image     X    X    X    X    X    X
MAP_EXPORT_RASTER_FORMAT_PNG = "PNG"
#: "EPS"   Encasulated PostScript (``*.eps``)   Color Image                    X
MAP_EXPORT_RASTER_FORMAT_EPS = "EPS"
#: "TIFF"  TIFF (``*.tif``)                     Color Image     X    X    X    X    X    X
MAP_EXPORT_RASTER_FORMAT_TIFF = "TIFF"

#
# MAP_LIST_MODE constants
#
# Map List modes

#: All
MAP_LIST_MODE_ALL = 0
#: 3d
MAP_LIST_MODE_3D = 1
#: Not3d
MAP_LIST_MODE_NOT3D = 2

#
# MAP_OPEN constants
#
# Open Modes

#: Map writenew
MAP_WRITENEW = 1
#: Map writeold
MAP_WRITEOLD = 2	

#
# GXMAPL Constants
# 

	

#
# GXMAPTEMPLATE Constants
# 



#
# MAPTEMPLATE_OPEN constants
#
# Open Modes

#: Create new empty map template (will overwrite existing files)
MAPTEMPLATE_WRITENEW = 0
#: Create from existing template on disk
MAPTEMPLATE_EXIST = 1	

#
# GXMATH Constants
# 

	

#
# GXMESH Constants
# 



#
# ATTRIBUTE_DATA_TYPE constants
#
# Data Type of Attribute

#: DOUBLE
ATTRIBUTE_DOUBLE = 0
#: THEMATIC
ATTRIBUTE_THEMATIC = 1
#: VECTOR
ATTRIBUTE_VECTOR = 2

#
# ATTRIBUTE_TYPE constants
#
# Data Type of Attribute

#: Single Value Attribute
ATTRIBUTE_SINGLE = 0
#: Surface Sides Attribute
ATTRIBUTE_SURFACE_SIDES = 1
#: Vertices Attribute
ATTRIBUTE_VERTICES = 2
#: Faces Attribute
ATTRIBUTE_FACES = 3	

#
# GXMESHUTIL Constants
# 



#
# SURFACE_CLIP_MODE constants
#
# Surface Clip Mode

#: Output the surface item above clipper surface
SURFACE_CLIP_ABOVE = 0
#: Output the surface item below clipper surface
SURFACE_CLIP_BELOW = 1
#: Output the surface items both above & below the clipper surface
SURFACE_CLIP_BOTH = 2	

#
# GXMETA Constants
# 



#
# H_META_INVALID_TOKEN constants
#
# `GXMETA <geosoft.gxapi.GXMETA>` Invalid Token

#: H meta invalid token
H_META_INVALID_TOKEN = -1

#
# META_CORE_ATTRIB constants
#
# `GXMETA <geosoft.gxapi.GXMETA>` Core Attributes

#: Description of this class
META_CORE_ATTRIB_Class_Description = -300
#: Application that created this class
META_CORE_ATTRIB_Class_Application = -301
#: URL that defines this class
META_CORE_ATTRIB_Class_ReferenceURL = -302
#: Type of Class
META_CORE_ATTRIB_Class_Type = -303
#: Description of this type
META_CORE_ATTRIB_Type_Description = -304
#: URL that defines this type
META_CORE_ATTRIB_Type_ReferenceURL = -305
#: Fixed size of this type (in bytes)
META_CORE_ATTRIB_Type_FixedSize = -306
#: Byte order for this type
META_CORE_ATTRIB_Type_ByteOrder = -307
#: Minimum Value for this type
META_CORE_ATTRIB_Type_MinValue = -308
#: Maximum Value for this type
META_CORE_ATTRIB_Type_MaxValue = -309
#: Maximum Size in bytes for this type
META_CORE_ATTRIB_Type_MaxSize = -310
#: Object class that manages this type
META_CORE_ATTRIB_Type_ObjectClass = -311
#: Object creating function
META_CORE_ATTRIB_Type_hCreatS_Func = -312
#: Object serializationg function
META_CORE_ATTRIB_Type_sSerial_Func = -313
#: Enumeration Value
META_CORE_ATTRIB_Type_Enum_Value = -314
#: Is this attribute visible to the user
META_CORE_ATTRIB_Attrib_Visible = -315
#: Is this atttribute editable by the user
META_CORE_ATTRIB_Attrib_Editable = -316
#: The flat name of this attribute
META_CORE_ATTRIB_Attrib_FlatName = -317

#
# META_CORE_CLASS constants
#
# Meta Core Class Objects

#: All Classes are subordinate to this class
META_CORE_CLASS_Base = -100
#: All Predefined symbols are in this class
META_CORE_CLASS_Predefined = -101
#: Attributes
META_CORE_CLASS_Attributes = -102
#: Classattributes
META_CORE_CLASS_ClassAttributes = -103
#: Typeattributes
META_CORE_CLASS_TypeAttributes = -104
#: Objectattributes
META_CORE_CLASS_ObjectAttributes = -105
#: Enumattributes
META_CORE_CLASS_EnumAttributes = -106
#: Attributeattributes
META_CORE_CLASS_AttributeAttributes = -107
#: Itemattributes
META_CORE_CLASS_ItemAttributes = -108
#: Types
META_CORE_CLASS_Types = -109
#: Enums
META_CORE_CLASS_Enums = -110
#: Enum bool
META_CORE_CLASS_Enum_Bool = -111
#: Enum classtype
META_CORE_CLASS_Enum_ClassType = -112

#
# META_CORE_TYPE constants
#
# `GXMETA <geosoft.gxapi.GXMETA>` Core Data Types

#: Data Bytes (Base type)
META_CORE_TYPE_Bytes = -200
#: Boolean
META_CORE_TYPE_Bool = -201
#: Signed character
META_CORE_TYPE_I1 = -202
#: Unsigned character
META_CORE_TYPE_U1 = -203
#: Signed short
META_CORE_TYPE_I2 = -204
#: Unsigned short
META_CORE_TYPE_U2 = -205
#: Signed long
META_CORE_TYPE_I4 = -206
#: Unsigned long
META_CORE_TYPE_U4 = -207
#: Singed long long (64 bit int)
META_CORE_TYPE_I8 = -208
#: Unsigned long long
META_CORE_TYPE_U8 = -209
#: Float (32bit)
META_CORE_TYPE_R4 = -210
#: Double (64bit)
META_CORE_TYPE_R8 = -211
#: String
META_CORE_TYPE_String = -212
#: Predefined Object (`GXITR <geosoft.gxapi.GXITR>`,`GXIPJ <geosoft.gxapi.GXIPJ>`)
META_CORE_TYPE_Object = -213
#: Enumeration
META_CORE_TYPE_Enum = -214
#: Classtype
META_CORE_TYPE_ClassType = -215	

#
# GXMPLY Constants
# 

	

#
# GXMULTIGRID3D Constants
# 



#
# DIRECTION3D constants
#
# Direction in 3D

#: XYZ
DIRECTION3D_XYZ = 0
#: YXZ
DIRECTION3D_YXZ = 1
#: XZY
DIRECTION3D_XZY = 2
#: YZX
DIRECTION3D_YZX = 3
#: ZXY
DIRECTION3D_ZXY = 4
#: ZYX
DIRECTION3D_ZYX = 5

#
# GOCAD_ORIENTATION constants
#
# GOCAD Orientations

#: Normal
GOCAD_ORIENTATIONS_NORMAL = 0
#: Inverted (Z)
GOCAD_ORIENTATIONS_INVERTED = 1
#: Normal (ZFirst)
GOCAD_ORIENTATIONS_NORMAL_ZFIRST = 2
#: Inverted (Z) (ZFirst)
GOCAD_ORIENTATIONS_INVERTED_ZFIRST = 3

#
# VECTOR_IMPORT constants
#
# Vector grid3d import direction

#: X, Y and Z
VECTOR_IMPORT_XYZ = 0
#: U, V and W
VECTOR_IMPORT_UVW = 1
#: Amplitude, Inclination and Declination
VECTOR_IMPORT_AID = 2

#
# FILTER3D constants
#
# Voxel filter type

#: Specify a file containing the 27-point filter
FILTER3D_FILE = 0
#: Smoothing filter
FILTER3D_SMOOTHING = 1
#: Laplace filter
FILTER3D_LAPLACE = 2
#: X-Gradient filter
FILTER3D_X_GRADIENT = 3
#: Y-Gradient filter
FILTER3D_Y_GRADIENT = 4
#: Z-Gradient filter
FILTER3D_Z_GRADIENT = 5
#: Total-Gradient filter
FILTER3D_TOTAL_GRADIENT = 6

#
# MULTIGRID3D_DIRECTGRID_METHOD constants
#
# How to calculate the cell values for direct gridding.

#: Select the minimum value found in each cell
MULTIGRID3D_DIRECTGRID_MINIMUM = 0
#: Select the maximum value found in each cell
MULTIGRID3D_DIRECTGRID_MAXIMUM = 1
#: Select the mean of all values found in each cell
MULTIGRID3D_DIRECTGRID_MEAN = 2
#: The number of valid (non-dummy) items found in each cell - 0 if no items found
MULTIGRID3D_DIRECTGRID_ITEMS = 3
#: The number of valid (non-dummy) items found in each cell - DUMMY if no items found
MULTIGRID3D_DIRECTGRID_DUMMYITEMS = 4	

#
# GXMULTIGRID3DUTIL Constants
# 



#
# RBFKERNEL constants
#
# Math kernel to use in the RBF Computation

#: Distance
RBFKERNEL_DISTANCE = 0
#: Multiquadratic
RBFKERNEL_MULTIQUADRATIC = 1	

#
# GXMVIEW Constants
# 



#
# MAKER constants
#
# Maker defines

#: GX
MAKER_GX = 0

#
# MVIEW_CLIP constants
#
# Boolean clipping defines

#: Turn ON clipping
CLIP_ON = 1
#: Turn OFF clipping
CLIP_OFF = 0

#
# MVIEW_COLOR constants
#
# 24-bit color defines
# The `color <geosoft.gxapi.GXMVIEW.color>` function can be used to create a color int from a
# color string description.
# The iColorXXX_MVIEW macros can be used to create colors from component
# intensities.

#: Black
C_BLACK = 33554432
#: Red
C_RED = 33554687
#: Green
C_GREEN = 33619712
#: Blue
C_BLUE = 50266112
#: Cyan
C_CYAN = 50331903
#: Magenta
C_MAGENTA = 50396928
#: Yellow
C_YELLOW = 67043328
#: Grey
C_GREY = 41975936
#: Light Red
C_LT_RED = 54542336
#: Light Green
C_LT_GREEN = 54526016
#: Light Blue
C_LT_BLUE = 50348096
#: Light Cyan
C_LT_CYAN = 50331712
#: Light Magenta
C_LT_MAGENTA = 50348032
#: Light Yellow
C_LT_YELLOW = 54525952
#: Light Grey
C_LT_GREY = 54542400
#: Grey 10%
C_GREY10 = 51910680
#: Grey 25%
C_GREY25 = 54542400
#: Grey 50%
C_GREY50 = 41975936
#: White
C_WHITE = 50331648
#: Transparent or no-draw
C_TRANSPARENT = 0

#
# MVIEW_CYLINDER3D constants
#
# What parts of the cylinder are closed

#: Open
MVIEW_CYLINDER3D_OPEN = 0
#: Closestart
MVIEW_CYLINDER3D_CLOSESTART = 1
#: Closeend
MVIEW_CYLINDER3D_CLOSEEND = 2
#: Closeall
MVIEW_CYLINDER3D_CLOSEALL = 3

#
# MVIEW_DRAW constants
#
# Polygon drawing defines

#: Draw Polylines
MVIEW_DRAW_POLYLINE = 0
#: Draw Polygons
MVIEW_DRAW_POLYGON = 1

#
# MVIEW_DRAWOBJ3D_ENTITY constants
#
# What types of entities to draw

#: Draw 3D Points (no normals) [1 verticies per object]
MVIEW_DRAWOBJ3D_ENTITY_POINTS = 0
#: Draw 3D Lines (no normals) [2 verticies per object]
MVIEW_DRAWOBJ3D_ENTITY_LINES = 1
#: Draw 3D Line strip (no normals) [2+x verticies per object]
MVIEW_DRAWOBJ3D_ENTITY_LINE_STRIPS = 2
#: Draw 3D Line loop (no normals, closes loop with first point) [2+x verticies per object]
MVIEW_DRAWOBJ3D_ENTITY_LINE_LOOPS = 3
#: Draw 3D Triangles [3 verticies per object]
MVIEW_DRAWOBJ3D_ENTITY_TRIANGLES = 4
#: Draw 3D Triangle strips [3+x verticies per object]
MVIEW_DRAWOBJ3D_ENTITY_TRIANGLE_STRIPS = 5
#: Draw 3D Triangle fans [3+x verticies per object]
MVIEW_DRAWOBJ3D_ENTITY_TRIANGLE_FANS = 6
#: Draw 3D Quads (Must be in the same plane) [4 verticies per object]
MVIEW_DRAWOBJ3D_ENTITY_QUADS = 7
#: Draw 3D Quad Strips (Must be in the same plane) [4+2x verticies per object]
MVIEW_DRAWOBJ3D_ENTITY_QUADS_STRIPS = 8
#: Draw 3D Quad Polygones (Must be in the same plane, must be convex and cannot intersect itself)
MVIEW_DRAWOBJ3D_ENTITY_POLYGONS = 9

#
# MVIEW_DRAWOBJ3D_MODE constants
#
# What types of entities to draw

#: Draw flat shaded faces (one normal and color per object)
MVIEW_DRAWOBJ3D_MODE_FLAT = 0
#: Draw smooth shaded faces (one normal and color per vertex)
MVIEW_DRAWOBJ3D_MODE_SMOOTH = 1

#
# MVIEW_EXTENT constants
#
# Types of extents defines

#: All objects
MVIEW_EXTENT_ALL = 0
#: Clipping regions
MVIEW_EXTENT_CLIP = 1
#: Map extents
MVIEW_EXTENT_MAP = 2
#: Visible objects
MVIEW_EXTENT_VISIBLE = 3

#
# MVIEW_FIT constants
#
# Fit area defines

#: Fit it to the map area
MVIEW_FIT_MAP = 0
#: Fit it to the view area
MVIEW_FIT_VIEW = 1

#
# MVIEW_FONT_WEIGHT constants
#
# Font weight defines

#: Normal
MVIEW_FONT_WEIGHT_NORMAL = 0
#: Ultralight
MVIEW_FONT_WEIGHT_ULTRALIGHT = 1
#: Light
MVIEW_FONT_WEIGHT_LIGHT = 2
#: Medium
MVIEW_FONT_WEIGHT_MEDIUM = 3
#: Bold
MVIEW_FONT_WEIGHT_BOLD = 4
#: Xbold
MVIEW_FONT_WEIGHT_XBOLD = 5
#: Xxbold
MVIEW_FONT_WEIGHT_XXBOLD = 6

#
# MVIEW_GRID constants
#
# Grid Drawing defines

#: Dot
MVIEW_GRID_DOT = 0
#: Line
MVIEW_GRID_LINE = 1
#: Cross
MVIEW_GRID_CROSS = 2

#
# MVIEW_GROUP constants
#
# Open Group defines

#: New Group (destroy any existing group)
MVIEW_GROUP_NEW = 1
#: Append to an existing Group
MVIEW_GROUP_APPEND = 0

#
# MVIEW_GROUP_LIST constants
#
# What groups to list

#: All the groups.
MVIEW_GROUP_LIST_ALL = 0
#: Those groups marked using the various mark functions.
MVIEW_GROUP_LIST_MARKED = 1
#: Those groups checked as visible in the view/group manager.
MVIEW_GROUP_LIST_VISIBLE = 2

#
# MVIEW_HIDE constants
#
# Boolean hidding defines

#: Turn ON hidding
HIDE_ON = 1
#: Turn OFF hidding
HIDE_OFF = 0

#
# MVIEW_IS constants
#
# Defines for mview types

#: Agg
MVIEW_IS_AGG = 0
#: Movable
MVIEW_IS_MOVABLE = 3
#: Csymb
MVIEW_IS_CSYMB = 4
#: Linked
MVIEW_IS_LINKED = 5
#: Made
MVIEW_IS_MADE = 6
#: Hidden
MVIEW_IS_HIDDEN = 7
#: Clipped
MVIEW_IS_CLIPPED = 8
#: Meta
MVIEW_IS_META = 9
#: Voxd
MVIEW_IS_VOXD = 10
#: Shadow 2d interpretation
MVIEW_IS_SHADOW_2D_INTERPRETATION = 11
#: Vector3d
MVIEW_IS_VECTOR3D = 12

#
# MVIEW_LABEL_BOUND constants
#
# Label Binding Defines

#: Label Not Bound
MVIEW_LABEL_BOUND_NO = 0
#: Label Bound
MVIEW_LABEL_BOUND_YES = 1

#
# MVIEW_LABEL_JUST constants
#
# Label Justification Defines

#: Top
MVIEW_LABEL_JUST_TOP = 0
#: Bottom
MVIEW_LABEL_JUST_BOTTOM = 1
#: Left
MVIEW_LABEL_JUST_LEFT = 2
#: Right
MVIEW_LABEL_JUST_RIGHT = 3

#
# MVIEW_LABEL_ORIENT constants
#
# Label Orientation Defines

#: Horizontal
MVIEW_LABEL_ORIENT_HORIZONTAL = 0
#: Top right
MVIEW_LABEL_ORIENT_TOP_RIGHT = 1
#: Top left
MVIEW_LABEL_ORIENT_TOP_LEFT = 2

#
# MVIEW_NAME_LENGTH constants
#
# Maximum length for view and group names

#: Maximum Length (1040)
MVIEW_NAME_LENGTH = 1040

#
# MVIEW_OPEN constants
#
# Open `GXMVIEW <geosoft.gxapi.GXMVIEW>` define

#: Read Only - No changes
MVIEW_READ = 0
#: Create new `GXMVIEW <geosoft.gxapi.GXMVIEW>` - destroys any existing `GXMVIEW <geosoft.gxapi.GXMVIEW>`
MVIEW_WRITENEW = 1
#: Open existing `GXMVIEW <geosoft.gxapi.GXMVIEW>` for read/write (must exist)
MVIEW_WRITEOLD = 2

#
# MVIEW_PJ constants
#
# Projection modes

#: No reprojection is used and all locations and
#: attributes are assumed to be in the view coordinate
#: system.
MVIEW_PJ_OFF = 0
#: Only locations will be transformed to the view
#: coordinate system.
MVIEW_PJ_LOCATION = 1
#: Locations and attributes (sizes, thicknesses, angles)
#: will be transformed to the view coordinate system.
MVIEW_PJ_ALL = 2
#: Mode before the last `MVIEW_PJ_OFF <geosoft.gxapi.MVIEW_PJ_OFF>`.
MVIEW_PJ_ON = 3

#
# MVIEW_RELOCATE constants
#
# Relocation Defines

#: Will fit the image to fill the specified area
MVIEW_RELOCATE_FIT = 0
#: Will maintain aspect ratio
MVIEW_RELOCATE_ASPECT = 1
#: Will maintain aspect ratio and center in specified area
MVIEW_RELOCATE_ASPECT_CENTER = 2

#
# MVIEW_SMOOTH constants
#
# Interpolation method to use for drawing line and polygon edges

#: Nearest neighbour
MVIEW_SMOOTH_NEAREST = 0
#: Cubic Spline
MVIEW_SMOOTH_CUBIC = 1
#: Akima
MVIEW_SMOOTH_AKIMA = 2

#
# MVIEW_TILE constants
#
# Tiling defines

#: Rectangular
MVIEW_TILE_RECTANGULAR = 0
#: Diagonal
MVIEW_TILE_DIAGONAL = 1
#: Triangular
MVIEW_TILE_TRIANGULAR = 2
#: Random
MVIEW_TILE_RANDOM = 3

#
# MVIEW_UNIT constants
#
# Coordinate systems defines

#: View coordinates
MVIEW_UNIT_VIEW = 0
#: Plot hi-metric (mm*100) on the map.
MVIEW_UNIT_PLOT = 1
#: Plot mm on the map.
MVIEW_UNIT_MM = 2
#: View coordinates without a warp if there is one
MVIEW_UNIT_VIEW_UNWARPED = 3

#
# MVIEW_EXTENT_UNIT constants
#
# Types of units for extents (these map to the
# :ref:`MVIEW_UNIT` defines directly)

#: `MVIEW_UNIT_VIEW <geosoft.gxapi.MVIEW_UNIT_VIEW>`
MVIEW_EXTENT_UNIT_VIEW = 0
#: `MVIEW_UNIT_PLOT <geosoft.gxapi.MVIEW_UNIT_PLOT>`
MVIEW_EXTENT_UNIT_PLOT = 1
#: `MVIEW_UNIT_MM <geosoft.gxapi.MVIEW_UNIT_MM>`
MVIEW_EXTENT_UNIT_MM = 2
#: `MVIEW_UNIT_VIEW_UNWARPED <geosoft.gxapi.MVIEW_UNIT_VIEW_UNWARPED>`
MVIEW_EXTENT_UNIT_VIEW_UNWARPED = 3

#
# TEXT_REF constants
#
# Text reference locations

#: Bottom left
TEXT_REF_BOTTOM_LEFT = 0
#: Bottom center
TEXT_REF_BOTTOM_CENTER = 1
#: Bottom right
TEXT_REF_BOTTOM_RIGHT = 2
#: Middle left
TEXT_REF_MIDDLE_LEFT = 3
#: Middle center
TEXT_REF_MIDDLE_CENTER = 4
#: Middle right
TEXT_REF_MIDDLE_RIGHT = 5
#: Top left
TEXT_REF_TOP_LEFT = 6
#: Top center
TEXT_REF_TOP_CENTER = 7
#: Top right
TEXT_REF_TOP_RIGHT = 8

#
# MVIEW_3D_RENDER constants
#
# 3D Geometry rendering defines. These flags only affect mixed geometry groups and not the data
# specific groups (e.g. voxels, vector voxels surfaces etc.). Each of those groups 
# has predefined optimum behaviour and any changes to these flags are ignored.

#: This flag is enabled if the backfaces of geometry should be rendered
MVIEW_3D_RENDER_BACKFACES = 1
#: If the exaggeration scales of the 3D view in X, Y and/or Z is set to anything other than 1.0
#: any geometric objects (spheres, cubes etc.) for 3D groups with the following flags 
#: will render untransformed while only the centers of the objects are changed.
#: This ensures the objects appear in the correct place with respect to other data being rendered (and scaled).
MVIEW_3D_DONT_SCALE_GEOMETRY = 2	

#
# GXMVU Constants
# 



#
# EMLAY_GEOMETRY constants
#
# Type of Geometry

#: 0
EMLAY_V_COPLANAR = 0
#: 1
EMLAY_H_COPLANAR = 1
#: 2
EMLAY_V_COAXIAL = 2

#
# ARROW_ALIGNMENT constants
#
# Direction of alignment

#: Horizontal
ARROW_ALIGNMENT_HORIZONTAL = 0
#: Vertical
ARROW_ALIGNMENT_VERTICAL = 1

#
# BARCHART_LABEL constants
#
# Place to draw bar labels

#: No label
BARCHART_LABEL_NO = 0
#: Label below X axis
BARCHART_LABEL_BELOWX = 1
#: Label above X axis
BARCHART_LABEL_ABOVEX = 2
#: Label at positive end of bar
BARCHART_LABEL_PEND = 3
#: Label at negative end of bar
BARCHART_LABEL_NEND = 4
#: Label at alternative ends,1st label at positive end
BARCHART_LABEL_ALTERNAT1 = 5
#: Label at alternative ends,1st label at negative end
BARCHART_LABEL_ALTERNAT2 = 6

#
# COLORBAR_LABEL constants
#
# Label text orientation

#: (default)
COLORBAR_LABEL_HORIZONTAL = 0
#: Gives text an orientation of -90 degrees
COLORBAR_LABEL_VERTICAL = 1

#
# COLORBAR_STYLE constants
#
# Label text orientation

#: Don't draw
COLORBAR_STYLE_NONE = 0
#: Post max/min values
COLORBAR_STYLE_MAXMIN = 1

#
# MVU_ORIENTATION constants
#
# Orientation (of whatever)

#: Vertical
MVU_ORIENTATION_VERTICAL = 0
#: Horizontal
MVU_ORIENTATION_HORIZONTAL = 1

#
# MVU_DIVISION_STYLE constants
#
# Orientation (of whatever)

#: No division marks
MVU_DIVISION_STYLE_NONE = 0
#: Division line
MVU_DIVISION_STYLE_LINES = 1
#: Inside tics, both sides
MVU_DIVISION_STYLE_TICS = 2

#
# MVU_ARROW constants
#
# Type Arrow. These definitions are used as binary flags, and can be
# used together by passing sums.

#: Plot the head as a solid triangle, otherwise plot a "stick arrow"
#: with three lines for the tail and two barbs.
MVU_ARROW_SOLID = 1
#: If used, input the actual length of the barbs on the arrow, in
#: view X-axis units, as measured along the tail. If not used, enter the ratio
#: between the length of the barbs and full length of the arrow (e.g. 0.4).
#: In the latter case, the longer the arrow, the bigger the arrow head.
MVU_ARROW_FIXED = 2

#
# MVU_FLIGHT_COMPASS constants
#
# Compass direction

#: None
MVU_FLIGHT_COMPASS_NONE = -1
#: East
MVU_FLIGHT_COMPASS_EAST = 0
#: North
MVU_FLIGHT_COMPASS_NORTH = 1
#: West
MVU_FLIGHT_COMPASS_WEST = 2
#: South
MVU_FLIGHT_COMPASS_SOUTH = 3

#
# MVU_FLIGHT_DUMMIES constants
#
# Show Dummies

#: Notincluded
MVU_FLIGHT_DUMMIES_NOTINCLUDED = 0
#: Included
MVU_FLIGHT_DUMMIES_INCLUDED = 1

#
# MVU_FLIGHT_LOCATE constants
#
# Line label locations

#: No label
MVU_FLIGHT_LOCATE_NONE = 0
#: ::
#: 
#:     L100.2 -------------------------- L100.2
#: 
#: dOffA controls distance from label to line.
#: dOffB controls vertical offset from center.
MVU_FLIGHT_LOCATE_END = 1
#: ::
#: 
#:     L100.2                            L100.2
#:     ----------------------------------------
#: 
#: dOffA controls label distance above the line.
#: dOffB controls offset in from line end.
MVU_FLIGHT_LOCATE_ABOVE = 2
#: ::
#: 
#:     ----------------------------------------
#:     L100.2                            L100.2
#: 
#: dOffA controls label distance below the line.
#: dOffB controls offset in from line end.
MVU_FLIGHT_LOCATE_BELOW = 3
#: To add '>' to label to indicate direction, for example:
#: `MVU_FLIGHT_LOCATE_END <geosoft.gxapi.MVU_FLIGHT_LOCATE_END>`+`MVU_FLIGHT_DIRECTION <geosoft.gxapi.MVU_FLIGHT_DIRECTION>`
MVU_FLIGHT_DIRECTION = 8

#
# MVU_VOX_SURFACE_METHOD constants
#
# TODO

#: Marching cubes
MVU_VOX_SURFACE_METHOD_MARCHING_CUBES = 0

#
# MVU_VOX_SURFACE_OPTION constants
#
# TODO

#: Open
MVU_VOX_SURFACE_OPTION_OPEN = 0
#: Closed
MVU_VOX_SURFACE_OPTION_CLOSED = 1

#
# MVU_TEXTBOX constants
#
# Type of Box

#: Left
MVU_TEXTBOX_LEFT = 0
#: Center
MVU_TEXTBOX_CENTER = 1
#: Right
MVU_TEXTBOX_RIGHT = 2

#
# MVU_VPOINT constants
#
# Head Acuteness

#: Sharp
MVU_VPOINT_SHARP = 0
#: Medium
MVU_VPOINT_MEDIUM = 1
#: Blunt
MVU_VPOINT_BLUNT = 2

#
# MVU_VPOS constants
#
# Head Position

#: Head
MVU_VPOS_HEAD = 0
#: Middle
MVU_VPOS_MIDDLE = 1
#: Tail
MVU_VPOS_TAIL = 2

#
# MVU_VSIZE constants
#
# Head Size

#: Nohead
MVU_VSIZE_NOHEAD = 0
#: Smallhead
MVU_VSIZE_SMALLHEAD = 1
#: Mediumhead
MVU_VSIZE_MEDIUMHEAD = 2
#: Largehead
MVU_VSIZE_LARGEHEAD = 3
#: Notail
MVU_VSIZE_NOTAIL = 4

#
# MVU_VSTYLE constants
#
# Head Style

#: Lines
MVU_VSTYLE_LINES = 0
#: Barb
MVU_VSTYLE_BARB = 1
#: Triangle
MVU_VSTYLE_TRIANGLE = 2	

#
# GXMXD Constants
# 

	

#
# GXPAT Constants
# 

	

#
# GXPG Constants
# 



#
# PG_3D_DIR constants
#
# 3D Pager direction

#: Xyz
PG_3D_DIR_XYZ = 0
#: Yxz
PG_3D_DIR_YXZ = 1
#: Xzy
PG_3D_DIR_XZY = 2
#: Yzx
PG_3D_DIR_YZX = 3
#: Zxy
PG_3D_DIR_ZXY = 4
#: Zyx
PG_3D_DIR_ZYX = 5

#
# PG_BF_CONV constants
#
# Pager binary conversions

#: The Data is in Raw form
PG_BF_CONV_NONE = 0
#: The data needs to be byte swapped
PG_BF_CONV_SWAP = 1	

#
# GXPJ Constants
# 



#
# PJ_ELEVATION constants
#
# Elevation correction method

#: Elevation transform not supported.
PJ_ELEVATION_NONE = 0
#: elevation transformation uses earth-centre shift
#: and is not accurate.
PJ_ELEVATION_GEOCENTRIC = 1
#: elevation transformation uses a geoid model
#: and is as accurate as the geoid data.
PJ_ELEVATION_GEOID = 2

#
# PJ_RECT constants
#
# Conversion direction

#: Xy2ll
PJ_RECT_XY2LL = 0
#: Ll2xy
PJ_RECT_LL2XY = 1	

#
# GXPLY Constants
# 



#
# PLY_CLIP constants
#
# Polygon clipping mode

#: The polygons do not intersect
PLY_CLIP_NO_INTERSECT = 0
#: The polygons do intersect
PLY_CLIP_INTERSECT = 1
#: Polygon A is completely inside polygon B
PLY_CLIP_A_IN_B = 2
#: Polygon B is completely inside polygon A
PLY_CLIP_B_IN_A = 3

#
# PLY_POINT_CLIP constants
#
# Polygon point clipping mode

#: The point is inside the polygon
PLY_POINT_CLIP_INSIDE = 0
#: The point is outside the polygon
PLY_POINT_CLIP_OUTSIDE = 1
#: An error occurred
PLY_POINT_CLIP_ERROR = 2

#
# PLY_LINE_CLIP constants
#
# Polygon line clip indicator

#: The start point of the line is inside
PLY_LINE_CLIP_INSIDE = 0
#: This name is a misnomer - it should have been `PLY_LINE_CLIP_INSIDE <geosoft.gxapi.PLY_LINE_CLIP_INSIDE>`, but is retained to support legacy code
PLY_LINE_CLIP_NO_INTERSECT = 0
#: The start point of the line is outside
PLY_LINE_CLIP_OUTSIDE = 1
#: Error
PLY_LINE_CLIP_ERROR = 2	

#
# GXRA Constants
# 

	

#
# GXREG Constants
# 



#
# REG_MERGE constants
#
# `GXREG <geosoft.gxapi.GXREG>` merge options

#: Replace Values
REG_MERGE_REPLACE = 0
#: Only append values
REG_MERGE_ADD = 1	

#
# GXSBF Constants
# 



#
# SBF_OPEN constants
#
# `GXSBF <geosoft.gxapi.GXSBF>` Open defines

#: Read only
SBF_READ = 0
#: Read/write - erases structured file
SBF_READWRITE_NEW = 1
#: Read/write - open and append onto pre-existing structured file
SBF_READWRITE_OLD = 2

#
# SBF_TYPE constants
#
# `GXSBF <geosoft.gxapi.GXSBF>` Object type defines

#: Embedded directory names
SBF_TYPE_DIRS = 1
#: Embedded file names
SBF_TYPE_FILES = 2
#: Embedded file and directory names
SBF_TYPE_BOTH = 3	

#
# GXSEGYREADER Constants
# 

	

#
# GXST Constants
# 



#
# ST_INFO constants
#
# Information to retrieve

#: Number of non-dummy items
ST_ITEMS = 0
#: Number of items greater than zero
ST_NPOS = 1
#: Number of items equal to zero
ST_NZERO = 22
#: St dummies
ST_DUMMIES = 2
#: St min
ST_MIN = 3
#: St max
ST_MAX = 4
#: St range
ST_RANGE = 5
#: St mean
ST_MEAN = 6
#: St median
ST_MEDIAN = 7
#: St mode
ST_MODE = 8
#: St geomean
ST_GEOMEAN = 9
#: St variance
ST_VARIANCE = 10
#: St stddev
ST_STDDEV = 11
#: St stderr
ST_STDERR = 12
#: St skew
ST_SKEW = 13
#: St kurtosis
ST_KURTOSIS = 14
#: St base
ST_BASE = 15
#: Sums and sums of powers
ST_SUM = 16
#: St sum2
ST_SUM2 = 17
#: St sum3
ST_SUM3 = 18
#: St sum4
ST_SUM4 = 19
#: Smallest value greater than zero.
ST_MINPOS = 21
#: St hist maxcount
ST_HIST_MAXCOUNT = 100	

#
# GXST2 Constants
# 



#
# ST2_CORRELATION constants
#
# Correlation style

#: Simple correlation
ST2_CORR = 0
#: Pearson's correlation (normalized to standard deviations)
ST2_PCORR = 1	

#
# GXSTORAGEPROJECT Constants
# 

	

#
# GXSTR Constants
# 



#
# FILE_EXT constants
#
# Extension option

#: Will add the extension only if no extension is present.
FILE_EXT_ADD_IF_NONE = 0
#: Will cause a renaming of the file extension to the new extension.
FILE_EXT_FORCE = 1

#
# STR_CASE constants
#
# Case sensitivity

#: Tolerant
STR_CASE_TOLERANT = 0
#: Sensitive
STR_CASE_SENSITIVE = 1

#
# STR_ESCAPE constants
#
# How to handle escape

#: Converts non-standard characters in a string to escape sequences.
ESCAPE_CONVERT = 0
#: Replaces escape sequences with original characters.
ESCAPE_REPLACE = 1

#
# STR_FILE_PART constants
#
# Parts of a path string

#: File Name
STR_FILE_PART_NAME = 0
#: Extension
STR_FILE_PART_EXTENSION = 1
#: Directory
STR_FILE_PART_DIRECTORY = 2
#: Drive
STR_FILE_PART_VOLUME = 3
#: Qualifiers
STR_FILE_PART_QUALIFIERS = 4
#: Name and the Extension together
STR_FILE_PART_NAME_EXTENSION = 5
#: Full name of file with no qualifiers
STR_FILE_PART_FULLPATH_NO_QUALIFIERS = 6

#
# STR_JUSTIFY constants
#
# String justification style

#: Left
STR_JUSTIFY_LEFT = 0
#: Center
STR_JUSTIFY_CENTER = 1
#: Right
STR_JUSTIFY_RIGHT = 2

#
# STR_TRIM constants
#
# What to trim

#: Str trimright
STR_TRIMRIGHT = 1
#: Str trimleft
STR_TRIMLEFT = 2
#: Str trimboth
STR_TRIMBOTH = 3	

#
# GXSURFACE Constants
# 



#
# SURFACE_OPEN constants
#
# Open Modes

#: Read
SURFACE_OPEN_READ = 0
#: Readwrite
SURFACE_OPEN_READWRITE = 1	

#
# GXSURFACEITEM Constants
# 



#
# SURFACERENDER_MODE constants
#
# Open Modes

#: Surfacerender smooth
SURFACERENDER_SMOOTH = 0
#: Surfacerender fill
SURFACERENDER_FILL = 1
#: Surfacerender edges
SURFACERENDER_EDGES = 2	

#
# GXSYS Constants
# 



#
# ARC_LICENSE constants
#
# ArcGIS platform types

#: The Engine or any qualifying ArcGIS product is missing
ARC_LICENSE_ENGINENOTPRESENT = 0
#: Desktop Engine
ARC_LICENSE_DESKTOPENGINE = 1
#: ArcView
ARC_LICENSE_ARCVIEW = 2
#: ArcEditor
ARC_LICENSE_ARCEDITOR = 3
#: ArcInfo
ARC_LICENSE_ARCINFO = 4
#: ArcServer
ARC_LICENSE_ARCSERVER = 5

#
# GEO_DIRECTORY constants
#
# Geosoft directory defines

#: None
GEO_DIRECTORY_NONE = 0
#: Geosoft\\
GEO_DIRECTORY_GEOSOFT = 1
#: Geosoft\\bin
GEO_DIRECTORY_BIN = 2
#: Geosoft\\ger
GEO_DIRECTORY_GER = 3
#: Geosoft\\omn
GEO_DIRECTORY_OMN = 4
#: Geosoft\\tbl
GEO_DIRECTORY_TBL = 5
#: Geosoft\\fonts
GEO_DIRECTORY_FONTS = 6
#: Geosoft\\gx
GEO_DIRECTORY_GX = 7
#: Geosoft\\gs
GEO_DIRECTORY_GS = 8
#: Geosoft\\apps
GEO_DIRECTORY_APPS = 9
#: Geosoft\\user\\etc and then Geosoft\\etc
GEO_DIRECTORY_ETC = 10
#: Geosoft\\hlp
GEO_DIRECTORY_HLP = 11
#: Geosoft\\user\\csv
GEO_DIRECTORY_USER_CSV = 14
#: Geosoft\\user\\lic
GEO_DIRECTORY_USER_LIC = 15
#: Geosoft\\user\\ini
GEO_DIRECTORY_USER_INI = 16
#: Geosoft\\temp (or where the user put it)
GEO_DIRECTORY_USER_TEMP = 17
#: Geosoft\\user\\etc
GEO_DIRECTORY_USER_ETC = 18
#: Geosoft\\img
GEO_DIRECTORY_IMG = 19
#: Geosoft\\bar
GEO_DIRECTORY_BAR = 20
#: Geosoft\\maptemplate
GEO_DIRECTORY_MAPTEMPLATE = 22
#: Geosoft\\user\\maptemplate
GEO_DIRECTORY_USER_MAPTEMPLATE = 23
#: Geosoft\\pygx
GEO_DIRECTORY_PYGX = 24
#: Geosoft\\user\\pygx
GEO_DIRECTORY_USER_PYGX = 25
#: Geosoft\\user\\gx
GEO_DIRECTORY_USER_GX = 26

#
# REG_DOMAIN constants
#
# Registry key domains

#: Same as HKEY_LOCAL_MACHINE in Windows
REG_DOMAIN_MACHINE = 0
#: Same as HKEY_CURRENT_USER in Windows
REG_DOMAIN_USER = 1

#
# SHELL_EXECUTE constants
#
# Shell execute defines

#: Sw hide
SW_HIDE = 0
#: Sw shownormal
SW_SHOWNORMAL = 1
#: Sw showminimized
SW_SHOWMINIMIZED = 2
#: Sw showmaximized
SW_SHOWMAXIMIZED = 3
#: Sw shownoactivate
SW_SHOWNOACTIVATE = 4
#: Sw show
SW_SHOW = 5
#: Sw minimize
SW_MINIMIZE = 6
#: Sw showminnoactive
SW_SHOWMINNOACTIVE = 7
#: Sw showna
SW_SHOWNA = 8
#: Sw restore
SW_RESTORE = 9
#: Sw showdefault
SW_SHOWDEFAULT = 10
#: Sw forceminimize
SW_FORCEMINIMIZE = 11

#
# SYS_DIR constants
#
# `GXSYS <geosoft.gxapi.GXSYS>` Directory locations

#: Is the workspace working directory
SYS_DIR_LOCAL = 0
#: Is the geosoft installation directory (read-only)
SYS_DIR_GEOSOFT = 1
#: is the geosoft installation directory that
#: contains user read/write files.
SYS_DIR_USER = 2
#: Geosoft Temp folder
SYS_DIR_GEOTEMP = 3
#: Windows folder
SYS_DIR_WINDOWS = 4
#: Windows SYSTEM folder
SYS_DIR_SYSTEM = 5
#: Where the license file is stored
SYS_DIR_LICENSE = 6
#: User RESOURCEFILES Folder
SYS_DIR_RESOURCEFILES = 7
#: BAR folder
SYS_DIR_GEOSOFT_BAR = 100
#: BIN folder
SYS_DIR_GEOSOFT_BIN = 101
#: CSV folder
SYS_DIR_GEOSOFT_CSV = 102
#: CSV ALIASES folder
SYS_DIR_GEOSOFT_CSV_ALIASES = 103
#: DATA folder
SYS_DIR_GEOSOFT_DATA = 104
#: DBG folder
SYS_DIR_GEOSOFT_DBG = 105
#: Encrypted Files folder
SYS_DIR_GEOSOFT_ENCRYPTEDFILES = 106
#: ETC folder
SYS_DIR_GEOSOFT_ETC = 107
#: FONTS folder
SYS_DIR_GEOSOFT_FONTS = 108
#: `GXGER <geosoft.gxapi.GXGER>` folder
SYS_DIR_GEOSOFT_GER = 109
#: GS folder
SYS_DIR_GEOSOFT_GS = 110
#: GX folder
SYS_DIR_GEOSOFT_GX = 111
#: HLP folder
SYS_DIR_GEOSOFT_HLP = 112
#: `GXIMG <geosoft.gxapi.GXIMG>` folder
SYS_DIR_GEOSOFT_IMG = 113
#: INI folder
SYS_DIR_GEOSOFT_INI = 114
#: `GXMAPTEMPLATE <geosoft.gxapi.GXMAPTEMPLATE>` folder
SYS_DIR_GEOSOFT_MAPTEMPLATE = 115
#: OMN folder
SYS_DIR_GEOSOFT_OMN = 116
#: PAGE folder
SYS_DIR_GEOSOFT_PAGE = 117
#: SCHEMA folder
SYS_DIR_GEOSOFT_SCHEMA = 118
#: SPEC INI older
SYS_DIR_GEOSOFT_SPEC_INI = 119
#: STYLE SHEETS folder
SYS_DIR_GEOSOFT_STYLESHEETS = 120
#: TBL folder
SYS_DIR_GEOSOFT_TBL = 121
#: User CSV Folder
SYS_DIR_USER_CSV = 200
#: User ETC Folder
SYS_DIR_USER_ETC = 201
#: User GS Folder
SYS_DIR_USER_GS = 202
#: User HLP Folder
SYS_DIR_USER_HLP = 203
#: User INI Folder
SYS_DIR_USER_INI = 204
#: User LIC Folder
SYS_DIR_USER_LIC = 205
#: User `GXMAPTEMPLATE <geosoft.gxapi.GXMAPTEMPLATE>` Folder
SYS_DIR_USER_MAPTEMPLATE = 206
#: User OMN Folder
SYS_DIR_USER_OMN = 207
#: User BAR Folder
SYS_DIR_USER_BAR = 214
#: User `GXIMG <geosoft.gxapi.GXIMG>` Folder
SYS_DIR_USER_IMG = 215
#: User STACKS Folder
SYS_DIR_USER_STACKS = 209
#: User TEMP Folder
SYS_DIR_USER_TEMP = 210
#: User SERVICES Folder
SYS_DIR_USER_SERVICES = 211
#: User STYLESHEETS Folder
SYS_DIR_USER_STYLESHEETS = 212

#
# SYS_FONT constants
#
# Font types

#: Geosoft GFN fonts.
SYS_FONT_GFN = 1
#: Available TrueType fonts
SYS_FONT_TT = 0

#
# SYS_INFO constants
#
# System information

#: Version major
SYS_INFO_VERSION_MAJOR = 0
#: Version minor
SYS_INFO_VERSION_MINOR = 1
#: Version sp
SYS_INFO_VERSION_SP = 2
#: Build number
SYS_INFO_BUILD_NUMBER = 3
#: Build label
SYS_INFO_BUILD_LABEL = 4
#: Version label
SYS_INFO_VERSION_LABEL = 5
#: Productname
SYS_INFO_PRODUCTNAME = 6
#: Servername
SYS_INFO_SERVERNAME = 7
#: Legalcopyright
SYS_INFO_LEGALCOPYRIGHT = 8
#: Registry
SYS_INFO_REGISTRY = 9
#: Registry environment
SYS_INFO_REGISTRY_ENVIRONMENT = 10
#: Registry support
SYS_INFO_REGISTRY_SUPPORT = 11
#: Registry interapp
SYS_INFO_REGISTRY_INTERAPP = 12
#: Ois registry
SYS_INFO_OIS_REGISTRY = 13
#: Test registry
SYS_INFO_TEST_REGISTRY = 14

#
# SYS_LINEAGE_SOURCE constants
#
# Type of lineage sources

#: Map
SYS_LINEAGE_SOURCE_MAP = 0
#: Mxd
SYS_LINEAGE_SOURCE_MXD = 1
#: Db
SYS_LINEAGE_SOURCE_DB = 2
#: Maptemplate
SYS_LINEAGE_SOURCE_MAPTEMPLATE = 3
#: Grid
SYS_LINEAGE_SOURCE_GRID = 4
#: Voxel
SYS_LINEAGE_SOURCE_VOXEL = 5

#
# SYS_MENU_CLEAR constants
#
# Font types

#: Clear all menus excluding the coremenus.omn
#: but including any default menus specified in the settings (these will not come back in this project).
SYS_MENU_CLEAR_ALL = 0
#: Clear all menus excluding the coremenus.omn
#: but reload any default menus specified in the settings (essentially this is a refresh
#: back to the default state again).
SYS_MENU_CLEAR_DEFAULT = 1

#
# SYS_PATH constants
#
# Get specific Geosoft paths. The path name will
# have a directory separator at the end.

#: Is the workspace working directory
SYS_PATH_LOCAL = 0
#: Is the geosoft installation directory (read-only)
SYS_PATH_GEOSOFT = 1
#: is the geosoft installation directory that
#: contains user read/write files.
SYS_PATH_GEOSOFT_USER = 2
#: Geosoft Temp folder
SYS_PATH_GEOTEMP = 3
#: Windows folder
SYS_PATH_WINDOWS = 4
#: System folder
SYS_PATH_SYSTEM = 5
#: Where the license file is stored
SYS_PATH_LICENSE = 6
#: User RESOURCEFILES Folder
SYS_PATH_RESOURCEFILES = 7
#: BAR folder
SYS_PATH_GEOSOFT_BAR = 100
#: BIN folder
SYS_PATH_GEOSOFT_BIN = 101
#: CSV folder
SYS_PATH_GEOSOFT_CSV = 102
#: CSV ALIASES folder
SYS_PATH_GEOSOFT_CSV_ALIASES = 103
#: DATA folder
SYS_PATH_GEOSOFT_DATA = 104
#: DBG folder
SYS_PATH_GEOSOFT_DBG = 105
#: Encrypted Files folder
SYS_PATH_GEOSOFT_ENCRYPTEDFILES = 106
#: ETC folder
SYS_PATH_GEOSOFT_ETC = 107
#: FONTS folder
SYS_PATH_GEOSOFT_FONTS = 108
#: `GXGER <geosoft.gxapi.GXGER>` folder
SYS_PATH_GEOSOFT_GER = 109
#: GS folder
SYS_PATH_GEOSOFT_GS = 110
#: PYGX folder
SYS_PATH_GEOSOFT_PYGX = 126
#: GX folder
SYS_PATH_GEOSOFT_GX = 111
#: HLP folder
SYS_PATH_GEOSOFT_HLP = 112
#: `GXIMG <geosoft.gxapi.GXIMG>` folder
SYS_PATH_GEOSOFT_IMG = 113
#: INI folder
SYS_PATH_GEOSOFT_INI = 114
#: `GXMAPTEMPLATE <geosoft.gxapi.GXMAPTEMPLATE>` folder
SYS_PATH_GEOSOFT_MAPTEMPLATE = 115
#: OMN folder
SYS_PATH_GEOSOFT_OMN = 116
#: PAGE folder
SYS_PATH_GEOSOFT_PAGE = 117
#: SCHEMA folder
SYS_PATH_GEOSOFT_SCHEMA = 118
#: SPEC INI older
SYS_PATH_GEOSOFT_SPEC_INI = 119
#: STYLE SHEETS folder
SYS_PATH_GEOSOFT_STYLESHEETS = 120
#: TBL folder
SYS_PATH_GEOSOFT_TBL = 121
#: User CSV Folder
SYS_PATH_GEOSOFT_USER_CSV = 200
#: User ETC Folder
SYS_PATH_GEOSOFT_USER_ETC = 201
#: User GS Folder
SYS_PATH_GEOSOFT_USER_GS = 202
#: User GX Folder
SYS_PATH_GEOSOFT_USER_GX = 217
#: User PYGX Folder
SYS_PATH_GEOSOFT_USER_PYGX = 216
#: User HLP Folder
SYS_PATH_GEOSOFT_USER_HLP = 203
#: User INI Folder
SYS_PATH_GEOSOFT_USER_INI = 204
#: User LIC Folder
SYS_PATH_GEOSOFT_USER_LIC = 205
#: User `GXMAPTEMPLATE <geosoft.gxapi.GXMAPTEMPLATE>` Folder
SYS_PATH_GEOSOFT_USER_MAPTEMPLATE = 206
#: User OMN Folder
SYS_PATH_GEOSOFT_USER_OMN = 207
#: User STACKS Folder
SYS_PATH_GEOSOFT_USER_STACKS = 209
#: User TEMP Folder
SYS_PATH_GEOSOFT_USER_TEMP = 210
#: User SERVICES Folder
SYS_PATH_USER_SERVICES = 211
#: User STYLESHEETS Folder
SYS_PATH_USER_STYLESHEETS = 212

#
# SYS_RUN_DISPLAY constants
#
# Windows Display Options
# Determine how applications are started.
# These options are not yet implemented.

#: In a window  (default)
SYS_RUN_DISPLAY_WINDOW = 0
#: Maximized
SYS_RUN_DISPLAY_MINIMIZE = 8
#: Full Screen
SYS_RUN_DISPLAY_FULLSCREEN = 16

#
# SYS_RUN_HOLD constants
#
# DOS Console Options
# These options determine if and when the DOS/EXE
# console window is held. These options only work
# on DOS and EXE programs.

#: Don't wait (Default)
SYS_RUN_HOLD_NEVER = 0
#: Hold the screen if there is an error
SYS_RUN_HOLD_ONERROR = 512
#: Always hold the screen
SYS_RUN_HOLD_ALWAYS = 1024

#
# SYS_RUN_TYPE constants
#
# Type of application to run

#: Things such as .BAT files, copy commands, etc. (A console window is created)
SYS_RUN_TYPE_DOS = 1
#: Any program (.EXE) (a console window is created)
SYS_RUN_TYPE_EXE = 0
#: Windows applications that do not require a console window.
SYS_RUN_TYPE_WINDOWS = 2

#
# SYS_RUN_WIN constants
#
# Windows Options
# Should we wait for the application to
# finish or should we continue executing. If you wait
# for another program, Oasis montaj will not
# redraw or respond. We always wait for EXE and DOS programs.

#: Never wait (default)
SYS_RUN_WIN_NOWAIT = 0
#: Always wait
SYS_RUN_WIN_WAIT = 2048

#
# SYS_SEARCH_PATH constants
#
# Find File define

#: Local and then Geosoft directory
FIND_LOCAL_GEOSOFT = 0
#: Geosoft directory
FIND_GEOSOFT = 1
#: Local directory
FIND_LOCAL = 2
#: Make the name short (FLAG that is added on)
FIND_SHORT = 1024

#
# SYS_ENCRYPTION_KEY constants
#
# How to encrypt a string. Determines the portability of the encrypted string.

#: Encrypt string to currently signed-in user. The string can be decrypted
#: by the same user on any machine.
SYS_ENCRYPTION_KEY_GEOSOFT_ID = 0
#: Encrypt string to current machine. The string can be decrypted by any
#: user on the same machine.
SYS_ENCRYPTION_KEY_GLOBAL_ID = 1

#
# TD_ICON constants
#
# TaskDialog Icon

#: No icon.
TD_ICON_NONE = 0
#: An exclamation-point icon appears in the task dialog.
TD_ICON_WARNING = 1
#: A stop-sign icon appears in the task dialog.
TD_ICON_ERROR = 2
#: An icon consisting of a lowercase letter i in a circle appears in the task dialog.
TD_ICON_INFORMATION = 3
#: A shield icon appears in the task dialog.
TD_ICON_SUCCESS = 4
#: A shield icon appears in the task dialog.
TD_ICON_CONFIRMATION = 5

#
# TD_BUTTON constants
#
# TaskDialog Common Buttons

#: No common buttons.
TD_BUTTON_NONE = 1
#: Button results in `TD_ID_OK <geosoft.gxapi.TD_ID_OK>` return value.
TD_BUTTON_OK = 1
#: Button results in `TD_ID_YES <geosoft.gxapi.TD_ID_YES>` return value.
TD_BUTTON_YES = 2
#: Button results in `TD_ID_NO <geosoft.gxapi.TD_ID_NO>` return value.
TD_BUTTON_NO = 4
#: Button results in `TD_ID_CANCEL <geosoft.gxapi.TD_ID_CANCEL>` return value.
TD_BUTTON_CANCEL = 8
#: Button results in `TD_ID_RETRY <geosoft.gxapi.TD_ID_RETRY>` return value.
TD_BUTTON_RETRY = 16
#: Button results in `TD_ID_CLOSE <geosoft.gxapi.TD_ID_CLOSE>` return value.
TD_BUTTON_CLOSE = 32

#
# TD_ID constants
#
# TaskDialog Common Button Return Values

#: `TD_BUTTON_OK <geosoft.gxapi.TD_BUTTON_OK>` pressed.
TD_ID_OK = 1
#: `TD_BUTTON_CANCEL <geosoft.gxapi.TD_BUTTON_CANCEL>` pressed.
TD_ID_CANCEL = 2
#: `TD_BUTTON_RETRY <geosoft.gxapi.TD_BUTTON_RETRY>` pressed.
TD_ID_RETRY = 4
#: `TD_BUTTON_YES <geosoft.gxapi.TD_BUTTON_YES>` pressed.
TD_ID_YES = 6
#: `TD_BUTTON_NO <geosoft.gxapi.TD_BUTTON_NO>` pressed.
TD_ID_NO = 7
#: `TD_BUTTON_CLOSE <geosoft.gxapi.TD_BUTTON_CLOSE>` pressed.
TD_ID_CLOSE = 8	

#
# GXTB Constants
# 



#
# TB_SEARCH constants
#
# `GXTB <geosoft.gxapi.GXTB>` Searching mode

#: Random searches in a table.
TB_SEARCH_BINARY = 0
#: Linear searches up or down a table (Default).
TB_SEARCH_LINEAR = 1

#
# TB_SORT constants
#
# `GXTB <geosoft.gxapi.GXTB>` Sorting mode

#: Unique values only when sorting.
TB_SORT_UNIQUE = 0
#: Allow duplicates when sorting.
TB_SORT_ALLOW_DUPLICATES = 1	

#
# GXTPAT Constants
# 



#
# TPAT_STRING_SIZE constants
#
# Default string sizes.

#: Tpat code size
TPAT_CODE_SIZE = 21
#: Tpat label size
TPAT_LABEL_SIZE = 32
#: Tpat desc size
TPAT_DESC_SIZE = 128
#: Tpat symbfont size
TPAT_SYMBFONT_SIZE = 32	

#
# GXTR Constants
# 

	

#
# GXUSERMETA Constants
# 



#
# USERMETA_FORMAT constants
#
# `GXUSERMETA <geosoft.gxapi.GXUSERMETA>` Format Types

#: Use the standard type for the system
USERMETA_FORMAT_DEFAULT = -1
#: ISO 19139 standard
USERMETA_FORMAT_ISO = 0
#: FGDC Metadata Standard
USERMETA_FORMAT_FGDC = 1	

#
# GXVA Constants
# 



#
# VA_AVERAGE constants
#
# `GXVA <geosoft.gxapi.GXVA>` Object to average

#: Average the Rows
VA_AVERAGE_ROWS = 0
#: Average the Columns
VA_AVERAGE_COLUMNS = 1

#
# VA_OBJECT constants
#
# `GXVA <geosoft.gxapi.GXVA>` Object to select

#: Row
VA_ROW = 0
#: Column
VA_COL = 1	

#
# GXVECTOR3D Constants
# 

	

#
# GXVM Constants
# 

	

#
# GXVOX Constants
# 



#
# VOX_DIR constants
#
# Voxel direction

#: X/Y Plane (Fastest)
VOX_DIR_XY = 0
#: X/Z Plane (Middle)
VOX_DIR_XZ = 1
#: Y/Z Plane (Slowest)
VOX_DIR_YZ = 2

#
# VOX_DIRECTION constants
#
# Voxel export direction

#: XYZ
VOX_3D_DIR_XYZ = 0
#: YXZ
VOX_3D_DIR_YXZ = 1
#: XZY
VOX_3D_DIR_XZY = 2
#: YZX
VOX_3D_DIR_YZX = 3
#: ZXY
VOX_3D_DIR_ZXY = 4
#: ZYX
VOX_3D_DIR_ZYX = 5

#
# VOX_FILTER3D constants
#
# Voxel filter type

#: Specify a file containing the 27-point filter
VOX_FILTER3D_FILE = 0
#: Smoothing filter
VOX_FILTER3D_SMOOTHING = 1
#: Laplace filter
VOX_FILTER3D_LAPLACE = 2
#: X-Gradient filter
VOX_FILTER3D_X_GRADIENT = 3
#: Y-Gradient filter
VOX_FILTER3D_Y_GRADIENT = 4
#: Z-Gradient filter
VOX_FILTER3D_Z_GRADIENT = 5
#: Total-Gradient filter
VOX_FILTER3D_TOTAL_GRADIENT = 6

#
# VOX_GOCAD_ORIENTATION constants
#
# GOCAD Orientations

#: Normal
VOX_GOCAD_ORIENTATIONS_NORMAL = 0
#: Inverted (Z)
VOX_GOCAD_ORIENTATIONS_INVERTED = 1
#: Normal (ZFirst)
VOX_GOCAD_ORIENTATIONS_NORMAL_ZFIRST = 2
#: Inverted (Z) (ZFirst)
VOX_GOCAD_ORIENTATIONS_INVERTED_ZFIRST = 3

#
# VOX_GRID_LOGOPT constants
#
# Voxel log gridding options

#: Linear
VOX_GRID_LOGOPT_LINEAR = 0
#: Log, save as linear
VOX_GRID_LOGOPT_LOG_SAVELINEAR = -1
#: Log-linear, save as linear
VOX_GRID_LOGOPT_LOGLINEAR_SAVELINEAR = -2
#: Log, save as log
VOX_GRID_LOGOPT_LOG_SAVELOG = 1
#: Log-linear, save as log
VOX_GRID_LOGOPT_LOGLINEAR_SAVELOG = 2

#
# VOX_ORIGIN constants
#
# Voxel origin

#: Bottom corner (standard Geosoft)
VOX_ORIGIN_BOTTOM = 0
#: Top corner
VOX_ORIGIN_TOP = 1

#
# VOX_SLICE_MODE constants
#
# Voxel export direction

#: Linear
VOX_SLICE_MODE_LINEAR = 1
#: Nearest
VOX_SLICE_MODE_NEAREST = 0

#
# VOX_VECTORVOX_IMPORT constants
#
# Voxel direction

#: X, Y and Z
VOX_VECTORVOX_XYZ = 0
#: U, V and W
VOX_VECTORVOX_UVW = 1
#: Amplitude, Inclination and Declination
VOX_VECTORVOX_AID = 2	

#
# GXVOXD Constants
# 



#
# VOXELRENDER_MODE constants
#
# Render Modes

#: Render voxel cells
VOXELRENDER_FILL = 0
#: Render wireframe only
VOXELRENDER_EDGES = 1
#: Render both voxel cells and wireframe
VOXELRENDER_FILL_EDGES = 2
#: Trilinear interpolation
VOXELRENDER_SMOOTH = 3	

#
# GXVOXE Constants
# 



#
# VOXE_EVAL constants
#
# Voxel Evaluation modes

#: Nearest value
VOXE_EVAL_NEAR = 0
#: Linear Interpolation
VOXE_EVAL_INTERP = 1
#: Best Interpolation
VOXE_EVAL_BEST = 2	

#
# GXVULCAN Constants
# 



#
# BLOCK_MODEL_VARIABLE_TYPE constants
#
# Which variables to return from sReadBlockModelVariableInfo

#: Return numeric variable names
BLOCK_MODEL_NUMERIC_VARIABLE = 1
#: Return string variable names
BLOCK_MODEL_STRING_VARIABLE = 2	

#
# GXVV Constants
# 



#
# VV_DOUBLE_CRC_BITS constants
#
# Number of bits to use in double CRC's

#: Exact CRC
VV_DOUBLE_CRC_BITS_EXACT = 0
#: Default inaccuracy in double (10 Bits)
VV_DOUBLE_CRC_BITS_DEFAULT = 10
#: Maximum number of inaccuracy bits
VV_DOUBLE_CRC_BITS_MAX = 51

#
# VV_FLOAT_CRC_BITS constants
#
# Number of bits to use in float CRC's

#: Exact CRC
VV_FLOAT_CRC_BITS_EXACT = 0
#: Default inaccuracy in floats (7 Bits)
VV_FLOAT_CRC_BITS_DEFAULT = 7
#: Maximum number of inaccuracy bits
VV_FLOAT_CRC_BITS_MAX = 22

#
# VV_LOG_BASE constants
#
# Type of log to use

#: Base 10
VV_LOG_BASE_10 = 0
#: Base e
VV_LOG_BASE_E = 1

#
# VV_LOGMODE constants
#
# Ways to handle negatives

#: Dummies out value less than the minimum.
VV_LOGMODE_CLIPPED = 0
#: if the data is in the range +/- minimum,
#: it is left alone.  Otherwise, the data
#: is divided by the minimum, the log is
#: applied, the minimum is added and the
#: sign is reapplied. Use `log_linear <geosoft.gxapi.GXVV.log_linear>` function
#: if decades in results are required.
VV_LOGMODE_SCALED = 1
#: Any values below the minimum are turned to the minimum.
VV_LOGMODE_CLAMPED = 2
#: Similar to Scaled but using a smoother function. Identical to LogLinear_VV.
VV_LOGMODE_LINEAR = 3

#
# VV_LOOKUP constants
#
# Lookup style

#: Only exact matches are used
VV_LOOKUP_EXACT = 0
#: Nearest match is used (regardless of sampling range)
VV_LOOKUP_NEAREST = 1
#: Interpolate between values (regardless of sampling range)
VV_LOOKUP_INTERPOLATE = 2
#: Use nearest match only if within sampling range
VV_LOOKUP_NEARESTCLOSE = 3
#: Interpolate only if within sampling range
VV_LOOKUP_INTERPCLOSE = 4

#
# VV_MASK constants
#
# Where to mask

#: Inside
VV_MASK_INSIDE = 0
#: Outside
VV_MASK_OUTSIDE = 1

#
# VV_ORDER constants
#
# Specify if the data is montonically increasing or decreasing.

#: There is no specific data size ordering in the `GXVV <geosoft.gxapi.GXVV>`.
VV_ORDER_NONE = 0
#: Every value is greater than or equal to the previous value.
VV_ORDER_INCREASING = 1
#: Every value is less than or equal to the previous value.
VV_ORDER_DECREASING = 2

#
# VV_SORT constants
#
# Sort order

#: Ascending
VV_SORT_ASCENDING = 0
#: Descending
VV_SORT_DESCENDING = 1

#
# VV_WINDOW constants
#
# How to handle `GXVV <geosoft.gxapi.GXVV>` limits

#: Dummy values outside the limits
VV_WINDOW_DUMMY = 0
#: Set values outside the limits to the limits
VV_WINDOW_LIMIT = 1	

#
# GXWA Constants
# 



#
# WA_ENCODE constants
#
# `GXWA <geosoft.gxapi.GXWA>` Encode defines

#: Current Ansi Code Page (Conversion from UTF-8 data, if an exisiting BOM header found with `WA_APPEND <geosoft.gxapi.WA_APPEND>`,
#: encoding will switch to `WA_ENCODE_UTF8 <geosoft.gxapi.WA_ENCODE_UTF8>`)
WA_ENCODE_ANSI = 0
#: Write all data without any conversion check
WA_ENCODE_RAW = 1
#: :ref:`UTF8` (If no exisiting BOM header found with `WA_APPEND <geosoft.gxapi.WA_APPEND>`, encoding will switch to `WA_ENCODE_ANSI <geosoft.gxapi.WA_ENCODE_ANSI>`)
WA_ENCODE_UTF8 = 2
#: :ref:`UTF8` w.o. header (will assume :ref:`UTF8` encoding if `WA_APPEND <geosoft.gxapi.WA_APPEND>` is used)
WA_ENCODE_UTF8_NOHEADER = 3
#: UTF16 w.o. header (will assume UTF16 encoding if `WA_APPEND <geosoft.gxapi.WA_APPEND>` is used)
WA_ENCODE_UTF16_NOHEADER = 4

#
# WA_OPEN constants
#
# `GXWA <geosoft.gxapi.GXWA>` Open defines

#: Create new file
WA_NEW = 0
#: Append to existing file
WA_APPEND = 1	

#
# GXACQUIRE Constants
# 



#
# ACQUIRE_SEL constants
#
# Type of Selection

#: Holes
ACQUIRE_SEL_HOLES = 0
#: Point
ACQUIRE_SEL_POINT = 1	

#
# GXARCDB Constants
# 



#
# ARC_SELTBL_TYPE constants
#
# Describes what kind of table was selected

#: Standalone Table
ARC_SELTBL_STANDALONE = 0
#: Feature Layer
ARC_SELTBL_FEATURELAYER = 1
#: User Canceled
ARC_SELTBL_CANCELED = -1	

#
# GXARCDH Constants
# 

	

#
# GXARCMAP Constants
# 



#
# ARCMAP_LOAD_FLAGS constants
#
# Flags that can be combined and passed to iLoadMap_ARCMAP

#: If an existing frame is found delete it
ARCMAP_LOAD_DELFRAME = 1
#: If an existing layer is found delete it
ARCMAP_LOAD_DELLAYER = 2
#: If an existing frame is found add new layers to it
ARCMAP_LOAD_EXISTFRAME = 4
#: If an existing layer is found make a copy
ARCMAP_LOAD_COPYLAYER = 8
#: Hide all other existing layers in frame
ARCMAP_LOAD_HIDESIBLINGS = 16
#: Prefix the map filename part as part of the frame name
ARCMAP_LOAD_PREFIXMAPFRAME = 32
#: Prefix the map filename part as part of the layer name
ARCMAP_LOAD_PREFIXMAPLAYER = 64
#: Will render all views in single layer with the data view defining the coordinate system
ARCMAP_LOAD_MERGETOSINGLEVIEW = 128
#: Load everything into the current data frame
ARCMAP_LOAD_INTOCURRENTFRAME = 256
#: Use the map only for sizing data frames in layout, only load extra datasets.
ARCMAP_LOAD_NOMAPLAYERS = 512
#: Activates the main quickmap layer when done (e.g. 3D Viewer)
ARCMAP_LOAD_ACTIVATE = 1024
#: New method for loading maps introduced in 7.1. Will mimic what happens in montaj (i.e. base groups and 3D become graphics and views gets split into separate LYRs).
ARCMAP_LOAD_NEW = 2048
#: Use a provided name tag as prefix when naming a newly created map layer.
ARCMAP_LOAD_NAMETAGISPREFIX = 4096	

#
# GXARCPY Constants
# 

	

#
# GXARCSYS Constants
# 

	

#
# GXBIGRID Constants
# 

	

#
# GXCHIMERA Constants
# 



#
# CHIMERA_MAX_CHAN constants
#
# Maximum channels in Chimera database

#: Chimera max chan
CHIMERA_MAX_CHAN = 128

#
# CHIMERA_PLOT constants
#
# Chimera plot type

#: Rose
CHIMERA_PLOT_ROSE = 0
#: Pie
CHIMERA_PLOT_PIE = 1
#: Bar
CHIMERA_PLOT_BAR = 2	

#
# GXCOM Constants
# 



#
# COM_BAUD constants
#
# Connection Speed

#: 110
COM_BAUD_110 = 0
#: 300
COM_BAUD_300 = 1
#: 600
COM_BAUD_600 = 2
#: 1200
COM_BAUD_1200 = 3
#: 2400
COM_BAUD_2400 = 4
#: 4800
COM_BAUD_4800 = 5
#: 9600
COM_BAUD_9600 = 6
#: 14400
COM_BAUD_14400 = 7
#: 19200
COM_BAUD_19200 = 8
#: 56000
COM_BAUD_56000 = 9
#: 57600
COM_BAUD_57600 = 10
#: 115200
COM_BAUD_115200 = 11
#: 128000
COM_BAUD_128000 = 12
#: 256000
COM_BAUD_256000 = 13
#: 38400
COM_BAUD_38400 = 14

#
# COM_DATASIZE constants
#
# Data Bits

#: Five
COM_DATASIZE_FIVE = 5
#: Six
COM_DATASIZE_SIX = 6
#: Seven
COM_DATASIZE_SEVEN = 7
#: Eight
COM_DATASIZE_EIGHT = 8

#
# COM_FLOWCONTROL constants
#
# Flow Control Options

#: None
COM_FLOWCONTROL_NONE = 0
#: Rts cts
COM_FLOWCONTROL_RTS_CTS = 1
#: Dtr dsr
COM_FLOWCONTROL_DTR_DSR = 2
#: Xon xoff
COM_FLOWCONTROL_XON_XOFF = 3

#
# COM_PARITY constants
#
# Parity

#: Even
COM_PARITY_EVEN = 0
#: Nark
COM_PARITY_NARK = 1
#: None
COM_PARITY_NONE = 2
#: Odd
COM_PARITY_ODD = 3
#: Space
COM_PARITY_SPACE = 4

#
# COM_STOPBITS constants
#
# Stop Bits

#: One
COM_STOPBITS_ONE = 0
#: One5
COM_STOPBITS_ONE5 = 1
#: Two
COM_STOPBITS_TWO = 2	

#
# GXCSYMB Constants
# 



#
# CSYMB_COLOR constants
#
# Color Symbol filling defines

#: Draw Edges only
CSYMB_COLOR_EDGE = 0
#: Fill Symbols
CSYMB_COLOR_FILL = 1	

#
# GXDGW Constants
# 



#
# DGW_OBJECT constants
#
# Dialog object defines
# INFO TYPE   EDIT   FEDIT  LEDIT  CEDIT  EBUT
# =========   =====  =====  =====  =====  =====
# LABEL       RW     RW     RW     RW     RW          R - can use GetInfo_DGW
# TEXT        RW     RW     RW     RW     .           W - can use `set_info <geosoft.gxapi.GXDGW.set_info>`
# PATH        .      RW     .      .      .
# FILEPATH    .      RW     .      .      .
# LISTVAL     .      .      R      .      .
# LISTALIAS   .      .      RW     .      .

#: The text label tied to each Dialog component.
DGW_LABEL = 0
#: The edit field text.
DGW_TEXT = 1
#: The file edit path.
DGW_PATH = 2
#: The complete file name, path included.
DGW_FILEPATH = 3
#: The alias value associated with the list entry.
DGW_LISTVAL = 4
#: The text value associated with the list entry.
DGW_LISTALIAS = 5
#: The extension associated with a filename entry.
DGW_EXT = 7
#: Hide the button or entry and its label, if string is not "0"
DGW_HIDE = 8	

#
# GXDH Constants
# 



#
# DH_DEFAULT_FILENAMES constants
#
# Default filenames

#: Dh default rockcode file
DH_DEFAULT_ROCKCODE_FILE = "agso.csv"
#: Dh default structurecode file
DH_DEFAULT_STRUCTURECODE_FILE = "structcodes.csv"

#
# STR_DH_HOLES constants
#
# This declares the size of the string used in various
# `GXDH <geosoft.gxapi.GXDH>` GXs to store all the currently selected holes, as input to the two-panel
# selection tool. This should be big enough for 65,000 16-character hole names!

#: Str dh holes
STR_DH_HOLES = 1048576

#
# DH_COMP_CHOICE constants
#
# Composition

#: User is done
DH_COMP_DONE = 0
#: User canceled
DH_COMP_CANCEL = -1
#: User chose to select an interval interactively
DH_COMP_SELECT = 1
#: User chose to refresh
DH_COMP_REFRESH = 2

#
# DH_COMPSTDB_HOLSEL constants
#
# Composite Hole Selection

#: All
DH_COMPSTDB_HOLSEL_ALL = 0
#: Selected
DH_COMPSTDB_HOLSEL_SELECTED = 1

#
# DH_COMPSTDB_INTSEL constants
#
# Composite Interval

#: Fixed
DH_COMPSTDB_INTSEL_FIXED = 0
#: Lithology
DH_COMPSTDB_INTSEL_LITHOLOGY = 1
#: Bestfitlith
DH_COMPSTDB_INTSEL_BESTFITLITH = 2
#: Intfile
DH_COMPSTDB_INTSEL_INTFILE = 3

#
# DH_DATA constants
#
# What to import

#: Dipazimuth
DH_DATA_DIPAZIMUTH = 0
#: Eastnorth
DH_DATA_EASTNORTH = 1
#: Fromto
DH_DATA_FROMTO = 2
#: Point
DH_DATA_POINT = 3
#: Collar
DH_DATA_COLLAR = 4
#: The type is not known
DH_DATA_UNKNOWN = 100

#
# DH_DEFINE_PLAN constants
#
# Plans

#: Dh define plan
DH_DEFINE_PLAN = 1

#
# DH_DEFINE_SECT constants
#
# Types of Sections

#: Ns
DH_DEFINE_SECT_NS = 1
#: Ew
DH_DEFINE_SECT_EW = 2
#: Angled
DH_DEFINE_SECT_ANGLED = 3

#
# DH_EXP constants
#
# Type of Export

#: Csv
DH_EXP_CSV = 0
#: Ascii
DH_EXP_ASCII = 1
#: Access
DH_EXP_ACCESS = 2
#: Collars as points
DH_EXP_SHP = 3
#: To Surpace Geological database (special format ACCESS)
DH_EXP_SURPAC = 4
#: Hole traces as polylines
DH_EXP_SHP_TRACES = 5

#
# DH_HOLES constants
#
# Holes to select

#: All
DH_HOLES_ALL = 0
#: Selected
DH_HOLES_SELECTED = 1

#
# DH_MASK constants
#
# Masks

#: Append
DH_MASK_APPEND = 0
#: New
DH_MASK_NEW = 1

#
# DH_PLOT constants
#
# Type of Plot

#: Plan
DH_PLOT_PLAN = 0
#: Section
DH_PLOT_SECTION = 1
#: Striplog
DH_PLOT_STRIPLOG = 2
#: Hole traces
DH_PLOT_HOLE_TRACES = 3
#: 3d
DH_PLOT_3D = 4
#: Section stack
DH_PLOT_SECTION_STACK = 5
#: Section fence
DH_PLOT_SECTION_FENCE = 6
#: Section crooked
DH_PLOT_SECTION_CROOKED = 7

#
# DH_SECT_PAGE constants
#
# Sections

#: Section
DH_SECT_PAGE_SECTION = 1

#
# DH_SURFACE constants
#
# Surface selection for creation of geological
# top or bottom surfaces.

#: First layer from
DH_SURFACE_FIRST_LAYER_FROM = 0
#: First layer to
DH_SURFACE_FIRST_LAYER_TO = 1
#: Second layer from
DH_SURFACE_SECOND_LAYER_FROM = 2
#: Second layer to
DH_SURFACE_SECOND_LAYER_TO = 3
#: Last layer from
DH_SURFACE_LAST_LAYER_FROM = 4
#: Last layer to
DH_SURFACE_LAST_LAYER_TO = 5

#
# DIP_CONVENTION constants
#
# Dip convention

#: Negative
DIP_CONVENTION_NEGATIVE = -1
#: Positive
DIP_CONVENTION_POSITIVE = 1	

#
# GXDMPPLY Constants
# 

	

#
# GXDOCU Constants
# 



#
# DOCU_OPEN constants
#
# How to open document

#: View
DOCU_OPEN_VIEW = 0
#: Edit
DOCU_OPEN_EDIT = 1	

#
# GXDU Constants
# 



#
# DB_DUP constants
#
# Duplicate Types

#: First
DB_DUP_FIRST = 1
#: Average
DB_DUP_AVERAGE = 2
#: Minimum
DB_DUP_MINIMUM = 3
#: Maximum
DB_DUP_MAXIMUM = 4
#: Median
DB_DUP_MEDIAN = 5
#: Last
DB_DUP_LAST = 6

#
# DB_DUPEDIT constants
#
# Duplicate Edit Flags

#: Single
DB_DUPEDIT_SINGLE = 0
#: All
DB_DUPEDIT_ALL = 1

#
# DU_CHANNELS constants
#
# Channels to Display

#: Displayed
DU_CHANNELS_DISPLAYED = 0
#: All
DU_CHANNELS_ALL = 1

#
# DU_EXPORT constants
#
# Export Type

#: Csv
DU_EXPORT_CSV = 0
#: Oddf
DU_EXPORT_ODDF = 1
#: Post pc
DU_EXPORT_POST_PC = 2
#: Post unix
DU_EXPORT_POST_UNIX = 3

#
# DU_FILL constants
#
# Filling Options

#: Inside
DU_FILL_INSIDE = 0
#: Outside
DU_FILL_OUTSIDE = 1

#
# DU_IMPORT constants
#
# Import Mode

#: Append
DU_IMPORT_APPEND = 0
#: Replace
DU_IMPORT_REPLACE = 1
#: Merge
DU_IMPORT_MERGE = 2
#: Merge append
DU_IMPORT_MERGE_APPEND = 3

#
# DU_INTERP constants
#
# Inside Interpolation Method

#: Nearest
DU_INTERP_NEAREST = 1
#: Linear
DU_INTERP_LINEAR = 2
#: Cubic
DU_INTERP_CUBIC = 3
#: Akima
DU_INTERP_AKIMA = 4
#: Predict
DU_INTERP_PREDICT = 5

#
# DU_INTERP_EDGE constants
#
# Edge Interpolation Method

#: None
DU_INTERP_EDGE_NONE = 0
#: Same
DU_INTERP_EDGE_SAME = 1
#: Nearest
DU_INTERP_EDGE_NEAREST = 2
#: Linear
DU_INTERP_EDGE_LINEAR = 3

#
# DU_LAB_TYPE constants
#
# File Types

#: The delimiter string identifies
#: characters to be used as delimiters.  Use C style escape
#: sequences to identify non-printable characters.  The
#: default delimiters for FREE format files are " \\t,".
DU_LAB_TYPE_FREE = 1
#: For COMMA type files, the delimiter string identifies
#: characters to be removed before comma delimiting.  The
#: default for COMMA delimited files is " \\t".
DU_LAB_TYPE_COMMA = 2

#
# DU_LEVEL constants
#
# Leveling Options

#: Extract line corrections
DU_LEVEL_LINES = 0
#: Extract tie corrections
DU_LEVEL_TIES = 1
#: Extract all corrections
DU_LEVEL_ALL = 2

#
# DU_LINEOUT constants
#
# Lineout Options (du.h)

#: Single
DU_LINEOUT_SINGLE = 0
#: Multiple
DU_LINEOUT_MULTIPLE = 1

#
# DU_FEATURE_TYPE_OUTPUT constants
#
# Export to geodatabase feature type (du.h)

#: Point
DU_FEATURE_TYPE_OUTPUT_POINT = 0
#: Line
DU_FEATURE_TYPE_OUTPUT_LINE = 1

#
# DU_GEODATABASE_EXPORT_TYPE constants
#
# Export to geodatabase overwrite mode(du.h)

#: Overwrite geodatabase
DU_GEODATABASE_EXPORT_TYPE_OVERWRITE_GEODATABASE = 0
#: Overwrite featureclass
DU_GEODATABASE_EXPORT_TYPE_OVERWRITE_FEATURECLASS = 1
#: Append
DU_GEODATABASE_EXPORT_TYPE_APPEND = 2

#
# DU_LINES constants
#
# Lines to display

#: Displayed
DU_LINES_DISPLAYED = 0
#: Selected
DU_LINES_SELECTED = 1
#: All
DU_LINES_ALL = 2

#
# DU_LOADLTB constants
#
# Load table options

#: Replace
DU_LOADLTB_REPLACE = 0
#: Append
DU_LOADLTB_APPEND = 1

#
# DU_LOOKUP constants
#
# Lookup Mode

#: Requires an exact match in all indexes.
#: Results will dummy if Indexes are not found.
DU_LOOKUP_EXACT = 0
#: Requires that the first index match exactly.
#: The nearest second index will be used for the finding
#: the lookup value.
#: The results will be dummy only if the first index
#: does not have a match.
DU_LOOKUP_NEAREST = 1
#: The same as _NEAREST, except that the value will
#: be interpolated between the two nearest
#: framing values in the table.
DU_LOOKUP_INTERPOLATE = 2
#: Same as _NEAREST mode except that the target
#: value must be within the CLOSE distance to a
#: table value.
#: a) the primary index channel for single index
#: lookups;
#: b) the secondary index channel for
#: double index lookups.
#: Values not in data spacing are dummy.
DU_LOOKUP_NEARESTCLOSE = 3
#: Same as _INTERPOLATE mode except that the target
#: value must be within the CLOSE distance to a
#: table value.
#: a) the primary index channel for single index
#: lookups;
#: b) the secondary index channel for
#: double index lookups.
#: Values not in data spacing are dummy.
DU_LOOKUP_INTERPCLOSE = 4
#: Interpolate between values, dummy beyond two ends
DU_LOOKUP_INTERPOLATE_DUMMYOUTSIDE = 5
#: Interpolate between values, constant end values beyond two ends
DU_LOOKUP_INTERPOLATE_CONSTOUTSIDE = 6
#: Interpolate between values, extrapolate beyond two ends
DU_LOOKUP_INTERPOLATE_EXTPLOUTSIDE = 7
#: Maximum option value
DU_LOOKUP_MAXOPTION = 8

#
# DU_MASK constants
#
# Masking Options

#: Inside
DU_MASK_INSIDE = 0
#: Outside
DU_MASK_OUTSIDE = 1

#
# DU_MERGE constants
#
# Merge flags

#: Append
DU_MERGE_APPEND = 0

#
# DU_MODFID constants
#
# Fid Update Options

#: Will insert fid range by moving data.  Inserted
#: range will always be dummied out.  If the insertion point
#: is before start of data, the fid start is changed.
DU_MODFID_INSERT = 0
#: Will delete the range of fids.
DU_MODFID_DELETE = 1
#: Is like INSERT, except that it is only used to
#: add fids to the start or end of the existing data.  The
#: data is not moved with repect to the current fid locations.
DU_MODFID_APPEND = 2

#
# DU_MOVE constants
#
# Move Style

#: Move input to absolute value in control channel
DU_MOVE_ABSOLUTE = 0
#: Subtract control channel from input channel
DU_MOVE_MINUS = 1
#: Add control channel to input channel
DU_MOVE_PLUS = 2
#: data is NOT moved, but dummies in the input are interpolated
#: based on the control channel, assuming both the input and control
#: vary linearly inside the gaps
DU_MOVE_INTERP = 3

#
# DU_REFID constants
#
# Interpolation mode

#: 0
DU_REFID_LINEAR = 0
#: 1
DU_REFID_MINCUR = 1
#: 2
DU_REFID_AKIMA = 2
#: 3
DU_REFID_NEAREST = 3

#
# DU_SORT constants
#
# Sort Direction

#: Ascending
DU_SORT_ASCENDING = 0
#: Descending
DU_SORT_DESCENDING = 1

#
# DU_SPLITLINE constants
#
# Sort Direction

#: Xyposition
DU_SPLITLINE_XYPOSITION = 0
#: Sequential
DU_SPLITLINE_SEQUENTIAL = 1
#: Toversions
DU_SPLITLINE_TOVERSIONS = 2

#
# DU_STORAGE constants
#
# Storage Type

#: Line
DU_STORAGE_LINE = 0
#: Group
DU_STORAGE_GROUP = 1

#
# QC_PLAN_TYPE constants
#
# Type Plan

#: Qc plan surveyline
QC_PLAN_SURVEYLINE = 0
#: Qc plan tieline
QC_PLAN_TIELINE = 1
#: Qc plan bothlines
QC_PLAN_BOTHLINES = 2

#
# DU_DISTANCE_CHANNEL_TYPE constants
#
# Distance channel direction type

#: Zero distance is always at the start of the line.
DU_DISTANCE_CHANNEL_MAINTAIN_DIRECTION = 0
#: Put zero at the end of the line with min X if X changes most, or min Y if Y changes most
DU_DISTANCE_CHANNEL_CARTESIAN_COORDINATES = 1

#
# DU_DIRECTGRID_METHOD constants
#
# How to calculate the cell values for direct gridding.

#: Du directgrid min
DU_DIRECTGRID_MIN = 0
#: Du directgrid max
DU_DIRECTGRID_MAX = 1
#: Du directgrid mean
DU_DIRECTGRID_MEAN = 2	

#
# GXDXFI Constants
# 

	

#
# GXEDB Constants
# 



#
# MAX_PROF_WND constants
#
# The following value should be kept synchronized with the value defined in src\\geoguilib\\stdafx.h

#: Max prof wnd
MAX_PROF_WND = 5

#
# EDB_PATH constants
#
# Four forms

#: d:\\directory\\file.gdb
EDB_PATH_FULL = 0
#: \\directory\\file.gdb
EDB_PATH_DIR = 1
#: File.gdb
EDB_PATH_NAME_EXT = 2
#: File
EDB_PATH_NAME = 3

#
# EDB_PROF constants
#
# Profile data

#: DB_SYMB
EDB_PROF_I_CHANNEL = 0
#: 0 - no line
#: 1 - solid
#: 2 - long dash
#: 3 - short dash
EDB_PROF_I_LINE_STYLE = 1
#: 0 - no line
#: 1 - normal
#: 2 - medium
#: 3 - heavy
EDB_PROF_I_LINE_WEIGHT = 2
#: 0 - no symbol
#: 1 - rectangle
#: 2 - circle
#: 3 - triangle
#: 4 - diamond
#: 5 - x
#: 6 - +
EDB_PROF_I_SYMBOL = 3
#: 0 - normal
#: 1 - large
EDB_PROF_I_SYMBOL_WEIGHT = 4
#: `GXMVIEW <geosoft.gxapi.GXMVIEW>` Color Value
EDB_PROF_I_COLOR = 5
#: 0-no, 1-yes
EDB_PROF_I_WRAP = 6
#: 0-no, 1-yes
EDB_PROF_I_BREAK_ON_DUMMY = 7
#: 0-no, 1-yes
EDB_PROF_I_GRID_LINE = 8
#: 0-no, 1-yes
EDB_PROF_R_GRID_LINE_INTERVAL = 9
#: 0-Linear, 1-Log, 2-LogLinear
EDB_PROF_I_LOG = 10
#: Minimum Value
EDB_PROF_R_LOG_MINIMUM = 11
#: 0-no, 1-yes
EDB_PROF_I_SAMESCALE = 12
#: 0 - current line
#: -1 - previous line
#: -2 - next line
EDB_PROF_I_SOURCELINE = 13
#: 0 - scale to fit for each line
#: 1 - fix the range
#: 2 - fix the scale, center the range
EDB_PROF_I_SCALEOPTION = 14
#: 0-no, 1-yes
EDB_PROF_I_SAMERANGE = 15
#: 0-no, 1-yes
EDB_PROF_I_VERT_GRID_LINE = 16
#: 0-no, 1-yes
EDB_PROF_R_VERT_GRID_LINE_INTERVAL = 17
#: 0-no, 1-yes
EDB_PROF_I_AUTO_RESCALE_X = 18

#
# EDB_PROFILE_SCALE constants
#
# Profile Scale Options

#: Linear
EDB_PROFILE_SCALE_LINEAR = 0
#: Log
EDB_PROFILE_SCALE_LOG = 1
#: Loglinear
EDB_PROFILE_SCALE_LOGLINEAR = 2

#
# EDB_REMOVE constants
#
# How to handle pending changes in document

#: Save
EDB_REMOVE_SAVE = 0
#: Prompt
EDB_REMOVE_PROMPT = 1
#: Discard
EDB_REMOVE_DISCARD = 2

#
# EDB_UNLOAD constants
#
# What type of prompt

#: No prompt
EDB_UNLOAD_NO_PROMPT = 0
#: Single prompt
EDB_UNLOAD_SINGLE_PROMPT = 1
#: Obsolete
EDB_UNLOAD_MULTI_PROMPT = 2

#
# EDB_WINDOW_POSITION constants
#
# Window Positioning Options

#: Docked
EDB_WINDOW_POSITION_DOCKED = 0
#: Floating
EDB_WINDOW_POSITION_FLOATING = 1

#
# EDB_WINDOW_STATE constants
#
# Window State Options

#: Edb window restore
EDB_WINDOW_RESTORE = 0
#: Edb window minimize
EDB_WINDOW_MINIMIZE = 1
#: Edb window maximize
EDB_WINDOW_MAXIMIZE = 2

#
# EDB_YAXIS_DIRECTION constants
#
# Window State Options

#: Edb yaxis normal
EDB_YAXIS_NORMAL = 0
#: Edb yaxis inverted
EDB_YAXIS_INVERTED = 1	

#
# GXEDOC Constants
# 



#
# EDOC_PATH constants
#
# Four forms

#: d:\\directory\\file.gdb
EDOC_PATH_FULL = 0
#: \\directory\\file.gdb
EDOC_PATH_DIR = 1
#: file.gdb
EDOC_PATH_NAME_EXT = 2
#: file
EDOC_PATH_NAME = 3

#
# EDOC_TYPE constants
#
# Avaialable generic document types

#: `GXGMSYS <geosoft.gxapi.GXGMSYS>` 3D Model
EDOC_TYPE_GMS3D = 0
#: Voxel
EDOC_TYPE_VOXEL = 1
#: Voxel Inversion
EDOC_TYPE_VOXEL_INVERSION = 2
#: `GXGMSYS <geosoft.gxapi.GXGMSYS>` 2D Model
EDOC_TYPE_GMS2D = 3

#
# EDOC_UNLOAD constants
#
# What type of prompt

#: No prompt
EDOC_UNLOAD_NO_PROMPT = 0
#: Prompt
EDOC_UNLOAD_PROMPT = 1

#
# EDOC_WINDOW_POSITION constants
#
# Window Positioning Options

#: Docked
EDOC_WINDOW_POSITION_DOCKED = 0
#: Floating
EDOC_WINDOW_POSITION_FLOATING = 1

#
# EDOC_WINDOW_STATE constants
#
# Window State Options

#: Edoc window restore
EDOC_WINDOW_RESTORE = 0
#: Edoc window minimize
EDOC_WINDOW_MINIMIZE = 1
#: Edoc window maximize
EDOC_WINDOW_MAXIMIZE = 2

#
# GMS3D_MODELTYPE constants
#
# Avaialable model types

#: Depth Model
GMS3D_MODELTYPE_DEPTH = 0
#: Time Model
GMS3D_MODELTYPE_TIME = 1

#
# GMS2D_MODELTYPE constants
#
# Avaialable model types

#: Depth Model
GMS2D_MODELTYPE_DEPTH = 0
#: Time Model
GMS2D_MODELTYPE_TIME = 1	

#
# GXEMAP Constants
# 



#
# EMAP_FONT constants
#
# Font Types

#: Tt
EMAP_FONT_TT = 0
#: Gfn
EMAP_FONT_GFN = 1

#
# EMAP_PATH constants
#
# Four forms

#: d:\\directory\\file.gdb
EMAP_PATH_FULL = 0
#: \\directory\\file.gdb
EMAP_PATH_DIR = 1
#: File.gdb
EMAP_PATH_NAME_EXT = 2
#: File
EMAP_PATH_NAME = 3

#
# EMAP_REDRAW constants
#
# Redraw Options

#: No
EMAP_REDRAW_NO = 0
#: Yes
EMAP_REDRAW_YES = 1

#
# EMAP_REMOVE constants
#
# How to handle pending changes in document

#: Save
EMAP_REMOVE_SAVE = 0
#: Prompt
EMAP_REMOVE_PROMPT = 1
#: Discard
EMAP_REMOVE_DISCARD = 2

#
# EMAP_TRACK constants
#
# Tracking Options

#: Erase Object after you return?
EMAP_TRACK_ERASE = 1
#: Allow use of right-menu
EMAP_TRACK_RMENU = 2
#: If user holds down left-mouse, will return many times
EMAP_TRACK_CYCLE = 4

#
# EMAP_VIEWPORT constants
#
# Tracking Options

#: Normal map usage
EMAP_VIEWPORT_NORMAL = 0
#: Zoom Mode
EMAP_VIEWPORT_BROWSEZOOM = 1
#: Change Area Of Interest Mode
EMAP_VIEWPORT_BROWSEAOI = 2

#
# EMAP_WINDOW_POSITION constants
#
# Window Positioning Options

#: Docked
EMAP_WINDOW_POSITION_DOCKED = 0
#: Floating
EMAP_WINDOW_POSITION_FLOATING = 1

#
# EMAP_WINDOW_STATE constants
#
# Window State Options

#: Emap window restore
EMAP_WINDOW_RESTORE = 0
#: Emap window minimize
EMAP_WINDOW_MINIMIZE = 1
#: Emap window maximize
EMAP_WINDOW_MAXIMIZE = 2

#
# LAYOUT_VIEW_UNITS constants
#
# Base dlayout display units

#: Millimeters
LAYOUT_VIEW_MM = 0
#: Centimeters
LAYOUT_VIEW_CM = 1
#: Inches
LAYOUT_VIEW_IN = 2	

#
# GXEMAPTEMPLATE Constants
# 



#
# EMAPTEMPLATE_PATH constants
#
# Four forms

#: d:\\directory\\file.gdb
EMAPTEMPLATE_PATH_FULL = 0
#: \\directory\\file.gdb
EMAPTEMPLATE_PATH_DIR = 1
#: file.gdb
EMAPTEMPLATE_PATH_NAME_EXT = 2
#: file
EMAPTEMPLATE_PATH_NAME = 3

#
# EMAPTEMPLATE_TRACK constants
#
# Tracking Options

#: Erase Object after you return?
EMAPTEMPLATE_TRACK_ERASE = 1
#: Allow use of right-menu
EMAPTEMPLATE_TRACK_RMENU = 2
#: If user holds down left-mouse, will return many times
EMAPTEMPLATE_TRACK_CYCLE = 4

#
# EMAPTEMPLATE_WINDOW_POSITION constants
#
# Window Positioning Options

#: Docked
EMAPTEMPLATE_WINDOW_POSITION_DOCKED = 0
#: Floating
EMAPTEMPLATE_WINDOW_POSITION_FLOATING = 1

#
# EMAPTEMPLATE_WINDOW_STATE constants
#
# Window State Options

#: Emaptemplate window restore
EMAPTEMPLATE_WINDOW_RESTORE = 0
#: Emaptemplate window minimize
EMAPTEMPLATE_WINDOW_MINIMIZE = 1
#: Emaptemplate window maximize
EMAPTEMPLATE_WINDOW_MAXIMIZE = 2	

#
# GXEUL3 Constants
# 



#
# EUL3_RESULT constants
#
# Euler result types

#: X
EUL3_RESULT_X = 1
#: Y
EUL3_RESULT_Y = 2
#: Depth
EUL3_RESULT_DEPTH = 3
#: Background
EUL3_RESULT_BACKGROUND = 4
#: Deptherror
EUL3_RESULT_DEPTHERROR = 5
#: Locationerror
EUL3_RESULT_LOCATIONERROR = 6
#: Windowx
EUL3_RESULT_WINDOWX = 7
#: Windowy
EUL3_RESULT_WINDOWY = 8	

#
# GXEXP Constants
# 

	

#
# GXFFT Constants
# 



#
# FFT_DETREND constants
#
# Detrending option

#: No trend remove
FFT_DETREND_NONE = 0
#: Detrend order 1 using only two end points
FFT_DETREND_ENDS = 1
#: Detrend order 1 using all data points
FFT_DETREND_ALL = 2
#: Remove mean value
FFT_DETREND_MEAN = 3	

#
# GXFFT2 Constants
# 



#
# FFT2_PG constants
#
# Pager Direction

#: Forward
FFT2_PG_FORWARD = 0
#: Inverse
FFT2_PG_INVERSE = 1	

#
# GXFLT Constants
# 

	

#
# GXGD Constants
# 



#
# GD_STATUS constants
#
# Grid open mode

#: Readonly
GD_STATUS_READONLY = 0
#: New
GD_STATUS_NEW = 1
#: Old
GD_STATUS_OLD = 2	

#
# GXGER Constants
# 

	

#
# GXGMSYS Constants
# 

	

#
# GXGU Constants
# 



#
# EM_ERR constants
#
# Error Scaling

#: Unscaled
EM_ERR_UNSCALED = 0
#: Logscaling
EM_ERR_LOGSCALING = 1

#
# EM_INV constants
#
# Type of Inversion

#: Inphase
EM_INV_INPHASE = 0
#: Quadrature
EM_INV_QUADRATURE = 1
#: Both
EM_INV_BOTH = 2

#
# EMPLATE_DOMAIN constants
#
# Type of Domain

#: Emplate frequency
EMPLATE_FREQUENCY = 1
#: Emplate time
EMPLATE_TIME = 9

#
# EMPLATE_TX constants
#
# Orientation

#: X
EMPLATE_TX_X = 1
#: Y
EMPLATE_TX_Y = 2
#: Z
EMPLATE_TX_Z = 3

#
# GU_DAARC500_DATATYPE constants
#
# Supported serial data types for import

#: Gu daarc500 unknown
GU_DAARC500_UNKNOWN = 0
#: Gu daarc500 generic ascii
GU_DAARC500_GENERIC_ASCII = 1
#: Gu daarc500 gps
GU_DAARC500_GPS = 2
#: Gu daarc500 gr820 256d
GU_DAARC500_GR820_256D = 3
#: Gu daarc500 gr820 256du
GU_DAARC500_GR820_256DU = 4
#: Gu daarc500 gr820 512du
GU_DAARC500_GR820_512DU = 5
#: Gu daarc500 nav
GU_DAARC500_NAV = 6

#
# PEAKEULER_XY constants
#
# Fit Options

#: Nofit
PEAKEULER_XY_NOFIT = 0
#: Fit
PEAKEULER_XY_FIT = 1	

#
# GXGUI Constants
# 



#
# AOI_RETURN_STATE constants
#
# AOI query return state

#: User canceled
AOI_RETURN_CANCEL = -1
#: User chose to continue with no AOI defined or available
AOI_RETURN_NODEFINE = 0
#: User chose to continue and defined valid AOI parameters
AOI_RETURN_DEFINE = 1

#
# COORDSYS_MODE constants
#
# Coordinate system wizard `GXIPJ <geosoft.gxapi.GXIPJ>` types allowed on return.
# The wizard present three types of projections for selection
# by the user, Geographic (GCS), Projected (PCS), and Unknown.
# (Unknown requires only that the units be defined.)
# The Editable flag must be Yes for this option to take affect,
# and is overridden internally if the user's license does not
# allow modification of projections (e.g. the OM Viewer).

#: Allow Geographic (GCS), Projected (PCS), and Unknown
COORDSYS_MODE_ALL = 0
#: Allow only Geographic (GCS)
COORDSYS_MODE_GCS = 1
#: Allow only Projected (PCS)
COORDSYS_MODE_PCS = 2
#: Allow only Geographic (GCS) and Projected (PCS)
COORDSYS_MODE_GCS_PCS = 3
#: Allow only Projected (PCS), or Unknown
COORDSYS_MODE_PCS_UNKNOWN = 4

#
# DAT_TYPE constants
#
# Type of files (grids, images) to support

#: Display only grid formats
DAT_TYPE_GRID = 0
#: Display only image formats
DAT_TYPE_IMAGE = 1
#: Displays both grids and image formats
DAT_TYPE_GRID_AND_IMAGE = 2

#
# FILE_FILTER constants
#
# File filters

#: All files              ``*.*``                  ANYWHERE
FILE_FILTER_ALL = 1
#: Geosoft Database       ``*.gdb``                LOCAL
FILE_FILTER_GDB = 2
#: Geosoft Executable     ``*.gx``                 GEOSOFT
FILE_FILTER_GX = 3
#: Geosoft Script         ``*.gs``                 BOTH
FILE_FILTER_GS = 4
#: Parameter files        ``*.ini``                GEOSOFT
FILE_FILTER_INI = 5
#: Oasis Menu files       ``*.omn``                GEOSOFT
FILE_FILTER_OMN = 6
#: Oasis View files       ``*.vu``                 LOCAL
FILE_FILTER_VU = 7
#: Oasis Map files        ``*.map``                LOCAL
FILE_FILTER_MAP = 8
#: Projection file        ``*.prj``                LOCAL
FILE_FILTER_PRJ = 9
#: Configuration file     ``*.con``                LOCAL
FILE_FILTER_CON = 10
#: Sushi MNU files        ``*.mnu``                GEOSOFT
FILE_FILTER_MNU = 11
#: PDF files              ``*.pdf``                GEOSOFT
FILE_FILTER_PDF = 12
#: Geosoft PLT files      ``*.plt``                LOCAL
FILE_FILTER_PLT = 13
#: Geosoft workspace      ``*.gws``                LOCAL
FILE_FILTER_GWS = 14
#: Aggregate              ``*.agg``                LOCAL
FILE_FILTER_AGG = 15
#: Color table            ``*.tbl``                GEOSOFT
FILE_FILTER_TBL = 16
#: Zone                   ``*.zon``                LOCAL
FILE_FILTER_ZON = 17
#: Image transform        ``*.itr``                LOCAL
FILE_FILTER_ITR = 18
#: AutoCAD DXF files      ``*.dxf``                LOCAL
FILE_FILTER_DXF = 19
#: TIFF files             ``*.tif``                LOCAL
FILE_FILTER_TIF = 20
#: Enhanced Metafies      ``*.emf``                LOCAL
FILE_FILTER_EMF = 21
#: Bitmap files           ``*.bmp``                LOCAL
FILE_FILTER_BMP = 22
#: ER Mapper LUT          ``*.lut``                GEOSOFT
FILE_FILTER_LUT = 23
#: PNG files              ``*.png``                LOCAL
FILE_FILTER_PNG = 24
#: JPG files              ``*.jpg``                LOCAL
FILE_FILTER_JPG = 25
#: PCX files              ``*.pcx``                LOCAL
FILE_FILTER_PCX = 26
#: GIF files              ``*.gif``                LOCAL
FILE_FILTER_GIF = 27
#: GRD files              ``*.grd``                LOCAL
FILE_FILTER_GRD = 28
#: ERS files              ``*.ers``                LOCAL
FILE_FILTER_ERS = 29
#: EPS files              ``*.eps``                LOCAL
FILE_FILTER_EPS = 30
#: ArcView Shape files    ``*.shp``                LOCAL
FILE_FILTER_SHP = 31
#: CGM files              ``*.cgm``                LOCAL
FILE_FILTER_CGM = 32
#: MapInfo Tab files      ``*.tab``                LOCAL
FILE_FILTER_TAB = 33
#: Software Components    Components           LOCAL
FILE_FILTER_COMPS = 34
#: MapInfo Tab files      ``*.tab``                LOCAL
FILE_FILTER_CSV = 35
#: Geosoft Project        ``*.gpf``                LOCAL
FILE_FILTER_GPF = 36
#: Geosoft Polygons       ``*.ply``                LOCAL
FILE_FILTER_PLY = 37
#: Scatter templates      ``*.stm``                LOCAL
FILE_FILTER_STM = 38
#: Triplot templates      ``*.ttm``                LOCAL
FILE_FILTER_TTM = 39
#: Geosoft XYZ files      ``*.xyz``                LOCAL
FILE_FILTER_XYZ = 40
#: Geosoft Bar file       ``*.geobar``             LOCAL
FILE_FILTER_BAR = 41
#: Geosoft License files   ``*.geosoft_license``   LOCAL
FILE_FILTER_GEOSOFT_LICENSE = 42
#: XML files              ``*.xml``                LOCAL
FILE_FILTER_XML = 43
#: GX.NET files           ``*.dll``                GEOSOFT
FILE_FILTER_GXNET = 44
#: ECW files              ``*.ecw``                LOCAL
FILE_FILTER_ECW = 45
#: J2K JPEG 2000 files    ``*.j2k``                LOCAL
FILE_FILTER_J2K = 46
#: JP2 JPEG 2000 files    ``*.jp2``                LOCAL
FILE_FILTER_JP2 = 47
#: acQuire parameters     ``*.sel``                LOCAL
FILE_FILTER_SEL = 48
#: SVG file               ``*.svg``                LOCAL
FILE_FILTER_SVG = 49
#: SVG Compressed file    ``*.svz``                LOCAL
FILE_FILTER_SVZ = 50
#: Warp file              ``*.wrp``                LOCAL
FILE_FILTER_WRP = 51
#: MAPPLOT file           ``*.con``                LOCAL
FILE_FILTER_MAPPLOT = 52
#: Surpac DTM files       ``*.dtm``                LOCAL
FILE_FILTER_DTM = 53
#: Geosoft Voxel          ``*.geosoft_voxel``      LOCAL
FILE_FILTER_VOXEL = 54
#: Map Template file      ``*.geosoft_maptemplate``      LOCAL
FILE_FILTER_MAPTEMPLATE = 55
#: Action Scripts         ``*.action``             LOCAL
FILE_FILTER_ACTION = 56
#: Datamine files         ``*.dm``                 LOCAL
FILE_FILTER_DM = 57
#: Google Earth KML       ``*.kml``                LOCAL
FILE_FILTER_KML = 58
#: Google Earth Compressed KML  ``*.kmz``          LOCAL
FILE_FILTER_KMZ = 59
#: Target parameter ini file for plans      ``*.inp``    LOCAL
FILE_FILTER_TARGET_PLAN = 60
#: Target parameter ini file for sections   ``*.ins``    LOCAL
FILE_FILTER_TARGET_SECTION = 61
#: Target parameter ini file for strip logs ``*.inl``    LOCAL
FILE_FILTER_TARGET_STRIPLOG = 62
#: Target parameter ini file for 3D plots   ``*.in3``    LOCAL
FILE_FILTER_TARGET_3D = 63
#: ArcGIS Layer files			 ``*.lyr``    LOCAL
FILE_FILTER_ARGIS_LYR = 64
#: ArcGIS Map Document files	 ``*.mxd``    LOCAL
FILE_FILTER_ARGIS_MXD = 65
#: GOCAD TSurf files			 ``*.ts``     LOCAL
FILE_FILTER_GOCAD_TS = 66
#: Geosoft list of items: names, values  ``*.lst``     LOCAL
FILE_FILTER_LST = 67
#: GM-SYS external coordinate system     ``*.ecs``     LOCAL
FILE_FILTER_ECS = 68
#: Target parameter ini file for fence sections   ``*.ins``    LOCAL
FILE_FILTER_TARGET_FENCE = 69
#: GM-SYS 3D model   ``*.geosoft_gmsys3d``    LOCAL
FILE_FILTER_GMS3D = 70
#: GEMCOM BT2 ``*.bt2`` LOCAL
FILE_FILTER_BT2 = 71
#: GEMCOM BPR ``*.bpr`` LOCAL
FILE_FILTER_BPR = 72
#: GEMCOM BPR2 ``*.bpr2`` LOCAL
FILE_FILTER_BPR2 = 73
#: Excel 97-2003 workbook		``*.xls``					LOCAL
FILE_FILTER_XLS = 74
#: Excel 2007 workbook 			``*.xlsx``				LOCAL
FILE_FILTER_XLSX = 75
#: Access 97-2003  				``*.mdb`` 				LOCAL
FILE_FILTER_MDB = 76
#: Access 2007 					``*.accdb`` 				LOCAL
FILE_FILTER_ACCDB = 77
#: Levelling intersection		``*.tbl``					LOCAL
FILE_FILTER_INTERSECTION_TBL = 78
#: UBC DCIP2D Conductivity model files ``*.con``		LOCAL
FILE_FILTER_UBC_CON = 79
#: UBC DCIP2D Chargeability model files ``*.chg``	LOCAL
FILE_FILTER_UBC_CHG = 80
#: UBC DCIP2D Mesh files		``*.msh``					LOCAL
FILE_FILTER_UBC_MSH = 81
#: UBC DCIP2D Mesh files		``*.dat``					LOCAL
FILE_FILTER_UBC_MSH_DAT = 82
#: UBC DCIP2D Topo files		``*.dat``					LOCAL
FILE_FILTER_UBC_TOPO_DAT = 83
#: UBC DCIP2D Topo files		``*.xyz``					LOCAL
FILE_FILTER_UBC_TOPO_XYZ = 84
#: XYZ Import Templates		      ``*.i0``				LOCAL
FILE_FILTER_XYZ_TEMPLATE_I0 = 85
#: Picodas Import Templates      ``*.i1``				LOCAL
FILE_FILTER_PICO_TEMPLATE_I1 = 86
#: Block Binary Import Templates ``*.i2``				LOCAL
FILE_FILTER_BB_TEMPLATE_I2 = 87
#: ASCII Import Templates		   ``*.i3``				LOCAL
FILE_FILTER_ASCII_TEMPLATE_I3 = 88
#: ODBC Import Templates		   ``*.i4``				LOCAL
FILE_FILTER_ODBC_TEMPLATE_I4 = 89
#: Math expression files		   ``*.exp``  			LOCAL
FILE_FILTER_EXP = 90
#: SEG-Y files							``*.sgy``  			LOCAL
FILE_FILTER_SEGY = 91
#: DAARC500 files						xYYMMDD 		   LOCAL
FILE_FILTER_DAARC500 = 92
#: Text files							``*.txt``  			LOCAL
FILE_FILTER_TXT = 93
#: Voxi									``*.geosoft_voxi``	LOCAL
FILE_FILTER_VOXEL_INVERSION = 94
#: GM-SYS Profile model file		``*.gms``	LOCAL
FILE_FILTER_GMS = 95
#: Geosoft 3D filter files			``*.flt3d``			LOCAL
FILE_FILTER_FLT3D = 96
#: Geosoft Resource Update Packages ``*.geosoft_resource_pack`` LOCAL
FILE_FILTER_RESOURCE_PACK = 97
#: Geostring files ``*.geosoft_string`` LOCAL
FILE_FILTER_GEOSTRING = 98
#: Geosurface files ``*.geosoft_surface`` LOCAL
FILE_FILTER_GEOSURFACE = 99
#: Geosoft `GX3DV <geosoft.gxapi.GX3DV>` ``*.geosoft_3dv`` LOCAL
FILE_FILTER_GEOSOFT3DV = 100
#: Geosoft Vector Voxel ``*.geosoft_vectorvoxel`` LOCAL
FILE_FILTER_VECTORVOXEL = 101
#: Geosoft Filters ``*.flt`` LOCAL
FILE_FILTER_FLT = 102
#: XYZ Export Templates ``*.o0`` LOCAL
FILE_FILTER_XYZ_TEMPLATE_O0 = 103
#: GM-SYS Profile model    ``*.geosoft_gmsys2d``   LOCAL
FILE_FILTER_GMS2D = 104
#: `GXIP <geosoft.gxapi.GXIP>` Database Template ``*.geosoft_ipdatabasetemplate`` LOCAL
FILE_FILTER_IP_DATABASE_TEMPLATE = 105
#: Geosoft Resource Module ``*.geosoft_resources``  LOCAL
FILE_FILTER_GEOSOFT_RESOURCE_MODULE = 106
#: Shell VT files     ``*.vt``        LOCAL
FILE_FILTER_VT = 107
#: Shell INT files     ``*.int``      LOCAL
FILE_FILTER_INT = 108
#: Shell SGT files     ``*.sgt``      LOCAL
FILE_FILTER_SGT = 109
#: Image Viewer files  ``*.imgview``  LOCAL
FILE_FILTER_IMGVIEW = 110
#: Zip files  ``*.zip``  LOCAL
FILE_FILTER_ZIP = 111
#: GPS Table ``*.tbl`` GEOSOFT
FILE_FILTER_GPS_TABLE = 112
#: Maptek Vulcan trianguilation file   ``*.tbl``     LOCAL
FILE_FILTER_VULCAN_TRIANGULATION = 113
#: Maptek Vulcan block model file       ``*.bmf``                        LOCAL
FILE_FILTER_VULCAN_BLOCK_MODEL = 114
#: Layout files  ``*.prjview``  LOCAL
FILE_FILTER_PRJVIEW = 115
#: Leapfrog model files  ``*.lfm``  LOCAL
FILE_FILTER_LEAPFROG_MODEL = 116
#: Reflex ioGAS files  ``*.gas``  LOCAL
FILE_FILTER_IOGAS = 117
#: ASEG ESF file  ``*.esf``  LOCAL
FILE_FILTER_ASEG_ESF = 118
#: Micro-g LaCoste MGS-6 gravity files  ``*.:class``:`DAT`  LOCAL
FILE_FILTER_LACOSTE_DAT = 119
#: Geosoft variogram file  ``*.var``  LOCAL
FILE_FILTER_VAR = 120
#: UKOOA data exchange file  ``*.p190``  LOCAL
FILE_FILTER_P190 = 121
#: UBC observation files ``*.dat``		LOCAL
FILE_FILTER_UBC_OBS_DAT = 122
#: UBC location files ``*.loc``		LOCAL
FILE_FILTER_UBC_LOC = 123
#: UBC model files ``*.mod``		LOCAL
FILE_FILTER_UBC_MOD = 124
#: UBC density model files ``*.den``		LOCAL
FILE_FILTER_UBC_DEN = 125
#: UBC susceptibility model files ``*.sus``		LOCAL
FILE_FILTER_UBC_SUS = 126
#: GOCAD voxet files ``*.vo``		LOCAL
FILE_FILTER_GOCAD_VOXET = 127
#: Scintrex gravity files  ``*.dat`  LOCAL
FILE_FILTER_SCINTREX_DAT = 128
#: Dump files  ``*.dmp`  LOCAL
FILE_FILTER_DMP = 129
#: Geosoft RAW gravity files  ``*.raw`  LOCAL
FILE_FILTER_RAW = 130
#: Data files  ``*.dat`  LOCAL
FILE_FILTER_DAT = 131

#
# FILE_FORM constants
#
# File Form Defines

#: Open a file
FILE_FORM_OPEN = 0
#: Save a file
FILE_FORM_SAVE = 1

#
# GS_DIRECTORY constants
#
# Geosoft predefined directory

#: None
GS_DIRECTORY_NONE = 0
#: Geosoft
GS_DIRECTORY_GEOSOFT = 1
#: Bin
GS_DIRECTORY_BIN = 2
#: Ger
GS_DIRECTORY_GER = 3
#: Omn
GS_DIRECTORY_OMN = 4
#: Tbl
GS_DIRECTORY_TBL = 5
#: Fonts
GS_DIRECTORY_FONTS = 6
#: Gx
GS_DIRECTORY_GX = 7
#: Gs
GS_DIRECTORY_GS = 8
#: Apps
GS_DIRECTORY_APPS = 9
#: Etc
GS_DIRECTORY_ETC = 10
#: Hlp
GS_DIRECTORY_HLP = 11
#: Gxdev
GS_DIRECTORY_GXDEV = 12
#: Component
GS_DIRECTORY_COMPONENT = 13
#: Csv
GS_DIRECTORY_CSV = 14
#: Lic
GS_DIRECTORY_LIC = 15
#: Ini
GS_DIRECTORY_INI = 16
#: Temp
GS_DIRECTORY_TEMP = 17
#: Uetc
GS_DIRECTORY_UETC = 18
#: Umaptemplate
GS_DIRECTORY_UMAPTEMPLATE = 19
#: Component scripts
GS_DIRECTORY_COMPONENT_SCRIPTS = 50
#: Component html
GS_DIRECTORY_COMPONENT_HTML = 51
#: Img
GS_DIRECTORY_IMG = 52
#: Bar
GS_DIRECTORY_BAR = 53
#: Gxnet
GS_DIRECTORY_GXNET = 54
#: Maptemplate
GS_DIRECTORY_MAPTEMPLATE = 55

#
# IMPCH_TYPE constants
#
# Import Chem defines

#: Data
IMPCH_TYPE_DATA = 0
#: Assay
IMPCH_TYPE_ASSAY = 1

#
# WINDOW_STATE constants
#
# Window State Options

#: Window restore
WINDOW_RESTORE = 0
#: Window minimize
WINDOW_MINIMIZE = 1
#: Window maximize
WINDOW_MAXIMIZE = 2

#
# XTOOL_ALIGN constants
#
# XTool docking alignment flags

#: Left
XTOOL_ALIGN_LEFT = 1
#: Top
XTOOL_ALIGN_TOP = 2
#: Right
XTOOL_ALIGN_RIGHT = 4
#: Bottom
XTOOL_ALIGN_BOTTOM = 8
#: Any
XTOOL_ALIGN_ANY = 15

#
# XTOOL_DOCK constants
#
# XTool default docking state

#: Top
XTOOL_DOCK_TOP = 1
#: Left
XTOOL_DOCK_LEFT = 2
#: Right
XTOOL_DOCK_RIGHT = 3
#: Bottom
XTOOL_DOCK_BOTTOM = 4
#: Float
XTOOL_DOCK_FLOAT = 5	

#
# GXHTTP Constants
# 

	

#
# GXIEXP Constants
# 

	

#
# GXINTERNET Constants
# 

	

#
# GXIP Constants
# 



#
# IP_ARRAY constants
#
# `GXIP <geosoft.gxapi.GXIP>` Array options

#: Dpdp
IP_ARRAY_DPDP = 0
#: Pldp
IP_ARRAY_PLDP = 1
#: Plpl
IP_ARRAY_PLPL = 2
#: Grad
IP_ARRAY_GRAD = 3
#: Wenner
IP_ARRAY_WENNER = 5
#: Schlumberger
IP_ARRAY_SCHLUMBERGER = 6
#: Unknown
IP_ARRAY_UNKNOWN = 7
#: 3d
IP_ARRAY_3D = 9
#: 3d pldp
IP_ARRAY_3D_PLDP = 10
#: 3d plpl
IP_ARRAY_3D_PLPL = 11

#
# IP_CHANNELS constants
#
# Channels to display

#: Displayed
IP_CHANNELS_DISPLAYED = 0
#: Selected
IP_CHANNELS_SELECTED = 1
#: All
IP_CHANNELS_ALL = 2

#
# IP_DOMAIN constants
#
# Types of Domains

#: None
IP_DOMAIN_NONE = -1
#: Time
IP_DOMAIN_TIME = 0
#: Frequency
IP_DOMAIN_FREQUENCY = 1
#: Both
IP_DOMAIN_BOTH = 2

#
# IP_DUPLICATE constants
#
# How to handle duplicates

#: Append
IP_DUPLICATE_APPEND = 0
#: Overwrite
IP_DUPLICATE_OVERWRITE = 1

#
# IP_FILTER constants
#
# Fraser Filters

#: Regular pant-leg filter::
#: 
#:        _!_    
#:       /*_*\\   n1
#:      /*/ \\*\\  n2`
#:     /*/   \\*\\ n3
#:        :  :
IP_FILTER_PANTLEG = 1
#: Regular pant-leg filter with top at first point::
#: 
#:        !  nscp:
#:       /*\\   n1
#:      /*_*\\  n2
#:     /*/ \\*\\ n3
#:       :  :
IP_FILTER_PANTLEGP = 2
#: Regular pyramid filter::
#: 
#:        _!_  maxn:
#:       /* *\\   n1
#:      /* * *\\  n2
#:     /* * * *\\ n3
#:        :  :
IP_FILTER_PYRIAMID = 3
#: Regular pyramid filter with peak on a point::
#: 
#:        !  maxn:
#:       /*\\   n1
#:      /* *\\  n2
#:     /* * *\\ n3
#:       :  :
IP_FILTER_PYRIAMIDP = 4

#
# IP_I2XIMPMODE constants
#
# Interpext Import Mode

#: Recreates the line from scratch.
IP_I2XIMPMODE_REPLACE = 0
#: Looks for matching Tx1 and N values and
#: replaces data in matching lines only.
IP_I2XIMPMODE_MERGE = 1

#
# IP_I2XINV constants
#
# Type of Inversion

#: Image
IP_I2XINV_IMAGE = 0
#: Zonge
IP_I2XINV_ZONGE = 1

#
# IP_LINES constants
#
# Lines to display

#: Displayed
IP_LINES_DISPLAYED = 0
#: Selected
IP_LINES_SELECTED = 1
#: All
IP_LINES_ALL = 2

#
# IP_PLOT constants
#
# Type of Plot

#: Pseudosection
IP_PLOT_PSEUDOSECTION = 0
#: Stackedsection
IP_PLOT_STACKEDSECTION = 1

#
# IP_QCTYPE constants
#
# Type of Measurement

#: Resistivity
IP_QCTYPE_RESISTIVITY = 0
#: `GXIP <geosoft.gxapi.GXIP>`
IP_QCTYPE_IP = 1

#
# IP_STACK_TYPE constants
#
# Spacing Types

#: Use map-based spacing, and preserve the directions of the
#: original lines by rotating the sections as desired to their true
#: locations. (At present only N-S and E-W sections are supported).
IP_STACK_TYPE_MAP = 0
#: Spaces the sections equally, with enough room to
#: guarantee no overlap with high N-values or closely spaced lines.
IP_STACK_TYPE_EQUAL = 1
#: Now the same as IP_STACK_MAP
IP_STACK_TYPE_GEOGRAPHIC = 2

#
# IP_STNSCALE constants
#
# Station Scaling

#: Station numbers become X or Y locations
IP_STNSCALE_NONE = 0
#: Multiply station numbers by the A spacing
IP_STNSCALE_ASPACE = 1
#: Multiply by an input value.
IP_STNSCALE_VALUE = 2
#: Look up locations from a CSV Line/Station/X/Y file
IP_STNSCALE_FILE = 3

#
# IP_SYS constants
#
# Instrument

#: Ipdata
IP_SYS_IPDATA = 0
#: Ip2
IP_SYS_IP2 = 1
#: Ip6
IP_SYS_IP6 = 2
#: Ip10
IP_SYS_IP10 = 3
#: Syscalr2
IP_SYS_SYSCALR2 = 4
#: Ipr11
IP_SYS_IPR11 = 5
#: Ipr12
IP_SYS_IPR12 = 6
#: Phoenix
IP_SYS_PHOENIX = 7
#: Phoenix v2
IP_SYS_PHOENIX_V2 = 8
#: Elrec pro
IP_SYS_ELREC_PRO = 9
#: Prosys ii
IP_SYS_PROSYS_II = 10

#
# IP_UBC_CONTROL constants
#
# Types of Domains

#: None
IP_UBC_CONTROL_NONE = -1
#: Default
IP_UBC_CONTROL_DEFAULT = 0
#: File
IP_UBC_CONTROL_FILE = 1
#: Value
IP_UBC_CONTROL_VALUE = 2
#: Length
IP_UBC_CONTROL_LENGTH = 3

#
# IP_PLDP_CONV constants
#
# Types of Domains

#: Close rx
IP_PLDP_CONV_CLOSE_RX = 0
#: Mid rx
IP_PLDP_CONV_MID_RX = 1
#: Distant rx
IP_PLDP_CONV_DISTANT_RX = 2	

#
# GXIPGUI Constants
# 

	

#
# GXKGRD Constants
# 

	

#
# GXLMSG Constants
# 

	

#
# GXMISC Constants
# 

	

#
# GXMSTK Constants
# 

	

#
# GXMVG Constants
# 



#
# MVG_DRAW constants
#
# `GXMVG <geosoft.gxapi.GXMVG>` draw define

#: Polyline
MVG_DRAW_POLYLINE = 0
#: Polygon
MVG_DRAW_POLYGON = 1

#
# MVG_GRID constants
#
# `GXMVG <geosoft.gxapi.GXMVG>` grid define

#: Dot
MVG_GRID_DOT = 0
#: Line
MVG_GRID_LINE = 1
#: Cross
MVG_GRID_CROSS = 2

#
# MVG_LABEL_BOUND constants
#
# `GXMVG <geosoft.gxapi.GXMVG>` label bound define

#: No
MVG_LABEL_BOUND_NO = 0
#: Yes
MVG_LABEL_BOUND_YES = 1

#
# MVG_LABEL_JUST constants
#
# `GXMVG <geosoft.gxapi.GXMVG>` label justification define

#: Top
MVG_LABEL_JUST_TOP = 0
#: Bottom
MVG_LABEL_JUST_BOTTOM = 1
#: Left
MVG_LABEL_JUST_LEFT = 2
#: Right
MVG_LABEL_JUST_RIGHT = 3

#
# MVG_LABEL_ORIENT constants
#
# `GXMVG <geosoft.gxapi.GXMVG>` label orientation

#: Horizontal
MVG_LABEL_ORIENT_HORIZONTAL = 0
#: Top right
MVG_LABEL_ORIENT_TOP_RIGHT = 1
#: Top left
MVG_LABEL_ORIENT_TOP_LEFT = 2

#
# MVG_SCALE constants
#
# `GXMVG <geosoft.gxapi.GXMVG>` scale define

#: Linear
MVG_SCALE_LINEAR = 0
#: Log
MVG_SCALE_LOG = 1
#: Loglinear
MVG_SCALE_LOGLINEAR = 2

#
# MVG_WRAP constants
#
# `GXMVG <geosoft.gxapi.GXMVG>` wrap define

#: No
MVG_WRAP_NO = 0
#: Yes
MVG_WRAP_YES = 1	

#
# GXPDF3D Constants
# 

	

#
# GXPGEXP Constants
# 

	

#
# GXPGU Constants
# 



#
# BLAKEY_TEST constants
#
# Types of BLAKEY tests

#: Oneside
BLAKEY_TEST_ONESIDE = 1
#: Twoside
BLAKEY_TEST_TWOSIDE = 2
#: Threeside
BLAKEY_TEST_THREESIDE = 3
#: Fourside
BLAKEY_TEST_FOURSIDE = 4

#
# PGU_CORR constants
#
# Correlation (must be synchronized with :ref:`ST2_CORRELATION`)

#: Simple correlation
PGU_CORR_SIMPLE = 0
#: Pearson's correlation (normalized to standard deviations)
PGU_CORR_PEARSON = 1

#
# PGU_DIRECTGRID constants
#
# Type of statistic to use on the data points in each cell.

#: Select the minimum value found in each cell
PGU_DIRECTGRID_MINIMUM = 0
#: Select the maximum value found in each cell
PGU_DIRECTGRID_MAXIMUM = 1
#: Select the mean of all values found in each cell
PGU_DIRECTGRID_MEAN = 2
#: The number of valid (non-dummy) items found in each cell
PGU_DIRECTGRID_ITEMS = 3

#
# PGU_DIRECTION constants
#
# Direction

#: Forward direction: Removes mean and standard deviation,
#: storing the values in the VVs.
PGU_FORWARD = 0
#: Backward direction: Applies mean and standard deviation
#: values in the VVs to the data.
PGU_BACKWARD = 1

#
# PGU_TRANS constants
#
# Transform methods for the columns

#: None
PGU_TRANS_NONE = 0
#: Log
PGU_TRANS_LOG = 1

#
# PGU_INTERP_ORDER constants
#
# Interpolation direction order

#: Xyz
PGU_INTERP_ORDER_XYZ = 0
#: Xzy
PGU_INTERP_ORDER_XZY = 1
#: Yxz
PGU_INTERP_ORDER_YXZ = 2
#: Yzx
PGU_INTERP_ORDER_YZX = 3
#: Zxy
PGU_INTERP_ORDER_ZXY = 4
#: Zyx
PGU_INTERP_ORDER_ZYX = 5	

#
# GXPRAGA3 Constants
# 

	

#
# GXPROJ Constants
# 



#
# COMMAND_ENV constants
#
# Command environments

#: Normal
COMMAND_ENV_NORMAL = 0
#: Executing from inside 3D Viewer
COMMAND_ENV_IN3DVIEWER = 1

#
# TOOL_TYPE constants
#
# Tool type defines

#: Geosoft created default tools
TOOL_TYPE_DEFAULT = 0
#: Auxiliary tools (including custom XTools)
TOOL_TYPE_AUXILIARY = 1
#: All tools
TOOL_TYPE_ALL = 2

#
# PROJ_DISPLAY constants
#
# How to display an object

#: Do not display the object
PROJ_DISPLAY_NO = 0
#: Display the object unless user set option not to
PROJ_DISPLAY_YES = 1
#: Always display the object
PROJ_DISPLAY_ALWAYS = 2	

#
# GXRGRD Constants
# 

	

#
# GXSEMPLOT Constants
# 



#
# SEMPLOT_GROUP_CLASS constants
#
# `GXSEMPLOT <geosoft.gxapi.GXSEMPLOT>` group class.

#: Semplot group class
SEMPLOT_GROUP_CLASS = "Semplot"

#
# SEMPLOT_EXPORT constants
#
# `GXSEMPLOT <geosoft.gxapi.GXSEMPLOT>` export type selection.

#: Exports Sample info channels, oxides/ratios, totals, extra channels.
SEMPLOT_EXPORT_NORMAL = 0
#: Exports Sample info, oxides/ratios, totals.
SEMPLOT_EXPORT_NOEXTRA = 1

#
# SEMPLOT_EXT constants
#
# `GXSEMPLOT <geosoft.gxapi.GXSEMPLOT>` file extension selection

#: Use for selection only. Selects both "Semplot" and "`GXCHIMERA <geosoft.gxapi.GXCHIMERA>`" type
#: files when creating LSTs etc.
SEMPLOT_EXT_ALL = 0
#: Read/write templates with extensions ".xyt", ".tri" and ".semtemplate"
#: Read/write overlays with extensions ".oly" and ".semoverlay"
SEMPLOT_EXT_SEMPLOT = 1
#: Read/write templates with extensions ".geosoft_template"
#: Read/write overlays with extensions ".geosoft_overlay"
SEMPLOT_EXT_CHIMERA = 2

#
# SEMPLOT_PLOT constants
#
# `GXSEMPLOT <geosoft.gxapi.GXSEMPLOT>` plot type selection.

#: Use for selection only. Selects both "XYPlot" and "TriPlot"
#: plots when creating LSTs etc.
SEMPLOT_PLOT_ALL = 0
#: Select XY (Scatter) plot.
SEMPLOT_PLOT_XYPLOT = 1
#: Select Tri (Triangular) plot.
SEMPLOT_PLOT_TRIPLOT = 2
#: Returned as an error status from some functions.
SEMPLOT_PLOT_UNKNOWN = 3	

#
# GXSHP Constants
# 



#
# SHP_GEOM_TYPE constants
#
# Shape file geometry types

#: Single (X, Y) point
SHP_GEOM_TYPE_POINT = 1
#: Arc (polyline) multiple (X, Y) points.
SHP_GEOM_TYPE_ARC = 3
#: Polygon. Multiple (X, Y) points.
SHP_GEOM_TYPE_POLYGON = 5
#: Single (X, Y, Z) point
SHP_GEOM_TYPE_POINTZ = 11
#: Arc (polyline) multiple (X, Y, Z) points.
SHP_GEOM_TYPE_ARCZ = 13
#: Polygon. Multiple (X, Y, Z) points.
SHP_GEOM_TYPE_POLYGONZ = 15	

#
# GXSQLSRV Constants
# 



#
# MFCSQL_DRIVER constants
#
# SQL Server Driver

#: No dialog box, Error if authentication parameters are wrong
MFCSQL_DRIVER_NOPROMPT = 0
#: Only shows dialog box if authentication parameters are wrong
MFCSQL_DRIVER_COMPLETE = 1
#: Always show dialog box, with option to change parameter
MFCSQL_DRIVER_PROMPT = 2
#: Same as `MFCSQL_DRIVER_COMPLETE <geosoft.gxapi.MFCSQL_DRIVER_COMPLETE>` except only missing parameters are editable
MFCSQL_DRIVER_COMPLETE_REQUIRED = 3	

#
# GXSTK Constants
# 



#
# STK_AXIS constants
#
# `GXSTK <geosoft.gxapi.GXSTK>` Axis defines

#: X Axis
STK_AXIS_X = 0
#: Y Axis
STK_AXIS_Y = 1

#
# STK_FLAG constants
#
# Stack flags

#: Profile
STK_FLAG_PROFILE = 0
#: Fid
STK_FLAG_FID = 1
#: Symbol
STK_FLAG_SYMBOL = 2
#: Xbar
STK_FLAG_XBAR = 3
#: Xlabel
STK_FLAG_XLABEL = 4
#: Xtitle
STK_FLAG_XTITLE = 5
#: Ybar
STK_FLAG_YBAR = 6
#: Ylabel
STK_FLAG_YLABEL = 7
#: Ytitle
STK_FLAG_YTITLE = 8
#: Grid1
STK_FLAG_GRID1 = 9
#: Grid2
STK_FLAG_GRID2 = 10

#
# STK_GRID constants
#
# Stack Grid define

#: Primary Grid
STK_GRID_PRIMARY = 0
#: Secondary Grid
STK_GRID_SECONDARY = 1	

#
# GXSTRINGS Constants
# 

	

#
# GXTC Constants
# 



#
# TC_OPT constants
#
# Optimization

#: (slow)    no optimization
TC_OPT_NONE = 0
#: (faster)  desampling and using qspline (4x4 points) interpolation
#: on coarser averaged grid
TC_OPT_MAX = 1

#
# TC_SURVEYTYPE constants
#
# Survey Type

#: Ground
TC_SURVEYTYPE_GROUND = 0
#: Shipborne
TC_SURVEYTYPE_SHIPBORNE = 1
#: Airborne
TC_SURVEYTYPE_AIRBORNE = 2

#
# GG_ELEMENT constants
#
# GG element

#: Gxx
GG_ELEMENT_XX = 0
#: Gyy
GG_ELEMENT_YY = 1
#: Gxy
GG_ELEMENT_XY = 2
#: Gxz
GG_ELEMENT_XZ = 3
#: Gyz
GG_ELEMENT_YZ = 4	

#
# GXTEST Constants
# 

	

#
# GXTIN Constants
# 

	

#
# GXTRND Constants
# 



#
# TRND_NODE constants
#
# Node to find

#: Trnd min
TRND_MIN = 0
#: Trnd max
TRND_MAX = 1	

#
# GXUNC Constants
# 



#
# UTF8 constants
#
# UTF-8 Defines

#: Maximum width of a single Unicode code point as a :ref:`UTF8` string, including terminator (5)
UTF8_MAX_CHAR = 5	

#
# GXVAU Constants
# 



#
# VAU_PRUNE constants
#
# Prune Options

#: Dummy
VAU_PRUNE_DUMMY = 0
#: Valid
VAU_PRUNE_VALID = 1	

#
# GXVVEXP Constants
# 

	

#
# GXVVU Constants
# 



#
# QC_CRITERION constants
#
# Criterion

#: 1
QC_CRITERION_1 = 0
#: 2
QC_CRITERION_2 = 1
#: 12
QC_CRITERION_12 = 2

#
# TEM_ARRAY constants
#
# Array Type

#: Verticalsounding
TEM_ARRAY_VERTICALSOUNDING = 0
#: Profiling
TEM_ARRAY_PROFILING = 1
#: Borehole
TEM_ARRAY_BOREHOLE = 2

#
# VV_DUP constants
#
# Duplicate handling mode

#: Average numeric values (for strings, same as `VV_DUP_1 <geosoft.gxapi.VV_DUP_1>`)
VV_DUP_AVERAGE = 0
#: Use first value of the pair
VV_DUP_1 = 1
#: Use second value of the pair
VV_DUP_2 = 2
#: Set to dummy
VV_DUP_DUMMY = 3
#: Set to "3" (cannot use with string data `GXVV <geosoft.gxapi.GXVV>`)
VV_DUP_SAMPLE = 4

#
# VV_XYDUP constants
#
# Sample handling

#: Average
VV_XYDUP_AVERAGE = 0
#: Sum
VV_XYDUP_SUM = 1

#
# VVU_CASE constants
#
# String case handling

#: Tolerant
VVU_CASE_TOLERANT = 0
#: Sensitive
VVU_CASE_SENSITIVE = 1

#
# VVU_CLIP constants
#
# Type of clipping

#: Clip replaces clipped values with a dummy.
VVU_CLIP_DUMMY = 0
#: Clip replaces clipped values with the limit.
VVU_CLIP_LIMIT = 1

#
# VVU_DUMMYREPEAT constants
#
# How to deal with repeats

#: Dummies all but first point.
VVU_DUMMYREPEAT_FIRST = 0
#: Dummies all but last point.
VVU_DUMMYREPEAT_LAST = 1
#: Dummies all but middle point.
VVU_DUMMYREPEAT_MIDDLE = 2

#
# VVU_INTERP constants
#
# Interpolation method to use

#: Nearest
VVU_INTERP_NEAREST = 1
#: Linear
VVU_INTERP_LINEAR = 2
#: Cubic
VVU_INTERP_CUBIC = 3
#: Akima
VVU_INTERP_AKIMA = 4
#: Predict
VVU_INTERP_PREDICT = 5

#
# VVU_INTERP_EDGE constants
#
# Interpolation method to use on edges

#: None
VVU_INTERP_EDGE_NONE = 0
#: Same
VVU_INTERP_EDGE_SAME = 1
#: Nearest
VVU_INTERP_EDGE_NEAREST = 2
#: Linear
VVU_INTERP_EDGE_LINEAR = 3

#
# VVU_LINE constants
#
# Line Types

#: Line 2 points
LINE_2_POINTS = 0
#: Line point azimuth
LINE_POINT_AZIMUTH = 1

#
# VVU_MASK constants
#
# Type of clipping

#: Mask `GXVV <geosoft.gxapi.GXVV>` is set to dummy at locations inside the `GXPLY <geosoft.gxapi.GXPLY>`.
VVU_MASK_INSIDE = 0
#: Mask `GXVV <geosoft.gxapi.GXVV>` is set to dummy at locations outside the `GXPLY <geosoft.gxapi.GXPLY>`.
VVU_MASK_OUTSIDE = 1

#
# VVU_MATCH constants
#
# Matching style

#: Entire string
VVU_MATCH_FULL_STRINGS = 0
#: Match the first part of a string.
VVU_MATCH_INPUT_LENGTH = 1

#
# VVU_MODE constants
#
# Statistic to select

#: Mean
VVU_MODE_MEAN = 0
#: Median
VVU_MODE_MEDIAN = 1
#: Maximum
VVU_MODE_MAXIMUM = 2
#: Minimum
VVU_MODE_MINIMUM = 3

#
# VVU_OFFSET constants
#
# Heading

#: Forward
VVU_OFFSET_FORWARD = 0
#: Backward
VVU_OFFSET_BACKWARD = 1
#: Right
VVU_OFFSET_RIGHT = 2
#: Left
VVU_OFFSET_LEFT = 3

#
# VVU_PRUNE constants
#
# Prune options

#: 0
VVU_PRUNE_DUMMY = 0
#: 1
VVU_PRUNE_VALID = 1

#
# VVU_SPL constants
#
# Spline types

#: Linear
VVU_SPL_LINEAR = 0
#: Cubic
VVU_SPL_CUBIC = 1
#: Akima
VVU_SPL_AKIMA = 2
#: Nearest
VVU_SPL_NEAREST = 3

#
# VVU_SRCHREPL_CASE constants
#
# Search and Replace handling of string case

#: Tolerant
VVU_SRCHREPL_CASE_TOLERANT = 0
#: Sensitive
VVU_SRCHREPL_CASE_SENSITIVE = 1	

### endblock Constants

### block ClassImports
# NOTICE: Do not edit anything here, it is generated code

__all__ = [

    'GXContext',
    'GX3DN',
    'GX3DV',
    'GXAGG',
    'GXBF',
    'GXDAT',
    'GXDATALINKD',
    'GXDATAMINE',
    'GXDB',
    'GXDBREAD',
    'GXDBWRITE',
    'GXDSEL',
    'GXE3DV',
    'GXEXT',


    'GXGEOSTRING',
    'GXGIS',
    'GXGRID3D',
    'GXHGD',
    'GXHXYZ',
    'GXIGRF',
    'GXIMG',
    'GXIMU',
    'GXIPJ',
    'GXITR',
    'GXLAYOUT',
    'GXLL2',
    'GXLPT',
    'GXLST',
    'GXLTB',
    'GXMAP',
    'GXMAPL',
    'GXMAPTEMPLATE',
    'GXMATH',
    'GXMESH',
    'GXMESHUTIL',
    'GXMETA',
    'GXMPLY',
    'GXMULTIGRID3D',
    'GXMULTIGRID3DUTIL',
    'GXMVIEW',
    'GXMVU',
    'GXMXD',
    'GXPAT',
    'GXPG',
    'GXPJ',
    'GXPLY',
    'GXRA',
    'GXREG',
    'GXSBF',
    'GXSEGYREADER',
    'GXST',
    'GXST2',
    'GXSTORAGEPROJECT',
    'GXSTR',
    'GXSURFACE',
    'GXSURFACEITEM',
    'GXSYS',
    'GXTB',
    'GXTPAT',
    'GXTR',
    'GXUSERMETA',
    'GXVA',
    'GXVECTOR3D',
    'GXVM',
    'GXVOX',
    'GXVOXD',
    'GXVOXE',
    'GXVULCAN',
    'GXVV',
    'GXWA',
    'GXACQUIRE',
    'GXARCDB',
    'GXARCDH',
    'GXARCMAP',
    'GXARCPY',
    'GXARCSYS',
    'GXBIGRID',
    'GXCHIMERA',
    'GXCOM',
    'GXCSYMB',
    'GXDGW',
    'GXDH',
    'GXDMPPLY',
    'GXDOCU',
    'GXDU',
    'GXDXFI',
    'GXEDB',
    'GXEDOC',
    'GXEMAP',
    'GXEMAPTEMPLATE',
    'GXEUL3',
    'GXEXP',
    'GXFFT',
    'GXFFT2',
    'GXFLT',
    'GXGD',
    'GXGER',
    'GXGMSYS',
    'GXGU',
    'GXGUI',
    'GXHTTP',
    'GXIEXP',
    'GXINTERNET',
    'GXIP',
    'GXIPGUI',
    'GXKGRD',
    'GXLMSG',
    'GXMISC',
    'GXMSTK',
    'GXMVG',
    'GXPDF3D',
    'GXPGEXP',
    'GXPGU',
    'GXPRAGA3',
    'GXPROJ',
    'GXRGRD',
    'GXSEMPLOT',
    'GXSHP',
    'GXSQLSRV',
    'GXSTK',
    'GXSTRINGS',
    'GXTC',
    'GXTEST',
    'GXTIN',
    'GXTRND',
    'GXUNC',
    'GXVAU',
    'GXVVEXP',
    'GXVVU',
]

from .GXContext import GXContext
from .GX3DN import GX3DN
from .GX3DV import GX3DV
from .GXAGG import GXAGG
from .GXBF import GXBF
from .GXDAT import GXDAT
from .GXDATALINKD import GXDATALINKD
from .GXDATAMINE import GXDATAMINE
from .GXDB import GXDB
from .GXDBREAD import GXDBREAD
from .GXDBWRITE import GXDBWRITE
from .GXDSEL import GXDSEL
from .GXE3DV import GXE3DV
from .GXEXT import GXEXT


from .GXGEOSTRING import GXGEOSTRING
from .GXGIS import GXGIS
from .GXGRID3D import GXGRID3D
from .GXHGD import GXHGD
from .GXHXYZ import GXHXYZ
from .GXIGRF import GXIGRF
from .GXIMG import GXIMG
from .GXIMU import GXIMU
from .GXIPJ import GXIPJ
from .GXITR import GXITR
from .GXLAYOUT import GXLAYOUT
from .GXLL2 import GXLL2
from .GXLPT import GXLPT
from .GXLST import GXLST
from .GXLTB import GXLTB
from .GXMAP import GXMAP
from .GXMAPL import GXMAPL
from .GXMAPTEMPLATE import GXMAPTEMPLATE
from .GXMATH import GXMATH
from .GXMESH import GXMESH
from .GXMESHUTIL import GXMESHUTIL
from .GXMETA import GXMETA
from .GXMPLY import GXMPLY
from .GXMULTIGRID3D import GXMULTIGRID3D
from .GXMULTIGRID3DUTIL import GXMULTIGRID3DUTIL
from .GXMVIEW import GXMVIEW
from .GXMVU import GXMVU
from .GXMXD import GXMXD
from .GXPAT import GXPAT
from .GXPG import GXPG
from .GXPJ import GXPJ
from .GXPLY import GXPLY
from .GXRA import GXRA
from .GXREG import GXREG
from .GXSBF import GXSBF
from .GXSEGYREADER import GXSEGYREADER
from .GXST import GXST
from .GXST2 import GXST2
from .GXSTORAGEPROJECT import GXSTORAGEPROJECT
from .GXSTR import GXSTR
from .GXSURFACE import GXSURFACE
from .GXSURFACEITEM import GXSURFACEITEM
from .GXSYS import GXSYS
from .GXTB import GXTB
from .GXTPAT import GXTPAT
from .GXTR import GXTR
from .GXUSERMETA import GXUSERMETA
from .GXVA import GXVA
from .GXVECTOR3D import GXVECTOR3D
from .GXVM import GXVM
from .GXVOX import GXVOX
from .GXVOXD import GXVOXD
from .GXVOXE import GXVOXE
from .GXVULCAN import GXVULCAN
from .GXVV import GXVV
from .GXWA import GXWA
from .GXACQUIRE import GXACQUIRE
from .GXARCDB import GXARCDB
from .GXARCDH import GXARCDH
from .GXARCMAP import GXARCMAP
from .GXARCPY import GXARCPY
from .GXARCSYS import GXARCSYS
from .GXBIGRID import GXBIGRID
from .GXCHIMERA import GXCHIMERA
from .GXCOM import GXCOM
from .GXCSYMB import GXCSYMB
from .GXDGW import GXDGW
from .GXDH import GXDH
from .GXDMPPLY import GXDMPPLY
from .GXDOCU import GXDOCU
from .GXDU import GXDU
from .GXDXFI import GXDXFI
from .GXEDB import GXEDB
from .GXEDOC import GXEDOC
from .GXEMAP import GXEMAP
from .GXEMAPTEMPLATE import GXEMAPTEMPLATE
from .GXEUL3 import GXEUL3
from .GXEXP import GXEXP
from .GXFFT import GXFFT
from .GXFFT2 import GXFFT2
from .GXFLT import GXFLT
from .GXGD import GXGD
from .GXGER import GXGER
from .GXGMSYS import GXGMSYS
from .GXGU import GXGU
from .GXGUI import GXGUI
from .GXHTTP import GXHTTP
from .GXIEXP import GXIEXP
from .GXINTERNET import GXINTERNET
from .GXIP import GXIP
from .GXIPGUI import GXIPGUI
from .GXKGRD import GXKGRD
from .GXLMSG import GXLMSG
from .GXMISC import GXMISC
from .GXMSTK import GXMSTK
from .GXMVG import GXMVG
from .GXPDF3D import GXPDF3D
from .GXPGEXP import GXPGEXP
from .GXPGU import GXPGU
from .GXPRAGA3 import GXPRAGA3
from .GXPROJ import GXPROJ
from .GXRGRD import GXRGRD
from .GXSEMPLOT import GXSEMPLOT
from .GXSHP import GXSHP
from .GXSQLSRV import GXSQLSRV
from .GXSTK import GXSTK
from .GXSTRINGS import GXSTRINGS
from .GXTC import GXTC
from .GXTEST import GXTEST
from .GXTIN import GXTIN
from .GXTRND import GXTRND
from .GXUNC import GXUNC
from .GXVAU import GXVAU
from .GXVVEXP import GXVVEXP
from .GXVVU import GXVVU
### endblock ClassImports


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer