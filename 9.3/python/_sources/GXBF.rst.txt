
.. _GXBF:

 
GXBF class
==================================

.. autoclass:: geosoft.gxapi.GXBF
   :members:

.. _BF_BYTEORDER:

BF_BYTEORDER constants
-----------------------------------------------------------------------

::

   Byte order for read/write 

.. autoattribute:: geosoft.gxapi.BF_BYTEORDER_LSB

::

   Least significant byte first (Intel, Windows) 

.. autoattribute:: geosoft.gxapi.BF_BYTEORDER_MSB

::

   Most significant byte first (Mororola, Sun) 

.. _BF_CLOSE:

BF_CLOSE constants
-----------------------------------------------------------------------

::

   Close Flags 

.. autoattribute:: geosoft.gxapi.BF_KEEP


.. autoattribute:: geosoft.gxapi.BF_DELETE


.. _BF_ENCODE:

BF_ENCODE constants
-----------------------------------------------------------------------

::

   The way a string is encoded 

.. autoattribute:: geosoft.gxapi.BF_ENCODE_ANSI

::

   String is stored as ANSI code page 

.. autoattribute:: geosoft.gxapi.BF_ENCODE_UTF8

::

   String is stored as UTF8 

.. _BF_OPEN_MODE:

BF_OPEN_MODE constants
-----------------------------------------------------------------------

::

   Open Status 

.. autoattribute:: geosoft.gxapi.BF_READ

::

   Read only 

.. autoattribute:: geosoft.gxapi.BF_READWRITE_NEW

::

   erases existing file 

.. autoattribute:: geosoft.gxapi.BF_READWRITE_OLD

::

   file must pre-exist 

.. autoattribute:: geosoft.gxapi.BF_READWRITE_APP

::

   open and append onto pre-existing file (cannot be read from) 

.. _BF_SEEK:

BF_SEEK constants
-----------------------------------------------------------------------

::

   Seek Location 

.. autoattribute:: geosoft.gxapi.BF_SEEK_START


.. autoattribute:: geosoft.gxapi.BF_SEEK_CURRENT


.. autoattribute:: geosoft.gxapi.BF_SEEK_EOF


	