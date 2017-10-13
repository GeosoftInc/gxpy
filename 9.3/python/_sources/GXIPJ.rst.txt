
.. _GXIPJ:

 
GXIPJ class
==================================

.. autoclass:: geosoft.gxapi.GXIPJ
   :members:

.. _IPJ_3D_FLAG:

IPJ_3D_FLAG constants
-----------------------------------------------------------------------

::

   3D Flags 

.. autoattribute:: geosoft.gxapi.IPJ_3D_FLAG_NONE

::

   Standard 

.. autoattribute:: geosoft.gxapi.IPJ_3D_FLAG_INVERTANGLES

::

   Invert angle rotation during matrix creation 

.. autoattribute:: geosoft.gxapi.IPJ_3D_FLAG_INVERTZ

::

   Invert the Z plane to make up down. 

.. autoattribute:: geosoft.gxapi.IPJ_3D_FLAG_ORDER_ROTATION

::

   Apply rotations in a specific order, determined by pdParm[7] 

.. _IPJ_3D_ROTATE:

IPJ_3D_ROTATE constants
-----------------------------------------------------------------------

::

   3D Rotation Mode 

.. autoattribute:: geosoft.gxapi.IPJ_3D_ROTATE_DEFAULT


.. autoattribute:: geosoft.gxapi.IPJ_3D_ROTATE_XYZ


.. autoattribute:: geosoft.gxapi.IPJ_3D_ROTATE_XZY


.. autoattribute:: geosoft.gxapi.IPJ_3D_ROTATE_YXZ


.. autoattribute:: geosoft.gxapi.IPJ_3D_ROTATE_YZX


.. autoattribute:: geosoft.gxapi.IPJ_3D_ROTATE_ZXY


.. autoattribute:: geosoft.gxapi.IPJ_3D_ROTATE_ZYX


.. _IPJ_CSP:

IPJ_CSP constants
-----------------------------------------------------------------------

::

   Projection Setting 

.. autoattribute:: geosoft.gxapi.IPJ_CSP_SCALE


.. autoattribute:: geosoft.gxapi.IPJ_CSP_FALSEEAST


.. autoattribute:: geosoft.gxapi.IPJ_CSP_FALSENORTH


.. autoattribute:: geosoft.gxapi.IPJ_CSP_LATORIGIN


.. autoattribute:: geosoft.gxapi.IPJ_CSP_LONORIGIN


.. autoattribute:: geosoft.gxapi.IPJ_CSP_PARALLEL_1


.. autoattribute:: geosoft.gxapi.IPJ_CSP_PARALLEL_2


.. autoattribute:: geosoft.gxapi.IPJ_CSP_AZIMUTH


.. autoattribute:: geosoft.gxapi.IPJ_CSP_ANGLE


.. autoattribute:: geosoft.gxapi.IPJ_CSP_POINTLAT_1


.. autoattribute:: geosoft.gxapi.IPJ_CSP_POINTLON_1


.. autoattribute:: geosoft.gxapi.IPJ_CSP_POINTLAT_2


.. autoattribute:: geosoft.gxapi.IPJ_CSP_POINTLON_2


.. _IPJ_NAME:

IPJ_NAME constants
-----------------------------------------------------------------------

::

   Project Name 

.. autoattribute:: geosoft.gxapi.IPJ_NAME_PCS

::

   Projected coordinate system name 

.. autoattribute:: geosoft.gxapi.IPJ_NAME_PROJECTION

::

   Projection name 

.. autoattribute:: geosoft.gxapi.IPJ_NAME_METHOD

::

   Projection method name 

.. autoattribute:: geosoft.gxapi.IPJ_NAME_DATUM

::

   Datum name 

.. autoattribute:: geosoft.gxapi.IPJ_NAME_ELLIPSOID

::

   Ellipsoid name 

.. autoattribute:: geosoft.gxapi.IPJ_NAME_LDATUM

::

   Local datum name 

.. autoattribute:: geosoft.gxapi.IPJ_NAME_UNIT_ABBR

::

   Unit abbreviation 

.. autoattribute:: geosoft.gxapi.IPJ_NAME_UNIT_FULL

::

   Full unit name 

.. autoattribute:: geosoft.gxapi.IPJ_NAME_TYPE

::

   Projection type description 

.. autoattribute:: geosoft.gxapi.IPJ_NAME_LLDATUM

::

   Datum transform table name 

.. autoattribute:: geosoft.gxapi.IPJ_NAME_METHOD_PARMS

::

   Projection method parameters in GXF order 

.. autoattribute:: geosoft.gxapi.IPJ_NAME_METHOD_LABEL

::

   Projection method parameters labels 

.. autoattribute:: geosoft.gxapi.IPJ_NAME_DATUM_PARMS

::

   Datum parameters (major axis, flattening, prime meridian) 

.. autoattribute:: geosoft.gxapi.IPJ_NAME_LDATUM_PARMS

::

   
   					local datum parameters (dX,dY,dZ,rX,rY,rZ,scale)
   					See GXF revision 3 for parameter list order and
   					specifications.
   				 

.. autoattribute:: geosoft.gxapi.IPJ_NAME_GEOID

::

   Geoid name if known 

.. autoattribute:: geosoft.gxapi.IPJ_NAME_LDATUMDESCRIPTION

::

   Local datum description 

.. autoattribute:: geosoft.gxapi.IPJ_NAME_METHOD_PARMS_NATIVE

::

   Projection method parameters in GXF order (Native units for eastings/northings) 

.. autoattribute:: geosoft.gxapi.IPJ_NAME_ORIENTATION_PARMS

::

   Orientation parameters 

.. _IPJ_ORIENT:

IPJ_ORIENT constants
-----------------------------------------------------------------------

::

   Projection Orientation 

.. autoattribute:: geosoft.gxapi.IPJ_ORIENT_DEFAULT

::

   
   					no special orientation - plan view. All views in maps
   					created before v5.1.3 will return this value.
   				 

.. autoattribute:: geosoft.gxapi.IPJ_ORIENT_PLAN

::

   
   					A plan view with a reference elevation and
   					optional rotation.
   				 

.. autoattribute:: geosoft.gxapi.IPJ_ORIENT_SECTION

::

   
   					Has an azimuth and swing.
   					The section view projects all plotted objects
   					HORIZONTALLY onto the viewing plan in order to
   					preserve elevations, even if the section has a swing.
   				 

.. autoattribute:: geosoft.gxapi.IPJ_ORIENT_SECTION_NORMAL

::

   
   					Same as IPJ_ORIENT_SECTION, but the projection is perpendicular
   					to the section, not horizonatl, so elevatins are not preserved
   					on swung sections.
   				 

.. autoattribute:: geosoft.gxapi.IPJ_ORIENT_DEPTH_SECTION

::

   
   					This simple section has no azimuth or swing defined;
   					only the depth is of importance, and it is output as
   					the Y parameter, increasing downward. Used (for instance)
   					for strip logs in Wholeplot.
   				 

.. autoattribute:: geosoft.gxapi.IPJ_ORIENT_3D

::

   A 3D rotation/scaling/translation orientation 

.. autoattribute:: geosoft.gxapi.IPJ_ORIENT_3D_MATRIX

::

   A 3D matrix orientation 

.. autoattribute:: geosoft.gxapi.IPJ_ORIENT_SECTION_CROOKED

::

   
   					This is a vertical section that follows a
   					curving path, like a river or survey traverse.
   					The horizontal section location is the distance along
   					the path, while the vertical axis gives the elevation.
   				 

.. _IPJ_PARM_LST:

IPJ_PARM_LST constants
-----------------------------------------------------------------------

::

   Projection List 

.. autoattribute:: geosoft.gxapi.IPJ_PARM_LST_COORDINATESYSTEM


.. autoattribute:: geosoft.gxapi.IPJ_PARM_LST_DATUM


.. autoattribute:: geosoft.gxapi.IPJ_PARM_LST_PROJECTION


.. autoattribute:: geosoft.gxapi.IPJ_PARM_LST_UNITS


.. autoattribute:: geosoft.gxapi.IPJ_PARM_LST_LOCALDATUMDESCRIPTION


.. autoattribute:: geosoft.gxapi.IPJ_PARM_LST_LOCALDATUMNAME


.. autoattribute:: geosoft.gxapi.IPJ_PARM_LST_UNITSDESCRIPTION


.. _IPJ_TYPE:

IPJ_TYPE constants
-----------------------------------------------------------------------

::

   IPJ Types 

.. autoattribute:: geosoft.gxapi.IPJ_TYPE_PRJ

::

   
   					Read from a PRJ file:
   					string 1 - Source file name
   					string 2 and 3 are not used.
   				 

.. autoattribute:: geosoft.gxapi.IPJ_TYPE_PCS

::

   
   					Projected coordinate system:
   					string 1 - POSC PCS name
   					string 2 - POSC Datum transform name
   					string 3 - not used.
   				 

.. autoattribute:: geosoft.gxapi.IPJ_TYPE_GCS

::

   
   					Geographic coordinate system:
   					string 1 - POSC Datum name
   					string 2 - POSC Datum transform name
   					string 3 - not used.
   				 

.. autoattribute:: geosoft.gxapi.IPJ_TYPE_ANY

::

   
   					Custom projection
   					string 1 - POSC Datum name
   					string 2 - POSC Datum transform name
   					string 3 - POSC Transform, "" if geographic
   				 

.. autoattribute:: geosoft.gxapi.IPJ_TYPE_NONE

::

   
   					Not used for \ :func:`geosoft.gxapi.GXIPJ.read`\ .  This is used for
   					\ :func:`geosoft.gxapi.GXIPJ.source_type`\  to indicate no projection.
   				 

.. autoattribute:: geosoft.gxapi.IPJ_TYPE_WRP


.. autoattribute:: geosoft.gxapi.IPJ_TYPE_TEST

::

   
   					tests the projection tables for internal consistency
   					and creates report files in the project directory.
   					string 1 - outout report file name
   					string 2 - ESRI coordinate strings file.  This contains one
   					ESRI coordinate string per line.  Lines that
   					start with '#' are skipped.
   					string 3 - not currently used
   				 

.. _IPJ_UNIT:

IPJ_UNIT constants
-----------------------------------------------------------------------

::

   Projection Unit Type 

.. autoattribute:: geosoft.gxapi.IPJ_UNIT_ABBREVIATION


.. autoattribute:: geosoft.gxapi.IPJ_UNIT_FULLNAME


.. _IPJ_WARP:

IPJ_WARP constants
-----------------------------------------------------------------------

::

   Warp (Transformation) type 

.. autoattribute:: geosoft.gxapi.IPJ_WARP_MATRIX

::

   Matrix Warp 

.. autoattribute:: geosoft.gxapi.IPJ_WARP_NONE

::

   No warp 

.. autoattribute:: geosoft.gxapi.IPJ_WARP_TRANS1

::

   Translate only (needs 1 point) 

.. autoattribute:: geosoft.gxapi.IPJ_WARP_TRANS2

::

   Translate, rotate, normal scale (needs 2 pts) 

.. autoattribute:: geosoft.gxapi.IPJ_WARP_TRANS3

::

   Translate, rotate, scale X and Y (needs 3 pts or more, least-square fit) 

.. autoattribute:: geosoft.gxapi.IPJ_WARP_QUAD

::

   Quadrilateral warp (needs 4 points) 

.. autoattribute:: geosoft.gxapi.IPJ_WARP_MULTIPOINT

::

   Multipoint warp (needs at least 3 points) 

.. autoattribute:: geosoft.gxapi.IPJ_WARP_LOG

::

   Convert from linear to log coords in X and/or Y 

.. autoattribute:: geosoft.gxapi.IPJ_WARP_MULTIPOINT_Y

::

   Multipoint warp in Y only (needs at least 3 points) 

	