
.. _GXDB:

 
GXDB class
==================================

.. autoclass:: geosoft.gxapi.GXDB
   :members:


.. _DB_ACTIVITY_BLOB:

DB_ACTIVITY_BLOB constants
-----------------------------------------------------------------------

Activity Blob

.. autodata:: geosoft.gxapi.DB_ACTIVITY_BLOB
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.DB_ACTIVITY_BLOB


.. _DB_CATEGORY_BLOB:

DB_CATEGORY_BLOB constants
-----------------------------------------------------------------------

Blob Categories

.. autodata:: geosoft.gxapi.DB_CATEGORY_BLOB_NORMAL
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.DB_CATEGORY_BLOB_NORMAL


.. _DB_CATEGORY_CHAN:

DB_CATEGORY_CHAN constants
-----------------------------------------------------------------------

Channel Categories
For STRING type channels, use negative integers
to specify channel width. For example, use -10
to define a string channel with up to 10 characters.
Use the GS_SIMPLE_TYPE() macro to convert to INT,REAL or string.

.. autodata:: geosoft.gxapi.DB_CATEGORY_CHAN_BYTE
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.DB_CATEGORY_CHAN_BYTE
.. autodata:: geosoft.gxapi.DB_CATEGORY_CHAN_USHORT
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.DB_CATEGORY_CHAN_USHORT
.. autodata:: geosoft.gxapi.DB_CATEGORY_CHAN_SHORT
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.DB_CATEGORY_CHAN_SHORT
.. autodata:: geosoft.gxapi.DB_CATEGORY_CHAN_LONG
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.DB_CATEGORY_CHAN_LONG
.. autodata:: geosoft.gxapi.DB_CATEGORY_CHAN_FLOAT
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.DB_CATEGORY_CHAN_FLOAT
.. autodata:: geosoft.gxapi.DB_CATEGORY_CHAN_DOUBLE
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.DB_CATEGORY_CHAN_DOUBLE
.. autodata:: geosoft.gxapi.DB_CATEGORY_CHAN_UBYTE
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.DB_CATEGORY_CHAN_UBYTE
.. autodata:: geosoft.gxapi.DB_CATEGORY_CHAN_ULONG
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.DB_CATEGORY_CHAN_ULONG
.. autodata:: geosoft.gxapi.DB_CATEGORY_CHAN_LONG64
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.DB_CATEGORY_CHAN_LONG64
.. autodata:: geosoft.gxapi.DB_CATEGORY_CHAN_ULONG64
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.DB_CATEGORY_CHAN_ULONG64


.. _DB_CATEGORY_LINE:

DB_CATEGORY_LINE constants
-----------------------------------------------------------------------

Line Categories

.. autodata:: geosoft.gxapi.DB_CATEGORY_LINE_FLIGHT
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.DB_CATEGORY_LINE_FLIGHT
.. autodata:: geosoft.gxapi.DB_CATEGORY_LINE_GROUP
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.DB_CATEGORY_LINE_GROUP
.. autodata:: geosoft.gxapi.DB_CATEGORY_LINE_NORMAL
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.DB_CATEGORY_LINE_NORMAL


.. _DB_CATEGORY_USER:

DB_CATEGORY_USER constants
-----------------------------------------------------------------------

User Categories

.. autodata:: geosoft.gxapi.DB_CATEGORY_USER_NORMAL
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.DB_CATEGORY_USER_NORMAL


.. _DB_CHAN_FORMAT:

DB_CHAN_FORMAT constants
-----------------------------------------------------------------------

Channel formats

.. autodata:: geosoft.gxapi.DB_CHAN_FORMAT_NORMAL
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.DB_CHAN_FORMAT_NORMAL
.. autodata:: geosoft.gxapi.DB_CHAN_FORMAT_EXP
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.DB_CHAN_FORMAT_EXP
.. autodata:: geosoft.gxapi.DB_CHAN_FORMAT_TIME
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.DB_CHAN_FORMAT_TIME
.. autodata:: geosoft.gxapi.DB_CHAN_FORMAT_DATE
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.DB_CHAN_FORMAT_DATE
.. autodata:: geosoft.gxapi.DB_CHAN_FORMAT_GEOGR
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.DB_CHAN_FORMAT_GEOGR
.. autodata:: geosoft.gxapi.DB_CHAN_FORMAT_SIGDIG
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.DB_CHAN_FORMAT_SIGDIG
.. autodata:: geosoft.gxapi.DB_CHAN_FORMAT_HEX
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.DB_CHAN_FORMAT_HEX


.. _DB_CHAN_PROTECTION:

DB_CHAN_PROTECTION constants
-----------------------------------------------------------------------

Channel Read-only Protection Status

.. autodata:: geosoft.gxapi.DB_CHAN_UNPROTECTED
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.DB_CHAN_UNPROTECTED
.. autodata:: geosoft.gxapi.DB_CHAN_PROTECTED
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.DB_CHAN_PROTECTED


.. _DB_CHAN_SYMBOL:

DB_CHAN_SYMBOL constants
-----------------------------------------------------------------------

Channel symbol for special channels

.. autodata:: geosoft.gxapi.DB_CHAN_X
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.DB_CHAN_X
.. autodata:: geosoft.gxapi.DB_CHAN_Y
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.DB_CHAN_Y
.. autodata:: geosoft.gxapi.DB_CHAN_Z
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.DB_CHAN_Z


.. _DB_COMP:

DB_COMP constants
-----------------------------------------------------------------------

Supported compression levels

.. autodata:: geosoft.gxapi.DB_COMP_NONE
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.DB_COMP_NONE
.. autodata:: geosoft.gxapi.DB_COMP_SPEED
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.DB_COMP_SPEED
.. autodata:: geosoft.gxapi.DB_COMP_SIZE
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.DB_COMP_SIZE


.. _DB_COORDPAIR:

DB_COORDPAIR constants
-----------------------------------------------------------------------

Used to indicate the matching coordinate pair of a channel.

.. autodata:: geosoft.gxapi.DB_COORDPAIR_NONE
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.DB_COORDPAIR_NONE
.. autodata:: geosoft.gxapi.DB_COORDPAIR_X
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.DB_COORDPAIR_X
.. autodata:: geosoft.gxapi.DB_COORDPAIR_Y
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.DB_COORDPAIR_Y


.. _DB_GROUP_CLASS_SIZE:

DB_GROUP_CLASS_SIZE constants
-----------------------------------------------------------------------

Class name max size

.. autodata:: geosoft.gxapi.DB_GROUP_CLASS_SIZE
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.DB_GROUP_CLASS_SIZE


.. _DB_INFO:

DB_INFO constants
-----------------------------------------------------------------------

Integer Database Information

.. autodata:: geosoft.gxapi.DB_INFO_BLOBS_MAX
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.DB_INFO_BLOBS_MAX
.. autodata:: geosoft.gxapi.DB_INFO_LINES_MAX
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.DB_INFO_LINES_MAX
.. autodata:: geosoft.gxapi.DB_INFO_CHANS_MAX
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.DB_INFO_CHANS_MAX
.. autodata:: geosoft.gxapi.DB_INFO_USERS_MAX
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.DB_INFO_USERS_MAX
.. autodata:: geosoft.gxapi.DB_INFO_BLOBS_USED
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.DB_INFO_BLOBS_USED
.. autodata:: geosoft.gxapi.DB_INFO_LINES_USED
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.DB_INFO_LINES_USED
.. autodata:: geosoft.gxapi.DB_INFO_CHANS_USED
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.DB_INFO_CHANS_USED
.. autodata:: geosoft.gxapi.DB_INFO_USERS_USED
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.DB_INFO_USERS_USED
.. autodata:: geosoft.gxapi.DB_INFO_PAGE_SIZE
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.DB_INFO_PAGE_SIZE
.. autodata:: geosoft.gxapi.DB_INFO_DATA_SIZE
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.DB_INFO_DATA_SIZE
.. autodata:: geosoft.gxapi.DB_INFO_LOST_SIZE
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.DB_INFO_LOST_SIZE
.. autodata:: geosoft.gxapi.DB_INFO_FREE_SIZE
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.DB_INFO_FREE_SIZE
.. autodata:: geosoft.gxapi.DB_INFO_COMP_LEVEL
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.DB_INFO_COMP_LEVEL
.. autodata:: geosoft.gxapi.DB_INFO_BLOB_SIZE
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.DB_INFO_BLOB_SIZE
.. autodata:: geosoft.gxapi.DB_INFO_FILE_SIZE
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.DB_INFO_FILE_SIZE
.. autodata:: geosoft.gxapi.DB_INFO_INDEX_SIZE
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.DB_INFO_INDEX_SIZE
.. autodata:: geosoft.gxapi.DB_INFO_MAX_BLOCK_SIZE
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.DB_INFO_MAX_BLOCK_SIZE
.. autodata:: geosoft.gxapi.DB_INFO_CHANGESLOST
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.DB_INFO_CHANGESLOST


.. _DB_LINE_LABEL_FORMAT:

DB_LINE_LABEL_FORMAT constants
-----------------------------------------------------------------------

Line Label Formats

.. autodata:: geosoft.gxapi.DB_LINE_LABEL_FORMAT_LINE
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.DB_LINE_LABEL_FORMAT_LINE
.. autodata:: geosoft.gxapi.DB_LINE_LABEL_FORMAT_VERSION
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.DB_LINE_LABEL_FORMAT_VERSION
.. autodata:: geosoft.gxapi.DB_LINE_LABEL_FORMAT_TYPE
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.DB_LINE_LABEL_FORMAT_TYPE
.. autodata:: geosoft.gxapi.DB_LINE_LABEL_FORMAT_FLIGHT
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.DB_LINE_LABEL_FORMAT_FLIGHT
.. autodata:: geosoft.gxapi.DB_LINE_LABEL_FORMAT_FULL
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.DB_LINE_LABEL_FORMAT_FULL
.. autodata:: geosoft.gxapi.DB_LINE_LABEL_FORMAT_DATE
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.DB_LINE_LABEL_FORMAT_DATE
.. autodata:: geosoft.gxapi.DB_LINE_LABEL_FORMAT_LINK
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.DB_LINE_LABEL_FORMAT_LINK


.. _DB_LINE_SELECT:

DB_LINE_SELECT constants
-----------------------------------------------------------------------

Select modes

.. autodata:: geosoft.gxapi.DB_LINE_SELECT_INCLUDE
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.DB_LINE_SELECT_INCLUDE
.. autodata:: geosoft.gxapi.DB_LINE_SELECT_EXCLUDE
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.DB_LINE_SELECT_EXCLUDE


.. _DB_LINE_TYPE:

DB_LINE_TYPE constants
-----------------------------------------------------------------------

Line types

.. autodata:: geosoft.gxapi.DB_LINE_TYPE_NORMAL
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.DB_LINE_TYPE_NORMAL
.. autodata:: geosoft.gxapi.DB_LINE_TYPE_BASE
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.DB_LINE_TYPE_BASE
.. autodata:: geosoft.gxapi.DB_LINE_TYPE_TIE
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.DB_LINE_TYPE_TIE
.. autodata:: geosoft.gxapi.DB_LINE_TYPE_TEST
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.DB_LINE_TYPE_TEST
.. autodata:: geosoft.gxapi.DB_LINE_TYPE_TREND
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.DB_LINE_TYPE_TREND
.. autodata:: geosoft.gxapi.DB_LINE_TYPE_SPECIAL
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.DB_LINE_TYPE_SPECIAL
.. autodata:: geosoft.gxapi.DB_LINE_TYPE_RANDOM
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.DB_LINE_TYPE_RANDOM


.. _DB_LOCK:

DB_LOCK constants
-----------------------------------------------------------------------

Lock Modes

.. autodata:: geosoft.gxapi.DB_LOCK_NONE
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.DB_LOCK_NONE
.. autodata:: geosoft.gxapi.DB_LOCK_READONLY
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.DB_LOCK_READONLY
.. autodata:: geosoft.gxapi.DB_LOCK_READWRITE
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.DB_LOCK_READWRITE


.. _DB_NAME:

DB_NAME constants
-----------------------------------------------------------------------

Get Database file names

.. autodata:: geosoft.gxapi.DB_NAME_FILE
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.DB_NAME_FILE


.. _DB_OWN:

DB_OWN constants
-----------------------------------------------------------------------

Symbol Ownership

.. autodata:: geosoft.gxapi.DB_OWN_SHARED
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.DB_OWN_SHARED
.. autodata:: geosoft.gxapi.DB_OWN_USER
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.DB_OWN_USER


.. _DB_SYMB_TYPE:

DB_SYMB_TYPE constants
-----------------------------------------------------------------------

Symbol types

.. autodata:: geosoft.gxapi.DB_SYMB_BLOB
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.DB_SYMB_BLOB
.. autodata:: geosoft.gxapi.DB_SYMB_LINE
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.DB_SYMB_LINE
.. autodata:: geosoft.gxapi.DB_SYMB_CHAN
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.DB_SYMB_CHAN
.. autodata:: geosoft.gxapi.DB_SYMB_USER
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.DB_SYMB_USER


.. _DB_SYMB_NAME_SIZE:

DB_SYMB_NAME_SIZE constants
-----------------------------------------------------------------------

Size of Symbol Names

.. autodata:: geosoft.gxapi.DB_SYMB_NAME_SIZE
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.DB_SYMB_NAME_SIZE


.. _DB_WAIT:

DB_WAIT constants
-----------------------------------------------------------------------

Wait Times

.. autodata:: geosoft.gxapi.DB_WAIT_NONE
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.DB_WAIT_NONE
.. autodata:: geosoft.gxapi.DB_WAIT_INFINITY
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.DB_WAIT_INFINITY


.. _DB_ARRAY_BASETYPE:

DB_ARRAY_BASETYPE constants
-----------------------------------------------------------------------

Array channel base coordinate type

.. autodata:: geosoft.gxapi.DB_ARRAY_BASETYPE_NONE
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.DB_ARRAY_BASETYPE_NONE
.. autodata:: geosoft.gxapi.DB_ARRAY_BASETYPE_TIME_WINDOWS
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.DB_ARRAY_BASETYPE_TIME_WINDOWS
.. autodata:: geosoft.gxapi.DB_ARRAY_BASETYPE_TIMES
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.DB_ARRAY_BASETYPE_TIMES
.. autodata:: geosoft.gxapi.DB_ARRAY_BASETYPE_FREQUENCIES
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.DB_ARRAY_BASETYPE_FREQUENCIES
.. autodata:: geosoft.gxapi.DB_ARRAY_BASETYPE_ELEVATIONS
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.DB_ARRAY_BASETYPE_ELEVATIONS
.. autodata:: geosoft.gxapi.DB_ARRAY_BASETYPE_DEPTHS
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.DB_ARRAY_BASETYPE_DEPTHS
.. autodata:: geosoft.gxapi.DB_ARRAY_BASETYPE_VELOCITIES
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.DB_ARRAY_BASETYPE_VELOCITIES
.. autodata:: geosoft.gxapi.DB_ARRAY_BASETYPE_DISCRETE_TIME_WINDOWS
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.DB_ARRAY_BASETYPE_DISCRETE_TIME_WINDOWS
.. autodata:: geosoft.gxapi.DB_ARRAY_BASETYPE_ENERGIES
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.DB_ARRAY_BASETYPE_ENERGIES


.. _NULLSYMB:

NULLSYMB constants
-----------------------------------------------------------------------

Database Null

.. autodata:: geosoft.gxapi.NULLSYMB
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.NULLSYMB

	