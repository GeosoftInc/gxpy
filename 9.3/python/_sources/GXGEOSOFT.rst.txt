
.. _GXGEOSOFT:

   

GXGEOSOFT class
==================================

This is not a class but a collection of global defines. It
is used by all functions.

.. _CRC_INIT_VALUE:

CRC_INIT_VALUE constant
-----------------------------------------------------------------------


.. autoattribute:: geosoft.gxapi.CRC_INIT_VALUE

::

   Initial value for starting a CRC 

.. _DATE_FORMAT:

DATE_FORMAT constants
-----------------------------------------------------------------------

::

   Old Date formats 

.. autoattribute:: geosoft.gxapi.DATE_FORMAT_YYYYMMDD

::

   Standard Date (YYYY/MM/DD, YY/MM/DD, YYYYMMDD or YYMMDD, space or / delimited) 

.. autoattribute:: geosoft.gxapi.DATE_FORMAT_DDMMYYYY

::

   Date (DD/MM/YYYY or DD/MM/YY century 20 if YY>50, DISC compliant) 

.. autoattribute:: geosoft.gxapi.DATE_FORMAT_MMDDYYYY

::

   Date (MM/DD/YYYY or MM/DD/YY century 19) 

.. _GEO_DUMMY:

GEO_DUMMY constants
-----------------------------------------------------------------------

::

   Special numbers indicating NULLL 

.. autoattribute:: geosoft.gxapi.iDUMMY

::

   Integer Dummy (-2147483647) 

.. autoattribute:: geosoft.gxapi.rDUMMY

::

   Floating Point Dummy (-1.0E32) 

.. _GEO_FULL_LIMITS:

GEO_FULL_LIMITS constants
-----------------------------------------------------------------------

::

   Data ranges of all Geosoft types 

.. autoattribute:: geosoft.gxapi.GS_S1MX

::

   (signed char   )   127 

.. autoattribute:: geosoft.gxapi.GS_S1MN

::

   (signed char   )  -126 

.. autoattribute:: geosoft.gxapi.GS_S1DM

::

   (signed char   )  -127 

.. autoattribute:: geosoft.gxapi.GS_U1MX

::

   (unsigned char )   254U 

.. autoattribute:: geosoft.gxapi.GS_U1MN

::

   (unsigned char )   0U 

.. autoattribute:: geosoft.gxapi.GS_U1DM

::

   (unsigned char )   255U 

.. autoattribute:: geosoft.gxapi.GS_S2MX

::

   (short         )   32767 

.. autoattribute:: geosoft.gxapi.GS_S2MN

::

   (short         )  -32766 

.. autoattribute:: geosoft.gxapi.GS_S2DM

::

   (short         )  -32767 

.. autoattribute:: geosoft.gxapi.GS_U2MX

::

   (unsigned short)   65534U 

.. autoattribute:: geosoft.gxapi.GS_U2MN

::

   (unsigned short)   0U 

.. autoattribute:: geosoft.gxapi.GS_U2DM

::

   (unsigned short)   65535U 

.. autoattribute:: geosoft.gxapi.GS_S4MX

::

   2147483647L 

.. autoattribute:: geosoft.gxapi.GS_S4MN

::

   -2147483646L 

.. autoattribute:: geosoft.gxapi.GS_S4DM

::

   -2147483647L 

.. autoattribute:: geosoft.gxapi.GS_U4MX

::

   (unsigned long )   0xFFFFFFFE 

.. autoattribute:: geosoft.gxapi.GS_U4MN

::

   (unsigned long )   0x00000000 

.. autoattribute:: geosoft.gxapi.GS_U4DM

::

   (unsigned long )   0xFFFFFFFF 

.. autoattribute:: geosoft.gxapi.GS_S8MX

::

   (__GS_INT64    )   0x7FFFFFFFFFFFFFFF 

.. autoattribute:: geosoft.gxapi.GS_S8MN

::

   (__GS_INT64    )   0x8000000000000001 

.. autoattribute:: geosoft.gxapi.GS_S8DM

::

   (__GS_INT64    )   0x8000000000000000 

.. autoattribute:: geosoft.gxapi.GS_U8MX

::

   (__GS_UINT64   )   0xFFFFFFFFFFFFFFFE 

.. autoattribute:: geosoft.gxapi.GS_U8MN

::

   (__GS_UINT64   )   0x0000000000000000 

.. autoattribute:: geosoft.gxapi.GS_U8DM

::

   (__GS_UINT64   )   0xFFFFFFFFFFFFFFFF 

.. autoattribute:: geosoft.gxapi.GS_R4MX

::

   (float         )   1.0E32   (In C these must be declared as external constants:) 

.. autoattribute:: geosoft.gxapi.GS_R4MN

::

   (float         )  -0.9E32     const float r4min=(float)-0.9E32, 

.. autoattribute:: geosoft.gxapi.GS_R4DM

::

   
   					(float         )  -1.0E32                 r4max=(float)1.0E32,
   r4dum=(float)-1.0E32;
   				 

.. autoattribute:: geosoft.gxapi.GS_R8MX

::

   (double        )   1.0E32 

.. autoattribute:: geosoft.gxapi.GS_R8MN

::

   (double        )  -0.9E32 

.. autoattribute:: geosoft.gxapi.GS_R8DM

::

   (double        )  -1.0E32 

.. autoattribute:: geosoft.gxapi.GS_R4EPSILON

::

   (float         )   1.0E-32 

.. autoattribute:: geosoft.gxapi.GS_R8EPSILON

::

   (double        )   1.0E-32 

.. _GEO_LIMITS:

GEO_LIMITS constants
-----------------------------------------------------------------------

::

   Data ranges of numbers 

.. autoattribute:: geosoft.gxapi.iMIN

::

   Smallest Integer (-2147483646) 

.. autoattribute:: geosoft.gxapi.iMAX

::

   Largest Integer (2147483647) 

.. autoattribute:: geosoft.gxapi.rMIN

::

   Smallest Floating Point (-0.9E32) 

.. autoattribute:: geosoft.gxapi.rMAX

::

   Largest Floating Point (1.0E32) 

.. _GEO_STRING_SIZE:

GEO_STRING_SIZE constants
-----------------------------------------------------------------------

::

   
   				Default string sized for different uses
   GX's must use these unless there is a
   very good reason not to. The path strings
   here are generally larger than what is possible
   in the OS, but it is defined as such for Unicode
   conversion reasons.
   			 

.. autoattribute:: geosoft.gxapi.STR_DEFAULT

::

   Default Size for almost everything (128 characters) 

.. autoattribute:: geosoft.gxapi.STR_DEFAULT_SHORT

::

   Default Size for a short string (64 characters) 

.. autoattribute:: geosoft.gxapi.STR_DEFAULT_LONG

::

   Default Size for a long string (1024 characters) 

.. autoattribute:: geosoft.gxapi.STR_ERROR

::

   Default Size for an error string (2048 characters) 

.. autoattribute:: geosoft.gxapi.STR_VERY_LONG

::

   Default Size for a long string (16384 characters) 

.. autoattribute:: geosoft.gxapi.STR_VIEW

::

   Name of a View (2080) 

.. autoattribute:: geosoft.gxapi.STR_GROUP

::

   Name of a Group (1040) 

.. autoattribute:: geosoft.gxapi.STR_VIEW_GROUP

::

   Combined View/Group Name (2080) 

.. autoattribute:: geosoft.gxapi.STR_FILE

::

   Name of a file (1040) 

.. autoattribute:: geosoft.gxapi.STR_MULTI_FILE

::

   Name of multiple files (16384) 

.. autoattribute:: geosoft.gxapi.STR_DB_SYMBOL

::

   Name of database symbol (64) 

.. autoattribute:: geosoft.gxapi.STR_GXF

::

   Size of strings for GXF projection info (160). 

.. autoattribute:: geosoft.gxapi.STR_MAX_PATH

::

   Maximum path length (1040) 

.. autoattribute:: geosoft.gxapi.STR_MULTI_PATH

::

   Multi-file path (16384) 

.. autoattribute:: geosoft.gxapi.GS_MAX_PATH

::

   Same as STR_FILE 

.. autoattribute:: geosoft.gxapi.GS_MULTI_PATH

::

   Same as STR_MULTI_FILE 

.. _GEO_VAR:

GEO_VAR constants
-----------------------------------------------------------------------

::

   
   				Variable types.
   Use -X for strings of X length
   			 

.. autoattribute:: geosoft.gxapi.GS_INT

::

   Integer (long) 

.. autoattribute:: geosoft.gxapi.GS_REAL

::

   Floating Point (double) 

.. _GS_FORMATS:

GS_FORMATS constants
-----------------------------------------------------------------------

::

   
   				Special use data types. String are indicated by a
   negative maximum string length (including NULL).
   			 

.. autoattribute:: geosoft.gxapi.FORMAT_DECIMAL

::

   Standard numbers (-134.534) 

.. autoattribute:: geosoft.gxapi.FORMAT_SIG_DIG

::

   Decimals imply number of significant digits 

.. autoattribute:: geosoft.gxapi.FORMAT_EXP

::

   Exponential notation (-1.345e45) 

.. autoattribute:: geosoft.gxapi.FORMAT_TIME_COLON

::

   Standard Time (HH:MM:SS.SSSS) 

.. autoattribute:: geosoft.gxapi.FORMAT_TIME_HMS

::

   Time (HH.MMSSSSSSS) 

.. autoattribute:: geosoft.gxapi.FORMAT_TIME_HHMMSS

::

   Time (HHMMSS) 

.. autoattribute:: geosoft.gxapi.FORMAT_DATE_YYYYMMDD

::

   Standard Date (YYYY/MM/DD, YY/MM/DD, YYYYMMDD or YYMMDD, space or / delimited) 

.. autoattribute:: geosoft.gxapi.FORMAT_DATE_DDMMYYYY

::

   Date (DD/MM/YYYY or DD/MM/YY century 20 if YY>50, DISC compliant) 

.. autoattribute:: geosoft.gxapi.FORMAT_DATE_MMDDYYYY

::

   Date (MM/DD/YYYY or MM/DD/YY century 19) 

.. autoattribute:: geosoft.gxapi.FORMAT_GEOGRAPHIC

::

   Standard Geographical (DEG.MM.SS.SSS) 

.. autoattribute:: geosoft.gxapi.FORMAT_GEOGRAPHIC_1

::

   GeoGraph (DEG:MM:SS.SSS) 

.. autoattribute:: geosoft.gxapi.FORMAT_GEOGRAPHIC_2

::

   GeoGraph (DEG.MMSSSSS) 

.. autoattribute:: geosoft.gxapi.FORMAT_GEOGRAPHIC_3

::

   GeoGraph (DEGMMmmmm or DEGMM.mmmm or DEG.MM.mmmm)  (mmmm: decimal minute) 

.. _GS_TYPES:

GS_TYPES constants
-----------------------------------------------------------------------

::

   
   				Special use data types. String are indicated by a
   negative maximum string length (including NULL).
   			 

.. autoattribute:: geosoft.gxapi.GS_BYTE

::

   Signed Byte 

.. autoattribute:: geosoft.gxapi.GS_USHORT

::

   Unsigned Short 

.. autoattribute:: geosoft.gxapi.GS_SHORT

::

   Signed Short 

.. autoattribute:: geosoft.gxapi.GS_LONG

::

   Signed Long 

.. autoattribute:: geosoft.gxapi.GS_FLOAT

::

   32-Bit floating point 

.. autoattribute:: geosoft.gxapi.GS_DOUBLE

::

   64-Bit floating point 

.. autoattribute:: geosoft.gxapi.GS_UBYTE

::

   Unsigned byte 

.. autoattribute:: geosoft.gxapi.GS_ULONG

::

   Unsigned Long 

.. autoattribute:: geosoft.gxapi.GS_LONG64

::

   64-Bit signed long 

.. autoattribute:: geosoft.gxapi.GS_ULONG64

::

   64-Bit unsigned long 

.. autoattribute:: geosoft.gxapi.GS_FLOAT3D

::

   3 x 32-Bit floating point 

.. autoattribute:: geosoft.gxapi.GS_DOUBLE3D

::

   3 x 64-Bit floating point 

.. autoattribute:: geosoft.gxapi.GS_FLOAT2D

::

   2 x 32-Bit floating point 

.. autoattribute:: geosoft.gxapi.GS_DOUBLE2D

::

   2 x 64-Bit floating point 

.. autoattribute:: geosoft.gxapi.GS_MAXTYPE

::

   Maximum supported type (GS_DOUBLE2D) 

.. autoattribute:: geosoft.gxapi.GS_TYPE_DEFAULT

::

   Default. Can be used only when a method specifically allows a default type. 

.. _SYS_CRYPT_KEY:

SYS_CRYPT_KEY constants
-----------------------------------------------------------------------

::

   Special Encryption Keys 

.. autoattribute:: geosoft.gxapi.SYS_CRYPT_LICENSE_KEY

::

   Using the current license key 

.. autoattribute:: geosoft.gxapi.SYS_CRYPT_COMPUTER_ID

::

   Use the current computer ID 

.. autoattribute:: geosoft.gxapi.SYS_CRYPT_GLOBAL_ID

::

   Use the non-changing computer ID 

.. _TIME_FORMAT:

TIME_FORMAT constants
-----------------------------------------------------------------------

::

   Old Time formats 

.. autoattribute:: geosoft.gxapi.TIME_FORMAT_COLON

::

   Standard Time (HH:MM:SS.SSSS) 

.. autoattribute:: geosoft.gxapi.TIME_FORMAT_HMS

::

   Time (HH.MMSSSSSSS) 

	