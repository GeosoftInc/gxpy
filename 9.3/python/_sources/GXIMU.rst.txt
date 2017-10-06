
.. _GXIMU:

 
GXIMU class
==================================

.. autoclass:: geosoft.gxapi.GXIMU
   :members:

.. _IMU_BOOL_OLAP:

IMU_BOOL_OLAP constants
-----------------------------------------------------------------------

::

   Overlapping area option 

.. autoattribute:: geosoft.gxapi.IMU_BOOL_OLAP_AVE

::

   Overlap values are averaged 

.. autoattribute:: geosoft.gxapi.IMU_BOOL_OLAP_1

::

   Overlap values use grid 1 value 

.. autoattribute:: geosoft.gxapi.IMU_BOOL_OLAP_2

::

   Overlap values use grid 2 value 

.. _IMU_BOOL_OPT:

IMU_BOOL_OPT constants
-----------------------------------------------------------------------

::

   Boolean logic option 

.. autoattribute:: geosoft.gxapi.IMU_BOOL_OPT_AND

::

   Valid areas are only where grids overlap 

.. autoattribute:: geosoft.gxapi.IMU_BOOL_OPT_OR

::

   Valid areas are where either grid is a valid value 

.. autoattribute:: geosoft.gxapi.IMU_BOOL_OPT_XOR

::

   Overlap areas are dummied 

.. _IMU_BOOL_SIZING:

IMU_BOOL_SIZING constants
-----------------------------------------------------------------------

::

   Sizing option 

.. autoattribute:: geosoft.gxapi.IMU_BOOL_SIZING_MIN

::

   Output grid is sized to overlapping region 

.. autoattribute:: geosoft.gxapi.IMU_BOOL_SIZING_0

::

   Output grid is sized to grid 1 

.. autoattribute:: geosoft.gxapi.IMU_BOOL_SIZING_1

::

   Output grid is sized to grid 2 

.. autoattribute:: geosoft.gxapi.IMU_BOOL_SIZING_MAX

::

   Output grid is sized to maximum combined area of both grids 

.. _IMU_DOUBLE_CRC_BITS:

IMU_DOUBLE_CRC_BITS constants
-----------------------------------------------------------------------

::

   Bits to use in double CRC's 

.. autoattribute:: geosoft.gxapi.IMU_DOUBLE_CRC_BITS_EXACT

::

   Exact CRC 

.. autoattribute:: geosoft.gxapi.IMU_DOUBLE_CRC_BITS_DEFAULT

::

   Default inaccuracy in double (10 Bits) 

.. autoattribute:: geosoft.gxapi.IMU_DOUBLE_CRC_BITS_MAX

::

   Maximum number of inaccuracy bits (51 Bits) 

.. _IMU_EXPAND_SHAPE:

IMU_EXPAND_SHAPE constants
-----------------------------------------------------------------------

::

   Shape of output grid 

.. autoattribute:: geosoft.gxapi.IMU_EXPAND_SHAPE_RECTANGLE


.. autoattribute:: geosoft.gxapi.IMU_EXPAND_SHAPE_SQUARE


.. _IMU_FILL_ROLLOPT:

IMU_FILL_ROLLOPT constants
-----------------------------------------------------------------------

::

   Defines for Grid Filling Method Options 

.. autoattribute:: geosoft.gxapi.IMU_FILL_ROLLOPT_LINEAR


.. autoattribute:: geosoft.gxapi.IMU_FILL_ROLLOPT_SQUARE


.. _IMU_FILT_DUMMY:

IMU_FILT_DUMMY constants
-----------------------------------------------------------------------

::

   
   				Settings for placing dummy values in grid if any of filter
   				values are dummy
   			 

.. autoattribute:: geosoft.gxapi.IMU_FILT_DUMMY_NO


.. autoattribute:: geosoft.gxapi.IMU_FILT_DUMMY_YES


.. _IMU_FILT_FILE:

IMU_FILT_FILE constants
-----------------------------------------------------------------------

::

   
   				Flags which indicate if a file is to be used to read the
   				filter values
   			 

.. autoattribute:: geosoft.gxapi.IMU_FILT_FILE_NO


.. autoattribute:: geosoft.gxapi.IMU_FILT_FILE_YES


.. _IMU_FILT_HZDRV:

IMU_FILT_HZDRV constants
-----------------------------------------------------------------------

::

   
   				Flags which indicate which type of horizontal derivative
   				is being applied (X direction, Y direction, none at all)
   			 

.. autoattribute:: geosoft.gxapi.IMU_FILT_HZDRV_NO


.. autoattribute:: geosoft.gxapi.IMU_FILT_HZDRV_X


.. autoattribute:: geosoft.gxapi.IMU_FILT_HZDRV_Y


.. _IMU_FLOAT_CRC_BITS:

IMU_FLOAT_CRC_BITS constants
-----------------------------------------------------------------------

::

   Bits to use in float CRC's 

.. autoattribute:: geosoft.gxapi.IMU_FLOAT_CRC_BITS_EXACT

::

   Exact CRC 

.. autoattribute:: geosoft.gxapi.IMU_FLOAT_CRC_BITS_DEFAULT

::

   Default inaccuracy in floats (7 Bits) 

.. autoattribute:: geosoft.gxapi.IMU_FLOAT_CRC_BITS_MAX

::

   Maximum number of inaccuracy bits (22 Bits) 

.. _IMU_MASK:

IMU_MASK constants
-----------------------------------------------------------------------

::

   Defined options for masking grids 

.. autoattribute:: geosoft.gxapi.IMU_MASK_INSIDE


.. autoattribute:: geosoft.gxapi.IMU_MASK_OUTSIDE


.. _IMU_STAT_FORCED:

IMU_STAT_FORCED constants
-----------------------------------------------------------------------

::

   Defined options for forcing recalculating the grid values 

.. autoattribute:: geosoft.gxapi.IMU_STAT_FORCED_NO


.. autoattribute:: geosoft.gxapi.IMU_STAT_FORCED_YES


.. _IMU_TRANS:

IMU_TRANS constants
-----------------------------------------------------------------------

::

   
   				Transpose Options available for \ :func:`geosoft.gxapi.GXIMU.grid_trns`\ 
   				implies original grid lines:
   			 

.. autoattribute:: geosoft.gxapi.IMU_TRANS_DEFAULT

::

   can be ANY orientation 

.. autoattribute:: geosoft.gxapi.IMU_TRANS_Y

::

   MUST be parallel to Y-Axis 

.. autoattribute:: geosoft.gxapi.IMU_TRANS_X

::

   MUST be parallel to X-Axis 

.. _IMU_TREND:

IMU_TREND constants
-----------------------------------------------------------------------

::

   Points in grid to use 

.. autoattribute:: geosoft.gxapi.IMU_TREND_ALL


.. autoattribute:: geosoft.gxapi.IMU_TREND_EDGE


.. _IMU_WIND_COORD:

IMU_WIND_COORD constants
-----------------------------------------------------------------------

::

   Output grid coordinate units 

.. autoattribute:: geosoft.gxapi.IMU_WIND_GRID


.. autoattribute:: geosoft.gxapi.IMU_WIND_GROUND


.. _IMU_WIND_DUMMIES:

IMU_WIND_DUMMIES constants
-----------------------------------------------------------------------

::

   Option for handling out-of-range Z values 

.. autoattribute:: geosoft.gxapi.IMU_WIND_DUMMY


.. autoattribute:: geosoft.gxapi.IMU_WIND_CLIP


.. _IMU_XYZ_INDEX:

IMU_XYZ_INDEX constants
-----------------------------------------------------------------------

::

   
   				Flags whether to use grid index numbers as
   				station numbers.
   			 

.. autoattribute:: geosoft.gxapi.IMU_XYZ_INDEX_NO


.. autoattribute:: geosoft.gxapi.IMU_XYZ_INDEX_YES


.. _IMU_XYZ_LABEL:

IMU_XYZ_LABEL constants
-----------------------------------------------------------------------

::

   XYZ Label Flags 

.. autoattribute:: geosoft.gxapi.IMU_XYZ_LABEL_NO


.. autoattribute:: geosoft.gxapi.IMU_XYZ_LABEL_YES


	