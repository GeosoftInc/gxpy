
.. _GXDB:

 
GXDB class
==================================

.. autoclass:: geosoft.gxapi.GXDB
   :members:

.. _DB_ACTIVITY_BLOB:

DB_ACTIVITY_BLOB constant
-----------------------------------------------------------------------


.. autoattribute:: geosoft.gxapi.DB_ACTIVITY_BLOB

::

   Activity Blob 

.. _DB_CATEGORY_BLOB:

DB_CATEGORY_BLOB constants
-----------------------------------------------------------------------

::

   Blob Categories 

.. autoattribute:: geosoft.gxapi.DB_CATEGORY_BLOB_NORMAL


.. _DB_CATEGORY_CHAN:

DB_CATEGORY_CHAN constants
-----------------------------------------------------------------------

::

   
   				Channel Categories
   				For STRING type channels, use negative integers
   				to specify channel width. For example, use -10
   				to define a string channel with up to 10 characters.
   				Use the GS_SIMPLE_TYPE() macro to convert to INT,REAL or string.
   			 

.. autoattribute:: geosoft.gxapi.DB_CATEGORY_CHAN_BYTE


.. autoattribute:: geosoft.gxapi.DB_CATEGORY_CHAN_USHORT


.. autoattribute:: geosoft.gxapi.DB_CATEGORY_CHAN_SHORT


.. autoattribute:: geosoft.gxapi.DB_CATEGORY_CHAN_LONG


.. autoattribute:: geosoft.gxapi.DB_CATEGORY_CHAN_FLOAT


.. autoattribute:: geosoft.gxapi.DB_CATEGORY_CHAN_DOUBLE


.. autoattribute:: geosoft.gxapi.DB_CATEGORY_CHAN_UBYTE


.. autoattribute:: geosoft.gxapi.DB_CATEGORY_CHAN_ULONG


.. autoattribute:: geosoft.gxapi.DB_CATEGORY_CHAN_LONG64


.. autoattribute:: geosoft.gxapi.DB_CATEGORY_CHAN_ULONG64


.. _DB_CATEGORY_LINE:

DB_CATEGORY_LINE constants
-----------------------------------------------------------------------

::

   Line Categories 

.. autoattribute:: geosoft.gxapi.DB_CATEGORY_LINE_FLIGHT


.. autoattribute:: geosoft.gxapi.DB_CATEGORY_LINE_GROUP


.. autoattribute:: geosoft.gxapi.DB_CATEGORY_LINE_NORMAL

::

   Same as DB_CATEGORY_LINE_FLIGHT 

.. _DB_CATEGORY_USER:

DB_CATEGORY_USER constants
-----------------------------------------------------------------------

::

   User Categories 

.. autoattribute:: geosoft.gxapi.DB_CATEGORY_USER_NORMAL


.. _DB_CHAN_FORMAT:

DB_CHAN_FORMAT constants
-----------------------------------------------------------------------

::

   Channel formats 

.. autoattribute:: geosoft.gxapi.DB_CHAN_FORMAT_NORMAL


.. autoattribute:: geosoft.gxapi.DB_CHAN_FORMAT_EXP


.. autoattribute:: geosoft.gxapi.DB_CHAN_FORMAT_TIME


.. autoattribute:: geosoft.gxapi.DB_CHAN_FORMAT_DATE


.. autoattribute:: geosoft.gxapi.DB_CHAN_FORMAT_GEOGR


.. autoattribute:: geosoft.gxapi.DB_CHAN_FORMAT_SIGDIG


.. autoattribute:: geosoft.gxapi.DB_CHAN_FORMAT_HEX


.. _DB_CHAN_PROTECTION:

DB_CHAN_PROTECTION constants
-----------------------------------------------------------------------

::

   Channel Read-only Protection Status 

.. autoattribute:: geosoft.gxapi.DB_CHAN_UNPROTECTED


.. autoattribute:: geosoft.gxapi.DB_CHAN_PROTECTED


.. _DB_CHAN_SYMBOL:

DB_CHAN_SYMBOL constants
-----------------------------------------------------------------------

::

   Channel symbol for special channels 

.. autoattribute:: geosoft.gxapi.DB_CHAN_X


.. autoattribute:: geosoft.gxapi.DB_CHAN_Y


.. autoattribute:: geosoft.gxapi.DB_CHAN_Z


.. _DB_COMP:

DB_COMP constants
-----------------------------------------------------------------------

::

   Supported compression levels 

.. autoattribute:: geosoft.gxapi.DB_COMP_NONE


.. autoattribute:: geosoft.gxapi.DB_COMP_SPEED


.. autoattribute:: geosoft.gxapi.DB_COMP_SIZE


.. _DB_COORDPAIR:

DB_COORDPAIR constants
-----------------------------------------------------------------------


.. autoattribute:: geosoft.gxapi.DB_COORDPAIR_NONE


.. autoattribute:: geosoft.gxapi.DB_COORDPAIR_X


.. autoattribute:: geosoft.gxapi.DB_COORDPAIR_Y


.. _DB_GROUP_CLASS_SIZE:

DB_GROUP_CLASS_SIZE constant
-----------------------------------------------------------------------


.. autoattribute:: geosoft.gxapi.DB_GROUP_CLASS_SIZE

::

   Class name max size 

.. _DB_INFO:

DB_INFO constants
-----------------------------------------------------------------------

::

   Integer Database Information 

.. autoattribute:: geosoft.gxapi.DB_INFO_BLOBS_MAX

::

   Maximum Number of Blobs in the Database 

.. autoattribute:: geosoft.gxapi.DB_INFO_LINES_MAX

::

   Maximum number of lines in the database 

.. autoattribute:: geosoft.gxapi.DB_INFO_CHANS_MAX

::

   Maximum Number of Channels in the Database 

.. autoattribute:: geosoft.gxapi.DB_INFO_USERS_MAX

::

   Maximum number of Users 

.. autoattribute:: geosoft.gxapi.DB_INFO_BLOBS_USED

::

   Number of Blobs currently used 

.. autoattribute:: geosoft.gxapi.DB_INFO_LINES_USED

::

   Number of Lines currently used 

.. autoattribute:: geosoft.gxapi.DB_INFO_CHANS_USED

::

   Number of Channels currently used 

.. autoattribute:: geosoft.gxapi.DB_INFO_USERS_USED

::

   Number of Users in the database 

.. autoattribute:: geosoft.gxapi.DB_INFO_PAGE_SIZE

::

   Size of the smallest database block in bytes 

.. autoattribute:: geosoft.gxapi.DB_INFO_DATA_SIZE

::

   Number of Blocks in Entire Database 

.. autoattribute:: geosoft.gxapi.DB_INFO_LOST_SIZE

::

   Number of Lost Blocks in the Database 

.. autoattribute:: geosoft.gxapi.DB_INFO_FREE_SIZE

::

   Number of Free Blocks in the Database 

.. autoattribute:: geosoft.gxapi.DB_INFO_COMP_LEVEL

::

   Compression Level in use 

.. autoattribute:: geosoft.gxapi.DB_INFO_BLOB_SIZE

::

   Number of pages given to blobs 

.. autoattribute:: geosoft.gxapi.DB_INFO_FILE_SIZE

::

   Entire Size of File (in kbytes) 

.. autoattribute:: geosoft.gxapi.DB_INFO_INDEX_SIZE

::

   Size of Index (in kbytes) 

.. autoattribute:: geosoft.gxapi.DB_INFO_MAX_BLOCK_SIZE

::

   Naximum number of bytes in a block 

.. autoattribute:: geosoft.gxapi.DB_INFO_CHANGESLOST

::

   Will changes to this database be lost when this database is closed? 

.. _DB_LINE_LABEL_FORMAT:

DB_LINE_LABEL_FORMAT constants
-----------------------------------------------------------------------

::

   Line Label Formats 

.. autoattribute:: geosoft.gxapi.DB_LINE_LABEL_FORMAT_LINE


.. autoattribute:: geosoft.gxapi.DB_LINE_LABEL_FORMAT_VERSION


.. autoattribute:: geosoft.gxapi.DB_LINE_LABEL_FORMAT_TYPE


.. autoattribute:: geosoft.gxapi.DB_LINE_LABEL_FORMAT_FLIGHT


.. autoattribute:: geosoft.gxapi.DB_LINE_LABEL_FORMAT_FULL


.. autoattribute:: geosoft.gxapi.DB_LINE_LABEL_FORMAT_DATE


.. autoattribute:: geosoft.gxapi.DB_LINE_LABEL_FORMAT_LINK


.. _DB_LINE_SELECT:

DB_LINE_SELECT constants
-----------------------------------------------------------------------

::

   Select modes 

.. autoattribute:: geosoft.gxapi.DB_LINE_SELECT_INCLUDE


.. autoattribute:: geosoft.gxapi.DB_LINE_SELECT_EXCLUDE


.. _DB_LINE_TYPE:

DB_LINE_TYPE constants
-----------------------------------------------------------------------

::

   Line types 

.. autoattribute:: geosoft.gxapi.DB_LINE_TYPE_NORMAL


.. autoattribute:: geosoft.gxapi.DB_LINE_TYPE_BASE


.. autoattribute:: geosoft.gxapi.DB_LINE_TYPE_TIE


.. autoattribute:: geosoft.gxapi.DB_LINE_TYPE_TEST


.. autoattribute:: geosoft.gxapi.DB_LINE_TYPE_TREND


.. autoattribute:: geosoft.gxapi.DB_LINE_TYPE_SPECIAL


.. autoattribute:: geosoft.gxapi.DB_LINE_TYPE_RANDOM


.. _DB_LOCK:

DB_LOCK constants
-----------------------------------------------------------------------

::

   Lock Modes 

.. autoattribute:: geosoft.gxapi.DB_LOCK_NONE

::

   Used only by GetSymbLock_DB 

.. autoattribute:: geosoft.gxapi.DB_LOCK_READONLY


.. autoattribute:: geosoft.gxapi.DB_LOCK_READWRITE


.. _DB_NAME:

DB_NAME constants
-----------------------------------------------------------------------

::

   Get Database file names 

.. autoattribute:: geosoft.gxapi.DB_NAME_FILE


.. _DB_OWN:

DB_OWN constants
-----------------------------------------------------------------------

::

   Symbol Ownership 

.. autoattribute:: geosoft.gxapi.DB_OWN_SHARED


.. autoattribute:: geosoft.gxapi.DB_OWN_USER


.. _DB_SYMB_TYPE:

DB_SYMB_TYPE constants
-----------------------------------------------------------------------

::

   Symbol types 

.. autoattribute:: geosoft.gxapi.DB_SYMB_BLOB


.. autoattribute:: geosoft.gxapi.DB_SYMB_LINE


.. autoattribute:: geosoft.gxapi.DB_SYMB_CHAN


.. autoattribute:: geosoft.gxapi.DB_SYMB_USER


.. _DB_SYMB_NAME_SIZE:

DB_SYMB_NAME_SIZE constant
-----------------------------------------------------------------------


.. autoattribute:: geosoft.gxapi.DB_SYMB_NAME_SIZE

::

   Size of Symbol Names 

.. _DB_WAIT:

DB_WAIT constants
-----------------------------------------------------------------------

::

   Wait Times 

.. autoattribute:: geosoft.gxapi.DB_WAIT_NONE


.. autoattribute:: geosoft.gxapi.DB_WAIT_INFINITY


.. _DB_ARRAY_BASETYPE:

DB_ARRAY_BASETYPE constants
-----------------------------------------------------------------------


.. autoattribute:: geosoft.gxapi.DB_ARRAY_BASETYPE_NONE


.. autoattribute:: geosoft.gxapi.DB_ARRAY_BASETYPE_TIME_WINDOWS


.. autoattribute:: geosoft.gxapi.DB_ARRAY_BASETYPE_TIMES


.. autoattribute:: geosoft.gxapi.DB_ARRAY_BASETYPE_FREQUENCIES


.. autoattribute:: geosoft.gxapi.DB_ARRAY_BASETYPE_ELEVATIONS


.. autoattribute:: geosoft.gxapi.DB_ARRAY_BASETYPE_DEPTHS


.. autoattribute:: geosoft.gxapi.DB_ARRAY_BASETYPE_VELOCITIES


.. autoattribute:: geosoft.gxapi.DB_ARRAY_BASETYPE_DISCRETE_TIME_WINDOWS


.. _NULLSYMB:

NULLSYMB constant
-----------------------------------------------------------------------


.. autoattribute:: geosoft.gxapi.NULLSYMB

::

   Database Null 

	