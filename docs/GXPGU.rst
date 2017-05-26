
.. _GXPGU:

 
GXPGU class
==================================

.. autoclass:: geosoft.gxapi.GXPGU
   :members:

.. _BLAKEY_TEST:

BLAKEY_TEST constants
-----------------------------------------------------------------------

::

   Types of BLAKEY tests 

.. autoattribute:: geosoft.gxapi.BLAKEY_TEST_ONESIDE


.. autoattribute:: geosoft.gxapi.BLAKEY_TEST_TWOSIDE


.. autoattribute:: geosoft.gxapi.BLAKEY_TEST_THREESIDE


.. autoattribute:: geosoft.gxapi.BLAKEY_TEST_FOURSIDE


.. _PGU_CORR:

PGU_CORR constants
-----------------------------------------------------------------------

::

   Correlation (must be synchronized with \ :ref:`ST2_CORRELATION`\ ) 

.. autoattribute:: geosoft.gxapi.PGU_CORR_SIMPLE

::

   Simple correlation 

.. autoattribute:: geosoft.gxapi.PGU_CORR_PEARSON

::

   Pearson's correlation (normalized to standard deviations) 

.. _PGU_DIRECTGRID:

PGU_DIRECTGRID constants
-----------------------------------------------------------------------

::

   Type of statistic to use on the data points in each cell. 

.. autoattribute:: geosoft.gxapi.PGU_DIRECTGRID_MINIMUM

::

   Select the minimum value found in each cell 

.. autoattribute:: geosoft.gxapi.PGU_DIRECTGRID_MAXIMUM

::

   Select the maximum value found in each cell 

.. autoattribute:: geosoft.gxapi.PGU_DIRECTGRID_MEAN

::

   Select the mean of all values found in each cell 

.. autoattribute:: geosoft.gxapi.PGU_DIRECTGRID_ITEMS

::

   The number of valid (non-dummy) items found in each cell 

.. _PGU_DIRECTION:

PGU_DIRECTION constants
-----------------------------------------------------------------------

::

   Direction 

.. autoattribute:: geosoft.gxapi.PGU_FORWARD

::

   Forward direction: Removes mean and standard deviation,
   storing the values in the VVs. 

.. autoattribute:: geosoft.gxapi.PGU_BACKWARD

::

   Backward direction: Applies mean and standard deviation
   values in the VVs to the data. 

.. _PGU_TRANS:

PGU_TRANS constants
-----------------------------------------------------------------------

::

   transform methods for the columns 

.. autoattribute:: geosoft.gxapi.PGU_TRANS_NONE


.. autoattribute:: geosoft.gxapi.PGU_TRANS_LOG


.. _PGU_INTERP_ORDER:

PGU_INTERP_ORDER constants
-----------------------------------------------------------------------

::

   interpolation direction order 

.. autoattribute:: geosoft.gxapi.PGU_INTERP_ORDER_XYZ


.. autoattribute:: geosoft.gxapi.PGU_INTERP_ORDER_XZY


.. autoattribute:: geosoft.gxapi.PGU_INTERP_ORDER_YXZ


.. autoattribute:: geosoft.gxapi.PGU_INTERP_ORDER_YZX


.. autoattribute:: geosoft.gxapi.PGU_INTERP_ORDER_ZXY


.. autoattribute:: geosoft.gxapi.PGU_INTERP_ORDER_ZYX


	