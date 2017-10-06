
.. _GXVVU:

 
GXVVU class
==================================

.. autoclass:: geosoft.gxapi.GXVVU
   :members:

.. _QC_CRITERION:

QC_CRITERION constants
-----------------------------------------------------------------------

::

   Criterion 

.. autoattribute:: geosoft.gxapi.QC_CRITERION_1


.. autoattribute:: geosoft.gxapi.QC_CRITERION_2


.. autoattribute:: geosoft.gxapi.QC_CRITERION_12


.. _TEM_ARRAY:

TEM_ARRAY constants
-----------------------------------------------------------------------

::

   Array Type 

.. autoattribute:: geosoft.gxapi.TEM_ARRAY_VERTICALSOUNDING


.. autoattribute:: geosoft.gxapi.TEM_ARRAY_PROFILING


.. autoattribute:: geosoft.gxapi.TEM_ARRAY_BOREHOLE


.. _VV_DUP:

VV_DUP constants
-----------------------------------------------------------------------

::

   Duplicate handling mode 

.. autoattribute:: geosoft.gxapi.VV_DUP_AVERAGE

::

   average numeric values (for strings, same as VV_DUP_1) 

.. autoattribute:: geosoft.gxapi.VV_DUP_1

::

   Use first value of the pair 

.. autoattribute:: geosoft.gxapi.VV_DUP_2

::

   Use second value of the pair 

.. autoattribute:: geosoft.gxapi.VV_DUP_DUMMY

::

   Set to dummy 

.. autoattribute:: geosoft.gxapi.VV_DUP_SAMPLE

::

   Set to "3" (cannot use with string data VV) 

.. _VV_XYDUP:

VV_XYDUP constants
-----------------------------------------------------------------------

::

   Sample handling 

.. autoattribute:: geosoft.gxapi.VV_XYDUP_AVERAGE


.. autoattribute:: geosoft.gxapi.VV_XYDUP_SUM


.. _VVU_CASE:

VVU_CASE constants
-----------------------------------------------------------------------

::

   String case handling 

.. autoattribute:: geosoft.gxapi.VVU_CASE_TOLERANT


.. autoattribute:: geosoft.gxapi.VVU_CASE_SENSITIVE


.. _VVU_CLIP:

VVU_CLIP constants
-----------------------------------------------------------------------

::

   Type of clipping 

.. autoattribute:: geosoft.gxapi.VVU_CLIP_DUMMY

::

   clip replaces clipped values with a dummy. 

.. autoattribute:: geosoft.gxapi.VVU_CLIP_LIMIT

::

   clip replaces clipped values with the limit. 

.. _VVU_DUMMYREPEAT:

VVU_DUMMYREPEAT constants
-----------------------------------------------------------------------

::

   How to deal with repeats 

.. autoattribute:: geosoft.gxapi.VVU_DUMMYREPEAT_FIRST

::

   dummies all but first point. 

.. autoattribute:: geosoft.gxapi.VVU_DUMMYREPEAT_LAST

::

   dummies all but last point. 

.. autoattribute:: geosoft.gxapi.VVU_DUMMYREPEAT_MIDDLE

::

   dummies all but middle point. 

.. _VVU_INTERP:

VVU_INTERP constants
-----------------------------------------------------------------------

::

   Interpolation method to use 

.. autoattribute:: geosoft.gxapi.VVU_INTERP_NEAREST


.. autoattribute:: geosoft.gxapi.VVU_INTERP_LINEAR


.. autoattribute:: geosoft.gxapi.VVU_INTERP_CUBIC


.. autoattribute:: geosoft.gxapi.VVU_INTERP_AKIMA


.. autoattribute:: geosoft.gxapi.VVU_INTERP_PREDICT


.. _VVU_INTERP_EDGE:

VVU_INTERP_EDGE constants
-----------------------------------------------------------------------

::

   Interpolation method to use on edges 

.. autoattribute:: geosoft.gxapi.VVU_INTERP_EDGE_NONE


.. autoattribute:: geosoft.gxapi.VVU_INTERP_EDGE_SAME


.. autoattribute:: geosoft.gxapi.VVU_INTERP_EDGE_NEAREST


.. autoattribute:: geosoft.gxapi.VVU_INTERP_EDGE_LINEAR


.. _VVU_LINE:

VVU_LINE constants
-----------------------------------------------------------------------

::

   Line Types 

.. autoattribute:: geosoft.gxapi.LINE_2_POINTS


.. autoattribute:: geosoft.gxapi.LINE_POINT_AZIMUTH


.. _VVU_MASK:

VVU_MASK constants
-----------------------------------------------------------------------

::

   Type of clipping 

.. autoattribute:: geosoft.gxapi.VVU_MASK_INSIDE

::

   Mask VV is set to dummy at locations inside the PLY. 

.. autoattribute:: geosoft.gxapi.VVU_MASK_OUTSIDE

::

   Mask VV is set to dummy at locations outside the PLY. 

.. _VVU_MATCH:

VVU_MATCH constants
-----------------------------------------------------------------------

::

   Matching style 

.. autoattribute:: geosoft.gxapi.VVU_MATCH_FULL_STRINGS

::

   entire string 

.. autoattribute:: geosoft.gxapi.VVU_MATCH_INPUT_LENGTH

::

   match the first part of a string. 

.. _VVU_MODE:

VVU_MODE constants
-----------------------------------------------------------------------

::

   Statistic to select 

.. autoattribute:: geosoft.gxapi.VVU_MODE_MEAN


.. autoattribute:: geosoft.gxapi.VVU_MODE_MEDIAN


.. autoattribute:: geosoft.gxapi.VVU_MODE_MAXIMUM


.. autoattribute:: geosoft.gxapi.VVU_MODE_MINIMUM


.. _VVU_OFFSET:

VVU_OFFSET constants
-----------------------------------------------------------------------

::

   Heading 

.. autoattribute:: geosoft.gxapi.VVU_OFFSET_FORWARD


.. autoattribute:: geosoft.gxapi.VVU_OFFSET_BACKWARD


.. autoattribute:: geosoft.gxapi.VVU_OFFSET_RIGHT


.. autoattribute:: geosoft.gxapi.VVU_OFFSET_LEFT


.. _VVU_PRUNE:

VVU_PRUNE constants
-----------------------------------------------------------------------

::

   Prune options 

.. autoattribute:: geosoft.gxapi.VVU_PRUNE_DUMMY

::

   0 

.. autoattribute:: geosoft.gxapi.VVU_PRUNE_VALID

::

   1 

.. _VVU_SPL:

VVU_SPL constants
-----------------------------------------------------------------------

::

   Spline types 

.. autoattribute:: geosoft.gxapi.VVU_SPL_LINEAR


.. autoattribute:: geosoft.gxapi.VVU_SPL_CUBIC


.. autoattribute:: geosoft.gxapi.VVU_SPL_AKIMA


.. autoattribute:: geosoft.gxapi.VVU_SPL_NEAREST


.. _VVU_SRCHREPL_CASE:

VVU_SRCHREPL_CASE constants
-----------------------------------------------------------------------

::

   Search and Replace handling of string case 

.. autoattribute:: geosoft.gxapi.VVU_SRCHREPL_CASE_TOLERANT


.. autoattribute:: geosoft.gxapi.VVU_SRCHREPL_CASE_SENSITIVE


	