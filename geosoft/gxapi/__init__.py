### extends 'init_empty.py'

### block Header
# NOTICE: The code generator will not replace the code in this block

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


class GXError(RuntimeError):
    """
    A subclass of `RuntimeError <https://docs.python.org/3/library/exceptions.html#RuntimeError>`_ which is raised whenever 
    a GX Python API call encounters an error. Often the message string of these errors are informative to the user (e.g. File 
    'x' is locked in another application) but there could be cases where this is not the case. In most cases an attribute, 
    :attr:`number`, is also available on the exception object that matches the number in the :code:`geosoft.ger` file.
    These numbers instead of the string (which could change or even be translated) should be used to identify and handle
    very specific exceptions.

    .. versionadded:: 9.1
    """
    pass
    
### endblock Header

### block Constants
# NOTICE: Do not edit anything here, it is generated code
# BEGIN GXGEOSOFT Constants
# NOTICE: Do not edit anything here, it is generated code



CRC_INIT_VALUE = 4294967295



DATE_FORMAT_YYYYMMDD = 1

DATE_FORMAT_DDMMYYYY = 2

DATE_FORMAT_MMDDYYYY = 3



iDUMMY = -2147483647

rDUMMY = -1.0E32



GS_S1MX = 127

GS_S1MN = -126

GS_S1DM = -127

GS_U1MX = 254

GS_U1MN = 0

GS_U1DM = 255

GS_S2MX = 32767

GS_S2MN = -32766

GS_S2DM = -32767

GS_U2MX = 65534

GS_U2MN = 0

GS_U2DM = 65535

GS_S4MX = 2147483647

GS_S4MN = -2147483646

GS_S4DM = -2147483647

GS_U4MX = 0xFFFFFFFE

GS_U4MN = 0x00000000

GS_U4DM = 0xFFFFFFFF

GS_S8MX = 0x7FFFFFFFFFFFFFFF

GS_S8MN = 0x8000000000000001

GS_S8DM = 0x8000000000000000

GS_U8MX = 0xFFFFFFFFFFFFFFFE

GS_U8MN = 0x0000000000000000

GS_U8DM = 0xFFFFFFFFFFFFFFFF

GS_R4MX = 1.0E32

GS_R4MN = -0.9E32

GS_R4DM = -1.0E32

GS_R8MX = 1.0E32

GS_R8MN = -0.9E+32

GS_R8DM = -1.0E+32

GS_R4EPSILON = 1.0E-32

GS_R8EPSILON = 1.0E-32



iMIN = -2147483646

iMAX = 2147483647

rMIN = -0.9E32

rMAX = 1.0E32



STR_DEFAULT = 128

STR_DEFAULT_SHORT = 64

STR_DEFAULT_LONG = 1024

STR_ERROR = 2048

STR_VERY_LONG = 16384

STR_VIEW = 2080

STR_GROUP = 1040

STR_VIEW_GROUP = 2080

STR_FILE = 1040

STR_MULTI_FILE = 16384

STR_DB_SYMBOL = 64

STR_GXF = 160

STR_MAX_PATH = 1040

STR_MULTI_PATH = 16384

GS_MAX_PATH = 1040

GS_MULTI_PATH = 16384



GS_INT = 0

GS_REAL = 1



FORMAT_DECIMAL = 0

FORMAT_SIG_DIG = 5

FORMAT_EXP = 1

FORMAT_TIME_COLON = 2

FORMAT_TIME_HMS = 8

FORMAT_TIME_HHMMSS = 9

FORMAT_DATE_YYYYMMDD = 3

FORMAT_DATE_DDMMYYYY = 6

FORMAT_DATE_MMDDYYYY = 7

FORMAT_GEOGRAPHIC = 4

FORMAT_GEOGRAPHIC_1 = 10

FORMAT_GEOGRAPHIC_2 = 11

FORMAT_GEOGRAPHIC_3 = 12



GS_BYTE = 0

GS_USHORT = 1

GS_SHORT = 2

GS_LONG = 3

GS_FLOAT = 4

GS_DOUBLE = 5

GS_UBYTE = 6

GS_ULONG = 7

GS_LONG64 = 8

GS_ULONG64 = 9

GS_FLOAT3D = 10

GS_DOUBLE3D = 11

GS_FLOAT2D = 12

GS_DOUBLE2D = 13

GS_MAXTYPE = 13

GS_TYPE_DEFAULT = -32767



SYS_CRYPT_LICENSE_KEY = "{***LICENSE_KEY***}"

SYS_CRYPT_COMPUTER_ID = "{***COMPUTER_ID***}"

SYS_CRYPT_GLOBAL_ID = "{***GLOBAL_COMPUTER_ID***}"



TIME_FORMAT_COLON = 1

TIME_FORMAT_HMS = 2

	

# BEGIN GXGEOSOFT Constants

# BEGIN GX3DN Constants
# NOTICE: Do not edit anything here, it is generated code

	

# BEGIN GX3DN Constants

# BEGIN GXVV Constants
# NOTICE: Do not edit anything here, it is generated code



VV_DOUBLE_CRC_BITS_EXACT = 0

VV_DOUBLE_CRC_BITS_DEFAULT = 10

VV_DOUBLE_CRC_BITS_MAX = 51



VV_FLOAT_CRC_BITS_EXACT = 0

VV_FLOAT_CRC_BITS_DEFAULT = 7

VV_FLOAT_CRC_BITS_MAX = 22



VV_LOG_BASE_10 = 0

VV_LOG_BASE_E = 1



VV_LOG_NEGATIVE_NO = 0

VV_LOG_NEGATIVE_YES = 1



VV_LOOKUP_EXACT = 0

VV_LOOKUP_NEAREST = 1

VV_LOOKUP_INTERPOLATE = 2

VV_LOOKUP_NEARESTCLOSE = 3

VV_LOOKUP_INTERPCLOSE = 4



VV_MASK_INSIDE = 0

VV_MASK_OUTSIDE = 1



VV_ORDER_NONE = 0

VV_ORDER_INCREASING = 1

VV_ORDER_DECREASING = 2



VV_SORT_ASCENDING = 0

VV_SORT_DESCENDING = 1



VV_WINDOW_DUMMY = 0

VV_WINDOW_LIMIT = 1

	

# BEGIN GXVV Constants

### endblock Constants

### block ClassImports
# NOTICE: Do not edit anything here, it is generated code

__all__ = [

    'GX3DN',
    'GXVV',
]


from .GX3DN import GX3DN
from .GXVV import GXVV
### endblock ClassImports


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer