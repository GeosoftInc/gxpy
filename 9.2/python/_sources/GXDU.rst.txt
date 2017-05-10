 

.. _GXDU:

GXDU class
==================================

.. autoclass:: geosoft.gxapi.GXDU
   :members:

.. _DB_DUP:

DB_DUP constants
-----------------------------------------------------------------------

::

   Duplicate Types 

.. autoattribute:: geosoft.gxapi.DB_DUP_FIRST


.. autoattribute:: geosoft.gxapi.DB_DUP_AVERAGE


.. autoattribute:: geosoft.gxapi.DB_DUP_MINIMUM


.. autoattribute:: geosoft.gxapi.DB_DUP_MAXIMUM


.. autoattribute:: geosoft.gxapi.DB_DUP_MEDIAN


.. autoattribute:: geosoft.gxapi.DB_DUP_LAST


.. _DB_DUPEDIT:

DB_DUPEDIT constants
-----------------------------------------------------------------------

::

   Duplicate Edit Flags 

.. autoattribute:: geosoft.gxapi.DB_DUPEDIT_SINGLE


.. autoattribute:: geosoft.gxapi.DB_DUPEDIT_ALL


.. _DU_CHANNELS:

DU_CHANNELS constants
-----------------------------------------------------------------------

::

   Channels to Display 

.. autoattribute:: geosoft.gxapi.DU_CHANNELS_DISPLAYED


.. autoattribute:: geosoft.gxapi.DU_CHANNELS_ALL


.. _DU_EXPORT:

DU_EXPORT constants
-----------------------------------------------------------------------

::

   Export Type 

.. autoattribute:: geosoft.gxapi.DU_EXPORT_CSV


.. autoattribute:: geosoft.gxapi.DU_EXPORT_ODDF


.. autoattribute:: geosoft.gxapi.DU_EXPORT_POST_PC


.. autoattribute:: geosoft.gxapi.DU_EXPORT_POST_UNIX


.. _DU_FILL:

DU_FILL constants
-----------------------------------------------------------------------

::

   Filling Options 

.. autoattribute:: geosoft.gxapi.DU_FILL_INSIDE


.. autoattribute:: geosoft.gxapi.DU_FILL_OUTSIDE


.. _DU_IMPORT:

DU_IMPORT constants
-----------------------------------------------------------------------

::

   Import Mode 

.. autoattribute:: geosoft.gxapi.DU_IMPORT_APPEND


.. autoattribute:: geosoft.gxapi.DU_IMPORT_REPLACE


.. autoattribute:: geosoft.gxapi.DU_IMPORT_MERGE


.. autoattribute:: geosoft.gxapi.DU_IMPORT_MERGE_APPEND


.. _DU_INTERP:

DU_INTERP constants
-----------------------------------------------------------------------

::

   Inside Interpolation Method 

.. autoattribute:: geosoft.gxapi.DU_INTERP_NEAREST


.. autoattribute:: geosoft.gxapi.DU_INTERP_LINEAR


.. autoattribute:: geosoft.gxapi.DU_INTERP_CUBIC


.. autoattribute:: geosoft.gxapi.DU_INTERP_AKIMA


.. autoattribute:: geosoft.gxapi.DU_INTERP_PREDICT


.. _DU_INTERP_EDGE:

DU_INTERP_EDGE constants
-----------------------------------------------------------------------

::

   Edge Interpolation Method 

.. autoattribute:: geosoft.gxapi.DU_INTERP_EDGE_NONE


.. autoattribute:: geosoft.gxapi.DU_INTERP_EDGE_SAME


.. autoattribute:: geosoft.gxapi.DU_INTERP_EDGE_NEAREST


.. autoattribute:: geosoft.gxapi.DU_INTERP_EDGE_LINEAR


.. _DU_LAB_TYPE:

DU_LAB_TYPE constants
-----------------------------------------------------------------------

::

   File Types 

.. autoattribute:: geosoft.gxapi.DU_LAB_TYPE_FREE

::

   
   					The delimiter string identifies
   					characters to be used as delimiters.  Use C style escape
   					sequences to identify non-printable characters.  The
   					default delimiters for FREE format files are " \t,".
   				 

.. autoattribute:: geosoft.gxapi.DU_LAB_TYPE_COMMA

::

   
   					For COMMA type files, the delimiter string identifies
   					characters to be removed before comma delimiting.  The
   					default for COMMA delimited files is " \t".
   				 

.. _DU_LEVEL:

DU_LEVEL constants
-----------------------------------------------------------------------

::

   Leveling Options 

.. autoattribute:: geosoft.gxapi.DU_LEVEL_LINES

::

   extract line corrections 

.. autoattribute:: geosoft.gxapi.DU_LEVEL_TIES

::

   extract tie corrections 

.. autoattribute:: geosoft.gxapi.DU_LEVEL_ALL

::

   extract all corrections 

.. _DU_LINEOUT:

DU_LINEOUT constants
-----------------------------------------------------------------------

::

   Lineout Options (du.h) 

.. autoattribute:: geosoft.gxapi.DU_LINEOUT_SINGLE


.. autoattribute:: geosoft.gxapi.DU_LINEOUT_MULTIPLE


.. _DU_FEATURE_TYPE_OUTPUT:

DU_FEATURE_TYPE_OUTPUT constants
-----------------------------------------------------------------------

::

   Export to geodatabase feature type (du.h) 

.. autoattribute:: geosoft.gxapi.DU_FEATURE_TYPE_OUTPUT_POINT


.. autoattribute:: geosoft.gxapi.DU_FEATURE_TYPE_OUTPUT_LINE


.. _DU_GEODATABASE_EXPORT_TYPE:

DU_GEODATABASE_EXPORT_TYPE constants
-----------------------------------------------------------------------

::

   Export to geodatabase overwrite mode(du.h) 

.. autoattribute:: geosoft.gxapi.DU_GEODATABASE_EXPORT_TYPE_OVERWRITE_GEODATABASE


.. autoattribute:: geosoft.gxapi.DU_GEODATABASE_EXPORT_TYPE_OVERWRITE_FEATURECLASS


.. autoattribute:: geosoft.gxapi.DU_GEODATABASE_EXPORT_TYPE_APPEND


.. _DU_LINES:

DU_LINES constants
-----------------------------------------------------------------------

::

   Lines to display 

.. autoattribute:: geosoft.gxapi.DU_LINES_DISPLAYED


.. autoattribute:: geosoft.gxapi.DU_LINES_SELECTED


.. autoattribute:: geosoft.gxapi.DU_LINES_ALL


.. _DU_LOADLTB:

DU_LOADLTB constants
-----------------------------------------------------------------------

::

   Load table options 

.. autoattribute:: geosoft.gxapi.DU_LOADLTB_REPLACE


.. autoattribute:: geosoft.gxapi.DU_LOADLTB_APPEND


.. _DU_LOOKUP:

DU_LOOKUP constants
-----------------------------------------------------------------------

::

   Lookup Mode 

.. autoattribute:: geosoft.gxapi.DU_LOOKUP_EXACT

::

   
   					Requires an exact match in all indexes.
   					Results will dummy if Indexes are not found.
   				 

.. autoattribute:: geosoft.gxapi.DU_LOOKUP_NEAREST

::

   
   					Requires that the first index match exactly.
   					The nearest second index will be used for the finding
   					the lookup value.
   					The results will be dummy only if the first index
   					does not have a match.
   				 

.. autoattribute:: geosoft.gxapi.DU_LOOKUP_INTERPOLATE

::

   
   					The same as _NEAREST, except that the value will
   					be interpolated between the two nearest
   					framing values in the table.
   				 

.. autoattribute:: geosoft.gxapi.DU_LOOKUP_NEARESTCLOSE

::

   
   					Same as _NEAREST mode except that the target
   					value must be within the CLOSE distance to a
   					table value.
   					a) the primary index channel for single index
   					lookups;
   					b) the secondary index channel for
   					double index lookups.
   					Values not in data spacing are dummy.
   				 

.. autoattribute:: geosoft.gxapi.DU_LOOKUP_INTERPCLOSE

::

   
   					Same as _INTERPOLATE mode except that the target
   					value must be within the CLOSE distance to a
   					table value.
   					a) the primary index channel for single index
   					lookups;
   					b) the secondary index channel for
   					double index lookups.
   					Values not in data spacing are dummy.
   				 

.. autoattribute:: geosoft.gxapi.DU_LOOKUP_INTERPOLATE_DUMMYOUTSIDE

::

   Interpolate between values, dummy beyond two ends 

.. autoattribute:: geosoft.gxapi.DU_LOOKUP_INTERPOLATE_CONSTOUTSIDE

::

   Interpolate between values, constant end values beyond two ends 

.. autoattribute:: geosoft.gxapi.DU_LOOKUP_INTERPOLATE_EXTPLOUTSIDE

::

   Interpolate between values, extrapolate beyond two ends 

.. autoattribute:: geosoft.gxapi.DU_LOOKUP_MAXOPTION

::

   Maximum option value 

.. _DU_MASK:

DU_MASK constants
-----------------------------------------------------------------------

::

   Masking Options 

.. autoattribute:: geosoft.gxapi.DU_MASK_INSIDE


.. autoattribute:: geosoft.gxapi.DU_MASK_OUTSIDE


.. _DU_MERGE:

DU_MERGE constants
-----------------------------------------------------------------------

::

   Merge flags 

.. autoattribute:: geosoft.gxapi.DU_MERGE_APPEND


.. _DU_MODFID:

DU_MODFID constants
-----------------------------------------------------------------------

::

   Fid Update Options 

.. autoattribute:: geosoft.gxapi.DU_MODFID_INSERT

::

   
   					Will insert fid range by moving data.  Inserted
   					range will always be dummied out.  If the insertion point
   					is before start of data, the fid start is changed.
   				 

.. autoattribute:: geosoft.gxapi.DU_MODFID_DELETE

::

   Will delete the range of fids. 

.. autoattribute:: geosoft.gxapi.DU_MODFID_APPEND

::

   
   					Is like INSERT, except that it is only used to
   					add fids to the start or end of the existing data.  The
   					data is not moved with repect to the current fid locations.
   				 

.. _DU_MOVE:

DU_MOVE constants
-----------------------------------------------------------------------

::

   Move Style 

.. autoattribute:: geosoft.gxapi.DU_MOVE_ABSOLUTE

::

   move input to absolute value in control channel 

.. autoattribute:: geosoft.gxapi.DU_MOVE_MINUS

::

   subtract control channel from input channel 

.. autoattribute:: geosoft.gxapi.DU_MOVE_PLUS

::

   add control channel to input channel 

.. autoattribute:: geosoft.gxapi.DU_MOVE_INTERP

::

   
   					data is NOT moved, but dummies in the input are interpolated
   					based on the control channel, assuming both the input and control
   					vary linearly inside the gaps
   				 

.. _DU_REFID:

DU_REFID constants
-----------------------------------------------------------------------

::

   Interpolation mode 

.. autoattribute:: geosoft.gxapi.DU_REFID_LINEAR

::

   0 

.. autoattribute:: geosoft.gxapi.DU_REFID_MINCUR

::

   1 

.. autoattribute:: geosoft.gxapi.DU_REFID_AKIMA

::

   2 

.. autoattribute:: geosoft.gxapi.DU_REFID_NEAREST

::

   3 

.. _DU_SORT:

DU_SORT constants
-----------------------------------------------------------------------

::

   Sort Direction 

.. autoattribute:: geosoft.gxapi.DU_SORT_ASCENDING


.. autoattribute:: geosoft.gxapi.DU_SORT_DESCENDING


.. _DU_SPLITLINE:

DU_SPLITLINE constants
-----------------------------------------------------------------------

::

   Sort Direction 

.. autoattribute:: geosoft.gxapi.DU_SPLITLINE_XYPOSITION


.. autoattribute:: geosoft.gxapi.DU_SPLITLINE_SEQUENTIAL


.. autoattribute:: geosoft.gxapi.DU_SPLITLINE_TOVERSIONS


.. _DU_STORAGE:

DU_STORAGE constants
-----------------------------------------------------------------------

::

   Storage Type 

.. autoattribute:: geosoft.gxapi.DU_STORAGE_LINE


.. autoattribute:: geosoft.gxapi.DU_STORAGE_GROUP


.. _QC_PLAN_TYPE:

QC_PLAN_TYPE constants
-----------------------------------------------------------------------

::

   Type Plan 

.. autoattribute:: geosoft.gxapi.QC_PLAN_SURVEYLINE


.. autoattribute:: geosoft.gxapi.QC_PLAN_TIELINE


.. autoattribute:: geosoft.gxapi.QC_PLAN_BOTHLINES


.. _DU_DISTANCE_CHANNEL_TYPE:

DU_DISTANCE_CHANNEL_TYPE constants
-----------------------------------------------------------------------

::

   Distance channel direction type 

.. autoattribute:: geosoft.gxapi.DU_DISTANCE_CHANNEL_MAINTAIN_DIRECTION

::

   Zero distance is always at the start of the line. 

.. autoattribute:: geosoft.gxapi.DU_DISTANCE_CHANNEL_CARTESIAN_COORDINATES

::

   Put zero at the end of the line with min X if X changes most, or min Y if Y changes most 

.. _DU_DIRECTGRID_METHOD:

DU_DIRECTGRID_METHOD constants
-----------------------------------------------------------------------

::

   How to calculate the cell values for direct gridding. 

.. autoattribute:: geosoft.gxapi.DU_DIRECTGRID_MIN


.. autoattribute:: geosoft.gxapi.DU_DIRECTGRID_MAX


.. autoattribute:: geosoft.gxapi.DU_DIRECTGRID_MEAN


	