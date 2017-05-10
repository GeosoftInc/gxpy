 

.. _GXWA:

GXWA class
==================================

.. autoclass:: geosoft.gxapi.GXWA
   :members:

.. _WA_ENCODE:

WA_ENCODE constants
-----------------------------------------------------------------------

::

   WA Encode defines 

.. autoattribute:: geosoft.gxapi.WA_ENCODE_ANSI

::

   
   					Current Ansi Code Page (Conversion from UTF-8 data, if an exisiting BOM header found with WA_APPEND,
   					encoding will switch to WA_ENCODE_UTF8)
   				 

.. autoattribute:: geosoft.gxapi.WA_ENCODE_RAW

::

   Write all data without any conversion check 

.. autoattribute:: geosoft.gxapi.WA_ENCODE_UTF8

::

   UTF8 (If no exisiting BOM header found with WA_APPEND, encoding will switch to WA_ENCODE_ANSI) 

.. autoattribute:: geosoft.gxapi.WA_ENCODE_UTF8_NOHEADER

::

   UTF8 w.o. header (will assume UTF8 encoding if WA_APPEND is used) 

.. autoattribute:: geosoft.gxapi.WA_ENCODE_UTF16_NOHEADER

::

   UTF16 w.o. header (will assume UTF16 encoding if WA_APPEND is used) 

.. _WA_OPEN:

WA_OPEN constants
-----------------------------------------------------------------------

::

   WA Open defines 

.. autoattribute:: geosoft.gxapi.WA_NEW

::

   Create new file 

.. autoattribute:: geosoft.gxapi.WA_APPEND

::

   Append to existing file 

	