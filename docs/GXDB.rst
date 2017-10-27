
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


.. _DB_CATEGORY_BLOB:

DB_CATEGORY_BLOB constants
-----------------------------------------------------------------------

Blob Categories

.. autodata:: geosoft.gxapi.DB_CATEGORY_BLOB_NORMAL
    :annotation:


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
.. autodata:: geosoft.gxapi.DB_CATEGORY_CHAN_USHORT
    :annotation:
.. autodata:: geosoft.gxapi.DB_CATEGORY_CHAN_SHORT
    :annotation:
.. autodata:: geosoft.gxapi.DB_CATEGORY_CHAN_LONG
    :annotation:
.. autodata:: geosoft.gxapi.DB_CATEGORY_CHAN_FLOAT
    :annotation:
.. autodata:: geosoft.gxapi.DB_CATEGORY_CHAN_DOUBLE
    :annotation:
.. autodata:: geosoft.gxapi.DB_CATEGORY_CHAN_UBYTE
    :annotation:
.. autodata:: geosoft.gxapi.DB_CATEGORY_CHAN_ULONG
    :annotation:
.. autodata:: geosoft.gxapi.DB_CATEGORY_CHAN_LONG64
    :annotation:
.. autodata:: geosoft.gxapi.DB_CATEGORY_CHAN_ULONG64
    :annotation:


.. _DB_CATEGORY_LINE:

DB_CATEGORY_LINE constants
-----------------------------------------------------------------------

Line Categories

.. autodata:: geosoft.gxapi.DB_CATEGORY_LINE_FLIGHT
    :annotation:
.. autodata:: geosoft.gxapi.DB_CATEGORY_LINE_GROUP
    :annotation:
.. autodata:: geosoft.gxapi.DB_CATEGORY_LINE_NORMAL
    :annotation:


.. _DB_CATEGORY_USER:

DB_CATEGORY_USER constants
-----------------------------------------------------------------------

User Categories

.. autodata:: geosoft.gxapi.DB_CATEGORY_USER_NORMAL
    :annotation:


.. _DB_CHAN_FORMAT:

DB_CHAN_FORMAT constants
-----------------------------------------------------------------------

Channel formats

.. autodata:: geosoft.gxapi.DB_CHAN_FORMAT_NORMAL
    :annotation:
.. autodata:: geosoft.gxapi.DB_CHAN_FORMAT_EXP
    :annotation:
.. autodata:: geosoft.gxapi.DB_CHAN_FORMAT_TIME
    :annotation:
.. autodata:: geosoft.gxapi.DB_CHAN_FORMAT_DATE
    :annotation:
.. autodata:: geosoft.gxapi.DB_CHAN_FORMAT_GEOGR
    :annotation:
.. autodata:: geosoft.gxapi.DB_CHAN_FORMAT_SIGDIG
    :annotation:
.. autodata:: geosoft.gxapi.DB_CHAN_FORMAT_HEX
    :annotation:


.. _DB_CHAN_PROTECTION:

DB_CHAN_PROTECTION constants
-----------------------------------------------------------------------

Channel Read-only Protection Status

.. autodata:: geosoft.gxapi.DB_CHAN_UNPROTECTED
    :annotation:
.. autodata:: geosoft.gxapi.DB_CHAN_PROTECTED
    :annotation:


.. _DB_CHAN_SYMBOL:

DB_CHAN_SYMBOL constants
-----------------------------------------------------------------------

Channel symbol for special channels

.. autodata:: geosoft.gxapi.DB_CHAN_X
    :annotation:
.. autodata:: geosoft.gxapi.DB_CHAN_Y
    :annotation:
.. autodata:: geosoft.gxapi.DB_CHAN_Z
    :annotation:


.. _DB_COMP:

DB_COMP constants
-----------------------------------------------------------------------

Supported compression levels

.. autodata:: geosoft.gxapi.DB_COMP_NONE
    :annotation:
.. autodata:: geosoft.gxapi.DB_COMP_SPEED
    :annotation:
.. autodata:: geosoft.gxapi.DB_COMP_SIZE
    :annotation:


.. _DB_COORDPAIR:

DB_COORDPAIR constants
-----------------------------------------------------------------------


.. autodata:: geosoft.gxapi.DB_COORDPAIR_NONE
    :annotation:
.. autodata:: geosoft.gxapi.DB_COORDPAIR_X
    :annotation:
.. autodata:: geosoft.gxapi.DB_COORDPAIR_Y
    :annotation:


.. _DB_GROUP_CLASS_SIZE:

DB_GROUP_CLASS_SIZE constants
-----------------------------------------------------------------------

Class name max size

.. autodata:: geosoft.gxapi.DB_GROUP_CLASS_SIZE
    :annotation:


.. _DB_INFO:

DB_INFO constants
-----------------------------------------------------------------------

Integer Database Information

.. autodata:: geosoft.gxapi.DB_INFO_BLOBS_MAX
    :annotation:
.. autodata:: geosoft.gxapi.DB_INFO_LINES_MAX
    :annotation:
.. autodata:: geosoft.gxapi.DB_INFO_CHANS_MAX
    :annotation:
.. autodata:: geosoft.gxapi.DB_INFO_USERS_MAX
    :annotation:
.. autodata:: geosoft.gxapi.DB_INFO_BLOBS_USED
    :annotation:
.. autodata:: geosoft.gxapi.DB_INFO_LINES_USED
    :annotation:
.. autodata:: geosoft.gxapi.DB_INFO_CHANS_USED
    :annotation:
.. autodata:: geosoft.gxapi.DB_INFO_USERS_USED
    :annotation:
.. autodata:: geosoft.gxapi.DB_INFO_PAGE_SIZE
    :annotation:
.. autodata:: geosoft.gxapi.DB_INFO_DATA_SIZE
    :annotation:
.. autodata:: geosoft.gxapi.DB_INFO_LOST_SIZE
    :annotation:
.. autodata:: geosoft.gxapi.DB_INFO_FREE_SIZE
    :annotation:
.. autodata:: geosoft.gxapi.DB_INFO_COMP_LEVEL
    :annotation:
.. autodata:: geosoft.gxapi.DB_INFO_BLOB_SIZE
    :annotation:
.. autodata:: geosoft.gxapi.DB_INFO_FILE_SIZE
    :annotation:
.. autodata:: geosoft.gxapi.DB_INFO_INDEX_SIZE
    :annotation:
.. autodata:: geosoft.gxapi.DB_INFO_MAX_BLOCK_SIZE
    :annotation:
.. autodata:: geosoft.gxapi.DB_INFO_CHANGESLOST
    :annotation:


.. _DB_LINE_LABEL_FORMAT:

DB_LINE_LABEL_FORMAT constants
-----------------------------------------------------------------------

Line Label Formats

.. autodata:: geosoft.gxapi.DB_LINE_LABEL_FORMAT_LINE
    :annotation:
.. autodata:: geosoft.gxapi.DB_LINE_LABEL_FORMAT_VERSION
    :annotation:
.. autodata:: geosoft.gxapi.DB_LINE_LABEL_FORMAT_TYPE
    :annotation:
.. autodata:: geosoft.gxapi.DB_LINE_LABEL_FORMAT_FLIGHT
    :annotation:
.. autodata:: geosoft.gxapi.DB_LINE_LABEL_FORMAT_FULL
    :annotation:
.. autodata:: geosoft.gxapi.DB_LINE_LABEL_FORMAT_DATE
    :annotation:
.. autodata:: geosoft.gxapi.DB_LINE_LABEL_FORMAT_LINK
    :annotation:


.. _DB_LINE_SELECT:

DB_LINE_SELECT constants
-----------------------------------------------------------------------

Select modes

.. autodata:: geosoft.gxapi.DB_LINE_SELECT_INCLUDE
    :annotation:
.. autodata:: geosoft.gxapi.DB_LINE_SELECT_EXCLUDE
    :annotation:


.. _DB_LINE_TYPE:

DB_LINE_TYPE constants
-----------------------------------------------------------------------

Line types

.. autodata:: geosoft.gxapi.DB_LINE_TYPE_NORMAL
    :annotation:
.. autodata:: geosoft.gxapi.DB_LINE_TYPE_BASE
    :annotation:
.. autodata:: geosoft.gxapi.DB_LINE_TYPE_TIE
    :annotation:
.. autodata:: geosoft.gxapi.DB_LINE_TYPE_TEST
    :annotation:
.. autodata:: geosoft.gxapi.DB_LINE_TYPE_TREND
    :annotation:
.. autodata:: geosoft.gxapi.DB_LINE_TYPE_SPECIAL
    :annotation:
.. autodata:: geosoft.gxapi.DB_LINE_TYPE_RANDOM
    :annotation:


.. _DB_LOCK:

DB_LOCK constants
-----------------------------------------------------------------------

Lock Modes

.. autodata:: geosoft.gxapi.DB_LOCK_NONE
    :annotation:
.. autodata:: geosoft.gxapi.DB_LOCK_READONLY
    :annotation:
.. autodata:: geosoft.gxapi.DB_LOCK_READWRITE
    :annotation:


.. _DB_NAME:

DB_NAME constants
-----------------------------------------------------------------------

Get Database file names

.. autodata:: geosoft.gxapi.DB_NAME_FILE
    :annotation:


.. _DB_OWN:

DB_OWN constants
-----------------------------------------------------------------------

Symbol Ownership

.. autodata:: geosoft.gxapi.DB_OWN_SHARED
    :annotation:
.. autodata:: geosoft.gxapi.DB_OWN_USER
    :annotation:


.. _DB_SYMB_TYPE:

DB_SYMB_TYPE constants
-----------------------------------------------------------------------

Symbol types

.. autodata:: geosoft.gxapi.DB_SYMB_BLOB
    :annotation:
.. autodata:: geosoft.gxapi.DB_SYMB_LINE
    :annotation:
.. autodata:: geosoft.gxapi.DB_SYMB_CHAN
    :annotation:
.. autodata:: geosoft.gxapi.DB_SYMB_USER
    :annotation:


.. _DB_SYMB_NAME_SIZE:

DB_SYMB_NAME_SIZE constants
-----------------------------------------------------------------------

Size of Symbol Names

.. autodata:: geosoft.gxapi.DB_SYMB_NAME_SIZE
    :annotation:


.. _DB_WAIT:

DB_WAIT constants
-----------------------------------------------------------------------

Wait Times

.. autodata:: geosoft.gxapi.DB_WAIT_NONE
    :annotation:
.. autodata:: geosoft.gxapi.DB_WAIT_INFINITY
    :annotation:


.. _DB_ARRAY_BASETYPE:

DB_ARRAY_BASETYPE constants
-----------------------------------------------------------------------


.. autodata:: geosoft.gxapi.DB_ARRAY_BASETYPE_NONE
    :annotation:
.. autodata:: geosoft.gxapi.DB_ARRAY_BASETYPE_TIME_WINDOWS
    :annotation:
.. autodata:: geosoft.gxapi.DB_ARRAY_BASETYPE_TIMES
    :annotation:
.. autodata:: geosoft.gxapi.DB_ARRAY_BASETYPE_FREQUENCIES
    :annotation:
.. autodata:: geosoft.gxapi.DB_ARRAY_BASETYPE_ELEVATIONS
    :annotation:
.. autodata:: geosoft.gxapi.DB_ARRAY_BASETYPE_DEPTHS
    :annotation:
.. autodata:: geosoft.gxapi.DB_ARRAY_BASETYPE_VELOCITIES
    :annotation:
.. autodata:: geosoft.gxapi.DB_ARRAY_BASETYPE_DISCRETE_TIME_WINDOWS
    :annotation:


.. _NULLSYMB:

NULLSYMB constants
-----------------------------------------------------------------------

Database Null

.. autodata:: geosoft.gxapi.NULLSYMB
    :annotation:

	