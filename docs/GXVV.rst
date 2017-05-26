
.. _GXVV:

 
GXVV class
==================================

.. autoclass:: geosoft.gxapi.GXVV
   :members:

.. _VV_DOUBLE_CRC_BITS:

VV_DOUBLE_CRC_BITS constants
-----------------------------------------------------------------------

::

   Number of bits to use in double CRC's 

.. autoattribute:: geosoft.gxapi.VV_DOUBLE_CRC_BITS_EXACT

::

   Exact CRC 

.. autoattribute:: geosoft.gxapi.VV_DOUBLE_CRC_BITS_DEFAULT

::

   Default inaccuracy in double (10 Bits) 

.. autoattribute:: geosoft.gxapi.VV_DOUBLE_CRC_BITS_MAX

::

   Maximum number of inaccuracy bits 

.. _VV_FLOAT_CRC_BITS:

VV_FLOAT_CRC_BITS constants
-----------------------------------------------------------------------

::

   Number of bits to use in float CRC's 

.. autoattribute:: geosoft.gxapi.VV_FLOAT_CRC_BITS_EXACT

::

   Exact CRC 

.. autoattribute:: geosoft.gxapi.VV_FLOAT_CRC_BITS_DEFAULT

::

   Default inaccuracy in floats (7 Bits) 

.. autoattribute:: geosoft.gxapi.VV_FLOAT_CRC_BITS_MAX

::

   Maximum number of inaccuracy bits 

.. _VV_LOG_BASE:

VV_LOG_BASE constants
-----------------------------------------------------------------------

::

   Type of log to use 

.. autoattribute:: geosoft.gxapi.VV_LOG_BASE_10

::

   Base 10 

.. autoattribute:: geosoft.gxapi.VV_LOG_BASE_E

::

   Base e 

.. _VV_LOG_NEGATIVE:

VV_LOG_NEGATIVE constants
-----------------------------------------------------------------------

::

   Ways to handle negatives 

.. autoattribute:: geosoft.gxapi.VV_LOG_NEGATIVE_NO

::

   dummies out value less than the minimum. 

.. autoattribute:: geosoft.gxapi.VV_LOG_NEGATIVE_YES

::

   
   					if the data is in the range +/- minimum,
   					it is left alone.  Otherwise, the data
   					is divided by the minimum, the log is
   					applied, the minimum is added and the
   					sign is reapplied. Use LogLinear_VV function
   					if decades in results are required.
   				 

.. _VV_LOOKUP:

VV_LOOKUP constants
-----------------------------------------------------------------------

::

   Lookup style 

.. autoattribute:: geosoft.gxapi.VV_LOOKUP_EXACT

::

   only exact matches are used 

.. autoattribute:: geosoft.gxapi.VV_LOOKUP_NEAREST

::

   nearest match is used (regardless of sampling range) 

.. autoattribute:: geosoft.gxapi.VV_LOOKUP_INTERPOLATE

::

   interpolate between values (regardless of sampling range) 

.. autoattribute:: geosoft.gxapi.VV_LOOKUP_NEARESTCLOSE

::

   use nearest match only if within sampling range 

.. autoattribute:: geosoft.gxapi.VV_LOOKUP_INTERPCLOSE

::

   interpolate only if within sampling range 

.. _VV_MASK:

VV_MASK constants
-----------------------------------------------------------------------

::

   Where to mask 

.. autoattribute:: geosoft.gxapi.VV_MASK_INSIDE


.. autoattribute:: geosoft.gxapi.VV_MASK_OUTSIDE


.. _VV_ORDER:

VV_ORDER constants
-----------------------------------------------------------------------

::

   Specify if the data is montonically increasing or decreasing. 

.. autoattribute:: geosoft.gxapi.VV_ORDER_NONE

::

   There is no specific data size ordering in the VV. 

.. autoattribute:: geosoft.gxapi.VV_ORDER_INCREASING

::

   Every value is greater than or equal to the previous value. 

.. autoattribute:: geosoft.gxapi.VV_ORDER_DECREASING

::

   Every value is less than or equal to the previous value. 

.. _VV_SORT:

VV_SORT constants
-----------------------------------------------------------------------

::

   Sort order 

.. autoattribute:: geosoft.gxapi.VV_SORT_ASCENDING


.. autoattribute:: geosoft.gxapi.VV_SORT_DESCENDING


.. _VV_WINDOW:

VV_WINDOW constants
-----------------------------------------------------------------------

::

   How to handle VV limits 

.. autoattribute:: geosoft.gxapi.VV_WINDOW_DUMMY

::

   Dummy values outside the limits 

.. autoattribute:: geosoft.gxapi.VV_WINDOW_LIMIT

::

   Set values outside the limits to the limits 

	